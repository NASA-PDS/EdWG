
 
  Instrument Overview
  ===================
    The principal components of MOLA are a diode-pumped, Nd:YAG laser
    transmitter that emits 1.064 micrometer wavelength laser pulses, a
    0.5 m diameter telescope, a silicon avalanche photodiode detector,
    and a time interval unit with 10 nsec resolution.  When in the
    Mapping Phase of the mission, MOLA provides measurements of the
    topography of Mars within approximately 120 m diameter footprints
    and a center-to-center along-track footprint spacing of 300 m along
    the MGS nadir ground-track.  The elevation measurements are
    quantized with 1.5 m vertical resolution by the 100 MHz timing
    interval unit (TIU) and an interpolator, giving it effectively
    0.375 m resolution.  MOLA profiles are adjusted for orbit and
    pointing errors using 66 million altimetric crossover constraints.
    MOLA profiles are assembled into global planetocentric grids
    referenced to Mars' center-of-mass with an absolute accuracy of
    approximately 1 m.  Standard data products include NASA level 0
    (CODMAC Level 2) corrected telemetry, NASA level 1a (CODMAC Level 3)
    profiles in  engineering and geophysical units, and NASA level 2
    (CODMAC Level 5) maps at various resolutions of planetary shape
    (radius) areoid (equipotential datum surface), topography
    (shape-equipotential), and maps of shot counts per bin. With roughly
    10,000 usable orbital profiles, each with ascending and descending
    equator crossings, mapping resolution is limited mainly by the
    across-track spacing of individual orbits, and by the along-track
    spacing of MOLA footprints.  At 1/32 degree by 1/32 degree per
    pixel, more than one half of all pixels contain at least one
    observation, while higher density occurs at the poles. Products at
    resolutions of up to 128 pixels per degree are available, in
    factor-of-two increments, interpolated where necessary by
    minimum-curvature surfaces under tension [SMITH&WESSEL1990].
    Special products include images of topographic gradients, kilometer-
    and footprint-scale roughness, and a global 0.25 x 0.25 degree grid
    of 1.064 micrometer surface reflectivity.
 
    All major components of MOLA except for the laser and telescope were
    designed, built and tested at NASA's Goddard Space Flight Center,
    Greenbelt, MD.
 
    On June 31, 2001, after firing 670 million shots during 4.5 years of
    the primary and extended missions and undergoing several hundred
    power cycles, MOLA ceased operation as an altimeter. A 100 MHz
    timing oscillator signal, divided down to a 10 Hz interrupt,
    degraded rapidly and then failed.  Laser firing, controlled in
    hardware by the 10 Hz signal, is no longer possible, but the
    receiver electronics are fully operational.  A software patch was
    uplinked that records at high resolution the detector noise counts
    in place of laser data, providing a radiometric signal. The
    background noise counts from the MOLA receiver can be used as a
    radiometric measurement in the 1.064 micron band.
 
    In radiometer mode, MOLA is clocked by 8 Hz interrupts from the
    spacecraft master clock, and the original MOLA 10 Hz interupt has
    been masked.  Flight software sets the receiver threshold every 10
    interrupts, to maintain an approximately constant rate of noise
    triggers. Noise counts are recorded at every interrupt on channels
    1 and 2, and the totals for a half-frame of 10 interrupts are
    stored for all four channels in a compressed (pseudo-log) format.
    The precision  of the measurement is limited by the statistics of
    the approximately 1000 noise counts per shot. Summing channels 1
    and 2 increases precision. Each half-frame constitutes a single
    record with a duration of 1.25 seconds and provides 10 radiometric
    measurements.  The threshold settings and noise counts are
    interpreted radiometrically using an analytical model of the MOLA
    receiver characteristics. This model [SUNETAL1992, SUNETAL2001] has
    been calibrated with respect to preflight test data and in-flight
    experience, as well as similar measurements obtained by the Mars
    Global Surveyor Thermal Emission Spectrometer Bolometer and by the
    Hubble Space Telescope. Precision orbit data describing the
    instrument's position and target location has been added to each
    record. The precision orbit data is supplied by the MOLA Science
    Team.
 
 
  MOLA Science Objectives
  =======================
    The primary MOLA objective is to determine globally the topography
    of Mars at a level suitable for addressing problems in geology and
    geophysics [ZUBERETAL1992, SMITHETAL1998].  Secondary objectives
    include characterizing the 1.064 micrometer wavelength surface
    reflectivity of Mars to contribute to analyses of global surface
    mineralogy and seasonal albedo changes.  Other objectives include
    addressing problems in atmospheric circulation and providing
    geodetic control and topographic context for the assessment of
    possible future Mars landing sites.
 
 
  Instrument Specifications
  =========================
    The following table summarizes MOLA characteristics.
 
    Parameter                          Value            Unit
    ----------------------------------------------------------------
    Physical Characteristics
    Volume                              0.15            m^3
    Mass                               26.18            kg
    Power (TOTAL)                      28.74            W
    Heater Power                       10.00            W
 
    Laser Transmitter
    Laser type                 Q-switched, diode-pumped Nd:YAG*
    Wavelength                         1.064            micrometer
    Laser energy                       40-30            mJ pulse^-1
    Laser power consumption            13.7             W
    Pulse width                        ~8.5             ns (FWHM**)
    Pulse repetition rate              10               sec^-1
    Beam cross-section                 25x25            mm^2
    Beam divergence                    0.25             mrad
 
    Altimeter Receiver
    Telescope type                     Cassegrain
    Mirror composition                 Gold-coated beryllium
    Telescope diameter                 0.5              m
    Focal length                       0.74             m
    Detector type          Silicon avalanche photodiode (Si APD)
    Sensitivity                        1                nW
    Optical filter                     2.2              nm bandpass
    Field of view                     ~0.85             mrad
 
    Receiver Electronics
    Receiver type            Match-filtered leading-edge trigger
    Time resolution                    10               nsec
    Range resolution                   1.5              m
    Pulse energy resolution            20%
 
    Measurements
    Footprint size (@ 400 km)          120              m
    Footprint spacing (@ velocity = 3 km/sec)
   (center-to-center, along-track)   300                m
 
    Computer
    Type                               80C86
    Data rate                          617.14           bits sec^-1
 
    * Nd:YAG is neodymium-doped yttrium aluminum garnet.
    ** FWHM is full width at half maximum.
    ----------------------------------------------------------------
 
 
  Operational Considerations
  ==========================
    The MOLA instrument measures the round-trip time of flight of
    infrared laser pulses transmitted from the MGS spacecraft to the
    martian surface.  The instrument normally operates in a single
    autonomous mode, in which it produces ranging measurements.
    Surface topography estimates can be derived from these data, given
    appropriate corrections for the position and attitude of the
    spacecraft.
 
    MOLA's transmitter is a Q-switched, Nd:YAG laser oscillator which
    is pumped by a 44 bar laser array.  Each bar contains ~1000 AlGaAs
    (Aluminum, Gallium Arsenide) laser diodes.  The Q-switch controls
    the emission of the laser, and Nd:YAG refers to the composition of
    the material that is optically excited to produce laser action:
    Neodymium-doped Yttrium Aluminum Garnet. The laser emits 8.5-ns-wide
    (full width at half the maximum pulse amplitude, FWHM) pulses at
    1.064 micrometers.  The pulse repetition rate is 10 Hz. The
    pulse energy was 45 mJ at the beginning of the Mapping Phase
    and 20 mJ at end of mission.  Energy fluctuated somewhat as
    temperature varied aboard the spacecraft, and dropped several times
    when individual diode bars failed. The remaining diodes appear
    to have been operating at full output when the firing signal
    stopped.  The laser consumed 13.7 W when operating.
 
    The development of a space-qualified, long-lifetime laser represents
    one of the primary engineering challenges associated with MOLA.  For
    comparison, the ruby flashlamp laser altimeters flown on the Apollo
    15, 16 and 17 missions [KAULAETAL1972, KAULAETAL1973, KAULAETAL1974]
    each operated for less than 10^4 laser pulses.  High
    pulse-repetition-rate lasers with lifetimes on the order of 10^9
    shots have been made possible due to breakthroughs in solid-state
    laser technology, resulting in improvements in the peak power,
    brightness, and availability of semiconductor diodes and arrays
    [CROSSETAL1987, BYERETAL1988].  The key technological advance has
    been the replacement of the flashlamp, which is the device that has
    traditionally been used to pump optical energy into the laser rod,
    with a highly efficient array of laser diodes.  While flashlamp
    lasers fail catastrophically, diode-pumped lasers such as MOLA's
    instead undergo a gradual degradation in energy output as individual
    pump diodes fail.  Laser diodes also produce the required pump
    energy only in a narrow region near the laser rod's absorption band,
    which dramatically improves the laser's electrical to optical
    efficiency.

        