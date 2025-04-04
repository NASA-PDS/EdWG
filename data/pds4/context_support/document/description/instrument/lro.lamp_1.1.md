
 
 
  INSTRUMENT OVERVIEW
  ===================
    The LAMP description is adapted from Gladstone et al. (2005)
    [GLADSTONEETAL2005] and Gladstone et al. (2008) [GLADSTONEETAL2008].
 
    The Lyman Alpha Mapping Project (LAMP) instrument is one of the remote
    sensing instruments on the Lunar Reconnaissance Orbiter (LRO) spacecraft
    that will acquire orbital observations of the lunar surface during a one
    year primary mapping phase.  LRO is scheduled to launch in April 2009 and
    arrive at the Moon approximately four days later.  Lunar orbit insertion
    will place the spacecraft into a quasi-frozen 30 x 216 kilometer near-
    polar orbit suitable for the commissioning phase, which will last
    approximately 60 days.  At the end of commissioning, final orbit maneuvers
    will insert LRO into the nominal mission orbit, a mean 50 kilometer polar
    orbit in which LRO will remain for at least one year.
 
    LAMP is a far ultraviolet spectrograph provided by the Southwest Research
    Institute (SwRI).  LAMP's nadir observing geometry on the LRO spacecraft
    will translate its 0.3 x 6 degree field of view into a footprint of 0.26 x
    5.2 kilometers on the lunar surface from an altitude of 50 kilometers.
    LAMP will measure the signal reflected from the nightside lunar surface
    and Permanently Shaded Regions (PSRs) using Lyman-alpha sky-glow and UV
    starlight as light sources.  LAMP data will nominally be taken entirely in
    time-tagged mode, allowing mapping at a variety of resolutions.
    Reflectance data will yield albedo maps of PSRs, spectra of PSRs will
    yield exposed water frost abundances, and atmospheric spectra will yield
    species abundances and variability.
 
    The LAMP instrument is closely based on the Pluto Alice (P-Alice)
    instrument design (Stern et al. 2005 [STERNETAL2005]; Slater et al. 2005
    [SLATERETAL2005]; Stern et al. 2008 [STERNETAL2008]), which is, in turn,
    based largely on the Rosetta Alice (R-Alice) instrument design (Stern et
    al. 1998 [STERNETAL1998]; Slater et al. 2001 [SLATERETAL2001]), with only
    relatively minor changes in baffling, software, and the addition of a
    lunar terminator sensor.
 
    SPECIFICATIONS
    --------------
 
    NAME:                    LAMP
    DESCRIPTION:             Ultraviolet Mapping Spectrograph
    PRINCIPAL INVESTIGATOR:  Randy Gladstone, SwRI
    WAVELENGTH RANGE:        57.5 - 196.5 nm (first order) [Note 1]
    FIELD OF VIEW:           (0.31 +/- 0.01) X (6.00 +/- 0.01) deg [Note 1]
    ANGULAR RESOLUTION:      0.29 +/- 0.03 deg per spatial pixel [Note 1]
    WAVELENGTH RESOLUTION:   0.182 +/- 0.001 nm [Note 1]
 
    Note 1:  Measured performance
 
 
  SCIENTIFIC OBJECTIVES
  =====================
    The primary scientific objectives of LAMP are:
 
    1) To generate albedo maps of all PSRs
 
    2) To develop exposed water-frost concentration maps of the lunar polar
    regions
 
 
  CALIBRATION
  ===========
    Ground radiometric characterization and absolute calibration of the
    instrument was performed at SwRI's UV space instrument calibration
    facility located in SwRI's Space Science and Engineering Division.  The
    radiometric vacuum chamber consists of a 4-inch diameter off-axis
    parabolic collimator mirror that is fed by a differentially pumped hollow-
    cathode UV light source and an Acton Research Corporation VM-502 vacuum
    monochromator.  A variable slit and pinhole assembly at the output of the
    monochromator (and situated at the focus of the collimator mirror) allowed
    for point source illumination of the LAMP airglow input apertures.
    Radiometric characterization tests included the detector dark count rate,
    wavelength calibration, spectral and spatial point spread function (PSF)
    versus wavelength, filled slit spectral resolution, off-axis stray light
    attenuation, and absolute effective area measurements as a function of
    wavelength.  See Gladstone et al. (2008) for further details.
 
    During the commissioning phase, the LAMP instrument will be commanded to
    perform five different calibration activities: (1) raster scan star
    calibrations; (2) stare star calibrations; (3) dark count rate
    calibrations; (4) flat field calibrations; and (5) stray light
    calibration.  In addition to these calibration activities, LAMP will
    perform instrument characterizations such as high voltage (HV)
    discriminator setting tests as well as periodic decontamination using
    internal heaters.
 
    During the nominal mission phase, instrument calibrations will be
    performed in conjunction with the monthly station-keeping maneuvers.  For
    LAMP these will include all five types mentioned above for the
    commissioning phase.
 
 
  OPERATIONAL CONSIDERATIONS
  ==========================
    The LAMP instrument will collect measurement data only over the night
    portion of the orbit until minimum mission objectives are satisfied.
    Nominally, LAMP will operate in pixel list (time-tagged photon)
    acquisition mode.  When LRO crosses the lunar terminator (day to night),
    the high voltage (HV) will be ramped up to full operating level.  The
    ramp-up is triggered by the Lunar Terminator Sensor (LTS).  Prior to
    crossing the terminator again (night to day), the HV will be ramped down
    to a safe level by the LTS.  While LAMP is operating over the night
    portion of the orbit, the instrument will generate measurement data at a
    rate of about 30 kbps. The spacecraft will collect and store the data on
    the flight recorder.  The spacecraft will store about 113 minutes' worth
    (one orbit's worth) of measurement data in each data file. After minimum
    mission objectives have been completed, LAMP will operate over the full
    orbit.  A small pin-hole in the aperture door of LAMP allows the
    instrument to operate over the entire orbit.
 
    The LAMP Science Operations Center (SOC) will generate any required
    command activity request.  Activity requests are used to request special
    operations or update command sequences.  During nominal operations, the
    LTS will be used to trigger the high-to-low and low-to-high voltage
    transitions.  As a contingency, the Mission Operations Team (MOT) will
    have the ability to generate the daily command loads that include commands
    to trigger the voltage transitions based on the predicted terminator-
    crossing times generated by the Flight Dynamics Facility (FDF).  This
    procedure will be used, if needed, as a backup to the LTS.
 
    LAMP operations also involve a number of constraints to avoid damage to
    the instrument.  These include keeping the LAMP boresight pointed away
    from the Sun and other designated UV-bright stars, as well as making sure
    that the instrument is in a proper state prior to conducting certain
    operations.
 
 
  DETECTORS
  =========
    The 2-D imaging photon-counting detector located in the spectrograph
    section of the instrument utilizes a microchannel plate (MCP) Z-stack that
    feeds the double-delay line (DDL) readout array.  The input surface of the
    Z-stack is coated with an opaque photocathode of CsI.  The detector body
    tube is a custom design made of a lightweight brazed alumina-Kovar
    structure that is welded to a housing that supports the DDL anode array.
 
    To capture the entire 57.5-196.5 nm passband and 6 degree spatial field of
    view (FOV), the size of the detector's active area is 35 mm (in the
    dispersion direction) by 20 mm (in the spatial dimension), with a pixel
    format of 1024 x 32 pixels.  The 6 degree slit-height is imaged onto the
    central 22 of the detector's 32 spatial channels; the remaining spatial
    channels are used for dark count monitoring.  LAMP's pixel format allows
    Nyquist sampling with a spectral resolution of 0.36 nm, and a spatial
    resolution of ~0.6 degree.
 
    The MCP Z-stack is composed of three 80:1 length-to-diameter MCPs that are
    cylindrically curved with a radius of curvature of 75 mm to match the
    Rowland-circle for optimum focus.  The total Z-stack resistance is ~300
    MOhms. The MCPs are rectangular in format (46 x 30 mm^2), with 12 um
    diameter pores. Above the MCP Z-stack is a repeller grid that is biased
    ~900 V more negative than the top of the MCP Z-stack.  This repeller grid
    reflects electrons liberated in the interstitial regions of the MCP back
    down to the MCP input surface to enhance the detector quantum efficiency.
    The MCP Z-stack requires a high voltage bias of ~-3 kV; an additional -600
    V is required between the MCP Z-stack output and the anode array (the
    anode array is referenced to ground).  The lab-measured dark count rate of
    the flight MCP stack is quite low and stable--less than 6 Hz over the
    entire MCP active area.  The on-orbit dark count rate will likely be
    considerably larger, however, (probably ~20 Hz or so) due to the energetic
    particle environment in space.
 
 
  ELECTRONICS
  ===========
    The detector electronics amplify and convert the detected output pulses
    from the MCP Z-stack to pixel address locations.  Only those analog pulses
    output from the MCP that have amplitudes above a set threshold level are
    processed and converted to pixel address locations.  For each detected and
    processed event, a 10-bit X (spectral) address and a 5-bit Y (spatial)
    address are generated by the detector electronics and sent to the LAMP
    command and data handling (C&DH) electronics for data storage and
    manipulation.  In addition to the pixel address words, the detector
    electronics also digitizes the analog amplitude of the detected event
    output by the preamplifiers and sends this datum to the C&DH electronics.
    Histogramming of this 'pulse-height' information creates a pulse-height
    distribution used to monitor the health and status of the detector during
    operation.  An analog count rate signal is output from the detector
    electronics to the C&DH to allow monitoring and recording of the detector
    total array count rate.  This count rate is updated once per second and is
    included in the LAMP housekeeping data.  A built-in 'stim-pulser' is
    included in the electronics that stimulates photon events at two pixel
    locations on the array.  This pulser can be turned on and off by command
    and allows testing of the entire detector and C&DH electronics signal path
    without having to power on the detector high-voltage power supplies
    (HVPSs) or put light on the detector.
 
    The LAMP instrument support electronics include the low-voltage power
    supply (LVPS) and actuator electronics, the C&DH electronics, the optics
    decontamination heater system, and the redundant detector HVPSs.  All of
    these subsystems are controlled by a radiation-hardened version of the
    Intel 8052 microprocessor with 32 kB of fuse programmable PROM, 128 kB of
    EEPROM, 32 kB of SRAM, and 128 kB of acquisition memory.  The C&DH
    electronics are contained on four circuit boards located just behind the
    detector electronics.
 
 
  OPTICS
  ======
    The LAMP spectrograph comprises a telescope and Rowland-circle
    spectrograph. LAMP has a single 40 x 40 mm^2 entrance aperture that feeds
    light to the telescope section of the instrument.  Entering light is
    collected and focused by an f/3 off-axis paraboloidal (OAP) primary mirror
    at the back end of the telescope section onto the instrument's entrance
    slit.  After passing through the entrance slit, the light falls onto a
    toroidal holographic diffraction grating, which disperses the light onto
    the DDL MCP detector.
 
    The OAP mirror and diffraction grating are constructed from monolithic
    pieces of aluminum, coated with electroless nickel and polished using low-
    scatter polishing techniques.  The aluminum optics, in conjunction with
    the aluminum housing, form an athermal optical design.  Both the OAP
    mirror and the grating are overcoated with sputtered Al/MgF2 for optimum
    reflectivity within LAMP's spectral passband.  Besides using low-scatter
    optics, additional control of internal stray light is achieved using
    internal baffle vanes within both the telescope and spectrograph sections
    of the housing, a holographic diffraction grating that has low scatter and
    near-zero line ghost problems, and an internal housing with alodyned
    aluminum surfaces.  In addition, the zero order baffle is treated with a
    nickel-phosphorus (Ni-P) black coating with very low surface reflectance
    at EUV/FUV wavelengths.
 
 
  OPERATIONAL MODES
  =================
    LAMP has two detector data collection modes: i) pixel list mode; and ii)
    histogram mode.  However, because of its nature and its mission, nearly
    all the LAMP data will be obtained in pixel list mode (exceptions will be
    made for flat-field and pulse-height distribution measurements).  The
    science data from the detector are collected in the dual port acquisition
    memory that consists of two separate 32K x 16-bit memory channels.  In
    pixel list mode each memory channel can hold up to 32K detector and/or
    time-hack events, where each detector event consists of a 16-bit word--an
    X-position word 10 bits in length, a Y-position word 5 bits in length, and
    a single status bit that distinguishes between a time-hack word and a
    detector event word.  A time-hack word includes a single status bit plus
    15 bits that encode the instrument time.  When 32K detector address and
    time-hack events have accumulated in one of the two acquisition memories,
    that acquisition memory stops accumulating event data and begins to read
    the data out to a parallel-to-serial converter and a low-voltage
    differential signaling (LVDS) interface to the spacecraft on-board memory.
    At the same time that this LVDS readout is taking place, the other side of
    the dual acquisition memory continues to collect detector and time-hack
    data until it fills up, whereupon it reads out to the LVDS interface to
    the spacecraft memory, while the first acquisition memory takes over
    collecting detector and time-hack data.  This back-and-forth data
    collection flow between both acquisition memories is called 'ping-pong'
    acquisition--it allows contiguous readout of detector event data as long
    as the event data rate does not exceed the rate at which the data can be
    read out of memory to the LVDS interface.  The 'ping-pong' acquisition
    process is controlled using logic encoded in one of two floating-point
    gate arrays (FPGAs) within the C&DH electronics.
 
    LAMP also includes a flight software mechanism to filter out events from
    selected areas of the detector.  This may be used to suppress 'hot' pixels
    that could develop in the detector, especially in the pixel list mode,
    which might otherwise consume a large fraction of the available
    acquisition memory. This filtering is performed before events are
    processed in either histogram or pixel list mode.  The system defines up
    to 8 rectangular regions of 32 X 4 pixels that suppress any events from
    the selected regions from being processed.  Configuration parameters allow
    for the placement of these filtered areas at any desired positions within
    the detector area.
 
 
  MEASURED PARAMETERS
  ===================
    See the discussion above regarding Operational Modes.

        