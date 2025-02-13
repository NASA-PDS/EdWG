
 
  Instrument Host Overview
  ========================
    For most Mars Odyssey experiments, data were collected by
    instruments on the spacecraft.  Those data were then relayed
    via the telemetry system to stations of the NASA Deep Space
    Network (DSN) on the ground.  Radio Science observations (such
    as radio tracking) required that DSN hardware also participate
    in data acquisition.  The following sections provide an
    overview first of the spacecraft and then of the DSN ground
    system as both supported Mars Odyssey science activities.
 
 
  Instrument Host Overview - Spacecraft
  =====================================
    The Mars Odyssey spacecraft was built by Lockheed Martin
    Astronautics (LMA).  The spacecraft structure was divided into
    two modules: the equipment module and the propulsion module.
    The shape was not uniform, but can be approximated by
    envisioning a box 2.2 x 1.7 x 2.6 meters.  The framework was
    composed of aluminum and titanium.  Most spacecraft systems
    were redundant in order to provide backup should a device fail.
    For more information, see [JPLD-16303].
 
    Command and Data Handling
    -------------------------
      This subsystem handled all computing functions for Mars
      Odyssey.  It ran the flight software and controlled the
      spacecraft through interface electronics.  The system was
      based around a RAD6000 computer with 128 megabytes of
      random access memory (RAM) and 3 megabytes non-volatile
      memory, which allowed data to be maintained by the system
      in the event of a power failure.  The interface
      electronics were computer cards that communicated with
      external peripherals.  The cards fit into the computer's
      main board.  There were two identical sets of the
      computer and interface electronics for back up in case
      one failed.  One card was not redundant.  It was a one
      gigabyte mass memory card that was used to store imaging
      data.
 
    Telecommunications
    ------------------
      The telecommunication subsystem was composed of two parts.
      The first was a radio system that operated in the X-band
      microwave frequency range.  It was used for communications
      between Earth and the spacecraft.  The other system operated
      in the ultra high frequency (UHF) range for communications
      between future Mars landers and Odyssey.
 
      Communication between the spacecraft and Earth occurred
      through the use of three antennas.  The high-gain antenna was
      a dish with 1.3 meter diameter (4.25 feet).  It was used
      during the late Cruise and Science and relay phases of the
      mission when data rates were high.  It simultaneously
      received commands from Earth and transmitted science data to
      Earth.  The medium-gain antenna was a 7.1 cm (2.8 inch) wide
      rectangular horn antenna that protruded through the high-gain
      dish.  The low-gain antenna was 4.4 cm (1.75 inches) and
      provided wide- angle communications in emergencies or when
      the high-gain antenna was not pointed directly at Earth.
 
    Electrical Power
    ----------------
      A 7 square meter (75 square feet) solar panel containing an
      array of gallium arsenide cells generated power for the
      spacecraft.  The power distribution and drive unit sent power
      to the electrical loads of the spacecraft through a system of
      switches.
 
    Guidance, Navigation and Control
    --------------------------------
      This subsystem used three redundant pairs of sensors to
      determine the spacecraft's attitude.  A star camera was used
      to look at star fields and a sun sensor detected the position
      of the Sun in order to back up the star camera.  The inertial
      measurement unit collected spacecraft orientation data
      between star camera updates.  The reaction wheels along with
      the thrusters operated to control the attitude.  There were
      four reaction wheels - three primary and one for backup.
      Odyssey was a three-axis stabilized spacecraft.
 
    Propulsion
    ----------
      The propulsion system comprised a main engine, which aided in
      placing Odyssey in orbit around Mars, and sets of small
      thrusters, which performed attitude control and trajectory
      correction maneuvers.  The main engine produced a thrust of
      about 695 Newtons (156 pounds of force).  Each of the four
      attitude controlling thrusters produced a thrust of 0.9
      Newtons (0.2 pounds of force) and the four spacecraft turning
      thrusters produced a force of 22 Newtons (5 pounds of force).
      The propulsion system also included one gaseous helium tank
      used to pressurize the fuel and oxidizer tanks, miscellaneous
      tubing, pyro valves, and filters.
 
    Structures
    ----------
      The spacecraft was composed of two modules - propulsion and
      equipment.  The propulsion module contained tanks, thrusters,
      and associated plumbing.  The equipment module consisted of
      the equipment deck, which supported the Mars Radiation
      Environment Experiment (MARIE), and engineering components.
      The other component of the equipment module was the science
      deck which housed the Thermal Emission Imaging System
      (THEMIS), Gamma Ray Spectrometer (GRS), High-Energy Neutron
      Detector (HEND), Neutron Spectrometer (NS), and star cameras
      on top and engineering components and the GRS central
      electronics box on the underside.
 
    Thermal Control
    ---------------
      A combination of heaters, radiators, louvers, blankets, and
      thermal coatings maintained each spacecraft component's
      temperature within its allowable limits.
 
    Mechanisms
    ----------
      Odyssey functioned via several mechanisms, many of which were
      associated with the high-gain antenna.  The antenna was
      locked down during launch, cruise, and aerobraking through
      three 'retention and release devices,' or latches.  The
      antenna was released and deployed with a motor-driven hinge
      once the science orbit around Mars was attained. A two-axis
      gimbal assembly controlled the position of the antenna. The
      solar array used four latches which folded together and
      locked down the panels during launch.  After deployment, a
      two-axis gimbal assembly controlled the solar array.  The
      last mechanism was a latch for the deployment of the 6-meter
      GRS boom.
 
    Flight Software
    ---------------
      Odyssey received commands from Earth via radio and then
      translated them into spacecraft actions. The flight software
      had the capability to run many sequences concurrently in
      addition to executing received commands immediately.
 
      The data collection software was quite flexible.  The science
      and engineering data were collected and then put in a variety
      of holding bins called Application Identifiers (APIDs).  Ground
      commands could easily modify the data routing and sampling
      frequency.
 
      A number of autonomous spacecraft performance functions were
      part of the flight software.  The spacecraft ran routines
      to control attitude and orientation without commands sent
      from Earth.  The software also executed fault protection
      routines to determine if any internal problem occurred.  If
      a problem was found, a number of automatic preset actions
      would occur to resolve the problem and put the spacecraft
      into a standby mode until ground controllers provided
      further direction.
 
    Coordinate System
    -----------------
      The spacecraft frame is defined with the X axis parallel to
      the stowed HGA boresight, the Y axis normal to the stowed
      solar arrays, and the Z axis in the direction of the main
      engine thrust (see figure below).  The origin of the frame
      is centered on the launch vehicle separation plane.
 
                                 _______________ HGA
                                 \             /
              Science        ..   `._________.'
               Orbit         || ._______________.
             Velocity        || |       ^+Xsc   | Science Deck
                ^.           || |       |       |
                  `.         || |       |       |
                    `.       || +Ysc    |       |
                             ||@| <-----o +Zsc (out of page)
                             || |               |
                             || |               |
                             || | Science Deck  |
                      Solar  || ._______________.
                      Array  ..
 
                                   /
                                  /
                                 /
                                V Nadir
 
 
  Instrument Host Overview - DSN
  ==============================
    The Deep Space Network is a telecommunications facility managed
    by the Jet Propulsion Laboratory of the California Institute of
    Technology for the U.S. National Aeronautics and Space
    Administration (NASA).
 
    The primary function of the DSN is to provide two-way
    communications between the Earth and spacecraft exploring the
    solar system.  To carry out this function it is equipped with
    high-power transmitters, low-noise amplifiers and receivers,
    and appropriate monitoring and control systems.
 
    The DSN consists of three complexes situated at approximately
    equally spaced longitudinal intervals around the globe at
    Goldstone (near Barstow, California), Robledo (near Madrid,
    Spain), and Tidbinbilla (near Canberra, Australia).  Two of
    the complexes are located in the Northern Hemisphere while the
    third is in the Southern Hemisphere.
 
    Each complex includes several antennas, defined by their
    diameters, construction, or operational characteristics:
    70-m diameter, standard 34-m diameter, high-efficiency 34-m
    diameter (HEF), and 34-m beam waveguide (BWG).

        