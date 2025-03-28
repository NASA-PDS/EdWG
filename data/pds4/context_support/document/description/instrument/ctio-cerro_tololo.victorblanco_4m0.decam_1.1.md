The information was copied from various NOIRLab websites on October 31, 2023. DECam
is a high-performance, wide-field CCD imager mounted at the prime focus of the Víctor
M. Blanco 4-meter Telescope at Cerro Tololo Inter-American Observatory, with 62
science CCDs (60.5 useful) with 520 megapixels and images 3 square degrees (2.2
degree wide) field at 0.263 arcsecond/pixel resolution. DECam is a facility
instrument, available to all users. DECam was built to carry out the Dark Energy
Survey (DES) Project by the DES Collaboration, which finished observations in January
2019. Main Characteristics of Focal Plane
-------------------------------------------- Field of View 3 square degree (2.2
degree field of view) Pixel scale 0.2637 arcsec/pixel (center), 0.2626 arcsec/pixel
(edge) Detector 62, 2048x4096 pixel red-sensitive science CCDs from LBNL, 520
megapixels total (570 Mpix including guide and focus CCDs) Read-out noise 7e-
Read-out time 20 seconds Dark-current ~ QE 40% at 400 nm, 70% at 520 nm, then around
90% until 920 nm, falling to 40% at 1000 nm, 10% at 1050 nm Dynamical range 16 bit
Inter-CCD Gaps 3.0 mm (201 pixels) along long edge (e.g., between S4 and N4); 2.3 mm
(153 pixels) along short edge (e.g., between N4 and N5) Cosmetics Good to excellent.
On average, each CCD has 0.05% bad pixels and the worst CCD has 0.39% bad pixels.
Filters 8 filters now available (ugrizY, wide VR, narrow N964) Gain 4 e-/ADU (typica)
Non linearity For normal observing, keep level below 100,000 e-, 22,000 ADU Raw data
format FITS (with extensions),1 GB/file, ~600 Mbyte/file compressed Instrument F
ratio f/2.7 Status of DECam CCDs ------------------------------ Nov. 16, 2018
(original), updated April 10 2019 and February 13 2020 (ARW). The following is a
report on the current status of DECam CCDs that have presented problems in the past:
CCD 61 = N30 Fault: Very low full well following an over-illumination event in
November 2012. Comment: This CCD is normally masked out in reduction pipelines. This
failure prompted extra â€œno bright lightâ€ operations procedures for DECam,
observations closer to 10 deg from the Moon are prevented, and we added extra
protection photodiodes to supplement those already on the FPA. CCD 31 = S7 Fault:
Amplifier B has unstable gain, from installation September 2012. Comment: Generally
the whole CCD is masked out in reduction pipelines. However Amplifier A does function
correctly. CCD 2 = S30 Fault: Stopped working November 2013, restarted 29 Dec 2016.
Comment: It is postulated without any proof that a piece of electrically conducting
debris within the Imager fell on exposed serial clock lines for this CCD, and then
after three years fell off again. There are reports that the amplifier(s) are
unstable at the 0.3% level so caveat emptor for critical work. CCD 46 = N15 Fault:
Hot spot started 10 Nov 2017, intermittent, not seen since January 2018. Comment: The
hot spot was a charge defect and did not generate light. Generally hot spots are
associated with a pixel-level defect, e.g. a short in the gate structure, and are not
intermittent nor do they heal themselves. So there is no explanation for why this
very prominent defect disappeared, with the affected pixel (800, 2630) now looking
completely normal. CCD 41 = N10 Fault: Poor serial charge transfer on amp B, started
31 August 2018, intermittent, most recent incident 20 October 2018 Comment: This was
diagnosed as a fault associated with a single serial clock line (H3). All relevant
external hardware (clock card, transition card, cables to VIB) has been changed, but
the fault kept reappearing. It was discovered that a script which toggles vsub for
all CCDs, and disables/enables the clock lines for the associated backplane (#5, 18
CCDs), fixes the fault. This could be understood if it was clearing a latched driver.
CCD 44 = N13 Fault: From November 2018, appears to be a thread or similar stuck to
the surface of the detector near x=1133, y=1980. FN2 and FS4 Fault: Half of each of
these two F&A CCDs has low full well (10%). Comment: Diagnosed as damage to output
amplifier or signal chain inside the Imager. Since installation, September 2012. FN2
Fault: Has developed a super-hot pixel (~1645, 2096), since 9 April 2015 Comment:
This is on the very edge of the format.. It was previously known as a slightly hot
pixel, now it is very bright, clearly visible on bias exposures. General: Every time
the DECam CCDs are warmed up and cooled down again the conduction between the CCDs
and their mount can change very slightly, and with it the operating temperature for
the CCD relative to the average for all the others. This temperature change means
that the CCD response cutoff near 1.05 microns can change slightly (warmer CCD
implies redder cutoff), and this can be seen in the relative flat-field response
through the Y filter, which has detector-defined red cutoff. Such changes have been
seen now and then but they are always very small (no more than a 1% change in Y band
throughput), although a possible 2% change for CCD 27 = S3 as a result of the 2018
March warm/cool cycle is under investigation by DES. As expected, this is a Y-band
effect only. DECam Shutter -------------------- The DECam shutter is a large shutter
made by Bonn Shutter and consists of two accurately-controlled blades that sweep
across the focal plane, the first movement lets light to the focal plane, the second
closes off the light. The length of time it takes a shutter blade to sweep across the
focal plane is approximately one second. For any exposures longer than one second,
the movement of the two blades is sequential, but for shorter exposures the movement
of the two blades occurs simultaneously, and the two blades form a “slit” that sweeps
across the focal plane. Since the blades are accurately synchronized, very short
exposures (a few milliseconds} are possible. The longest exposures regularly taken,
through u band or narrowband filters normally do not exceed 1200 seconds although
there is no technical limitation to going longer. The number of cosmic ray events on
the CCDs starts getting obnoxious for long exposure times. There are several aspects
to be considered if doing short exposures of moving objects, or very rapid variables.
Firstly, the the blades move in the East-West direction. Blade “A” is on the west
side and Blade “B” is on the east side. So for an exposure assume Blade A covers the
focal plane. It then moves to the west position and so the exposure starts, then at
the end of the exposure Blade B moves from its east position to cover the focal
plane. The following exposure reverses the direction the blades move, and so on.
Unfortunately, which of the two situations (blades moving to the east or to the west)
applies to any given exposure is NOT written into the image header or to the SISPI
log. It is however in the low level PanView log. Since one only needs to know which
of the two situations you have for one “fiducial” exposure in a given night, that
information can easily be provided upon request. Secondly, the actual epoch at which
the shutter opens for a given CCD pixel depends on where that pixel is situated. The
time for the blade to sweep across the focal plan is approximately one second, so
this effect could be of importancce for short exposure times. Thirdly, the shutter is
sited, along with the filters, between corrector elements C3 and C4, a long way from
the focal plane. Photons falling on a given pixel are contained in a cone that is
some 20 cm diameter by the time it passes through the shutter. And finally, the
shutter control is not hardware-synced to the CCD readout. The complications that
might be relevant for short exposures of moving objects, or rapid variables, are
likely to be irrelevant for the great majority of DECam programs. The following
outstanding specifications mean that very few people need worry about any
shutter-related effects on their photometry, and indeed the shutter performance far
exceeds the DECam design specifications in all respects. Minimum recommended shutter
time: 100 msec (non-uniformity is then < 1% over the whole focal plane) Maximum
recommended shutter time: 1800 sec (but beware cosmic rays) Minimum allowed shutter
time: 10 msec Exposure time uniformity: < 1 msec Exposure time repeatability: <<
1msec Exposure time accuracy: << 1 msec Absolute timing: < 1 msec ( internal to the
shutter, but the external error in the absolute timing is very much larger due to
external connections) Note these specifications are those demonstrated at the factory
at time of acceptance in 2011. Most of these specifications we have no way of testing
to the required accuracy with DECam on the Blanco telescope.