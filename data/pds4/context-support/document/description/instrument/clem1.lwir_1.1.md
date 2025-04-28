
              Online Reference: http://wundow.wustl.edu/clbin/clsearch.pl

 
    Instrument Overview
    ===================
      The Longwave Infrared Camera (LWIR) camera uses a catadioptric
      lens with a 128 x 128 mercury cadmium telluride (HCT) focal
      plane array (FPA).  The FPA was mechanically cooled to
      cryogenic temperatures during operation with a temperature set
      point goal of 65 K.  The optics design incorporates an internal
      relay with 100% cold shield efficiency.  Wavelength range was
      controlled by the cold filter to between 8.0 and 9.5 microns.
 
      Camera electronic design is virtually identical to the NIR
      camera, with a minor alteration in line readout to compensate
      for the difference in column count between the two arrays (256
      for the NIR, 128 for the LWIR).  The NIR and LWIR cameras also
      share a common cryocooler and dewar design, with minor
      modifications made to accommodate cold shield and cold filter
      differences.
 
 
    Scientific Objectives
    =====================
      The LWIR camera performed thermal observations of the Lunar
      surface in the broad-band spectral region centered at 8750
      nanometers.  Because of the narrow field-of-view of the LWIR
      camera, overlapping coverage in the cross track-direction was
      not possible between -80 and +80 degrees of latitude.
 
 
    Calibration
    ===========
      The radiometric calibration converts the digitized signal
      received from the camera (DN value) into a quantity that is
      proportional to the radiance reaching the sensor.  The
      sensitivity of the CCD focal plane array varies across the
      field of view.  The instrument response is sensitive to the
      temperatures of the FPA, optics, and cryocooler.  During
      mission operations it was discovered that a sufficient
      cryocooler cool-down period was needed before temperatures of
      the instrument became stable.
 
      The LWIR camera was calibrated before launch.  Laboratory
      observations of a flat field under various operating
      temperatures and camera operation modes provide information
      about the sensitivity of the camera under expected spaceflight
      conditions.  During inflight operations, calibration observations
      were made over the Apollo 17 Landing site where surface
      temperatures were measured in-situ.
 
      Geometric calibration removes optical distortions of the
      imaging system.  The geometric distortion of the LWIR camera
      has been shown to be minimal (maximum optical distortion does
      not exceed 0.1 pixels) and can be satisfactorily modeled by a
      radially dependent 2nd order polynomial.
 
      For additional information of radiometric calibration of the
      LWIR camera see [LAWSONETAL2000].
 
    Operational Modes
    =================
      The LWIR camera had three operating modes:
 
      1.  Four selectable image integration times (0.144, 0.92, 2.30,
      4.60 ms) were available, but only 0.144 ms was used.
 
      2.  Gain Mode.  The gain mode represents the multiplicative
      constant applied to the image data passing through the A/D
      converter.  There were 32 (5 bit) gain state settings were available.
 
      3.  Offset Mode.  The offset mode represents the additive
      constant applied to the image data passing through the A/D
      converter.  There were 256 (8 bit) offset mode settings.
 
 
    Camera Specifications
    =====================
 
      Detectors
      ---------
        Focal Plane Array -
        Type                     : Amber PV HgCdTe
        Pixel format             : 128x128
        Pixel size               : 50x50 microns
        Non-operable pixels      : <5%
        FPA Operating Temperature: 65 K nominal
        FPA well capacity        : 42 million electrons
        Field of view            : 1 deg. x 1 deg.
        Pixel IFOV               : 143 x 143 microrad
        Point spread             : >60% energy in 79 micrometer slit
 
 
      Electronics
      -----------
        A/D resolution     : 8 bits
        Frame rate         : 52.9 Hz (single frame mode)
        Pixel rate         : 500kHz
        Integration times  : 0.144, 0.92, 2.30, and 4.60 ms
        Digitization gain  : 0.5 to 36 X voltage multiplication
        Offset control     : 8 bits
        Power              : 13.0 W
 
 
      Filters
      -------
        No filter wheel housing existed on the LWIR camera.  The
        single spectral band is centered at 8750 nm with a band width
        of 1500 nm.
 
 
      Optics
      ------
        Equivalent clear aperture : 29nm
        Effective focal length    : 96 mm
        Cold stop                 : F/2.67, 7.47 mm diameter
        Cold shield efficiency    : 100%
        Focal Length              : 350 nm
 
 
      Mechanical
      ----------
        Mass              : 2100 grams
        Size              : 14.7 cm diameter x 36.1 cm long
 
 
    Subsystems
    ==========
 
      Cryocooler
      ----------
        Type              : Ricor K506B integral Stirling with
                            H-10 FPA temperature closed-loop
                            control electronics
        Avg. power        : 11.0 W steady-state

        