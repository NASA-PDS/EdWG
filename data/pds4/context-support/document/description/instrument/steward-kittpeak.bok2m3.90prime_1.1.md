There are four CCDs each with 4032 columns x 4096 rows physical pixels and 20 pixels
of overscan for each amp.
Each CCD is read out from 4 amplifiers located in each corner
Each single amplifier image extension contains data from one amplifier, so it has
2016+20=2032 columns and 2048 rows
Current system gain is defined in the image header, and is about 1.5 electrons/DN
(Data Numbers)
Dark current is ~7 electrons/pixel/hour.
Full well is ~90,000 electrons or about the 65k DN ADC 16-bit ADC limit.
The CCDs are linear to 65k DN, but stay below about 60,000 DN to be safe.
Noise is about 7-8 electrons in the active imaging area in most channels. A few less
well behaved channels sometimes measure around 11 electrons.
Readout time plus file creating time is 35 seconds.
The operating temperature is about -135 C.