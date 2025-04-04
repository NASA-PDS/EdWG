  Instrument Overview
  ===================
    The Microscopic Imager (MI) is a fixed-focus camera mounted
    on the end of an extendable instrument arm, the Instrument
    Deployment Device (IDD). The MI was designed to acquire images
    at a spatial resolution of 30 microns/pixel over a broad
    spectral range (400 - 700 nm). The MI uses the same electronics
    design as the other MER cameras but has optics that yield a
    field of view of 31 x 31 mm across a 1024 x 1024 pixel
    charge-coupled device (CCD) image. The MI acquires images using
    only solar or skylight illumination of the target surface. A
    contact sensor is used to place the MI slightly closer to the
    target surface than its best focus distance (about 69 mm),
    allowing concave surfaces to be imaged in good focus. Coarse
    focusing (~ 2 mm precision) is achieved by moving the IDD away
    from a rock target after the contact sensor has been activated.
    The MI optics are protected from the Martian environment by a
    retractable dust cover. The dust cover includes a Kapton window
    that is tinted orange to restrict the spectral bandpass to 500
    700 nm, allowing color information to be obtained by taking images
    with the dust cover open and closed. MI data will be used to place
    other MER instrument data in context and to aid in petrologic and
    geologic interpretations of rocks and soils on Mars.
 
    Information in this instrument description is taken from the Athena
    Microscopic Imager Investigation paper[HERKENHOFFETAL2003]. See
    this paper for more details.
 
 
  Scientific Objectives
  =====================
    The chief scientific objectives of the MI are:
 
    1) to image fine-scale morphology and reflectance of natural rock
       and surfaces,
 
    2) to image fine-scale texture and reflectance of abraded rock
       surfaces,
 
    3) to aid in the interpretation of data gathered by other Athena
       instruments by imaging areas examined by them at high resolution,
       and
 
    4) to monitor the accumulation of dust on the capture and filter
       magnets.
 
 
  Calibration
  ===========
    Many of the MI components were tested before they were built into
    the cameras, primarily to verify performance. Many component-level
    tests are important to overall camera calibration, including
    spectral transmission of the optics, filters, and dust cover
    windows, calibration of temperature sensors, and performance of the
    CCDs. The spectral transmission of the optical barrel assemblies was
    tested by the optics vendor, Kaiser Electro-Optics. The spectral
    transmission of the MI filters was measured at JPL, and the dust
    cover window spectral transmission was measured at the NASA Johnson
    Space Center. The temperature sensors were calibrated at the vendor,
    Rosemount Aerospace. The CCDs used in the MER cameras were
    thoroughly tested at JPL; the results of these tests (including
    photon transfer/linearity, dark current, flat field, residual bulk
    image, and spectral quantum efficiency) were used to select the best
    CCDs for the flight cameras. Residual bulk image is most prevalent
    at low temperatures and long (near-IR) wavelengths and is therefore
    not expected to be significant for the MI. The details of the CCD
    tests are given in MER project document 420-1-485 (JPL D-20247).
 
    The MER science cameras were assembled, tested, and calibrated in
    a clean laboratory environment at JPL. The laboratory configuration
    and equipment were customized for MER testing and calibration. Most
    of the science camera testing and calibration was done in two labs,
    one for ambient testing and another for thermal/vacuum testing. The
    geometric and other tests that were not significantly affected by
    temperature were performed at room temperature and pressure on
    optical benches with electrostatic discharge protection. Three
    science cameras (2 Pancams, 1 MI) were tested together in the
    thermal/vacuum chamber, all three viewing external targets and
    sources through an optical grade quartz window.  The thermal tests
    and calibration were performed under high vacuum (&lt;10-6 torr) at a
    variety of temperatures spanning the expected temperature range on
    the surface of Mars. Flight-acceptance thermal cycling was performed
    before camera calibration, and some calibration data were acquired
    during the acceptance tests. At very low temperature (163 K), the
    optimum video offset for each camera was determined by measuring the
    dark current in zero-exposure images and avoiding clipping the
    signal to zero DN. Most of the MI calibration was done at the
    extremes of the operating temperature range (218 K and 278 K) and at
    one intermediate temperature (263 K). All tests were successfully
    performed during the period July-September, 2002; 18.4 Gbytes of MI
    calibration data were generated and copied to the USGS for reduction
    and analysis.
 
 
  Operational Considerations
  ==========================
    The MI has several performance requirements:
 
    1) Instantaneous Field of View (IFOV) of 30 +/-1.5 micrometers/pixel
       on-axis
 
    2) Field of View (FOV) of 1024 x 1024 square pixels
 
    3) Spectral bandpass of 400-680 nanometers
 
    4) Effective depth of field of &gt;+/-3 millimeters
 
    5) Optics MTF &gt;0.35 at 30 lp/mm over spectral bandpass at best
       focus
 
    6) Radiometric calibration absolute accuracy of &lt;20% and relative
      (pixel-to-pixel) accuracy of &lt;5%
 
    7) Signal to Noise Ratio (SNR) &gt;100 for exposures of &gt;20% full
       well over the spectral bandpass within the calibrated operating
       temperature range
 
    8) Temperature sensor, accurate to +/-2 K, on the CCD
       package that can be read out and associated with the image data
       in telemetry
 
    9) Working f/# = 15 +/-0.75
 
    10) Operating temperature range within calibrated specifications
        = 218 +/-2 K to 278 +/-2 K
 
    Other circumstances that would affect the performance of the MI are
    involved in the positioning of the IDD. The IDD positioning
    requirements are:
 
    1) Position instruments to an angular accuracy of 5 degrees in free
       space within the dexterous workspace of the
       Instrument Positioning System (IPS)
 
    2) Position instruments to a positional accuracy of 5 mm in free
       space within the dexterous workspace of the IPS
 
    3) Repeatably position instruments to +/-4 mm in position and +/-3
       degrees in orientation
 
    4) Positioning each in situ payload element to within 10 mm of a
       science target that has not been previously contacted by another
       in situ instrument
 
    5) Orient each in situ payload element to within 10 degrees of
       normal to a science target&apos;s local surface that has not been
       previously contacted by another in situ instrument
 
    6) After placing the MI in position for imaging, the motion of the
       IDD shall damp down to an amplitude of less than 30 microns
       within 15 seconds
 
 
  Detectors and Electronics
  =========================
    To reduce complexity and cost, all MER cameras share the same
    electronics design. Some aspects of the MER camera design were
    inherited from the cameras built for the Athena Precursor
    Experiment. The MER cameras include a Mitel front-side illuminated,
    frame-transfer charge-coupled device (CCD) with 1024 x 2048 pixels.
    Half of the array is covered by aluminum and is used for image
    storage during readout. Immediately following image integration of
    0 to 335.5 seconds, the image is transferred into the storage area
    in 5.12 msec. Readout of a full image then requires 5.2 seconds,
    after which another integration may begin. The serial register has
    16 extra reference pixels on each end that are read out along with
    each line of data. The reference pixels are not exposed to light and
    therefore measure the bias level as each line of data is read out.
    The value of the last reference pixel is always replaced with the
    camera serial number. Within the operating temperature range of
    218 K to 278 K, the MI has a full well depth in excess of 140,000
    electrons and read noise of about 30 electrons. The gain of the MER
    science cameras (~50 e-/DN) was designed to optimize the 12-bit
    digitization over the expected full well of the CCDs. The video
    offset can be set by command to bias the dynamic range of the CCD
    analog output relative to the range of the analog-to-digital
    converter. After conversion, 12-bit digital image data are sent to
    the rover computer. The non-operating (survival) temperature range
    of the cameras is 163 K to 328 K. The temperature of the MI CCD and
    electronics will not be controlled during flight, so variations in
    performance with Athena Microscopic Imager temperature were
    carefully measured.  Temperature sensors on the MI CCDs and
    electronics will return data for each image obtained, allowing
    temperature calibration to be applied.
 
    Simple image processing tasks can be performed onboard the rovers to
    correct for transfer smear, bad pixels, and flat field variations.
    These processing options can be applied in sequence or one at a
    time. The correction for frame transfer smear, or shutter effect,
    can be applied if the exposure time is less than a given threshold.
    This conditional shutter correction will be very useful in
    conjunction with autoexposure, when the exposure time will not be
    known in advance. If the shutter correction is applied, a
    zero-second exposure is acquired immediately after the image to be
    corrected and subtracted from the original image.
 
 
  Filters
  =======
    The MI has a Schott BG-40 (light blue) filter that yields a spectral
    response similar to that of the human eye.  This restriction of the
    MI bandpass also increases the exposure time needed to image typical
    scenes on Mars and therefore reduces transfer smear.
 
 
  Optics
  ======
    The MI optics employ a fixed focus, f/15 Cooke triplet design that
    provides +/-3 mm depth-of-field at 30 um/pixel sampling. The field
    of view is therefore 31 x 31 mm at the working distance. The focal
    length is 20 mm, and the working distance is 69 mm from the front of
    the lens barrel to the object plane. The first element in the optics
    assembly is a durable sapphire window that is less likely to be
    damaged by windblown debris or inadvertent contact with objects on
    Mars. It is included to protect the rest of the MI optics. The
    object to image distance of 100 mm was selected with instrument
    accommodation as the primary constraint. This design places the MI
    best focus position at approximately the same distance from the IDD
    turret axis as the target position for the other IDD instruments.
    Because the MI has a relatively small depth of field (+/- 3 mm),
    a single MI image of a rough surface will contain both focused and
    unfocused areas.
 
 
  Location
  ========
    The MI is mounted on the IDD turret, between the RAT and the APXS.
