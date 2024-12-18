
 
 
  Instrument Overview
  ===================
    The PHX entry capsule contained two Inertial Measurement Units (IMUs)
    mounted on the underside of the lander on opposite sides of the
    spacecraft. Only one IMU was used during descent, entry and landing
    (EDL). The other IMU was a backup device that was not turned on. The
    Phoenix IMU is quasi-standard commercial product, sometimes called a
    Miniature IMU, or MIMU [GARAVELLIETAL1995]. This particular device
    was manufactured by Honeywell (Clearwater, FL) with model number
    YG9666BC. The IMU used three Allied Signal QFLEX accelerometers for
    linear acceleration measurement and three Honeywell GG1320 RLG
    ring-laser gyros for angular rotation measurement. However, the IMU
    was configured internally so that the linear accelerations were
    integrated and output as linear velocity changes while the gyro
    measurements were output as angle changes in a given sample time. No
    input from scientists was possible concerning the device selection
    and location within the lander, which was done by spacecraft
    engineers for the cancelled NASA Mars 2001 Lander prior to the
    initiation of the Phoenix project. The Phoenix lander was based on
    the Mars 2001 Lander design. Consequently, the IMU used during EDL of
    the Phoenix spacecraft was neither located at the entry vehicle
    center of mass nor the spin axis, which otherwise would have been
    desirable to optimize noise minimization for scientific purposes.
 
    The instrument attributes for the PHX IMU are discussed in
    [TAYLORETAL2008]. At a rate of 200 Hz, the IMU output the accumulated
    linear velocity change (the time integral of acceleration) in three
    Cartesian axes and accumulated angle change (the time integral of
    angular rate) about three Cartesian axes. Data was saved onboard PHX
    at the device output rate of 200 Hz and was not down-sampled.
 
    The IMU had a mass of 3.52 kg and approximately 4051 cc volume.  Each
    accelerometer within the IMU had a full-scale range of 36.8g (where g
    represents Earth's standard surface gravitational acceleration of
    9.80665 meters per second per second). The accelerometer and gyro
    signals were electronically integrated inside the IMU to produce an
    output of accumulated delta-v (linear velocity change) and delta-q
    (angular velocity change) at 200 Hz.  The accelerometers had two
    stages of digitization that resulted in pulses and then counts. The
    final raw digital output from the IMU accelerometers was in counts,
    in velocity units, where 1 output count = 0.0753 mm/sec.  But the
    final output moved up and down in pulses, which are leaps of many
    counts, with each pulse equivalent to 2.7 mm/sec. Thus, the amplitude
    of one pulse was equivalent to 2.7/0.0753 = 35.86 counts, on
    average. Added to this was noise in the system, which was on the
    order of 1 count, so that jumps in the raw output were typically 36
    or 37 counts. This determined the digital resolution of the raw 200
    Hz data to be a delta-v of 2.7 mm/sec and typical noise level of
    0.0753 mm/sec.
 
    Individual gyros measure the angular rotation about one axis. Each
    raw IMU gyro output is a 16 bit signed integer (i.e., from -32767 to
    +32767) with the least significant bit (LSB) equivalent to 1
    micro-radian. Because the data was generated at 200 Hz or every 5
    millisecs, a full-scale value of 32768 would correspond to 375
    deg/sec. (32,768 * 1 microradian /0.005 sec = 0.032768/0.005
    radian/sec = 6.5536 rad/sec = 375 deg/sec). The smallest motion in a
    200 Hz interval is one count, which corresponds to 0.01144 deg/sec (1
    * 1 microradian /0.005 sec = 200 micro-rad/sec = 0.01144 deg/sec).
    Smaller angular motions can be measured over longer time periods by
    integration of the raw data. Noise on the raw gyro output is
    estimated as 45 micro-radians (3 sigma).
 
  Entry State and Timing
   =====================
 
    The frictional drag of the atmosphere upon the entry vehicle resulted
    in a reduction in the speed of the entry vehicle. This deceleration
    was measured by the accelerometers within the IMU, while the
    orientation of the entry vehicle was provided by the gyroscope
    measurements.  Some ancillary parameters are necessary to use the IMU
    data scientifically.  These include the wet mass of the Phoenix probe
    at atmospheric entry, which was estimated as 572.743 kg. (Further
    mass properties during descent to landing will be documented in the
    DOCUMENT directory of this archive). Another parameter is the entry
    probe cross-sectional area of the entry probe, which was 5.515 m**2,
    based on an aeroshell diameter of 2.65 m. To integrate the IMU data
    to derive atmospheric structure, requires an entry state boundary
    condition.  Entry state information was derived by the Lockheed
    spacecraft team from navigation communications using two-way Doppler,
    ranging (the light time of signal transmit and receive to determine
    distance), and delta differential one-way ranging. The latter
    technique uses a fixed natural radio source such as a quasar and two
    stations on the Earth to allow difference ranging, which gives an
    accurate angular separation of the spacecraft from the fixed
    celestial source. From the angular separation the position of the
    spacecraft can be determined.  All this information was then
    propagated to the time and point of entry defined as 3522.2 km radius
    from the center of Mars. The best estimate of the Phoenix probe entry
    state was as follows: An entry position of 69.3660 deg N (1 sigma
    0.0040 deg), 197.7160 deg E (1 sigma 0.00031 deg) at a universal time
    on 2008-05-25 of 23:30:57.7330 (1 sigma 0.002 sec) with respect to a
    planetocentric Cartesian frame. The equivalent spacecraft clock
    (SCLK) time was 896225523.703.  Also the best estimate of the entry
    velocity was a speed of 5600.34 m/s (1 sigma 0.02 m/s) with a flight
    path angle below horizontal of -13.010 deg (1 sigma 0.00015 deg) and
    flight path azimuth, clockwise from north, of 77.6720 deg (1 sigma
    0.00055 deg) in the same planetocentric frame. The best estimate of
    the time of the first IMU data acquisition (with an uncertainty of
    0.02 seconds) was a universal time on 2008-05-25 of 23:30:47.913,
    equivalent to a spacecraft clock (SCLK) time of
    896225513.881. However, the first EDR data point for delta-velocity
    and delta-angle was derived from a difference between the first two
    IMU readings, which gave a time stamp 0.005 seconds later on
    2008-05-25 at 23:30:47.918. Thus, the EDR data points began 9.82
    seconds before the nominal atmospheric entry state position as
    defined above.
 
  Platform Mounting Description
  =============================
 
    There were two IMUs mounted on the underside of the Phoenix Lander
    deck, on opposite sides, denoted by Side A (or 1) and Side B (or 2).
    The location of the IMUs under the lander deck is described in the
    EDR SIS. However, only the IMU on side A was used in collecting
    data. This IMU is referred to as IMU-1 or IMU-A in PHX project
    documentation.
 
  Principal Investigator
  ======================
 
     The IMU for the PHX mission was not selected for characteristics
     needed for optimal atmospheric structure reconstruction but was
     inherited from NASA's cancelled Mars 2001 lander mission.  The IMU
     system was part of the engineering instrumentation and was selected,
     configured, installed, and operated by members of the Phoenix lander
     engineering team from Lockheed Martin. The IMU provided entry
     vehicle deceleration and orientation information that was used for
     triggering EDL events on the entry vehicle such as parachute
     deployment. However, the Atmospheric Science Theme Group (ASTG) of
     the Phoenix Science Team decided that the IMU data should be used
     for atmospheric structure reconstruction. David C. Catling from the
     ASTG became the cognizant scientist that led the effort to retreive
     and archive the PHX IMU data to enable atmospheric recontruction.
 
  Scientific Objectives
  =====================
 
    The IMU is an engineering device from which science can be
    derived. The measured delta-velocity values provided by the IMU, as a
    function of time (which needs to be used to determine the height
    above the surface) can be employed to deduce the vertical structure
    of density and pressure, and ultimately temperature along the
    atmospheric trajectory traversed by the Phoenix probe as it descended
    through the atmosphere.
 
  Operational Considerations
  ==========================
 
    EDL is a mission critical phase (if EDL fails, the mission is lost)
    and since the IMU was an active sensor of the EDL process, its
    operational characteristics as described above were wholly driven by
    EDL engineering considerations. These choices constrain the
    scientific return of the instrument.
 
  Calibration
  ===========
 
    The IMUs were delivered with a factory calibration based upon
    individual unit testing after assembly.  Outputs of velocity change
    from accelerometers and angle change from gyros are internally
    compensated for biases, scale factors and alignments based on
    coefficients determined by factory calibration tests. From cruise
    data, the Lockheed Martin spacecraft team estimated that there was a
    zero offset on the IMU output expressed in the [X, Y, Z] Cartesian
    axes of the cruise body frame of reference of the spacecraft of
    [-3.47845e-4, 2.42877e-4, 4.38682e-4] in units of m/s/s.
 
  Operational Modes
  =================
 
    From the time of IMU turn on through the EDL process of atmospheric
    entry to landing, IMU data were provided at 200 Hz and
    saved at this rate by the on-board software.  There were no gain
    changes or offset changes throughout this time period.

        