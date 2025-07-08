
 
  Instrument Host Overview
  ========================
    Lunar Prospector (LP) is a small, simple, spin-stabilized spacecraft
    with minimal operational requirements [BINDERETAL1998].  Its fueled
    mass is 305 kg.  The spacecraft bus is a graphite-epoxy drum that is
    1.37 m in diameter and 1.28 m tall.  Power is provided by solar
    cells mounted on the surface of the bus assembly, which produce an
    average of 186 w.  There is also a rechargeable, 4.8 amp-hr NiCd
    battery for power during night side passes.  The science instruments
    are mounted on three 2.5 m booms.  The Gamma Ray Spectrometer is
    mounted on one boom, the Neutron Spectrometer and Alpha Particle
    Spectrometers are mounted on another boom, and the Magnetometer and
    Electron Reflectometer are mounted on the third boom.  The
    Magnetometer instrument is mounted on a 1.2 m long boom extending
    beyond the main boom to isolate it from the Electron Reflectometer.
 
    The spacecraft bus houses three fuel tanks, six engines, and five
    electronic units.  The fuel tanks at launch hold 138 kg of hydrazine
    pressurized with helium.  There are two aft axial engines, two
    forward axial engines, and two tangential engines.
 
    The communication system consists of an S-band transponder, an omni
    antenna with 3-pi steradian antenna pattern for uplink and downlink,
    and a medium gain antenna for downlink.  The engineering-only
    downlink data rate is 300 bps and the science/engineering downlink
    data rate is 3600 bps.
 
    Command and control of the spacecraft is achieved by a simple
    Command and Data Handling (C&DH) unit.  As an individual command is
    uplinked to the spacecraft, the C&DH directs the command to the
    appropriate subsystem.  All science and engineering data are
    collected by the C&DH and then are buffered and formatted for
    downlink by the C&DH.  The data are downlinked at 1800 bps
    immediately and simultaneously dumped into a solid state recorder.
    The data stored on the solid state recorder is downlinked 53 minutes
    later.  These delayed data frames are interleaved into the real-time
    data stream, yielding a total downlink rate of 3600 bps.  The
    purpose of the delayed stream is to receive data acquired during
    communications blackout periods and to eliminate the need for a
    commandable data recorder.
 
    The LP spacecraft clock or frame counter increments once every 2
    seconds.  It is stored in a 24-bit register.  This means that the
    clock will reset after about 33.5 million seconds or about once per
    year.  The clock reset on January 30, 1999 at about 12:09 UTC, which
    was early in the Extended Mission.
 
 
  Spacecraft Coordinate System
  ============================
    The Trans-Lunar Injection (TLI) stage and spacecraft body
    coordinate system is discussed below.  The origin of
    coordinates is: a) in the separation plane between the
    spacecraft and the adapter of the TLI stage; and b) at the
    geometric center of the equilateral triangle defined by the
    bolt holes for the separation nuts.
 
    The Z axis is normal to the separation plane.  The +Z direction
    is towards the medium gain antenna (forward) end of the
    spacecraft.  The X axis is in the separation plane between the
    spacecraft and the adapter of the TLI stage.  The -X direction
    is parallel to the centerline of instrument boom No.  1 and
    towards the Gamma Ray Spectrometer.  The Y axis is defined by
    the right-hand rule.
 
 
  Instrument Host Overview - DSN
  ==============================
    The Deep Space Network (DSN) is a telecommunications facility
    managed by the Jet Propulsion Laboratory of the California Institute
    of Technology for the U.S. National Aeronautics and Space
    Administration (NASA).
 
    The primary function of the DSN is to provide two-way communications
    between the Earth and spacecraft exploring the solar system.  To
    carry out this function it is equipped with high-power transmitters,
    low-noise amplifiers and receivers, and appropriate monitoring and
    control systems.
 
    The DSN consists of three complexes situated at approximately
    equally spaced longitudinal intervals around the globe at Goldstone
    (near Barstow, California), Robledo (near Madrid, Spain), and
    Tidbinbilla (near Canberra, Australia).  Two of the complexes are
    located in the northern hemisphere while the third is in the
    southern hemisphere.
 
    Each complex includes several antennas, defined by their diameters,
    construction, or operational characteristics: 70-m diameter,
    standard 34-m diameter, high-efficiency 34-m diameter (HEF), and
    34-m beam waveguide (BWG).  These DSN complexes, in conjunction with
    telecommunications subsystems onboard planetary spacecraft,
    constitute the major elements of instrumentation for radio science
    investigations.
 
    For more information see [ASMAR&RENZETTI1993].
 
 
  Science Packages
  ================
    The Lunar Prospector spacecraft has five science instruments.  The
    instruments are a Gamma Ray Spectrometer (GRS), a Neutron
    Spectrometer (NS), an Alpha Particle Spectrometer (APS), a
    Magnetometer (MAG), and an Electron Reflectometer (ER).  A Doppler
    Gravity Experiment (DGE) uses Doppler tracking data for deriving
    gravity measurements.  In addition, the spacecraft spin rate and
    attitude are determined on the ground from data derived from a sun
    sensor and an IR Earth/Moon limb crossing sensor.

        