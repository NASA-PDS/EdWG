
 
 
  INSTRUMENT OVERVIEW
  ===================
 
    The LROC consists of two narrow-angle camera components (NACs), a wide-
    angle camera component (WAC), and a common Sequence and Compressor System
    (SCS).
 
    Each NAC has a 700 mm focal length Cassegrain (Ritchey-Chretien) telescope
    that images onto a 5064-pixel CCD line-array providing a cross-track
    field- of-view (FOV) of 2.86 degrees. The NAC readout noise is better than
    76 e- and the data are sampled at 12 bits. By ground command, these 12 bit
    pixel values are companded to 8 bit pixels using one of several selectable
    piecewise linear mappings during readout from the CCD. The NAC internal
    buffer holds 256 MB of uncompressed data, enough for a full-resolution
    image 52,224 lines long (26-km from 50-km orbit). NAC specifications are
    summarized in Table 1.
 
    Table 1 - NAC Specifications
    -------------------------------------------------------------------------
                                      NAC-L                  NAC-R
    -------------------------------------------------------------------------
    FOV                      =       2.8502 deg              2.8412 deg
    IFOV                     =      10.0042 #rad            9.9764 #rad
    Image scale              =       0.5 m/pixel            0.5 m/pixel
      (at 50 km altitude)
    Maximum Image size       =     2.49 x 26 km            2.48 x 26 km
      (at 50 km altitude)
    f/# (Ritchey-Chretien)   =       3.577                  3.590
    Effective Focal Length   =     699.62 +/- 0.08 mm     701.57 +/- 0.09 mm
    Distortion coefficient  = 0.0000181 +/- 0.0000005  0.0000183 +/- 0.0000005
    Optical center location  =  sample 2548 +/- 8        sample 2568 +/- 8
    Primary Mirror Diameter  =       195 mm                 195 mm
    MTF (Nyquist)            =       0.23                   0.23
    Gain                     =       69.3 +/- 6.5 e-/DN     71.1 +/- 1.5 e-/DN
    Noise                    =         76 +/- 7 e-              74 +/- 2 e-
    Detector Fullwell        =    260,000 +/- 25,000 e-    271,800 +/- 5500 e-
    SNR (400-750 nm)         =         > 48                   > 46
    Detector Digitization    =          12 bit, encoded to 8 bits
    Compression              =                   1.7:1
    Structure + baffle       =          Graphite-cyanate composite
    Detector                 =              Kodak KLI-5001G
    Pixel format             =                  1 x 5,064*
    Analog/Digital Converter =               Honeywell ADC9225
    FPGA                     =               Actel RT54SX32-S
    Voltage                  =                 28 +/- 7V DC
    Peak Power               =                    8.8 W
    Average Power            =                     6 W
    Mass                     =                    7.6 kg
    Volume                   =            70 cm x 27 cm (incl. radiator)
      (lengthxdiameter)
    --------------------------------------------------------------------------
    * Of the 5064 pixels, 39 masked pixels on the right and 21 masked pixels
      on the left are used for dark reference.
 
    The WAC electronics are a copy of those flown on cameras on Mars Climate
    Orbiter, Mars Polar Lander, Mars Odyssey, and Mars Reconnaissance Orbiter.
    The WAC has two lenses imaging onto the same 1024 x 1024 pixel,
    electronically shuttered CCD area-array, one imaging in the visible/near
    infrared (VIS), and the other in the Ultraviolet (UV). In monochrome mode,
    1024 x 14 pixels are read out in one visible band (645 nm). In color mode,
    only the center 704 x 14 visible pixels and 512 x 16 UV pixels, which are
    binned to 128 x 4, are read out for each band. The VIS optics have a
    cross- track FOV of 91.7 degrees (monochrome) and 61.4 degrees (color),
    and the UV optics a 58.96 degree FOV. From the nominal 50-km orbit, the
    WAC will provide a nadir ground sample distance of 74.9 m/pixel in the
    visible, and a swath width of 104.6 km (visible monochrome), 59.6 km
    (visible color) and 56.8 km (UV color). The seven-band color capability of
    the WAC is provided by a color filter array (see Figure 1) mounted
    directly over the detector, providing different sections of the CCD with
    different filters. Consequently the instrument has no moving parts; it
    acquires data in the seven channels in a 'pushframe' mode, with scanning
    of the WAC FOV provided by motion of the spacecraft and target. Continuous
    color coverage of the lunar surface is possible by repeated imaging such
    that each of the narrow framelets of each color band overlap. The WAC has
    a readout noise less than 72 e- and, as with the NAC, pixel values are
    digitized to 12 bits and are then commanded to 8 bit values through a
    square-root-like lookup table. WAC specifications are summarized in Table
    2. The two UV bands (320 and 360 nm) undergo 4x4 pixel on-chip analog
    summing before digitization to achieve better signal-to-noise ratio.
    Thus, UV pixels are recorded at reduced 383.5 m/pixel sampling but have
    improved signal properties. Only the center 704 pixels for the visible are
    digitized when all seven bands are being acquired. WAC band passes are
    arranged first UV then VIS (320, 360, 415, 565, 605, 645, 690), but the
    order is reversed after LRO performs a 180 degree yaw maneuver to align
    the solar panels with the sun.
 
    Figure 1 - WAC Color Filter Array
    --------------------------------------------------------------------------
                                                           Zoom-in of Visible
                                                                 Array
    __________________________________________________    _________________
    |                                                |   /|  VIS5 (680nm)  |
    |          VISIBLE TRANSMITTING AREA             |  / |----------------|
    |                                                | |  |  VIS4 (640nm)  |
    |                                                | |  |----------------|
    |       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx         | |  |  VIS3 (600nm)  |
    |       x UV & VISIBLE (200 - 1100 nm) x         | |  |----------------|
    |xxxxxxxxxxxxxxxx OPAQUE AREA xxxxxxxxxxxxxxxxxxx| |  |  VIS2 (560nm)  |
    |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|/   |----------------|
    |------------------------------------------------|    |  VIS1 (415nm)  |
    |------------------------------------------------|    |----------------|
    |------------------------------------------------|   /
    |------------------------------------------------|--Visible Optical Axis--
    |------------------------------------------------|  |
    |------------------------------------------------| /
    |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|/
    |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
    |  xxxxxxx UV & VISIBLE (200 - 1100 nm) xxxxxxx  |
    |  xxxxxxxxxxxxxxx OPAQUE AREA xxxxxxxxxxxxxxxx  |
    |  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  |
    |  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  |
    |------------------------------------------------|
    |                                                |
    |                UV2 (360 nm)                    |
    |                                                |
    |------------------------------------------------|--UV Optical Axis--
    |                                                |
    |                UV1 (300nm)                     |
    |                                                |
    |          VISIBLE TRANSMITTING AREA             |
    |________________________________________________|
 
 
    Table 2 - WAC Specifications
    ------------------------------------------------------------------------
                                        Visible               UV
    ------------------------------------------------------------------------
    FOV (monochrome / color)       = 91.7 deg / 61.4 deg    58.96 deg
    IFOV                           =  1.498 mrad      7.67 mrad (4x4 binned)
    Image scale                    = 74.9 m/pixel     383.5 m/pixel (binned)
      (nadir, 50 km altitude)
    Image frame width monochrome   =  104.6 km                 -
    Image frame width 7-band color =   59.6 km             56.8 km
    Image format monochrome        =  1024 samples             -
                                       x 14 lines
    Image format color             =   704 samples         128 samples
      (for each band)                  x 14 lines         x 4 lines (binned)
    f/#                            =      5.052               5.65
    Effective Focal Length         =    6.013 mm            4.693 mm
    Entrance Pupil Diameter        =    1.19 mm             0.85 mm
    System MTF (Nyquist)           =                0.37
    Gain                           =            26.3 +/- 3 e-/DN
    Noise                          =              72 +/- 9 e-
    Detector fullwell              =          47,000 +/- 5500 e-
    Band | #eff | FWHM | SNR       =   320 nm   321 nm   32.3 nm   157
                                       360 nm   360 nm   14.9 nm   147
                                       415 nm   415 nm   36.1 nm   157
                                       565 nm   566 nm   20.1 nm   157
                                       605 nm   604 nm   20.4 nm   159
                                       645 nm   643 nm   22.5 nm   157
                                       690 nm   689 nm   38.6 nm   158
    Detector Digitization          =       11 bit, encoded to 8 bits
    Compression                    =                1.7:1
    Electronics                    =           4 circuit boards
    Detector                       =            Kodak KLI-1001
    Pixel format                   =            1,024 x 1,024
    Voltage                        =            28 +/- 7 V DC
    Peak Power                     =                 4 W
    Mass                           =               0.9 kg
    Volume                         =      15.8 cm x 23.2 cm x 32.3 cm
      (width x length x height)                (incl. radiator)
    ------------------------------------------------------------------------
    * In BW mode, 1024 pixels are read out. In color mode only the center
      704 VIS pixels are read out.
 
    The two NACs and the WAC interface with the Sequencing and Compressor
    System (SCS), the third element of the LROC. As the name implies, the SCS
    commands individual image acquisition by the NACs and WAC from a stored
    sequence delivered to the SCS by the LRO spacecraft, and losslessly
    compresses the NAC and WAC data as they are read out and passed to the
    spacecraft data system. The SCS provides a single command and data
    interface between the LROC and the LRO spacecraft data system through a
    spacewire interface.
 
    Each NAC has an estimated mass of 5.4 kg, the WAC is 0.6 kg, and the SCS
    is 0.6 kg, for a total LROC mass of 12 kg. Each NAC will use 10 W during
    image acquisition or readout, 6 W at all other times; the WAC will use 4 W
    (continuous), and the SCS will use 6 W (continuous), for a total LROC
    power dissipation of 30 W peak, 22 W average.
 
    Malin Space Science Systems, located in San Diego, California, designed
    and constructed the LROC instruments. Malin subcontracted the following:
 
    NAC optics and structure to LightWorksOptics (LWO) of Tustin, CA;
 
    Composite structure to Vanguard Composite Group (VCG) of San Diego, CA
    (VCG was the structure vendor (for Kaiser Electro-Optics) on CTX);
 
    WAC optics and structure to LightWorksOptics (LWO) of Tustin, CA;
 
    WAC Color Filter Assembly (CFA) to Barr Associates of Westford, MA.

        