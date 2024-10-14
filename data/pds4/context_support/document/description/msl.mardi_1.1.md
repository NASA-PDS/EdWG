
 
 
The following was published prior to landing:
 
  Instrument Overview
  ===================
 
Introduction:
The Mars Descent Imager (MARDI) is a fixed-focus color camera
mounted on the forward port side of the Mars Science Laboratory
(MSL) rover.  The optic axis points in the +Z direction (towards
the ground). The camera can obtain 1600 x 1200 pixel images at
a rate of 4.5 frames per second throughout the period between
heatshield separation and touchdown plus a few seconds (a period
of about two minutes). The rover software issues a start imaging
command (that includes the frame rate and the number of frames;
substantial margin is commanded to take into account unusually
long descent durations) and the camera operates thereafter
autonomously. The data are written into permanent flash memory in
realtime during acquisition for later transmission.  Hundreds of
images will be acquired at scales many times greater than available
from orbit.
 
 
Objectives:
The MARDI science investigation primary objectives are to determine
where exactly the MSL vehicle has landed and to provide a geologic
and engineering-geologic framework of the landing site for early
operations. The rover is expected to leave the area imaged by MARDI
after the first few weeks of the mission. Vehicle horizontal offset
between images within the descent sequence may permit digital
elevation models (DEMs) to be created from the descent images.
Additional objectives of the investigation are to examine vehicle
ground-referenced motion deviations from inertial measurement unit
(IMU) derived inertial position during descent to extract wind
velocity from the lower boundary layer, and to help develop and test
algorithms for future autonomous landing and hazard avoidance systems.
Although not an original requirement or objective of the investigation,
additional images may be taken during rover traverses for visual
odometry and geologic mapping.
 
 
Instrument Details:
The MARDI, like the MSL Mastcams and MAHLI, consists of 2 parts:
a camera head, mounted on the rover body, and a Digital Electronics
Assembly (DEA), housed inside the warm electronics box of the rover's
chassis. The DEA and camera head electronics are the same design as
those of MAHLI and Mastcam. The camera, like the Mastcams and MAHLI,
uses a Kodak KAI-2020CM interline transfer CCD with 1600 by 1200
active 7.4 micron square pixels. Red/green/blue (RGB) color imaging
similar to the colors the human eye sees is achieved using filtered
microlenses arranged in a Bayer pattern.
 
The rectangular field of view (FOV) of the detector is inscribed
within a 90 degree diameter circular FOV, yielding a 70 degree by
55 degree frame with the long axis transverse to the direction of
motion. The instantaneous field of view (IFOV) of the camera is
~0.76 milliradians per pixel, which provides in-focus pixel scales
that range from about 1.5 m at 2 km altitude to 1.5 mm at 2 m altitude,
and covers between 2.4 x 1.8 km and 2.4 x 1.8 m at these respective
altitudes. At distances less than 2 m, out-of-focus blurring
increases at the same rate that spatial scale decreases, resulting
in a constant scale of 0.75 mm/pixel (calibration demonstrates the
potential for acquiring 1.5 mm resolution images of the surface
after landing).
 
An 8 Gbyte internal buffer permits the camera to acquire over
4,000 raw frames (equivalent to 800 seconds of descent, which
is many times the actual descent duration). For a landing at
3 p.m. local time (incidence = 55 degrees) and an albedo of 0.2,
the nominal SNR will be ~80:1 in the green and red, and >50:1 in
the blue. Lossy JPEG or lossless predictive compression is applied,
and 200 x 150 pixel thumbnails are created, during read out from
the buffer.
 
Large angular rate motion while the vehicle is descending on parachute,
and rocket thruster induced vibratory motion, are likely to blur some
of the images despite a 1.3 millisecond exposure time.
 
A white swatch of beta cloth is affixed to the interior surface of the
MSL heat shield to serve as a MARDI white balance target as the heat
shield falls away during descent to the martian surface.
 
 
 
Updates post-landing:
 
The rover entry, descent, and landing (EDL) sequence, operating within
the rover computer, issued a start imaging command to the MARDI,
triggered on actual event times during EDL.  That sequence told the
MARDI to take 1504 images as fast as it could (frame rate is a complex
function of image size, image sub-framing, camera clock speeds, and
charge flushing; the final frame rate was 3.88 frames per second), and
started that sequence ~13 seconds after parachute deployment, while
the heat shield was still attached.  These images were un-illuminated.
Heat shield jettison occurred ~6 seconds later (between the 26th and
27th MARDI image).  A total of 626 images were acquired while the
vehicle was in flight, with an additional 878 acquired on the surface
after landing.  Of the 626 acquired in-flight, ~140 were at pixel
scales better than 35 cm.

        