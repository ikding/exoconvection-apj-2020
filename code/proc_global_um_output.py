#!/usr/bin/env python
# coding: utf-8
"""Process global UM output by interpolating selected fields to common grid."""

# Commonly used standard library tools
import argparse
from pathlib import Path
from time import time
import re
import warnings

import iris

# My packages and local scripts
from aeolus.coord_utils import (
    regrid_3d,
    replace_z_coord,
    ensure_bounds,
    UM_HGT,
)
from aeolus.core import Run
from aeolus.grid import roll_cube_pm180
from aeolus.subset import CM_MEAN_CONSTR

from commons import GLM_FILE_REGEX, GLM_MODEL_TIMESTEP, GLM_RUNID, GLM_START_DAY
import mypaths
from utils import create_logger


# Global definitions and styles
warnings.filterwarnings("ignore")
SCRIPT = Path(__file__).name

# Selected variables
SINGLE_LEVEL_VARS = [
    "surface_temperature",
    "toa_incoming_shortwave_flux",
    "toa_outgoing_longwave_flux",
    "toa_outgoing_longwave_flux_assuming_clear_sky",
    "toa_outgoing_shortwave_flux",
    "toa_outgoing_shortwave_flux_assuming_clear_sky",
    "surface_downwelling_shortwave_flux_in_air",
    "upwelling_shortwave_flux_in_air",
    "surface_downwelling_longwave_flux_in_air",
    "upwelling_longwave_flux_in_air",
    "surface_upward_sensible_heat_flux",
    "surface_upward_latent_heat_flux",
    "convective_rainfall_flux",
    "convective_snowfall_flux",
    "high_type_cloud_area_fraction",
    "low_type_cloud_area_fraction",
    "medium_type_cloud_area_fraction",
    "stratiform_rainfall_flux",
    "stratiform_snowfall_flux",
]
MULTI_LEVEL_VARS = [
    "air_potential_temperature",
    "air_pressure",
    "specific_humidity",
    "mass_fraction_of_cloud_liquid_water_in_air",
    "mass_fraction_of_cloud_ice_in_air",
    "upward_air_velocity",
]
HORIZ_WINDS_CONSTR = ["x_wind", "y_wind"]
INCR_CONSTR = iris.AttributeConstraint(STASH=lambda x: x.item in [181, 182, 233])


def parse_args(args=None):
    """Argument parser."""
    ap = argparse.ArgumentParser(
        SCRIPT,
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    ap.add_argument(
        "-p", "--planet", type=str, required=True, help="Planet configuration"
    )
    ap.add_argument("-r", "--run", type=str, required=True, help="Run key")
    ap.add_argument(
        "-s",
        "--startday",
        type=int,
        default=GLM_START_DAY,
        help="Load files with timestamp >= this",
    )

    return ap.parse_args(args)


def process_cubes(
    cubelist, timestep=GLM_MODEL_TIMESTEP, ref_cube_constr="specific_humidity"
):
    """Post-process data for easier analysis."""
    cubes = iris.cube.CubeList()

    # First, extract all multi-level fields (30-day averages)
    cubes += cubelist.extract(MULTI_LEVEL_VARS).extract(CM_MEAN_CONSTR)

    # Horizontal wind components
    for cube in cubelist.extract(HORIZ_WINDS_CONSTR):
        cube.units = "m s^-1"
        cubes.append(cube)

    # Increments
    for cube in cubelist.extract(INCR_CONSTR):
        if cube.attributes["STASH"].item in [181, 233]:
            incr_unit = "K"
        else:
            incr_unit = "kg kg^-1"
        if cube.attributes["STASH"].item == 233:
            cube.units = f"{incr_unit} s^-1"
        else:
            cube.units = f"{1/timestep} {incr_unit} s^-1"
            cube.convert_units(f"{incr_unit} s^-1")
        cubes.append(cube)

    # Interpolation & regridding to common grid
    ref_cube = cubes.extract_strict(ref_cube_constr)
    ref_cube = replace_z_coord(ref_cube, UM_HGT)

    # Interpolate to common levels
    cubes = iris.cube.CubeList(
        [regrid_3d(replace_z_coord(cube, UM_HGT), ref_cube, UM_HGT) for cube in cubes]
    )

    # Add all single-level cubes
    cubes += cubelist.extract(SINGLE_LEVEL_VARS).extract(CM_MEAN_CONSTR)

    # Roll cubes to +/- 180 degrees in longitude for easier analysis
    r_cubes = iris.cube.CubeList()
    for cube in cubes:
        r_c = roll_cube_pm180(cube)
        ensure_bounds(r_c)
        r_cubes.append(r_c)

    return r_cubes


def get_filename_list(
    path_to_dir,
    glob_pattern=f"{GLM_RUNID}*",
    ts_start=0,
    regex=GLM_FILE_REGEX,
    regex_key="timestamp",
):
    """Get a list of files with timestamps greater or equal than start in a directory."""
    fnames = []
    for fpath in sorted(path_to_dir.glob(glob_pattern)):
        match = re.match(regex, fpath.name)
        if match:
            if int(match[regex_key]) >= ts_start:
                fnames.append(fpath)
    return fnames


def main(args=None):
    """Main entry point of the script."""
    # Parse command-line arguments
    args = parse_args(args)
    planet = args.planet
    run_key = args.run

    label = f"{planet}_{run_key}"
    L.info(f"label = {label}")

    # Create a subdirectory for processed data
    outdir = mypaths.sadir / label / "_processed"
    outdir.mkdir(parents=True, exist_ok=True)

    # Make a list of files matching the file mask and the start day threshold
    fnames = get_filename_list(mypaths.sadir / label, ts_start=args.startday)
    L.debug(f"fnames = {fnames[0]} ... {fnames[-1]}")

    # Initialise a `Run` by loading data from the selected files
    run = Run(files=fnames, name=label, planet=planet, timestep=GLM_MODEL_TIMESTEP)

    # Regrid & interpolate data
    run.proc_data(process_cubes, timestep=run.timestep)

    # Write the data to a netCDF file
    fname_out = outdir / f"{run.name}.nc"
    run.to_netcdf(fname_out)
    L.success(f"Saved to {fname_out}")


if __name__ == "__main__":
    t0 = time()
    L = create_logger(Path(__file__))
    main()
    L.info(f"Execution time: {time() - t0:.1f}s")
