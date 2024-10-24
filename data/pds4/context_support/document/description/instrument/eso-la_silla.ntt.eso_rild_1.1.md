The ESO Multi-Mode Instrument (EMMI) is a multipurpose instrument allowing
observations in thevisible wavelengths. EMMI supports wide-field imaging,
low-resolution multi-object or long-slit grism spectroscopy, medium-resolution
long-slit grating spectroscopy, and echelle spectroscopy, using various detector
modes.

The RILD mode, for low-dispersion spectroscopy, is described here.  Low-resolution
long-slit spectroscopy is done in the RILD mode by combining one of the grisms with
one of the fixed slits (starplates) and, if needed, an order-sorting filter. The
grisms cannot be rotated: the achievable wavelength range is fixed for each grism. 
Many grisms show a second order contamination, hence the use of an order sorting
filter is recommended.

There are six fixed slits available, with widths of 0.5, 1.0, 1.5, 2, 5 and 10 arsec,
and each with a length of 8'. The 0.5 arsec slit will cause undersampling of the
spectra, except when used in 1 x 1 binning mode, under exceptional seeing conditions.

The orientation of the slit can be adjusted by applying an offset to the rotation
angle of EMMI.

Grisms and filters can also be combined to obtain slitless spectra imaged on the CCD.
The use of filters in combination with a grism reduces the sky background intensity.
It also selects the wavelength region of interest and limits the length of the
spectrum, thus reducing crowding. The spectral coverage within this wavelength region
depends on the position of the object in the field.

The following table summarizes the Grisms available on EMMI and their
characteristics.

Grism g/mm Blaze Blaze  Eff.[a]  Dispersion[d]   Rs[b] Wavelength range
           angle lambda
           (deg) (nm)     (%)   (nm/mm) (A/pix)            (nm)
------------------------------------------------------------------------
1     150   8.6   560     79     24.5    3.68    263      385 - 1000 [c]
2     300  14.6   490     78     11.6    1.74    570      380 - 920 [c]
3     360  15.0   460     77      9.4    1.43    760      380 - 907 [c]
4     300  22.0   650     72     11.6    1.76    613      550 - 1000
5     600  34.0   530     66      5.5    0.83   1100      380 - 702
6     600  54.0   650     55      5.0    0.73   1490      575 - 867
7     150  10.8   720     80     24.0    3.62    280      490 - 1000 [c]

[a] Efficiency at blaze.
[b] Resolution with 1" slit at 600 nm (at central lambda for grisms 4,5 and 6) and
for binning 2
[c] Second overlap occurs beyond 800 nm if not using an order-sorting filter.
[d] Dispersion with 1 x 1 binning
        