
 
  Abstract
  ========
    The Mars Global Surveyor magnetic field instrument consists of
    dual, triaxial fluxgate magnetometers, capable of measuring fields
    between +/- 4 nT and +/- 65536 nT. Automated range switching allows
    the instrument to maintain maximum digital resolution over a wide
    range of field strengths.
 
    The text of this instrument description has been abstracted from
    the instrument paper [ACUNAETAL1992]:
 
      Acuna, M. A., J. E. P. Connerney, P. Wasilewski, R. P. Lin,
      K. A. Anderson, C. W. Carlson, J. McFadden, D. W. Curtis, H.
      Reme, A. Cros, J. L. Medale, J. A. Sauvaud, C. d'Uston, S. J.
      Bauer, P. Cloutier, M. Mayhew, and N. F. Ness, Mars Observer
      Magnetic Fields Investigation, J. Geophys. Res., 97, 7799-7814,
      1992.
 
    The description and ASCII drawings of the instrument mounting and
    frames are derived from the SPICE instrument kernel version 1.2
    dated Sept. 16, 1998. Please review the published material for a
    complete description of the instrument.
 
 
  Scientific Objectives
  =====================
    The primary objective of the Mars Global Surveyor (MGS) magnetic
    field experiment is to establish the nature of the magnetic field
    of Mars. This includes determining whether or not Mars has a global
    field of internal origin indicating either present or past dynamo
    field generation. The existence of an internally generated field
    would place significant constraints on the composition, thermal
    state, and dynamics of the interior of the planet.
 
    Even if dynamo activity ceased as the planet cooled, there is
    evidence that dynamo activity existed in the past. Remanent
    magnetization has been observed in meteorites that are widely
    believed to have originated on Mars [BOGARD&JOHNSON1983]. An
    important objective of the magnetic field investigation is to
    identify and characterize crustal remanent magnetization. Magnetic
    anomaly maps, together with geological data will provide a history
    of Martian magnetism and crustal evolution.
 
    Previous missions to Mars have determined that if there is a global
    magnetic field at Mars it must be small [LUHMANN1991]. Remanent
    magnetic fields are also likely to be small [ACUNAETAL1992]. In
    order to accurately measure magnetic fields of Martian origin, the
    nature of the solar wind and interplanetary magnetic field
    interactions with Mars must be well determined.
 
 
  Calibration
  ===========
    The flight software incorporated into the on-board data processor
    includes diagnostic and self-calibration routines [ACUNAETAL1992].
    On-board calibration sequences provide the currents required for
    determination of the gain of each axis sensor for the various
    dynamic ranges, as well as for determination of electronic offsets
    by reversal of the polarity of the signals processed by the
    magnetometer electronics. In addition, spacecraft maneuvers will be
    performed that will allow the spacecraft field and sensor offsets
    to be determined independently.
 
 
  Operational Considerations
  ==========================
    The magnetometer power consumption is 375 mW in zero field and
    increases with the magnitude of the measured field up to 420 mW.
    The typical rms noise level in the sensors is 0.006 nT over a 10 Hz
    bandwidth. The zero-level stability is less than 0.15 nT over the
    range of -40 to +60 degrees Centigrade and for durations up to a
    year. The upper range of 65,536 nT allows the instrument to be
    operated in the Earth's magnetic field without special shields or
    field cancellation magnets.
 
 
  Detectors
  =========
    The MGS magnetometer experiment consists of two, fully redundant,
    fluxgate magnetometers. There are two sensor triads, two sets
    of electronics, and two power converter packages. Either sensor
    triad can be connected to either electronics package. Only one of
    the two systems is powered at any time. The other system is powered
    off and maintained in a standby state for redundancy.
 
    The detectors are constructed using the ring core geometry, which
    has been shown to have excellent performance characteristics in
    terms of long-term zero-level stability and drive power
    requirements. The magnetic material used to manufacture the sensors
    in an advanced molybdenum-permalloy alloy developed for low-noise,
    high-stability applications.
 
    The MGS spacecraft does not have a magnetometer boom to mount the
    sensors on as the original Mars Observer spacecraft did. Instead,
    the two sensor packages are mounted on the solar panel arrays.
 
    The following diagram shows dimensions required for determination
    of locations of the MAG sensors relative to the s/c center:
 
   -Y MAG       yoke   gimbal    s/c    gimbal  yoke        +Y MAG
     |            |       |       |       |       |            |
     |  3.817m    | 0.729m|0.669m | 0.669m| 0.729m|    3.817m  |
     |    or      |   or  |   or  |   or  |   or  |      or    |
     | 150.285in  | 28.7in|26.33in|26.33in| 28.7in|   150.285in|
     |<---------->|<----->|<----->|<----->|<----->|<---------->|
     |            |       |    ___|____   |       |            |
     |            |       V   /   |   /|  V       |            |
     |  __________|_ _____   /____|__/ |      ____|__ _________|__
     V /          V//     |  |    |  | |     /    V //         V /
      /  -Y Solar //      |  |    |  | |   /       // +Y Solar  /
     @     Array /@       @--|    |  | ---@       @/   Array   @ -----
    /           //       /   |    |  | |  |      //           / ^
   /___________//______/     |    |  | |  |_____//___________/  |0.934m
                             |____V__|/                         |36.77in
                                /   \                           V
                               /__@__\                     -----------
 
    The orientations of the instrument frames of the +Y and -Y MAG
    sensors relative to the corresponding solar array frames are shown
    below:
 
       -Y Solar Array frame                  +Y Solar Array frame
 
                      +Z   +X                              +Z
                       |   /                                |
                       |  /                                 |
                       | /                                  |
             +Y _______|/                                   |_______ +Y
                                                           /
                                                          /
                                                      +X /
 
       -Y MAG Sensor frame                   +Y MAG Sensor frame
                        _______ +Y                           _______ +Y
                      /|                                   /|
                     / |                                  / |
                    /  |                                 /  |
                   /   |                                /   |
                 +Z   +X                              +Z   +X
 
    This schema shows that +Y MAG is +90 degrees rotated about Y axis
    relative to the +Y solar array and -Y MAG sensor is -90 degrees
    rotated about Y axis and after that +180 degrees rotated about the
    new position of Z axis relative to the -Y solar array.
 
 
    Frames diagram
    --------------
      The following diagrams shows the frames defines for the MGS
      spacecraft, solar arrays and MAG sensors:
                                    +Z
                                    |
                                    |
                                    *--- +Y
                                +X /
 
 
                               S/C body FR
                   +Z        (MGS_SPACECRAFT)           +Z
                     | +X           |                   |
                     |/             |                   |
               +Y ---*              |                   *--- +Y
                                    |               +X /
                      -Y Gimbal FR  |   +Y Gimbal FR
                      (MGS_RIGHT_   |   (MGS_LEFT_              +Z
            +Z        SOLAR_ARRAY)  |   SOLAR_ARRAY)           |
             | +X           |       |       |                  |
             |/             |       |       |                  *--- +Y
       +Y ---*              |       |       |              +X /
                -Y Yoke FR  |       |       |   +Y Yoke FR
              (MGS_+Y_SOLAR |       |       | (MGS_+Y_SOLAR
                 _ARRAY)    |       |       |     _ARRAY)
     *--- +Y        |       |       |       |       |            *--- +Y
    /|              |       |       |       |       |           /|
 +Z  |              |       |       |       |       |        +Z  |
    +X              |       |       |       |       |             +X
                    |       |       V       |       |
-Y MAG sensor FR    |       |    ________   |       |  +Y MAG sensor FR
(MGS_MAG_-Y_SENSOR) |       V   /       /|  V       |(MGS_MAG_+Y_SENSOR)
       |  __________|_ _____   /_______/ |      ____|__ _________|__
       V /          V//     |  |       | |     /    V //         V /
        /  -Y Solar //      |  |       | |   /       // +Y Solar  /
       @     Array /@       @--|       | ---@       @/   Array   @
      /           //      /    |       | |  |      //           /
     /___________//_____/      |       | |  |_____//___________/
                               |_______|/
 
      'MGS_SPACECRAFT' frame is the frame associated with the MGS
      spacecraft main bus. This frame is defined in an MGS SCLK file
      created by mgs_scet2sclk program at LMA. Orientation of this
      frame is provided in the CK files produced by the ATTREC program
      at LMA.
 
      'MGS_LEFT_SOLAR_ARRAY' and 'MGS_RIGHT_SOLAR_ARRAY' frames are
      associated with the +Y and -Y solar array gimbals respectively.
      These frames are defined in an MGS SCLK file created by the
      mgs_scet2sclk program at LMA. Orientation of these frames is
      provided in the CK files produced by the MGSSCK program at LMA.
      Note that there are no separate frames defined for inboard
      ('elevation') and outboard ('azimuth') gimbals for each solar
      array. Instead each pair of gimbals is considered as a single
      gimbal having two degrees of rotation. These frame can be
      considered as 'nominal' solar array position frames since they
      specify gimbal orientation and do not take into account any
      additional rotations/transformation that can (did) occur due to
      incomplete deployment of an array.
 
      'MGS_+Y_SOLAR_ARRAY' and 'MGS_-Y_SOLAR_ARRAY' frames are
      associated with the +Y and -Y solar array yokes respectively.
      These frames are 'fixed offset' frames whose orientation is
      specified by a set of Euler angles relative to the corresponding
      frames associated with gimbals. Defining these frames was
      required because of -Y Solar array deployment failure, which
      introduced an additional rotation in the yoke for that panel.
      For the +Y panel this frame is the same as the gimbal frame.
 
      'MGS_MAG_+Y_SENSOR' and 'MGS_MAG_-Y_SENSOR' frames are associated
      with +Y and -Y MAG sensors. These frames are fixed offset frames
      whose orientation is specified by a set of Euler angles relative
      to the corresponding yoke frames.
 
 
  Electronics
  ===========
    Signals from the sensors are first processed by the analog
    electronics and then by the digital processing unit (DPU). Analog
    data are anti-alias filtered and then sent to a twelve bit
    (12-bit) successive approximation analog to digital (A/D) converter
    that is controlled by a microprocessor. Variable time resolution
    data are derived from the basic measurements and the spacecraft
    telemetry mode. The microprocessor activates the automatic gain
    control logic in the electronics. If the magnitude of the measured
    vector component falls within upper or lower guard bands (256 data
    numbers), then the range (scale factor) is incremented or
    decremented to maintain maximum digital resolution. Range
    adjustments change the dynamic range and digital quantization by a
    factor of four.
 
         Range        Field Strength     Quantization
         --------------------------------------------
           0            +/-     4 nT          .002 nT
           1            +/-    16 nT          .008 nT
           2            +/-    64 nT          .032 nT
           3            +/-   256 nT          .128 nT
           4            +/-  1024 nT          .512 nT
           5            +/-  4096 nT         2.048 nT
           6            +/- 16384 nT         8.192 nT
           7            +/- 65536 nT        32.768 nT
 
    The DPU unit's primary function is to acquire the magnetic field
    data and package it with instrument state and housekeeping data in
    a form that can be picked up and transmitted to the ground by the
    Payload Data System (PDS). The system consists of a master
    executive program that is resident in ROM. The DPU uses the 80C86
    microprocessor and associated memory and peripheral devices. Default
    parameter tables used for data processing are stored in ROM but can
    be modified by ground command. Parameters such as sensor zero
    levels, alignment matrices, scale factors, etc. are expected to be
    updated periodically under normal operating conditions. RAM memory
    is used to double buffer data while packets are being created and
    accessed by the PDS. Double buffering allows a completed packet to
    be read out while a new packet is being created without access
    conflicts between the instrument and the PDS. Data collection and
    processing routines are interrupt driven by a real time interrupt
    (RTI) signal provided eight times per second by the onboard PDS.
    The clock is multiplied four times (32 Hz) and is the fundamental
    timing signal for all processes in the instrument.
 
    Data compression techniques are used to maximize data return within
    the bandwidth allocated to the experiment. Raw magnetometer data are
    averaged and then 6-bit differenced between adjacent averages. The
    differences are combined with periodic 12-bit 'full-words' and
    formatted into data packets. If the differences exceed the dynamic
    range of six bits, the system folds the values (modulo 64) over
    rather than saturating. This allows the reconstruction of rapidly
    varying fields that would otherwise be lost. If the number of
    folded differences exceeds a predetermined value, the DPU left
    shifts the differencing scheme by the least significant bit doubling
    the dynamic range. There is a maximum of two left shifts permitted.
    The data return sample rate is linked to the spacecraft data rate.
    The instrument has three data rate allocations. Both the rate of
    primary (compressed) samples and secondary (full-word) samples
    varies with the data rate.
 
       Data Rate          Primary Values         Secondary Values
       (bits/sec)         (samples/sec)            (samples/sec)
       -----------------------------------------------------------
         324                   8                       1/6
         648                  16                       1/3
        1296                  32                       2/3in
 
    ===================================================================

        