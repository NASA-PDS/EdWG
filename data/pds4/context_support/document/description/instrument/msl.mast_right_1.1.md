
 
 
The following was published prior to landing:
 
  Instrument Overview
  ===================
 
Introduction:
The Mast-mounted Cameras (Mastcams) are two instrument suite
of imaging systems on the Mars Science Laboratory rover's
Remote Sensing Mast (RSM).
 
 
Objectives:
The MastCam primary objective is to characterize and determine
details of the history and processes recorded in geologic material
at the MSL site, particularly as they pertain to habitability.
MastCam will acquire panoramic, stereo, color, multispectral
(400-1100 nm), and selected mosaics, zoom (close-up) images, and
high-definition video observations to address the following specific
objectives:
 
1. Observe Landscape Phyisography and Processes. Provide a full
description of the topography, geomorphology, and geologic setting
of the MSL landing site, and the nature of past and present geologic
processes at the site.
 
2. Examine the Properties of Rocks. Observe rocks (outcrops and
clasts 3-4 mm) and the results of interaction of rover hardware with
rocks to help determine morphology, texture, structure, mineralogy,
stratigraphy, rock type, history/ sequence, depositional, diagenetic,
and weathering processes for these materials.
 
3. Study the Properties of Fines. Examine martian fines (clasts
<4 mm) to determine the processes that acted on these materials
and individual grains within them, including physical and mechanical
properties, the results of interaction of rover hardware with fines,
plus stratigraphy, texture, mineralogy, and depositional processes.
 
4. View Frost, Ice, and Related Processes. Characterize frost or ice,
if present, to determine texture, morphology, thickness, stratigraphic
position, and relation to regolith and, if possible, observe changes
over time; also examine ice-related (e.g., periglacial) geomorphic
features.
 
5. Document Atmospheric and Meteorologic Events and Processes. Observe
clouds, dust-raising events, properties of suspended aerosols (dust,
ice crystals), and (using the video capability) eolian transport of
fines.
 
6. Support and Facilitate Rover Operations, Analytical Laboratory
Sampling, Contact Instrument Science, and Other MSL Science. To
assist rover navigation, acquire images that help determine the
location of the Sun, horizon features, and provide information
pertinent to rover trafficability (e.g., hazards at hundreds of
meters distance). For MSL science instruments, provide data that
help the MSL science teams identify materials to be collected for,
and characterize samples before delivery to, the MSL Analytical
Laboratory; help teams identify and document materials to be
examined by the Contact Instruments; and acquire images that
support other MSL instruments that may need them.
 
 
Instrument Details:
The Mastcams are two cameras with different focal lengths and
different science color filters. One camera, referred to as the
M-34 has a 34 mm focal length, f/8 lens that illuminates a 15
degree x 20 degree FOV over 1200 x 1600 pixels with slight corner
vignetting. A typical image is likely to be 1152 x 1536 pixels
owing to JPEG encoding constraints.  The other camera, referred
to as M-100, has a 100 mm focal length, f/10 lens that
illuminates a 5.1 degree x 6.8 degree, 1200 x 1600 pixel FOV.
Both cameras can focus from closer than 2.1 m (nearest view to
the surface) and to infinity. The M-100 IFOV is 7.4 x 10^-5
radians, yielding 7.4 cm/pixel scale at 1 km distance and ~150
micron/pixel scale at 2 m distance.  The M-34 IFOV is 2.2 x 10^-4
radians, giving a pixel scale of 450 micron at 2 m distance and
22 cm at 1 km. A strict definition of in focus is used for
these cameras wherein the optical blur circle is less than or
equal to 1 pixel.
 
Each camera has an 8 Gbyte internal buffer that permits it to
store about 4,200 raw frames. Each is capable of losslessly
compressing the images, or applying lossy JPEG compression, in
realtime during acquisition and storage, or during readout of
the buffer. A full-scale mosaic of 360 degrees x 80 degrees
imaged in 3 science color filters with greater than or equal
to 20% overlap between adjacent images with lossless compression
is about 6.6 GBytes; with minimally lossy JPEG compression, less
than or equal to 2.5x (3.2 bits/pixel), a mosaic including all
science filters could be acquired. This is much more than can be
sent back to Earth under normal communication limitations.
Subframing of images is also available during image acquisition
but not after and pixel summing is not available. Color 144 x 192
pixel thumbnail images can be created and compressed during
readout, or from previously acquired raw or compressed images.
Mosaics of thumbnail images from the M-34 can be used to synthesize
wider-angle FOVs.
 
Both Mastcams are color imagers. Integrated over each detector is
a RGB pattern filter. A broadband (IR cutoff) filter through which
RGB imaging will occur is included in one of the 8 filter positions
within each camera's filter wheel. Both cameras also have a narrow
band filter with 10^5 neutral density attenuation to image the sun.
The filters are distributed between the 34 mm and 100 mm cameras to
ensure each can address some of the compositional objectives of the
investigation should the other camera fail. The science filters are
imaged through the RGB filter array; for some science filters, the
throughput in some pixels of the unit cell will be poorer than in
other pixels, but beyond 700 nm, all three Bayer colors have nearly
identical throughput (i.e., they have large IR leaks, that we are
using to our advantage). In-flight calibration uses the MER Pancam
spare target with magnets mounted beneath the 4 color chips and
white and gray surfaces to provide dust-free spots (following the
approach of the Phoenix SSI team).
 
Mastcam hardware and internal processing permits a wide range of
operational flexibility. Each camera is capable of acquiring images
at very high frame rates compared to previous missions, including 720p
high definition video (720 x 1280 pixel) at ~8 frames per second, and
full science frames at somewhat greater than 4.5 fps. Traverse of the
full focus range requires between 45 and 60 seconds, but autofocus
around a known focus position can be accomplished much faster. Changes
to consecutive filter positions takes 5-8 seconds, and between 30 and
45 seconds to rotate the filter wheel a full 360 degrees. Mosaic
acquisition is paced by the time it takes the rover RSM to move and for
motion induced vibration to settle (greater than or equal to 5 seconds
between movements). The cameras include auto- and command-focus
capability and auto- and command-exposure control. Radiometric accuracy
is better than 10-15%, and precision 5-8%. Exposure times are expected
to vary from a few tens of msec to a couple hundred msec, depending on
filter bandpass and desired signal-to-noise ratio.

        