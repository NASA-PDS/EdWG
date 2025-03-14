
 
  Instrument Overview
  ===================
    The SHAllow RADar instrument (SHARAD) is the sub-surface sounding
    radar provided by the Italian Space Agency (ASI) as one of six
    science instruments onboard NASA's 2005 Mars Reconnaissance Orbiter
    (MRO). SHARAD is a wideband radar sounder that operates on a 20 MHz
    central frequency with a 10 MHz bandwidth and transmits frequency-
    modulated radar pulses of about 85 microseconds in length.
 
    SHARAD is designed to create subsurface profiles with
    approximately 10 to 20 m vertical resolution (15 m in free space),
    300 to 1000 m along-track resolution, and 1500 to 8000 m across-track
    resolution, depending on spacecraft altitude and terrain roughness.
    Radar penetration depends on the dielectric properties of subsurface
    materials, and is estimated from several hundred meters up to 1 km
    for the range of dielectric properties of expected Martian rocks.
 
    Information in this instrument description is taken from the
    SHARAD mission paper [SEUETAL2007]. See this paper for more details.
 
 
  Scientific Objectives
  =====================
    The chief scientific objectives of SHARAD are:
 
    1) to map dielectric interfaces in the Martian subsurface to depths
    up to one kilometer,
 
    2) to interpret these interfaces in terms of the occurrence and
    distribution of expected materials, including rock, regolith, water,
    and ice, and
 
    3) to determine the 3-D distribution and state of subsurface H2O.
 
 
  Subsystems
  =====================
    SHARAD has three major subsystems: Antenna S/S, RF S/S, and Digital
    S/S.
 
    1) The Antenna S/S is a dipole radiating element with a length about
    half the wavelength of the carrier frequency.
 
    2) The RF S/S includes the transmitter, Tx/Rx switching net, and
    receiver down to the Analog-to-Digital Converter.
 
    3) The Digital S/S includes the command and control functions,
    interfacing with the spacecraft bus, and the processing capabilities
    for digital synthesis of the radar pulse and generation of system
    timings.
 
 
  Detectors
  =====================
    SHARAD's antenna is a 10-m dipole made of two 5-m foldable tubes,
    which, in stowed configuration, are kept in place by a system of
    cradles, and, when released, self-deploy because of their elastic
    properties. Electrically, the antenna is fed at the center,
    interfacing with the SEB by means of two wires (one for each
    dipole). The connected wires together form a balanced connection
    line. The line itself has no controlled impedance, and the load seen
    on the TFE side is therefore frequency dependent, requiring
    frequency compensation within the TFE.
 
    The antenna also includes its release mechanism (two solenoid
    controlled actuators to release the right and left dipoles). During
    deployment operations, heaters installed on the spacecraft panel
    will heat the antenna cradle hinges in order to keep the actuator
    mechanism within suitable temperature range.
 
 
  Electronics
  =====================
    SHARAD's Electronics Box (SEB) includes all of the transceiver
    electronics and the signal processing and control functions. It is
    made of two separate electronic assemblies, mounted on a support
    structure that acts as radiator for thermal control and includes the
    heaters and temperature sensors. The two electronic assemblies are:
 
    1) The Receiver and Digital Section (RDS) includes the Digital
    Electronic Section (DES), which includes the Digital Signal
    Processor (DSP) Module (Command and Control Board and Slave board),
    Service Module (Timing Board and DC/DC Converter board), and the
    Digital Chirp Generator (DCG) Module (DCG Board). The DES is
    responsible for most of SHARAD's functions, including:
 
    a) Command and control capability
    b) Formatting of science data and their transfer as telemetry to
       the spacecraft's solid state recorder (SSR)
    c) Generation of housekeeping telemetry and its transfer to the
       spacecraft's SSR
    d) Generation of the radar chirp signal
    e) Processing of the raw radar data
    f) Provision of a high-stability oscillator and generation of
    timekeeping and synchronization signals for all SHARAD units
    g) Power conditioning and distribution to the other SHARAD units
 
    The Digital Chirp Generator (DCG) synthesizes chirp signals in the
    DES using the Direct Digital Synthesis Technique: it generates
    discrete samples of a sine wave at different frequencies and
    reconstructs the desired waveform at the analog level. The DCG uses
    a Numerical Controlled Oscillator (NCO) to do this, which features:
 
    a) 32-bit frequency resolution (0.018 Hz @ 80 MHz clock)
    b) 0-32 MHz @ 80 MHz clock bandwidth
    c) 10-bit chirp signal generator
    d) Micron Processor Compatible input (16 bits Bus Address and 16 bits
       Bus Data)
    e) 520 mW @ 80 MHz power dissipation
    f) Automatic download of external look-up table PROM content
    g) All parameters previously configured (start frequency, frequency
       slope, phase compensation, pulse duration)
 
    The RDS also includes the Receiver (Rx), which amplifies, filters,
    and digitizes the received signal.
 
    2) The Transmitter and Front End (TFE) amplifies the low-level chirp
    signals coming from the DES and couples them to the dipole antenna.
    The TFE also manages sharing the antenna between the transmitter and
    the receiver path. It also includes an internal DC/DC converter to
    supply all internal circuitry.
 
 
  Operational Modes
  =====================
    Operational (or Measurement) Modes correspond to the different
    actions that the instrument may perform under the guidance of the
    Operation Sequence Table (OST). Each OST entry specifies details for
    the transition to, and the execution of, a given Operational Mode.
    Telemetry is always generated during Operational Modes and
    monitoring is active. In case of other error or anomalies during
    Operational Modes processing, an automatic transition is performed
    to Safe/Idle State.
 
    SHARAD can operate in one of four modes:
 
    1) Subsurface Sounding Mode (SS) is the main measurement mode for
    SHARAD. In this Mode the instrument performs scientific measurements
    by transmitting radar pulses and collecting, processing and
    formatting received echoes. Pulse repetition interval and duration
    are variable depending on parameters specified in each OST entry. A
    variable Science Data rate is produced in this Mode depending on the
    specific processing parameters.
 
    2) Receive Only (RO) Mode is used to perform passive measurements
    mainly during the on-orbit phase, but can also be used to check the
    performances of the instrument during the cruise phase (even with
    the antenna folded). No transmissions will be performed. A variable
    Science Data rate will be produced in this Mode depending on the
    specific processing parameters.
 
    3) Calibration Mode is used to perform instrument calibrations
    during the on-orbit phase.
 
    4) Test Mode is a debug mode used to generate a stream of science
    data simulating an instrument operational mode, to exercise all
    internal functions of the instrument. Data produced using these two
    Operational Modes have no scientific value and will not be used to
    produce EDR data products.
 
  Calibration
  ===========
    Before flight, the ground calibration checked the transmitter and
    receiver chain parameters, the reference oscillator parameters, the
    antenna radiation pattern, and the end-to-end parameters.
 
    During the Transition Orbit, SHARAD's antenna was both passively and
    actively calibrated. Both methods assumed that the spacecraft
    configuration does not affect the shape of the antenna pattern in
    the section of interest (+ 10 degrees pitch, + 20 degrees roll, with
    referenced to the nadir), but only its absolute amplitude.
 
    During Primary Science Orbit, SHARAD has undergone a number of
    calibrations. The best approach to calibration is to observe the
    same local and minimize scene dependence of the calibration.
    Calibration is complicated by the fact that it is difficult to fully
    characterize the antenna pattern due to the varying backscattering
    properties of the surface. Only a limited number of orbits can be
    devoted solely to this task during the science data collection
    phase.
 
 
  Operational Considerations
  ==========================
    SHARAD is able to operate at any time while the MRO spacecraft is
    orbiting Mars, regardless of solar illumination conditions.
    Constraints are a result of tradeoffs among the various instruments
    on board. The data volume for SHARAD is limited by the MRO
    allocation of 15% of its total data, which typically ranges from 40
    to 90 Gb/day. SHARAD is fundamentally a nadir-pointing instrument,
    though it can still acquire good data up to 10 degrees off-nadir.
 
    SHARAD has considerable freedom in both its preprocessing parameters
    and its data production rate (300 kbps to >20 Mbps, depending on the
    pulse repetition frequency, presuming strategy, and number of bits
    per sample).

        