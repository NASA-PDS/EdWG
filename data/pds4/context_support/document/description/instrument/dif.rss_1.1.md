
 
 
    Instrument Overview
    ===================
      The DI comet Tempel 1 flyby Radio Science investigations
      utilized instrumentation with elements on the spacecraft
      and at the NASA Deep Space Network (DSN).  Much of this
      was shared equipment, being used for routine telecommunications
      as well as for Radio Science.  The performance and calibration
      of both the spacecraft and tracking stations directly affected
      the radio science data accuracy, and they played a major role
      in determining the quality of the results.  The spacecraft part
      of the radio science instrument is described immediately below;
      that is followed by a description of the DSN (ground) part of
      the instrument.
 
 
    Instrument Specifications - Spacecraft
    ======================================
      The DI comet Tempel 1 flyby spacecraft telecommunications
      subsystem served as part of a radio science subsystem for
      investigations of Tempel 1.  Many details of the subsystem
      are unknown; its 'build date' is taken to be 1995-02-01,
      the date on which acceptance testing began at Ball.
 
 
      Instrument Id                  : RSS
      Instrument Host Id             : DI
      Pi Pds User Id                 : UNK
      Instrument Name                : RADIO SCIENCE SUBSYSTEM
      Instrument Type                : RADIO SCIENCE
      Build Date                     : 1995-02-01
      Instrument Mass                : UNK
      Instrument Length              : UNK
      Instrument Width               : UNK
      Instrument Height              : UNK
      Instrument Manufacturer Name   : Motorola
 
 
 
    Instrument Overview - Spacecraft
    ================================
      The DI flyby spacecraft radio system operates at X-band
      through the DSN 34 m (BWG) and 70 m nets to receive commands,
      downlink telemetry and provide tracking for navigation.  There
      are two low, and one high gain X-band antennas, two small
      deep-space transponders and a pair of 20W TWTA power amplifiers.
 
 
      The X-band capability reduced plasma effects on radio
      signals by a factor of 10 compared with previous S-band
      systems, but absence of a dual-frequency capability (both
      S- and X-band) meant that plasma effects could not be
      estimated and removed from radio data.
 
 
      The HGA was a 1.0 m diameter dish of a Cassegrain design that
      was directed in the spacecraft's +Z direction.
 
 
 
    Science Objectives
    ==================
      Because of the relatively distant flyby (close approach = 500 km) of
      the DI spacecraft past the nucleus of comet Tempel 1 and the rapid
      relative velocity of the flyby (10.1 km/s), there was not expected
      to be any indication of the spacecraft's deflection due to the
      neighboring comet mass nor was there expected to be any indication
      that the spacecraft was slowed down as a result of gas and dust drag
      upon the spacecraft.  Both of these expectations came to pass (i.e.,
      no effects noted in the tracking data).  Yet, it is not out of the
      question that future researchers will find a use for these tracking
      data.
 
 
 
    Operational Considerations - Spacecraft
    =======================================
      Descriptions given here are for nominal performance.  The
      spacecraft transponder system comprised redundant units,
      each with slightly different characteristics.  As
      transponder units age, their performance changes slightly.
      Their performance also depends upon factors which were not
      always under the control of the DI Project.
 
 
 
    Calibration Description - Spacecraft
    ====================================
      No information available.
 
 
 
    Platform Mounting Descriptions - Spacecraft
    ===========================================
      The spacecraft +Z axis vector was aligned with the HGA boresight
      perpendicular to the top surface of the spacecraft.  The +Y
      axis vector ran through the power switching electronics box
      and the +X axis completed the orthogonal, right-handed,
      rectangular coordinate system.
 
 
      The axes of the two low gain antennas were in the +Z and -Z
      directions.
 
 
 
    Investigators
    =============
      Team Leader for the DI Radio Science Team was D.K. Yeomans
      of the Jet Propulsion Laboratory (JPL).  Collaborating on
      this investigation were Jon D. Giorgini and Steve R. Chesley,
 
 
    Instrument Overview - DSN
    =========================
      Three Deep Space Communications Complexes (DSCCs) (near
      Barstow, CA; Canberra, Australia; and Madrid, Spain) comprise
      the DSN tracking network.  Each complex is equipped with
      several antennas [including at least one each 70-m, 34-m High
      Efficiency (HEF), and 34-m Beam WaveGuide (BWG)], associated
      electronics, and operational systems.  A primary activity
      at each complex is radiation of commands to and reception of
      telemetry data from active spacecraft.  Transmission and
      reception are possible in several radio frequency bands; the
      most common are S-band (nominally a frequency of 2100-2300 MHz,
      or a wavelength of 14.2-13.0 cm) and X-band (7100-8500 MHz, or
      4.2-3.5 cm).  Transmitter output powers of up to 100 kW S-band
      and 20 kW X-band are available.
 
      Ground stations have the ability to transmit coded and uncoded
      waveforms which can be echoed by distant spacecraft.  Analysis
      of the received coding allows navigators to determine the
      distance to the spacecraft; and analysis of Doppler shift on the
      carrier signal allows estimation of the line-of-sight
      spacecraft velocity.  Range and Doppler measurements are used
      to calculate the spacecraft trajectory and to infer gravity
      fields of objects near the spacecraft.
 
      Ground stations can record spacecraft signals that have
      propagated through or been scattered from target media.
      Measurements of signal parameters after wave interactions with
      surfaces, atmospheres, rings, and plasmas are used to infer
      physical and electrical properties of the target.
 
      The Deep Space Network (DSN) is managed by the Jet Propulsion
      Laboratory (JPL) of the California Institute of Technology for
      the U.S. National Aeronautics and Space Administration (NASA).
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
      radio science see reports by [ASMAR&RENZETTI1993],
      [ASMAR&HERRERA1993], and [ASMARETAL1995].  For design
      specifications on DSN subsystems see [DSN810-5].
 
 
    Subsystems - DSN
    ================
      The Deep Space Communications Complexes (DSCCs) are an integral
      part of Radio Science instrumentation, along with the spacecraft
      RFS and RFIS.  Their system performance directly determines the
      degree of success of Radio Science investigations, and their
      system calibration determines the degree of accuracy in the
      results of the experiments.  The following paragraphs describe
      the functions performed by the individual subsystems of a DSCC.
      This material has been adapted from [ASMAR&HERRERA1993] and
      [DSN871-011]; for additional information, consult [DSN810-5],
      [DSN821-110], and [DSN821-104].
 
      Each DSCC includes a set of antennas, a Signal Processing
      Center (SPC), and communication links to the Jet Propulsion
      Laboratory (JPL).  The general configuration is illustrated
      below.
 
 
          --------   --------   --------   --------   --------
         | DSS 25 | | DSS 27 | | DSS 14 | | DSS 15 | | DSS 16 |
         |34-m BWG| |34-m HSB| |  70-m  | |34-m HEF| |  26-m  |
          --------   --------   --------   --------   --------
              |            |     |             |          |
              |            v     v             |          v
              |           ---------            |     ---------
               --------->|GOLDSTONE|<----------     |EARTH/ORB|
                         | SPC  10 |<-------------->|   LINK  |
                         |---------|                |---------|
                         |   SPC   |<-------------->|   26-M  |
                         |  COMM   |         ------>|   COMM  |
                          ---------         |        ---------
                              |             |            |
                              v             |            v
             ------       ---------         |        ---------
            | NOCC |<--->|   JPL   |<-------        |         |
             ------      | CENTRAL |                |  GSFC   |
             ------      |   COMM  |                | NASCOMM |
            |AMMOS |<--->| TERMINAL|<-------------->|         |
             ------       ---------                  ---------
                                                      ^     ^
                                                      |     |
                   CANBERRA (SPC 40) <----------------      |
                                                            |
                     MADRID (SPC 60) <----------------------
 
 
      The following table gives a list of the current DSN antennas
      (Deep Space Stations, or DSSs -- a term carried over from
      earlier times when antennas were individually instrumented).
 
 
                          GOLDSTONE     CANBERRA      MADRID
            Antenna        SPC 10        SPC 40       SPC 60
            --------      ---------     --------     --------
            26-m            DSS 16       DSS 46       DSS 66
            34-m HEF        DSS 15       DSS 45       DSS 65
            34-m BWG        DSS 24       DSS 34       DSS 54
                            DSS 25                    DSS 55
                            DSS 26
            34-m HSB        DSS 27
                            DSS 28
            70-m            DSS 14       DSS 43       DSS 63
            Developmental   DSS 13
 
 
      Subsystem interconnections at each DSCC are shown in the two
      diagrams below, and are described in the sections that follow.
      The first diagram is for the pre-NSP (Network Simplification
      Project) era, and the second diagram is for the post-NSP era.
      NSP implementation took place over a period of about 5 months
      in 2003 (from January through May).  The Monitor and Control
      Subsystem is connected to all other subsystems; and the Test
      Support Subsystem can be.
 
 
      Pre-NSP DSCC
      ------------
 
         -----------   ------------------   ---------   ---------
        |TRANSMITTER|_|                  |_| TRACKING|_| COMMAND |_
        | SUBSYSTEM | |                  | |SUBSYSTEM| |SUBSYSTEM| |
         -----------  | RECEIVER-EXCITER |  ---------   ---------  |
               |      |     SUBSYSTEM    |       |           |     |
         -----------  |                  |  ---------------------  |
        | MICROWAVE |_|                  |_|      TELEMETRY      |_|
        | SUBSYSTEM | |                  | |      SUBSYSTEM      | |
         -----------   ------------------   ---------------------  |
               |                                                   |
         -----------    -----------    ---------   --------------  |
        |  ANTENNA  |  |  MONITOR  |  |   TEST  | |    DIGITAL   |_|
        | SUBSYSTEM |  |AND CONTROL|  | SUPPORT | |COMMUNICATIONS|
         -----------   | SUBSYSTEM |  |SUBSYSTEM| |   SUBSYSTEM  |
                        -----------    ---------   --------------
 
 
      Post-NSP DSCC
      -------------
 
         -----------   ------------------   ---------------------
        |TRANSMITTER|_|      UPLINK      |_|       COMMAND       |_
        | SUBSYSTEM | |     SUBSYSTEM    | |       SUBSYSTEM     | |
         -----------   ------------------   ---------------------  |
               |                                                   |
         -----------   ------------------   ---------------------  |
        | MICROWAVE |_|     DOWNLINK     |_|      TELEMETRY      |_|
        | SUBSYSTEM | |     SUBSYSTEM    | |      SUBSYSTEM      | |
         -----------   ------------------   ---------------------  |
               |                                                   |
         -----------    -----------    ---------   --------------  |
        |  ANTENNA  |  |  MONITOR  |  |   TEST  | |    DIGITAL   |_|
        | SUBSYSTEM |  |AND CONTROL|  | SUPPORT | |COMMUNICATIONS|
         -----------   | SUBSYSTEM |  |SUBSYSTEM| |   SUBSYSTEM  |
                        -----------    ---------   --------------
 
 
      DSCC Monitor and Control Subsystem
      ----------------------------------
        The DSCC Monitor and Control Subsystem (DMC) is part of the
        Monitor and Control System (MON) which also includes the
        ground communications Central Communications Terminal (CCT) and
        the Network Operations Control Center (NOCC) Monitor and Control
        Subsystem.  The DMC is the center of activity at a DSCC.  The
        DMC receives and archives most of the information from the
        NOCC needed by the various DSCC subsystems during their
        operation.  Control of most of the DSCC subsystems, as well
        as the handling and displaying of any responses to control
        directives and configuration and status information received
        from each of the subsystems, is done through the DMC.  The
        effect of this is to centralize the control, display, and
        short-term archiving functions necessary to operate a DSCC.
        Communication among the various subsystems is done using a
        Local Area Network (LAN) hooked up to each subsystem via a
        network interface unit (NIU).
 
        DMC operations are divided into two separate areas: the
        Complex Monitor and Control (CMC) and the Network Monitor and
        Control (NMC).  The primary purpose of the CMC processor for
        Radio Science support is to receive and store all predict
        sets transmitted from NOCC -- such as antenna pointing,
        tracking, receiver, and uplink predict sets -- and then, at a
        later time, to distribute them to the appropriate subsystems
        via the LAN.  Those predict sets can be stored in the CMC for
        a maximum of three days under normal conditions.  The CMC also
        receives, processes, and displays event/alarm messages, and
        maintains an operator log.  Assignment and configuration of
        the NMCs is done through the CMC; to a limited degree the CMC
        can perform some of the functions performed by the NMC.  There
        are two CMCs (one on-line and one backup) and three NMCs at
        each DSCC.   The backup CMC can function as an additional NMC
        if necessary.
 
        The NMC processor provides the operator interface for monitor
        and control of a link -- a group of equipment required to
        support a spacecraft pass.  For Radio Science, a link might
        include one or more Radio Science Receivers (RSRs), the DSCC
        Tracking Subsystem (DTK), and special equipment required for
        Ka-band uplink and/or downlink (i.e., aberration correction,
        monopulse receiver, and advanced media calibration system).
        The NMC also maintains an operator log which includes all
        operator directives and subsystem responses.  One important
        Radio Science-specific function that the NMC performs is
        receipt and transmission of the system temperature and signal
        level data from the PPM, for display at the NMC console and
        for inclusion in Monitor blocks.  These blocks are recorded
        on magnetic tape as well as appearing in the NOCC displays.
        The NMC is required to operate without interruption for the
        duration of the Radio Science data acquisition period.
 
        The Area Routing Assembly (ARA), which is part of the Digital
        Communications Subsystem, controls all data communication
        between the stations and JPL.  The ARA receives all required
        data and status messages from the NMC/CMC, and can record them
        to tape as well as transmit them to JPL via data lines.  The
        ARA also receives predicts and other data from JPL, and passes
        them on to the CMC.
 
 
      DSCC Antenna Mechanical Subsystem
      ---------------------------------
        Multimission Radio Science activities require support from
        the 70-m, 34-m HEF, and 34-m BWG antenna subnets.  The
        antennas at each DSCC function as large-aperture collectors
        which, by double reflection, cause the incoming radio
        frequency (RF) energy to enter the feed horns.  The large
        collecting surface of the antenna focuses the incoming energy
        onto a subreflector, which is adjustable in both axial and
        angular position.  These adjustments are made to correct for
        gravitational deformation of the antenna as it moves between
        zenith and the horizon; the deformation can be as large as
        7 cm.  The subreflector adjustments optimize the channeling
        of energy from the primary reflector to the subreflector,
        and then to the feed horns.  The 70-m and 34-m HEF antennas
        have 'shaped' primary and secondary reflectors, with forms
        that are modified paraboloids.  This customization allows
        more uniform illumination of one reflector by another.  The
        BWG reflector shape is ellipsoidal.
 
        On the 70-m antennas, the subreflector directs
        received energy from the antenna onto a dichroic plate, a
        device which reflects S-band energy to the S-band feed horn
        and passes X-band energy through to the X-band feed horn.  In
        the 34-m HEF, there is one 'common aperture feed,' which
        accepts both frequencies without requiring a dichroic plate.
        In the 34-m BWG, a series of small mirrors (approximately 2.5
        meters in diameter) directs microwave energy from the
        subreflector region to a collection area at the base of
        the antenna -- typically in a pedestal room.  A retractable
        dichroic reflector separates the S and X bands on some BWG
        antennas, or the X and Ka bands on others.  RF energy to be
        transmitted into space by the horns is focused by the
        reflectors into narrow cylindrical beams, pointed with high
        precision (either to the dichroic plate or directly to the
        subreflector) by a series of drive motors and gear trains
        that can rotate the movable components and their support
        structures.
 
        The different antennas can be pointed by several means.  Two
        pointing modes commonly used during tracking passes are
        CONSCAN and 'blind pointing.' With CONSCAN enabled and a
        closed-loop receiver locked to a spacecraft signal, the
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
        (OCIs) from the NMC to the Subreflector Controller (SRC)
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
        consist of time-tagged AZ-EL points at selected time intervals
        along with polynomial coefficients for interpolation between
        points.
 
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
        'planetary' mode -- a simpler mode which uses right ascension
        (RA) and declination (DEC) values.  These change very slowly
        with respect to the celestial frame.  Values are provided to
        the station in text form for manual entry.  The ACS
        quadratically interpolates among three RA and DEC points
        which are on one-day centers.
 
        A third pointing mode -- sidereal -- is available for
        tracking radio sources fixed with respect to the celestial
        frame.
 
        Also, at DSS 25, there is a special pointing mode to enable
        tracking at Ka-band frequency.  Reception of the extremely
        narrow beamwidth Ka-band signals required the development
        of a monopulse receiver to continuously monitor and correct
        antenna pointing to maintain lock on the signal peak.  And
        an aberration correction system had to be implemented such
        that the Ka-band uplink signal would be aimed at where the
        spacecraft would be when the signal arrived (simultaneously
        keeping the receiver pointed to where the downlink signal
        was when it left the spacecraft).  This is accomplished by
        mounting the Ka-band transmit feed on a movable X-Y platform
        that can be displaced by as much as 30 millidegrees from the
        received beam.  The monopulse tracking system (and Ka-band
        downlink) will be implemented at the other BWGs by the end
        of 2005.
 
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
        70-m Antennas: Each 70-m antenna has three feed cones installed
        in a structure at the center of the main reflector.  The feeds
        are positioned 120 degrees apart on a circle.  Selection of the
        feed is made by rotation of the subreflector.  A dichroic mirror
        assembly, half on the S-band cone and half on the X-band cone,
        permits simultaneous use of the S- and X-band frequencies.  The
        third cone is devoted to R&D and more specialized work.
 
        The Antenna Microwave Subsystem (AMS) accepts the received S-
        and X-band signals at the feed horn and transmits them through
        polarizer plates to an orthomode transducer.  The polarizer
        plates are adjusted so that the signals are directed to a pair
        of redundant amplifiers for each frequency, thus facilitating
        the simultaneous reception of signals in two orthogonal
        polarizations.  For S-band these are two Block IVA S-band
        Traveling Wave Masers (TWMs); for X-band the amplifiers are
        Block IIA TWMs.
 
        34-m HEF Antennas:  The 34-m HEF uses a single feed for both
        S- and X-band.  Simultaneous S- and X-band receive as well as
        X-band transmit is possible thanks to the presence of an S/X
        'combiner' which acts as a diplexer.  For S-band, RCP or LCP
        is user selected through a switch, so neither a polarizer nor
        an orthomode transducer is needed.  The X-band amplification
        options include two Block II TWMs or a High Electron Mobility
        Transistor (HEMT) Low Noise Amplifier (LNA), while the S-band
        amplification is provided by a Field Effect Transistor (FET)
        LNA.
 
        34-m BWG Antennas: These antennas use feeds and low-noise
        amplifiers (LNA) in the pedestal room, which can be switched
        in and out as needed.  Typically the following modes are
        available:
 
           1. downlink non-diplexed path (RCP or LCP) to LNA-1, with
              uplink in the opposite circular polarization;
           2. downlink non-diplexed path (RCP or LCP) to LNA-2, with
              uplink in the opposite circular polarization;
           3. downlink diplexed path (RCP or LCP) to LNA-1, with
              uplink in the same circular polarization;
           4. downlink diplexed path (RCP or LCP) to LNA-2, with
              uplink in the same circular polarization.
 
        For BWG antennas with dual-band capabilities (e.g., DSS 25)
        and dual LNAs, each of the above four modes can be used in a
        single-frequency or dual-frequency configuration.  Thus, for
        antennas with the most complete capabilities, there are sixteen
        possible ways to receive (2 polarizations, 2 waveguide path
        choices, 2 LNAs, and 2 bands).
 
 
      DSCC Receiver-Exciter Subsystem -- Pre-NSP
      ------------------------------------------
        The Receiver-Exciter Subsystem is composed of three groups of
        equipment: the closed-loop receiver group (which includes the
        exciter equipment), the open-loop receiver group, and the RF
        monitor group.  This subsystem is controlled by the Receiver-
        Exciter Controller (REC) which communicates directly with the
        DMC for predicts, and for OCI reception and status reporting.
 
        The exciter generates a sky-level signal which is provided to
        the Transmitter Subsystem for the spacecraft uplink signal.
        It is tunable under command of the DCO ( Digitally Controlled
        Oscillator), which receives uplink predicts from the Metric
        Data Assembly (MDA).
 
        The diplexer in the signal path between the transmitter and
        the feed horn for all antenna types (used for simultaneous
        transmission and reception) may be configured such that it is
        out of the received signal path (in listen-only or bypass
        mode) in order to improve the signal-to-noise ratio in the
        receiver system.
 
        Closed-Loop Receivers: The current closed-loop group consists
        of the Block V Receiver (BVR) and the Block V Exciter (BVE).
        The BVR allows for simultaneous use of two receiver channels,
        each configured independently of the other (thus allowing for
        the reception of two different frequencies/wavelengths/bands,
        or different polarizations of the same downlink band).  Based
        on predicts from the MDA, the BVE provide a sky-level uplink
        signal to either the low-power or the high-power transmitter.
 
        The closed-loop receivers provide the capability for the rapid
        acquisition of a spacecraft signal, and telemetry lock-up.  In
        order to accomplish signal acquisition within a short time, the
        receivers are predict driven to search for, acquire, and track
        the downlink automatically.  Rapid acquisition precludes manual
        tuning, though that remains as a backup capability.  The BVRs
        utilize FFT analyzers for rapid lock-up.  The downlink predicts
        are generated by the NSS and then transmitted to the CMC, which
        sends them to the Receiver-Exciter Subsystem where two sets can
        be stored.  The receiver starts acquisition at the beginning of
        a track (pass), or at an operator-specified time.  The BVRs may
        also be operated from the NMC without local operators attending
        them.  The receivers also send performance and status data,
        displays, and event messages to the NMC.
 
        With the BVRs, the simulation (SIM) synthesizer signal is used
        as the reference for the Doppler extractor.  The synthesizer is
        adjusted before the beginning of the pass to a frequency that
        is appropriate for the channel (i.e., within the band) of the
        incoming signal; and will generally remain constant during the
        pass.
 
        The closed-loop receiver AGC loop can be configured to one
        of three settings: narrow, medium, or wide.  It will be
        configured such that the expected amplitude changes are
        accommodated with minimum distortion.  The loop bandwidth
        (2BLo) will be configured such that the expected phase
        changes can be accommodated while maintaining the best
        possible loop SNR.
 
        Open-Loop Receivers: The open-loop Radio Science Receiver (RSR)
        is a dedicated receiver that gets a downconverted signal (about
        300 MHz), filters the signal to limit its bandwidth (to 265-375
        MHz, centered at 320 MHz), and then further downconverts (to a
        center frequency of 64 MHz) and digitizes the signal.  The RSR
        filters are specified by their bandwidths, desired resolution,
        and offset from the predicted sky frequency.
 
        The open-loop receivers operate in both a link-assigned and a
        stand-alone mode.  In the link-assigned mode, the NMC receives
        monitor data from the RSR for incorporation into the data set
        for tracking support, and provides a workstation from which the
        RSR can be operated.  RSRs that are not assigned to a link may
        be operated in a stand-alone mode without interference to any
        activities in progress at the complex.  Monitor data is not sent
        to the NMC by RSRs operating in the stand-alone mode.
 
 
      DSCC Receiver-Exciter Subsystem -- Post-NSP
      -------------------------------------------
        With the implementation of NSP, the receiver-exciter subsystem
        was split into the exciter component (called the UPL or Uplink
        Subsystem) and a separate receiver component (called the DTT or
        Downlink Tracking and Telemetry Subsystem).  The UPL comprises
        the Exciter, the Command Modulation, the Uplink Controller, and
        the Uplink Ranging assemblies.  The DTT comprises the Downlink
        Controller, the Receiver and Ranging Processor (RRP), and the
        Telemetry Processor (TLP) assemblies.
 
        The Post-NSP system is still based around the (Pre-NSP) Block V
        Exciter (BVE) and Block V Receiver (BVR) equipment.  The output
        from the BVEs is uplink carrier and range phase, and the output
        from the BVRs is downlink carrier and range phase.  The primary
        difference between the old and new systems is that these phase
        data (and not Doppler counts and ranging units) are what get
        delivered to the users.  Furthermore, the UPL and DTT deliver
        these (phase) data directly to the Project, without passing it
        through any intervening system (that is, there is no longer an
        MDA or an SRA in the data flow path).
 
        Closed-Loop Receivers: Per the above, the closed-loop receiver
        is still based on the Block V receivers; but with NSP, it now
        has the capability to simultaneously support as many downlink
        channels as can be assigned by the NMC (up to a maximum of the
        total number of RRPs available at a given complex).  The only
        other constraint is that any selected downlink band/bands must
        be supported by that antenna.  Except that the MDA and SRA are
        now eliminated, the Pre-NSP and Post-NSP closed-loop receiver
        subsystems are basically the same.
 
        Open-Loop Receivers: The open-loop Radio Science Receiver (RSR)
        was unchanged by NSP, and its description is the same as that
        provided above in the Pre-NSP open-loop receiver description.
 
 
      DSCC Transmitter Subsystem -- Pre-NSP
      -------------------------------------
        The Transmitter (TXR) Subsystem accepts a sky-level frequency
        exciter signal from the Receiver-Exciter Subsystem exciter.
        This signal is routed via the diplexer through the feed horn
        to the antenna, where it is then focused and beamed to the
        spacecraft.
 
        The Transmitter Subsystem power capabilities range from 18 kW
        to 400 kW, for S- and X-band uplink.  Power levels above 18 kW
        are available only at 70-m stations.  For Ka-band uplink (only
        at DSS 25), available powers range from 100 to 800 W.
 
 
      DSCC Transmitter Subsystem -- Post-NSP
      --------------------------------------
        The Transmitter (TXR) Subsystem accepts a sky-level frequency
        exciter signal from the Uplink (Exciter) Subsystem exciter.
        This signal is routed via the diplexer through the feed horn
        to the antenna, where it is then focused and beamed to the
        spacecraft.
 
        The Transmitter Subsystem power capabilities range from 18 kW
        to 400 kW, for S- and X-band uplink.  Power levels above 20 kW
        are available only at 70-m stations.  For Ka-band uplink (only
        at DSS 25), available powers range from 100 to 800 W.
 
 
      DSCC Tracking Subsystem -- Pre-NSP
      ----------------------------------
        The primary functions of the DSCC Tracking Subsystem (DTK) are
        to acquire and maintain communications with the spacecraft, and
        to generate and format radio metric data containing Doppler,
        range, and uplink frequencies (ramps).
 
        The DTK receives the carrier signals and ranging spectra from
        the Receiver-Exciter Subsystem.  The Doppler cycle counts are
        computed from BVR-provided carrier phase measurements, and are
        then formatted and transmitted to JPL in real time.  Ranging
        data are also formatted and transmitted to JPL in real time.
        Also contained in these blocks is the AGC information from the
        Receiver-Exciter Subsystem.  The Radio Metric Data Conditioning
        Team (RMDCT) at JPL receives all of the DTK-generated tracking
        data and produces an Archival Tracking Data File (ATDF) which
        contains all of the Doppler, ranging, and ramp data.
 
        In addition, the Tracking Subsystem receives from the CMC
        frequency predicts (used to compute frequency residuals and
        noise estimates), receiver tuning predicts (used to tune the
        closed-loop receivers), and uplink tuning predicts (used to
        tune the exciter).  From the NMC, it receives configuration
        and control directives, as well as configuration and status
        information on the transmitter, microwave, and frequency and
        timing subsystems.
 
        The Metric Data Assembly (MDA) controls all of the DTK
        functions supporting the uplink and downlink activities.  The
        MDA receives uplink predicts, and controls the uplink tuning
        by commanding the DCO.  The MDA also controls the Sequential
        Ranging Assembly (SRA).  It formats the Doppler and ranging
        measurements, and the uplink frequency history (ramps), and
        provides them to the GCF for transmission to NOCC and RMDCT.
 
        The Sequential Ranging Assembly (SRA) measures the round trip
        light time (RTLT) of a radio signal traveling from a ground
        tracking station to a spacecraft and back.  From the RTLT,
        phase, and Doppler data, the range to the spacecraft can be
        determined.  A coded signal is modulated on an uplink carrier
        and transmitted to the spacecraft, where it is detected and
        transponded back to the ground station.  As a result, the
        signal received at the tracking station is delayed by its
        round trip through space, and shifted in frequency by the
        Doppler effect due to the relative motion between the ground
        station on Earth and the spacecraft.
 
 
      DSCC Tracking Subsystem -- Post-NSP
      -----------------------------------
        With NSP, all the Tracking Subsystem functions are incorporated
        within the Uplink Subsystem (UPL) and the Downlink Tracking and
        Telemetry Subsystem (DTT) -- the DTK, MDA, and SRA have now all
        been eliminated.
 
 
      DSCC Frequency and Timing Subsystem
      -----------------------------------
        The Frequency and Timing Subsystem (FTS) provides all of the
        frequency and timing references required by the other DSCC
        subsystems.  It contains four frequency standards, of which
        one is prime and the other three are backups.  Selection of
        the prime standard is done via the CMC.  Of these four
        standards, two are hydrogen masers followed by clean-up loops
        (CUL) and two are cesium standards.  These four standards all
        feed the Coherent Reference Generator (CRG), which provides
        the frequency references used by the rest of the complex.  It
        also provides the frequency reference to the Master Clock
        Assembly (MCA), which in turn provides time to the Time
        Insertion and Distribution Assembly (TID), which provides UTC
        and SIM-time to the complex.
 
        JPL's ability to monitor the FTS at each DSCC is limited to
        the station-calculated Doppler pseudo-residuals, the Doppler
        noise, the RSR, the SSI, and to a system that uses the Global
        Positioning System (GPS).  GPS receivers at each DSCC receive
        a one-pulse-per-second signal from the station's (hydrogen-
        maser-referenced) FTS and a pulse from a GPS satellite at
        scheduled times.  After compensating for the satellite signal
        delay, the timing offset is reported to JPL, where a database
        is kept.  The clock offsets stored in the JPL database are
        given in microseconds; each entry is a mean reading of the
        measurements from several GPS satellites, and a time tag
        associated with the mean reading.  The clock offsets that are
        provided include those of SPC 10 relative to UTC (NIST), SPC
        40 relative to SPC 10, etc.
 
 
    Optics - DSN
    ============
      Performance of the DSN ground stations depends primarily on size
      of the antenna and capabilities of the electronics.  These are
      summarized in the following set of tables.  Note that the 64-m
      antennas were upgraded to 70-m between 1986 and 1989.
      Beamwidth is half-power full angular width.  Polarization is
      circular; L denotes left circular polarization (LCP), and R
      denotes right circular polarization (RCP).
 
 
                           DSS S-Band Characteristics
 
                                         70-m     34-m     34-m
           Transmit                                BWG      HEF
           --------                     -----    -----    -----
           Frequency (MHz)              2110-    2025-     N/A
                                         2120     2120
           Wavelength (m)               0.142    0.142     N/A
           Ant Gain (dBi)                62.7     56.1     N/A
           Beamwidth (deg)              0.119      N/A     N/A
           Polarization                L or R   L or R     N/A
           Tx Power (kW)               20-100       20     N/A
 
 
           Receive
           -------
           Frequency (MHz)              2270-    2270-    2200-
                                         2300     2300     2300
           Wavelength (m)               0.131    0.131    0.131
           Ant Gain (dBi)                63.3     56.7     56.0
           Beamwidth (deg)              0.108      N/A     0.24
           Polarization                 L & R   L or R   L or R
           System Temp (K)                 20       31       38
 
 
                           DSS X-Band Characteristics
 
                                         70-m     34-m     34-m
           Transmit                                BWG      HEF
           --------                     -----    -----    -----
           Frequency (MHz)               8495    7145-    7145-
                                                  7190     7190
           Wavelength (m)               0.035    0.042    0.042
           Ant Gain (dBi)                74.2     66.9       67
           Beamwidth (deg)                         N/A    0.074
           Polarization                L or R   L or R   L or R
           Tx Power (kW)                   20       20       20
 
 
           Receive
           -------
           Frequency (MHz)              8400-    8400-    8400-
                                         8500     8500     8500
           Wavelength (m)               0.036    0.036    0.036
           Ant Gain (dBi)                74.2     68.1     68.3
           Beamwidth (deg)              0.031      N/A    0.063
           Polarization                 L & R    L & R    L & R
           System Temp (K)                 20       30       20
 
 
                           DSS Ka-Band Characteristics
 
                                         70-m     34-m     34-m
           Transmit                                BWG      HEF
           --------                     -----    -----    -----
           Frequency (GHz)               N/A     34.2-     N/A
                                                  34.7
           Wavelength (m)                N/A       tbd*    N/A
           Ant Gain (dBi)                N/A       tbd*    N/A
           Beamwidth (deg)               N/A       tbd*    N/A
           Polarization                  N/A         L     N/A
           Tx Power (W)                  N/A       800     N/A
 
 
           Receive
           -------
           Frequency (GHz)               N/A     31.8-     N/A
                                                  32.3
           Wavelength (m)                N/A     0.009     N/A
           Ant Gain (dBi)                N/A      77.9     N/A
           Beamwidth (deg)               N/A     0.017     N/A
           Polarization                  N/A         R     N/A
           System Temp (K)               N/A       tbd*    N/A
 
 
           NB: The X-band 70-m transmitting parameters are given
               at 8495 MHz, the frequency used by the Goldstone
               planetary radar system.  For telecommunications, the
               transmitting frequency would be in the range 7145-7190
               MHz, the power would typically be 20 kW, and the gain
               would be about 72.6 dB (70-m antenna).  When ground
               transmitters are used in spacecraft radio science
               experiments, the details of transmitter and antenna
               performance rarely impact the results.
 
 
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
        optical feedback system.  At DSS 25 (only) there is also an
        'aberration correction' mode that is needed whenever doing
        Ka-band uplink coherent downlink, because the transmit and
        receive beams must be pointed differently at the same time.
        In addition, it is possible on most antennas to freeze the
        z-axis motion of the subreflector to minimize phase changes
        in the received signal.
 
 
      DSCC Downlink Tracking and Telemetry Subsystem
      ----------------------------------------------
        The diplexer in the signal path between the transmitter and
        the feed horns on all antennas may be configured so that it
        is out of the received signal path in order to improve the
        signal-to-noise ratio in the receiver system.  This is known
        as the 'listen-only' or 'bypass' mode.
 
 
      Closed-Loop vs. Open-Loop Reception
      -----------------------------------
        Radio Science data can be collected in two modes: closed-
        loop, in which a phase-locked loop receiver tracks the
        spacecraft signal, or open-loop, in which a receiver samples
        and records a band within which the desired signal presumably
        resides.  Closed-loop data are collected using Closed-Loop
        Receivers, and open-loop data are collected using Open-Loop
        Receivers in conjunction with the Full Spectrum Processing
        Subsystem (FSP).  See the Subsystems section for further
        information.
 
 
      Closed-Loop Receiver AGC Loop
      -----------------------------
        The closed-loop receiver AGC loop can be configured to one of
        three settings: narrow, medium, or wide.  In general, it is
        configured so that expected signal amplitude changes are
        accommodated with minimum distortion.  The loop bandwidth is
        typically configured so that expected phase changes can be
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
        as expressed in the table below:
 
            Uplink    Downlink    Turn-Around
             Band       Band         Ratio
            ---------------------------------
              X          X          880/749
              X          S          240/749
              X          Ka        3344/749
              Ka         Ka          14/15
 
 
        In the non-coherent mode, the downlink carrier frequency is
        derived from the spacecraft's on-board, crystal-controlled
        oscillator.  Either closed-loop or open-loop receivers (or
        both) can be used with either spacecraft frequency reference
        mode.  Closed-loop reception in the two-way mode is usually
        preferred for routine tracking/navigation.  Occasionally the
        spacecraft operates coherently such that one ground station
        does the transmitting, and a second/different ground station
        receives the 'downlink' signal -- this is referred to as the
        'three-way' mode.
 
 
      Media Calibration System
      ------------------------
        The Earth's atmosphere contributes phase and amplitude noise
        to the spacecraft radio signal received at a ground station.
        Each DSCC has a GPS receiver subsystem to calibrate for both
        the ionosphere and troposphere (both wet and dry components),
        along the zenith direction.  This subsystem also measures the
        temperature, pressure, humidity, wind speed and direction, and
        Faraday rotation.
 
        Radio Science experiments that utilize Ka-band downlink, where
        excellent end-to-end frequency and phase stability are required,
        necessitated the development of a new system to calibrate the
        effects of the atmosphere on the phase of the microwave signal.
        The purpose of this new media calibration system is to provide
        a line-of-sight measurement of water vapor delay (responsible
        for the majority of the atmosphere-induced phase fluctuations
        at microwave frequencies).  It also provides estimates of total
        zenith delay and delay fluctuation.  This is accomplished via:
        (1) an advanced water vapor radiometer to sense the number of
        water vapor molecules along the line-of-sight; (2) a microwave
        temperature profiler to sense vertical temperature distribution;
        (3) a surface meteorology package to measure the temperature,
        pressure, and humidity; and (4) a GPS receiver to provide the
        total zenith delay estimates.  This 'advanced' system is only
        implemented at DSS 25 at this time.
 
 
    Location - DSN
    ==============
      Accurate spacecraft navigation using radio metric data requires
      knowledge of the locations of the DSN tracking stations.  The
      coordinate system in which the locations of the tracking stations
      are expressed should be consistent with the reference frame
      definitions used to provide Earth orientation calibrations.
 
      The International Earth Rotation Service (IERS) has established
      a terrestrial reference frame for use with Earth orientation
      measurements. The IERS issues a new realization of the terrestrial
      reference frame each year.  The definition of the coordinate
      system has been changing slowly as the data have been improved,
      and as ideas about how to best define the coordinate system have
      developed.  The overall changes from year to year have been at the
      few-cm level.  The 1993 version of the IERS Terrestrial Reference
      Frame (ITRF1993) [BOUCHERETAL1994] is most used for DSN station
      locations.
 
      The DSN station locations have been determined by use of VLBI
      measurements, and by conventional and GPS surveying.  Tables of
      station locations are available in either Cartesian or geodetic
      coordinates.  The geodetic coordinates are referred to a geoid
      with an equatorial radius of 6378136.3 m, and a flattening factor
      f=298.257, as described in IERS Technical Note 13.
 
      The DSN Station Locations in ITRF1993 Cartesian reference frame
      at epoch 1993.0 (assuming subreflector-fixed configuration) are
      as follows:
 
      Antenna     x(m)          y(m)          z(m)
      ------------------------------------------------
      DSS 12  -2350443.812  -4651980.837  +3665630.988
      DSS 13  -2351112.491  -4655530.714  +3660912.787
      DSS 14  -2353621.251  -4641341.542  +3677052.370
      DSS 15  -2353538.790  -4641649.507  +3676670.043
      DSS 16  -2354763.158  -4646787.462  +3669387.069
      DSS 17  -2354730.357  -4646751.776  +3669440.659
      DSS 23  -2354757.567  -4646934.675  +3669207.824
      DSS 24  -2354906.528  -4646840.114  +3669242.295
      DSS 25  -2355021.795  -4646953.325  +3669040.628
      DSS 26  -2354890.967  -4647166.925  +3668872.212
      DSS 27  -2349915.260  -4656756.484  +3660096.529
      DSS 28  -2350101.849  -4656673.447  +3660103.577
      DSS 33  -4461083.514  +2682281.745  -3674570.392
      DSS 34  -4461146.720  +2682439.296  -3674393.517
      DSS 42  -4460981.016  +2682413.525  -3674582.072
      DSS 43  -4460894.585  +2682361.554  -3674748.580
      DSS 45  -4460935.250  +2682765.710  -3674381.402
      DSS 46  -4460828.619  +2682129.556  -3674975.508
      Parkes  -4554231.843  +2816758.983  -3454036.065
      DSS 53  +4849330.129  -0360338.092  +4114758.766
      DSS 54  +4849434.496  -0360724.062  +4114618.570
      DSS 55  +4849525.318  -0360606.299  +4114494.905
      DSS 61  +4849245.211  -0360278.166  +4114884.445
      DSS 63  +4849092.647  -0360180.569  +4115109.113
      DSS 65  +4849336.730  -0360488.859  +4114748.775
      DSS 66  +4849148.543  -0360474.842  +4114995.021
 
 
      The DSN Station Locations in ITRF1993 Geodetic reference frame
      at epoch 1993.0 (assuming subreflector-fixed configuration) are
      as follows:
 
               latitude            longitude            height
      Antenna  deg min sec         deg  min sec           (m)
      ----------------------------------------------------------
      DSS 12    35  17  59.77577    243  11  40.24697     962.87517
      DSS 13    35  14  49.79342    243  12  19.95493    1071.17855
      DSS 14    35  25  33.24518    243   6  37.66967    1002.11430
      DSS 15    35  25  18.67390    243   6  46.10495     973.94523
      DSS 16    35  20  29.54391    243   7  34.86823     944.71108
      DSS 17    35  20  31.83778    243   7  35.38803     937.65000
      DSS 23    35  20  22.38335    243   7  37.70043     946.08556
      DSS 24    35  20  23.61492    243   7  30.74701     952.14515
      DSS 25    35  20  15.40494    243   7  28.70236     960.38138
      DSS 26    35  20   8.48213    243   7  37.14557     970.15911
      DSS 27    35  14  17.78052    243  13  24.06569    1053.20312
      DSS 28    35  14  17.78136    243  13  15.99911    1065.38171
      DSS 33   -35  24   1.76138    148  58  59.12204     684.83864
      DSS 34   -35  23  54.53984    148  58  55.06236     692.71119
      DSS 42   -35  24   2.44494    148  58  52.55396     675.35557
      DSS 43   -35  24   8.74388    148  58  52.55394     689.60780
      DSS 45   -35  23  54.46400    148  58  39.65992     675.08630
      DSS 46   -35  24  18.05462    148  58  59.08571     677.55141
      Parkes   -32  59  54.25297    148  15  48.64683     415.52885
      DSS 53    40  25  38.48036    355  45   1.24307     827.50081
      DSS 54    40  25  32.23152    355  44  45.24459     837.60097
      DSS 55    40  25  27.45965    355  44  50.51161     819.70966
      DSS 61    40  25  43.45508    355  45   3.51113     841.15897
      DSS 63    40  25  52.34908    355  45   7.16030     865.54412
      DSS 65    40  25  37.86055    355  44  54.88622     834.53926
      DSS 66    40  25  47.90367    355  44  54.88739     850.58213
 
 
    Measurement Parameters - DSN
    ============================
 
      Open-Loop System
      ----------------
        Output from the Open-Loop Receivers (OLRs), as sampled and
        recorded by the Radio Science Receiver (RSR), is a stream of
        1-, 2-, 4-, 8-, or 16-bit I (In-Phase) and Q (Quadrature-Phase)
        samples.  The spacecraft transmits an RF signal to an antenna,
        where the signal gets downconverted to IF.  The RSR selects an
        IF signal for a particular frequency band and passes it through
        a digitizer (where it is attenuated and then mixed with timing
        information).  The signal is then decimated, filtered (to I&Q
        samples), and then multiplied by the signal from a numerically
        controlled oscillator.  Finally, the RSR reduces the bandwidth
        and sample rate of the samples, and truncates the results (thus
        creating an offset of -0.5 in the output data).  The samples of
        data are packed into SFDU blocks (nominally containing a single
        second's worth of data), and a header is attached to provide
        the following associated data for the record:
 
        -  time tag for the first sample in the data block
        -  data source identification (DSS, RSR, and sub-channel), and
           frequency band
        -  data sample resolution (bits per sample) and rate (samples
           per second)
        -  filter gain, ADC RMS amplitude, and attenuation
        -  frequency and phase polynomial coefficients
 
 
      Closed-Loop System
      ------------------
        Prior to mid 2003, closed-loop data were recorded in Archival
        Tracking Data Files (ATDFs), as well as certain higher-level
        products such as Orbit Data Files (ODFs).  After May 2003 these
        data were provided in Tracking and Navigation Files (TNFs).
        During NSP implementation (January through May 2003), there was
        a transition from ATDFs to TNFs as the ground stations switched
        to the new DSN tracking system, one at a time.  The ATDFs and
        the ODFs contained fixed-length, fixed-format, bit-oriented,
        binary integer data records; the TNFs, on the other hand, are
        comprised of SFDUs that have variable-length, variable-format
        records with mixed typing (i.e., can contain ASCII, integer,
        and floating-point items in a single record).  These files all
        contain entries that include measurements of Doppler, range,
        and signal strength, along with status and uplink frequency
        information.
 
 
    ACRONYMS AND ABBREVIATIONS - DSN
    ================================
      ACS      Antenna Control System
      ADC      Analog-to-Digital Converter
      AGC      Automatic Gain Control
      AMMOS    Advanced Multi-Mission Operations System
      AMS      Antenna Microwave System
      APA      Antenna Pointing Assembly
      ARA      Area Routing Assembly
      ATDF     Archival Tracking Data File
      AUX      Auxiliary
      AZ       Azimuth
      BPF      Band Pass Filter
      bps      bits per second
      BVE      Block V Exciter
      BVR      Block V Exciter
      BWG      Beam WaveGuide (antenna)
      CAS      Cassini
      CCT      Central Communications Terminal
      CDU      Command Detector Unit
      CMC      Complex Monitor and Control
      CONSCAN  Conical Scanning (antenna pointing mode)
      CRG      Coherent Reference Generator
      CSO      Compensated Sapphire Oscillator
      CUL      Clean-up Loop
      DANA     a type of frequency synthesizer
      dB       deciBel
      dBi      dB relative to isotropic
      dBm      dB relative to one milliwatt
      DCO      Digitally Controlled Oscillator
      DEC      Declination
      deg      degree
      DMC      DSCC Monitor and Control Subsystem
      DOD      Differential One-Way Doppler
      DOR      Differential One-way Ranging
      DSCC     Deep Space Communications Complex
      DSN      Deep Space Network
      DSS      Deep Space Station
      DST      Deep Space Transponder
      DTK      DSCC Tracking Subsystem
      DTT      DSCC Downlink Tracking and Telemetry Subsystem
      E        east
      EIRP     Effective Isotropic Radiated Power
      EL       Elevation
      FET      Field Effect Transistor
      FFT      Fast Fourier Transform
      FSP      Full Spectrum Processor Subsystem
      FTS      Frequency and Timing Subsystem
      GCF      Ground Communications Facility
      GHz      Gigahertz
      GPS      Global Positioning System
      GSFC     Goddard Space Flight Center
      HA       Hour Angle
      HEF      High-Efficiency (as in 34-m HEF antennas)
      HEMT     High Electron Mobility Transistor (amplifier)
      HGA      High-Gain Antenna
      HSB      High-Speed BWG
      I        In-phase
      IERS     International Earth Rotation Service
      IF       Intermediate Frequency
      IVC      IF Selection Switch
      JPL      Jet Propulsion Laboratory
      K        Kelvin
      Ka-Band  approximately 32 GHz
      KAT      Ka-Band Translator
      kbps     kilobits per second
      KEX      Ka-Band Exciter
      kHz      kilohertz
      km       kilometer
      kW       kilowatt
      LAN      Local Area Network
      LCP      Left-Circularly Polarized
      LGA      Low-Gain Antenna
      LMC      Link Monitor and Control
      LNA      Low-Noise Amplifier
      LO       Local Oscillator
      m        meters
      MCA      Master Clock Assembly
      MDA      Metric Data Assembly
      MHz      Megahertz
      MON      Monitor and Control System
      MSA      Mission Support Area
      N        north
      NAR      Noise Adding Radiometer
      NBOC     Narrow-Band Occultation Converter
      NIST     SPC 10 time relative to UTC
      NIU      Network Interface Unit
      NMC      Network Monitor and Control
      NOCC     Network Operations and Control System
      NRV      NOCC Radio Science/VLBI Display Subsystem
      NSP      Network Simplification Project
      NSS      NOCC Support Subsystem
      OCI      Operator Control Input
      ODF      Orbit Data File
      ODR      Original Data Record
      OLR      Open-Loop Receiver
      OSC      Oscillator
      PDS      Planetary Data System
      PPM      Precision Power Monitor
      Q        Quadrature
      RA       Right Ascension
      REC      Receiver-Exciter Controller
      RCP      Right-Circularly Polarized
      RF       Radio Frequency
      RFE      (Probe) Receiver Front End
      RFIS     Radio Frequency Instrument Subsystem
      RFS      Radio Frequency Subsystem
      RMDCT    Radio Metric Data Conditioning Team
      RMS      Root Mean Square
      RNS      Reliable Network Server
      RRP      Receiver and Ranging Processor
      RSR      Radio Science Receiver
      RSS      Radio Science Subsystem
      RSSG     Radio Science Systems Group
      RTLT     Round-Trip Light Time
      S-band   approximately 2100-2300 MHz
      SBT      S-Band Transmitter
      sec      second
      SEC      Systematic Error Correction
      SFDU     Standard Format Data Unit
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
      tbd      to be determined
      TDDS     Tracking Data Delivery Subsystem
      TID      Time Insertion and Distribution Assembly
      TLM      Telemetry
      TLP      Telemetry Processor
      TSF      Tracking Synthesizer Frequency
      TWM      Traveling Wave Maser
      TWNC     Two-Way Non-Coherent
      TWTA     Traveling Wave Tube Amplifier
      TXR      Transmitter (subsystem)
      UNK      unknown
      UPL      DSCC Uplink Subsystem
      USO      UltraStable Oscillator
      UTC      Universal Coordinated Time
      VCO      Voltage-Controlled Oscillator
      VF       Video Frequency
      VLBI     Very Long Baseline Interferometry
      X-band   approximately 7800-8500 MHz

        