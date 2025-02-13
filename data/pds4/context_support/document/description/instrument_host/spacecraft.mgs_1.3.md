
 
    Instrument Host Overview
    ========================
      For most Mars Global Surveyor experiments, data were collected
      by instruments on the spacecraft.  Those data were then relayed
      via the telemetry system to stations of the NASA Deep Space
      Network (DSN) on the ground.  Radio Science experiments (such
      as radio occultations) required that DSN hardware also
      participate in data acquisition.  The following sections
      provide an overview first of the spacecraft and then of the
      DSN ground system as both supported Mars Global Surveyor
      science activities.
 
 
    Instrument Host Overview - Spacecraft
    =====================================
      The Mars Global Surveyor (MGS) spacecraft was built by
      Lockheed Martin Astronautics (LMA).  The spacecraft structure
      included four subassemblies: the equipment module, the
      propulsion module, the solar array support structure, and the
      high-gain antenna (HGA) support structure.
 
      The equipment module housed the avionics packages and science
      instruments.  Its dimensions were 1.221 x 1.221 x 0.762 meters
      in X, Y, and Z, respectively.  With the exception of the
      Magnetometer, all of the science instruments were bolted to
      the nadir equipment deck, mounted above the equipment module on
      the +Z panel.  The Mars Relay antenna was the tallest
      instrument rising 1.115 meters above the nadir equipment deck.
 
      Inside, two identical computers orchestrated almost all of
      the spacecraft's flight activities.  Although only one of the
      two units controlled Surveyor at any one time, identical
      software ran concurrently in the backup unit in case of an
      emergency.  Each computer consisted of a Marconi 1750A
      microprocessor, 128 Kbytes of RAM for storage, and 20 Kbytes
      of ROM that contained code to run basic survival routines in
      the event that the computers experienced a reset.
 
      Additional storage for science and spacecraft health data
      was provided by two solid-state recorders with a combined
      capacity of 375 megabytes.  Mars Global Surveyor was NASA's
      first planetary spacecraft to use RAM exclusively (instead of
      a tape recorder) for mass data storage.  This technological
      improvement reduced operational complexity and cost.
 
      The equipment module also housed three 'reaction wheels'
      mounted at right angles to each other.  By transferring angular
      momentum to and from the rapidly spinning reaction wheels, MGS
      flight computers could control the spacecraft attitude to high
      precision.  A fourth reaction wheel, mounted in a direction
      skewed to the other three, provided redundancy and backup.
 
      Sun sensors were placed at several locations about the
      spacecraft.  They provided basic information on spacecraft
      attitude -- namely, a rough vector toward the Sun.  Their
      primary use was during attitude reinitialization after a
      spacecraft anomaly.
 
      The Inertial Measurement Unit (IMU) contained gyroscopes
      and accelerometers to measure angular rates and linear
      accelerations.  Angular rate measurements were used to
      determine yaw attitude during the Mapping Phase.  The IMU
      also provided inertial attitude control, as might be
      required during maneuvers.
 
      The Mars Horizon Sensor Assembly (MHSA) determined the horizon
      as seen from the spacecraft; from this, an empirical nadir
      could be derived for pointing the science instruments.  The
      MHSA was mounted to the +Z panel of the equipment module, next
      to the science instruments.
 
      The Celestial Sensor Assembly (CSA) complemented the IMU by
      providing attitude data based on determination of positions
      of known stars.  It was used during the Cruise Phase and Orbit
      Insertion Phase for both attitude determination and control.
      It was also used when precise attitude knowledge was required
      during the Mapping Phase.  The CSA was mounted to the +Z panel
      of the equipment module, next to the science instruments.
 
      The propulsion module contained the propellant tanks, main
      engines, propulsion feed system and attitude control
      thrusters.  It was a rectangular box 1.063 meters on a side
      and was bolted to the equipment module on the latter's -Z
      panel.  The propulsion module also served as the adaptor to
      the launch vehicle.
 
      Propulsion was provided by a dual mode bi-propellant system
      using nitrogen tetroxide (NTO) and hydrazine.  This dual mode
      differed from conventional bi-propellant systems in that the
      hydrazine was used by both the main engine and the attitude
      control thrusters, rather than having separate hydrazine
      tanks for each.  The main engine was the only one that used
      the bi-propellant system.  The main engine maximum thrust
      was 659 N.  It was used for major maneuvers including large
      trajectory corrections during Cruise, Mars orbit injection
      (MOI), and transfer to the Mapping orbit (TMO).
 
      Four rocket engine modules (REM), each containing three 4.45 N
      thrusters, were provided.  Each REM contained two aft-facing
      thrusters and one roll control thruster.  Four of the eight
      aft-facing thrusters were used for the smaller trajectory
      corrections during Cruise and for Orbit Trim Maneuvers (OTM)
      during Mapping; they could also be used for attitude control
      during main engine burns.  Two sets of four thrusters were on
      redundant strings so that one string could be isolated in the
      event of a failure.  Four thrusters were provided for
      attitude control.  In addition to their role during maneuvers,
      the 4.45 N thrusters were also used for momentum management.
 
      MGS carried about 385 kg of propellant; nearly 75 percent of
      that was used during MOI.
 
      Two solar arrays, each 3.53 meters long by 1.85 meters wide
      provided power.  Each array was mounted close to the top of
      the propulsion module on the +Y and -Y panels and near the
      interface between the propulsion and equipment modules.
      Including the adaptor that held the array to the propulsion
      module, the tip of each array was designed to stand 4.270
      meters from the side of the spacecraft.  During initial
      deployment, the -Y solar array yoke was damaged leaving its
      exact position and orientation in some doubt (and leading to
      several changes in mission design).  Rectangular, metal
      'drag flaps' were mounted to the end of each array; these
      flaps increased the total surface area of the structure and
      added another 0.813 meters to the overall dimensions.
      Between each array and flap was mounted a magnetometer sensor.
 
      Each array consisted of two panels, an inner and outer panel,
      comprised of gallium arsenide and silicon solar cells,
      respectively.  During mapping operations at Mars, the amount
      of power produced by the arrays varied from a high of 980
      Watts at perihelion to a low of 660 Watts at aphelion.
 
      While in orbit around Mars, the solar arrays provided
      power as MGS flew over the day side of the planet.  When
      the spacecraft passed over the night side, energy flowed
      from two nickel-hydrogen (NiH2) batteries, each with a
      capacity of about 20 Amp-hours.  Eclipses lasted from 36 to
      41 minutes per orbit; depth of battery discharge was limited
      to 27% except during emergencies.
 
      The high-gain antenna structure was also bolted to the
      outside of the propulsion module.  When fully deployed, the
      1.5-meter diameter antenna sat at the end of a 2-meter boom
      which was mounted to the +X panel of the propulsion module.
      Two rotating joints (gimbals) held the antenna to the boom
      and allowed the antenna to track and point at Earth while
      the science instruments observed Mars.
 
      One of the two main functions of the HGA was to receive
      command sequences sent by the flight operations
      team on Earth.  During command periods, data flowed to MGS
      at rates in multiples of two from 7.8125 bits per second
      (emergency rate) to 500 bits per second (750 commands per
      minute); the nominal rate was 125 bits per second.
 
      The other main function of the HGA was to send data back
      to Earth.  All transmissions from MGS utilized an X-band
      radio link near 8.4 gigahertz.  The transmitted power was
      about 25 watts.  Data rates as high as 85333 bits per second
      were used.
 
      The spacecraft was also equipped with four low-gain antennas
      (LGA), two for transmit and two for receive.  The LGAs were
      used in Inner Cruise, during special events such as maneuvers,
      during aerobraking, and for emergency communications following
      a spacecraft anomaly.
 
      The primary transmitting low-gain antenna (LGT1) was mounted
      on the traveling wave tube amplifier (TWTA) enclosure, which
      was mounted on the rim of the HGA reflector; its boresight
      was aligned with the HGA boresight, which was in the +X
      direction until HGA deployment.  The backup (LGT2) was also
      mounted on the TWTA enclosure.  LGT2 boresight was aligned
      at a cant angle approximately 160 degrees away from the
      shared boresights of the HGA and LGT1.  This angle was chosen
      to minimize the consequences of a gimbal failure once
      articulation commenced after deployment of the HGA boom in
      mapping orbit.  LGT2 was not used prior to HGA deployment
      because its orientation and proximity to the nadir payload
      deck would lead to irradiation of the payload instruments
      while the HGA was in its stowed position.  One receiving LGA
      (LGR) was mounted on the -X panel of the equipment module;
      the other was on the +X side of the propulsion module.
 
      The spacecraft was equipped with an experimental Ka-band
      downlink radio system.  The transmitter converted the X-band
      signal to 32 Ghz and amplified it to about 0.5 watts; the
      Ka-band output was radiated through the HGA.
 
      The spacecraft +Z axis vector was normal to the nadir equipment
      deck; the main engine was aimed in the -Z direction.  The -X
      axis vector was in the direction of the velocity vector during
      nominal Mapping (e.g., May 1999).  +X was in the direction of
      the HGA boresight during Cruise, and the HGA boom was mounted to
      the +X panel of the propulsion module.  The +Y axis completed an
      orthogonal rectangular coordinate system.  The +/-Y axes defined
      generally the deployment directions of the solar panels.  The
      solar cells themselves were on the -Z sides of the panels.
 
      There were three levels of anomaly response in the spacecraft
      flight software.  The first, emergency mode, was entered in
      response to a command-loss timeout.  Entry into emergency mode
      reconfigured the telecom subsystem to its lowest data rate
      settings to enhance the chances of successful contact from
      Earth.  After a programmable period of time in emergency mode,
      the spacecraft transitioneds to contingency mode.
 
      Contingency mode was entered by four paths: failure to regain
      contact with Earth while in emergency mode, power-related faults
      such as gimbal faults and low battery state of charge, loss of
      inertial reference, and explicit ground command.  Contingency
      mode sets telecom rates to their minimum values, turneds off
      non-essential power loads (including the payload), disableds
      stored sequences not explicitly specified as enabled for this
      mode, and changeds the spacecraft attitude to sun-coning to
      optimize power and communications.
 
      Safe mode was the deepest level of anomaly response.  It couldan be
      be entered by three paths: failures of key spacecraft components
      that could cannot be corrected by normal fault protection, power-on
      reset of both Spacecraft Control Processors (SCPs), or explicit
      ground command.  The response to safe mode entry was similar to
      that of contingency mode.  Safe mode program code for the SCP was
      executed from Programmable Read-Only-Memory (PROM).
 
      For more information on the spacecraft and mission see
      [JPLD-12088].
 
 
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

        