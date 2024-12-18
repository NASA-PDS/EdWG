
 
  Instrument Host Overview
  ========================
    For most Mars Exploration Rover (MER) experiments, data were
    collected by instruments on the spacecraft.  Those data were then
    relayed directly to stations of the NASA Deep Space Network (DSN)
    on Earth or indirectly using the Mars orbiters Mars Global Surveyor
    (MGS) or 2001 Mars Odyssey (ODY).  MER Radio Science observations
    required that DSN and/or ODY hardware also participate in data
    acquisition.  The following sections provide an overview first of
    the MER spacecraft, then of the DSN ground system, and finally of
    2001 Mars Odyssey as each supported MER science activities.
 
 
  Instrument Host Overview - Rover
  ================================
    The Mars Exploration Rover (MER) mission sent two identical
    spacecraft to two different landing sites on Mars.  The hardware on
    the first spacecraft is referred to as MER-2 (the rover named
    Spirit which was sent to Gusev Crater), and the hardware on
    the second spacecraft is referred to as MER-1 (the rover named
    Opportunity sent to Meridiani Planum).  The spacecraft design owed a
    lot of its heritage to the Mars Pathfinder configuration for cruise
    and entry, descent, and landing.  For more detailed information on
    the MER spacecraft, see [CRISPETAL2003].
 
 
    Spacecraft Configuration for Entry, Descent, and Landing
    --------------------------------------------------------
      After separation from the cruise stage, the 840 kg entry vehicle
      consisted of a backshell and heatshield enclosing the lander.  The
      550 kg lander had a tetrahedral structure that the air bags were
      deployed from and surrounded, and that housed the gas generators
      for the airbags, the RADAR altimeter, motors for the unfolding of
      the tetrahedron's four sides or 'petals,' and the rover lift
      mechanism for standing up the rover.  On route to Mars, the rover
      was stowed within the lander, and contained most of the power,
      computing, and communication electronics for all phases of the
      mission.  The backshell and heatshield provided thermal protection
      from the hyperbolic entry into the Martian atmosphere through the
      use of ablating materials.  Mounted inside the backshell was the
      parachute, the deceleration and transverse impulse solid
      rocket (TIRS) motors, a backshell inertial measurement unit, and
      thermal batteries for the entry and descent phase.  The Entry,
      Descent, and Landing camera was mounted on the lander radar
      bracket.  The Descent Image Motion Estimation Subsystem (DIMES)
      gathered the results of a real-time image correlation of surface
      features contained in three successive Entry, Descent, and Landing
      camera images of the Martian surface to compute the horizontal
      velocity of the descending vehicle. TIRS used this horizontal
      velocity measurement along with measurements of the attitude of
      the backshell to compute a TIRS rocket firing solution.
 
 
    Rover on the Surface of Mars
    ----------------------------
      After landing, the instrument host for each spacecraft is just the
      rover itself, which is a 6-wheeled drive, 4-wheel-steered vehicle
      180 kg in mass, including the science package.  At its wheel base,
      the rover is approximately 141 cm long and 122 cm wide.  At the
      height of the solar panel, the rover is approximately 225 cm wide
      by 151 cm long.  In its deployed configuration with the Pancam
      Mast Assembly (PMA) deployed, the rover is 154 cm tall.
 
      The rocker bogie suspension system gave the rover the ability to
      drive over obstacles approximately one wheel diameter (26 cm) in
      size while providing a stable platform for instrument
      measurements.  The distribution of mass of the vehicle allowed the
      vehicle to be stable even at a 45 degree tilt.  Each wheel and
      steering degree of freedom was independently actuated, which
      allowed the vehicle to turn in place (turning diameter 1.9 m), to
      skid steer to a tighter angle (turning diameter as small
      as 0.9 m), to turn in gradual arcs, or to drag wheels that
      effectively trench the Martian regolith.  When moving on flat
      terrain, the vehicle could achieve a top speed of 5 cm/s.  Under
      autonomous control using its hazard avoidance system, the rover
      drove with an average speed of about 1 cm/sec.
 
      The rover was powered by a combination of solar arrays and
      rechargeable batteries.  The solar panel provides 30 strings of
      triple junction cells (gallium indium phosphorus, gallium
      arsenide, and germanium) covering 1.3 square meters, which
      produced about 800 to 900 W hours per sol at the beginning of the
      MER mission.  Each rover had two reference solar cells, one that
      measures short circuit current and another that measures open
      circuit voltage.  Due to the change in season from late southern
      summer to early southern autumn, and the degradation in
      performance due to dust deposition, the energy produced by this
      array dropped to about 600 W h per sol, 90 sols after landing.
      Energy was stored in two 8 A h lithium ion rechargeable batteries
      to provide over 400 W h of energy to support rover peak power
      operations and provide auxiliary heating and operations overnight.
 
      Temperature-sensitive electronics were housed in the rover warm
      electronics box (WEB) which is a box built with honeycomb
      composite material and insulated with 2.5 cm of opacified aerogel.
      A combination of radioisotope heater units, waste heat from
      electronics, and auxiliary heating by survival heaters ensured
      that the internal electronics were maintained between -40 and +50
      degrees C as the external Mars environment cycle ranged from 0 to
      -97 degrees C.  Survival heating in the WEB requires not more than
      100 W h of energy during the coldest environment conditions.  The
      rechargeable batteries housed in the WEB supplied this energy.
 
      The rover received commands and transmitted data to the Earth
      through two distinct systems: a direct-to-Earth X-band system
      supported by both a low-gain antenna and a steerable high-gain
      antenna (HGA), and a UHF system supported by a monopole antenna
      which enables relay communication to orbiters at Mars.  Early in
      the surface mission, the X-band system through the high-gain
      antenna supported up to 28.8 kbps to a 70 m Deep Space Network
      (DSN) station.  Commands were received through the high-gain
      antenna at a rate of up to 2000 bps.  The X-band system through
      the low-gain antenna provided a minimum capability of transmitting
      telemetry at 40 bps and receiving commands at 40 bps throughout
      the MER missions.  The UHF system supported telemetry rates of up
      to 256 kbps during orbiter passes which lasted up to 8 minutes
      each.  The UHF system also supported a command receipt capability
      of 8 kbps through Odyssey only.
 
      The computing, command, and data handling functions of the rover
      were supported by a 20 MHz 32-bit RAD6000 processor housed in a
      Versa Module Europa (VME) card cage.  This radiation hardened
      processor had access to 128 Mbytes of DRAM and 256 Mbytes of
      nonvolatile flash memory that supported a multiprocess C-coded
      software architecture.  This system, supported by auxiliary
      processing functions housed on boards within the VME card cage,
      had the capability to acquire images from pairs of cameras, drive
      up to 10 motors simultaneously from 35 motors located on the
      vehicle, and process data from three spectrometers.  The
      multiprocess architecture allowed communication, image
      acquisition, and operation of payload elements to proceed
      simultaneously.
 
      During the surface mission, the rovers communicated on X-band
      typically once a day, reporting on status and the results of the
      execution of commands transmitted that day.  Data were also
      relayed through the UHF communication system to the Mars Global
      Surveyor and Mars Odyssey orbiters.  Useful over-flights by these
      orbiters at the landing site occurred as frequently as twice
      per day per orbiter.
 
      Each rover carried the Athena Science Payload consisting of two
      remote sensing instruments that viewed the terrain from the top of
      a mast 154 cm above the ground, four devices for in-situ analysis
      on the end of a robotic arm and several magnets and calibration
      targets.  [SQUYRESETAL2003] describes this payload, the mast, the
      robotic arm, and the plans for science investigation in more
      detail.  Azimuth and elevation actuators permitted the collection
      of data sets for specific targets, regions, or full 360-degree
      panoramas from the mast instruments, which are the stereo
      multispectral Panoramic Camera (Pancam) and Miniature Thermal
      Emission Spectrometer (Mini-TES).  The five degree-of-freedom
      robotic arm positioned the following devices on rocks and soils
      for in-situ analysis or rock abrasion: Alpha Particle X-ray
      Spectrometer (APXS), Moessbauer Spectrometer (MB), Microscopic
      Imager (MI), and Rock Abrasion Tool (RAT).
 
      In addition, the stereo navigation cameras (Navcams) mounted on
      the top of the mast and the stereo hazard detection cameras
      (Hazcams) pointed towards the ground beneath the solar panels in
      the front and rear of the rover were required for engineering
      purposes (rover navigation, hazard avoidance, and safe movement
      purposes and positioning of the robotic arm), but were also used
      for science analysis [MAKIETAL2003].  [ARVIDSONETAL2003] provides
      more detail on the use of rover engineering sensors for assessing
      terrain and soil physical properties, dust accumulation, and
      other related investigations.
 
      The MER rover coordinate frame is defined as follows:
 
      -- +Zr axis is normal to the rover top deck plane and points down,
         from the top deck toward the wheels;
 
      -- +Xr axis is parallel to the rover top deck plane and points
         from the center of the top deck toward the PMA assembly;
 
      -- +Yr completes the right hand frame.
 
      The origin of the MER rover 'navigation' frame is directly above
      the middle wheels, as shown in the diagram below.  A separate
      MER rover 'mechanical' frame has its origin 29 cm toward the
      front wheels (in the +Xr direction) but is otherwise identical.
 
                                 UHF    /\
                         HGA            \/ PMA
                          .--.    #     ||
                         /    \   #     ||
                        |      |  #     ||
                         \    /=. #     ||
                          `--' || #     ||                 Rover
                       =======================           (deployed)
                             |    =o=.    |
                             |  .' Yr `.__|o====o
                           .===o=== o------> Xr \\
                          .-.      .|.    `.-.  ##o###
                         | o |    | | |   | o |
                          `-'      `|'     `-'
                                    V Zr
 
 
  Instrument Host Overview - DSN
  ==============================
    The Deep Space Network is a telecommunications facility managed
    by the Jet Propulsion Laboratory of the California Institute of
    Technology for the U.S.  National Aeronautics and Space
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
    the complexes are located in the northern hemisphere while the
    third is in the southern hemisphere.
 
    Each complex includes several antennas, defined by their
    diameters, construction, or operational characteristics:
    70-m diameter, standard 34-m diameter, high-efficiency 34-m
    diameter (HEF), and 34-m beam waveguide (BWG).
 
    For more information see [ASMAR&RENZETTI1993].
 
 
  Instrument Host Overview - 2001 Mars Odyssey
  ============================================
    The 2001 Mars Odyssey (ODY) spacecraft was built by Lockheed Martin
    Astronautics (LMA).  Most spacecraft systems were redundant
    in order to provide backup should a device fail.  In addition
    to transmitting data collected by ODY instruments and systems,
    the telecommunications system was used to relay data from Mars
    surface assets and measure their relative motion radiometrically
    in the 400 MHz frequency range.  For more information, see
    [JPLD-16303].

        