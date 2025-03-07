
 
Instrument Overview
===================
 
The Framing Camera (FC) is a multispectral CCD imager in a refracting
telescope that also serves as optical navigation camera for the NASA Dawn
mission to the asteroids 4 Vesta and 1 Ceres. The camera consists of two
identical units, FC1 and FC2, which are mounted side-by-side on the +Z deck
of the spacecraft. The instrument uses a re-closable front door to protect
the optical system and commands eight filters in a wheel, one clear and
seven narrow-band. The instrument hardware and scientific objectives are
documented in [SIERKSETAL2011].
 
Scientific Objectives
=====================
 
The FC science objectives at Vesta and Ceres are to
 
- Determine the asteroid's origin and evolution
 
- Determine shape and volume
 
- Measure the spin rate and pole position
 
- Map the topography
 
- Map the basic mineralogical composition
 
- Determine the regolith properties through photometric analysis and search
for evidence of regolith transport
 
- Study crater morphology and distribution
 
- Age determination of the surfaces
 
- Search for fractures and evidence of volcanism
 
- Study the dust environment
 
- Search for moons and determine their properties
 
- Provide a context for the HED meteorites and enable identification of
possible meteorites from Ceres
 
To this end the FC images will be used to create global topography, albedo,
and color maps, determine the surface Bidirectional Reflectance Distribution
Function, and search for orbiting dust and moons. Through the radio science
experiment it will be possible to determine the gravity field and density of
the asteroids.
 
Calibration
===========
 
The FC has been calibrated using the results of laboratory and in-flight
measurements. The lab measurements were acquired at the Max Planck Institute
for Solar System Research (MPS), and were aimed at determining dark current
and the absolute photometric response in each of the filters. Flat fields
were acquired by imaging the inside of an integrating sphere. The in-flight
measurements, acquired during the Initial Check-Out campaign in the months
after launch, focused on characterizing the dark current and geometric
distortion (through observation of star fields), and validating the lab
radiometric calibration (photometric standard stars). The calibration
pipeline is described by [SCHROEDER&GUTIER2011].
 
Dark current, and the associated emergence of bad pixels, and the amount of
geometric distortion will continue to be monitored during semi-annual
check-outs. A better understanding of the FC flat field response and
in-field stray light characteristics may require recalibrating of image data
in the future.
 
The FC harbors a calibration lamp to monitor camera performance during
flight. The calibration lamp is a set of six AlGaInP light emitting diodes
attached to the top flange of the objective barrel. When powered on they
illuminate the inner face of the front door through a sequence of pulses on
the 5.2 V line. The diode spectrum peaks at approximately 635 nm, with half
maxima at 614 and 660 nm. Command parameters available to control the
illumination are illumination time, offset with respect to imaging start
time, pulse frequency, and duty cycle.
 
Operational Considerations
==========================
 
To ensure the safe operation of the FC, the following operational guidelines
and constraints have been defined in the form of flight rules. In principle,
these rules can be waived under given circumstances, following a justified
request by the instrument team, and with the agreement of the mission team.
 
To avoid contamination of the optical system, the FC front door is kept
closed during IPS thrusting, from Earth to Vesta approach, and following
Vesta departure to Ceres approach. This rule does not apply during orbit
transfers or maintenance maneuvers. As a precaution in case of the filter
wheel of one camera getting stuck on a colored filter, the inactive camera
is kept in clear filter to ensure that OpNav images (which are mission
critical) can be acquired after such a failure. Additionally, only one
camera is powered at any given time. To ensure an adequate thermal
environment for the camera there are two additional rules. First, the Sun is
kept away from the radiator prior to, and during, the operational phases to
reduce thermal noise to a minimum in the sensor. Second, the Sun is kept low
above the instrument deck to prevent overheating of the electronic box.
However, this rule expires once the critical heliocentric range (2.1 AU) is
exceeded. Finally, to avoid damage to the CCD, Sunlight is not allowed to
enter the baffle at an angle lower than 20 degrees.
 
 
 
There are several considerations related to image acquisitions. The size of
the FC mass memory is 1 GB and can store around 435 uncompressed full frame
images of 2.2 MB each. Assuming an achievable lossless compression ratio of
1.8, this number grows to approximately 780 images, a number that will be
higher for higher compression ratios. The maximum image acquisition rate is
approximately 1 image every 3.5 seconds, plus the applicable exposure time,
when no filter wheel changes are required. This time is needed for memory
allocation, readout of the CCD and, writing the image data to memory. For
image acquisitions involving filter changes 3 additional seconds should be
allowed to ensure safe mechanism handling. Finally, the number of commands
the FC can process is restricted to one per second. So when commanding
several image acquisitions as individual commands, one additional second has
to be allowed. Concerning the onboard processing of the images, the typical
duration is around 70 seconds for a compression ratio of 2. Lower
compression ratios will take longer to process (more data to be output).
With respect to transmission to the spacecraft, the assigned 151 kbps data
rate results in typical transmission times of 60 seconds for images
compressed by factor 2.
 
Detectors
=========
 
The FC detector is an Atmel/Thomson (now E2V) TH7888A front-side illuminated
frame-transfer CCD. This device is designed with a 1024x1024 pixel active
area and an equally sized storage area, which is covered by an optically
opaque aluminum mask. The CCD makes use of a lateral anti-blooming gate
structure, which prevents photo-generated charge from overexposed regions
from spilling over across the columns. This additional structure is
insensitive to light, so that the sensitive to total area ratio (fill factor)
of a 14 micrometer sized pixel is reduced. The front-side illuminated
architecture with semitransparent layers on the detector substrate further
decreases the effective fill factor to about 40%, with a peak quantum
efficiency of the detector at around 20%. The CCD also contains extra
columns and lines that are optically masked. These areas provide reference
values for bias and dark current.
 
The exposure time is coded in exponential form with base 10, where 3 bits
specify the exponent and 7 bits identify the mantissa. Exposure duration can
be set between 1 msec and about 3.5 h. After an exposure the charge
accumulated in the CCD active area is rapidly shifted into the storage area,
with a shift time of 1.32 msec. Subsequently, the charge is clocked out
row-by-row into the horizontal serial register and then serially shifted to
the output amplifier. The readout is clocked at one megapixel/sec, which
results in a readout time of about 1.2 s.
 
The pixel charge is conditioned by correlated double sampling (CDS)
circuitry, and digitized to 14-bit depth. The electronic gain of the analog
chain is about 18 electrons/DN at operational temperatures. When not
exposing or reading out, the FEE is in idle mode and accumulated charge is
continuously erased by simultaneously shifting the parallel and serial
registers.
 
Electronics
===========
 
The CCD controller is implemented in a field programmable gate array (FPGA),
manufactured by Actel. It generates the timing waveforms necessary for the
CCD charge shift and readout, for the CDS and for the exposure. It also
supervises the data transfer to the DPU by implementing a high speed serial
protocol. In addition to the nominal imaging operation, the CCD controller
provides a number of engineering acquisition modes: a synthetic test pattern
image, a serial readout which reads the serial register without line shift,
a storage readout which reads an image without the frame transfer, and a
crop mode where only the image area of 1024x1024 pixels is transmitted to
the DPU.
 
Filters
=======
 
The FC has 8 filters at its disposal, numbered F1 to F8. F1 is a broadband
(clear) filter, sensitive in the wavelength interval from 400 to 1100 nm,
peaking at 700 nm. The narrow-band color filters are of the interference
type, and were constructed by multilayer, thin film deposition on front and
back surfaces of silica (Suprasil) substrates. The filters are located in a
wheel, and each measure 20 mm by 20 mm with varying thickness. Their
effective wavelengths are (FWHM in brackets):
 
F2: 555 nm (+15, -28)
F3: 749 nm (+22, -22)
F4: 917 nm (+24, -21)
F5: 965 nm (+56, -29)
F6: 829 nm (+18, -18)
F7: 653 nm (+18, -24)
F8: 438 nm (+10, -30)
 
The effective wavelength is calculated as the integrated product of
wavelength and responsivity divided by the integrated responsivity, with the
integration performed over the filter passband.
 
Optics
======
 
The FC has a telecentric four-lens design. To maintain a fixed focal length
under changing temperature, the two central lenses are mounted in an inner
barrel with a different thermal expansion coefficient than the main barrel.
The resulting differential movement with changing temperature maintains the
focal plane location constant within 30 um. The chromatic variation of the
focal plane was compensated for by varying the filter thickness per filter.
Chromatic aberration was compensated for by the choice of glasses for the
lenses. The optical design required an adequate back focal length to
accommodate the filter wheel mechanism inside the camera head, between the
lens system and the CCD. The design was optimized to ensure minimal
geometric distortion (<0.1%). The following optics parameters apply to both
units:
 
----------------------------------
parameter                    FC
----------------------------------
Focal Length (mm)          150.0
Aperture (mm)               19.9
f/ratio                      f/8
IFOV (microrad/pixel)       93.3
Field of view (degree)
    Cross-track              5.46
    Along-track              5.46
----------------------------------
 
Location
========
 
The FC is mounted on the +Z deck of the spacecraft, and has the following
layout of the FOV :
 
                                  ^ +Xfc1 (down-track)
                                  | +Xfc2
                                  |
       ---              +---------|---------+
        ^               |         |         |
        |               |         |         |
        |               |         |         |
        |               |         |         |
        |5.46 deg  1024 |         x-------------> +Yfc1 (cross-track)
        |         lines |       +Zfc1       |     +Yfc2
        |               |       +Zfc2       |
        |               |                   |
        V             Pixel                 |
       ---            (0,0)-----------------+
                          1024 pixels/line
 
                        |      5.46 deg     |      Boresight (+Z axis)
                        |<----------------->|       is into the page
                        |                   |
 
Measured Parameters
===================
 
The FC measures radiance. The raw data numbers (DN) are converted to
physical units through the radiometric calibration step in the calibration
pipeline. The units associated with the calibrated Level 1b images are [W /
m^2 / nm / sr] for the color filters (F2-F8) and [W / m^2 / sr] for the
clear filter (F1).
 
Data Compression
================
 
Two wavelet compression algorithms are available on board to reduce the
image data volume: LIFT (either 16 or 32-bit) and TAP (32-bit). Three
parameters control the outcome of the compression step: - The compression
flag determines if a frame is to be compressed or not. The allowed values
are 'Compress' and 'Do not compress'. - The compression algorithm ID
determines which filtering algorithm is used. Allowed values are 16-bit LIFT,
32-bit LIFT and 32-bit TAP. - The compression ratio establishes how
strongly compressed the image will be. It is defined as the ratio between
the original data volume and the compressed volume, and is encoded as a
7-bit mantissa and 1 bit for units or tenths. Allowed values are 1 to 127.
 
The requested compression ratio is the minimum value that can be achieved,
If the compression algorithm finds a particular frame can be compressed with
higher efficiency than requested, it will do so. A requested ratio of 1 is
equivalent to requesting lossless compression. Only LIFT can compress truly
lossless. 'Lossless' TAP leads to artifacts of at most 1 DN. Lossy TAP
preserves the original image much better than lossy LIFT. Lossy TAP
compression leads to a smoothing of the data, producing absolute image
artifacts that are bigger for the bright areas than for the dark areas,
similar to the behavior of photon noise. Consequently, at relatively low
compression ratios TAP effectively smoothes photon noise. A well exposed
image of Vesta is expected to compress losslessly with a ratio of about 1.8.
 
References
==========
 
Schroder, S.E. and P. Gutierrez-Marques, Calibration Pipeline, MPS report
DA-FC-MPAE-RP-272 (29 Jan 2009).
 
Sierks, H.,  et al., The DAWN Framing Camera, P&SS Dawn special issue (2011)

        