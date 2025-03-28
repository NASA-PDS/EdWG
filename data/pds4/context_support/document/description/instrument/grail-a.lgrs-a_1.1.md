
 
    Instrument Overview
    ===================
 
      Radio science investigations utilize instrumentation with
      elements both on a spacecraft and at ground stations -- in this
      case, at the NASA Deep Space Network (DSN). The spacecraft part
      of the radio science instrument is described immediately below;
      that is followed by a description of the DSN (ground) part of the
      instrument.
 
 
    Instrument Specifications - Spacecraft
    ======================================
 
      Instrument Id                  : LGRS-A
      Instrument Host Id             : GRAIL-A
      PI PDS User Id                 : UNK
      Instrument Name                : LUNAR GRAVITY RANGING SYSTEM A
      Instrument Type                : RADIO SCIENCE
      Build Date                     : UNK
      Instrument Mass                : UNK
      Instrument Length              : UNK
      Instrument Width               : UNK
      Instrument Height              : UNK
      Instrument Manufacturer Name   : UNK
 
 
    Instrument Overview - Spacecraft
    ================================
      The Lunar Gravity Ranging System (LGRS) instruments on board the
      twin GRAIL spacecraft generate radio signals at Ka-band, X-band,
      and S-band. The time and frequency of each signal is referenced
      to its respective Ultra-Stable Oscillator (USO).  The Ka-band
      and S-band signals are captured by the other spacecraft, and
      precise measurements of signal properties are recorded for later
      transmission to Earth.  The X-band link is received by stations
      of the NASA Deep Space Network (DSN). Operations are continuous
      and simultaneous on both spacecraft except that the X-Band
      downlink to Earth is only used when a DSN station is available.
 
      The sinusoidal Ka-band link is used to determine distance
      (range) between the two spacecraft from the phase of the
      received signal. The modulated S-band signal is for exchange of
      Timing and Time Synchronization (TTS). The X-band link is a
      one-way transmission to the DSN via the Radio Science Beacon
      (RSB).
 
      Except for mounting differences, LGRS-A and LGRS-B (on GRAIL-A
      and GRAIL-B, respectively) are identical.  Each is responsible
      for working with its twin to send and receive the signals needed
      to accurately and precisely measure the changes in range between
      the two orbiters. Each LGRS consists of an Ultra-Stable
      Oscillator (USO), Microwave Assembly (MWA), a Time-Transfer
      Assembly (TTA), and the Gravity Recovery Processor Assembly
      (GPA).
 
      The USO provides a steady reference signal that is used by all
      of the instrument subsystems. Within the LGRS, the USO provides
      the reference frequency for the MWA and the TTA. The MWA
      converts the USO reference signal to the Ka-band frequency,
      which is transmitted to the other orbiter.
 
      The function of the TTA is to provide a two-way time-transfer
      link between the spacecraft both to synchronize and to measure
      the clock offset between the two LGRS clocks. The TTA generates
      an S-band signal from the USO reference frequency and sends a
      GPS-like ranging code to the other spacecraft. The GPA combines
      all the inputs received from the MWA and TTA to produce the
      radiometric data that are downlinked to the ground.
 
      Finally, each Radio Science Beacon (RSB) transmits an X-Band
      signal to the ground based on its USO; the drift of the USO is
      derived from the one-way Doppler data.
 
 
      Science Objectives
      ==================
      The inter-spacecraft radio links and the X-band radio link to
      Earth are used to generate a high resolution gravitational field
      of the Moon.
 
 
      Operational Considerations - Spacecraft
      =======================================
      GRAIL Primary Mission (PM) & Extended Mission (XM) operational
      considerations
 
      The GRAIL PM started on March 01, 2012 and ended on May 29,
      2012.  The GRAIL XM started on August 29, 2012, and ended on
      December 12, 2012, followed by decommissioning from December 12,
      2012, to December 18, 2012. Spacecraft events for these phases
      (for example, propulsive maneuvers, Ka boresight calibration
      attitude maneuvers, telecommunication configuration changes and
      the science Lunar Gravity Ranging System (LGRS) events) are
      described below including their impact on science processing.
 
      1)Propulsive Maneuvers
 
      During PM, there were propulsive maneuvers for GRAIL-B but not
      for GRAIL-A.
 
      During the XM, weekly Eccentricity Correction Maneuvers (ECM)
      were needed on both GRAIL spacecraft to correct rapid orbit
      eccentricity changes due to large gravity variations at low
      altitudes. The ECMs were between 5 and 15 m/sec and required
      near radial thrusting which meant that the science measurements
      were interrupted for about 15 minutes while the spacecraft
      executed the ECMs. In the day following the ECMs a cleanup Orbit
      Trim Maneuver (OTM) maneuver was executed if needed. The OTMs in
      general were at the cm/sec level and science measurements were
      not interrupted during an OTM.
 
      The mass change history for both spacecraft can be found in the
      MAS1A/B Level-1 products, and the thruster on-times are
      available in the THR1A/B level-1 products. LGRS measurements are
      taken during the propulsive maneuvers but it is recommended to
      break science data arcs at the propulsive maneuver event times,
      since the velocity changes imparted on the spacecraft are not
      known with sufficient accuracy for science processing.
 
      XM GRAIL-A Propulsive Maneuvers
 
start time               end time                 duration  dV       comment
(TDB)                    (TDB)                    (sec)     (mm/sec)
2012-09-10 15:15:55.328  2012-09-10 15:18:14.469  139.141   10060.0  ECM-A4
2012-09-11 16:28:49.256  2012-09-11 16:30:12.158   82.902      24.4  OTM-A4
2012-09-17 16:52:32.843  2012-09-17 16:54:50.128  137.285    9900.0  ECM-A5
2012-09-24 11:17:48.378  2012-09-24 11:20:04.296  135.918    9780.0  ECM-A6
2012-09-25 14:55:51.299  2012-09-25 14:57:46.318  115.019      34.2  OTM-A6
2012-10-01 14:27:05.888  2012-10-01 14:28:59.583  113.695    8030.0  ECM-A7
2012-10-08 15:42:01.403  2012-10-08 15:43:28.056   86.652    5900.0  ECM-A8
2012-10-09 15:07:12.336  2012-10-09 15:08:41.735   89.398      27.0  OTM-A8
2012-10-15 15:36:38.923  2012-10-15 15:38:50.911  131.988    9480.0  ECM-A9
2012-10-16 15:37:23.854  2012-10-16 15:38:34.421   70.566      21.5  OTM-A9
2012-10-22 09:55:25.458  2012-10-22 09:57:22.095  116.637    8530.0  ECM-A10
2012-10-29 12:58:38.969  2012-10-29 13:00:44.184  125.215    9030.0  ECM-A11
2012-10-30 15:54:51.892  2012-10-30 15:56:01.013   69.121      20.8  OTM-A11
2012-11-05 16:08:02.479  2012-11-05 16:10:46.440  163.961   12100.0  ECM-A12
2012-11-06 17:26:51.407  2012-11-06 17:28:35.239  103.832       0.0  OTM-A12
2012-11-12 16:15:42.998  2012-11-12 16:18:14.588  151.590   10950.0  ECM-A13
2012-11-13 16:09:16.930  2012-11-13 16:14:20.297  303.367      89.9  OTM-A13
2012-11-19 19:40:31.508  2012-11-19 19:41:57.781   86.273    5820.0  ECM-A14
2012-11-20 21:15:56.434  2012-11-20 21:17:12.809   76.375      21.8  OTM-A14
2012-12-06 15:35:45.352  2012-12-06 15:37:25.122   99.769    6800.0  ECM-A15
2012-12-07 16:12:22.282  2012-12-07 16:14:04.465  102.184      30.0  OTM-A15
2012-12-10 17:43:53.071  2012-12-10 17:46:30.427  157.355   11370.0  ECM-A16
2012-12-11 15:57:58.008  2012-12-11 16:00:42.629  164.621      50.2  OTM-A16
2012-12-14 15:08:23.804  2012-12-14 15:09:35.120  71.316     4580.0  ECM-A17
2012-12-17 21:35:56.580  2012-12-17 21:40:13.411  256.832   20590.0  BTD-A
 
      2) Angular momentum desaturation maneuvers
 
      The GRAIL spacecraft attitude is maintained with angular
      momentum wheels. The angular momentum wheels apply torques on
      the spacecraft by spinning up or down to maintain attitude. The
      angular momentum wheels are only allowed to operate within a
      specified wheel speed range. If the wheel speeds exceed the
      specified range then attitude control thrusters (desaturation
      maneuver) are used to apply a torque on the spacecraft to slow
      or speed up the wheels, such that the resulting wheel speed is
      within the specified range. In general the wheel speeds are
      predictable, the desaturation maneuvers are planned in
      advance, and the burns occur over the lunar poles. Since the
      attitude control thrusters are not perfectly balanced, a
      velocity is imparted on the spacecraft for every maneuver. The
      velocity changes in general are small (< 5 mm/sec). LGRS
      measurements are taken during the desaturation maneuvers but it
      is recommended to break science data arcs at the desaturation
      maneuver event times, since the velocity changes imparted on the
      spacecraft are not known with sufficient accuracy for science
      processing. A table for all desaturation events is shown below
      for each spacecraft. The time reported in the table is the
      average for all thruster activations associated with one
      desaturation event. For detailed thruster on time histories see
      level-1 product THR1A/B. The spacecraft mass change is very
      small at the level of a few grams per event. For the December
      2012 and June 2013 deliveries, the spacecraft mass change is not
      accounted for in the MAS1A/B products, but it will be in future
      higher version of the level-1 products.
 
      PM GRAIL-A Angular momentum desaturation maneuvers
 
      Time (TDB)             dV (mm/sec)
      01-MAR-2012  16:16:08  3.07787
      02-MAR-2012  15:16:38  1.12157
      06-MAR-2012  22:10:18  7.48061
      07-MAR-2012  21:45:38  1.96178
      10-MAR-2012  14:05:48  5.43986
      13-MAR-2012  15:54:24  6.27925
      16-MAR-2012  23:23:18  6.86991
      20-MAR-2012  10:39:03  7.05885
      23-MAR-2012  21:55:20  6.94661
      27-MAR-2012  19:51:24  5.96857
      28-MAR-2012  02:13:10  0.48094
      30-MAR-2012  07:12:28  3.96800
      01-APR-2012  12:11:33  3.99191
      03-APR-2012  13:23:08  3.72816
      06-APR-2012  13:18:15  4.90296
      12-APR-2012  07:27:47  7.49176
      22-APR-2012  02:07:36  9.31918
      24-APR-2012  07:06:16  2.09266
      26-APR-2012  13:58:55  2.49039
      28-APR-2012  22:44:55  2.75867
      30-APR-2012  23:56:39  2.79112
      03-MAY-2012  01:08:58  2.99911
      05-MAY-2012  19:23:40  4.13733
      08-MAY-2012  21:12:11  4.81434
      11-MAY-2012  17:19:23  4.34395
      14-MAY-2012  13:26:42  4.41361
      17-MAY-2012  07:40:53  4.43868
      19-MAY-2012  22:08:18  4.20894
      22-MAY-2012  14:29:12  4.27568
      25-MAY-2012  04:55:35  4.22526
      27-MAY-2012  19:22:06  4.03179
      29-MAY-2012  16:46:53  2.99687
 
      XM GRAIL-A Angular momentum desaturation maneuvers
 
      Time(TDB)             dV (mm/sec)
      30-AUG-2012 16:17:08  3.27194
      02-SEP-2012 01:58:51  4.00243
      04-SEP-2012 11:06:17  4.26111
      06-SEP-2012 12:51:12  3.66917
      08-SEP-2012 14:36:08  3.74911
      12-SEP-2012 23:36:37  4.35803
      15-SEP-2012 08:43:02  4.53634
      20-SEP-2012 01:07:07  4.35287
      22-SEP-2012 10:14:06  4.45473
      26-SEP-2012 19:14:49  4.35090
      29-SEP-2012 04:20:58  4.17409
      03-OCT-2012 22:35:43  3.80467
      06-OCT-2012 07:42:52  3.81365
      11-OCT-2012 00:05:07  3.84110
      13-OCT-2012 09:11:49  3.48413
      17-OCT-2012 23:45:09  2.89231
      20-OCT-2012 08:51:56  2.87865
      24-OCT-2012 17:52:37  2.91584
      27-OCT-2012 02:59:07  2.95717
      31-OCT-2012 21:14:06  3.26799
      03-NOV-2012 06:20:59  3.35196
      08-NOV-2012 00:34:10  3.76771
      10-NOV-2012 09:41:17  3.95966
      15-NOV-2012 02:05:08  4.14310
      17-NOV-2012 11:11:41  4.26021
      22-NOV-2012 05:13:52  4.42137
      24-NOV-2012 14:10:07  4.17644
      26-NOV-2012 23:06:32  4.13729
      29-NOV-2012 09:52:37  4.24329
      01-DEC-2012 20:38:11  4.15837
      04-DEC-2012 07:24:06  4.06381
      08-DEC-2012 15:43:35  3.14428
      12-DEC-2012 18:13:41  2.99236
 
      3) GPA reboots
 
      During PM and XM the LGRS Gravity Processor Assemby (GPA)
      rebooted several times resulting in the loss of Ka range and the
      Time Transfer System (TTS) observables for about 1.5 minutes.
      After a GPA reboot the LGRS clock is synched with the LGRS clock
      on the non-rebooting spacecraft using the TTS system. GPA
      reboots will cause a gap in the inter-satellite range data
      products (KBR1B, SBR1B) of about 2 minutes. In the tables below
      all GPA reboots are listed. The reboot times are approximate and
      can be off as much as 30 seconds.
 
      PM GRAIL-A GPA reboots table
 
      time (UTC)                  data gap (sec)
      11-Apr-2012   17:37:29      80.0
 
      XM GRAIL-A GPA reboots table
 
      time (UTC)                  data gap (sec)
      30-AUG-2012 23:31:44.000    80.0
      06-DEC-2012 17:11:43.000    90.0
      08-DEC-2012 02:59:03.000    80.0
 
      4) S-band phase resets
 
      Applicable to GRAIL-B but not GRAIL-A
 
      5) X-band and S-band antenna switching
 
      Due to orbital viewing geometry the GRAIL spacecraft are
      changing between the +X and -X S-band and X-band (Radio Science
      Beacon) antennas approximately every 14 days. The complete
      history for the antenna change are listed in the VGS1B product
      (S-band) and VGX1B product (X-band).
 
      6) Ka boresight vector calibrations
 
      During the primary and extended missions, the GRAIL spacecraft
      were in nominal science attitude called orbiter point attitude
      mode. For this mode the solar arrays of the spacecraft are
      parallel to the orbital plane and the Ka boresight vectors (2.1
      degrees off the -Z axis in the YZ spacecraft frame) are pointed
      in the direction of line of sight toward the other spacecraft.
      The GRAIL spacecraft remained in orbit point attitude mode
      except during Ka boresight vector calibration maneuvers when the
      spacecraft performed two orthogonal slews of 3 deg about the
      line of sight vector between the two spacecraft. The tables
      below are showing all the Ka boresight calibration maneuvers for
      each spacecraft. LGRS measurements are taken during the
      maneuvers but should not be used in the science processing
      because the measured range change is the sum of orbit geometry,
      lunar gravity, and range change induced by spacecraft attitude
      variation. Ka boresight vector data contain range corrections
      for the phase center to center of mass offset during the
      maneuvers but these corrections are not reliable and should not
      be used.
 
      PM GRAIL-A Ka boresight maneuvers
 
      start time (UTC)      end time (UTC)
      02-MAR-2012  19:20    02-MAR-2012  19:35
      08-MAR-2012  20:05    08-MAR-2012  20:20
      08-MAR-2012  21:05    08-MAR-2012  21:20
      08-MAR-2012  16:54    08-MAR-2012  17:09
      08-MAR-2012  17:55    08-MAR-2012  18:10
      03-APR-2012  19:30    03-APR-2012  19:45
      03-APR-2012  20:30    03-APR-2012  20:45
      02-MAY-2012  16:40    02-MAY-2012  16:55
      02-MAY-2012  17:40    02-MAY-2012  17:55
      29-MAY-2012  09:21    29-MAY-2012  09:36
      29-MAY-2012  11:15    29-MAY-2012  11:30
 
      XM GRAIL-A Ka boresight maneuvers
 
      start time (UTC)      end time (UTC)
      05-SEP-2012  10:00    05-SEP-2012  10:15
      05-SEP-2012  11:00    05-SEP-2012  11:15
      12-SEP-2012  10:00    12-SEP-2012  10:15
      12-SEP-2012  11:00    12-SEP-2012  11:15
      19-SEP-2012  10:00    19-SEP-2012  10:15
      19-SEP-2012  11:00    19-SEP-2012  11:15
      26-SEP-2012  10:00    26-SEP-2012  10:15
      26-SEP-2012  11:00    26-SEP-2012  11:15
      03-OCT-2012  10:00    03-OCT-2012  10:15
      03-OCT-2012  11:00    03-OCT-2012  11:15
      10-OCT-2012  10:00    10-OCT-2012  10:15
      10-OCT-2012  11:00    10-OCT-2012  11:15
      17-OCT-2012  10:00    17-OCT-2012  10:15
      17-OCT-2012  11:00    17-OCT-2012  11:15
      24-OCT-2012  10:00    24-OCT-2012  10:15
      24-OCT-2012  11:00    24-OCT-2012  11:15
      31-OCT-2012  10:00    31-OCT-2012  10:15
      31-OCT-2012  11:00    31-OCT-2012  11:15
      07-NOV-2012  10:00    07-NOV-2012  10:15
      07-NOV-2012  11:00    07-NOV-2012  11:15
      14-NOV-2012  10:00    14-NOV-2012  10:15
      14-NOV-2012  11:00    14-NOV-2012  11:15
      21-NOV-2012  10:00    21-NOV-2012  10:15
      21-NOV-2012  11:00    21-NOV-2012  11:15
      28-NOV-2012  10:00    28-NOV-2012  10:15
      28-NOV-2012  11:00    28-NOV-2012  11:15
      08-DEC-2012  10:00    08-DEC-2012  10:15
      08-DEC-2012  11:00    08-DEC-2012  11:15
      11-DEC-2012  22:00    11-DEC-2012  22:15
      11-DEC-2012  23:00    11-DEC-2012  23:15
 
 
      Calibration Description - Spacecraft
      ====================================
      Performance calibrations were done on the ground and the
      requirements for a measurement were met if science instrument
      temperatures were used to calibrate the science measurements.
      During the Prime Mission, other error sources dominated the
      gravity field determination, but with the inclusion of the
      Extended Mission, the temperature-correlated science
      measurements will be applied.
 
 
      Platform Mounting Descriptions - Spacecraft
      ===========================================
      Platform mounting is part of the instrument design. The
      following antennas are mounted to each spacecraft:
 
      - 2 S-band transponder antennas to communicate with Earth
      (LGA1 & LGA2)
      - 2 X-band beacon antennas for Doppler ranging measurements from
      Earth of the Moon's near side (RSB1 & RSB2)
      - S-band time-transfer system (TTS) antenna, which sends a
      time-synchronization code back and forth between the spacecraft
      - Ka-band ranging antenna for precision distance measurement
      between the spacecraft
 
      The spacecraft frame is defined such that the -Y axis of GRAIL-A
      and the +Y axis of GRAIL-B point to nadir. The solar panels are
      on the -X side of each spacecraft. The +/-Z axes of the
      spacecraft are along the direction of flight.
 
      The two S-Band transponder antennas are on opposite faces of the
      spacecraft to provide full sky coverage. The LGA1 boresight is
      along the -X axis of the spacecraft, facing in the direction of
      the solar panels. LGA2 is on the opposite side, facing the +X
      direction.
 
      The two RSB antennas are oriented similarly, with RSB1 on the -X
      side and RSB2 on the +X side. During the mission, transmissions
      switch between the two in sync with the S-Band transponder
      antennas.
 
      The Ka-Band Antenna Assembly and the TTS are oriented along the
      -Z axis of the spacecraft. Since these antennas point at each
      other to form a communications link, one is always pointed in
      the direction of flight while the other is pointed away. During
      the prime mission, the direction of flight is along GRAIL-A's -Z
      axis and GRAIL-B's +Z axis. During extended mission, they are
      reversed. In addition, the antennae on each spacecraft are
      rotated 45 degrees around their boresight, so that in the flight
      configuration they form mirror images of each other. This allows
      orthogonal polarizations to separate the transmit and receive
      channels in the antenna.
 
      For more specific information, see
      lib_10_grail_coord_trans_rev1.pdf in the document directory.
 
 
    Instrument Overview - DSN
    =========================
      Three Deep Space Communications Complexes (DSCCs) (near Barstow,
      CA; Canberra, Australia; and Madrid, Spain) comprise the DSN
      tracking network.  Each complex is equipped with several
      antennas [including at least one each 70-m, 34-m High Efficiency
      (HEF), and 34-m Beam WaveGuide (BWG)], associated electronics,
      and operational systems.  Primary activity at each complex is
      radiation of commands to and reception of telemetry data from
      active spacecraft.  Transmission and reception is possible in
      several radio-frequency bands, the most common being S-band
      (nominally a frequency of 2100-2300 MHz or a wavelength of
      14.2-13.0 cm) and X-band (7100-8500 MHz or 4.2-3.5 cm).
      Transmitter output powers of up to 400 kW are available.
 
      Ground stations have the ability to transmit coded and uncoded
      waveforms which can be echoed by distant spacecraft.  Analysis
      of the received coding allows navigators to determine the
      distance to the spacecraft; analysis of Doppler shift on the
      carrier signal allows estimation of the line-of-sight spacecraft
      velocity.  Range and Doppler measurements are used to calculate
      the spacecraft trajectory and to infer gravity fields of objects
      near the spacecraft.
 
      Ground stations can record spacecraft signals that have
      propagated through or been scattered from target media.
      Measurements of signal parameters after wave interactions with
      surfaces, atmospheres, rings, and plasmas are used to infer
      physical and electrical properties of the target.
 
      Principal investigators vary from experiment to experiment. See
      the corresponding section of the spacecraft instrument
      description or the data set description for specifics.
 
      The Deep Space Network is managed by the Jet Propulsion
      Laboratory of the California Institute of Technology for the
      U.S. National Aeronautics and Space Administration.
      Specifications include:
 
      Instrument Id                  : RSS
      Instrument Host Id             : DSN
      Pi Pds User Id                 : N/A
      Instrument Name                : RADIO SCIENCE SUBSYSTEM
      Instrument Type                : RADIO SCIENCE
      Build Date                     : N/A
      Instrument Mass                : N/A
      Instrument Length              : N/A
      Instrument Width               : N/A
      Instrument Height              : N/A
      Instrument Manufacturer Name   : N/A
 
      For more information on the Deep Space Network and its use in
      radio science see reports by [ASMAR&RENZETTI1993] and
      [ASMARETAL1995].  For design specifications on DSN subsystems
      see [DSN810-5].
 
 
    Subsystems - DSN
    ================
      The Deep Space Communications Complexes (DSCCs) are an integral
      part of Radio Science instrumentation, along with the spacecraft
      Radio Frequency Subsystem.  Their system performance directly
      determines the degree of success of Radio Science
      investigations, and their system calibration determines the
      degree of accuracy in the results of the experiments.  The
      following paragraphs describe the functions performed by the
      individual subsystems of a DSCC.  This material has been
      adapted from [ASMARETAL1995] and [JPLD-14027]; for additional
      information, consult [DSN810-5].
 
      Each DSCC includes a set of antennas, a Signal Processing
      Center (SPC), and communication links to the Jet Propulsion
      Laboratory (JPL).  The general configuration is illustrated
      below; antennas (Deep Space Stations, or DSS -- a term carried
      over from earlier times when antennas were individually
      instrumented) are listed in the table.
 
          --------   --------   --------   --------   --------
         | DSS 25 | | DSS 27 | | DSS 14 | | DSS 15 | | DSS 16 |
         |34-m BWG| |34-m HSB| |  70-m  | |34-m HEF| |  26-m  |
          --------   --------   --------   --------   --------
              |            |     |             |          |
              |            v     v             |          v
              |           ---------            |     ---------
               --------->|GOLDSTONE|<----------     |EARTH/ORB|
                         | SPC  10 |<-------------->|   LINK  |
                          ---------                  ---------
                         |   SPC   |<-------------->|   26-M  |
                         |  COMM   |         ------>|   COMM  |
                          ---------         |        ---------
                              |             |            |
                              v             |            v
             ------       ---------         |        ---------
            | NOCC |<--->|   JPL   |<-------        |         |
             ------      | CENTRAL |                |   GSFC  |
             ------      |   COMM  |                | NASCOMM |
            | MCCC |<--->| TERMINAL|<-------------->|         |
             ------       ---------                  ---------
                                                      ^     ^
                                                      |     |
                   CANBERRA (SPC 40) <----------------      |
                                                            |
                     MADRID (SPC 60) <----------------------
 
                          GOLDSTONE     CANBERRA      MADRID
             Antenna        SPC 10       SPC 40       SPC 60
            --------      ---------     --------     --------
            26-m            DSS 16       DSS 46       DSS 66
            34-m HEF        DSS 15       DSS 45       DSS 65
            34-m BWG        DSS 24       DSS 34       DSS 54
                            DSS 25
                            DSS 26
            34-m HSB        DSS 27
                            DSS 28
            70-m            DSS 14       DSS 43       DSS 63
            Developmental   DSS 13
 
 
      Subsystem interconnections at each DSCC are shown in the diagram
      below, and they are described in the sections that follow.  The
      Monitor and Control Subsystem is connected to all other
      subsystems; the Test Support Subsystem can be.
 
       -----------   ------------------   ---------   ---------
      |TRANSMITTER| |                  | | TRACKING| | COMMAND |
      | SUBSYSTEM |-| RECEIVER/EXCITER |-|SUBSYSTEM|-|SUBSYSTEM|-
       -----------  |                  |  ---------   ---------  |
             |      |     SUBSYSTEM    |       |           |     |
       -----------  |                  |  ---------------------  |
      | MICROWAVE | |                  | |      TELEMETRY      | |
      | SUBSYSTEM |-|                  |-|      SUBSYSTEM      |-
       -----------   ------------------   ---------------------  |
             |                                                   |
       -----------    -----------    ---------   --------------  |
      |  ANTENNA  |  |  MONITOR  |  |   TEST  | |    DIGITAL   | |
      | SUBSYSTEM |  |AND CONTROL|  | SUPPORT | |COMMUNICATIONS|-
       -----------   | SUBSYSTEM |  |SUBSYSTEM| |   SUBSYSTEM  |
                      -----------    ---------   --------------
 
 
      DSCC Monitor and Control Subsystem
      ----------------------------------
        The DSCC Monitor and Control Subsystem (DMC) is part of the
        Monitor and Control System (MON) which also includes the
        ground communications Central Communications Terminal and the
        Network Operations Control Center (NOCC) Monitor and Control
        Subsystem.  The DMC is the center of activity at a DSCC.  The
        DMC receives and archives most of the information from the
        NOCC needed by the various DSCC subsystems during their
        operation.  Control of most of the DSCC subsystems, as well
        as the handling and displaying of any responses to control
        directives and configuration and status information received
        from each of the subsystems, is done through the DMC.  The
        effect of this is to centralize the control, display, and
        archiving functions necessary to operate a DSCC. Communication
        among the various subsystems is done using a Local Area
        Network (LAN) hooked up to each subsystem via a network
        interface unit (NIU).
 
 
      DSCC Antenna Mechanical Subsystem
      ---------------------------------
        Multi-mission Radio Science activities require support from
        the 70-m, 34-m HEF, and 34-m BWG antenna subnets.  The
        antennas at each DSCC function as large-aperture collectors
        which, by double reflection, cause the incoming radio
        frequency (RF) energy to enter the feed horns.  The large
        collecting surface of the antenna focuses the incoming energy
        onto a subreflector, which is adjustable in both axial and
        angular position.  These adjustments are made to correct for
        gravitational deformation of the antenna as it moves between
        zenith and the horizon; the deformation can be as large as
        5 cm.  The subreflector adjustments optimize the channeling
        of energy from the primary reflector to the subreflector
        and then to the feed horns.  The 70-m and 34-m HEF antennas
        have 'shaped' primary and secondary reflectors, with forms
        that are modified paraboloids.  This customization allows
        more uniform illumination of one reflector by another.  The
        BWG reflector shape is ellipsoidal.
 
        On the 70-m antennas, the subreflector directs received energy
        from the antenna onto a dichroic plate, a device which
        reflects S-band energy to the S-band feed horn and passes
        X-band energy through to the X-band feed horn.  In the 34-m
        HEF, there is one 'common aperture feed,' which accepts both
        frequencies without requiring a dichroic plate. In the 34-m
        BWG, a series of small mirrors (approximately 2.5 meters in
        diameter) directs microwave energy from the subreflector
        region to a collection area at the base of the antenna --
        typically in a pedestal room.  A retractable dichroic
        reflector separates S- and X-band on some BWG antennas or X-
        and Ka-band on others.  RF energy to be transmitted into space
        by the horns is focused by the reflectors into narrow
        cylindrical beams, pointed with high precision (either to the
        dichroic plate or directly to the subreflector) by a series of
        drive motors and gear trains that can rotate the movable
        components and their support structures.
 
        The different antennas can be pointed by several means.  Two
        pointing modes commonly used during tracking passes are
        CONSCAN and 'blind pointing.' With CONSCAN enabled and a
        closed loop receiver locked to a spacecraft signal, the
        system tracks the radio source by conically scanning around
        its position in the sky.  Pointing angle adjustments are
        computed from signal strength information (feedback) supplied
        by the receiver.  In this mode the Antenna Pointing Assembly
        (APA) generates a circular scan pattern which is sent to the
        Antenna Control System (ACS).  The ACS adds the scan pattern
        to the corrected pointing angle predicts.  Software in the
        receiver-exciter controller computes the received signal
        level and sends it to the APA.  The correlation of scan
        position with the received signal level variations allows the
        APA to compute offset changes which are sent to the ACS.
        Thus, within the capability of the closed-loop control
        system, the scan center is pointed precisely at the apparent
        direction of the spacecraft signal source.  An additional
        function of the APA is to provide antenna position angles and
        residuals, antenna control mode/status information, and
        predict-correction parameters to the Area Routing Assembly
        (ARA) via the LAN, which then sends this information to JPL
        via the Ground Communications Facility (GCF) for antenna
        status monitoring.
 
        During periods when excessive signal level dynamics or low
        received signal levels are expected (e.g., during an
        occultation experiment), CONSCAN should not be used.  Under
        these conditions, blind pointing (CONSCAN OFF) is used, and
        pointing angle adjustments are based on a predetermined
        Systematic Error Correction (SEC) model.
 
        Independent of CONSCAN state, subreflector motion in at least
        the z-axis may introduce phase variations into the received
        Radio Science data.  For that reason, during certain
        experiments, the subreflector in the 70-m and 34-m HEFs may
        be frozen in the z-axis at a position (often based on
        elevation angle) selected to minimize phase change and signal
        degradation.  This can be done via Operator Control Inputs
        (OCIs) from the LMC to the Subreflector Controller (SRC)
        which resides in the alidade room of the antennas.  The SRC
        passes the commands to motors that drive the subreflector to
        the desired position.
 
        Pointing angles for all antenna types are computed by
        the NOCC Support System (NSS) from an ephemeris provided by
        the flight project.  These predicts are received and archived
        by the CMC.  Before each track, they are transferred to the
        APA, which transforms the direction cosines of the predicts
        into AZ-EL coordinates.  The LMC operator then downloads the
        antenna predict points to the antenna-mounted ACS computer
        along with a selected SEC model.  The pointing predicts
        consist of time-tagged AZ-EL points at selected time
        intervals along with polynomial coefficients for
        interpolation between points.
 
        The ACS automatically interpolates the predict points,
        corrects the pointing predicts for refraction and
        subreflector position, and adds the proper systematic error
        correction and any manually entered antenna offsets.  The ACS
        then sends angular position commands for each axis at the
        rate of one per second.  In the 70-m and 34-m HEF, rate
        commands are generated from the position commands at the
        servo controller and are subsequently used to steer the
        antenna.
 
        When not using binary predicts (the routine mode for
        spacecraft tracking), the antennas can be pointed using
        'planetary mode' -- a simpler mode which uses right ascension
        (RA) and declination (DEC) values.  These change very slowly
        with respect to the celestial frame.  Values are provided to
        the station in text form for manual entry.  The ACS
        quadratically interpolates among three RA and DEC points
        which are on one-day centers.
 
        A third pointing mode -- sidereal -- is available for
        tracking radio sources fixed with respect to the celestial
        frame.
 
        Regardless of the pointing mode being used, a 70-m antenna
        has a special high-accuracy pointing capability called
        'precision' mode.  A pointing control loop derives the
        main AZ-EL pointing servo drive error signals from a two-
        axis autocollimator mounted on the Intermediate Reference
        Structure.  The autocollimator projects a light beam to a
        precision mirror mounted on the Master Equatorial drive
        system, a much smaller structure, independent of the main
        antenna, which is exactly positioned in HA and DEC with shaft
        encoders.  The autocollimator detects elevation/cross-
        elevation errors between the two reference surfaces by
        measuring the angular displacement of the reflected light
        beam.  This error is compensated for in the antenna servo by
        moving the antenna in the appropriate AZ-EL direction.
        Pointing accuracies of 0.004 degrees (15 arc seconds) are
        possible in 'precision' mode.  The 'precision' mode is not
        available on 34-m antennas -- nor is it needed, since their
        beamwidths are twice as large as on the 70-m antennas.
 
 
      DSCC Antenna Microwave Subsystem
      --------------------------------
        70-m Antennas: Each 70-m antenna has three feed cones
        installed in a structure at the center of the main reflector.
        The feeds are positioned 120 degrees apart on a circle.
        Selection of the feed is made by rotation of the
        subreflector.  A dichroic mirror assembly, half on the S-band
        cone and half on the X-band cone, permits simultaneous use of
        the S- and X-band frequencies.  The third cone is devoted to
        R&D and more specialized work.
 
        The Antenna Microwave Subsystem (AMS) accepts the received S-
        and X-band signals at the feed horn and transmits them
        through polarizer plates to an orthomode transducer.  The
        polarizer plates are adjusted so that the signals are
        directed to a pair of redundant amplifiers for each
        frequency, thus allowing simultaneous reception of signals in
        two orthogonal polarizations.  For S-band these are two Block
        IVA S-band Traveling Wave Masers (TWMs); for X-band the
        amplifiers are Block IIA TWMs.
 
        34-m HEF Antennas:  The 34-m HEF uses a single feed for both
        S- and X-band.  Simultaneous S- and X-band receive as well as
        X-band transmit is possible thanks to the presence of an S/X
        'combiner' which acts as a diplexer.  For S-band, RCP or LCP
        is user selected through a switch so neither a polarizer nor
        an orthomode transducer is needed.  X-band amplification
        options include two Block II TWMs or an HEMT Low Noise
        Amplifier (LNA).  S-band amplification is provided by an FET
        LNA.
 
        34-m BWG Antennas: These antennas use feeds and low-noise
        amplifiers (LNA) in the pedestal room, which can be switched
        in and out as needed.  Typically the following modes are
        available:
           1. downlink non-diplexed path (RCP or LCP) to LNA-1, with
              uplink in the opposite circular polarization;
           2. downlink non-diplexed path (RCP or LCP) to LNA-2, with
              uplink in the opposite circular polarization
           3. downlink diplexed path (RCP or LCP) to LNA-1, with
              uplink in the same circular polarization
           4. downlink diplexed path (RCP or LCP) to LNA-2, with
              uplink in the same circular polarization
        For BWG antennas with dual-band capabilities (e.g., DSS 25)
        and dual LNAs, each of the above four modes can be used in a
        single-frequency or dual-frequency configuration.  Thus, for
        antennas with the most complete capabilities, there are
        sixteen possible ways to receive at a single frequency
        (2 polarizations, 2 waveguide path choices, 2 LNAs, and 2
        bands).
 
 
      DSCC Receiver-Exciter Subsystem
      -------------------------------
        The Receiver-Exciter Subsystem is composed of two groups of
        equipment: the closed-loop receiver group and the open-loop
        receiver group.  This subsystem is controlled by the
        Receiver-Exciter Controller (REC) which communicates
        directly with the DMC for predicts and OCI reception and
        status reporting.
 
        The exciter generates the S-band signal (or X-band for the
        34-m HEF only) which is provided to the Transmitter Subsystem
        for the spacecraft uplink signal.  It is tunable under
        command of the Digitally Controlled Oscillator (DCO) which
        receives predicts from the Metric Data Assembly (MDA).
 
        The diplexer in the signal path between the transmitter and
        the feed horn for all three antennas (used for simultaneous
        transmission and reception) may be configured such that it is
        out of the received signal path (in listen-only or bypass
        mode) in order to improve the signal-to-noise ratio in the
        receiver system.
 
        Closed Loop Receivers: The Block V receiver-exciter at the
        70-m stations allows for two receiver channels, each capable
        of L-Band (e.g., 1668 MHz frequency or 18 cm wavelength),
        S-band, or X-band reception, and an S-band exciter for
        generation of uplink signals through the low-power or
        high-power transmitter.
 
        The closed-loop receivers provide the capability for rapid
        acquisition of a spacecraft signal and telemetry lockup.  In
        order to accomplish acquisition within a short time, the
        receivers are predict driven to search for, acquire, and
        track the downlink automatically.  Rapid acquisition
        precludes manual tuning though that remains as a backup
        capability.  The subsystem utilizes FFT analyzers for rapid
        acquisition.  The predicts are NSS generated, transmitted to
        the CMC which sends them to the Receiver-Exciter Subsystem
        where two sets can be stored.  The receiver starts
        acquisition at uplink time plus one round-trip-light-time or
        at operator specified times.  The receivers may also be
        operated from the LMC without a local operator attending
        them.  The receivers send performance and status data,
        displays, and event messages to the LMC.
 
        Either the exciter synthesizer signal or the simulation
        (SIM) synthesizer signal is used as the reference for the
        Doppler extractor in the closed-loop receiver systems,
        depending on the spacecraft being tracked (and Project
        guidelines).  The SIM synthesizer is not ramped; instead it
        uses one constant frequency, the Track Synthesizer Frequency
        (TSF), which is an average frequency for the entire pass.
 
        The closed-loop receiver AGC loop can be configured to one
        of three settings: narrow, medium, or wide.  It will be
        configured such that the expected amplitude changes are
        accommodated with minimum distortion.  The loop bandwidth
        (2BLo) will be configured such that the expected phase
        changes can be accommodated while maintaining the best
        possible loop SNR.
 
        Open-Loop Receivers (OLR):  The OLR utilized a fixed first
        Local Oscillator (LO) frequency and a tunable second LO
        frequency to minimize phase noise and improve frequency
        stability.  The OLR consisted of an RF-to-IF downconverter
        located at the feed , an IF selection switch (IFS), and a
        Radio Science Receiver (RSR).  The RF-IF downconverters
        in the 70-m antennas were equipped for four IF channels:
        S-RCP, S-LCP, X-RCP, and X-LCP.  The 34-m HEF stations
        were equipped with a two-channel RF-IF: S-band and X-band.
        The IFS switched the IF input among the antennas.
 
 
      DSCC Transmitter Subsystem
      --------------------------
        The Transmitter Subsystem accepts the S-band frequency
        exciter signal from the Receiver-Exciter Subsystem exciter
        and amplifies it to the required transmit output level.  The
        amplified signal is routed via the diplexer through the feed
        horn to the antenna and then focused and beamed to the
        spacecraft.
 
        The Transmitter Subsystem power capabilities range from 18 kW
        to 400 kW.  Power levels above 18 kW are available only at
        70-m stations.
 
 
      DSCC Tracking Subsystem
      -----------------------
        The Tracking Subsystem primary functions are to acquire and
        maintain communications with the spacecraft and to generate
        and format radiometric data containing Doppler and range.
 
        The DSCC Tracking Subsystem (DTK) receives the carrier
        signals and ranging spectra from the Receiver-Exciter
        Subsystem.  The Doppler cycle counts are counted, formatted,
        and transmitted to JPL in real time.  Ranging data are also
        transmitted to JPL in real time.  Also contained in these
        blocks is the AGC information from the Receiver-Exciter
        Subsystem.  The Radio Metric Data Conditioning Team (RMDCT)
        at JPL produces an Archival Tracking Data File (ATDF) which
        contains Doppler and ranging data.
 
        In addition, the Tracking Subsystem receives from the CMC
        frequency predicts (used to compute frequency residuals and
        noise estimates), receiver tuning predicts (used to tune the
        closed-loop receivers), and uplink tuning predicts (used to
        tune the exciter).  From the LMC, it receives configuration
        and control directives as well as configuration and status
        information on the transmitter, microwave, and frequency and
        timing subsystems.
 
        The Metric Data Assembly (MDA) controls all of the DTK
        functions supporting the uplink and downlink activities.  The
        MDA receives uplink predicts and controls the uplink tuning
        by commanding the DCO.  The MDA also controls the Sequential
        Ranging Assembly (SRA).  It formats the Doppler and range
        measurements and provides them to the GCF for transmission to
        NOCC.
 
        The Sequential Ranging Assembly (SRA) measures the round trip
        light time (RTLT) of a radio signal traveling from a ground
        tracking station to a spacecraft and back.  From the RTLT,
        phase, and Doppler data, the spacecraft range can be
        determined.  A coded signal is modulated on an uplink carrier
        and transmitted to the spacecraft where it is detected and
        transponded back to the ground station.  As a result, the
        signal received at the tracking station is delayed by its
        round trip through space and shifted in frequency by the
        Doppler effect due to the relative motion between the
        spacecraft and the tracking station on Earth.
 
 
      DSCC Frequency and Timing Subsystem
      -----------------------------------
        The Frequency and Timing Subsystem (FTS) provides all
        frequency and timing references required by the other DSCC
        subsystems.  It contains four frequency standards of which
        one is prime and the other three are backups.  Selection of
        the prime standard is done via the CMC.  Of these four
        standards, two are hydrogen masers followed by clean-up loops
        (CUL) and two are cesium standards.  These four standards all
        feed the Coherent Reference Generator (CRG) which provides
        the frequency references used by the rest of the complex.  It
        also provides the frequency reference to the Master Clock
        Assembly (MCA) which in turn provides time to the Time
        Insertion and Distribution Assembly (TID) which provides UTC
        and SIM-time to the complex.
 
        JPL's ability to monitor the FTS at each DSCC is limited to
        the MDA calculated Doppler pseudo-residuals, the Doppler
        noise, the SSI, and to a system which uses the Global
        Positioning System (GPS).  GPS receivers at each DSCC receive
        a one-pulse-per-second pulse from the station's (hydrogen
        maser referenced) FTS and a pulse from a GPS satellite at
        scheduled times.  After compensating for the satellite signal
        delay, the timing offset is reported to JPL where a database
        is kept.  The clock offsets stored in the JPL database are
        given in microseconds; each entry is a mean reading of
        measurements from several GPS satellites and a time tag
        associated with the mean reading.  The clock offsets provided
        include those of SPC 10 relative to UTC (NIST), SPC 40
        relative to SPC 10, etc.
 
 
      Radio Science Receiver (RSR)
      ----------------------------
        A radio frequency (RF) spacecraft signal at S-band, X-band,
        or Ka-band is captured by a receiving antenna on Earth, down
        converted to an intermediate frequency (IF) near 300 MHz and
        then fed via a distribution network to one input of an IF
        Selector Switch (IFS).  The IFS allows each RSR to select any
        of the available input signals for its RSR Digitizer (DIG).
        Within the RSR the digitized signal is then passed to the
        Digitial Down Converter (DDC), VME Data Processor (VDP), and
        Data Processor (DP) [JPLD-16765].
 
        \       -----------      ------      -----      -----   -----
         \     | RF  TO IF |    |      |----|     |    |     | |     |
          |----|    DOWN   |----|      |----|     |----| DIG | |  DP |
         /     | CONVERTER |    |      |----|     |    |     | |     |
        /       -----------     |  IF  |----| IFS |     -----   -----
        ANTENNA               --| DIST |----|     |       |       |
                300 MHz IF    --|      | .. |     |     -----   -----
                FROM OTHER    --|      |----|     |    |     | |     |
                 ANTENNAS     --|      |     -----     | DDC | | VDP |
                                 ------                |     | |     |
                                                        -----   -----
                                                          |       |
                                                           -------
 
        In the DIG the IF signal is passed through a programmable
        attenuator, adjusted to provide the proper level to the
        Analog to Digital Converter (ADC).  The attenuated signal is
        then passed through a Band Pass Filter (BPF) which selects a
        frequency band in the range 265-375 MHz.  The filtered output
        from the BPF is then mixed with a 256 MHz Local Oscillator
        (LO), low pass filtered (LPF), and sampled by the ADC.  The
        output of the ADC is a stream of 8-bit real samples at 256
        Msamples/second (Msps).  DIG timing is derived from the
        station FTS 5 MHz clock and 1 pulse per second (1PPS)
        reference; the DIG generates a 256 MHz clock signal for later
        processing.  The 1PPS signal marks the data sample taken at
        the start of each second.
 
        The DDC selects one 16 MHz subchannel from the possible 128
        MHz bandwidth available from the DIG by using Finite Impulse
        Response (FIR) filters with revolving banks of filter
        coefficients.  The sample stream from the DIG is separated
        into eight decimated streams, each of which is fed into two
        sets of FIR filters.  One set of filters produces in-phase
        (I) 8-bit data while the other produces quadrature-phase (Q)
        8-bit data.  The center frequency of the desired 16 MHz
        channel is adjustable in 1 MHz steps and is usually chosen to
        be near the spacecraft carrier frequency.  After combining
        the I and Q sample streams, the DDC feeds the samples to the
        VDP.  The DDC also converts the 256 MHz data clock and 1PPS
        signals into a msec time code, which is also passed to the
        VDP.
 
        The VDP contains a quadruply-redundant set of custom boards
        which are controlled by a real-time control computer (RT).
        Each set of boards comprises a numerically controlled
        oscillator (NCO), a complex multiplier, a decimating FIR
        filter, and a data packer.  The 16 Msps complex samples
        from the DDC are digitally mixed with the NCO signal in the
        complex multiplier.  The NCO phase and frequency are updated
        every millisecond by the RT and are selected so that the
        center frequency of the desired portion of the 16 MHz channel
        is down-converted to 0 Hz.  The RT uses polynomials derived
        from frequency predictions.  The output of the complex
        multiplier is sent to the decimating FIR filter where its
        bandwidth and sample rate are reduced (see table below).  The
        decimating FIR filter also allows adjustment of the
        sub-channel gain to take full advantage of the dynamic range
        available in the hardware.  The data packer truncates samples
        to 1, 2, 4, 8, or 16 bits by dropping the least significant
        bits and packs them into 32-bit data words.  Q-samples are
        packed into the first 16 bits of the word, and I-samples into
        the least significant 16 bits (see below).  In 'narrow band'
        operation all four sets of sets of custom boards can be
        supported simultaneously.  In 'medium band' operation no more
        than two channels can be supported simultaneously.  In
        'wide band' operation, only one sub-channel can be recorded.
 
        |============================================================|
        |         RSR Sample Rates and Sample Sizes Supported        |
        |================+=======+======+=================+==========|
        |    Category    |  Rate | Size |    Data Rate    |Rec Length|
        |                | (ksps)|(bits)|(bytes/s) (rec/s)|  (bytes) |
        |================+=======+======+=========+=======+==========|
        |Narrow Band (NB)|     1 |   8  |    2000 |    1  |    2000  |
        |                |     2 |   8  |    4000 |    1  |    4000  |
        |                |     4 |   8  |    8000 |    1  |    8000  |
        |                |     8 |   8  |   16000 |    1  |   16000  |
        |                |    16 |   8  |   32000 |    2  |   16000  |
        |                |    25 |   8  |   50000 |    2  |   25000  |
        |                |    50 |   8  |  100000 |    4  |   25000  |
        |                |   100 |   8  |  200000 |   10  |   20000  |
        |                |     1 |  16  |    4000 |    1  |    4000  |
        |                |     2 |  16  |    8000 |    1  |    8000  |
        |                |     4 |  16  |   16000 |    1  |   16000  |
        |                |     8 |  16  |   32000 |    2  |   16000  |
        |                |    16 |  16  |   64000 |    4  |   16000  |
        |                |    25 |  16  |  100000 |    4  |   25000  |
        |                |    50 |  16  |  200000 |   10  |   20000  |
        |                |   100 |  16  |  400000 |   20  |   20000  |
        |Medium Band (MB)|   250 |   1  |   62500 |    5  |   12500  |
        |                |   500 |   1  |  125000 |    5  |   25000  |
        |                |  1000 |   1  |  250000 |   10  |   25000  |
        |                |  2000 |   1  |  500000 |   20  |   25000  |
        |                |  4000 |   1  | 1000000 |   40  |   25000  |
        |                |   250 |   2  |  125000 |    5  |   25000  |
        |                |   500 |   2  |  250000 |   10  |   25000  |
        |                |  1000 |   2  |  500000 |   20  |   25000  |
        |                |  2000 |   2  | 1000000 |   40  |   25000  |
        |                |  4000 |   2  | 2000000 |  100  |   20000  |
        |                |   250 |   4  |  250000 |   10  |   25000  |
        |                |   500 |   4  |  500000 |   20  |   25000  |
        |                |  1000 |   4  | 1000000 |   40  |   25000  |
        |                |  2000 |   4  | 2000000 |  100  |   20000  |
        |                |   250 |   8  |  500000 |   20  |   25000  |
        |                |   500 |   8  | 1000000 |   40  |   25000  |
        |                |  1000 |   8  | 2000000 |  100  |   20000  |
        |Wide Band (WB)  |  8000 |   1  | 2000000 |  100  |   20000  |
        |                | 16000 |   1  | 4000000 |  200  |   20000  |
        |                |  8000 |   2  | 4000000 |  200  |   20000  |
        |============================================================|
 
        |============================================================|
        |                        Sample Packing                      |
        |=================+==========================================|
        | Bits per Sample |  Contents of 32-bit Packed Data Register |
        |=================+==========================================|
        |         16      |     (Q1),(I1)                            |
        |          8      |     (Q2,Q1),(I2,I1)                      |
        |          4      |     (Q4,Q3,Q2,Q1),(I4,I3,I2,I1)          |
        |          2      |     (Q8,Q7,...Q1),(I8,I7,...I1)          |
        |          1      |     (Q16,Q15,...Q1),(I16,I15,...I1)      |
        |============================================================|
 
        Once per second the RT sends the accumulated data records from
        each sub-channel to the Data Processor (DP) over a 100 Mbit/s
        ethernet connection.  In addition to the samples, each data
        record includes header information such as time tags and NCO
        frequency and phase that are necessary for analysis.  The DP
        processes the data records to provide monitor data, such as
        power spectra.  If recording has been enabled, the records
        are stored by the DP.
 
 
        NCO Phase and Frequency
        -----------------------
          At the start of each DSN pass, the RSR is provided with a
          file containing a list of predicted frequencies. Using
          these points, the RT computes expected sky frequencies at
          the beginning, middle, and end of each one second time
          interval. Based on the local oscillator frequencies
          selected and any offsets entered, the RT computes the
          coefficients of a frequency polynomial fitted to the DDC
          channel frequencies at these three times.  The RT also
          computes a phase polynomial by integrating the frequency
          polynomial and matching phases at the one second
          boundaries.
 
          The phase and frequency of the VDP NCO's are computed every
          millisecond (000-999) from the polynomial coefficients as
          follows:
 
              nco_phase(msec) = phase_coef_1 +
                                phase_coef_2 * (msec/1000) +
                                phase_coef_3 * (msec/1000)**2 +
                                phase_coef_4 * (msec/1000)**3
 
              nco_freq(msec)  = freq_coef_1 +
                                freq_coef_2 * ((msec + 0.5)/1000) +
                                freq_coef_3 * ((msec + 0.5)/1000)**2
 
 
          The sky frequency may be reconstructed using
 
                  sky_freq = RF_to_IF_LO +
                             DDC_LO -
                             nco_freq +
                             reside_freq
 
            where  RF_to_IF_LO  is the down conversion from the
                                microwave frequency to IF (bytes
                                42-43 in the data record header)
                   DDC_LO       is the down-conversion applied in the
                                DIG and DDC (bytes 40-41 in the data
                                record header)
                   Resid_Freq   is the frequency of the signal in the
                                VDP output
 
 
    Detectors - DSN
    ===============
      Nominal carrier tracking loop threshold noise bandwidth at
      X-band is 10 Hz.  Coherent (two-way) closed-loop system
      stability is shown in the table below:
 
            integration time            Doppler uncertainty
                 (secs)               (one sigma, microns/sec)
                 ------               ------------------------
                    10                            50
                    60                            20
                  1000                             4
 
      For the open-loop subsystem, signal detection is done in
      software.
 
 
    Calibration - DSN
    =================
      Calibrations of hardware systems are carried out periodically
      by DSN personnel; these ensure that systems operate at required
      performance levels -- for example, that antenna patterns,
      receiver gain, propagation delays, and Doppler uncertainties
      meet specifications.  No information on specific calibration
      activities is available.  Nominal performance specifications
      are shown in the tables above.  Additional information may be
      available in [DSN810-5].
 
      Prior to each tracking pass, station operators perform a series
      of calibrations to ensure that systems meet specifications for
      that operational period.  Included in these calibrations is
      measurement of receiver system temperature in the configuration
      to be employed during the pass.  Results of these calibrations
      are recorded in (hard copy) Controller's Logs for each pass.
 
      The nominal procedure for initializing open-loop receiver
      attenuator settings is described below.  In cases where widely
      varying signal levels are expected, the procedure may be
      modified in advance or real-time adjustments may be made to
      attenuator settings.
 
 
    Operational Considerations - DSN
    ================================
      The DSN is a complex and dynamic 'instrument.' Its performance
      for Radio Science depends on a number of factors from equipment
      configuration to meteorological conditions.  No specific
      information on 'operational considerations' can be given here.
 
 
    Operational Modes - DSN
    =======================
 
      DSCC Antenna Mechanical Subsystem
      ---------------------------------
        Pointing of DSCC antennas may be carried out in several ways.
        For details see the subsection 'DSCC Antenna Mechanical
        Subsystem' in the 'Subsystem' section.  Binary pointing is
        the preferred mode for tracking spacecraft; pointing
        predicts are provided, and the antenna simply follows those.
        With CONSCAN, the antenna scans conically about the optimum
        pointing direction, using closed-loop receiver signal
        strength estimates as feedback.  In planetary mode, the
        system interpolates from three (slowly changing) RA-DEC
        target coordinates; this is 'blind' pointing since there is
        no feedback from a detected signal.  In sidereal mode, the
        antenna tracks a fixed point on the celestial sphere.  In
        'precision' mode, the antenna pointing is adjusted using an
        optical feedback system.  It is possible on most antennas to
        freeze z-axis motion of the subreflector to minimize phase
        changes in the received signal.
 
 
      DSCC Receiver-Exciter Subsystem
      -------------------------------
        The diplexer in the signal path between the transmitter and
        the feed horns on all antennas may be configured so
        that it is out of the received signal path in order to
        improve the signal-to-noise ratio in the receiver system.
        This is known as the 'listen-only' or 'bypass' mode.
 
 
      Closed-Loop Receiver AGC Loop
      -----------------------------
        The closed-loop receiver AGC loop can be configured to one of
        three settings: narrow, medium, or wide.  Ordinarily it is
        configured so that expected signal amplitude changes are
        accommodated with minimum distortion.  The loop bandwidth is
        ordinarily configured so that expected phase changes can be
        accommodated while maintaining the best possible loop SNR.
 
 
      Coherent vs. Non-Coherent Operation
      -----------------------------------
        The frequency of the signal transmitted from the spacecraft
        can generally be controlled in two ways -- by locking to a
        signal received from a ground station or by locking to an
        on-board oscillator.  These are known as the coherent (or
        'two-way') and non-coherent ('one-way') modes, respectively.
        Mode selection is made at the spacecraft, based on commands
        received from the ground.  When operating in the coherent
        mode, the transponder carrier frequency is derived from the
        received uplink carrier frequency with a 'turn-around ratio'
        typically of 880/749.  In the non-coherent mode, the
        downlink carrier frequency is derived from the spacecraft
        on-board crystal-controlled oscillator.  Either closed-loop
        or open-loop receivers (or both) can be used with either
        spacecraft frequency reference mode.  Closed-loop reception
        in two-way mode is usually preferred for routine tracking.
        Occasionally the spacecraft operates coherently while two
        ground stations receive the 'downlink' signal; this is
        sometimes known as the 'three-way' mode.
 
 
    Location - DSN
    ==============
      Station locations are documented in [DSN810-005-301H].  Geocentric
      coordinates are summarized here. All antennas are AZ-EL type unless
      otherwise specified.
 
 
    Antenna Geocentric Coordinates
    ------------------------------
    Name    Description  Latitude       Longitude       Geocentric Radius
                         (deg)          (deg)           (m)
    ---------------------------------------------------------------------
Goldstone
    DSS 13  34-m R & D   35.0660180     243.2055410     6372125.096
    DSS 14  70-m         35.2443523     243.1104618     6371993.267
    DSS 15  34-m HEF     35.2403129     243.1128049     6371966.511
    DSS 24  34-m BWG     35.1585346     243.1252056     6371973.601
    DSS 25  34-m BWG     35.1562591     243.1246368     6371982.537
    DSS 26  34-m BWG     35.1543409     243.1269835     6371992.264
    DSS 27  34-m HSB     35.0571452     243.2233496     6372110.240
Canberra
    DSS 34  34-m BWG    -35.2169824     148.9819644     6371693.538
    DSS 43  70-m        -35.2209189     148.9812673     6371688.998
    DSS 45  34-m HEF    -35.2169608     148.9776856     6371675.873
Madrid
    DSS 54  34-m BWG     40.2357726     355.7459032     6370025.490
    DSS 55  34-m BWG     40.2344478     355.7473667     6370007.988
    DSS 63  70-m         40.2413554     355.7519915     6370051.198
    DSS 65  34-m HEF     40.2373555     355.7493011     6370021.709
 
 
    Measurement Parameters - DSN
    ============================
      Closed-loop data are recorded in Archival Tracking Data Files
      (ATDFs), as well as certain secondary products such as the
      Orbit Data File (ODF).  The ATDF Tracking Logical Record
      contains 150 entries including status information and
      measurements of ranging, Doppler, and signal strength.
 
 
    ACRONYMS AND ABBREVIATIONS - DSN
    ================================
      ACS      Antenna Control System
      ADC      Analog-to-Digital Converter
      AGC      Automatic Gain Control
      AMS      Antenna Microwave System
      APA      Antenna Pointing Assembly
      ARA      Area Routing Assembly
      ATDF     Archival Tracking Data File
      AUX      Auxiliary
      AZ       Azimuth
      BPF      Band Pass Filter
      bps      bits per second
      BWG      Beam WaveGuide (antenna)
      CDU      Command Detector Unit
      CMC      Complex Monitor and Control
      CONSCAN  Conical Scanning (antenna pointing mode)
      CRG      Coherent Reference Generator
      CUL      Clean-up Loop
      DANA     a type of frequency synthesizer
      dB       deciBel
      dBi      dB relative to isotropic
      dBm      dB relative to one milliwatt
      DCO      Digitally Controlled Oscillator
      DDC      Digital Down Converter
      DEC      Declination
      deg      degree
      DIG      RSR Digitizer
      DMC      DSCC Monitor and Control Subsystem
      DOR      Differential One-way Ranging
      DP       Data Processor
      DSCC     Deep Space Communications Complex
      DSN      Deep Space Network
      DSP      DSCC Spectrum Processing Subsystem
      DSS      Deep Space Station
      DTK      DSCC Tracking Subsystem
      E        east
      EIRP     Effective Isotropic Radiated Power
      EL       Elevation
      FET      Field Effect Transistor
      FFT      Fast Fourier Transform
      FIR      Finite impulse Response
      FTS      Frequency and Timing Subsystem
      GCF      Ground Communications Facility
      GHz      Gigahertz
      GPS      Global Positioning System
      HA       Hour Angle
      HEF      High-Efficiency (as in 34-m HEF antennas)
      HEMT     High Electron Mobility Transistor (amplifier)
      HGA      High-Gain Antenna
      HSB      High-Speed BWG
      IF       Intermediate Frequency
      IFS      IF Selector Switch
      IVC      IF Selection Switch
      JPL      Jet Propulsion Laboratory
      K        Kelvin
      Ka-Band  approximately 32 GHz
      KaBLE    Ka-Band Link Experiment
      kbps     kilobits per second
      kHz      kilohertz
      km       kilometer
      kW       kilowatt
      LAN      Local Area Network
      LCP      Left-Circularly Polarized
      LGR      Low-Gain Receive (antenna)
      LGT      Low-Gain Transmit (antenna)
      LMA      Lockheed Martin Astronautics
      LMC      Link Monitor and Control
      LNA      Low-Noise Amplifier
      LO       Local Oscillator
      LPF      Low Pass Filter
      m        meters
      MCA      Master Clock Assembly
      MCCC     Mission Control and Computing Center
      MDA      Metric Data Assembly
      MGS      Mars Global Surveyor
      MHz      Megahertz
      MOLA     Mars Orbiting Laser Altimeter
      MON      Monitor and Control System
      MOT      Mars Observer Transponder
      MSA      Mission Support Area
      N        north
      NAR      Noise Adding Radiometer
      NBOC     Narrow-Band Occultation Converter
      NCO      Numerically Controlled Oscillator
      NIST     SPC 10 time relative to UTC
      NIU      Network Interface Unit
      NOCC     Network Operations and Control System
      NRV      NOCC Radio Science/VLBI Display Subsystem
      NSS      NOCC Support System
      OCI      Operator Control Input
      ODF      Orbit Data File
      ODR      Original Data Record
      ODS      Original Data Stream
      OLR      Open Loop Receiver
      OSC      Oscillator
      PDS      Planetary Data System
      POCA     Programmable Oscillator Control Assembly
      PPM      Precision Power Monitor
      RA       Right Ascension
      REC      Receiver-Exciter Controller
      RCP      Right-Circularly Polarized
      RF       Radio Frequency
      RIC      RIV Controller
      RIV      Radio Science IF-VF Converter Assembly
      RMDCT    Radio Metric Data Conditioning Team
      RMS      Root Mean Square
      RSR      Radio Science Receiver
      RSS      Radio Science Subsystem
      RT       Real-Time (control computer)
      RTLT     Round-Trip Light Time
      S-band   approximately 2100-2300 MHz
      sec      second
      SEC      System Error Correction
      SIM      Simulation
      SLE      Signal Level Estimator
      SNR      Signal-to-Noise Ratio
      SNT      System Noise Temperature
      SOE      Sequence of Events
      SPA      Spectrum Processing Assembly
      SPC      Signal Processing Center
      sps      samples per second
      SRA      Sequential Ranging Assembly
      SRC      Sub-Reflector Controller
      SSI      Spectral Signal Indicator
      TID      Time Insertion and Distribution Assembly
      TLM      Telemetry
      TSF      Tracking Synthesizer Frequency
      TWM      Traveling Wave Maser
      TWNC     Two-Way Non-Coherent
      TWTA     Traveling Wave Tube Amplifier
      UNK      unknown
      USO      UltraStable Oscillator
      UTC      Universal Coordinated Time
      VCO      Voltage-Controlled Oscillator
      VDP      VME Data Processor
      VF       Video Frequency
      X-band   approximately 7800-8500 MHz

        