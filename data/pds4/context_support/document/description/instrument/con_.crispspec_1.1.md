
 
CONTOUR Remote Imaging Spectrograph - Spectrometer (CRISPEC)
 
The CRISP instrument is effectively two instruments working independently
in a single package. For that reason the same description is supplied
for both the imager (CRISPIMAG) and the spectrograph (CRISPSPEC).
 
Instrument Overview
===================
CRISP actively tracks the comet's nucleus near CONTOUR's closest approach,
taking high resolution images, color images through 10 filters, and an
infrared spectral map.
 
 
Once light enters the reflective telescope, wavelengths shorter than 800 nm
are reflected by a beamsplitter to an imager. The imager has a 10-position
filter wheel, with one filter for fast, clear- filter imaging and nine
filters for measuring color differences indicative of differences in
composition of the non-ice portion of the nucleus surface. The digital image
is captured by a CCD that provides a field-of-view 1.2deg x 1.2deg (1024 x
1024 pixels). Infrared light at wavelengths beyond 800 nm is sent through a
narrow slit into the spectrometer part of CRISP. The slit forms an image of a
long, narrow portion of the nucleus. This long, narrow image is dispersed by
the spectrometer into 256 different near-infrared wavelengths from 800 nm to
2500 nm. In the resulting two- dimensional image, which is measured by a
Rockwell mercury-cadmium telluride (HgCdTe) detector cooled cryogenically to
90degK, one direction corresponds to spatial location along the slit and the
other direction corresponds to wavelength of light.
 
 
CRISP's scan mirror is the critical component that allows the instrument to
take high-resolution images (as good as 4 meters per pixel) while passing as
close as 100 kilometers from its target at high velocity. The imager and
spectrometer both 'look' at a scan mirror. The mirror steers the
fields-of-view to track the comet nucleus and take out its relative motion so
that unsmeared images can be obtained. The tracking process begins about
10,000 km before closest approach, when the comet is only a few tens of
pixels across. At this point the field-of-view is still large compared to
navigational uncertainties, so it can be pointed at the comet's position and
be assured of capturing the comet. Image processing in CRISP's Data
Processing Unit (DPU) autonomously calculates the center of the illuminated
part of the nucleus, and keeps track of the location of that point in
subsequent images. This series of measurements is used by a program in the
DPU that extrapolates into the future where it expects the nucleus to be, and
then compares the prediction with the actual position from the image
processing software. Both procedures progressively refine the estimated
location of the nucleus as a function of time before closest approach. By the
time the critical close- up data are taken, a preprogrammed set of
observations is matched with the actual flyby time to better than 1 second.
The updated three-dimensional estimate of the nucleus's location is used to
point the mirror, keep the nucleus in the center of the field-of-view, and
take out smear. This approach requires that CRISP's line-of-sight is
accurately referenced into inertial coordinates. As a result the spacecraft
star cameras, which provide the inertial reference for spacecraft pointing,
are mounted directly to CRISP instead of to the spacecraft.
 
At the Encke encounter, in the hours prior to one hour before closest
approach, CONTOUR is occasionally tilted by a few degrees so that CRISP can
monitor the distant nucleus's rotation unobstructed by the dust shield.
Subsequently, the dust shield is oriented to protect the body of the
spacecraft from impacts by dust in the comet's coma. Beginning about 6
minutes prior to closest approach, image acquisition is begun at a high rate
so that the nucleus' position can be determined and tracked. During this time
CRISP's aperture is partly occulted by the edge of the dust shield. CRISP's
main period of data acquisition begins only about 50 seconds before closest
approach when the dust shield no longer interferes with the view of the
nucleus. The mirror keeps the nucleus in the field-of-view and scans the
spectrometer slit across the surface, building up an infrared compositional
map showing features as small as about 100 meters across. Color images taken
by the imager show variations at scales three times smaller. Then a series of
clear-filter images is taken as the spacecraft's changing view of the nucleus
provides a stereo perspective. The mirror continues tracking the nucleus
until it is 30 degrees off the forward direction, about 6 seconds before
closest approach, when the highest-resolution images (about 4 meters per
pixel) are obtained. Outbound from a comet, the sequence will be repeated in
reverse.
 
                CRISP Vital Statistics
 
                         Imager            Spectrometer
 
Telescope aperture       100 mm
Telescope focal length   683 mm
Field-of-view            1.2deg x 1.2deg       0.86deg x 0.003deg
Pixel field-of-view      20 mrad (0.001deg)  59 mrad (0.003deg)
Wavelength range         450-770 nm        800-2550 nm
Spectral channels        10                256
Detector type            TH7888A Rockwell  PICNIC HgCdTe array
Pixels per image         1024 x 1024       256 spatial x 256 spectral
Typical exposure times   9-150 ms          0.2 sec
 
 
                CRISP Camera Filters
 
Wavelength   FWHM1    Purpose
 
'Clear'      350      Navigation / tracking
450          40       Nucleus geology, color
490          40       ditto
530          40       ditto
570          40       ditto
610          40       ditto
650          40       ditto
690          40       ditto
730          40       ditto
770          40       ditto
 
FWHM = full width of the wavelength range passed by the filter at greater
than half intensity
 
From http://www.contour2002.org/instruments2.html
 
Copyright 2002 NASA Discovery Program
Used by Permission

        