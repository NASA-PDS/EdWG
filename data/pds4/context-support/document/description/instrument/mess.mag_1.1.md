
 
    The MErcury Surface, Space ENvironment, GEochemistry and Ranging
    (MESSENGER) mission is designed to orbit Mercury following one Earth
    flyby, two flybys of Venus and three of Mercury.  It launched in
    August 2004 and will use these flybys to achieve an orbit insertion
    around Mercury in March 2011.  Initial data collection will begin
    during the three flybys of Mercury, and will primarily consist of
    global mapping and measurements of the surface, atmosphere and
    magnetosphere composition.  MESSENGER will remain in orbit for the
    rest of the nominal mission, which is scheduled to end in March
    2012. Once in orbit around Mercury it will begin a series of
    observations using multiple instruments. These observations will
    provide data to answer questions about the nature and composition of
    the crust, tectonic history, the structure of the atmosphere and
    magnetosphere, and the nature of the polar caps.
 
    The science objectives of the MESSENGER Magnetometer (MAG) are to
    determine the structure and the origin of the intrinsic magnetic
    field of Mercury, and to characterize the solar-wind interaction
    with the planet.  The magnetic field data are also needed to
    interpret data from the Energetic Particle and Plasma Spectrometer.
    The MAG instrument is a miniature three-axis ring-core fluxgate
    magnetometer with low-noise electronics.  It is mounted on a 3.6 m
    boom in the anti-sunward direction.  The MAG has +/- 1530 and +/-
    51300 nT ranges with 20-bit internal resolution and 17-bit output
    resolution.  The MAG probe samples magnetic field values along the
    X, Y, and Z axes at a rate of 20 samples/second.  The data passes
    through an A/D converter where it is also filtered by the hardware.
    The MAG software interfaces with the MAG electronics via
    memory-mapped I/O for data collection, range control, and
    electronics calibration.
 
    The MAG software receives vector magnetic field samples, 20 bits per
    X, Y, and Z axes, from the MAG electronics at 20 Hz.  After bias
    removal, it filters and sub samples this data to generate output
    data samples at the commanded rate: 0.01, 0.02, 0.05, 0.1, 0.2, 0.5,
    1, 2, 5, 10 or 20 samples/second.  The MAG software consistently
    builds science records with compressed (if commanded) MAG data
    obtained from the above processing for transmission to the DPU via
    CCSDS telemetry packets.
 
    Furthermore, the MAG software detects magnetic bursts during a
    commandable time period during orbit.  The detection is done by
    passing the field samples of a selected axis from the bias removal
    logic through a 1 to 10 Hz pass-band filter and determining a log AC
    value from this data.  If this value indicates that the magnetic
    field is fluctuating above a trigger level, burst data over eight
    consecutive minutes is collected, compressed, and sent to the DPU
    via CCSDS telemetry packets.
 
    Finally, the MAG software collects housekeeping data indicating the
    state of the MAG instrument and software for packaging into
    low-rate- housekeeping (LRH) telemetry packets.
 
    The MAG instrument is described in full detail in
    [ANDERSONETAL2007].

        