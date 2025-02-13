
              Online Reference: http://wundow.wustl.edu/clbin/clsearch.pl

 
    Instrument Overview
    ===================
      The Ultraviolet/Visible Camera (UVVIS) has a catadioptic
      telescope using fused silica lenses focused onto a
      metachrome-coated charge couple device (CCD) imager.  Active
      wavelength response is limited on the short wavelength end by
      the transmission of fused silica and the optical blur of the
      lens.  Wavelength response on the long end is limited by the
      response of the CCD.  Six spectral bands can be selected from a
      filter wheel which is controlled through the same
      serial-addressable synchronous interface (SASI).
 
      The Thomson focal plane array (FPA) used is a frame-transfer
      device, accomplishing electronic shuttering by rapidly shifting
      the active pixel area into the storage area, pausing for the
      13-bit programmable shuttering system integration time, then
      rapidly shifting the captured image into a storage buffer from
      which the image is read out.  Post-FPA electronics allow three
      gain states followed by 5 bits of offset that span 248 counts
      in the analog regime to augment the basic 8-bit analog/digital
      (A/D) conversion.  Gain is A/D digitization noise limited, so
      proper exposure is critical.
 
      Working against the day side of the Moon as a target, typical
      integration times were as short as several milliseconds in the
      lowest gain state (1000 electrons/bit) near sub-solar
      illumination points at the brighter spectral bands, increasing
      to 40 msec near the polar regions in the mid-gain setting for
      the weaker 415 and 1000 nanometers (nm) spectral bands.  The
      UVVIS performance specifications are shown below.
 
    Scientific Objectives
    =====================
      The primary scientific objective of the UVVIS imaging
      instrument was to support lunar mineral mapping investigations.
      Pole-to-pole NADIR observations with solar phase angles kept to
      less than 30 degrees at mid-latitudes were the predominant
      viewing conditions during the two month systematic mapping
      phase of the mission.  The UVVIS and NIR cameras provided 100%
      coverage of the lunar surface in 11 spectral bands ranging in
      wavelength from 415 to 2690 nm.  Image resolution ranges from
      100 meters/pixel at periselene (-28 degrees south latitude for
      the first month's observations, +28 degrees the second month)
      to 400 meters/pixel at the poles.
 
    Calibration
    ===========
      The radiometric calibration converts the digitized signal
      received from the camera (DN value) into a quantity that is
      proportional to the radiance reaching the sensor.  The
      sensitivity of the CCD focal plane array varies across the
      field of view but appears to be time invariant during the two
      month lunar observation period.  The UVVIS camera was
      calibrated before launch.  Laboratory observations of a flat
      field under various operating temperatures and camera operation
      modes provides information about the sensitivity of the camera
      under expected spaceflight conditions.  During inflight
      operations, a variety of calibration observations were made
      including images of stars with known radiance (Vega) and the
      Apollo Landing sites where laboratory spectra of returned lunar
      samples have been measured.
 
      Geometric calibration removes optical distortions of the
      imaging system.  The geometric distortion of the UVVIS camera
      has been shown to be minimal (maximum optical distortion does
      not exceed 0.1 pixels) and can be satisfactorily modeled by a
      radially dependent 2nd order polynomial.
 
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
      time) and the gain and offset settings of the instrument were
      adjusted to properly record each image.  During the systematic
      mapping, the gain state of the camera was normally set to 1 for
      the mid-latitude observations and set to 2 (thereby increasing
      the sensitivity of the A/D converter) at the higher latitudes.
      Integration times were increased as observations approached the
      poles.  Lunar observations were broken into 10 latitude bins.
      Each latitude bin contained fixed gain and offset modes and
      integration times for each camera/filter combination.
 
      For the UVVIS camera two observations were made in rapid
      succession acquiring both high and low integration-time images
      for the same scene.  The multiple integration-time imaging was
      designed to optimally record both maria materials (dark albedo
      material optimally recorded by the high integration-time image)
      and highland materials (high albedo materials optimally
      recorded by the low integration-time image).
 
      The Clementine orbit was designed to provide overlapping
      coverage in both the down-track (~15% overlap) and cross-track
      (~10% overlap at the equator) directions.  The image overlap is
      necessary to geometrically control images in cartographic
      applications.
 
 
    Operational Modes
    =================
      The UVVIS camera had three operating modes:
 
      1.  13-bit programmable integration time.  The range of
      integration times (in microseconds) is given by: Integration
      Time = [(N+3)*94.5 - 45, N=0,2,3...2**13)].
 
      2.  Gain Mode.  The gain mode represents the multiplicative
      constant applied to the image data passing through the A/D
      converter.  Three gain state settings were available (1,2,4)
      although gain setting 4 was seldom used during lunar
      observations.
 
      3.  Offset Mode.  The offset mode represents the additive
      constant applied to the image data passing through the A/D
      converter.  There were 14 offset mode settings (1-14) although
      offset modes 1 and 6 were predominantly used during systematic
      lunar observations.
 
 
    Camera Specifications
    =====================
 
      Detectors
      ---------
        Thomson Focal Plane Array
 
        Type                    :  Si Charge Coupled Device
                                   Thomson TH7863-CRU-UV
        Pixel format            :  288x384
        Pixel size              :  23x23 microns
        Readout rate            :  4MHz
        Wavelength Sensitivity  :  0.3 to 1.1 microns
        Field of view           : 4.2 deg. x 5.6 deg.
        Pixel IFOV              : 255 microradians
        Point spread            : 1.1 to 1.5 pixels
 
      Electronics
      -----------
 
        A/D resolution          : 8 bits
        Frame rate              : 10 Hz
        Readout time            : 27.4 msec
        Integration time        : 0.2-733 msec
        Digitization gain       : 150,350,1000 electrons/count
        Offset control          : 248 gray levels
        Power                   : 4.5 W
 
 
      Filters
      -------
 
        Filter
        Wheel                   Spectral
        Position                Band
        -----------------------------------------------
        A                       : 415nm (plus-or-minus 20 nm bw)
        B                       : 750nm (plus-or-minus 5)
        C                       : 900nm (plus-or-minus 10)
        D                       : 950nm (plus-or-minus  15)
        E                       : 1000nm (plus-or-minus 15)
        F                       : 400 to 950nm  broad band
 
 
      Optics
      ------
        Clear aperture          :  46nm
        Speed                   :  F/1.96
 
      Mechanical
      ----------
 
        Mass                    : 410 grams
        Size                    : 15.5cm x 11.7 cm x 10.4 cm
 
        Filter Wheel System -
        Type                    : 6 position, 90 deg. stepper
                                  motor driven,
 
        Hall Effect Position Sensors -
        Step and Settle time    : <250ms
        Position repeatability  : 10mr
        Power                   : 0.15 W quiescent,
                                  11.0 W stepping
 

        