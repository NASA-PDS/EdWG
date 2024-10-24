
 
  Instrument Overview
  ===================
    An accelerometer is an instrument that measures the acceleration
    of the case of the sensor due to external forces. All
    accelerometers have a 'proof mass' and it is the tendency of the
    proof mass to move relative to the case that is a measure of the
    acceleration of the case. Early accelerometers produced output
    that was directly related to acceleration; but modern sensors
    integrate the internally measured signal, to reduce noise, and the
    output is proportional to the change in velocity over the
    integration time. In high precision accelerometers, like those on
    MGS, the proof mass is an electronically floating magnetic body.
    The electromagnetic field is varied to keep the proof mass
    stationary relative to the case. The voltage required to
    accomplish this is proportional to the acceleration. The accel-
    erometers on MGS are sensitive to acceleration of the center of
    mass (c.m.) of the s/c, pseudo-accelerations (i.e., centrifugal)
    due to rigid motion of the s/c about the c.m., and differences in
    gravitational force at the proof mass and the c.m. of the s/c
    (gravity gradient).
 
    The MGS Inertial Measurement Unit (IMU) contains four accel-
    erometers. The principal accelerometer used in the aerobraking
    analysis is the z-axis accelerometer. This accelerometer is
    located at approximately (-0.44, -0.38, 0.72) m relative to the
    center of mass. The accelerometers are Sundstrand QA1200-AA08
    model Q-Flex and continuously integrate acceleration to obtain
    velocity data. The instrument is sampled every 0.1 seconds. The
    data are recorded in instrument counts or quantized velocity
    increments equivalent to 0.332 mm/s per count. The QA1200 bias has
    a specified temperature sensitivity of 10 mg/K or approximately
    0.3 counts/K. The temperature of the IMU assembly is actively
    controlled. IMU telemetered temperatures are quantized at 0.12 K
    and typical changes during an entire aerobraking pass are between
    two quantized values. Consequently, only a single, constant bias
    is determined for each pass through the atmosphere.
 
 
  Scientific Objectives
  =====================
    Accelerometer data were used to characterize the nature of the
    atmosphere, to determine the effect of the atmosphere on each
    orbit, and to predict the effect of the atmosphere on future
    orbits.
 
 
  Calibration
  ===========
    The instrument was calibrated on each orbit to determine drift in
    instrument bias.  Bias is determined by monitoring the
    accelerometer instrument during periods of inactivity before and
    after entering the atmosphere. The bias acceleration is then
    estimated over the entire pass by trending the data from the pre-
    and post-atmospheric entry periods.  The pre- and post-atmospheric
    periods were defined by instrument turn-on and turn-off times and
    a lower limit on the altitude of data used for calibration,
    typically 200 km.
 
 
  Operational Considerations
  ==========================
    The instrument readings are affected by changes in temperature.
    The instrument is mounted in the inertial measurement unit (IMU).
    The temperature of the IMU box is monitored by two temperature
    sensors, one inside the box and one on the box housing, and
    controlled by a single heater. The quantum of temperature
    measurement inside the IMU is 0.117 deg C and the highest
    temperature variation was 2 quanta over a period of 4 seconds.
    To calculate the effect of this temperature variation on
    accelerometer measurements, the acclerometer manufacturer's
    estimate of 0.3 counts of acceleration change per deg C of
    temperature change was used. Therefore, a 2 quanta temperature
    variation over 4 seconds resulted in an acceleration change of
    5.8 * 10^-6 m/s^2. When compared to the acceleration values, the
    value of acceleration due to temperature change was negligible for
    altitudes within 30 km of periapsis. The temperature did not
    exhibit any increase or decrease that would indicate atmospheric
    heating was affecting the accelerometers inside the IMU. IMU
    temperature data, as telemetered during the first 201 orbits,
    yielded changes of less than 0.25 degrees C over an aerobraking
    pass.
 
  Operational Modes
  =================
    The data from the accelerometer are passed to the telemetry deck
    during an aerobraking pass from the time the s/c reaches
    aerobraking orientation until the s/c returns to nominal orbit
    attitude.
 
  Measured Parameters
  ===================
    An accelerometer is an instrument that measures the change in
    velocity of the spacecraft over a time interval by measuring the
    fluctuations of voltage to a magnetically floating assembly. The
    assembly is essentially a simple magnetic mass floating in a
    magnetically charged ring.  When the spacecraft accelerates, the
    position of the mass inside the ring is maintained by varying the
    voltage.  By recording the change in voltage to the ring and
    knowing the physical properties of the mass, the acceleration of
    the spacecraft can be calculated.

        