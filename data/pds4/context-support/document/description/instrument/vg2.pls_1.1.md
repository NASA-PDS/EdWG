
 
      INSTRUMENT: PLASMA SCIENCE EXPERIMENT
      SPACECRAFT: VOYAGER 2
 
      Instrument Information
      ======================
      Instrument Id                  : PLS
      Instrument Host Id             : VG2
      Principal Investigator         : JOHN W. BELCHER
      Pi Pds User Id                 : JBELCHER
      Instrument Name                : PLASMA SCIENCE EXPERIMENT
      Instrument Type                : PLASMA INSTRUMENT
      Build Date                     : 1973-01-01
      Instrument Mass                : 9.900000
      Instrument Length              : UNK
      Instrument Width               : UNK
      Instrument Height              : UNK
      Instrument Serial Number       : SN001
      Instrument Manufacturer Name   : MASSACHUSETTS INSTITUTE OF
                                       TECHNOLOGY
 
      Instrument Description
      ======================
      The Voyager Plasma Science experiment consists of four
      modulated grid Faraday Cups, three (A,B,C) of which are
      positioned about the Telemetry Antenna Axis and generally
      point toward the Earth with the fourth (D) at a right angle to
      this direction.  Ion currents are sampled simultaneously in
      all four cups, electrons in the D-cup only.  The instrument
      has an energy/charge range of 10-5950 V.  Data is taken in
      four ways, high and low resolution ion modes and high and low
      energy electron modes, with energy resolution varying between
      3.6 and 29%.  The integration time for each energy channel can
      be varied are used at Jupiter and Saturn and 0.93 and 0.21
      second integration times are used at Uranus and Neptune.
      Supersonic flow can be observed only when one of the detectors
      points into the flow orientation allows determination of the
      plasma density, temperature, and velocity.
 
      Science Objectives
      ==================
      The objective of the Plasma Instrument is to characterize
      plasma conditions throughout the Voyager trajectory, in the
      solar wind and during the planetary encounters.
 
      Operational Considerations
      ==========================
      Each detector has an effective field of view which is a cone of
      half angle 45 degrees falls off quickly at higher angles.
      Thus, for the instrument to measure ion parameters in a
      Supersonic or Transonic plasma some of the detectors must look
      into the plasma flow. Secondary ions and electrons produced
      within the detectors can also effect the measurements,
      especially if large fluxes of hot ions or electrons are present
      and these effects are not well modeled. The instrument does
      not measure composition, only energy/charge, so a model of
      plasma composition must be adopted to fit the ion data choice
      of models can be unambiguous for large Mach number flow (M>3)
      but is non-unique for lower Mach numbers. After the Jupiter
      encounter the highest channels of the A, B, and C detectors
      often contain spurious signal and currents in the upper half of
      the energy range should be examined carefully before use.
 
      Calibration Description
      =======================
      The instrument was calibrated at MIT using ion and electron
      beams and compared to output from other Faraday cups in the
      same beam. Current levels are also calibrated in-flight by
      injecting known currents into the detectors with the modulators
      on and off. Much theoretical modeling has been done on the
      response of the detectors to arbitrary plasma conditions.
      Contact the PI for more information.
 
      PLS Detectors 'A', 'B', 'C', and 'D'
      ====================================
      Detector Type                  : FARADAY CUP
      Detector Aspect Ratio          : 0.000000
      Nominal Operating Temperature  : 278.000000
 
      The PLS instrument consists of four Faraday cups. Three of
      these (A, B, C) are arranged in a cone whose central axis is
      parallel to the direction of the telemetry antenna. The look
      direction of each of these cups is offset 20 degrees from the
      central axis. Detector D has a look direction approximately
      perpendicular to the direction of the telemetry antenna. Each
      detector consists of three modulator grids, six shield grids
      and a suppressor grid in front of the collector. It measures
      ion currents in the range 10-5950 V.
 
      Depending on the integration time the detectors measure current
      from a minimum of 3.e-14 to 2.e-13 AMPS up to a maximum of
      6.e-8 AMPS. Sampling varies from .03 to .93 seconds.
 
      'PLS' Section Parameter 'ELECTRON CURRENT'
      ------------------------------------------
      Sampling Parameter Name        : TIME
      Section Id                     : PLS
      Instrument Parameter Unit      : AMPS
      Minimum Instrument Parameter   : 0.000000
      Maximum Instrument Parameter   : 0.000000
      Minimum Sampling Parameter     : 0.030000
      Maximum Sampling Parameter     : 0.930000
      Sampling Parameter Unit        : SECOND
 
 
      'PLS' Section Parameter 'ION CURRENT'
      -------------------------------------
      Sampling Parameter Name        : TIME
      Section Id                     : PLS
      Instrument Parameter Unit      : AMPS
      Minimum Instrument Parameter   : 0.000000
      Maximum Instrument Parameter   : 0.000000
      Minimum Sampling Parameter     : 0.030000
      Maximum Sampling Parameter     : 0.930000
      Sampling Parameter Unit        : SECOND
 
      Electronics
      ===========
      Currents from the four detectors are amplified, filtered, and
      integrated using four different measurement chains. A single
      8-bit logarithmic A-D converter samples the four outputs of the
      measurement chains and transfers the data to the spacecraft.
      The high voltage modulator supplies a DC pedestal and a super-
      imposed 400 HZ square wave modulation voltage. For positive
      ions the modulator grids of all four detectors are driven in
      parallel. A more complete description and block diagram of the
      instrument electronics is available in [BRIDGEETAL1977].
 
      Operating Modes
      ===============
      The eight operating modes of Voyager PLS are listed below.
      Instrument power consumption is 8.100000 for all modes.
 
      E1-LONG:  Low energy electron mode which measures the range
                10-140 V with 16 contiguous channels. The
                integration time for each channel is 0.93 sec.
 
      E1-SHORT: Low energy electron mode which measures the range
                10-140 V with 16 contiguous channels. The
                integration time for each channel is 0.21 sec.
 
      E2-LONG:  High energy electron mode which measures the range
                10-5950 V with 16 contiguous channels.  The
                integration time for each channel is 0.93 sec.
 
      E2-SHORT: High energy electron mode which measures the range
                10-5950 V with 16 contiguous channels. The
                integration time for each channel is 0.21 sec.
 
      L-LONG:   Low resolution ion mode which measures the range
                10-5950 V with 16 contiguous channels.  The
                integration time for each channel is 0.93 sec.
 
      L-SHORT:  Low resolution ion mode which measures the range
                10-5950 V with 16 contiguous channels.  The
                integration time for each channel is 0.21 sec.
 
      M-LONG:   High resolution ion mode which measures the range
                10-5950 V with 128 contiguous channels.  The
                integration time for each channel is 0.93 sec.
 
      M-SHORT:  High resolution ion mode which measures the range
                10-5950 V with 128 contiguous channels. The
                integration time for each channel is 0.21 sec.
 
      Instrument Mounting
      ===================
      The PLS instrument is located on the Science Boom. The center
      of the main detector cluster (A, B, C) points parallel to the
      spacecraft telemetry antenna and detector D is at right angles
      to this direction.

        