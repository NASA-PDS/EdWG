
              Online Reference: http://wundow.wustl.edu/clbin/clsearch.pl

 
 
 
    Instrument Overview
    ===================
      The Near Infrared Camera (NIR) uses a catadioptric lens with a
      256x256 indium antimonide (InSb) focal plane array (FPA)
      mechanically cooled to cryogenic temperature.  The FPA operated
      at 70 K plus-or-minus 0.5 K at the Moon and showed excellent
      stability over the more than 500 hours of operation in space.
      The lens design features all ZnSe refractive elements with a
      relay to provide an external pupil for 100% efficient cold
      shielding.  This lens design was chosen for image quality and
      focus stability.
 
      Wavelength range was constrained by the optics and the InSb
      response to between 1.0 and 5.5 microns.  Six wavebands were
      selected by the NASA advisory committee, all falling well
      inside this range.
 
      Programmable camera electronics allow 4 integration times, 5
      bits of gain, and 8 bits of offset.  Gain states are spaced
      approximately evenly from 0.5 to 36 factors of voltage
      multiplication.  Offset is subtracted before gain is applied,
      with a range from 0 volts to full well that can be set in 1/255
      full well increments.
 
 
    Scientific Objectives
    =====================
      The primary scientific objective of the NIR was to support
      lunar mineral mapping investigations.  Pole-to-pole NAIDR
      observations with solar phase angles kept to less than 30
      degrees at mid-latitudes were the predominant viewing
      conditions during the two month systematic mapping phase of the
      mission.  The UVVIS and NIR cameras provided 100% coverage of
      the lunar surface under 11 spectral bands ranging in
      wavelengths from 415 to 2690 nm.  Image resolution ranges from
      100 meters/pixel at periselene (-28 degrees south latitude
      during first month observations, +28 degrees the second month)
      to 400 meters/pixel at the poles.
 
 
    Calibration
    ===========
      The radiometric calibration converts the digitized signal
      received from the camera (DN value) into a quantity that is
      proportional to the radiance reaching the sensor.  The
      sensitivity of the CCD focal plane array varies across the
      field of view.  The instrument response is sensitive to the
      temperatures of the FPA, optics, and cyrocooler.  During
      mission operations it was discovered that a sufficient
      cryocooler cool-down period was needed before temperatures of
      the instrument became stable.  NIR images at the start of an
      observational pass over the Moon just prior to turning on the
      cryocooler may be difficult to calibrate due to temperature
      instabilities of the instrument.
 
      The NIR camera was calibrated before launch.  Laboratory
      observations of a flat field under various operating
      temperatures and camera operation modes provide information
      about the sensitivity of the camera under expected spaceflight
      conditions.  During inflight operations, a variety of
      calibration observations were made including Apollo Landing
      site observations where laboratory spectra of returned lunar
      samples have been measured.
 
      Geometric calibration removes optical distortions of the
      imaging system.  The geometric distortion of the NIR camera has
      been shown to be minimal (maximum optical distortion does not
      exceed 3.0 pixels) and can be satisfactorily modeled by a 2nd
      order polynomial.
 
      For additional information on the geometric and radiometric
      calibration of the Clementine imaging systems, contact the PDS
      Imaging Node.
 
 
    Operational Considerations
    ==========================
      The pole-to-pole lunar observations provided scenes with a
      broad range of viewing conditions, ranging from bright
      observations near zero phase angle at the equator to very low
      light-level observations at the poles.  In order to properly
      record an observation with an optimal signal-to-noise ratio it
      is important to adequately fill the 8-bit (255 levels) dynamic
      range of the A/D camera output.  The integration time (exposure
      time) and the gain and offset operating modes of the instrument
      were adjusted to properly record each image.  Lunar
      observations were broken into 10 latitude bins.  Each latitude
      bin contained fixed gain and offset modes and integration times
      for each camera/filter combination.
 
      The Clementine orbit was designed to provide overlapping
      coverage in both the down-track (~15% overlap) and cross-track
      (~10% overlap at the equator) directions.  The image overlap is
      necessary to geometrically control images in cartographic
      applications.
 
 
    Operational Modes
    =================
      The NIR camera had three operating modes:
 
      1. Four selectable image integration times (11, 33, 57, 95 ms)
 
      2. Gain Mode. The gain mode represents the multiplicative
      constant applied to the image data passing through the A/D
      converter.  Thirty two (5 bit) gain state settings were
      available.
 
      3. Offset Mode. The offset mode represents the additive constant
      applied to the image data passing through the A/D converter.
      There were 256 (8 bit) offset mode settings.
 
 
    Camera Specifications
    =====================
 
      Detectors
      ---------
        Focal Plane Array
        Type                   : Amber PV InSb
        Pixel format           : 256x256
        Pixel size             : 38x38 microns
        Non-operable pixels    : less than 0.5%
        FPA operating temp.    : 70 K
        FPA well capacity      : 11.7 million electrons
 
        Field of view          : 5.6 deg. x 5.6 deg.
        Pixel IFOV             : 400 x 400 microrad
        Point spread           : greater than 50% energy in 30
        micrometer slit
 
 
      Electronics
      -----------
        A/D resolution         : 8 bits
        Frame rate             : 7.1 Hz (single frame mode)
        Integration times      : 11, 33, 57, and 95 ms
        Digitization gain      : 0.5 to 36 X voltage multiplication
        Offset control         : 8 bits
        Power                  : 13.0 W
 
 
      Filters
      -------
        Filter
        Wheel          Spectral
        Position       Band
        ---------------------------------------------
        A            :  1100 nm (plus-or-minus 30 nm)
        B            :  1250 nm (plus-or-minus 30 nm)
        C            :  1500 nm (plus-or-minus 30 nm)
        D            :  2000 nm (plus-or-minus 30 nm)
        E            :  2600 nm (plus-or-minus 30 nm)
        F            :  2690 nm (plus-or-minus 60 nm)
 
 
      Optics
      ------
        Clear aperture          : 29nm
        Effective focal length  : 96 mm
        Cold stop               : F/3.33, 6.0 mm diameter
        Cold shield efficiency  : 100%
 
 
      Mechanical
      ----------
        Mass                   : 1920 grams
        Size                   : 10.4 cm x 11.5 cm x 36.5 cm long
 
 
    Subsystems
    ==========
 
      Cryocooler
      ----------
        Type              : Ricor K506B integral Stirling with
                            H-10 FPA temperature closed-loop
                            control electronics
        Avg. power        : 11.0 W steady-state
 
 

        