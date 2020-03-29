# Atmospheric convection plays a key role in the climate of tidally-locked terrestrial exoplanets: insights from high-resolution simulations
**Denis E. Sergeev, F. Hugo Lambert, Nathan J. Mayne, Ian Boutle, James Manners, and Krisztian Kohary**

**2020**

**Submitted to *Astrophysical Journal***

Code used to process and visualise the model output.
Model data are available upon request (raw data O(100 Gb)).

Notebooks for each individual figure as well as for two data tables are in the [`code/` directory](code), while the figures themselves are in the `plots/` directory.

### Figures
|  #  | Figure                                                                                                                                                                                                    | Notebook                                                                              | Dependencies                                                                                                                                                             |
|:---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | [Overview of the model set-up for the Trappist-1e case (interactive 3D Figure)](plots/trap1e_grcs_110d_view3d__enlarged.png)                                                                              | [Fig01-Model-Set-Up-3D.ipynb](code/Fig01-Model-Set-Up-3D.ipynb)                       | [pp_ns_data.py](code/pp_ns_data.py)                                                                                                                                      |
|  2 | [Surface temperature and horizontal wind vectors in the upper troposphere](plots/trap1e_proxb__grcs_llcs_all_rain_acoff__tsfc_winds__plev250hpa.pdf)                                                      | [Fig02-Map-Sfc-Temp-Winds.ipynb](code/Fig02-Map-Sfc-Temp-Winds.ipynb)                 | [pp_main_gl_data.py](code/pp_main_gl_data.py)                                                                                                                            |
|  3 | [Time average vertical profiles of temperature and water vapor at the sub-stellar point and its antipode](plots/trap1e_proxb__grcs_llcs_all_rain_acoff__vprof_daynight_pm01deg__temp_shum)                | [Fig03-Vert-Prof-Temp-Hum.ipynb](code/Fig03-Vert-Prof-Temp-Hum.ipynb)                 | [pp_main_gl_data.py](code/pp_main_gl_data.py)                                                                                                                            |
|  4 | [Eddy geopotential height and eddy components of horizontal wind vectors 250 hPa and air temperature at 700 hPa](plots/trap1e_proxb__grcs_llcs_all_rain_acoff__ghgt_winds_eddy__250hpa__temp__700hpa.pdf) | [Fig04-Map-Gpt-Hgt-Temp.ipynb](code/Fig04-Map-Gpt-Hgt-Temp.ipynb)                     | [pp_main_gl_data.py](code/pp_main_gl_data.py)                                                                                                                            |
|  5 | [Atmospheric circulation regimes](plots/trap1e_proxb__grcs_llcs_all_rain_acoff__nondim_rossby_rhines__hgt0-15km.pdf)                                                                                      | [Fig05-Rossby-Rhines.ipynb](code/Fig05-Rossby-Rhines.ipynb)                           | [pp_main_gl_data.py](code/pp_main_gl_data.py)                                                                                                                            |
|  6 | [Distribution of clouds and precipitation for the Trappist-1e and Proxima b cases](plots/trap1e_proxb__grcs_llcs_all_rain_acoff__cloud_types__w_precip.pdf)                                               | [Fig06-Map-Cloud-Precip.ipynb](code/Fig06-Map-Cloud-Precip.ipynb)                     | [pp_main_gl_data.py](code/pp_main_gl_data.py)                                                                                                                            |
|  7 | [Meridional average of vertically integrated divergence of MSE and its components](plots/trap1e_proxb__grcs_llcs_all_rain_acoff__mse_div_merid_mean.pdf)                                                  | [Fig07-MSE-Flux-Divergence.ipynb](code/Fig07-MSE-Flux-Divergence.ipynb)               | [pp_main_gl_data.py](code/pp_main_gl_data.py)                                                                                                                            |
|  8 | [Latitudinal cross-section of the zonal transport of sensible and latent heat across the eastern terminator](plots/trap1e_proxb__grcs_llcs_all_rain_acoff__vcross_lon90E__hgt0-16__zonal_fluxes.pdf)      | [Fig08-Vert-Cross-Heat-Flux.ipynb](code/Fig08-Vert-Cross-Heat-Flux.ipynb)             | [pp_main_gl_data.py](code/pp_main_gl_data.py)                                                                                                                            |
|  9 | [Snapshot of top-of-atmosphere outgoing longwave radiation in the Trappist-1e simulation](plots/trap1e__grcs__toa_olr_map__102d.pdf)                                                                      | [Fig09-Map-TOA-OLR-Trap1e.ipynb](code/Fig09-Map-TOA-OLR-Trap1e.ipynb)                 |                                                                                                                                                                          |
| 10 | [Snapshot of top-of-atmosphere outgoing longwave radiation in the Proxima b simulation](plots/proxb__grcs__toa_olr_map__100d.pdf)                                                                         | [Fig10-Map-TOA-OLR-Proxb.ipynb](code/Fig10-Map-TOA-OLR-Proxb.ipynb)                   |                                                                                                                                                                          |
| 11 | [Histograms of instantaneous TOA OLR values in the substellar region](plots/trap1e_proxb__grcs__toa_olr_hist.pdf)                                                                                         | [Fig11-Hist-TOA-OLR.ipynb](code/Fig11-Hist-TOA-OLR.ipynb)                             |                                                                                                                                                                          |
| 12 | [Snapshot of convection in the substellar region in the Proxima b case at the end of the HighRes simulation](plots/proxb__grcs__precip_w_map.pdf)                                                         | [Fig12-Map-Precip-Vert-Wind.ipynb](code/Fig12-Map-Precip-Vert-Wind.ipynb)             |                                                                                                                                                                          |
| 13 | [Vertical profiles of the cloud liquid water and ice mixing ratio in the substellar region](plots/trap1e_proxb__grcs__vprof_qcl_qcf.pdf)                                                                  | [Fig13-Vert-Prof-Cloud-Condensate.ipynb](code/Fig13-Vert-Prof-Cloud-Condensate.ipynb) | [pp_ns_data.py](code/pp_ns_data.py), [ns_mean_vprof.py](code/ns_mean_vprof.py)                                                                                           |
| 14 | [Vertical profiles of temperature increments due to the latent heating in the substellar region](plots/trap1e_proxb__grcs__vprof_t_incr_lh.pdf)                                                           | [Fig14-Vert-Prof-Latent-Heating.ipynb](code/Fig14-Vert-Prof-Latent-Heating.ipynb)     | [pp_ns_data.py](code/pp_ns_data.py), [ns_mean_vprof.py](code/ns_mean_vprof.py)                                                                                           |
| 15 | [Day-night surface temperature difference vs wind divergence in the free troposphere of the substellar region](plots/trap1e_proxb__grcs__scatter_w_linreg__hdiv_5_20km_ss__t_sfc_diff_dn.pdf)             | [Fig15-Day-Night-Impact-Lin-Reg.ipynb](code/Fig15-Day-Night-Impact-Lin-Reg.ipynb)     | [pp_ens_gl_data.py](code/pp_ens_gl_data.py), [aggr_ens_output.py](code/aggr_ens_output.py), [pp_ns_data.py](code/pp_ns_data.py), [aggr_ns_data.py](code/aggr_ns_data.py) |

### Tables
| #  | Figure                                                                                               | Notebook                                                    | Dependencies                                  |
|---:|:-----------------------------------------------------------------------------------------------------|:------------------------------------------------------------|:----------------------------------------------|
| 3 | Mean global, day-side, and night-side surface temperature in the control and sensitivity simulations | [Tab03-Mean-Sfc-Temp.ipynb](code/Tab03-Mean-Sfc-Temp.ipynb) | [pp_main_gl_data.py](code/pp_main_gl_data.py) |
| 4 | Global top-of-atmosphere cloud radiative effect in the control and sensitivity simulations           | [Tab04-CRE.ipynb](code/Tab04-CRE.ipynb)                     | [pp_main_gl_data.py](code/pp_main_gl_data.py) |


`page/` directory is for hosting an HTML page with an [interactive version of Fig. 1](https://dennissergeev.github.io/exoconvection-apj-2020).
