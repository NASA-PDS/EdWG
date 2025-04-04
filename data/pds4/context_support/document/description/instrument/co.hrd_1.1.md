
 
 
  Instrument Overview
  ===================
    Overview
    ========
 
    The High Rate Detector (HRD) is part of the Cosmic Dust Analyzer
    (CDA) on the Cassini mission payload.  The overall objective of
    the HRD is to carry out quantitative measurements of particle flux
    and mass distribution throughout the Saturn ring system. The
    particle impact rate and particle mass distribution will be
    determined with respect to Saturnian distances, distance from the
    rings, and to magnetospheric coordinates.  The particle mass range
    covered by the HRD (assuming a particle impact velocity of 15
    km/s) ranges from 8x10^-13 to 8x10^-8 g for differential and
    cumulative flux measurements, and > 8x10^-8 g for cumulative flux
    measurements.  For full information about the HRD instrument, see
    Srama et al. (2004).
 
    General Description
    ===================
 
    The HRD was designed, built and tested at the University of
    Chicago and measures differential and cumulative particle fluxes.
    The HRD has a high counting rate capability (up to 10^4 random
    impacts/s with <5% corrections) which will be particularly
    important during Saturn ring plane crossings, where fluxes are
    large enough to saturate the counting rate of DA (~1 c/s).
 
    The HRD has significant inheritance from the University of Chicago
    Dust Counter and Mass Analyzer instrument (DUCMA) flown earlier on
    the Vega-1 and Vega-2 spacecraft to Comet Halley (Perkins et al.,
    1985). The instrument employs the dust particle detection
    technique described by Simpson and Tuzzolino (1985) and consists
    of two polyvinylidene fluoride sensors with associated
    electronics. The PVDF sensors are round in shape with areas of 50
    cm^2 and 10 cm^2 respectively, and are mounted together as a unit
    on the front of the HRD electronics box. For images showing the
    geometry of the sensors see the figures in Srama et al. (2004).
    The HRD detects individual particles impacting the PVDF sensors
    and provides continuous measurements of cumulative particle fluxes
    for particle masses greater than four mass thresholds for each of
    the two sensors (see Table I).
 
    The HRD is an independent instrument containing its own memory and
    processor. The only interface to the Dust Analyzer (DA) of the CDA
    is via the power and data cables. HRD power is supplied by the DA
    main electronics and data transfer responds by latching the
    appropriate data into the HRD data output register. The latching
    of the data generates an interrupt to DA indicating that the data
    is ready to be read by DA and stored into DA memory.
 
    The HRD is rigidly mounted to the DA so that as the CDA turntable
    is rotated, the HRD scans different particle arrival directions.
    The HRD pointing is exactly the same as the DA pointing.
 
    HRD Instrument Specifications
    =============================
 
    Sensor #1: 50 cm^2, 28 microns thick PVDF detector;
    Sensor #2: 10 cm^2, 6 microns thick PVDF detector.
    Both sensors are sensitive to dust particles with velocity > 1
    km/s.
    Each sensor has four mass thresholds (M1, M2, M3, M4 for sensor #1
    and m1, m2, m3, m4 for sensor #2).These thresholds were set at
    values showing in the Table I for particles with a velocity of 15
    km/sec.
 
    Discrete events: recording of impact time (1 s accuracy) and
    threshold firings for each impact
    Counting rates: up to 10^4/s with no corrections, while for rates
    10^4 to 10^5 c/s the corrections have been determined and are
    known. We have not encountered such high rates during the entire
    Cassini mission
 
    Operating modes
    ===============
 
    1. NORMAL MODE (CRUISE): Continuous recording by the HRD of
    individual particle impact time, threshold firings for each
    impact, and integral counts.  This operating mode will be used for
    all interplanetary data collection.  It may also be used during
    ring plane crossings up to particle impact rates of approximately
    few hundred impacts/s.
 
    2. FAST MODE (ENCOUNTER, RING PLANE): Integral counts are recorded
    and stored by the HRD each At seconds during ring plane crossings.
    The time interval At is selectable at 0.1, 0.2, ..., 0.9, 1.0 s.
    At the highest time resolution (At = 0.1 s) the spatial resolution
    for the counting rates will be ~ 1 km.
 
    3. CALIBRATE MODE: Periodic electronic calibration of the HRD with
    the HRD inflight calibrator. This mode allows assessment of the
    electronic stability of the HRD throughout the mission.
 
    PVDF Dust Sensors
    =================
 
    The theory, fabrication and details of PVDF dust detector
    operation have been described in earlier reports (Simpson and
    Tuzzolino, 1985; Perkins et al., 1985; Simpson et al., 1989). A
    PVDF sensor consists of a thin film of permanently polarized
    material. A hypervelocity dust particle impacting the sensor
    produces rapid local destruction of dipoles (crater or penetration
    hole) which results in a large and fast current pulse at the input
    to the electronics (ns time range). The output pulse is sharp in
    time, with a maximum amplitude depending on impacting particle
    mass and velocity. Since the depolarization induced current pulse
    is fast, the output pulse shape is determined by the choice of
    electronic time constants for the pre-amplifiers and shapers.
    Electronic time constants (amplifier shaping time constants,
    discriminator width) in the few microsecond range permit a high
    counting rate capability for the HRD sensor-electronics
    combination (10^4 random impacts/s with <5% corrections). The high
    counting rate capability of the HRD is of particular importance
    for Saturn ring plane crossings, where high dust particle fluxes
    are encountered.
 
    Exposure Degradation of the PVDF Sensors
    ========================================
 
    The HRD PVDF detector efficiency is proportional to the detector
    area.
    It is expected that with exposure to high dust flux there will be
    some
    degradation of the detectors due to the physical removal of some
    of
    the area by the impacting dust particles.  However, for the small
    particles (most cosmic dust particles are less than 10 microns)
    the
    removed area is negligible compared to the total detector area of
    10 or 50 cm^2.
 
    Acoustic Signal Suppression
    ===========================
 
    PVDF detectors have a secondary but minor mode of response due to
    their piezoelectric properties. Therefore, background acoustic
    disturbances of sufficient intensity could trigger the HRD PVDF
    detector thresholds, and these threshold firings could be
    mistakenly recorded as dust particle impacts.  During the
    Cassini-Huygens mission, possible sources of acoustic disturbances
    include spacecraft gas jets, moving platforms, and large particle
    impacts on structures near the mounting positions of the HRD PVDF
    sensors.
 
    To minimize the effects of the possible acoustic backgrounds, the
    HRD PVDF sensors are mounted in sound absorbing pads. This design
    was highly effective in suppressing the acoustic response from
    mechanical shocks (Perkins et al., 1985).
 
    Thermal Aspects
    ===============
 
    Thermal Control. Although our studies have shown that PVDF sensors
    may be operated at temperatures up to ~+80 C for long periods of
    time (weeks) with small (<5%) degradation in dust particle
    response, our HRD sensor mounting technique, discussed above,
    acoustically and thermally insulates the sensor from its
    surroundings. Under these conditions, the effective sensor
    emissivity and absorbtivity are such that exposure of a PVDF
    sensor in space to direct solar illumination for a short period of
    time (~1 min) would result in sensor temperatures high enough to
    destroy the sensor.  Since there have been the possibility of
    direct exposure of the HRD sensors to solar illumination at a
    radial distance of 0.68 AU from the Sun during the Cassini-Huygens
    mission (Jaffe and Herrell, 1997), we studied different sensor
    coating techniques which would restrict the sensor temperature to
    ~80 C during solar exposure at 0.68 AU.
 
    Temperature dependence of sensor output signal
    ==============================================
 
    Of the several PVDF material parameters which determine the
    magnitude of the PVDF detector depolarization charge signal
    resulting from an impacting dust particle (Simpson and Tuzzolino,
    1985), the volume polarization magnitude, P, and its temperature
    dependence are the most important for determining the temperature
    dependence of the signal amplitude. Our laboratory measurements
    have shown that over the temperature range -50 to +80 C, the
    charge signal amplitude will vary by less than 6% from the values
    measured at room temperature. Thus, we expected an overall
    possible variation in output signal amplitude resulting from both
    detector capacitance and depolarization charge signal temperature
    effects of less than 10% over the expected temperature range for
    the detector. This maximum 10% effect will contribute a negligible
    uncertainty for the particle mass thresholds.
 
    HRD Electronics, Digital Data and Commands
    ==========================================
 
    The HRD linear electronics consists of charge sensitive
    pre-amplifiers (CSA), shaping amplifiers (SHAPER) and threshold
    discriminators. Each SHAPER provides single integration ~V single
    differentiation RC shaping with a shaping time constant of 2
    microsec.  A particle impact on either sensor #1 or sensor #2 will
    result in output signals from the shapers  which may trigger the
    M1, M2, M3, M4 thresholds for sensor #1, and m1, m2, m3, and m4
    for sensor #2. As a contingency either M or m, or both thresholds
    may be increased by a factor of 10 by ground command.
 
    Every time a dust particle hits one of the sensors, the event will
    increment one or more 16-bit counters associated with this
    particular sensor and set the 8-bit event latch, according to what
    thresholds are triggered. For a higher threshold to be fired, the
    lower threshold associated with the same sensor will also be
    fired. There are 4 thresholds for each detector and each threshold
    is connected to one of the counters. The thresholds for the large
    detector are indicated by M1, M2, M3, M4 and the thresholds for
    the smaller detector are indicated by m1, m2, m3, m4.  The 8-bit
    latch indicates which threshold fired when an event occurs.
 
    In normal mode if a discrete event occurs or data is requested by
    the
    Dust Analyzer instrument and the storage buffer is empty, the
    21-bit
    clock and the 8-bit latch are stored into HRD memory.  When 256
    discrete events have been stored, HRD stores the 64-byte header.
    The
    header consists of a 24-bit sync word, 8-bit HRD status, 32-bit
    HRD
    clock, 32-bit spacecraft clock, temperature, and the eight 16-bit
    counters.
 
    In fast mode, HRD will store the Fast Mode header at an interval
    form .1 sec to 1 sec, depending on which time interval is
    selected. The header is stored at the selected interval until the
    memory buffer is full.  Once the buffer is full HRD will
    automatically switch back to normal mode and will only store data
    when room is available in the buffer.
 
    HRD Normal (Cruise) Mode Format (Raw binary data Format)
    ---------------------------------------------------------
 
    *** H R D   D a t a   F r a m e   1 ***
 
    |-----------------------------------|----------------------------|
    |           HRD Sync (24 Bits)      |      HRD Status (8 Bits)   |
    |----------------------------------------------------------------|
    | (MSB)        HRD Clock (32 Bits)                    (LSB)      |
    |----------------------------------------------------------------|
    | (MSB)       Spacecraft Clock from DA      (32 Bits) (LSB)      |
    |--------------------|-------------------|-----------|-----------|
    | Sector   (8 bits)  | Sector   (8 Bits) |  Temp #1  |  Spare    |
    | Position (MSB)     | Position (LSB)    | (8 Bits)  |  (8 Bits) |
    |--------------------------------|-------------------------------|
    |          M1 (16 Bits)          |              M2 (16 Bits)     |
    |--------------------------------|-------------------------------|
    |          M3 (16 Bits)          |              M4 (16 Bits)     |
    |--------------------------------|-------------------------------|
    |          m1 (16 Bits)          |              m2 (16 Bits)     |
    |--------------------------------|-------------------------------|
    |          m3 (16 Bits)          |              m4 (16 Bits)     |
    |--------|-----------------------|---|---|---|---|---|---|---|---|
    | 3 Bit  |  Discrete #1 Clock    | M | M | M | M | m | m | m | m |
    | Sector | (21 Low Order Bits)   | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 |
    |--------|-----------------------|---|---|---|---|---|---|---|---|
    | 3 Bit  |  Discrete #2 Clock    | M | M | M | M | m | m | m | m |
    | Sector | (21 Low Order Bits)   | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 |
    |--------|-----------------------|---|---|---|---|---|---|---|---|
    | 3 Bit  |  Discrete #3 Clock    | M | M | M | M | m | m | m | m |
    | Sector | (21 Low Order Bits)   | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 |
    |--------|-----------------------|---|---|---|---|---|---|---|---|
    | 3 Bit  |  Discrete #4 Clock    | M | M | M | M | m | m | m | m |
    | Sector | (21 Low Order Bits)   | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 |
     ----------------------------------------------------------------
         *
         *
    Discrete Data 5 to 254
         *
         *
    |--------|-----------------------|---|---|---|---|---|---|---|---|
    | 3 Bit  |  Discrete #255 Clock  | M | M | M | M | m | m | m | m |
    | Sector | (21 Low Order Bits)   | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 |
    |--------|-----------------------|---|---|---|---|---|---|---|---|
    | 3 Bit  |  Discrete #256 Clock  | M | M | M | M | m | m | m | m |
    | Sector | (21 Low Order Bits)   | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 |
     ----------------------------------------------------------------
 
    *** H R D   D a t a   F r a m e   2 ***
 
    |-----------------------------------|----------------------------|
    |           HRD Sync (24 Bits)      |      HRD Status (8 Bits)   |
    |----------------------------------------------------------------|
    | (MSB)        HRD Clock (32 Bits)                    (LSB)      |
    |----------------------------------------------------------------|
    | (MSB)       Spacecraft Clock from DA      (32 Bits) (LSB)      |
    |--------------------|-------------------|-----------|-----------|
    | Sector   (8 bits)  | Sector   (8 Bits) |  Temp #1  |  Spare    |
    | Position (MSB)     | Position (LSB)    | (8 Bits)  |  (8 Bits) |
    |--------------------------------|-------------------------------|
    |          M1 (16 Bits)          |              M2 (16 Bits)     |
    |--------------------------------|-------------------------------|
    |          M3 (16 Bits)          |              M4 (16 Bits)     |
    |--------------------------------|-------------------------------|
    |          m1 (16 Bits)          |              m2 (16 Bits)     |
    |--------------------------------|------------------------------ |
    |          m3 (16 Bits)          |             m4 (16 Bits)      |
     ----------------------------------------------------------------
 
    HRD Fast (Encounter) Mode Format (Raw binary data Format)
    -----------------------------------------------------------
 
    |-----------------------------------|----------------------------|
    |           HRD Sync (24 Bits)      |      HRD Status (8 Bits)   |
    |--------------|-------------------------------------------------|
    | 5 Bit Sector |  (MSB)      HRD Clock (27Bits)            (LSB) |
    |--------------------------------|-------------------------------|
    |          M1 (16 Bits)          |              M2 (16 Bits)     |
    |--------------------------------|-------------------------------|
    |          M3 (16 Bits)          |              M4 (16 Bits)     |
    |--------------------------------|-------------------------------|
    |          m1 (16 Bits)          |              m2 (16 Bits)     |
    |--------------------------------|-------------------------------|
    |          m3 (16 Bits)          |              m4 (16 Bits)     |
     ----------------------------------------------------------------
 
 
    HRD Commands
    ============
 
    When the CDA main electronics supplies power to the HRD, the HRD
    turn on in NORMAL (CRUISE) MODE, with a sensor mass threshold
    relays in the ~SLOW MASS~T positions.
 
    HRD commands include:
 
    (a) ENCOUNTER MODE: Selects delta t at one value in the range
    delta t = 0.1, 0.2, ...,0.9, 1.0 s and runs the HRD in ENCOUNTER
    MODE.
    (b) SET RELAY: Selects the threshold relay switches for each
    sensor to LOW MASS RANGE or HIGH MASS RANGE (see Table I).
    (c) IN-FLIGHT CALIBRATE (IFC): Initiates a sequence of electronic
    pulses of varying amplitude within the HRD electronics which
    permits assessment of the stability of the HRD electronics.
 
    PVDF Sensor Calibrations
    ========================
 
    Particle calibrations of HRD-type PVDF sensors (28 and 6 microns
    thick) were carried out at the Heidelberg and Munich dust
    accelerator facilities, as summarized in Table 10 of Tuzzolino
    (1996). The calibration data show that the signal amplitude N may
    be fit by a power-law dependence on particle mass and velocity of
    the form m^av^b, with values for the mass index a and velocity
    index b, as given in the expressions included.
 
    From these data, and an assumed ring plane crossing particle
    impact velocity of 15 km/s the electronic thresholds set for the
    HRD flight unit will result in the particle mass thresholds given
    in Table I. The upper half of Table I lists the electronic and
    particle mass thresholds for the case where the sensor mass
    threshold switches are set for LOW MASS, and the lower half of
    Table I for the case where the switches are set for HIGH MASS (by
    ground command).
 
    Table I
    =======
 
    HRD PVDF sensors - electronic thresholds and corresponding
    particle mass thresholds and particle diamenter for 15 km/s impact
    speed (upper half: Low Mass, lower half: High Mass).
 
    PVDF Sensor #1: area= 50 cm^2, thickness = 28 microns
     Electronic             Mass Particle
    Threshold (electrons)   Threshold (g)      Diameter (microns)
    --------------         ---------------    --------------
    LM1 = 2.1 x 10^6        4.0 x 10^-12       1.5
    LM2 = 1.9 x 10^7        2.2 x 10^-11       2.6
    LM3 = 4.1 x 10^8        5.1 x 10^-9        15.7
    LM4 = 5.2 x 10^9        8.3 x 10^-8        40
    HM1 = 1.8 x 10^7        2.1 x 10^-11       2.5
    HM2 = 1.6 x 10^8        1.7 x 10^-9        10.9
    HM3 = 3.5 x 10^9        5.5 x 10^-8        35
    HM4 = 4.4 x 10^10       9.3 x 10^-7        89
 
    PVDF Sensor #2: area = 10 cm^2, thickness = 6 microns
     Electronic             Mass Particle
    Threshold (electrons)  Threshold (g)      Diameter (microns)
    --------------         ---------------    --------------
    m1 = 2.0 x 10^6         7.5 x 10^-13       0.8
    m2 = 1.9 x 10^7         4.0 x 10^-12       1.5
    m3 = 4.1 x 10^8         2.3 x 10^-9        12.1
    m4 = 5.2 x 10^9         8.5 x 10^-8        40.2
    m1 = 2.1 x 10^7         4.4 x 10^-12       1.5
    m2 = 2.0 x 10^8         9.0 x 10^-10       8.8
    m3 = 4.3 x 10^9         6.5 x 10^-8        36.7
    m4 = 5.4 x 10^10        2.5 x 10^-6        124
 
    assuming impacting particles with density 2.5 g/cm^3.
 
    References
    ==========
 
    Jaffe, L.D. and Herrell, L.M., Cassini/Huygens Science
    Instruments, Spacecraft, and Mission, J. Spacecraft Rockets 34(4),
    509, 1997.
 
    Perkins, M.A., Simpson, J.A., and Tuzzolino, A.J., A Cometary and
    Interplanetary Dust Experiment on the VEGA Spacecraft Missions to
    Halley's Comet, Nucl. Instrum. Method A239, 310, 1985.
 
    Ratcliff, P., Gogu, F., Gruen, E., and Srama, R., Adv. Space Res.
    17(12), 111-115, 1996.
 
    Tuzzolino, A. J., Applications of PVDF Dust Sensor Systems in
    Space, Adv. Space Res. 17(12), 123-132, 1996.
 
    Simpson, J.A. and Tuzzolino, A.J., Polarized Polymer Films as
    Electronic Pulse Detectors of Cosmic Dust Particles, Nucl.
    Instrum. Methods A236, 187-202, 1985.
 
    Simpson, J.A. and Tuzzolino, A.J., Cosmic Dust Investigations, II:
    PVDF Detector Signal Dependence on Mass and Velocity for
    Penetrating Particles, Nucl. Instrum. Methods A279, 625, 1989.

        