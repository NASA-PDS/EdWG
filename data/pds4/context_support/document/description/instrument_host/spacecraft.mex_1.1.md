
 
 
  Instrument Host Overview
  ========================
    Data obtained from the Mars Express instruments were send to
    ground via the spacecraft on-board computer. As spacecraft to
    Earth communication does typically exclude instrument operations,
    all data are relayed from the instrument to the spacecraft mass
    memory, the solid state mass memory (SSMM). The data was
    downlinked to Earth via the telemetry subsystem using ESA's
    antenna in New Norcia, Australia, and the Deep Space Network (DSN)
    antennas of NASA. The radio science experiment required data from
    the New Norcia and the DSN ground station hardware. This catalogue
    file gives an overview of the spacecraft and the ground stations
    used. For more detailed information see the spacecraft user
    manual, MEX-MMT-MA-1091.
 
 
  Instrument Host Overview - Spacecraft
  =====================================
    The spacecraft baseline design was the combination of mission
    customised configuration and mechanical / thermal architecture
    with a Rosetta inherited avionics. The spacecraft design was
    driven by mission requirements, science return  and system
    concept. A spacecraft articulation concept with body mounted
    instruments, fixed High Gain Antenna and 1 degree of freedom
    steerable Solar Arrays was baselined. The spacecraft design was
    based on a parallelipedic like shape sizing  about 1.7 m length,
    1.7 m width and 1.4 m height. The solar array was composed of two
    wings, providing a symmetrical configuration favourable to
    aerobraking  techniques and minimising torques and forces applied
    on the arrays and the drive mechanisms during the Mars insertion
    manoeuvres performed with the main engine. So as to offer the
    adequate dry mass / propellant mass ratio and large mounting
    surfaces and volumes for the Orbiter instruments necessary for
    Mars Express, the traditional cone/cylinder central structure has
    been found less efficient than a dedicated structural concept with
    only a Launch Vehicle Adapter connected to a stiffened 'box' as
    now developed for light weight satellites. Within the overall
    integrated design of the spacecraft, four main assemblies are
    planned to simplify the development and integration process:
    (1) the Propulsion Module with the core structure,
    (2) the Y lateral walls, supporting the spacecraft avionics and the
        solar arrays,
    (3) the Y/+X shear wall and the lower and upper floors, supporting
        the payload  units. The +Zb face was nominally Nadir pointed
        during science observation and Lander communication relay phases
        around Mars, and supported Beagle 2 (released prior to Mars
        capture) the Lander(s) relay antenna and ASPERA-3, and
    (4) the X lateral walls supporting the High Gain Antenna (-X) and
        the instruments radiators (-X).
 
    Attitude and Orbit Control was achieved using a set of star
    sensors, gyros, accelerometers and reaction wheels. A bi-
    propellant reaction control system was used for orbit and attitude
    manoeuvres by either a 400 N main engine or banks of 10N
    thrusters. The Data Handling is based on packet telemetry and
    telecommand. The Electrical Power generation was performed by
    solar arrays, the power storage by a Lithium-Ion battery. A
    standard 28 V regulated main bus is offered to the payload
    instruments. The RF Communications function transmitted X Band
    telemetry 8 hours per day via a High Gain Antenna at rates between
    about 19 and 230 kbps depending of the Mars to Earth Distance. A
    variable telecommand rate of 7.81 to 2000 bps was foreseen during
    up to 8 hour per day.
 
 
  Spacecraft Coordinate System
  ----------------------------
    The origin of the spacecraft Reference Frame, named Oa, was located
    at the separation plane between the spacecraft and the adapter, at
    the centre of the interface diameter of 937 mm.
    -  The Xa axis was contained in the spacecraft/launch vehicle
       separation plane, and oriented toward the High Gain Antenna side
       of the spacecraft.
    -  The Za axis was coincident with the launcher X1-axis. It
       represents the SC line of sight toward Mars during science
       operation, and the ejection direction for the Beagle 2 probe.
    -  The Ya axis was contained in the SC/LV separation plane, and
       oriented so as to complete the right handed co-ordinate system.
       It is therefore parallel to the solar array plane and positively
       oriented opposite to Marsis antenna support wall.
 
    The (Ob, Xb, Yb, Zb) Reference Frame is structure related, and is
    not used at S/C or operations level.
 
    Spacecraft Structure and Interface With Payload Units
    -----------------------------------------------------
    The selected SC structure limits the number of complex elements to
    the bare minimum. Indeed, the only cylindrical part of large
    dimensions was the Launch Vehicle Adapter ring, the rest of the
    structural items being principally flat, standard panels with
    aluminium skins and aluminium honeycomb. The structure was composed
    of:
    1) a Core Structure, built up from :
     - One Launch Vehicle Adapter ring machined from a solid aluminium
       cylinder of approx. diameter 940 mm, 200 mm height with a
       thickness of 3.5 mm. This LVA was the main load path transfer
       from the Spacecraft body to the launch vehicle interface.
     - Two Tank Beams supporting the lower tank bosses, and embedded in
       the LVA ring,
     - Two Upper Tank Floors, supporting the tanks upper bosses,
     - One Lower Floor.
     - Two X Shear Walls,
     - One Shear Walls in the Y direction
 
    2) an Outer Structure, built up from :
     - a +Z Top Floor,
     - two +Y and -Y Sidewalls,
     - two +X and -X Lateral Closure Panels (split to allow separate
       access into each quadrant),
     - various dedicated equipment support panels (PFS, Omega and
       pressurant tank)
     - miscellaneous brackets (e.g. to support sensors, antennas,
       propulsion items, instruments).
 
    All these elements were made of Aluminium Alloy, either from
    forgings (LVA ring, tank beams and main brackets) or from
    honeycomb sandwich panels. The panels were made of honeycomb
    (generally type 1/8-5056- 0.001P) of 10 to 20 mm thickness, bonded
    to Aluminium facesheets of thickness varying between 0.2 to 0.3 mm
    and up to 0.5mm additional doubler for local reinforcements.
 
    In general, the payload units were accommodated following their
    main     needs. The payloads needing a stringent thermal control
    and/or pointing performances (HRSC, OMEGA, PFS, SPICAM) were
    gathered on, or close to, the +X shear wall, inside the spacecraft
    and close to the AOCS reference (namely the Inertial Measurement
    Package and the Star Sensors). In order to meet the PFS scanner to
    PFS sensor co-alignment without disturbance caused by dismounting,
    these PFS units were installed on a stiff, removable mounting
    assembly which can be integrated as a single unit on the
    spacecraft. To expedite installation of the large Omega-SA, this
    instrument was installed via edge-mounted inserts in the Y-shear
    wall and a dedicated Omega support panel. The payloads requiring a
    large field of view and not necessitating stringent thermal
    control were located externally on the Top and Bottom Floors
    (ASPERA) or lower edge of the +Y sidewall (MARSIS). None of the
    payload units required isostatic mountings: they were rigidly
    fixed to the spacecraft structure utilising standard space-
    industry inserts and screws. Some of the payload units were of
    significant mass and therefore require the implementation of
    large, face-to-face inserts that are bonded inside the sandwich
    panels at the time of panel moulding. Beagle 2 was accommodated on
    the top floor of the S/C, in order to minimise dynamic disturbance
    (centre of mass transfer in the (X, Y) plane) and then maximise
    the reliability of the Mars orbit insertion manoeuvre. The
    remaining Beagle 2 hardware after probe ejection is constrained
    within 50 mm height and is thermally insulated to minimise
    straylight and thermal distortion disturbances respectively.
 
  Thermal Control
  ---------------
    The spacecraft thermal control was in charge of maintaining all
    spacecraft equipment within their allowed temperature ranges
    during all mission phases. The equipments fall into two
    categories: - the collectively controlled units, for which the
    heat rejection and heating capabilities (design and accommodation)
    are provided by the spacecraft thermal control, - the individually
    controlled units, self provided with their own thermal control
    features (coatings selection, heaters, insulators), for which the
    spacecraft thermal design controls the thermal interfaces within
    the required ranges.
 
    A passive thermal control design was implemented for the Mars
    Express     spacecraft; it was supplemented with an electrical
    heating system. The heat rejection toward space was performed
    using radiators mainly on the +/-Y panels for the platform
    internal units and the +X panel for the payload equipments. These
    sides of the spacecraft are the most favourable areas, being most
    of the time protected from the direct sun inputs (always for the
    +X side). The Mars planet flux are imposed by the spacecraft orbit
    and attitude and mainly significant during the pericentre phase in
    operation. The rest of the spacecraft is insulated with Multi
    Layer Insulation blankets to minimise the heat exchange and the
    temperature fluctuations.
 
    The spacecraft external units (Platform and Payload units) were
    thermally decoupled from the spacecraft and provided with their
    individual radiator when needed. The electrical heater system
    allowed to raise the temperature of the unit above their minimum
    allowed limits, with temperature regulation functions provided
    either by mechanical device or by the onboard software. Most of
    the spacecraft units were collectively controlled inside defined
    thermal enclosures in which the heat balances were controlled by
    proper sizing of heat rejecting radiators and heating power
    implementation. It allowed to maintain the unit temperatures to
    acceptable levels. The heat transfer from the units to the
    radiators was performed by conduction when unit baseplates were
    attached to the radiator honeycomb panels and by radiation. In
    that case units and panels had a black finish to maximise heat
    transfer inside the thermal enclosures. For more demanding units
    like the HRSC and OMEGA cameras, and the PFS spectrometer,
    featuring their own thermal control, special precautions were
    taken by individual trimming of their conductive and radiative
    isolation. The HRSC camera required a temperature control within a
    narrow temperature range): it was provided with a thermal strap
    connecting it to a dedicated radiator tuned to limit the
    temperature excursion in operation within a 10 degree C
    temperature range. OMEGA and PFS are provided with dedicated
    radiators, implemented on the +X side of the Spacecraft. Whatever
    the Sun / Earth / Mars / Spacecraft geometry, the +X side of the
    Spacecraft was oriented away from Sun over the complete Martian
    orbit, both during Nadir pointed science phase and Earth pointed
    communication phase. This allowed to provide the camera and the
    spectrometer with a thermal interface at temperature lower than
    175K and 190K respectively during the Planet observation. The
    connection to the radiators were performed by thermal straps, the
    radiators being themselves decoupled from the rest of the
    spacecraft using thermal blankets and insulating stand-offs.
 
    Payload external units like MARSIS and MELACOM antennas, ASPERA-3
    units, were individually controlled units. They required large
    field of view and thus were directly affected by the external
    environment and they had to withstand larger temperature ranges
    than the standard units. They are as far as possible insulated
    from the spacecraft. Their coatings were selected and trimmed to
    suit. The spacecraft interface temperature had a very limited
    influence on their thermal behaviour. The propulsion equipments
    that were mounted internally were in general isolated with MLI,
    and provided with their own thermal control heaters: tanks, fluid
    lines, valves, pressure sensors. The main engine and the thrusters
    had their thermal coupling with the spacecraft tailored to meet
    their thermal requirement while preserving the spacecraft thermal
    behaviour. They were provided with individual electrical heaters
    sized to maintain these external units within the acceptable
    temperature range accounting for wide change in radiative
    environment. The High Gain Antenna was using a passive thermal
    control: a Kapton/Germanium sunshield was covering the whole
    antenna on its front side, while a light weight MLI is used on the
    rear side of the reflector.
 
 
  MECHANISMS
  ----------
    The implementation of mechanisms into the spacecraft configuration
    had been kept to the minimum. The mechanisms employed are those
    associated with
    - Reaction Wheel Assembly (RWA),
    - Solar Array Drive Mechanism (SADM),
    - Solar Array Hold-Down and Release Mechanism (HDRM),
    - Solar Array Deployment System,
    - Beagle-2 Spin-Up and Ejection Mechanism (SUEM) and the
    - MARSIS antennas deployment mechanism.
 
    REACTION WHEEL ASSEMBLY
    The Attitude and Orbit Control System (AOCS) of the spacecraft
    required implementation of four reaction wheels, used with a three
    out of four redundancy. They were of ball bearing momentum /
    reaction wheel type, for clock-wise and counter-clockwise
    operation, with the wheel mass suspended by two angular contact
    ball bearings paired by solid preloading. The main functions of
    the RWA was to ensure correct orientation of the spacecraft in
    fine pointing modes, and to ensure spacecraft manoeuvrability
    (e.g. at transition between Mars orbit observation and
    communication phases), with minimum propellant consumption (the
    only related consumption lied with wheel momentum off-loading that
    had to be performed at regular intervals, typically every 2 days.)
 
    SOLAR ARRAY DRIVE MECHANISM
    There were two SADM used on the spacecraft, one for each Solar
    Array wing. The SADM were mounted on each side of the spacecraft,
    and were independently controlled by the AOCS Processor Module.
    The main functions of the SADM was to support the solar array wing
    throughout the mission, to provide the electrical power and signal
    interfaces to the spacecraft and to orient the solar array wing
    towards the Sun by rotation about the Ys axis. The SADM was
    composed of a motor and gearbox assembly, ensuring the orientation
    of the solar array by rotation, a shaft and bearing assembly
    ensuring mechanical connection and pointing accuracy, a twist
    capsule unit transferring electrical power to the spacecraft.
    Those elements were mounted on a baseplate which was attached to
    the spacecraft sidewall.
 
    SOLAR ARRAY HOLD-DOWN AND RELEASE MECHANISM
    Each wing of the solar array was attached on the spacecraft
    sidewall, in launch configuration, by Hold Down and Release
    Mechanisms (HDRM). Each HDRM consisted in a set of hold down
    bushings, attached to the structure of each panel which were held
    together via a stainless steel hold down pin of 3.5 mm diameter on
    a hold-down baseplate fixed on the spacecraft sidewall. The HRDM
    also incorporated a pair of pyro initiators, which were actuated
    after spacecraft separation from the launcher under control of the
    Data Handling Processor Module. The main functions of the HDRM was
    therefore to maintain safely stowed each solar array wing and to
    ensure their release for proper solar array power generation.
 
    SOLAR ARRAY DEPLOYMENT SYSTEM
    Each yoke and wing of the solar array was fitted with a deployment
    mechanism that ensured proper deployment and latching of the solar
    array after release of the HDRM. The deployment mechanism
    consisted in a set of spring energy driven hinges mounted by pair
    between each solar array panel, between the first panel and the
    yoke, and between the yoke and the SADM. Each hingeline was then
    linked to the others by a set of pulley and cables, that ensured a
    synchronised deployment of the wing. The torque margin of the
    Solar Array deployment system varied between 7.5 (at beginning of
    deployment) and 2.6 (at end of deployment).
 
    BEAGLE 2 SPIN-UP AND EJECTION MECHANISM
    Beagle 2 formed an integrated experiment, composed of a lander
    (featuring investigation experiments) encapsulated in a Entry,
    Descent and Landing System (EDLS). Those items were composing the
    probe, which interfaced to the orbiter top floor through the Spin-
    Up and Ejector Mechanism.
 
    MARSIS ANTENNAS DEPLOYMENT MECHANISMS
    The baseline configuration for MARSIS deployment mechanism had
    departed from the Cassini (STEM) concept, i.e. a tubular antenna
    made of 2 semi-circular formed strips made of Copper-Beryllium.
    The selected design was the ASTRO one, consisting of a boom made
    of a GFRP tube pierced with 2 diametrically opposed diamond shaped
    holes at the selected distance to provide folding capability. The
    antenna boom contained two wire elements forming the active
    radioelectrical part of the antenna, and was folded at each
    hollowed hinge and held flattened in specific containers. When
    release was initiated, the container was opened through pyro
    devices, and the boom was self deploying thanks to its intrinsic
    energy which had been stored during the folding/flattening process
    necessary to meet the launch volume constraints.
 
 
    ATTITUDE AND ORBIT CONTROL SYSTEM
    ---------------------------------
 
    AOCS BASIC CONCEPTS
    Due to the selection of a fixed high Gain antenna (HGA), and to
    the propulsion configuration including a Main Engine, the Mars
    Express mission required a high level of attitude manoeuvrability
    for the spacecraft. Attitude manoeuvres were performed: - Between
    the observation phase and the Earth communication phase, or to
    reach specific attitudes necessary for science observations (in
    particular SPICAM). - Before and after the Lander ejection, before
    and after each trajectory correction manoeuvre, performed either
    with the Main Engine or with the 10N thrusters. - To optimise the
    Wheel Off-Loading, through the selection of an adapted attitude
    for this operation.
 
    All the attitude manoeuvres of operational phase were defined on
    ground, using a polynomial description of the Quaternion to be
    followed by the Spacecraft. The attitude estimation was based on
    Star Tracker and gyros, ensuring the availability of the
    measurements in almost any attitudes. Some constraints had however
    to be fulfilled, the Star Tracker being unable to provide attitude
    data, when the sun or the planet are close to or inside its Field
    of view. Reaction wheels were used for almost all the attitude
    manoeuvres, providing a great flexibility to the Spacecraft and
    reducing the fuel consumption. The angular momentum of the wheels
    had however to be managed carefully from ground.
 
    STAR TRACKER (STR)
    The Star Tracker (STR) was the main optical sensor of the AOCS,
    used at the end of the attitude acquisition to acquire the final
    3-axes pointing, and during almost all the nominal operations of
    the mission. A medium Field Of View (16.4 deg circular) and a
    sensitivity to Magnitude 5.5 were used to provide  a 3-axes
    attitude measurement with at least 3 stars permanently present in
    the FOV. The STR included a star pattern recognition function and
    can perform autonomously the attitude acquisition. The Mars
    Express Star Tracker was produced by Officine Galileo, and is
    similar to the Rosetta one, except at S/W level. 2 Star Trackers
    were implemented on the minus Xa face of the Spacecraft, with an
    angle of 30 degree between their optical axes.
 
    INERTIAL MEASUREMENT UNITS (IMU)
    Two Inertial Measurement Units (IMU) were used by the AOCS, each
    IMU including a set of 3 gyros and 3 accelerometers aligned along
    3 orthogonal axes. The AOCS control used either the 3 gyros of the
    same IMU (reference solution at the beginning of life) or any
    combination of 3 gyros among the 6 provided by both IMUs. For the
    accelerometers, only a full set of accelerometers of one single
    IMU was used, due to the lower criticality of the accelerometer
    function, and to the availability onboard of an alternative method
    for the delta V measurement (pulse counting). The Gyros were
    useful during the attitude acquisition phase for the rate control,
    during the observation phase to ensure the required pointing
    performances and during the trajectory corrections, for the
    control robustness and failure detection. A non mechanical
    technology was selected to avoid the mechanical sources of failure
    in flight. The Accelerometers were essential during the main
    trajectory corrections such as the insertion manoeuvre to improve
    the accuracy of the delta V. The IMU of Mars Express is identical
    to the Rosetta unit. Only the number of units and the onboard
    management of the configuration was different.
 
    SUN ACQUISITION SENSORS (SAS)
    Two redunded Sun Acquisition Sensors (SAS) were implemented on the
    Spacecraft central body and are used for the pointing of the Sun
    Acquisition Mode (SAM) during the attitude acquisition or
    reacquisition in case of failure. The SAS are identical to Rosetta
    units, but provided with customised baffles.
 
    REACTION WHEEL ASSEMBLY (RWA)
    The Reaction Wheel Assembly (RWA) included 4 Reaction Wheels (RW)
    implemented on a skewed configuration. This configuration enabled
    to perform most of the nominal operations of the mission with a 3
    RWL configuration among 4. During some critical phase during which
    the transition to the SAM had to be avoided (before lander
    ejection and before Mars Insertion Manoeuvre), a 4 wheels
    configuration was be used, under ground request. The Reaction
    wheels provided the AOCS control torques during all the phases of
    the mission except the trajectory corrections, the attitude
    acquisition and back up modes.
 
    PROPULSION CONFIGURATION
    The Propulsion configuration included a Main Engine (414 N) which
    was used to perform all the major trajectory changes, and 10 N
    thrusters used for the attitude control and also to produce the
    thrust during the small trajectory corrections. The 10 N thrusters
    configuration was optimised to perform all the attitude control
    functions with only 4 redunded thrusters, each of them being
    implemented near a corner of the -Z face of the spacecraft.
 
    SOLAR ARRAY DRIVE MECHANISM
    2 redunded Solar Array Drive Mechanisms (SADM) were implemented on
    the Y+ and Y-walls of the spacecraft to control the orientation of
    the Solar Arrays. The SADM was only used for large angle
    orientation of the wings, the selected flight orientation during
    the observation phase near pericentre requiring no SADM actuation,
    once the observation attitude was reached. The SADM used a stepper
    motor, a gear, and a twist capsule technology. The SADM motion is
    defined in the range +/-180 deg (minus margins). The SADM is
    identical to the Rosetta unit, except for the speed levels which
    are specific to Mars Express.
 
AOCS HARDWARE ARCHITECTURE
 
AOCS unit Nb   Technology / characteristics   Heritage       Supplier
------------   ----------------------------   ----------     --------
Star Tracker   2 CCD detector. 16.4deg        Rosetta unit.  Officine
               circular FOV/ Magnitude 5.5                   Galileo
 
 
Gyro/accelero   2 Ring Laser Gyros (RLG).     Rosetta unit   Honeywell
                3 gyros/3 acceleros per
                unit.
 
Sun Acquisition 2 Solar cells mounted on      Rosetta/SOHO   TPD-TNO
Sensor (SAS)      a pyramid
 
 
Reaction Wheel  4 Ball bearing Momentum/      Telecom. Sat.  Teldix
                Reaction wheels.              Unit
                 12 Nms/0.075 Nm
 
SADM            2 Stepper motor with gear.    Rosetta unit   Kongsberg
                Twist capsule
 
 
    AOCS GENERIC FUNCTIONS
    ----------------------
    The AOCS modes used generic functions for the guidance, the attitude
    estimation and the actuators management. The role of the guidance was
    to provide onboard the reference attitude to be followed at each time
    of the mission by the attitude control. It concerned of course the
    orientation of the Spacecraft but also the Solar Array position. The
    analysis of the mission needs showed that 4 types of guidance are
    necessary along Mars Express mission:
    - Pointing of the High Gain Antenna (HGA) towards the Earth, and the
      Solar Array cells towards the Sun. This kind of guidance was used
      during the cruise phase and for communications during the
      scientific mission phase, these two cases corresponding to the AOCS
      Normal Mode, pointing on ephemeredes (NM/ GSEP phase).
      The information necessary to the guidance concerned the Spacecraft
      to Earth and the Spacecraft to Sun directions. They were contained
      in the ephemeris definition.
    - This type of guidance was also used in a different way for the
      Earth acquisition (SHM : Safe/Hold Mode), in order to perform the
      autonomous orientation of the spacecraft towards the Earth. The
      ephemeris data were then used to perform large angle slew
      manoeuvres with thruster control.
    - Attitude profiles : this type of guidance was necessary during the
      observation phase for the Nadir pointing or to follow more specific
      profiles. This function was ensured by an onboard profile
      description based on Chebychev polynomial, the parameters being
      uploaded from ground. This capability enabled also to ensure the
      attitude slew manoeuvres.
    - Fixed inertial pointing (fixed quaternion) : This type of guidance
      was used for specific phases of the mission, during Orbit Control
      Mode, Thruster Transition Mode or during the scientific mission
      phase for SPICAM specific needs (in NM/FPIP and NM/WDP).
 
    Three generic functions had been defined for this purpose at software
    level :
    - the Ground commanded guidance,
    - the Onboard Ephemeris propagation,
    - the Autonomous Attitude Guidance Function, this latter function
      generating the guidance information necessary either for the fixed
      Earth pointing or for the Earth acquisition in SHM.
 
 
    GYRO-STELLAR ESTIMATION FUNCTION
    The gyro-stellar estimation function was common to many AOCS modes :
    It was initialised during the Sun Acquisition Mode (SAM) to prepare
    the following Earth acquisition operation (SHM: Safe/Hold Mode). It
    provided accurate attitude estimation during the Normal Mode of
    course but also in the Orbit Control Mode (OCM) and Thruster
    Transition Mode( TTM) for instance. The gyro-stellar estimator
    processed gyro and star tracker (STR) measurements to provide an
    accurate estimate of the spacecraft attitude. It was based on a
    Kalman filter with constant covariance that allowed mixing
    measurements at different rates (8 Hz for the gyros and 2 Hz for the
    STR). The constant covariance reduces the computer load while
    ensuring good performances. The estimated attitude was a quaternion
    representing the spacecraft attitude in the J2000 inertial frame.
    The gyro-stellar estimator also estimated the gyros drifts to limit
    the attitude errors in case of STR measurement absence due, for
    instance, to a temporarily STR occultation. A specific management of
    the drift estimates was proposed for Mars Express, taking into
    account the specific conditions of the scientific mission phase
    (existence of rates due to varying profiles, and potential
    occultation). The gyro-stellar estimator implemented a coherency test
    between the gyro and STR measurements in order to detect failures
    that could not be detected at equipment level.
 
    REACTION-WHEEL OFF-LOADING FUNCTION
    The wheel Off-Loading function enabled to manage the angular momentum
    of the wheels to a target value, through thruster actuations. This
    function was completely autonomous during the last phase of the Earth
    acquisition sequence (SHM/EPP:Earth Pointing Phase). During the
    nominal operations around Mars, it was preferable to command the
    wheel Off-Loading from the ground, the date being optimised taking
    into account the mission constraints. The Off-Loading function
    managed simultaneously all the wheels. It included several sequences
    of thruster pulses until angular momentum of each wheel was close to
    the target value. This sequence was defined by a feed forward 3-axes
    wheel torque command combined with a thruster pulse.
    The sequence ended with a tranquillisation phase controlled by the
    wheels, in order to damp the dynamic excitation generated by the
    actuation of thrusters and wheels.
 
    REACTION WHEEL MANAGEMENT FUNCTION
    This function was active in all the modes controlled through wheel
    torques (Normal Mode and Safe/Hold Mode at the end of the attitude
    acquisition sequence), but also when the wheels were kept to a
    constant speed through a specific control loop but not used in the
    AOCS control, as in Orbit Control Mode, Thruster Transition Mode or
    Braking Mode. Six states of the wheel configuration are possible with
    this function depending on the control of the wheels in torques (t)
    or in speed (s). For instance, the nominal operation in Normal Mode,
    uses 3 wheels in torques (3t), but could sometime require a fourth
    wheel if a hot redundancy is useful (4t). During trajectory
    corrections the configuration included 3 wheels controlled in speed
    (3s). Intermediate states are necessary between these basic
    configurations in order to spin the wheels for instance (3t + 1s).
    This function was also in charge of the generation of wheel torque
    commands in wheel frame, and of the friction torque estimation
    necessary for compensation and for the failure detection. It
    interfaced also with the Wheel Off-Loading function.
 
    THRUSTER MODULATOR AND SELECTION FUNCTION
    The selected amplitude modulator and on-time summation algorithms
    were re- used from Rosetta and adapted to match more efficiently the
    Mars Express needs taking into account the specific thrusters
    configuration.
    The modulator had only one working phase where the four thrusters can
    be used:
    - to produce a force along the satellite Z axis direction
    - to control the 3-axes satellite attitude (three torques are
      commanded to the modulator).
 
    The modulator working frequency was 8Hz. At each step, the modulation
    type used (ON-modulation or OFF-modulation) was automatically
    selected so as to maximise the available torque capacity for attitude
    control. In the case the torque capacity was insufficient with
    respect to the commanded control torque, priority is given to the
    control and the commanded force ratio is automatically modified to
    recover the required torque capacity. Moreover in order to limit the
    actuation delay, the attitude control torque was always produced at
    the beginning of the actuation period.
    To limit the number of thrusters ON/OFF or to tune the control limit
    cycle amplitude when using thrusters, the modulator output period had
    to be changed to any period multiple of 125 ms.
 
    PROPULSION ARCHITECTURE DESCRIPTION
    -----------------------------------
    A bi-propellant system based on a telecommunication spacecraft
    heritage was adopted for the baseline. A set of isolation pyro valves
    and latch valves had been added to ensure safe operations during
    Launch and Cruise, and for a re- liable acquisition of the Mars orbit
    for science mission.
    At launch, the pressurant assembly (high and low pressure sections)
    were all isolated from the propellant tanks by normally closed
    pyrotechnic valves PVNC1 to PVNC6, by non return valves NRV1 to NRV4.
    The propellant tanks are pressurised to 4 bar. Similarly, the
    propellant was isolated from the Reaction Control Thrusters and Main
    Engine assembly by normally closed pyrotechnic valves PVNC7 to PVNC14
    and thruster/main engine Flow Control Valves (FCV).
    Following separation, the pyro valves protecting the pressurant
    assembly were fired to pressurise the system to its operating
    pressure of 17 bar. Then the latch valves were closed, isolating the
    non return valves from propellant. A pressure transducer (PT2)
    located at the regulator outlet could monitor pressure build up at
    the NRV location due to regulator leakage. When necessary the latch
    valves were opened and the pressure relieved into the propellant
    tanks. It was assumed that a pressure of up to 20.5 bar could be the
    criterion to initiate an open/ close cycle of the latch valves by
    telecommand.
    The 20.5 bar pressure was an initial suggestion which needed to be
    confirmed. It may affect component qualification issues because it
    exceeds existing MEOP values for the components in the section. Short
    duration opening times for the latch valves minimised propellant
    vapour migration and it was essential for both oxidiser side and fuel
    side latch valves to open simultaneously to limit vapour migration.
    The system operates in this pressure regulated mode, using the 10 N
    Reaction Control Thrusters only, during the period of the transfer
    orbit to Mars.
    A few days before Mars orbit insertion, the 400 N Main Engine was
    primed and then calibrated by specific blank manoeuvres, combined
    with re-targeting of the S/C after Beagle 2 probe ejection. This
    ensured that the Main Engine could be used safely for the Mars orbit
    insertion and acquisition of the operational orbit. Should a Main
    Engine failure be detected at this stage, a back-up scheme, using the
    Reaction Control Thrusters would have been implemented to reach at
    least a degraded orbit around Mars.
    After attaining the operational orbit, the pressurant and Main Engine
    assemblies were re-isolated by firing all the normally open
    pyrotechnic valves and closing the latch valves. The remainder of the
    mission was per- formed in blow down mode, using only the 10 N
    Reaction Control Thrusters. The number of Reaction Control Thruster
    had been limited to 8 (4 nominal, 4 redundant), located at the bottom
    (-Z) side of the spacecraft to provide thrust principally along Zb to
    compensate for Main Engine thrust imbalance caused by Main Engine
    alignment and Spacecraft Centre Of Mass (CoM) uncertainties. Adequate
    tilting of the Reaction Control Thrusters is implemented so as to
    provide the capability for torque around each main axis of the
    spacecraft.
    In order to maximise flexibility and adaptability to failure cases,
    each Reaction Control Thruster was fitted with a Thruster Latch Valve
    (TLV) upstream from the thruster Flow Control Valves, permitting
    individual switch over from prime to redundant for each Reaction
    Control Thruster. It had to be noted that this two-tank configuration
    was compatible with a horizontal handling of the spacecraft as
    required by Soyuz launch campaign, on the proviso that the tanks were
    filled at least up to 62% of their maximum capacity. The
    compatibility of this fill fraction wrt S/C global dynamic behaviour
    was under investigation to avoid fluid/structural modes coupling.
 
 
    RF COMMUNICATIONS
    -----------------
 
    OVERVIEW
    The communications with the Earth could be performed either in S-Band
    or X-Band in accordance with ESA Standards. Two Low Gain Antennas
    (LGA) allow omni-directional emission and reception in S-Band, while
    a dual band 1.65 m High Gain Antenna (HGA) allows high rate TM
    emission in S-Band and X-Band including TC reception in S-Band and X-
    Band. Demodulation of the up-link signal was performed by the Dual
    Band Transponder before routing the resulting bit flow to the Data
    Handling. The stored TM within the SSMM is modulated in either SBand
    or X-Band within the Dual Band Transponder, which also performed S-
    Band signal amplification with 5 W. X-Band signal amplification is
    performed using a 65 W Travelling Wave Tube Amplifier.
 
    UPLINK
    The communication from the ground station(s) to the spacecraft was
    performed in S-Band or X-Band. Two Low Gain S- Band Antennas (LGA)
    were accommodated, one on the upper Z-panel, aside of the High Gain
    Antenna and the other one on the bottom of the spacecraft, thus
    allowing a quasi omnidirectional coverage. The LGA was used mainly
    during Launch and Early Operation Phase (LEOP), critical phases and
    for emergency situations. A narrow-beam dual-band high-gain antenna
    was used for all nominal mission operations for the uplink in X-Band,
    like the Cruise Phase or when orbiting around Mars.
    The RF uplink signal, which was modulated with packetised
    telecommands as NRZ/PSK/PM data, was routed towards a diplexer,
    performing frequency discrimination, and then to the Dual Band
    Transponder input. The transponder performed carrier acquisition and
    demodulation, and transmitted the extracted signal to the Data
    Handling for further processing.
    The frequencies for the uplinks are:
    - 2114.676 MHZ (DSN 18) for S-Band,
    - 7166.936 MHZ (DSN 18) for X-Band.
 
    The following telecommand bit rates are handled by the Mars Express
    Spacecraft as provided by the CDMU design: 7.8125 bps and 15.625 bps,
    250 bps, 500 bps, 1000 bps and 2000 bps. These possible bit rates are
    selectable by Memory Load Command (MLC). As a baseline, the lowest
    bit rates was used in case of emergency via the Low Gain Antennas in
    S-Band, while the highest ones were used operationally through the
    High Gain Antenna in XBand.
 
    DOWNLINK
    A high data downlink capability was required, considering the large
    data volume generated by the instruments. Nevertheless, downlink
    capacity was limited by the large spacecraft to Earth distance. The
    downlink of the telemetry data to the ground stations were performed
    in either S or X-Band.
    The frequencies for the downlink were:
    - 2296.482 MHZ (DSN 18) for S-Band,
    - 8420.432 MHZ (DSN 18) for X-Band.
    Downlink was performed at a commandable, variable bit rate. The CDMU
    design allowed to generate a telemetry flow at any bit rate
    corresponding to a power of two multiplied by 32/n and lower than
    262.144 bps, where n is equal to 2, 3, 5 or 7. The possible bit rates
    were selected via Memory Load Command (MLC) and vary from 7.8 bps as
    a minimum and can be up to 230 kbps. The bit rate to which reference
    was made was the bit rate following Reed-Solomon encoding, but prior
    to convolutional encoding, if any. Due to hardware limitations,
    convolutional encoding was only performed for bit rates lower than
    65536 bps. Above this value, only Reed-Solomon encoding was
    performed.
    As a baseline, the lowest bit rates were used in case of emergency
    only using the Low Gain Antennas, whilst the highest ones were used
    operationally through the High Gain Antenna in X Band. The variable
    bit rate signal was transmitted to the Dual Band Transponder as SP-
    L/PSK for bit rates lower than 65536 bps and as SP-L (no subcarrier)
    for higher bit rates. This signal was phase- modulated in either S
    Band or X Band by the Dual Band Transponder, and added to the MPTS
    ranging signal if it had been detected on the uplink.
 
    DATA HANDLING ARCHITECTURE
    --------------------------
    The Data Management System (DMS) was in charge of telecommand
    distribution to the whole spacecraft, of telemetry data collection
    from the spacecraft sub- systems and payloads and data formatting,
    and of the overall supervision of spacecraft and payload functions
    and health.
    The DMS was based on a standard OBDH bus architecture enhanced by
    high rate IEEE 1355 serial data link between the CDMU (Control and
    Data Management Units) processors and the SSMM and STR. The OBDH bus
    was the data route for platform and payloads data acquisition and
    commands distribution via the RTU. The DMS included 4 identical
    Processor Modules (PM, 1 to 4) located in the 2 CDMU.  Two processor
    modules were dedicated to the DMS (PM2 and PM3), and two to the
    AOCS(PM1 and PM4). The PM selected for the DMS function acted as the
    bus master. It was in charge of Platform subsystem management
    (Communications, Power, Thermal, Payloads). The PM selected as the
    AOCS computer was in charge of all sensors, actuators and Solar Array
    Drive Electronics (SADE).
    TC-decoder and Transfer Frame Generator (TFG) were included in each
    CDMU. The Solid State Mass Memory (SSMM) was used for data storage
    including 12 Gbits of memory at BOL. It was coupled to the two DMS
    processors, the TFG, OMEGA, HRSC and MELACOM instruments. It stores
    science and global housekeeping telemetry packets.
 
    OVERVIEW
    The Data Handling architecture was organised around the two CDMU.
    They were in charge of controlling ground command reception and
    execution, on-board housekeeping and science data telemetry storage
    and formatting them for transmission. The on-board data management,
    controlled processing and execution of on-board control procedures
    belongs to their tasks as well. Each CDMU featured two MA3-1750
    Processor Modules, each of them being able to process either Data
    Management or AOCS software.
    A built-in failure operational Reconfiguration Module (RM) ensured
    system level FDIR and reconfigured the CDMU as necessary. Data
    transfer with other Data Handling units were ensured using standard
    links such as a redunded OBDH data bus or IEEE-1355 serial links. Two
    Interface Units were performing inter- face adaptation between those
    links and other spacecraft units. The AOCS Interface Unit (AIU) was
    dedicated to AOCS equipment, while the RTU interfaces with the
    remainders, including the Instruments. A file-organised 12 Gbits SSMM
    was implemented to store the Housekeeping and the Science Data. It
    also collected directly Science Data from the three high rate Payload
    Instruments.
 
    SSMM SOFTWARE
    -------------
    The Solid State Mass Memory (SSMM) consists of 2 processor systems:
    - The Memory System Supervisor (MSS), dedicated to the communication
      with the DMS MMS.
    - The File and Packet Controller (FPC), dedicated to the file
      management on the memory modules and to the data exchange with the
      instruments and the TFG.
    The SSMM software runs on the micro-processor based MSS and the
    micro- controller located in the FPC. The main part of the SSMM-SW is
    programmed in C language. Parts of the start-up function are
    programmed in Assembler. The SSMM software consists in two parts:
    - The Initialisation software covering the Init Mode and running in
      the MSS. It was executed in MSS PROM after activation of the SSMM.
      It performed the following main functions:
      - initialisation of system controller and control interface
        hardware, tables, data, etc.,
      - load nominal software from EEPROM to RAM, (reduced) commands
        handling, transition to Operational Mode.
    - The Operational software covering the Operational Mode and Test
      Mode. It did run in the MSS RAM and FPC RAM. It performed the
      following main functions:
      - execution and control of telecommands,
      - configuration and test of the memory modules,
      - control of data flow from instruments and to TFG to and from the
        Memory Modules,
      - failure handling, including management of failure log,
      - failure recovery,
      - creation of event report,
      - housekeeping,
      - TM packing for all required data, Watchdog control.
    In case of fatal failure, the SW returns to the Init software to
    allow for failure investigation.
 
    INSTRUMENTS SOFTWARE
    --------------------
    Each instrument had its own autonomous SW, located in the instrument
    electronic units. The command and control of the payloads was
    performed by the dedicated Payload Management function of the DMS SW.
    The physical interface of the DMS PM with the instruments is the
    Remote Terminal Unit (RTU). Data exchange between the payloads and
    the DMS software was performed by means of packetised TM/TC, both for
    commands, housekeeping and science telemetry data.
    -  Commands from the Ground are routed by the DMS software to the
       payloads through the RTU and the OBDH bus.
    -  Housekeeping data from all the instruments are transmitted from
       the RTU to the DMS SW through the OBDH bus.
    -  Scientific data from low rate payloads (PFS, ASPERA, MARSIS,
       SPICAM, VMC, OMEGA) are transmitted from the RTU to the DMS SW
       through the OBDH bus.
    -  Scientific data from high rate payloads (OMEGA, MELACOM and HRSC)
       are directly transferred to the SSMM through TM packets on the
       IEEE-1355 link.
 
 
 
    GROUND SEGMENT OVERVIEW
    -----------------------
    The Mars Express spacecraft will nominally be controlled from the ESA
    New Norcia (Australia) station during the Routine Operations phase.
    Shared operations with Rosetta provide a station availability of 8
    hours a day (design assumption), though longer duration might be
    achieved during Rosetta cruise phase. Additional Earth stations are
    considered, such as ESA General Purpose Network Kourou 15m station
    during LEOP and NASA DSN 34 m and 70 m stations in critical phases.
 
    ESA GROUND SEGMENT
    - ESA General Purpose Network Kourou station featuring 15 m antennas
      with S-band uplink capability and S-band / X-band down-link
      capability.
    - ESA New Norcia station, featuring a 35 m S-band / X-band antenna
      with S-band/X-band uplink and down-link capability.
 
    DSN COMPATIBILITY
    - NASA DSN stations featuring 34 m and 70 m antennas, with S-band and
      X-band up-link and down-link capabilities, as described in DSN
      Flight Project Interface Handbook (NASA/JPL 810.5).
 
    Summary of ground stations nominal performances:
 
                                    Kourou  New Norcia    DSN       DSN
                                    15m     35m           34 m      70m
 
    S Band Uplink  EIRP (2kW HPA)   81      87            98        117
                   Pointing Loss    0.05    0.1           0.1       0.1
                   Antenna Gain     48.5    55.0          55.2      61.7
    X Band Uplink  EIRP (2kW HPA)   N/A     97            108.8     114.9
                   Pointing Loss    N/A     0.1           0.3       0.3
                   Antenna Gain     N/A     64.3          66.8      72.2
    S Band Downlink G/T at 10 deg   29.85   37.5          40.5      46.9
                   Pointing Loss    0.03    0.1           0.1       0.1
                   Antenna Gain     49.2    56.0          56.9      62.3
    X Band Downlink G/T at 10 deg   38      50.1          50.1      56.7
                   Pointing Loss    0.1     0.3           0.3       0.3
                   Antenna Gain     60.0    68.0          68.2      73.1
 
 
    Acronyms
    --------
 
    AOCS        Attitude and Orbit Control System
    HDRM        array hold-down and release mechanism
    IMU         INERTIAL MEASUREMENT UNITS
    LV          launch vehicle
    MLI         multi layer insulation
    RWA         reaction wheel assembly
    SADM        solar array drive mechanism
    SAS         sun acquisition sensors
    SUEM        Beagle2 spin-up and ejection mechanism
    SC          spacecraft
    STR         star tracker

        