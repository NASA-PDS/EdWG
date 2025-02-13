
 
 
  (description excerpted from [SIMPSONETAL1992A])
 
  Instrument Overview
  ===================
    The high energy telescope (HET) is a large geometric factor
    cosmic ray telescope that uses particle trajectory
    determination together with the dE/dX vs.  residual E technique
    to measure the energy and identify the mass and charge of
    cosmic rays.  The HET with its analogue and digital electronics
    forms the largest part of SIM2, with the HFT, mounted on top.
    Detectors D[1]-D[6] provide signals that allow determination of
    the trajectory of the incident particle, and detectors K[1]-
    K[6] provide accurate measurement of the energy loss rates and
    total energy of particles which stop in the K detectors.  For
    particles which stop in the detector stack, the telescope
    provides charge and mass resolution sufficient for studies of
    the chemical and isotopic composition of cosmic rays from
    hydrogen through nickel (1 >= Z >= 28).
 
 
  Scientific Objectives
  =====================
    Through measurements of the intensity and chemical and isotopic
    composition of nucleonic cosmic rays with energies of order 10
    through a few hundred MeV/nucleon, the telescope provides data
    relevant to a number of important questions in heliospheric and
    galactic cosmic ray physics, including acceleration of
    particles in solar flares, the nature of solar modulation, the
    structure of the heliospheric modulation region, the
    characteristics of the interstellar medium, conditions in the
    acceleration region itself, and results of nucleosynthesis in
    supernovae.  In addition, the telescope provides measurements
    of electrons with energies of a few MeV for investigation of
    the propagation of solar and Jovian electrons throughout the
    heliosphere.
 
 
  Detectors
  =========
    Detectors D[1]-D[6] are multi-strip position sensitive Li-
    drifted silicon solid state detectors that measure both the
    energy loss in the detector and the location (by strip number)
    of the cosmic ray trajectory through the detector.  The
    detectors were developed and fabricated at the University of
    Chicago (Lamport et al., Nucl. Instr.  and Meth.  134, 71,
    1976), and are operated at a bias voltage of 35 volts.  The
    electrical contacts on the front surface of the detector
    consist of evaporated gold strips which are individually
    connected to a resistive divider chain on the detector ring,
    one end of which is connected to ground.  On the back surface,
    a single evaporated aluminum contact covers the entire
    sensitive area of the detector.  Thus, two signals are derived
    from each detector.  The signal from the back surface (E
    signal) measures the total energy lost in the detector, while
    the signal from the front surface (P signal) is proportional to
    the location along the resistive divider chain of the strip in
    which the charge was collected.  The position resolution
    achieved by this technique in the individual detectors is
    approximately 150 microns.  With the strips of successive
    detectors (e.g., D[1], D[2], D[3]) rotated by 60 [deg.], the
    trajectory of incident cosmic rays can be determined to an
    accuracy of better than 1 [deg.], as verified by accelerator
    calibration.  Furthermore, use of three detectors in both the
    front (D[1]-D[3]) and back (D[4]-D[6]) planes provides a viable
    position-sensing backup in case one of the detectors fails
    during the mission.
 
    Detectors K[1]-K[6] are thick (nominal 5 mm) Li-drift silicon
    detectors that, in combination, provide approximately 7 g cm^-2
    for stopping incident cosmic rays.  Detectors K[1]-K[6] were
    supplied by the Lawrence Berkely Laboratory, and detectors K[5]
    and K[6] were supplied by the Kevex corporation.  The K[1]-K[6]
    detectors are operated at a bias of 650 volts, which provides
    better than 99.5% charge collection within the amplifier
    shaping time constant of 5 microseconds.  Anticoincidence
    protection for the telescope is provided by a scintillator
    shield (S) surrounding the telescope, and by a solid state
    detector, A, which identifies particles which completely
    penetrate the telescope.
 
 
  Electronics
  ===========
    Signals from the front and back surfaces of D[1]-D[6] and from
    K[1]-K[6] (18 signals in all) are fed through charge-sensitive
    amplifiers and two sets of shaping post-amplifiers.  Signals
    from K[1]-K[6] and the E signals from D[1]-D[6] are fed to a
    fast (1 microsecond shaping time constant) set of amplifiers to
    provide inputs for discriminators which, through the digital
    logic, are used to identify the particle type for counting
    rates and to set logic flags.  In parallel, all 18 detector
    signals are fed to a slower (5 microsecond rise to maximum)
    dual-gain set of amplifiers which provide shaped signals for
    accurate amplitude measurement by the pulse height analysis
    circuitry.  Gains for the dual-gain amplifiers are selected
    based on signal size as determined by discriminators operated
    off the differentiated rise of the charge-sensitive amplifier
    signal.  To maintain the accuracy required for isotopic
    resolution through iron, the amplifiers in the PHA chain have
    been designed for extreme stability, and tests have
    demonstrated a drift in gain of < 0.007%/[deg.]C over the
    temperature range -20[deg.]C to +23[deg.] C.  Gains and
    thresholds are monitored by an in-flight calibration sequence
    which is normally performed monthly, initiated by ground
    command.
 
    If the combination of fired discriminators satisfies one of the
    logic conditions required for pulse-height analysis, output
    from the amplifiers goes to two peak-detector/sample-hold
    circuits that hold the signal amplitudes for processing by two
    4096 channel (12 bit) analogue to digital converters, each of
    which processes 9 of the signals.  Total processing time for a
    complete event is approximately 2 ms.  The pulse height
    analysis data for an individual event consists of 280 bits
    containing the 18 pulse height analyses described above and 64
    flag bits describing the state of discriminators attached to
    the individual detectors, the command state of the instrument,
    and the spin phase, divided into 8 sectors, at the time that
    the event was detected.  Six HET PHA events are recorded during
    each spacecraft telemetry format period, or 32 seconds at the
    nominal bit rate.
 
    Since the actual event rate in the telescope is much higher
    than can be returned as PHA data with the available telemetry,
    the PHA can only sample the events recorded by the telescope.
    To maximize the scientific return from the PHA sample, three
    priority levels have been established to govern selection of
    events for retention in the PHA sample.  The levels correspond,
    roughly, to heavy nuclei which stop in the telescope (P[1]), to
    any particle which stops in the telescope without triggering
    the anti-coincidence after penetrating at least to detector
    D[4] (P[2]), and to any nucleonic particle which triggers
    detectors D[1] and D[2] but not detectors A and S (P[3a]), or,
    with a 50% duty cycle, to any particle which triggers D[1],
    D[2], and D[4] (P[3b]).  P[3b] includes both high energy
    penetrating particles and background events.  P[3] is the
    lowest priority, and any P[3] event can be displaced by a P[2]
    or P[1] event.  Similarly, any P[2] event can be displaced by a
    P[1] event.  In quiet times since turn-on of the HET, about 40%
    of the events have been of type P[3], and of the order of 1%
    have been of type P[1].
 
    In addition to pulse height analysis, the HET provides 29
    digital counting rates.  Of these 13 are derived by logic from
    the discriminators to correspond to electrons, protons, and
    heavy nuclei in well defined energy ranges.  The counting rates
    are true spin averages, with accumulation intervals of an
    integral number of spins, as determined by the software of the
    data processing unit.  Two counting rates provide 8 sectored
    anisotropy information for protons and electrons, while the
    remaining 14 counting rates monitor the counting rates of
    individual detectors as a housekeeping function.  The
    characteristics of the counting rates are more fully described
    in Table 7 (below).  Energy ranges are based on computations
    from range energy tables for nucleons.  All counting rates are
    telemetered to earth in 27 --> 12 bit compressed format.
 
    Because of the duration of the mission, the possibility of a
    detector failure must be considered.  Consequently a number of
    commands have been implemented to allow reconfiguration of the
    telescope logic to compensate for failure of one or more
    detectors.  The telescope logic is fully protected to the
    extent that every term in the logic can be modified in a
    predetermined way by ground command.  In addition, there are
    commands to turn off high voltage supplies, to initiate (and
    turn off) the in- flight calibrate sequence, and to control
    power to three small heaters mounted in the analogue
    electronics of the HET to help maintain a stable thermal
    environment throughout the mission.
 
 
  Calibration
  ===========
    The HET unit now on the Ulysses spacecraft was tested on
    several occasions from 1982 - 1989 using beams of heavy nuclei
    from Ne through Fe accelerated by the Lawrence Berkeley
    Laboratory Bevalac.  The calibration data have been used to
    verify proper function of the telescope, to characterize the
    detector response, and to develop algorithms for selection of
    the data and for determination of mass and charge of incident
    particles by use of the multiple dE/dx vs.  residual E plus
    trajectory information returned by the telescope.
 
    Electron response was investigated over the energy range 3-35
    MeV making use of a linear electron accelerator at the
    University of Chicago Argonne Cancer Hospital.  Electron energy
    ranges were found to be very broad and poorly defined since no
    effort has been made to optimize the telescope for electron
    response.  Some uncertainty remains in the calibration results
    also because of the difficulty of using the accelerator at the
    very low intensities required for our tests.  Further
    experimental work on the electron calibration using the flight
    spare HET is planned.
 
    Response to the RTG radiations was tested using a simulated RTG
    (sRTG) at JPL in 1982 and, immediately before launch, by
    exposure to the flight RTG during the RTG mating test at the
    Kennedy Space Center (KSC).  Initial tests with the sRTG showed
    RTG-induced events in prime HET data channels at intensity
    levels comparable to those expected from galactic cosmic rays.
    After adjustments of discriminator thresholds and modifications
    to the telescope logic the level of interference was shown to
    be markedly reduced by a second exposure to the sRTG.  To
    further reduce background from the RTG's, a 1.6 kg tungsten
    shield was placed between the SIM-1 and SIM-2 units.  The
    configuration and placement of the shield was determined by use
    of Monte-Carlo techniques to provide the maximum shielding
    effect for the allotted tungsten mass given the known locations
    and shapes of the RTG radiation source and the detectors to be
    shielded.  Since detectors D[4] - D[6] are key detectors for
    the HET pulse height analysis priority system and logic and for
    the electron counting rates (H[6] - H[8]), they were chosen as
    the detectors in which the maximum possible reduction in the
    rate of RTG-induced events should be achieved.  Tests at KSC
    and in- flight experience show that the strategy was effective,
    and that RTG-induced events no longer make significant
    contributions to HET data channels except for the H[1] and H[6]
    counting rates, which, during quiet times, respond primarily to
    RTG-induced events.
 
    In flight, an in-flight calibrator (IFC) is commanded on once
    per month.  The IFC provides an exhaustive check of the gains
    and non-linearities of each amplifier by presenting at the
    inputs to the charge sensitive amplifiers a series of 2048
    pulses, timed to the readout cycle, which cover the entire
    dynamic ranges of both the high and low gain amplifiers used in
    the pulse-height analysis.  A normal IFC run consists of two
    passes through the pulse sequence, and requires approximately
    six hours at the nominal cruise telemetry bit rate.  In
    addition, house-keeping channels monitor the regulated voltage
    lines that supply the amplifiers and the detector biases, the
    temperatures of the detectors and electronics, and the zero-
    offset of the digital to analogue converter (DAC) of the IFC.
 
 
  Measured Parameters
  ===================
    Table 7.  High energy telescope data channels.
 
    Name     Prim.   Energy         Geometric  Avg    Sectors  PHA
    Part.   Range          Factor     Time            Priority
    Type    (MeV(/n))      (cm^2sr)   Res(s)
    ---------------------------------------------------------------
    H1       Proton  5.4-14         94          16      --     none
    H2       Proton  14-19          87          16      --     P3
    H3       Proton  24-31          16.2-14.9   16      --     P3
    H4       Proton  34-68          8.2-5.5     16      --     P2
    H5       Proton  68-92          5.2-3.6     16      --     P2
    H6       Elec.   ~1-3           87          16      --     P3
    H7       Elec.   ~5-10          8.2-5.5     16      --     P2
    H8       Elec.   ~3-5           16.2-14.9   16      --     P3
    H9       Proton   >92           3.6         16      --     P2
    H10      Z>=3     26-36(^12C)   87         128      --     P2
    H11      Z>=3     44-127(^12C)  16.2-5.5   128      --     P1
    H12      Z>=3     127-173(^12C) 5.2-3.6    128      --     P1
    H13      Z>=3     >173(^12C)    3.6         64      --     P1
    H45S     Proton   34-92         8.2-3.6    128       8     P2
    H7S      Elec.    ~5-10         8.2-5.5    128       8     P2
    H14-H19  --       --            --         128      --     --
    H20-H25  --       --            --         128      --     --
    H26,H27  --       --            --         128      --     --
 
  References
  ==========
    Lamport J.E., Mason G.M., Perkins M.A.  and Tuzzolino A.J.,
    Nucl. Instr.  and Meth.  134, 71, 1976.
 

        