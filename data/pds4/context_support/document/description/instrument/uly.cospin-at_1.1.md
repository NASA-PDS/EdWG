
 
 
  (the following descriptions are excerpted from
  [SIMPSONETAL1992A])
 
  Instrument Overview
  ===================
    The ATs sensor unit consists of two, identical charged-
    particle telescopes, each with a geometrical factor of 0.75
    cm^2 sr, whose role is to measure the three-dimensional
    charged-particle distribution in the energy ranges 0.7 to 2.2
    MeV for Z >= 1, 2.2 to 6.5 MeV for protons, and 3.1 to 23.0 MeV
    for Z >= 2.  The three dimensional distribution measurements
    are achieved by inclining the two telescopes at independent
    angles (AT1 at 145[deg.] and AT2 at 60[deg.]) to the spin axis
    of the spacecraft and sectoring (8 sectors) the data outputs of
    the telescopes during each spin.
 
 
  Detectors
  =========
    The AT unit, which is situated at the top of the SIM-1 package,
    comprises two telescopes, each with independent electronics
    systems.  [Each telescope] consists of a stack of three
    semiconductor silicon surface-barrier detectors surrounded by a
    passive aluminum collimator shield which defines the 70 deg.
    full-opening angle of the telescope.  The front detector has a
    nominal thickness of 30 [micro]m and a sensitive area of 2.0
    cm^2, while detectors B and C are each of thickness 300
    [micro]m and have areas of 4.5 cm^2 each.
 
    The exposed surface of the front detector has an evaporated
    layer of aluminium of 60 [micro]m/cm^2 on it to reduce optical
    sensitivity, and has an 8 micron thick foil of aluminized
    kapton over it to eliminate optical effects and provide
    physical protection.  It also eases the thermal balance
    problems of the telescope.  All three detectors are operated at
    depletion voltage plus 50% to minimize radiation damage
    effects.
 
    The C detector is operated in anti-coincidence with the A and B
    detectors and therefore provides active shielding over the
    reverse cone of the telescope.  The forward acceptance cones of
    the telescopes are defined by the passive aluminium collimator
    shield which imposes a minimum low energy cut-off of 20 MeV for
    protons and 1.35 MeV for electrons.  This reduces contamination
    of the energy channels to < 10% for an omni-directional E^-2
    differential spectrum, which is reasonable at these low
    energies.  Should a differential spectrum of E^-1 be observed
    at energies below ~ 100 MeV, a contamination correction may be
    necessary.
 
    Inside the collimator are a series of matt black anodized
    baffles to reduce scattered sunlight and to scatter away
    energetic electrons which could be reflected onto the front
    detector.  The electron and proton responses of the telescope
    are discussed below.
 
 
  Electronics
  ===========
    The outputs of the 3 detectors are combined to define a series
    of energy channels.  There are two specific features that need
    to be commented on.  One is the In-Flight Test Generator (IFTG)
    and the other is the Reconfiguration Logic.  The IFTG can be
    activated by command to produce a series of pulses which check
    the functioning and stability of the discriminator levels via
    the amplifier chain.  It has an automatic switch-off mode as
    well as a commanded-off mode.  The Reconfiguration Logic is
    designed to minimize the effects of possible electronic
    failures during the long time scale of the Ulysses mission, and
    permits some modification of the channel logics.  Since the A1
    discriminator plays a key role in enabling the logic, if it
    should fail its role is automatically assumed by the A2
    discriminator, albeit at the trigger level of A2.  As a part of
    the independent electronics chains, each telescope has an
    independent command-receive system.
 
    The purpose of the digital data system is to organize the data
    suitably prior to it being read into the CPU.  [In] essence,
    during any one spin of spacecraft the data are routed into the
    appropriate one of the eight equiangular sector accumulators,
    and a data sample is composed of an integral number of
    spacecraft spins.  Thus the data-collection time corresponds to
    this integral number of spin periods and is asynchronous with
    the (fixed) telemetry sampling rate.  The data system deals
    with this problem by suitably adjusting the integral number of
    spins per sample period to remain 'in-step' overall with the
    telemetry sampling period.
 
    This system is used to give some of the energy channels both
    spin averaged and sectored outputs.  The sampling times shown
    are the average sampling periods, since the actual sampling
    periods corresponding to an integral number of spin periods.
    The sectoring for the Z >= 2 (3.1 to 7.2 MeV) channel is
    reduced to quadrants to reflect the expected lower counting
    rates at these energies.
 
    After processing by the data system, the data for each
    telescope is routed by its independent interface to one of the
    two processing units in the CPU for processing into the COSPIN
    data format.  In contrast to other data channels in COSPIN,
    each AT is served exclusively by one of the redundant CPUs in
    the DPU.
 
 
  Calibration
  ===========
    The electron response of the front detector of a telescope is
    minimized by the use of a thin detector and a high
    discriminator level (equivalent to 300 keV) for channel A1.
    The 30 micron detector corresponds to an effective range for an
    electron of 66 keV.  The 300 keV discriminator can only be
    triggered by a 5-fold 'pile-up' effect at this energy, or by
    electron 'straggle' effects of electrons of 300 keV.
    Calculation indicates that a 30 micron detector has an
    efficiency of < 10^-3 for 300 keV electrons.  This is
    compatible with electron accelerator tests using 200 to 400 keV
    electrons from the Van de Graaf accelerator at Harwell which
    indicate a detection efficiency of ~ 2 x 10^-5 at these
    energies.
 
    Additional electron accelerator tests have been done on the
    electron accelerator at the Herzberg Institute in Ottawa.
    These were performed at an energy of 65 keV to try to measure
    'pile- up' effects for electrons just coming to rest in the
    front detector.  Interpretation of these results has proved
    complex, and a computer simulation of the electronics system is
    being used to produce a model that relates observed rates to
    actual rates.  This is obviously an important tool for
    interpreting results during the Jupiter fly-by.
 
    To calibrate channels A1 to A4 for particles with Z >= 1, tests
    were done on the IBIS accelerator at AERE, Harwell, which gave
    protons up to 3 MeV.  The minimum beam energy obtainable was
    0.65 Mev.  The 'mid-point' energies of the measured thresholds
    have been used to define the energy ranges given in Table 5.
    The differences between calculated and measured values were
    small and above 2 MeV the measured edge agreed with calculated
    value.
 
    Pre-launch calibration and test of the AT amplifiers was done
    using calibrated test generators, and the amplifiers are
    checked using the IFTG discussed above.
 
 
  In-flight Performance
  =====================
    The instrument performance since switch-on has been good.  The
    highest background counting rate, due to system noise, RTG
    induced counts and the cosmic ray background is in channel 1
    (0.7 to 0.9 MeV, Z >= 1), and corresponds to 0.05 particles
    cm^-2 sr^-1 s^-1 for either AT1 or AT2.  The background rates
    in the other channels are between a factor of 1.7 to 6 less
    than this.  Overall the AT telescopes are providing
    satisfactory performance.
 
    During [a] solar particle event starting on day 296, 1990, once
    particle isotropy had been established, the spin averaged
    counting rates observed by the two telescopes tracked each
    other closely.  Similarly the spin averaged energy spectra and
    sectored counting rates also compared closely.  This is also
    true of the other events observed.
 
    Of more interest is the behavior during the initial stages of
    an event.  Figure 14 shows the sectored counting rates at a
    time when the particle intensity was still rising.  AT2
    (looking sunward, in the direction of the spin axis) saw a
    markedly anisotropic distribution and a significantly higher
    intensity than telescope AT1 (viewing 'backscattered'
    particles) which saw a lower intensity, largely isotropic
    distribution.  For proton spectra derived from a fit to the
    integrated fluxes in the energy ranges of the AT channels,
    neither a power law nor an exponential in energy gives a good
    fit for this event.
 
 
  Measured Parameters
  ===================
    TABLE 5.  Anisotropy telescopes data channels (identical
    channels defined for each telescope).
 
    Name      Primary    Energy   Geometric   Avg. Time   Sectors
    Particle   Range    Factor      Resolution
    Type       (MeV)    (cm^2sr)       (s)
 
    A1        Z>=1       0.7-0.9   0.75         16          --
    A2        Z>=1       0.9-1.3   0.75         16          --
    A3        Z>=1       1.3-2.2   0.75         16          --
    A4        proton     2.2-3.6   0.75         16          --
    A5        proton     3.6-6.5   0.75         16          --
    A38       Z>=2       3.1-7.2   0.75        128          --
    A39       Z>=2       7.2-12    0.75        128          --
    A40       Z>=2       12-23     0.75        128          --
    A6-A13    Z>=1       0.7-1.3   0.75         16           8
    A14-A21   Z>=1       1.3-2.2   0.75         64           8
    A22-A29   proton     2.2-3.6   0.75         64           8
    A30-A37   proton     3.6-6.5   0.75         64           8
    A41-A44   Z>=2       3.1-7.2   0.75        128           4
    A45-A47   --         --        --          128          --
 

        