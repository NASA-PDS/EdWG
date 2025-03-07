
 
 
  Instrument Overview
  ===================
    The Imager for Mars Pathfinder or IMP is a stereo imaging
    system with color capability provided by twenty-four selectable
    filters for the two camera channels.  It is derived from the
    descent imager/spectral radiometer (DISR) instrument aboard the
    Cassini Huygens probe.
 
 
  Scientific Objectives
  =====================
    The IMP camera was designed to study martian geological
    processes and surface-atmosphere interactions similar to what
    was observed at the Viking landing sites.  Through the use of
    panoramic stereo images taken at various times of the day, it
    was also used to observe the general landscape, surface slopes,
    and the distribution of rocks.  Changes in the scene over the
    lifetime of the mission, possibly attributable to the actions
    of frost, dust or sand deposition, erosion or other
    surface-atmosphere interactions, were monitored.  A greater
    understanding of the surface and near-surface soil properties
    was sought.  This was to be obtained partly with data acquired
    by the Rover and APXS and partly by IMP imaging of Rover wheel
    tracks, holes dug by the Rover wheels, and any surface
    disruptions caused by airbag bounces or retractions.
 
    An investigation was made of atmospheric aerosols and water
    vapor.  This included the determination of the aerosol optical
    depth as a function of wavelength above the landing site, the
    size and density distribution of the aerosols, a
    characterization of the shape of the aerosol particles, the
    vertical distribution of the aerosols, and the imaginary
    refractive index of the particles.
 
    The IMP experiment also included a magnetic properties
    investigation.  A set of magnets of differing field strengths
    were mounted to a plate and attached to the lander.  Images
    taken over the duration of the landed mission were used to
    determine the accumulation of magnetic species in the
    wind-blown dust.  Multispectral images of these accumulations
    were used to differentiate among the several proposed mineral
    compositions.
 
    The IMP investigation included the observation of wind
    direction and velocity using wind socks mounted on the ASI/MET
    mast.
 
 
  Subsystems
  ==========
    The IMP consists of three physical subassemblies: (1) camera
    head (with stereo optics, filter wheel, CCD and pre-amp,
    mechanisms and stepper motors); (2) extensible mast with
    electronic cabling; and (3) two plug-in electronics cards (CCD
    data card and power supply / motor drive card) which plug into
    slots in the lander's Integrated Electronics Module.
 
    The major components of the camera head and electronics cards
    are described in greater detail below.
 
    The extensible mast was built by AEC Able Corp, and is a
    continuous longeron, open-lattice type used for magnetometers.
    It was held in its stowed position during cruise by a
    pyro-activated pin puller.  Upon deployment, the camera system,
    mounted at the top of the mast, sprung up to a height of 62 cm
    above its stowed position, or roughly .9 meters above the
    surface of Mars.
 
 
  Detectors
  =========
    Azimuth and elevation drives for the camera head are provided
    by stepper motors with gear heads, providing a field of regard
    of +/- 178 degrees in azimuth and +83 degrees to -72 degrees in
    elevation, relative to lander coordinates.
 
 
    IMP Mechanical Characteristics
    ------------------------------
      Stereo separation : 15.0 cm
      Toe-in            : 12.5 mrad (left); -24.5 mrad (right)
      AZ/EL step size   : 0.553 degrees, 1 degree hysteresis
                          (backlash)
      Repeatability     : < 5 mrad, when approaching from the same
                          direction
      Step speed        : 10 steps per second
      Pointing range    : 360 degrees azimuth, +90 to -67 degrees
                          elevation
      Data compression  : 1.3:1 lossless up to 24:1 lossy (JPEG)
                          (higher compression ratios achieved using
                          pixel blocking)
 
      The focal plane of the IMP consists of a CCD mounted at the
      foci of two optical paths where it is bonded to a small
      printed wiring board, which in turn is attached by a short
      flex cable to the preamplifier board.  The CCD is a
      front-illuminated frame transfer array with 23 micrometer
      square pixels.  Its image section is divided into two square
      frames, one for each half of the stereo FOV's.  Each has 256
      x 256 active elements.  A 256 x 512 storage section
      (identical to the imaging section) is located under a metal
      mask.  The IMP focal plane and electronics are nearly
      identical copies of the comparable subsystem employed in the
      Huygens Probe Descent Imaging Spectroradiometer (DISR), using
      the Loral 512 x 512 CCD.  The entire CCD subsystem is
      provided by the Max Planck Institute for Aeronomy.
 
 
    CCD specifications
    ------------------
      Readout noise     : 15 electrons
      Full well         : 125,000 electrons
      Readout time      : 2 sec. for full array; 1 sec. for left
                          eye only
      Exposure time     : 0 - 32.7675 seconds; step size is 0.5
                          milliseconds
      Spectral range    : 440 - 1000 nm
      Gain              : 30 electrons/pixel
      ADC               : 12 bits/pixel
      Frame transfer    : 0.5 milliseconds (no mechanical shutter)
      SNR               : <= 350
      Pixel size        : 23 x 17 micrometers; 6 micrometers for an
                          antiblooming channel
 
 
  Optics
  ======
    The stereoscopic imager includes two imaging triplets, two fold
    mirrors separated by 150 mm for stereo viewing, two 12-space
    filter wheels (one in each path), and a fold prism to place the
    images side-by-side on the CCD focal plane.  Fused silica
    windows at each path entrance prevent dust intrusion.  The
    optical triplets are an f/10 design, stopped down to f/18 with
    23-mm effective focal lengths and a 14.4 degree field of view.
    The pixel instantaneous field of view is one milliradian.
    There are a total of 24 filters (twelve on each filter wheel)
    divided into the following categories: four stereo geology
    channels, eleven monoscopic geology channels, eight monoscopic
    channels for solar and atmospheric studies, and one magnifying
    filter.
 
 
    IMP optical characteristics
    ---------------------------
      Resolution        : 0.981 mrad/pixel (left); 0.985 mrad/pixel
                          (right)
      Focal length      : 23 mm
      f/number          : f/18
      FOV               : 14.4 degrees x 14.0 degrees
      Depth of Field    : best focus, 1.3 m; DOF, 0.5 m to infinity
 
 
  Electronics
  ===========
    The IMP has three electronics boards, all of which are housed
    in the lander chassis, in order to keep them warm (above -50
    degrees Celsius).  They are connected to the onboard computer
    via the VME bus link.  The first board is a copy of the DISR
    power supply, which provides all the necessary voltages for the
    CCD system from the lander 28 V power bus.
 
    The second board sends clock pulses to the CCD.  The twelve bit
    ADC also receives the analog signals back from the pre-amp
    board and converts them to digital signals over a period of two
    seconds, to be stored in the frame buffer chip on the third
    board.
 
    The frame buffer board is connected to the VME backplane and is
    controlled by a field programmable gate array functioning as a
    state machine for command decoding.  This third board also
    phases the steps and drives the three motors.
 
 
  Filters
  =======
    Center wavelengths are shown for both the left and right eyes,
    and are measured in nanometers.
 
    Bandwidths shown are likewise for both left and right eyes, and
    are also measured in nanometers.
 
    Responsivity (R) as a function of temperature (T) is shown for
    each filter and each eye as the parameters of a quadratic,
    where:
 
    R(T) = a1 + (a2 * T) + (a3 * T^2)
 
 
    Filter 0
    --------
      Filter Name             : L440_R440
      Filter Application      : Stereo, Geology
      Filter Type             : Interference
      Center Wavelength       :  443.3  443.0
      Filter Bandwidth        :   26.2   26.2
      Responsivity, left eye  :  128.8   -0.387  -0.0007
      Responsivity, right eye :  117.9   -0.392  -0.0006
 
 
    Filter 1
    --------
      Filter Name             : L450_R670
      Filter Application      : Solar
      Filter Type             : Interference
      Center Wavelength       :  450.3  669.8
      Filter Bandwidth        :    4.91   5.30
      Responsivity, left eye  :    0.246 -0.0025 -0.00001
      Responsivity, right eye :    2.238 -0.0058 -0.00002
 
 
    Filter 2
    --------
      Filter Name             : L885_R947
      Filter Application      : Solar
      Filter Type             : Interference
      Center Wavelength       :  883.4  945.5
      Filter Bandwidth        :    5.60  43.7
      Responsivity, left eye  :   14.5    0.0233  0.00002
      Responsivity, right eye :   25.94   0.078   0.00005
 
 
    Filter 3
    --------
      Filter Name             : L925_R935
      Filter Application      : Solar
      Filter Type             : Interference
      Center Wavelength       :  924.9  935.6
      Filter Bandwidth        :    5.03   4.91
      Responsivity, left eye  :    5.389  0.0193  0.00004
      Responsivity, right eye :    9.738  0.028  -0.000003
 
 
    Filter 4
    --------
      Filter Name             : L935_R990
      Filter Application      : Solar
      Filter Type             : Interference
      Center Wavelength       :  935.4  988.9
      Filter Bandwidth        :    4.84   5.39
      Responsivity, left eye  :   10.42   0.0378  0.00006
      Responsivity, right eye :    1.857  0.0064 -0.000006
 
 
    Filter 5
    --------
      Filter Name             : L670_R670
      Filter Application      : Stereo, Geology
      Filter Type             : Interference
      Center Wavelength       :  671.4  671.2
      Filter Bandwidth        :   19.7   19.5
      Responsivity, left eye  :  575.3   -0.570  -0.0013
      Responsivity, right eye :  557.3   -0.575  -0.0014
 
 
    Filter 6
    --------
      Filter Name             : L800_R750
      Filter Application      : Geology
      Filter Type             : Interference
      Center Wavelength       :  801.6  752.0
      Filter Bandwidth        :   21.0   18.9
      Responsivity, left eye  :  872.2    0.237  -0.0029
      Responsivity, right eye :  787.1   -0.247  -0.0019
 
 
    Filter 7
    --------
      Filter Name             : L860_R-DIOPTER
      Filter Application      : Geology
      Filter Type             : Interference
      Center Wavelength       :  858.4  900.0
      Filter Bandwidth        :   34.4
      Responsivity, left eye  : 1435      2.491   0.0035
      Responsivity, right eye : 7596.9    9.057  -0.0235
 
 
    Filter 8
    --------
      Filter Name             : L900_R600
      Filter Application      : Geology
      Filter Type             : Interference
      Center Wavelength       :  897.9  599.5
      Filter Bandwidth        :   40.8   21.0
      Responsivity, left eye  : 1120      3.006   0.0059
      Responsivity, right eye :  592.7   -0.598  -0.0013
 
 
    Filter 9
    --------
      Filter Name             : L930_R530
      Filter Application      : Stereo, Ranging, Geology
      Filter Type             : Interference
      Center Wavelength       :  931.1  530.8
      Filter Bandwidth        :   27.0   29.6
      Responsivity, left eye  :  478.7    1.928   0.005
      Responsivity, right eye :  578.6   -0.893  -0.002
 
 
    Filter 10
    ---------
      Filter Name             : L1000_R480
      Filter Application      : Geology
      Filter Type             : Interference
      Center Wavelength       : 1002.9  479.9
      Filter Bandwidth        :   29.1   27.0
      Responsivity, left eye  :  213.4    1.606   0.0052
      Responsivity, right eye :  368.1   -0.668  -0.002
 
 
    Filter 11
    ---------
      Filter Name             : L965_R965
      Filter Application      : Stereo, Ranging, Geology
      Filter Type             : Interference
      Center Wavelength       :  968.0  966.8
      Filter Bandwidth        :   31.4   29.6
      Responsivity, left eye  :  395.8    2.027   0.0051
      Responsivity, right eye :  393.5    2.185   0.0065
 
 
  Operational Modes
  =================
    Many optional command parameters are available to control the
    exposure and processing.  These include everything from
    exposure time to the amount and type of data compression.
    Subframing boundaries and pixel averaging parameters can also
    be specified.  All of this information is attached to the image
    headers.
 
    Both lossless and lossy data compression are available.  The
    lossless compression (with a compression rate between 1.3:1 and
    2:1, depending on the busyness of the scene) employs a Rice
    algorithm developed at JPL.  For cases where lossy compression
    is acceptable, compression rates between 6:1 and 24:1 can be
    obtained using a modified JPEG compressor, which uses
    arithmetic coding developed at the Technical University of
    Braunschweig.  This compression is enhanced by local cosine
    transform prior to the JPEG-specific discrete cosine transform
    and made robust against data dropouts.  Higher compression
    ratios are achieved using pixel blocking.
 
    Additional alternatives for reducing the amount of data include
    image subframing and row and column averaging.  Subframing is
    primarily useful when imaging targets like the Sun; most Sun
    images are returned as 31 x 31 pixel blocks.  Row and column
    averaging can be used for sky images, providing a gradient and
    the edges of cloud features but not the high-resolution of a
    normal image.
 
    For more details on IMP data compression, please see the IMP
    EDR archive dataset object or [RUEFFERETAL1995].
 
 
  Calibration
  ===========
    The preparation of the IMP calibration files and algorithms has
    not yet been completed.  Until it is, please see
    [CROWEETAL1997] and [WELLMAN1996A].
 
 
  Operational Considerations
  ==========================
    There is some uncertainty in the height of the IMP camera above
    the surface of Mars.  If we assume a relatively flat surface
    under the lander, then the height (h) of the elevation axis of
    the camera above the Martian surface is given by:
 
      h = MAST + BASE + ISA + AIRBAG LAYER
 
      where
 
      MAST  = the distance between the stowed IMP elevation axis and
              the deployed IMP elevation axis (0.61825 m)
 
      BASE  = height of the stowed IMP elevation axis above the
              Integrated Support Assembly (ISA) (0.17550 m)
 
      ISA   = height of the ISA box (0.436576 m)
 
      LAYER = the vertical distance between the local Martian
              surface and the bottom of the ISA box: includes the
              petal, the airbag gas generator, the airbags, rocks,
              and anything else between the ISA and the flat
              Martian surface.  Current best estimate is 0.30 m
              +/- 50% uncertainty.
 
 
      Note: Drawing not to scale.
            ______
           | _  _ |  __________
           |______|            \
             |  |               \
             |  |                \
             |  |                 \
             |  |                  >------ MAST height = 0.61825 m
             |  |                 /
             |  |                /
             |  |               /
             |  |    __________/
            [    ]   __________>---------- BASE height = 0.17550 m
    |-----------------------|  \
    |                       |   \
    |                       |    >-------- ISA height = 0.43657 m
    |                       |   /
    |                       |__/__________________
    [][][][][][][][][][][]][][][][][][][]   petal \
    airbag gas generator, etc..                    \
    airbag airbag airbag airbag airbag airbag       >-- LAYER ~ 0.30 m
    airbag rocks airbag rocks airbag rocks        _/
    ------------------------------------------------------------------
 
      Minor note: The optical axis is displaced ~0.012 m above the
                  elevation axis.
 
    Therefore, the height of the camera in the stowed and deployed
    positions is:
 
      STOWED_HEIGHT_ABOVE_SURFACE = 0.62 + ~ 0.30 = ~ 0.92 m
      DEPLOYED_HEIGHT_ABOVE_SURFACE = 1.24 + ~ 0.30 = ~ 1.54 m
 
    Given a roughly 50% uncertainty in the thickness of the AIRBAG
    LAYER, the uncertainty in the stowed and deployed heights of
    the camera are around 20% and 10%, respectively.
 
    The flight model IMP has some measured characteristics which
    differ from the ideal, but which do not prevent success of the
    goals for mission science.  These characteristics are:
 
  1. Unequal toe-in between the two eyes.
 
  2. Some vignetting is present, primarily about three image lines in
     the left eye due to the left mirror mount.
 
  3. The left eye points downward about 0.8 milliradians compared to the
     right eye.
 
  4. The eyes have image scales differing by about 0.4%.
 
  5. Aliasing is significant at all wavelengths.
 
  6. Alignment changes by about 0.5 milliradian as a function of the
     filter selected.
 
  7. Camera pointing can be inexact due to a backlash effect.
 

        