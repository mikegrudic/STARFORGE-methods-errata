# Erratum for the STARFORGE methods paper (Grudic et al 2021)


[![DOI](https://zenodo.org/badge/1095186557.svg)](https://doi.org/10.5281/zenodo.17596225)

Here you will find materials associated with an erratum for the [STARFORGE simulation methods paper](https://academic.oup.com/mnras/article/506/2/2199/6276745), in which we explain the correction to our original incorrect dust opacity model. `planck_mean.py` generates all figures and tables, and `planck_mean_opacity.dat` and `rosseland_mean_opacity.dat` tabulate mean opacities for the Semenov 2003 porous 5-layered sphere model.

## Caveats
* (thanks to Ari Laor) The opacity tables computed here are for the Semenov 2003 model, which is very much targeted at modeling protoplanetary disks, and chose a dust composition appropriate for those conditions following Pollack 1994. Notably, the model does not contain graphite grains, and thus it is not expected to extrapolate well to the diffuse ISM at the shorter wavelengths where those grains dominate the opacity - see [Baskin & Loar 2018 Fig. 6](https://ui.adsabs.harvard.edu/abs/2018MNRAS.474.1970B). 
