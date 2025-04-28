
 
 
  Instrument Overview
  ===================
 
  Lidar
  -----
    The Phoenix mission to Mars [SMITHETAL2008] will advance our knowledge of
    the climate on Mars by combining lidar remote sensing of atmospheric dust
    and clouds with measurements of solar radiation [LEMMON2008] and in situ
    sampling of temperature, pressure, wind [TAYLOR2008], and water vapour.
    The day to day variation of the local weather on Mars is
    controlled primarily by the amount of solar radiation reaching the surface
    and this depends on the optical thickness of the dust suspended in the
    atmosphere. This affects local and global meteorological patterns which in
    turn determine the lifting of dust from the surface and long range
    transport [LEOVY2001; NEWMAN2002]. There is also a climate interaction
    with the distribution of water ice above and below the surface of Mars
    [BOYNTON2002, PATHAK2008]. This involves transport of water through the
    atmosphere and previous lidar measurements from orbit have indicated that
    clouds could have a substantial role [NEUMANN2003].
 
    The lidar on the Phoenix mission will record the height profile of laser
    backscatter from the dust and cloud layers that drift past the landing
    site with a view that is continuous in time. The attenuation of the lidar
    signal can be used to derive the optical extinction coefficient and this
    is related to atmospheric properties. For example, the extinction of solar
    radiation due to dust has a first order effect on heating of the surface
    of Mars. The measured optical extinction can also be related to the amount
    of scattering material. For example, for a thin cloud the extinction
    coefficient measured by a lidar can be used to derive the ice water
    content within the cloud [HEYMSFIELD2005]. Such a measurement will be of
    vital importance to the mission goal to investigate water on Mars. The
    combination of the lidar and passive remote sensing with in situ sampling
    will provide a view of the interacting processes that determine the local
    weather at the surface and also the role of the atmosphere in the water
    cycle on Mars.
 
    A basic atmospheric lidar (light detection and ranging) emits pulses of
    laser light into the atmosphere then detects and records the backscattered
    light as a function of time [MEASURES1984]. The time resolved signal is
    converted to distance using the speed of light and a factor of two to
    account for the round-trip path length.
 
    The lidar transmitter is based on a diode pumped, passively Q-switched,
    neodymium-doped yttrium garnet (Nd:YAG) laser. This configuration was
    chosen for its robustness and technological maturity as much as for its
    suitable lidar performance. The pump diode array emits at a wavelength of
    808 nm and is used to provide the energy to the Nd:YAG crystal within the
    laser cavity. Lasing is inhibited within the cavity through the use of a
    saturable absorber. The photon density within the oscillator cavity builds
    to a level where the saturable absorber bleaches and the energy within the
    cavity is dumped as a laser pulse over a very short time (a passive
    Q-switch). For this laser the output light pulse has a length of
    approximately 10 ns and an energy of 0.7 mJ.
 
    After the laser cavity emits its light pulse, part of the optical energy
    is converted from a wavelength of 1064 nm to 532 nm by second harmonic
    generation in a Potassium Titanyl Phosphate (KTP) crystal. The laser
    output is then expanded by a factor of 10 in order to reduce the
    divergence to 0.5 mrad. A small fraction of the outgoing laser pulse is
    'picked off' and separated into the two wavelength components in order to
    measure the relative amplitude of each wavelength with photodiodes. The
    signal from the photodiode detecting the 1064 nm pulse is used to trigger
    the data acquisition electronics, providing a zero-time reference, and
    also to shut off the pumping diodes.
 
    The atmospheric backscatter signals are collected by an afocal reflective
    telescope and split into the two relevant wavelengths using dichroic
    mirrors. The 1064 nm backscatter is detected by an Avalanche Photo-Diode
    (APD), and recorded using 14-bit analog to digital conversion (ADC). The
    532 nm backscatter is detected by a Photomultiplier (PMT) and the signal
    is recorded using both ADC and photon counting. Photon counting is
    required to record the weak signals from heights above 5 km and up to
    20 km.
 
  Scientific Objectives
  =====================
 
    The main objective of the Lidar is to measure the vertical distribution of
    scattering particles (both dust and clouds) in the Martian atmosphere.
    These measurements are expected to provide estimates of:
 
    * Martian ice cloud base heights and cloud thickness (for optical thick
      but spatially thin clouds)
    * Diurnal variation of surface ice fogs
    * Diurnal variation of the boundary layer height
    * Variation of vertical dust structure owing to local weather conditions.
 
 
  Location
  ========
 
    The Phoenix Mars Lander arrived at 68.2184N, 234.2487E on May 25, 2008.
 
 
  Operational Modes and Measured Parameters
  =========================================
 
    The signal as a function of height is integrated over a set number of
    laser pulses and height bins. For example the standard operating mode is
    to use 50m vertical resolution (ten 5-meter bins averaged) and 20.48
    second temporal resolution (1000 laser pulses averaged) for the Photon
    Counting Channel, and 10m, 20.48 sec resolution, respectively, for the two
    Analog Channels. These profiles are then stored sequentially within a
    data file. Typical operational times are 15min, with the expectation that
    this will be increased whenever power and data volume permit. The
    observable range is 0-20km for the photon counting, and 0-10km for the
    analog data, though it is possible to slide the observation window up
    (e.g. 1-21km) using a timing offset parameter.  The temporal and spatial
    averaging are parameters that are part of the commands transmitted from
    the ground station during the mission.  Owing to the flexibility in these
    parameters, there are no set operational 'modes' other than the 'default'
    outlined here.
 
    Each vertical/temporal bin represents the total number of measured photons
    (i.e. counts) for the Photon Counting Channel, and the average voltage for
    the 532nm and 1064nm Analog Channels.  The voltages are sampled at an
    effective range of 13 bits, with the sum for each spatial/temporal bin
    being stored at 32 bits before transmission to Ground. Subsequent
    processing converts this sum into an average in Volts: that is the average
    Voltage per shot and per 2.5m vertical bin (the highest possible
    resolution) for the purposes of inter-comparison.  The cumulative Photon
    Counts are left unprocessed.
 
    Laser Power data are also provided as a relative measure of the
    transmitted laser intensity, and comparison with zenith pointing SSI
    images may provide an estimate of the receiver efficiency.
 
 
  Verification and Calibration
  ============================
 
    Verification that the Phoenix lidar will function on Mars was achieved by
    operating it within a thermal vacuum (T-vac) chamber at the pressures and
    temperatures expected on the surface of Mars (e.g. 8 Torr, -70C). A window
    was installed in the T-vac chamber so that the output laser pulses and the
    receiver field of view could be directed across the clean room and through
    another window into the atmosphere in the zenith direction. Atmospheric
    observations could then be acquired and compared with simultaneous
    measurements with another lidar system.
 
    The lidar used for side-by-side comparison in testing was supplied by York
    University (referred to as the York Lidar).  This has the same essential
    characteristics as the Phoenix Lidar. For example, the transmitted
    wavelengths are the same (1064 nm and 532 nm), and the same detectors are
    applied in the receiver. The data acquisition electronics provide the same
    function as in the Phoenix lidar: analog to digital conversion (ADC) at
    1064 nm; both ADC and photon counting at 532 nm. The main difference is
    that the York Lidar has a more powerful laser than the Phoenix lidar.
 
    An important part of the testing was to ensure that the receiver and
    transmitter remain aligned over the full range of temperatures that are
    expected during the mission. The temperature within the lidar is
    controlled by heaters and the coldest it will get during the mission is
    -40C. The heat dissipated by the laser while operating will increase the
    temperature of the instrument by about +3C over a 15 minute interval. The
    baseline plan is to have the lidar operate for four separate 15 minute
    intervals at mid-day, evening, midnight and morning. In this scenario the
    temperature of the lidar chassis in not expected to rise above -20C. If
    the lidar is run for longer periods and more often, then the lidar chassis
    will get warmer. The alignment of the transmitter was optimized so that it
    was pointing within the receiver telescope FOV over a temperature range of
    -40C to -10C on the lidar chassis.
 
    The direction of the transmitted laser light relative to the receiver
    telescope field of view (FOV) was determined by deflecting the transmitted
    light with a variable optical wedge. The direction of the transmitted
    light was deflected until the atmospheric backscatter signal at a height
    of 1.5 km started to decrease and this was done in the four cardinal
    directions. The outline of the FOV could then be determined relative to
    the transmitter output. This was done at various temperatures between -40C
    and 0C. It was determined that the relative angle between the transmitted
    light pulse and the receiver telescope FOV axis changed by 0.9 mrad over
    the temperature range from -40oC to 0oC, moving inward toward the
    telescope axis as the temperature increased. The transmitted light pulse
    has a divergence of 0.5 mrad, so there is 1 mrad of tolerance within the
    1.5 mrad FOV to account for temperature variations. Thus it was possible
    to optimize the alignment of the system so that the transmitter is
    pointing within the FOV over the range of temperature from -40oC to 0C.
    This was done so that at -40C the transmitter output is pointing 0.4 mrad
    away from the central axis of the receiver telescope FOV. It is still
    within the full 1.5 mrad of the FOV, with a 0.1 mrad tolerance between the
    outside edge of the transmitted laser pulse and the edge of the FOV. At a
    temperature of 0C the transmitter was pointing 0.5 mrad toward the
    receiver telescope.
 
    The alignment of the Phoenix lidar in Mars conditions was verified by
    direct comparison to the York Lidar with simultaneous atmospheric
    measurements. An example of a comparison between the York lidar and
    Phoenix lidar with photon counting signal acquisition is shown in Fig. 4.
    The Phoenix lidar was in the T-vac chamber with 8 Torr of CO2 at a
    temperature of -70C, and the lidar chassis temperature was -36C. The ratio
    of the signals from the two lidars is constant with height up to above 15
    km and this is an indication that the Phoenix lidar transmitter is aligned
    within the receiver field of view. Another indication that the system is
    properly aligned is in the comparison with the expected signal from
    molecular backscatter. There is an enhancement in the signal between
    heights of 8.5 km and 10.5 km due to a cirrus cloud layer. There is also a
    thin cloud at a height of 1.5 km. It is expected that such thin ice clouds
    will be detected in the atmosphere of Mars [PATHAK2007]. Below a height of
    2 km there is a reduction in the signals recorded with both lidars in
    comparison with the expected molecular backscatter signal. This is a well
    known effect: the photon counting saturates due to electrical pulse
    overlap at count rates greater than 10 MHz. This well known nonlinear
    effect in photon counting has been characterized and can be corrected when
    there is not substantial variability within the averaging period. However,
    there is no saturation in the signal recorded by analog to digital
    conversion.
 
    The ratio of the Phoenix Lidar to the York Lidar signals was found to be
    constant with height above about 400m.  A difference below 400 m is owing
    to incomplete overlap between the outgoing laser pulse and the receiver
    FOV. This is consistent with the geometry of the system: the 12 cm
    separation between the telescope axis and the transmitter output, the 1.5
    mrad FOV, the 0.5 mrad divergence, and the 0.1 mrad tilt of the
    transmitter output away from the telescope axis that occurs at a chassis
    temperature of -30C. There is complete overlap at this temperature above
    400 m. Plots of this can be found in [WHITEWAY2008].

        