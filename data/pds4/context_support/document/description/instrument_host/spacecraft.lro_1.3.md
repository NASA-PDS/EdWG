
 
    Instrument Host Overview
    =========================
 
    For all LRO experiments, data are collected by science instruments on
    the spacecraft and then relayed via the spacecraft telemetry system
    to stations of the Space Communications Network (SCN), a term we use to
    encapsulate the various components used to carry out two way communication
    with the spacecraft. The following sections provide an overview of the
    spacecraft, the science instruments, and the ground component of the
    SCN.  Further detail about the individual components of the SCN is
    available in the file INST.CAT.
 
    Instrument Host Overview - Spacecraft
    =======================================
 
    The Lunar Reconnaissance Orbiter is designed for a one-year base mission
    [CHINETAL2007]with a goal of an extended mission of up to four
    additional years.  LRO will be launched on an Atlas 5 401 Launch
    Vehicle along with its companion spacecraft, the Lunar CRater
    Observation and Sensing Satellite (LCROSS), into a direct insertion
    trajectory to the Moon.  The on-board mono-propellant hydrazine
    propulsion system will be used to capture into a polar orbit at the Moon,
    timed to obtain an orbit plane that enables optimum lighting conditions
    in polar regions during summer and winter seasons.  Additional burns
    will circularize the orbit and maintain it during the base mission at
    an altitude of 50 +/- 20 km.  A lower-maintenance, elliptical orbit of
    30x216 km will be used for commissioning and may be used for the
    extended mission.  The spacecraft carries enough fuel to provide over
    1300 m/s of velocity change (delta V) for orbit capture and maintenance.
 
    LRO Description
    ===================
 
    The orbiter is a 3-axis stabilized, nadir-pointed spacecraft, designed
    to operate continuously during the primary mission.  Four reaction
    wheels provide attitude control to 60 arc sec and momentum storage of up
    to 2 weeks, with thrusters providing momentum dumping once per month.
    Two star trackers and an inertial reference unit provide attitude
    knowledge of 30 arc sec.  Coarse sun sensors provide attitude
    information in contingency modes, to enable and maintain proper attitude
    with respect to the sun, keeping the spacecraft power positive and
    thermally stable.
 
    A 10.7 square meter solar array provides 1850 W end-of-life during the
    sunlit portion of the orbit.  An 80 A-hr Lithium-ion battery maintains
    the bus voltage and provides operational power during the orbit eclipses
    and survival power during the rare, long eclipses of the sun by the
    earth.  The power electronics distributes the raw 28+7 V to the
    instruments and the spacecraft bus electronics, delivering over 800 W
    average power each orbit.
 
    The flight computer is a RAD-750 processor executing at 133 MHz.  Two
    100 Gbyte recorders store science data for playback to the earth at 100
    Mbps through a 40 W Ka-band transmitter and high-gain antenna.  An
    S-band system provides command, engineering telemetry, and navigation
    functions.  Laser ranging capability provides ~10 cm position precision
    during four one-hour passes per day.  These data, when combined with
    lunar measurements from LOLA, will improve the orbit determination
    capability of LRO.
 
    The thermal control system utilizes heat pipes to spread heat and move
    it to the zenith-facing radiators.  A modular structure design enables
    parallel assembly of the spacecraft.
 
    The total mass of the observatory is less than 949 kg dry and 1846 kg
    fully fueled.
 
    Orbiter Features
    ----------------
 
    The LRO Orbiter has the following key features:
 
    1. Single string with selected redundancy
    2. C&DH hosts flight software, handles data interfaces
    3. PSE controls battery charging and power distribution
    4. PDE controls thrusters, deployment devices, and inhibits
    5. S-band transponder and Ka-band transmitter support radio links
    6. 2-axis gimbals on array and high-gain antenna track sun and earth
    7. Omni antennas provide continuous receive capability
    8. Standard interfaces
       a. 1553
       b. Spacewire
    9. Modular Assembly
       a. Propulsion module, instrument module, avionics module
       b. Parallel development
 
    Spacecraft Subsystems
    ---------------------
 
    The spacecraft subsystems are summarized briefly below.
 
    Spacecraft Bus
    ---------------
 
    The LRO spacecraft bus consists of the following components:
 
    1. Primary Structure (aluminum)
       a. Heating/Cooling panel
       b. Edge members, fittings, and spools
       c. High Gain Antenna System (HGAS) support brackets
       d. Solar Array Substrates (SAS) stanchions
       e. Reaction wheel assemblies brackets
    2. Instruments
       a. CRaTER
       b. DLRE
       c. LAMP (on optical bench)
       d. LEND
       e. LOLA (on optical bench)
       f. LROC (on optical bench)
       g. MRF
    3. Avionics Components
       a. Reaction wheels
       b. Battery
       c. S-band OMNI antenna
       d. Coarse Sun Sensors (CSSs)
 
    High Gain Antenna System
    -------------------------
 
    The High Gain Antenna System (HGAS) includes a deployment system with
    two latches requiring mechanical release, and three restraint areas.
    The articulation system is a two axis gimbal system capable of slightly
    greater than 180 degrees of rotation about each axis, and two rotating
    cable wraps.  RF components include Ka-band antenna with an S-band
    patch antenna, an S-band coax cable and a Ka band waveguide, and rotary
    joints in each of two gimbal actuators. A small laser ranging
    telescope is mounted on the wave guide with fiber optic cable providing
    the connectivity to the LOLA instrument. Thermal control is provided
    through blanketing, T-stats, heaters, and radiators dedicated to the
    HGAS system.
 
    The latching release assembly utilizes a 400 lb preload, to include a
    1.3 gapping factor of safety. Release begins with actuation of the
    non-explosive actuator (NEA) which initiates the deployment sequence.
    The principle of operation of the NEA involves a tensile load reacting
    against a spring-wound split spool. Upon fuse wire initiation, the
    spring unwinds, allowing the halves of the spool to separate.  The slow
    release of the tensile load minimizes the release of strain energy and
    therefore minimizes shock.
 
    Propulsion System
    -----------------
 
    The propulsion system has been designed to provide mid-course transit
    corrections after separation from the launch vehicle, lunar orbit
    capture, and station keeping for the remainder of the mission. The
    propulsion system is a monopropellant hydrazine system. Fuel load is
    894 kg of hydrazine (~ 1300 m/sec delta-V capability) in two identical
    titanium diaphragm propellant tanks (40 in OD oblate spheroid TDRSS
    type tanks in TDRSS configuration)
 
    The system includes twelve dual coil catalytic hydrazine thrusters, four
    of which are on-axis 80 Newton class insertion thrusters located around
    the spacecraft center of gravity (in the x-axis). Eight canted 20
    Newton class attitude control thrusters provide attitude control, lunar
    orbit maintenance maneuvers, and momentum dumping.
 
    Isolation valves with redundant coils are used to isolate thruster banks
    in the event of a thruster failure. Flow control orifices prevent
    water hammer surges.
 
    The Helium Pressure Regulated System is a 4200 psi COPV Helium
    pressurant tank (17 in outside diameter by 29.6 in Length ). A two
    stage regulator (single fault tolerant) is set at 270 psi nominal.
    Redundant pyro valves provide for high pressure isolation during ground
    and launch operations with a high pressure latch valve to isolate high
    pressure source during mission  operations.
 
    Electrical Power System
    -----------------------
 
    The LRO Electrical Power System (EPS) provides the following functions:
 
    1. Load power requirements for all nominal mission modes
    2. Battery charging and control
    3. Interface to the C&DH subsystem for power system performance,
       monitoring, configuration and control
    4. Power interface to the electrical subsystem
    5. Capability to respond to Special Commands
    6. Power distribution and load switching capability
    7. External power interfaces for I&T, ground, and pre-launch operations
    8. Bus protection by automatically shedding loads if a defined fault
       condition occurs
    9. Restoration of power to shed loads shall be remotely controllable via
       ground command.
 
    The power system contains three sub-elements: the solar array, Power
    Sub-system Electronics (PSE), and the lithium-ion battery.
 
    Solar Array System (SAS)
    ------------------------
 
    Three low-CTE graphite composite solar array panels are contained within
    one articulated wing. The system is mounted on flexures to aluminum
    spacecraft structure to allow for differential thermal growth. Four
    NEAs are used to release the array.
 
    Articulation is provided through a two-axis gimbal with four panel
    hinges, two at each hinge line connecting center panel to two outer
    panels. When stowed, cells of the central panel face outward. For
    deployment, panel springs (less than 10 lb of stored force) are driven
    with viscous dampers to dissipate energy.
 
    The solar array mounts to a single structure. Benefits of such a design
    include straightforward integration, alignment, and testing. Further,
    the  design provides for reduced and less-sensitive loads on gimbal
    bearings, while structural loads are carried at cup/cone fittings
    rather than through more-flexible gimbal paths.
 
    Deployment is initiated through a software command delivered to the
    propulsion and deployment electronics (PDE), which then fire
    non-explosive actuators (NEA's) with a design similar to that shown for
    the high gain antenna. Separation nuts release rods that restrain the
    array in the stowed configuration. Restraining bolts are pulled by
    strings to the outer panel and captured panel-to-panel latches prevent
    panels from immediately unfurling. Firing the prime and redundant
    actuators on one unit at the  same time, then moving sequentially on to
    the next unit, ensures that the actuators will release the solar array
    in a deterministic order. Individual panel deployment is controlled by
    cam latches. The three panels unfold perpendicular to the spacecraft
    x-axis until all three panels are coplanar with panel surfaces,
    perpendicular to the x-axis.
 
    Once fully deployed, the wing rotates about two axes, with power going
    through Gimbal Actuators at each axis. Rotation required is 180 degrees
    for azimuth actuator and 90 degrees for elevation actuator. Position
    knowledge is obtained via incremental encoders at actuators and
    potentiometers at panel hinges.
 
    Power Sub-system Electronics
    ----------------------------
 
    The basic design and operation of the LRO PSE architecture is modeled
    after  the Microwave Anisotropy Probe (MAP) and utilizes the solar
    arrays to convert sunlight energy into electrical energy while in the
    sunlit, or solstice, period. The electrical power is then transferred
    to the PSE where it is conditioned and directed to all of the
    electrical loads connected to the spacecraft bus.  During the eclipse
    seasons, the PSE will also direct a  portion of the sunlight generated
    electrical power to the battery for energy storage recharging.  During
    the eclipse portion of the orbit the battery will provide all of the
    energy to the spacecraft. In order to achieve minimal electrical
    losses due to power converters as well as a maintaining a stable
    voltage range, the battery will be connected directly to the electrical
    bus.
 
    Any excess power from the solar arrays not needed for battery charging
    or spacecraft loads will be shunted back to the solar array. The PSE
    will perform all of the functions related to power distribution as well
    as battery charging and will be designed for single fault tolerance
    while still being capable of meeting all mission requirements.
 
    Lithium-Ion Battery
    -------------------
 
    A single Lithium Ion battery will provide power to the spacecraft. The
    battery energy storage capacity shall be greater than 80 Ampere-hours at
    Beginning of Life (BOL) within a 24 - 34V voltage range. The battery
    dimensions are (L x H x W) 700mm x 300mm x 180mm (max value). The
    battery is attached to the spacecraft structure at 15 locations around
    the perimeter of the battery, roughly evenly spaced. Thermal control
    is provided at the spacecraft level though a heat pipe assembly.
 
    The battery is constructed from cells arranged in blocks. The basic
    block  size is 8s12p (i.e. 12 strings of 8 cells each) and seven blocks
    are used, to give a total of 8s84p. Within each block the cells are
    connected in  strings with eight cells in each string in series. Four
    blocks are arranged to create the top deck, with three blocks in the
    lower deck.  Four positive connections for each block in a deck are led
    out to a 25-way positive power connector. Four negative connections
    for each block and half-string taps in  a deck are led to 35-way
    negative/telemetry connectors, In addition, PRT's  and thermistors
    installed in the battery are run out to the internal harness
    connectors.
 
    Internal 25- and 35 -way harnesses are connected to the power
    distribution system in the lower deck. Voltage monitoring lines are
    protected with resistors. The positive side of the battery is
    connected via two relays arranged in parallel to give redundancy
    against open-circuit failure of relays.  The relay system also includes
    status-monitoring lines and may be commanded from several sources.
    Command lines are isolated from each other with diodes.
 
    The SONY US18650HC Li-Ion Cell is 18 mm diameter by 65 mm high with a
    mass of 40.3 grams. The cell is a steel can (anode) containing a roll
    of interleaved electrodes soaked in electrolyte, with the necessary
    connections attached and cell safety features in the top cap (cathode).
    The insulation desks are used to isolate the electrode roll from the
    can top with electrical connections provided by tabs and the central
    anode pin. The cathode cap is crimped to the can. The cells are each
    identical SONY 18650HC from the same manufacturing lot, with a high
    level of uniformity in performance characteristics.
 
    Command and Data Handling (C&DH)
    --------------------------------
 
    The command and data handling sub-system includes a single board
    computer (SBC), a mass storage system, a space wire (SpW) interface
    which serves as a high speed interface for the instruments, and a 1553B
    Mil-standard low speed bus. Each has some level of heritage with
    previous NASA and/or DoD missions.
 
    The functions of the C&DH system include:
 
    1. Hosting the attitude control system (ACS) and flight software (FSW)
    2. Command and data handling functions (command acceptance and
       distribution, telemetry collection, science data storage) for the
       instruments
    3. Provide the interface for low rate telemetry, and command and control
       of spacecraft subsystems
    4. Provide the interface to the spacecraft communications transmitter
       and transponder for high speed telemetry (selected instruments and
       subsystems  requiring high data transfer rates)
    5. Science data formatting
 
    The C&DH subsystem has the following features:
 
    1. Ten Printed Wiring Assemblies (PWAs) in a single housing.
    2. The extensive use of SpaceWire European Cooperation for Space
       Standardization (ECSS-E-50-12A) and MIL-STD-1553 allows expandability
       and scalability.
    3. S-Band Communication (SComm)/ Ka-Band Communication (KaComm) cards are
       two independent functions, allowing the addition or deletion of either
       without redesign. They are referred to as a single assembly,
       Communications  (Comm) card, since they share a common backplane
       connector.
    4. The Single Board Computer (SBC) is a British Aerospace Engineering
       (BAE) off the shelf product, with the addition of MIL-STD-1553 Bus
       Controller (BC)/Remote Terminal (RT) and 4-port SpaceWire interface.
    5. Four Data Storage Boards (DSBs) operate as a mass storage system for
       the spacecraft. The DSB boards are designed to interface with the SBC
       via a Compact Peripheral Component Interconnect (cPCI) backplane
       interface.
    6. The Housekeeping / Input Output (HK/IO) card provides an interface to
       the LAMP instrument as well as providing synchronization to all
       instruments on the spacecraft.
    7. The Multi-function Analog Card (MAC) has been custom designed to
       manage the wide range of thermal environments in the lunar orbit.
    8. The Low Voltage Power Converter (LVPC) provides power to all the
       subassemblies except the Primary Ultra Stable Oscillator (USO).
    9. The backplane provides interconnectivity to all the cards within the
       C&DH enclosure.
    10. The primary and redundant USOs are components of the C&DH subsystem,
       but are externally mounted separate assemblies.
 
    Guidance, Navigation, and Control (GN&C) Attitude Control System (ACS)
    -------------------------------------------
 
    The GN&C Attitude Control System (ACS) controls the pointing of the LRO
    spacecraft. Through the use of Star Trackers and Coarse Sun Sensors,
    the  ACS will determine where the spacecraft is currently pointing in
    fine and coarse accuracies, respectively. A three axis, ring laser
    gyro (called an Inertial Measurement Unit) measures the rate at which
    the spacecraft is rotating. The use of Reaction Wheels allows the
    spacecraft to smoothly point into any desired direction as well as
    compensate for disturbance torques (such as High Gain Antenna movement
    and Solar Array movement). Eight small thrusters (20 N) are available
    to provide steering (attitude control) during large thruster firings
    (80 N) for Lunar Orbit Insertion (LOI). Additionally, the small
    thrusters are available to use every two weeks to zero out the momentum
    buildup in the Reaction Wheels and to perform station-keeping maneuvers
    while in the mission orbit.
 
    The Attitude Control System (ACS) will determine spacecraft attitude,
    guidance to reach the desired pointing vector, and use actuators to
    achieve the desired pointing vector. Additionally, the ACS will
    provide pointing support for High Gain Antenna and Solar Array.
 
    The ACS consists of:
 
    1. Sensors
       a. Star Trackers (2)
       b. Inertial Reference Unit (1)
       c. Coarse Sun Sensors (10)
    2. Actuators
       a. Reaction Wheels (4)
       b. 20-Newton ACS thrusters (8)
 
    The Propulsion Deployment Electronics (PDE) component will provide
    thruster  control as well as inhibit during launch. GN&C Flight
    software (FSW) will  be executed within the C&DH Single Board Computer
    (SBC).
 
    Four reaction wheels have the primary purpose of managing nadir pointing
    requirement for the spacecraft, and will be used initially as the
    primary  means of orienting the spacecraft after separation from the
    launch vehicle. The mass of each wheel is 13.2 kg, 18 inches in
    diameter, and 6 inches in  height. The fourth reaction wheel allows for
    redundancy throughout the mission, such that any one reaction wheel
    failure will allow the mission to continue. Momentum dumping is
    forecast at approximately two-week intervals throughout the mission,
    performed by the attitude control system (small)  thrusters.
 
    The wheels are mounted on the spacecraft structure. Operationally they
    will be 'off' at launch and will not be turned 'on' until after launch
    vehicle separation. At that time, the wheels will be powered and will
    begin to adjust the angular momentum vector that results from the
    separation sequence.
 
    Thermal Control System
    ----------------------
 
    The Thermal Control system basic design contains four major elements:
    the  spacecraft bus (avionics, reaction wheels, and battery), instrument
    module, propulsion module, and deployables (high gain antenna and solar
    array). The overall orbiter is designed with mainly zenith directed
    radiators providing minimal exposure to the lunar environment.
 
    Most avionics are thermally coupled into an embedded constant
    conductance heat pipe (CCHP) aluminum honeycomb panel.  Dual bore
    header heat pipes couple the isothermal panel to a CCHP radiator that
    is separately mounted on the zenith surface of the spacecraft.
 
    For the reaction wheel assemblies, two baseplate heat pipes are
    connected to two header pipes, that are then routed to the back of the
    Iso-Thermal Panel through a hole in the structural panel.
 
    The Lithium Ion battery is maintained on a separate CCHP network with
    two heat pipes mounted on its sidewalls, and an additional pipe coupled
    to the sidewalls to provide additional reliability (one fault
    tolerance).
 
    A de-coupled instrument optical bench (low thermal distortion) uses low
    coefficient of thermal expansion (CTE) M55J material, is fully
    blanketed, and is heated with low density heaters to maintain cold
    limit temperatures. The CRaTER and LEND instruments are provided with
    individual radiators that are thermostatically controlled. Mini-RF
    electronics are attached to the avionics header. The Diviner
    electronics box is mounted on the iso-thermal panel, while the
    remaining instruments are thermally isolated.
 
    Within the propulsion module, most components are attached to a
    temperature controlled cylinder that is part of the spacecraft bus
    structure, to include the upper propellant tank, pyro valves, and high
    and low pressure panels. Thruster valves are coupled to the spacecraft
    and tailored to survive soak-back after burn sequences. The lower
    propellant tank is thermally coupled to the aft deck for structural
    reasons. Remaining lines not on the structural cylinder are
    independently heated.
 
    The High Gain Antenna uses multi-layer insulation (MLI), thermal
    isolation, and heaters to maintain temperatures within allowable
    limits. The gimbal assembly has four heater circuits and two radiators
    to serve the actuators and rotary joints. The laser ranging telescope
    (mounted on the HGA) has a dedicated heater circuit with MLI thermal
    isolation. Optical fiber from the laser ranging telescope has a copper
    strap coupled to the high gain antenna structure. The solar array
    assembly uses MLI and heater control to maintain actuators and dampers.
 
    Communications System
    ---------------------
 
    The communications system consists of S-band forward and return links to
    support command, communications, tracking and telemetry, and a Ka-band
    return link for telemetry and science data transfer.
 
    S-Band forward link data rate is fixed at 4 kbps. The S-Band return
    link data rate is selectable on orbit and varies from 125 bps to 256
    kbps. The Ka-band return link is also selectable on orbit and varies
    from 25 Mbps to 100 Mbps.
 
    The Ka-band sub-system includes a Ka-Band modulator, a Traveling Wave
    Tube Amplifier (TWTA) consisting of a traveling wave tube (TWT), an
    Electronic Power Conditioner (EPC), and a High Power Isolator.  The
    S-Band subsystem consists of one Spacecraft Tracking and Data Network
    (STDN) compatible transponder, an S-band RF Switch, and the RF paths to
    and from the TT&C omni-directional antennas and the S-band feed on the
    High Gain Antenna (HGA).
 
    The Ka-band uses only the High Gain Antenna. The S-band can utilize
    either the Omni-directional or the High Gain Antennae as controlled
    through the RF transfer switch.
 
    Diplexers allow the transponder's receiver and transmitter to connect to
    a common antenna port that in turn connects to the appropriate RF
    network for each antenna system. The diplexers also include band pass
    and band reject filters in the transmit channel to suppress any receive
    signal component in the output of the transmitting power amplifier.
 
    The traveling wave tube amplifier (TWTA) operates in a bandwidth of 300
    MHZ  (+/- 150 MHz) with a voltage standing wave ratio (VWSR) of 2:1.
    Output power is a minimum of 40 Watts.  On/off commands are generated
    through a 28V signal into the electronic power conditioner (EPC).
 
    Data Storage Boards (DSB)
    -------------------------
 
    The four DSB cards are designed as a file system which handles the
    storage and retrieval of files.  The DSBs provide 384 Giga bits (Gbits)
    at Beginning of Life (BOL) of memory capacity for incoming data files
    for a 17.5 hour minimum science data and HK data collection.
 
    The DSB receive dedicated +3.3VDC MEM power for the main power source
    and +15 SWITCH power to power the switches that allow the SBC to turn
    off individual cards. Power is received via the backplane cPCI
    connector.
 
    Data transfer to and from the SBC is via a cPCI interface on the
    backplane.
 
    Instrument Module
    -----------------
 
    The instrument module includes a graphite composite optical bench with
    honeycomb panels, inserts, and spools.  Flexures for mounting the
    instruments are titanium. Three instruments are mounted on the optical
    bench (LAMP, LOLA, LROC) and the remainder are on the spacecraft bus
    (Diviner, Crater, LEND, and the mini-RF antenna). Star Trackers
    complete the instrument module.
 
    The Instrument module (IM) is of a 'Wine Box' design, which reduces mass
    (fewer fasteners) and increases stiffness with continuous bond lines
    (not just connected at fasteners). The entire structure has a low
    coefficient of thermal expansion (CTE) made of graphite material
    (M55/CyanateEster Q.I. sheets). Insert material is Titanium with BR127
    electrical conductive primer.
 
    LRO SCIENCE INSTRUMENTS
    ---------------------------
 
    LRO investigations provide the following high-priority measurement sets:
 
    1. Characterization of the deep space radiation environment in lunar
       orbit, including neutron albedo (especially at energies in excess of 10
       MeV, as well as:
       a. Characterization of biological effects caused by exposure to the
          lunar orbital radiation environment
       b. Characterization of changes in the properties of multifunctional
          radiation shielding materials caused by extended exposure to the
          lunar orbital environment
    2. Geodetic lunar global topography (at landing-site relevant scales)
    3. High spatial resolution hydrogen mapping of the Moon's surface
    4. Temperature mapping in the Moon's polar shadowed regions
    5. Landform-scale imaging of lunar surfaces in permanently shadowed
       regions
    6. Identification of putative deposits of appreciable near-surface water
       ice in the Moon's polar cold traps
    7. Assessment of meter and smaller-scale features to facilitate safety
       analysis for potential lunar landing sites
    8. Characterization of the illumination environment in the Moon's
       polar regions at relevant temporal scales (i.e., in terms of hours)
 
    Six instruments were selected for LRO to provide these measurement sets
    as well as ancillary datasets relevant to numerous outstanding lunar
    science questions. These instruments are:
 
    1. Cosmic Ray Telescope for the Effects of Radiation (CRaTER):
 
    CRaTER will investigate the effect of galactic cosmic rays on tissue-
    equivalent plastics as a constraint on models of biological response to
    background space radiation. Specific science and measurement objectives
    are:
 
    a. Measure and characterize the Linear Energy Transfer (LET) spectra of
       galactic and solar cosmic rays (particularly above 10 MeV) in the deep
       space radiation environment most critically important to the
       engineering and modeling communities to assure safe, long-term human
       presence in space.
    b. Develop a simple, compact, and comparatively low-cost instrument,
       based on previously flown instruments, with a sufficiently large
       geometric factor to measure LET spectra and its time variation
       globally in the lunar orbit.
    c. Investigate the effects of shielding by measuring LET spectra behind
       different amounts and types of areal density materials, including
       tissue- equivalent plastic.
    d. Test models of radiation effects and shielding by verifying/validating
       model predictions of LET spectra with LRO measurements, using
       high-quality galactic cosmic rays (GCR) and solar energetic protons
       (SEP) spectra available contemporaneously with ongoing/planned NASA
       (ACE, STEREO, SAMPEX) and other agency spacecraft (NOAA-GOES).
 
    2. Diviner Lunar Radiometer Experiment (DLRE):
 
    DLRE will chart the temperature of the entire lunar surface at
    approximately 500 meter horizontal scales to identify cold-traps and
    potential ice deposits. Specific science and measurement objectives are:
 
    a. Map Global Day/Night Surface Temperature
    b. Characterize Thermal Environments for Habitability
    c. Determine Rock Abundances Globally and at Landing Sites
    d. Identify Potential Polar Ice Reservoirs
    e. Map Variations in Silicate Mineralogy
 
    3. Lyman-Alpha Mapping Project (LAMP):
 
    The Lyman-Alpha Mapping Project (LAMP) will observe virtually the entire
    lunar surface in the far ultraviolet. LAMP will search for surface ices
    and frosts in the polar regions and provide frost abundance, landform
    and surface UV spectral maps of permanently shadowed regions illuminated
    only by starlight and interplanetary Lyman alpha. Specific science and
    measurement objectives are:
 
    a. Identify and pinpoint surface exposed frost in Permanently
       Shadowed Regions (PSRs).
    b. Map all permanently shadowed regions with resolutions down to 100m.
    c. Demonstrate the feasibility of natural starlight and Lyman-Alpha
       sky-glow illumination for future lunar surface mission applications.
    d. Assay the lunar atmosphere and its variability.
 
    4. Lunar Exploration Neutron Detector (LEND):
 
    LEND will map the flux of neutrons from the lunar surface to search for
    evidence of water ice, and will provide space radiation environment
    measurements that may be useful for future human exploration. Specific
    science and measurement objectives are:
 
    a. Determine hydrogen content of the subsurface at the polar regions with
       spatial resolution of 10km and with sensitivity to concentration
       variations of 100 parts per million (ppm) at the poles.
    b. Characterization of surface distribution and column density of
       possible near-surface water ice deposits in the Moon's polar cold
       traps.
    c. Global mapping of Lunar neutron emissions at an altitude of 30-50 km
       above Moon's surface, with a spatial resolution of 5 km (pixel radius)
       at the spectral range of thermal energies up to 15 MeV.
 
    5. Lunar Orbiter Laser Altimeter (LOLA):
 
    LOLA will determine the global topography of the lunar surface at high
    resolution, measure landing site slopes, surface roughness, and search
    for possible polar surface ice in shadowed regions. Specific science and
    measurement objectives are:
 
    a. Global Geodetic Lunar Topography.
    b. Characterize Polar Region Illumination.
    c. Image Permanently Shadowed Regions.
    d. Contribute to the assessment of meter-scale features to facilitate
       landing-site selection.
    e. Identify surface polar ice, if present.
 
    6. Lunar Reconnaissance Orbiter Camera (LROC):
 
    LROC will acquire targeted narrow angle images of the lunar surface
    capable of resolving meter-scale features to support landing site
    selection, as well as wide-angle images to characterize polar
    illumination conditions and to identify potential resources. Specific
    science and measurement objectives are:
 
    a. Landing site identification and certification, with unambiguous
       identification of meter-scale hazards.
    b. Mapping of permanent shadows and sunlit regions.
    c. Meter-scale mapping of polar regions.
    d. Repeat observations to enable derivation of meter-scale topography.
    e. Global multispectral imaging to map ilmenite and other minerals.
    f. Global black and white morphology base map.
    g. Characterize regolith properties.
    h. Determine recent small impactor rates by re-imaging regions
       photographed with the Apollo Panoramic Camera (1-2 meter m/pixel).
 
    Instrument Host Overview - SCN
    ================================
 
    The primary function of the SCN is to provide two-way communications
    between the Earth and the LRO spacecraft. S-band is used to support
    commanding (4 kbps), telemetry, and tracking. Ka-band telemetry (100
    Mbps) is used to downlink science instrument data. During operations
    after commissioning, the SCN consists of the White Sands 1 (WS1) ground
    station, S-Band Sites, and Laser Ranging (LR) site. WS1 transmits s-band
    commands to the spacecraft and receives both s-band telemetry and
    Ka-band data from the spacecraft. The S-Band Sites consist of 4
    Universal Space Network (USN) sites and Deep Space Network (DSN) as
    back-up, for transmitting s-band commands to the spacecraft and
    receiving s-band telemetry from the spacecraft. The Laser Ranging
    facility transmits laser pulses to the spacecraft as part of the
    capability of computing the range to the spacecraft.
 
    The WS1 facility includes an 18-meter S/Ka-band antenna at White Sands
    Complex (WSC), New Mexico.  The USN facilities include: a USN 13-meter
    s-band antenna at South Point, Hawaii; a German Aerospace Center (DLR)
    15-meter s-band antenna at Weilheim, Germany; a Swedish Space
    Corporation (SSC) 13-meter s-band antenna at Kiruna, Sweden; and, a USN
    13-meter s-band antenna at Dongara, Australia.  The DSN facilities
    include: a 34-meter s-band antenna at Goldstone, California; a 34-meter
    s-band antenna at Madrid, Spain; and, a 34-meter s-band antenna at
    Canberra, Australia.
 
    The LR site in Greenbelt, Maryland transmits 532 nm laser pulses to the
    LRO spacecraft. The receiver telescope on the spacecraft High Gain
    Antenna System (HGAS) provides the Lunar Orbiter Laser Altimeter (LOLA)
    instrument with the LR signal via LOLA channel 1. LR range data are sent
    from the LOLA instrument to the spacecraft and are then included in LOLA
    telemetry sent to the LRO Mission Operations Center (MOC), which in turn
    provides these data to the LOLA Science Operations Center (SOC). The SOC
    computes the range to the spacecraft.

        