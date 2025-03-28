
 
  Instrument Host Overview
  =========================
 
  For typical Radio Science experiments on other missions, the link
  from the spacecraft to the DSN stations contains the primary science
  content of the experiment, which makes the DSN a part of the
  extended Radio Science instrument.  For GRAIL this is partly true.
  There are two data types, the primary is from the links between the
  spacecraft, and those data become available via telemetry.  The
  second type is a one-way X-band Doppler link from each spacecraft to
  the DSN stations. This science link supplements the LGRS on-board
  observations and, again, make the DSN a part of the GRAIL science
  instrumentation.  The following sections provide an overview of the
  spacecraft and their science instruments followed by the DSN ground
  system.
 
 
  Instrument Host Overview - Spacecraft
  =====================================
 
    Gravity Recovery and Interior Laboratory Spacecraft
    ---------------------------------------------------
    The GRAIL spacecraft design was based on the Lockheed Martin (LM)
    Experimental Small Satellite-11 technology demonstration mission
    for the United States Air Force, and the avionics were derived
    from NASA's Mars Reconnaissance Orbiter. A single-string
    architecture met this short mission's reliability requirements.
    The resulting design met all GRAIL mission and science
    requirements with ample technical margins, providing flexibility
    to solve problems that might arise during development and which
    met or exceeded design principles established by the Jet
    Propulsion Laboratory.
 
    Each of the two GRAIL spacecraft, GRAIL-A and GRAIL-B, was about
    the size of a washing machine and had about 200 kg of mass. They
    were nearly identical; but the need to point antennas at one
    another required differences in the MoonKAM mounting and in the
    angles of the star trackers used for attitude control and the
    antennas through which the orbiters measured the changing
    distance between them. These factors also required that GRAIL-B
    precede GRAIL-A in lunar orbit.
 
    Each spacecraft bus was a rectangular composite structure. The
    science payload ranging antennas were in thermal enclosures and
    were mounted so that they were nominally on the line between the
    centers of mass of the two spacecraft. The other components of the
    payload instrument were on a single interior bus panel for easy
    integration and testing.
 
    Two non-articulated solar arrays of XSS-11 heritage were deployed
    just after separation from the launch vehicle. Warm gas systems,
    identical to those on XSS-11, provided delta-V for maneuvers and
    unloading of the 3 reaction wheels. Additional attitude sensing
    components included an inertial measurement unit (IMU), a sun
    sensor and a star tracker.
 
    Command and Data Handling (C&DH), power management, and the
    lithium ion battery also had XSS-11 heritage. The S-band
    telecommunications sub-system for communication with the DSN used
    components with heritage from Themis and Genesis.
 
    The spacecraft was built and the science payload was integrated
    and tested at Lockheed Martin's Denver facility. LM used two
    system-level spacecraft test labs (STL) and one software simulator
    (SoftSim) testbed with unlimited copies that enabled integration
    and verification of all hardware and software throughout the
    Assembly Test and Launch Operations (ATLO) cycle.
 
    See [HOFFMAN2009] for more information about the spacecraft.
 
    Spacecraft Configurations
    -------------------------
    During its mission, GRAIL needed to operate in four distinct
    mission configurations.
 
    Launch: During launch, the two spacecraft had to be fitted together
    within the nose cone, or payload fairing, of the launch vehicle.
    Large parts, such as the solar arrays, were designed to be folded
    up.
 
    Cruise: As soon as the two spacecraft were clear of the launch
    vehicle, the body-fixed solar arrays were deployed to begin
    producing power. The high-gain antenna also became operational.
 
    Lunar Orbit Insertion: The lunar orbit insertion required numerous
    maneuvers to circularize the two orbits. No science observations
    took place, as the spacecraft were not in formation flying yet.
 
    Science Operations: During the Science Phase, the two spacecraft
    were placed in a precision formation flying configuration in order
    to point to each other and exchange two radio links at Ka- and
    S-bands.
 
    Coordinate Systems
    ------------------
 
    Two coordinate systems are used to reference the various GRAIL
    instruments. The definitions are summarized below.
 
    1) Mechanical Frame (MF): This is defined by the spacecraft
    manufacturer. It is the reference frame for such things as KBR
    horn location, center of mass, and thruster locations.
 
    +X = Parallel to, and in opposite direction from, the solar array
    normal vector
    +Z = Normal to star tracker bus plate
    +Y = +Z ? +X
 
    An onboard attitude control sub-system approximately orients the
    mechanical frame with -Z along the line of flight and -/+ Y
    pointed towards the moon.
 
    2) Science Reference Frame (SRF): This is the Mechanical Frame as
    realized by the Star Tracker. If the Star Tracker were perfectly
    aligned, MF would equal SRF. SRF is the reference frame for GRAIL
    science measurements.
 
    Major Spacecraft Components
    ---------------------------
    Science Payload Instruments:
 
    There are two payload elements on each GRAIL orbiter: the Lunar
    Gravity Ranging System (LGRS) which is the science instrument, and
    the MoonKAM lunar-imager which is used for Education and Public
    Outreach. The LGRS is based on the instrument used for the Gravity
    Recovery and Climate Experiment (GRACE) mission, which has been
    mapping Earth's gravity since 2002. The LGRS is responsible for
    sending and receiving the signals needed to accurately and
    precisely measure the changes in range between the two orbiters.
    The LGRS consists of an Ultra-Stable Oscillator (USO), Microwave
    Assembly (MWA), a Time-Transfer Assembly (TTA), and the Gravity
    Recovery Processor Assembly (GPA).
 
    The USO provides a steady reference signal that is used by all of
    the instrument subsystems. Within the LGRS, the USO provides the
    reference frequency for the MWA and the TTA. The MWA converts the
    USO reference signal to the Ka-band frequency, which is
    transmitted to the other orbiter.
 
    The function of the TTA is to provide a two-way time-transfer link
    between the spacecraft to both synchronize and measure the clock
    offset between the two LGRS clocks. The TTA generates an S-band
    signal from the USO reference frequency and sends a GPS-like
    ranging code to the other spacecraft. The GPA combines all the
    inputs received from the MWA and TTA to produce the radiometric
    data that are downlinked to the ground. In addition to acquiring
    the inter-spacecraft measurements, the LGRS also provides a
    one-way signal to the ground based on the USO, which is
    transmitted via the X-band Radio Science Beacon (RSB). The
    steady-state drift of the USO is measured via the one-way Doppler
    data provided by the RSB.
 
    The LGRS instrument is summarized below.
 
         2 X-band beacon antennas for Doppler ranging measurements
           when the spacecraft was visible from Earth. The X-band
           signal was carrier-only and not
         1 S-band time-transfer system antenna, which sent a
           time-synchronization code back and forth between the
           spacecraft
         1 Ka-band ranging antenna for precision distance measurement
           between the spacecraft
 
    For more information on the GRAIL radio systems, see
    [KLIPSTEINETAL2009].
 
    Structures:
 
    The solar panels and antennas were body fixed, so there were no
    moving parts in the spacecraft structure that would affect science
    observations.
 
    Telecommunications Sub-System:
 
    The telecom sub-system included the following on each spacecraft:
 
         2 S-band transponder antennas to communicate with Earth
 
    Each of the pairs of S-band transponder antennas had one antenna
    mounted on the sunny side of the spacecraft and one mounted on the
    dark side. The sunny-side antennas pointed to Earth during the
    full moon and the dark-side antennas pointed to Earth during new
    moon. This design obviated the need to mechanically rotate the
    antennas during the mission, which would have moved the
    spacecraft's center of mass with respect to the Ka-Band ranging
    and X-Band beacon paths, disturbing the science measurements.
 
    Propulsion Sub-System:
 
    The propulsion sub-system on each spacecraft included:
 
    A propellant tank, which could hold up to 103.5 kilograms of the
    monopropellant hydrazine.
 
    A hydrazine catalytic thruster for lunar-orbit insertion and
    trajectory changes, and a warm-gas system with 8 thruster valves
    for attitude control and other small maneuvers.
 
    Command and Data-Handling Sub-System:
 
    The C&DH sub-system controlled all spacecraft functions. This
    system:
 
         * managed all forms of data on the spacecraft;
         * executed commands (including maneuver commands) sent from
           Earth;
         * prepared data for transmission to Earth;
         * managed collection of solar power and charging of the
           batteries;
         * collected and processed information about all sub-systems
           and payloads;
         * kept and distributed the spacecraft time;
         * calculated spacecraft position in orbit around the Moon;
         * autonomously monitored and responded to any onboard
           problems that occurred.
 
    The key parts of this system were:
 
         Space Flight Computer
         Flight Software
         Solid State Recorder
 
    Attitude Control Sub-system:
 
    The Attiude Control Sub-system (ACS) controlled the orientation of
    the orbiter as it traveled through space and maintained knowledge
    of where celestial bodies were located -- for example, Earth and
    the Sun. This knowledge was critical for the spacecraft to perform
    the correct maneuvers to get to the Moon, to keep its solar arrays
    pointed toward the Sun for battery charging, and to keep its
    S-Band antenna pointed toward the Earth in order to maintain
    communications.
 
    Once in orbit around the Moon, the ACS also maintained constant
    knowledge of where the spacecraft was in its orbit.
 
    The Attitude Control sub-system provided three-axis stabilized
    control and consisted of a sun sensor, a star tracker, reaction
    wheels, and an inertial measurement unit.
 
    Electrical Power:
 
    The electrical power sub-system was responsible for generating,
    storing, and distributing power to the orbiter systems. The
    electrical power system included two solar arrays and a lithium
    ion battery. Each solar array was capable of producing 700 watts
    at the end of the mission. The arrays were deployed shortly after
    separation from the launch vehicle and remained fixed throughout
    the mission. Each battery had a capacity of 30 amp-hours and was
    used to provide power when the spacecraft was in the Moon's
    shadow.
 
    Solar panels: The only source of replenishable power is sunlight.
    Solar panels are mounted one side of each orbiter and capable in a
    body-fixed position.
 
    Thermal Sub-Systems:
 
    The thermal sub-system maintained the right temperatures in all
    parts of the spacecraft. It employed several conduction- and
    radiation-based techniques for thermal control.  Its components
    included:
 
         Radiators
         Surface coatings
         Thermal blankets
         Heaters
 
 
  Instrument Host Overview - DSN
  ==============================
 
  Radio Science investigations utilized instrumentation with elements
  both on the spacecraft and at the NASA Deep Space Network (DSN).
  Much of this was shared equipment, being used for routine
  telecommunications as well as for Radio Science.
 
  The Deep Space Network was a telecommunications facility managed by
  the Jet Propulsion Laboratory of the California Institute of
  Technology for the U.S.  National Aeronautics and Space
  Administration.
 
  The primary function of the DSN was to provide two-way
  communications between the Earth and spacecraft exploring the solar
  system.  To carry out this function the DSN was equipped with
  high-power transmitters, low-noise amplifiers and receivers, and
  appropriate monitoring and control systems.
 
  The DSN consisted of three complexes situated at approximately
  equally spaced longitudinal intervals around the globe at Goldstone
  (near Barstow, California), Robledo (near Madrid, Spain), and
  Tidbinbilla (near Canberra, Australia).  Two of the complexes were
  located in the northern hemisphere while the third was in the
  southern hemisphere.
 
  The network comprised four subnets, each of which included one
  antenna at each complex.  The four subnets were defined according to
  the properties of their respective antennas: 70-m diameter, standard
  34-m diameter, high-efficiency 34-m diameter, and 26-m diameter.
 
  These DSN complexes, in conjunction with telecommunications
  subsystems onboard planetary spacecraft, constituted the major
  elements of instrumentation for radio science investigations.

        