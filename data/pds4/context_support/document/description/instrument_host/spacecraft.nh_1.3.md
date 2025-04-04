
 
This description is based on several sources used with the
permission of the New Horizons project, SWRI and JHU/APL:
 
- Stern & Spencer, New Horizons: The First Reconnaissance Mission to
  Bodies in the Kuiper Belt, 2004 [STERN&SPENCER2004A]
 
- The New Horizons web page originally at
  http://pluto.jhuapl.edu/
 
 
  Overview
  ========
    The New Horizons spacecraft observatory includes propulsion,
    navigation, and communications systems, plus the payload. The
    spacecraft is roughly 2.5 meters across and its mass is 465 kg
    including propellant. Design features include 64 Gbits of redundant
    solid-state data storage, a 290 m/s propulsion budget, and the
    capability to transmit data from 32 AU at almost 1 kilobit/second.
 
    The instrument payload [Stern & Cheng, 2002, STERN&CHENG2002]
    comprises the two-sensor RALPH Vis-IR remote sensing package, the
    ALICE UV imaging spectrometer, the REX radio/radiometry experiment,
    the two-sensor PEPSSI/SWAP plasma suite, the LORRI long-focal-length
    imager, and the SDC student-built dust counter.
 
 
  Payload
  =======
    The New Horizons team selected instruments that not only directly
    measure NASA-specified items of interest (NASA AO 01-OSS-01, 2001,
    [NASAAO2001]), but also provide backup to other instruments on the
    spacecraft should one fail during the mission.
 
    The payload comprises seven instruments:
 
 
    RALPH
    -----
      The main objectives for the RALPH instrument are to obtain high
      resolution color maps and surface composition maps of the surfaces
      of Pluto and Charon. The instrument has two separate channels: the
      Multispectral Visible Imaging Camera (MVIC) and the Linear Etalon
      Imaging Spectral Array (LEISA). A single telescope with a 3-inch
      (6-centimeter) aperture collects and focuses the light used in both
      channels.
 
      RALPH/MVIC operates at visible wavelengths and has 4 different
      filters for producing color maps. One filter allows measurement of
      the methane frost distribution over the surface, while the others
      are more generic and cover blue, red and near-infrared colors,
      respectively. MVIC also has two panchromatic filters that pass
      essentially all visible light.  This will be useful for low-light
      level observations requiring maximum sensitivity.  In all cases,
      the light passes from the telescope through the filters and is
      focused onto a charge coupled device (CCD).
 
      RALPH/LEISA operates at infrared wavelengths, and its etalon (a filter
      with a narrow spectral bandpass that varies linearly in one dimension)
      is bonded to the illuminated side of the IR detector.  As a result,
      each row of detector pixels receives only light of a particular
      wavelength.  Spectral maps are produced by sweeping the FOV of the
      instrument across a scene, sequentially sampling each point in the
      scene at each wavelength.  LEISA maps the distribution of frosts of
      methane (CH4), molecular nitrogen (N2), carbon monoxide (CO), and
      water (H2O) over the surface of Pluto and the water frost
      distribution over the surface of Charon.  LEISA data may also reveal
      new constituents on the surfaces that have never before been detected.
 
    ALICE
    -----
      Alice is an ultraviolet imaging spectrometer that probes the
      atmospheric composition of Pluto.
 
      Alice has two modes of operation: an airglow mode, which measures
      emissions from atmospheric constituents, and an occultation mode,
      which views either the Sun or a bright star through the atmosphere
      producing absorption by the atmospheric constituents. The Alice
      occultation mode occurs just after New Horizons passes behind Pluto
      and looks back at the Sun through the Pluto atmosphere.
 
 
    REX
    ---
      REX is an acronym for Radio EXperiment. It is integrated into the
      New Horizons radio telecommunications system.
 
      Using an occultation technique similar to that described above for
      the Alice instrument, REX probes the Pluto atmosphere. After New
      Horizons flies by Pluto, its 2.1 meter radio antenna points back at
      Earth. On Earth, powerful radio transmitters in the NASA Deep Space
      Network (DSN) point at New Horizons and send radio signals to the
      spacecraft.  As the spacecraft passes behind Pluto, the atmosphere
      bends the radio waves by an amount that depends on the average
      molecular weight of the gas in the atmosphere, the atmospheric
      temperature, and the closest approach distance of the raypath at
      each instant of time. REX samples the received radio signal and
      sends the data back to Earth for analysis
 
      REX also has a radiometry mode, which measures the weak radio
      thermal emission from Pluto itself. When REX looks back at Pluto
      following the flyby, radiometry data are taken to derive a value for
      the Pluto nightside temperature.
 
 
    LORRI
    -----
      The instrument that provides the highest spatial resolution on New
      Horizons is LORRI - short for LOng Range Reconnaissance Imager -
      which comprises a telescope with a 20.8cm aperture that focuses
      visible light onto a charge coupled device (CCD). LORRI has a very
      simple design; there are no filters or moving parts. Near the time
      of closest approach, LORRI takes images of the Pluto surface at 100m
      resolution.
 
 
    SWAP
    ----
      The Solar Wind Analyzer around Pluto (SWAP) instrument measures
      charged particles from the solar wind near Pluto to determine
      whether Pluto has a magnetosphere and how fast the atmosphere is
      escaping.
 
 
    PEPSSI
    ------
      Another plasma-sensing instrument, the Pluto Energetic Particle
      Spectrometer Science Investigation (PEPSSI), searches for neutral
      atoms that escape the Pluto atmosphere and subsequently become
      charged by their interaction with the solar wind.
 
    SDC
    ---
      The Student Dust Counter, which was later re-named The Venetia
      Burney Student Dust Counter (SDC), is an Education and Public
      Outreach project.  SDC measures the dust density of the
      Interplanetary Dust Particles (IDP) by measuring the charge
      generated in the SDC sensor from dust impact events.  From this may
      be inferred the size and distribution of dust particles along the
      entire New Horizons trajectory, including regions of interplanetary
      space never before sampled.  Such dust particles are created by
      comets shedding material and Kuiper Belt Objects (KBOs) colliding
      with other KBOs.  The SDC is managed and was built primarily by
      students at the University of Colorado in Boulder, with supervision
      from professional space scientists.
 
 
  Spacecraft reference frame (a.k.a. Coordinate system)
  =====================================================
    During hibernation and other periods of inactivity, the spacecraft is
    designed to spin about its +Y axis, which is also the nominal
    boresight of the High Gain Antenna (HGA) and REX.  Imaging instruments
    have nominal boresights pointing along the -X spacecraft axis.  The
    RTG (see Power below) is a cylinder extending out along the +X
    spacecraft axis to keep it away from the instruments.  The +Z axis
    completes a right-handed three-dimensional Cartesian coordinate
    system.  Note that each instrument has its own reference frame.
 
    The following two sketches, extracted from the SPICE Frames kernel,
    represent the spacecraft as viewed from the spacecraft +X and +Y
    directions.  The instrument locations are approximate; refer to
    [STERNETAL2008] and [FOUNTAINETAL2008] for more detail.
 
 
Spacecraft sketches
===================
     +X view:
     --------
                                     o
                                    /|\
                                   / | \
                                  /  |  \
                                 /   |   \
                                /    |    \
                               /     |     \
           ___________________/______|______\__________________
           `-.                                   HGA(REX)   ,-'
              `-.                                        ,-'
                 `-.                                  ,-'  __
                    `-.____________________________,-'    /  / PEPSSI
            __________/_\________________________/_\_____|___|
         .-|                |               |                |______
   Alice | |                |      RTG      |                |     ||
         '-|                |     .-*-.     |                |_____|| SWAP
           |                |    /     \    |                |     ||
      |----|                |    \     /    |                |     ||
      |    |                |     '-.-'     |                |
Ralph |___ |                |               |                |
      |    |________________|_______________|________________|
                           |         +X (out of page)
                          /__<------o_________\
                            +Zsc    |       adapter ring
                                    |
                                    |
                                    V
                                     -Ysc
 
 
 
 
     +Y view:
     --------
 
           ______
           ------
             ||   SWAP
            ----
           _|__|______   __..---..__
          | |  \     _`-'           ``-.   HGA(REX)
   PEPSSI | ----  _'     `-_            `-.
          |     .'          `-_            `.
        .-|   ,                `-_           `.
  LORRI : |  .                    `-_          `.
        : | /                        `-_         \
        '-|.                            `-_       . _______   _______
          |'                .-*-.          `-_    ||+|+|+|+| |+|+|+|+|
          |                /     \            `|--`-------------------|
          |               !   o-----> +X       |  |                   |
          |                \  |  /           _,|--.-------------------|
 ASTR 1 \ |.                '-|-'         _,-     ||+|+|+|+| |+|+|+|+|
        \\|'                  |        _,-        ' -------   -------
  Star   \| '                 V     _,-          /    RTG (Radioisotope
Trackers  |  `               +Z  _,-            .          Thermoelectric
         /|   `               _,-              -           Generator)
        //|    `.          _,-               .'
 ASTR 2 / |       '.    _,-              _.-'
          |__________',-__         __,,,'
            |     |       ' --- '
            |     |
            `-----'  Alice and Ralph
 
 
  Communications
  ==============
    The spacecraft has three antenna systems:  Low-, Medium- and High-Gain
    Antennas (LGA, MGA, HGA).  The New Horizons mission operations team
    communicates with the spacecraft through the Deep Space Network (DSN).
    The DSN comprises facilities in the Mojave Desert in California; near
    Madrid, Spain; and near Canberra, Australia.
 
 
  Power
  =====
    Electrical power for the New Horizons spacecraft and science
    instruments is provided by a single radioisotope thermoelectric
    generator, or RTG, supplied by the Department of Energy.  The New
    Horizons trajectory takes it more than 4 billion miles from Earth,
    where light from the Sun is 1,000 times fainter than at Earth.  An RTG
    is used on missions, such as New Horizons, that can not use solar
    power - yet require a proven, reliable power supply that can produce
    up to several kilowatts of power and operate under severe
    environmental conditions for many years.
 
    Carrying out the New Horizons mission safely is a top priority at
    NASA. As part of that focus, NASA informed the public about use by New
    Horizons of an RTG by publishing a detailed Environmental Impact
    Statement - or EIS - and several fact sheets. The Final EIS, which
    includes public comments on the Draft EIS and the NASA responses to
    those comments, was released in July 2005.
 
 
  Propulsion
  ==========
    The propulsion system (see [FOUNTAINETAL2008], section 3) includes
    twelve 0.8N thrusters, four 4.4N thrusters, and the hydrazine
    propellant tank and associated control valves. The titanium
    propellant/pressurant tank feeds the thrusters through a system
    filter, a flow control orifice, and a set of latch valves that prevent
    flow of the fuel until commanded to the open position after launch.
    Helium was selected as the tank pressurant instead of nitrogen to
    allow the loading of an additional kilogram of hydrazine. Measurements
    of tank pressure and temperatures at various points in the system
    allow the mission operations team to monitor system performance and
    the amount of fuel remaining in the tank.
 
    The 16 rocket engine assemblies (REAs) are organized into 8 sets and
    placed on the spacecraft as shown in Figure 5. Pairs of the 0.8N
    thrusters (each thruster from a different set) are usually fired to
    produce torques and control rotation about one of the three spacecraft
    axes. The one exception to the use of coupled thruster firings to
    control spacecraft rates is that of controlling rates about the
    spacecraft X axis during science observations, where uncoupled
    thruster firings are required to meet the maximum spacecraft drift
    rates allowed during this operation mode. Control rates for each of
    the spacecraft axes are shown below in Table II. One pair of the 4.4N
    thrusters is aligned along the -Y spacecraft axis to provide delta-V
    for large propulsive events such as trajectory correction maneuvers
    (TCMs). The second pair of 4.4N thrusters is aligned to produce thrust
    along the +Y axis. These thrusters are rotated 45 degrees in the YZ
    plane to minimize the plume impingement on the HGA dish. The net
    propulsive effect of these thrusters is therefore reduced. They still
    provide the required redundancy and the ability to generate thrust in
    both directions without a 180-degree rotation of the spacecraft.
 
    Each thruster requires a heater to warm its catalyst bed to a minimum
    temperature prior to use. Each thruster catalyst bed has both a
    primary and a secondary heater element, with each element drawing
    approximately 2.2 W of power. Control of the catalyst bed heater
    circuits is grouped functionally by pairs (to minimize the number of
    switches required), so that a total of 16 switches control the heater
    elements, allowing great flexibility to operate the spacecraft safely
    while drawing the minimum required power. Operational requirements for
    catalyst bed heater
 
    The pulse duration and total on-time of each thruster are commanded
    very precisely, providing accurate control of the total impulse
    generated during a maneuver. The 0.8N thrusters can be turned on for
    periods as short as 5 ms. The initial propellant load was allocated
    between primary mission TCMs, attitude control (including science and
    communication operations), and primary mission margin. At the end of
    the primary mission, sufficient margin may allow for an extended
    mission to one or more objects in the Kuiper Belt. The original margin
    was augmented during the final mission preparations when the unused
    dry mass margin was converted to additional propellant.
 
    Given the mass and moments of inertia at launch, the delta-V
    propellant cost is approximately 4.9 m/s/kg. A change in spin rate of
    5 rpm (i.e., the change from the nominal spin rate to zero rpm for
    3-axis control mode) requires approximately 0.125 kg of hydrazine.
 
 
    Propellant budget allocations
    -----------------------------
                                        delta-V   Propellant
        Description                         m/s           kg
        -----------------------------   -------   ----------
        Primary mission TCM                 110         22.3
        Attitude control                    N/A         29.3
        Primary mission margin              132         25.2
         - original margin allocation      ( 91)       (17.5)
         - Additional margin obtained      ( 41)       (29.3)
           from unused spacecraft dry
           mass allocation
        Total navigation delta-V            242
        Total propellant load                           76.8

        