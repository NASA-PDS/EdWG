
 
 
    Instrument Overview
    ===================
      The Voyager 2 Radio Science investigations at Neptune utilized
      instrumentation with elements both on the spacecraft and at
      the DSN.  Much of this was shared equipment, being used for
      routine telecommunications as well as for Radio Science.
      The performance and calibration of both the spacecraft and
      tracking stations directly affected the radio science data
      accuracy, and they played a major role in determining the
      quality of the results.  The spacecraft part of the radio
      science instrument is described immediately below; that is
      followed by a description of the DSN (ground) part of the
      instrument.
 
 
    Instrument Specifications - Spacecraft
    ======================================
      The Voyager 2 spacecraft telecommunications subsystem served
      as part of a radio science subsystem for investigations of
      Neptune.  Many details of the subsystem are unknown; its
      'build date' is taken to be 1977-08-20, which was the launch
      date for Voyager 2.
 
      Instrument Id                  : RSS
      Instrument Host Id             : VG2
      Pi Pds User Id                 : UNK
      Instrument Name                : RADIO SCIENCE SUBSYSTEM
      Instrument Type                : RADIO SCIENCE
      Build Date                     : 1977-08-20
      Instrument Mass                : UNK
      Instrument Length              : UNK
      Instrument Width               : UNK
      Instrument Height              : UNK
      Instrument Manufacturer Name   : UNK
 
 
    Instrument Overview - Spacecraft
    ================================
      The spacecraft radio system was constructed around a redundant
      pair of transponders.  Each transponder was equipped with an
      S-band receiver (2115 MHz nominal frequency) and transmitters
      at both S-band (2295 MHz nominal) and X-band (8415 MHz nominal).
      Compared with S-band, X-band is less sensitive to plasma effects
      by a factor of about 10; use of both frequencies coherently on
      the 'downlink' allowed estimation of plasma content along the
      radio path.  Use of X-band also significantly improved the
      quality of radio tracking data for gravity investigations.
 
      The transponder generated downlink signals in either 'coherent'
      or 'non-coherent' modes, also known as 'two-way' and 'one-way,'
      respectively.  When operating in the coherent mode, the
      transmitted carrier frequency was derived coherently from the
      received uplink carrier frequency with a 'turn-around ratio' of
      240/221 at S-band and (11/3)*240/221 at X-band.
 
      In non-coherent mode the transmitted frequency was controlled
      by an on-board oscillator; the X- and S-band remained coherent
      in the ratio 11/3.  A single Ultra-Stable Oscillator (USO) was
      used during radio occultations; it provided stabilities
      several orders of magnitude better than the conventional
      crystal oscillators, which were part of each transponder.
 
      Stability of the Voyager 2 USO was specified in terms of its
      Allan Deviation -- the fractional frequency deviation from
      linear drift [ALLAN1966].  Over 10 minute periods, the Allan
      Deviation ranged from 10^-12 to 4 10^-12 for integrations of
      1-10 sec.  Long-term fractional drift of the oscillator was
      about 5 10^-11 per day.  Although the oscillator was hardened,
      there were discontinuities in the drift when the spacecraft
      passed through the radiation belts of the outer planets.  The
      equivalent microwave frequency of the USO at Voyager 2
      Jupiter occultation ingress was:
 
                     2,296,481,070.940 Hz (S-band)
                     8,420,430,593.447 Hz (X-band)
 
      Traveling wave tube or solid state amplifiers boosted the
      transponder output.  Output powers of 9 and 26  watts could
      be selected at S-band; the choices at X-band were 12 and 22
      watts.
 
      The signals were radiated via a 3.66 m diameter parabolic high
      gain antenna (HGA).  The HGA transmit boresight gain of
      the HGA was 36 dB at S-band and 47 dB at X-band.  The half-power
      half-width of the antenna beam was 0.32 degrees at X-band and
      1.1 degrees at S-band.  Transmit polarization was right-hand
      circular at S-band and either right- or left-hand circular at
      X-band.  A Low-Gain Antenna (LGA) was mounted on the feed
      structure of the HGA and radiated approximately uniformly over
      the hemisphere into which the HGA pointed.  It was used during
      maneuvers, spacecraft anomalies, and at other times when the
      HGA was not appropriate.
 
      For receiving, the S-band HGA gain was 35 dB at 2115 MHz and the
      polarization was right-hand circular.  The receiving system
      noise temperature was approximately 2000K, the carrier tracking
      loop bandwidth was 18 Hz, and the ranging channel noise
      bandwidth was 1.5 MHz.
 
      More information can be found in [ESHLEMANETAL1977].
 
 
    Science Objectives
    ==================
      Science objectives fell into two broad areas of investigation --
      those that could be met using high-precision radiometric data
      (sometimes known as 'tracking' data) and those that could be met
      from studying characteristics of the radio signal after its
      interaction with an atmosphere, plasma, ring particles, or other
      intervening medium.  The tracking data were fundamental to
      inferring the gravitational forces on the spacecraft and
      relativistic effects along the radio path; both the measured
      time delay during a two-way transmission and the Doppler shift
      were used.  Investigators seeking knowledge of atmospheric
      structure, spatial and size distributions of ring particles,
      and velocity of the solar wind measured amplitude, frequency
      (and phase), and polarization of the radio signals which were
      captured by Earth receiving systems.  There are, of course,
      investigations which use both types of data.
 
 
      Gravity Measurements
      --------------------
        The frequency of the downlink carrier signal was precisely
        measured to determine the magnitude of the Doppler shift
        caused by acceleration of the spacecraft as it passed near
        either a single body or a system of bodies.  Since the
        magnitude of the Doppler shift is related to the gravitational
        field strength, the mass of the body (or bodies) can be
        determined.  If the radius of the body is known (as from
        calibrated images), the density can be calculated.
 
        Doppler and range tracking measurements yield accurate
        spacecraft trajectory solutions.  Simultaneously with
        reconstruction of the spacecraft orbit, observation equations
        for the central mass, low order coefficients for the field,
        and a small number of ancillary parameters can be solved.
        Measurements of the gravity field provide significant
        constraints on inferences about the interior structure of
        target bodies.
 
        The Pioneer 10 and 11 spacecraft came closer to Jupiter than
        Voyager, so there was no net improvement in the Jupiter mass
        estimate from Voyager.  But Voyager probed the Galilean
        satellites at closer range, and better mass estimates were
        obtained.  The Voyager encounters with Saturn, in conjunction
        with the close flyby of Pioneer 11, yielded a mass estimate
        comparable to that of Jupiter along with several low-order
        zonal harmonic coefficients.  Voyager 2 was targeted for a
        close encounter with Miranda, an inner satellite of Uranus;
        that, combined with long tracking arcs through the Uranian
        system, yielded the first good estimates of masses for the
        five largest satellites and an improved mass estimate for
        Uranus itself.  The Voyager 2 very close near-polar flyby
        with Neptune yielded estimates for the zonal harmonic
        coefficients J2 and J4 in addition to estimates for the mass
        of both Neptune and Triton.
 
 
      Atmospheric and Ionospheric Radio Occultation Measurements
      ----------------------------------------------------------
        Atmospheric measurements by the method of radio occultation
        contribute to an improved understanding of structure,
        circulation, dynamics, and transport in atmospheres of remote
        planetary bodies.  These results are based on detailed
        analysis of the radio signal received from the spacecraft as
        it enters and exits occultation by the planet.  Three phases
        of an atmospheric investigation may be defined.  The first is
        to obtain vertical profiles of atmospheric structure
        (temperature and pressure in the neutral atmosphere and
        electron density in the ionosphere) with emphasis on large-
        scale phenomena.  During this stage, it is necessary to know
        the mean molecular weight of the atmosphere; for Voyager
        the hydrogen-helium mixing ratio could be determined for each
        planet using the radio data in conjunction with Voyager IRIS
        data.  Second is to investigate absorption at various levels
        in the atmosphere -- such as by methane.  Third is to
        study details of the structure, such as result from
        propagation of buoyancy waves within a neutral atmosphere or
        from alignment of charged particles along magnetic field lines
        in an ionosphere.
 
        Retrieval of atmospheric profiles requires coherent
        samples of the radio signal that has propagated through
        the atmosphere, plus accurate knowledge of the antenna
        pointing and the spacecraft trajectory.  The spatial and
        temporal coverage in radio occultation experiments are
        determined by the observing geometry, including the spacecraft
        trajectory.  For deep atmospheres, changes in antenna pointing
        may be required to compensate for refractive bending by the
        atmosphere.  At Jupiter and Saturn both diametric and grazing
        occultations were obtained using the two Voyager spacecraft;
        measurements were obtained at both equatorial and polar
        latitudes.  Voyager 1 also obtained profiles for Titan.
        Voyager 2 continued to Uranus and Neptune, and also obtained
        occultation profiles at Triton.
 
 
      Radio Measurements on Planetary Rings
      -------------------------------------
        Radio occultation measurements of planetary rings are carried
        out using procedures similar to those employed for atmospheric
        occultations.  Although absorption by ring particles must be
        considered, the dominant effect on strength of the directly
        propagating signal is believed to be conservative scattering.
        Profiles of received signal strength can be inverted to yield
        the radial distribution of ring material.  Doppler spreading
        of the signal scattered in the near-forward direction can be
        used to infer the particle size distribution, especially when
        measurements at the two Voyager radio wavelengths are
        combined.
 
        Ring occultations were planned and observed at Saturn and
        Uranus.  Measurements were carried out at Neptune, but no
        rings or arcs were detected using the radio system.  A post-
        encounter search for a radio ring occultation at Jupiter was
        unsuccessful.
 
        Voyager 2 also carried out an oblique forward scattering
        experiment during its Saturn encounter.  The spacecraft high-
        gain antenna was deflected from the Earth direction so that
        it illuminated the ring system; but no scattered signal was
        detected.
 
 
      Solar Conjunction Experiments
      -----------------------------
        Solar conjunction experiments were conducted to improve
        understanding of the structure and dynamics of the solar
        corona and wind, to improve understanding of relativistic
        effects when radio waves propagate near the Sun, and to test
        the different elements of the radio science subsystem.
        Approximately once per year, each Voyager spacecraft appeared
        to pass behind the solar disk, as seen from Earth.  Radio
        waves propagating between Voyager and Earth stations were
        refracted and scattered (scintillation) by the solar plasma
        [WOO1993].  Intensity fluctuations can be related to
        fluctuations in electron density along the path, while Doppler
        or phase scintillations can be related to both electron
        density fluctuations and also the speed of the solar wind.
        Many plasma effects decrease as the square of the radio
        frequency; plasma effects are about an order of magnitude
        stronger at S-band than X-band.
 
 
      Experimental Relativity
      -----------------------
        The gravitational field of the Sun causes a time delay on
        signals that propagate near the Sun of approximately 300
        microseconds.  Although previous tests had verified the effect
        to an accuracy of a few percent, Voyager measurements could
        be conducted annually and at two frequencies, allowing
        separation of plasma effects.
 
        Gravitational fields of the gas giant planets also affected
        radio signals by causing them to have apparent frequencies
        lower than predicted.  The change in frequency is related to
        the mass of the planet.  By measuring the change in frequency
        as the spacecraft approached the planet, a value for the mass
        could be calculated.  This value could then be compared with
        the mass derived from two-way tracking data.  The spacecraft
        Ultra-Stable Oscillator was used for these measurements;
        two-way transmissions have nearly canceling frequency shifts
        as the signal travels to the spacecraft and then returns.  The
        dual frequencies available from Voyager allowed correction for
        plasma effects along the radio path, but calibration for
        radiation damage to the USO during encounters was more
        difficult.
 
 
    Operational Considerations - Spacecraft
    =======================================
      Descriptions given here are for nominal performance.  The
      spacecraft transponder system comprised redundant units,
      each with slightly different characteristics.  As
      transponder units age, their performance changes slightly.
      More importantly, the performance for radio science depended
      on operational factors such as the modulation state for the
      transmitters, which cannot be predicted in advance.  The
      performance also depended on factors which were not always
      under the control of the Voyager Project.
 
      Spacecraft receivers were designed to lock to the uplink
      signal.  Without locking, Doppler effects -- resulting from
      relative motion of the spacecraft and ground station -- could
      result in loss of the radio link as the frequency of the
      received signal drifted.  Unfortunately, a series of failures
      in the Voyager 2 receivers left that transponder unable to
      track the uplink signal.  Beginning in April 1978, Doppler
      shifts were predicted and the uplink carrier was tuned so
      that Voyager 2 would see what appeared to be a signal at
      constant frequency (to an accuracy of 100 Hz).
 
      During deep occultations by the giant planets, the bending angle
      resulting from refraction exceeded 10 degrees in some cases --
      well beyond the half power beamwidth of the spacecraft antenna.
      In those cases, the pointing of the HGA was adjusted so that
      it followed a 'virtual' Earth and maximum signal strength could
      be sustained.  These 'limb-track' maneuvers were critically
      dependent on accurate timing in the encounter.  To protect
      against timing errors at Titan (primarily from uncertaintes in
      the radius and position of the satellite), no limb-track was
      attempted during ingress while a fixed antenna offset was used
      during egress.
 
      Although the spacecraft radioisotope thermoelectric generators
      were not dependent on solar flux for power, their output decayed
      as the Voyager spacecraft moved outward through the solar
      system.  During encounters with the outer planets, caution was
      required in budgeting power and the high-power mode could not
      be used for the radio transmitters.
 
 
    Calibration Description - Spacecraft
    ====================================
      Prior to and during some encounter sequences, the spacecraft
      was commanded to execute a 'mini-azcal' maneuver.  The HGA was
      moved slightly above the Earth line then slightly below the
      Earth line.  The procedure was repeated to the left and right
      of the Earth line so that a 'cross-hair' pattern was mapped
      out.  During the maneuver, the amplitude of the carrier
      signal was measured carefully.  Analysis of the results would
      show whether the HGA was pointed accurately and, if not,
      approximately the error and direction.
 
      Prior to and after encounters, the spacecraft frequency
      reference was switched to the USO for several hours and the
      carrier signal was monitored using equipment at the DSN.
      These 'USO Tests' were used to calibrate the frequency and
      frequency drift of the USO.  USO tests were particularly
      important before and after the spacecraft entered a severe
      radiation environment since the radiation typically damaged
      the crystal and changed its characteristics slightly.
 
 
    Platform Mounting Descriptions - Spacecraft
    ===========================================
      The centerline of the bus was the roll axis of the
      spacecraft; it also served as the z-axis of the spacecraft
      coordinate system with the high-gain antenna (HGA) boresight
      defining the negative z-direction.  The HGA boresight was
      also defined as cone angle 0 degrees and as azimuth 180
      degrees, elevation 7 degrees.  The Low-Gain Antenna (LGA)
      was mounted on the feed structure of the HGA and radiated
      approximately uniformly over the hemisphere into which the
      HGA pointed.
 
 
    Principal Investigators
    =======================
      The Radio Science Team Leader through the Jupiter encounters
      was Von R. Eshleman.  The Team Leader for the Saturn, Uranus,
      and Neptune encounters was G. Leonard Tyler.
 
 
    Instrument Section / Operating Mode Descriptions - Spacecraft
    =============================================================
      The Voyager radio system consisted of two sections, which
      could be operated in the following modes:
 
      Section      Mode
      -------------------------------------------
      Oscillator   two-way (coherent)
                   one-way (non-coherent)
      RF output    low-gain antenna (no information available)
                   high-gain antenna
 
      Selected parameters describing NASA Standard Transponder (NST)
      performance are listed below:
 
      Oscillator Parameters:                    S-Band     X-Band
         Two-Way Transponder Turnaround Ratio  240/221    880/221
         One-Way Transmit Frequency (MHz)        2296.      8415.
         Nominal Wavelength (cm)                13.06       3.56
 
      RF Output parameters:                     S-Band     X-Band
         RF Power Output (w)                   9 or 26    12 or 22
         Low-Gain Antenna:
           Half-Power Half Beamwidth (deg)        UNK
           Gain (dBi)                             UNK
           EIRP (dBm)                             UNK
           Polarization                         Circular
         High-Gain Antenna:
           Half-Power Half-Beamwidth (deg)        1.1       0.32
           Gain (dBi)                              36        47
           Polarization                           RCP    RCP or LCP
 
 
    Instrument Overview - DSN
    =========================
      Three Deep Space Communications Complexes (DSCCs) (near
      Barstow, CA; Canberra, Australia; and Madrid, Spain) comprise
      the DSN tracking network.  Each complex is equipped with
      several antennas [including at least one each 70-m, 34-m High
      Efficiency (HEF), and 34-m standard (STD)], associated
      electronics, and operational systems.  Primary activity at each
      complex is radiation of commands to and reception of telemetry
      data from active spacecraft.  Transmission and reception is
      possible in several radio-frequency bands, the most common
      being S-band (nominally a frequency of 2100-2300 MHz or a
      wavelength of 14.2-13.0 cm) and X-band (7100-8500 MHz or 4.2-
      3.5 cm).  Transmitter output powers of up to 400 kw are
      available.
 
      Ground stations have the ability to transmit coded and uncoded
      waveforms which can be echoed by distant spacecraft.  Analysis
      of the received coding allows navigators to determine the
      distance to the spacecraft; analysis of Doppler shift on the
      carrier signal allows estimation of the line-of-sight
      spacecraft velocity.  Range and Doppler measurements are used
      to calculate the spacecraft trajectory and to infer gravity
      fields of objects near the spacecraft.
 
      Ground stations can record spacecraft signals that have
      propagated through or been scattered from target media.
      Measurements of signal parameters after wave interactions with
      surfaces, atmospheres, rings, and plasmas are used to infer
      physical and electrical properties of the target.
 
      Principal investigators vary from experiment to experiment.
      See the corresponding section of the spacecraft instrument
      description or the data set description for specifics.
 
      The Deep Space Network is managed by the Jet Propulsion
      Laboratory of the California Institute of Technology for the
      U.S.  National Aeronautics and Space Administration.
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
      radio science investigations see the reports by
      [ASMAR&RENZETTI1993], [ASMAR&HERRERA1993], and [ASMARETAL1995].
      For design specifications on DSN subsystems see [DSN810-5].  For
      an example of use of the DSN for Radio Science see
      [TYLERETAL1992].
 
 
    Subsystems - DSN
    ================
      The Deep Space Communications Complexes (DSCCs) are an integral
      part of the Radio Science instrument, along with other
      receiving stations and the spacecraft Radio Frequency
      Subsystem.  Their system performance directly determines the
      degree of success of Radio Science investigations, and their
      system calibration determines the degree of accuracy in the
      results of the experiments.  The following paragraphs describe
      the functions performed by the individual subsystems of a DSCC.
      This material has been adapted from [ASMAR&HERRERA1993]; for
      additional information, consult [DSN810-5].
 
      Each DSCC includes a set of antennas, a Signal Processing
      Center (SPC), and communication links to the Jet Propulsion
      Laboratory (JPL).  The general configuration is illustrated
      below; antennas (Deep Space Stations, or DSS -- a term carried
      over from earlier times when antennas were individually
      instrumented) are listed in the table.
 
          --------   --------   --------   --------   --------
         | DSS 12 | | DSS 18 | | DSS 14 | | DSS 15 | | DSS 16 |
         |34-m STD| |34-m STD| |  70-m  | |34-m HEF| |  26-m  |
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
            34-m STD        DSS 12       DSS 42       DSS 61
                            DSS 18       DSS 48       DSS 68
            34-m HEF        DSS 15       DSS 45       DSS 65
            70-m            DSS 14       DSS 43       DSS 63
            Developmental   DSS 13
 
 
      Subsystem interconnections at each DSCC are shown in the
      diagram below, and they are described in the sections that
      follow.  The Monitor and Control Subsystem is connected to all
      other subsystems; the Test Support Subsystem can be.
 
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
        archiving functions necessary to operate a DSCC.
        Communication among the various subsystems is done using a
        Local Area Network (LAN) hooked up to each subsystem via a
        network interface unit (NIU).
 
        DMC operations are divided into two separate areas: the
        Complex Monitor and Control (CMC) and the Link Monitor and
        Control (LMC).  The primary purpose of the CMC processor for
        Radio Science support is to receive and store all predict
        sets transmitted from NOCC such as Radio Science, antenna
        pointing, tracking, receiver, and uplink predict sets and
        then, at a later time, to distribute them to the appropriate
        subsystems via the LAN.  Those predict sets can be stored in
        the CMC for a maximum of three days under normal conditions.
        The CMC also receives, processes, and displays event/alarm
        messages; maintains an operator log; and produces tape labels
        for the DSP.  Assignment and configuration of the LMCs is
        done through the CMC; to a limited degree the CMC can perform
        some of the functions performed by the LMC.  There are two
        CMCs (one on-line and one backup) and three LMCs at each DSCC
        The backup CMC can function as an additional LMC if
        necessary.
 
        The LMC processor provides the operator interface for monitor
        and control of a link -- a group of equipment required to
        support a spacecraft pass.  For Radio Science, a link might
        include the DSCC Spectrum Processing Subsystem (DSP) (which,
        in turn, can control the SSI), or the Tracking Subsystem.
        The LMC also maintains an operator log which includes
        operator directives and subsystem responses.  One important
        Radio Science specific function that the LMC performs is
        receipt and transmission of the system temperature and signal
        level data from the PPM for display at the LMC console and
        for inclusion in Monitor blocks.  These blocks are recorded
        on magnetic tape as well as appearing in the Mission Control
        and Computing Center (MCCC) displays.  The LMC is required to
        operate without interruption for the duration of the Radio
        Science data acquisition period.
 
        The Area Routing Assembly (ARA), which is part of the Digital
        Communications Subsystem, controls all data communication
        between the stations and JPL.  The ARA receives all required
        data and status messages from the LMC/CMC and can record them
        to tape as well as transmit them to JPL via data lines.  The
        ARA also receives predicts and other data from JPL and passes
        them on to the CMC.
 
 
      DSCC Antenna Mechanical Subsystem
      ---------------------------------
        Multi-mission Radio Science activities require support from
        the 70-m, 34-m HEF, and 34-m STD antenna subnets.  The
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
        34-m STD primary reflectors are classical paraboloids, while
        the subreflectors are standard hyperboloids.
 
        On the 70-m and 34-m STD antennas, the subreflector directs
        received energy from the antenna onto a dichroic plate, a
        device which reflects S-band energy to the S-band feed horn
        and passes X-band energy through to the X-band feed horn.  In
        the 34-m HEF, there is one 'common aperture feed,' which
        accepts both frequencies without requiring a dichroic plate.
        RF energy to be transmitted into space by the horns is
        focused by the reflectors into narrow cylindrical beams,
        pointed with high precision (either to the dichroic plate or
        directly to the subreflector) by a series of drive motors and
        gear trains that can rotate the movable components and their
        support structures.
 
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
        the desired position.  Unlike the 70-m and 34-m HEFs which
        have azimuth-elevation (AZ-EL) drives, the 34-m STD antennas
        use (hour angle-declination) HA-DEC drives.  The same
        positioning of the subreflector on the 34-m STD does not
        create the same effect as on the 70-m and 34-m HEFs.
 
        Pointing angles for all three antenna types are computed by
        the NOCC Support System (NSS) from an ephemeris provided by
        the flight project.  These predicts are received and archived
        by the CMC.  Before each track, they are transferred to the
        APA, which transforms the direction cosines of the predicts
        into AZ-EL coordinates for the 70-m and 34-m HEFs or into
        HA-DEC coordinates for the 34-m STD antennas.  The LMC
        operator then downloads the antenna AZ-EL or HA-DEC predict
        points to the antenna-mounted ACS computer along with a
        selected SEC model.  The pointing predicts consist of
        time-tagged AZ-EL or HA-DEC points at selected time intervals
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
        antenna.  In the 34-m STD antennas motors, rather than
        servos, are used to steer the antenna; there is no feedback
        once the 34-m STD has been told where to point.
 
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
 
        34-m STD Antennas: These antennas have two feed horns, one
        for S-band signals and one for X-band.  The horns are mounted
        on a cone which is fixed in relation to the subreflector.  A
        dichroic plate mounted above the horns directs energy from
        the subreflector into the proper horn.
 
        The AMS directs the received S- and X-band signals through
        polarizer plates and on to amplification.  There are two
        Block III S-band TWMs and two Block I X-band TWMs.
 
        34-m HEF Antennas: Unlike the other antennas, the 34-m HEF
        uses a single feed for both S- and X-band.  Simultaneous S-
        and X-band receive as well as X-band transmit is possible
        thanks to the presence of an S/X 'combiner' which acts as a
        diplexer.  For S-band, RCP or LCP is user selected through a
        switch so neither a polarizer nor an orthomode transducer is
        needed.  X-band amplification options include two Block II
        TWMs or an HEMT Low Noise Amplifier (LNA).  S-band
        amplification is provided by an FET LNA.
 
 
      DSCC Receiver-Exciter Subsystem
      -------------------------------
        The Receiver-Exciter Subsystem is composed of three groups of
        equipment: the closed-loop receiver group, the open-loop
        receiver group, and the RF monitor group.  This subsystem is
        controlled by the Receiver-Exciter Controller (REC) which
        communicates directly with the DMC for predicts and OCI
        reception and status reporting.
 
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
 
        Closed Loop Receivers: The Block IV receiver-exciter at the
        70-m stations allows for two receiver channels, each capable
        of L-Band (e.g., 1668 MHz frequency or 18 cm wavelength),
        S-band, or X-band reception, and an S-band exciter for
        generation of uplink signals through the low-power or
        high-power transmitter.  The Block III receiver-exciter at
        the 34-m STD stations allows for two receiver channels, each
        capable of S-band or X-band reception and an exciter used to
        generate an uplink signal through the low-power transmitter.
        The receiver-exciter at the 34-m HEF stations allows for one
        channel only.
 
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
 
        The closed-loop receiver AGC loop can be configured to one of
        three settings: narrow, medium, or wide.  It will be
        configured such that the expected amplitude changes are
        accommodated with minimum distortion.  The loop bandwidth
        (2BLo) will be configured such that the expected phase
        changes can be accommodated while maintaining the best
        possible loop SNR.
 
        Open-Loop Receivers: There are two types of Radio Science
        Open-Loop Receivers (OLR) in use.  At 70-m and 34-m HEF
        stations the OLR is a dedicated four channel, narrow-band
        receiver which provides amplified and downconverted video band
        signals to the DSCC Spectrum Processing Subsystem (DSP); it
        sometimes goes by the designation 'RIV'.  At 34-m STD stations
        (DSS 42 and DSS 61) the OLR is an older system, the Multi-
        Mission Receiver (MMR), which provides two channels of narrow-
        band receiver output.  Both OLR systems are described in
        detail below under 'Electronics - DSN'; here the overview
        continues only for the RIV system.
 
        The 70-m and 34-m HEF OLR utilizes a fixed first Local
        Oscillator (LO) frequency and a tunable second LO frequency
        to minimize phase noise and improve frequency stability.
        The OLR consists of an RF-to-IF downconverter located in
        the antenna, an IF selection switch (IVC), and a Radio
        Science IF-VF downconverter (RIV) located in the SPC.
        The RF-IF downconverters in the 70-m antennas are equipped
        for four IF channels: S-RCP, S-LCP, X-RCP, and X-LCP.  The
        34-m HEF stations are equipped with a two-channel RF-IF:
        S-band and X-band.  The IVC switches the IF input between
        the 70-m and 34-m HEF antennas.
 
        The RIV contains the tunable second LO, a set of video
        bandpass filters, IF attenuators, and a controller (RIC).
        The LO tuning is done via DSP control of the POCA/PLO
        combination based on a predict set.  The POCA is a
        Programmable Oscillator Control Assembly and the PLO is a
        Programmable Local Oscillator (commonly called the DANA
        synthesizer).  The bandpass filters are selectable via the
        DSP.  The RIC provides an interface between the DSP and the
        RIV.  It is controlled from the LMC via the DSP.  The RIC
        selects the filter and attenuator settings and provides
        monitor data to the DSP.  The RIC could also be manually
        controlled from the front panel in case the electronic
        interface to the DSP is lost.
 
        RF Monitor -- SSI and PPM: The RF monitor group of the
        Receiver-Exciter Subsystem provides spectral measurements
        using the Spectral Signal Indicator (SSI) and measurements of
        the received channel system temperature and spacecraft signal
        level using the Precision Power Monitor (PPM).
 
        The SSI provides a local display of the received signal
        spectrum at a dedicated terminal at the DSCC and routes these
        same data to the DSP which routes them to NOCC for remote
        display at JPL for real-time monitoring and RIV/DSP
        configuration verification.  These displays are used to
        validate Radio Science Subsystem data at the DSS, NOCC, and
        Mission Support Areas.  The SSI configuration is controlled
        by the DSP and a duplicate of the SSI spectrum appears on the
        LMC via the DSP.  During real-time operations the SSI data
        also serve as a quick-look science data type for Radio
        Science experiments.
 
        The PPM measures system noise temperatures (SNT) using a
        Noise Adding Radiometer (NAR) and downlink signal levels
        using the Signal Level Estimator (SLE).  The PPM accepts its
        input from the closed-loop receiver.  The SNT is measured by
        injecting known amounts of noise power into the signal path
        and comparing the total power with the noise injection 'on'
        against the total power with the noise injection 'off.' That
        operation is based on the fact that receiver noise power is
        directly proportional to temperature; thus measuring the
        relative increase in noise power due to the presence of a
        calibrated thermal noise source allows direct calculation of
        SNT.  Signal level is measured by calculating an FFT to
        estimate the SNR between the signal level and the receiver
        noise floor where the power is known from the SNT
        measurements.
 
        There is one PPM controller at the SPC which is used to
        control all SNT measurements.  The SNT integration time can
        be selected to represent the time required for a measurement
        of 30K to have a one-sigma uncertainty of 0.3K or 1%.
 
 
      DSCC Transmitter Subsystem
      --------------------------
        The Transmitter Subsystem accepts the S-band frequency
        exciter signal from the Block III or Block IV Receiver-
        Exciter Subsystem exciter and amplifies it to the required
        transmit output level.  The amplified signal is routed via
        the diplexer through the feed horn to the antenna and then
        focused and beamed to the spacecraft.
 
        The Transmitter Subsystem power capabilities range from 18 kw
        to 400 kw.  Power levels above 18 kw are available only at
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
 
 
      DSCC Spectrum Processing Subsystem (DSP)
      ----------------------------------------
        The DSCC Spectrum Processing Subsystem (DSP) located at the
        SPC digitizes and records the narrowband output data from
        the RIV.  It consists of a Narrow Band Occultation Converter
        (NBOC) containing four Analog-to-Digital Converters (ADCs),
        a ModComp CLASSIC computer processor called the Spectrum
        Processing Assembly (SPA), and several magnetic tape drives.
        Magnetic tapes containing DSP output are known as Original
        Data Records (ODRs).  Electronic near real-time data
        transmission (known as an Original Data Stream, or ODS) may
        be possible in certain circumstances.
 
        The DSP is operated through the LMC.  Using the
        SPA-Radioscience (SPA-R) software, the DSP allows for
        real-time frequency and time offsets (while in RUN mode)
        and, if necessary, snap tuning between the two frequency
        ranges transmitted by the spacecraft: coherent and
        non-coherent.  The DSP receives Radio Science frequency
        predicts from the CMC, allows for multiple predict set
        archiving (up to 60 sets) at the SPA, and allows for manual
        predict generation and editing.  It accepts configuration
        and control data from the LMC, provides display data to the
        LMC, and transmits the signal spectra from the SSI as well
        as status information to NOCC and the Project Mission
        Support Area (MSA) via the GCF data lines.  The DSP records
        the digitized narrowband samples and the supporting header
        information (i.e., time tags, POCA frequencies, etc.) on
        9-track magnetic tapes in 6250 or 1600 bpi GCR format.
 
        Through the DSP-RIC interface the DSP controls the RIV filter
        selection and attenuation levels.  It also receives RIV
        performance monitoring via the RIC.  In case of failure of
        the DSP-RIC interface, the RIV can be controlled manually
        from the front panel.
 
        All the RIV and DSP control parameters and configuration
        directives are stored in the SPA in a macro-like file called
        an 'experiment directive' table.  A number of default
        directives exist in the DSP for the major Radio Science
        experiments.  Operators can create their own table entries.
 
        Items such as verification of the configuration of the prime
        open-loop recording subsystem, the selection of the required
        predict sets, and proper system performance prior to the
        recording periods will be checked in real-time at JPL via the
        NOCC displays using primarily the remote SSI display at NOCC
        and the NRV displays.  Because of this, transmission of the
        DSP/SSI monitor information is enabled prior to the start of
        recording.  The specific run time and tape recording times
        will be identified in the Sequence of Events (SOE) and/or DSN
        Keyword File.
 
        The DSP can be used to duplicate ODRs.  It also has the
        capability to play back a certain section of the recorded
        data after conclusion of the recording periods.
 
 
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
 
 
    Optics - DSN
    ============
      Performance of DSN ground stations depends primarily on size of
      the antenna and capabilities of electronics.  These are
      summarized in the following set of tables.  Note that 64-m
      antennas were upgraded to 70-m between 1986 and 1989.
      Beamwidth is half-power full angular width.  Polarization is
      circular; L denotes left circular polarization (LCP), and R
      denotes right circular polarization (RCP).
 
                           DSS S-Band Characteristics
 
                               64-m      70-m     34-m     34-m
           Transmit                                STD      HEF
           --------           -----     -----    -----    -----
           Frequency (MHz)    2110-     2110-    2025-     N/A
                               2120      2120     2120
           Wavelength (m)     0.142     0.142    0.142     N/A
           Ant Gain (dBi)                62.7     55.2     N/A
           Beamwidth (deg)              0.119     0.31     N/A
           Polarization                L or R   L or R     N/A
           Tx Power (kW)               20-400       20     N/A
 
           Receive
           -------
           Frequency (MHz)    2270-     2270-    2270-    2200-
                               2300      2300     2300     2300
           Wavelength (m)     0.131     0.131    0.131    0.131
           Ant Gain (dBi)      61.6      63.3     56.2     56.0
           Beamwidth (deg)              0.108     0.27     0.24
           Polarization       L & R     L & R   L or R   L or R
           System Temp (K)       22        20       22       38
 
                           DSS X-Band Characteristics
 
                               64-m      70-m     34-m     34-m
           Transmit                                STD      HEF
           --------           -----     -----    -----    -----
           Frequency (MHz)     8495      8495     N/A     7145-
                                                           7190
           Wavelength (m)     0.035     0.035     N/A     0.042
           Ant Gain (dBi)                74.2     N/A        67
           Beamwidth (deg)                        N/A     0.074
           Polarization      L or R    L or R     N/A    L or R
           Tx Power (kW)        360       360     N/A        20
 
           Receive
           -------
           Frequency (MHz)    8400-     8400-    8400-    8400-
                               8500      8500     8500     8500
           Wavelength (m)     0.036     0.036    0.036    0.036
           Ant Gain (dBi)      71.7      74.2     66.2     68.3
           Beamwidth (deg)              0.031    0.075    0.063
           Polarization       L & R     L & R    L & R    L & R
           System Temp (K)       27        20       25       20
 
           NB: X-band 64-m and 70-m transmitting parameters are given
               at 8495 MHz, the frequency used by the Goldstone
               planetary radar system.  For telecommunications, the
               transmitting frequency would be in the range 7145-7190
               MHz, the power would typically be 20 kW, and the gain
               would be about 72.6 dB (70-m antenna).  When ground
               transmitters are used in spacecraft radio science
               experiments, the details of transmitter and antenna
               performance rarely impact the results.
 
 
    Electronics - DSN
    =================
 
      DSCC Open-Loop Receiver (RIV)
      -----------------------------
        The open loop receiver block diagram shown below is for the
        RIV system at 70-m and 34-m High-Efficiency (HEF) antenna
        sites.  Input signals at both S- and X-band are mixed to
        approximately 300 MHz by fixed-frequency local oscillators
        near the antenna feed.  Based on a tuning prediction file,
        the POCA controls the DANA synthesizer, the output of which
        (after multiplication) mixes the 300 MHz IF to 50 MHz for
        amplification.  These signals in turn are down converted and
        passed through additional filters until they yield Output
        with bandwidths up to 45 kHz.  The Output is digitally
        sampled and either written to magnetic tape or electronically
        transferred for further analysis.
 
          S-Band                                          X-Band
         2295 MHz                                        8415 MHz
          Input                                            Input
            |                                                |
            v                                                v
           ---     ---                              ---     ---
          | X |<--|x20|<--100 MHz        100 MHz-->|x81|-->| X |
           ---     ---                              ---     ---
            |                                                |
         295|                                                |315
         MHz|                                                |MHz
            v                                                v
           ---     --                 33.1818       ---     ---
          | X |<--|x3|<------           MHz ------>|x11|-->| X |
           ---     --        |115          |        ---     ---
            |                |MHz          |                 |
            |                |             |                 |
          50|      71.8181  ---           ---                |50
         MHz|         MHz->| X |         | X |<-10MHz        |MHz
            v               ---           ---                v
           ---               ^             ^                ---
          | X |<--60 MHz     |             |      60 MHz-->| X |
           ---               |   approx    |                ---
            |        9.9     | 43.1818 MHz |      9.9        |
            |        MHz      -------------       MHz        |
            |         |             ^              |         |
          10|         v             |              v         |10
         MHz|        ---       ----------         ---        |MHz
            |------>| X |     |   DANA   |       | X |<------|
            |        ---      |Synthesizr|        ---        |
            |         |        ----------          |         |
            v         v             ^              v         v
         -------   -------          |           -------   -------
        |Filters| |Filters|    ----------      |Filters| |Filters|
        |3,4,5,6| |  1,2  |   |   POCA   |     |  1,2  | |3,4,5,6|
         -------   -------    |Controller|      -------   -------
            |         |        ----------          |         |
          10|         |0.1                      0.1|         |10
         MHz|         |MHz                      MHz|         |MHz
            v         v                            v         v
           ---       ---                          ---       ---
10 MHz -->| X |     | X |<------ 0.1 MHz ------->| X |     | X |<--
           ---       ---                          ---       ---    |
            |         |                            |         |  10 MHz
            v         v                            v         v
         Output     Output                      Output     Output
 
 
        Reconstruction of the antenna frequency from the frequency of
        the signal in the recorded data can be achieved through use
        of one of the following formulas.  Filters are defined below.
 
   FSant=3*SYN+1.95*10^9+3*(790/11)*10^6+Frec        (Filter 4)
        =3*SYN+1.95*10^9+3*(790/11)*10^6-Fsamp+Frec  (Filters 1-3,5,6)
 
   FXant=11*SYN + 7.940*10^9 +   Fsamp - Frec        (Filter 4)
        =11*SYN + 7.940*10^9 - 3*Fsamp + Frec        (Filters 1,2,3,6)
 
    where
        FSant,FXant  are the antenna frequencies of the incoming
                      signals at S and X bands, respectively,
        SYN          is the output frequency of the DANA synthesizer,
                      commonly labeled the readback POCA frequency on
                      data tapes,
        Fsamp        is the effective sampling rate of the digital
                      samples, and
        Frec         is the apparent signal frequency in a spectrum
                      reconstructed from the digital samples.
 
           NB: For many of the filter choices (see below) the Output
               is that of a bandpass filter.  The sampling rates
               in the table below are sufficient for the bandwidth
               but not the absolute maximum frequency, and aliasing
               results.  The reconstruction expressions above are
               appropriate ONLY when the sample rate shown in the
               tables below is used.
 
      DSCC Open-Loop Receiver (MMR at DSS 5 and 61)
      ---------------------------------------------
        The open loop receiver block diagram shown below is for MMR
        systems at the 34-m Standard (STD) DSS 61 antenna site and at
        the DSS 5 JPL DSN facility.  Based on a tuning prediction
        file, the POCA controls the DANA synthesizer, the output of
        which (after multiplication) mixes input signals at both
        S- and X-band to fixed intermediate frequencies for
        amplification.  These signals in turn are down converted
        and passed through additional filters until they yield Output
        with bandwidths up to 45 kHz.  The Output is digitally
        sampled and either written to magnetic tape or electronically
        transferred for further analysis.
 
          S-Band                                          X-Band
         2295 MHz                                        8415 MHz
          Input                                            Input
            |                                                |
            v                                                v
           ---                                              ---
          | X |<-------------               -------------->| X |
           ---           1995|             |8115            ---
            |             MHz|             |MHz              |
            |                |             |                 |
            |                |            ---                |
            |                |           | X |<--800 MHz     |
            |                |            ---                |
            |                |             |                 |
         300|                |             |                 |300
         MHz|               ---          ----                |MHz
            |              |x48|        |x176|               |
            v               ---          ----                v
           ---               ^             ^                ---
          | X |<--290 MHz    |             |     290 MHz-->| X |
           ---               |   approx    |                ---
            |        9.9     |  41.56 MHz  |      9.9        |
            |        MHz      -------------       MHz        |
            |         |             ^              |         |
          10|         v             |              v         |10
         MHz|        ---       ----------         ---        |MHz
            |------>| X |     |   DANA   |       | X |<------|
            |        ---      |Synthesizr|        ---        |
            |         |        ----------          |         |
            v         v             ^              v         v
         -------   -------          |           -------   -------
        |Filters| |Filters|    ----------      |Filters| |Filters|
        |  4-8  | |  1-3  |   |   POCA   |     |  1-3  | |  4-8  |
         -------   -------    |Controller|      -------   -------
            |         |        ----------          |         |
          10|         |0.1                      0.1|         |10
         MHz|         |MHz                      MHz|         |MHz
            v         v                            v         v
           ---       ---                          ---       ---
10 MHz -->| X |     | X |<------ 0.1 MHz ------->| X |     | X |<--
           ---       ---                          ---       ---    |
            |         |                            |         |    10
            v         v                            v         v    MHz
         Output     Output                      Output     Output
 
        Reconstruction of the antenna frequency from the frequency of
        the signal in the recorded data can be achieved through use
        of one of the following formulas.  Filters are defined below.
 
    FSant = 48*SYN + 300*10^6 - Fsamp + Frec        (Filters 1,2,3,8)
          = 48*SYN + 300*10^6 + Frec                (Filters 4,5,6,7)
 
    FXant = 176*SYN + 1100*10^6 - 3*Fsamp + Frec    (Filters 1,2,3,8)
          = 176*SYN + 1100*10^6 + Frec              (Filters 4,5,6,7)
 
        where the definition of terms and 'NB' are the same as for
        the RIV system (above).
 
      DSCC Open-Loop Receiver (MMR at DSS 7 and 42)
      ---------------------------------------------
        The open loop receiver block diagram shown below is for the
        MMR system at the 34-m Standard (STD) DSS 42 antenna site and
        the DSS 7 DSN facility at JPL.  Based on a tuning prediction
        file, the POCA controls the DANA synthesizer, the output of
        which (after multiplication) mixes input signals at both
        S- and X-band to fixed intermediate frequencies for
        amplification.  These signals in turn are down converted and
        passed through additional filters until they yield Output
        with bandwidths up to 45 kHz.  The Output is digitally
        sampled and either written to magnetic tape or electronically
        transferred for further analysis.
 
          S-Band                                          X-Band
         2295 MHz                                        8415 MHz
          Input                         800 MHz            Input
            |                              |                 |
            v                              v      8115       v
           ---        1995 MHz            ---      MHz      ---
          | X |<-------------            | X |------------>| X |
           ---               |            ---               ---
            |                |             |                 |
            |               ---           ---                |
            |              |x 3|         |x11|               |
            |               ---  approx   ---                |
            |                |   665 MHz   |                 |
            |                 -------------                  |
         300|                       |                        |300
         MHz|                      ---                       |MHz
            |                     | X |<--600 MHz            |
            v                      ---                       v
           ---                      ^                       ---
          | X |<--290 MHz           |            290 MHz-->| X |
           ---                    -----                     ---
            |        9.9         |x 1.5|          9.9        |
            |        MHz          -----           MHz        |
            |         |             ^              |         |
          10|         v             |              v         |10
         MHz|        ---       ----------         ---        |MHz
            |------>| X |     |   DANA   |       | X |<------|
            |        ---      |Synthesizr|        ---        |
            |         |        ----------          |         |
            v         v             ^              v         v
         -------   -------          |           -------   -------
        |Filters| |Filters|    ----------      |Filters| |Filters|
        |  4-8  | |  1-3  |   |   POCA   |     |  1-3  | |  4-8  |
         -------   -------    |Controller|      -------   -------
            |         |        ----------          |         |
          10|         |0.1                      0.1|         |10
         MHz|         |MHz                      MHz|         |MHz
            v         v                            v         v
           ---       ---                          ---       ---
10 MHz -->| X |     | X |<------ 0.1 MHz ------->| X |     | X |<--
           ---       ---                          ---       ---    |
            |         |                            |         |    10
            v         v                            v         v    MHz
         Output     Output                      Output     Output
 
        Reconstruction of the antenna frequency from the frequency of
        the signal in the recorded data can be achieved through use
        of one of the following formulas.  Filters are defined below.
 
    FSant = (9/2)*SYN + 2100*10^6 - Fsamp + Frec     (Filters 1,2,3,8)
          = (9/2)*SYN + 2100*10^6 + Frec             (Filters 4,5,6,7)
 
    FXant = (33/2)*SYN + 7700*10^6 - 3*Fsamp + Frec  (Filters 1,2,3,8)
          = (33/2)*SYN + 7700*10^6 + Frec            (Filters 4,5,6,7)
 
        where the definition of terms and 'NB' are the same as for the
        RIV system (above).
 
 
    Filters - DSN
    =============
 
      DSCC Open-Loop Receiver (RIV)
      -----------------------------
        Nominal filter center frequencies and bandwidths for the RIV
        Receivers are shown in the table below.  Recommended sampling
        rates are also given.
 
                            S-Band                    X-Band
                   ------------------------  -------------------------
                   Output   3 dB   Sampling  Output   3 dB    Sampling
         Filter    Center   Band     Rate    Center   Band      Rate
                    Freq    Width            Freq     Width
                    (Hz)    (Hz)     (sps)   (Hz)     (Hz)      (sps)
         ------    ------  ------  --------  ------  ------   --------
            1         150      82      200      550      82        200
            2         750     415     1000     2750     415       1000
            3        3750    2000     5000    13750    2000       5000
            4        1023    1700     5000     3750    6250      15000
            5       75000   45000   100000   275000   45000     100000
            6       37500   20000    50000   137500   20000      50000
 
      DSCC Open-Loop Receiver (MMR)
      -----------------------------
        MMR filters (DSS 5, 7, 42, and 61) and recommended sampling
        rates include the following:
 
                            S-Band                    X-Band
                   ------------------------  -------------------------
                   Output   3 dB Recommended Output   3 dB Recommended
         Filter    Center   Band   Sampling  Center   Band    Sampling
                    Freq    Width    Rate*   Freq     Width     Rate*
                    (Hz)    (Hz)     (sps)   (Hz)     (Hz)      (sps)
         ------    ------  ------  --------  ------  ------   --------
            1         150     100       200     550     100        200
            2         750     500      1000    2750     500       1000
            3        1500    1000      2000    5500    1000       2000
            4         409     818      2000    1500    3000       6000
            5        1023    2045      5000    3750    7500      15000
            6        2045    4091     10000    7500   15000      30000
            7        4091    8182     20000   15000   30000      60000
            8       37500   20000     50000  137500   20000      50000
 
         * Sampling rates depend on resolution of samples and number
           of analog-to-digital converters assigned to each channel --
           see discussion of modes under 'DSCC Spectrum Processing
           Subsystem' below.  The rates at which single A/D converters
           can operate with the MMR include:
 
            8-bit samples:      12-bit samples:      16-bit samples:
                         200                  200                 1250
                         250                 1000
                         400                 1250
                         500                 2000
                        1000                 5000
                        1250                10000
                        2000
                        2500
                        3125
                        4000
                        5000
                        6250
                       10000
                       12500
                       15625
                       20000
                       25000
                       31250
                       50000
 
    Detectors - DSN
    ===============
 
      DSCC Open-Loop Receivers
      ------------------------
        Open-loop receiver output is detected in software by the
        radio science investigator.
 
 
      DSCC Closed-Loop Receivers
      --------------------------
        Nominal carrier tracking loop threshold noise bandwidth at
        both S- and X-band is 10 Hz.  Coherent (two-way) closed-loop
        system stability is shown in the table below:
 
            integration time            Doppler uncertainty
                 (secs)               (one sigma, microns/sec)
                 ------               ------------------------
                    10                            50
                    60                            20
                  1000                             4
 
 
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
 
 
      Open-Loop Receiver Attenuation Calibration
      ------------------------------------------
        The open-loop receiver attenuator calibrations are performed
        to establish the output of the open-loop receivers at a level
        that will not saturate the analog-to-digital converters.  To
        achieve this, the calibration is done using a test signal
        generated by the exciter/translator that is set to the peak
        predicted signal level for the upcoming pass.  Then the
        output level of the receiver's video band spectrum envelope
        is adjusted to the level determined by equation (3) below (to
        five-sigma).  Note that the SNR in the equation (2) is in dB
        while the SNR in equation (3) is linear.
 
          Pn = -198.6 + 10*log(SNT) + 10*log(1.2*Fbw)              (1)
 
          SNR = Ps - Pn                               (SNR in dB)  (2)
 
          Vrms = sqrt(SNR + 1)/[1 + 0.283*sqrt(SNR)]  (SNR linear) (3)
 
           where    Fbw = receiver filter bandwidth (Hz)
                    Pn  = receiver noise power (dBm)
                    Ps  = signal power (dBm)
                    SNT = system noise temperature (K)
                    SNR = predicted signal-to-noise ratio
 
 
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
        the feed horns on all three antennas may be configured so
        that it is out of the received signal path in order to
        improve the signal-to-noise ratio in the receiver system.
        This is known as the 'listen-only' or 'bypass' mode.
 
 
      Closed-Loop vs. Open-Loop Reception
      -----------------------------------
        Radio Science data can be collected in two modes: closed-
        loop, in which a phase-locked loop receiver tracks the
        spacecraft signal, or open-loop, in which a receiver samples
        and records a band within which the desired signal presumably
        resides.  Closed-loop data are collected using Closed-Loop
        Receivers, and open-loop data are collected using Open-Loop
        Receivers in conjunction with the DSCC Spectrum Processing
        Subsystem (DSP).  See the Subsystems section for further
        information.
 
 
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
        typically of 240/221.  In the non-coherent mode, the
        downlink carrier frequency is derived from the spacecraft
        on-board crystal-controlled oscillator.  Either closed-loop
        or open-loop receivers (or both) can be used with either
        spacecraft frequency reference mode.  Closed-loop reception
        in two-way mode is usually preferred for routine tracking.
        Occasionally the spacecraft operates coherently while two
        ground stations receive the 'downlink' signal; this is
        sometimes known as the 'three-way' mode.
 
 
      DSCC Spectrum Processing Subsystem (DSP)
      ----------------------------------------
        The DSP can operate in four sampling modes with from 1 to 4
        input signals.  Input channels are assigned to ADC inputs
        during DSP configuration.  Modes and sampling rates are
        summarized in the tables below:
 
        Mode   Analog-to-Digital Operation
        ----   ----------------------------
          1    4 signals, each sampled by a single ADC
          2    1 signal, sampled sequentially by 4 ADCs
          3    2 signals, each sampled sequentially by 2 ADCs
          4    2 signals, the first sampled by ADC #1 and the second
                           sampled sequentially at 3 times the rate
                            by ADCs #2-4
 
             8-bit Samples               12-bit  Samples
            Sampling  Rates              Sampling  Rates
         (samples/sec per ADC)        (samples/sec per ADC)
         ---------------------        ---------------------
                 50000
                 31250
                 25000
                 15625
                 12500
                 10000                        10000
                  6250
                  5000                         5000
                  4000
                  3125
                  2500
                                               2000
                  1250
                  1000                         1000
                   500
                   400
                   250
                   200                          200
 
        Input to each ADC is identified in header records by a Signal
        Channel Number (J1 - J4).  Nominal channel assignments are
        shown below.
 
             Signal Channel Number              Receiver
                                        (70-m or HEF)  (34-m STD)
             ---------------------      -------------  ----------
                      J1                    X-RCP       not used
                      J2                    S-RCP       not used
                      J3                    X-LCP         X-RCP
                      J4                    S-LCP         S-RCP
 
 
    Location - DSN
    ==============
      Station locations are documented in [GEO-10REVD].  Geocentric
      coordinates are summarized here.
 
                            Geocentric  Geocentric  Geocentric
      Station              Radius (km) Latitude (N) Longitude (E)
      ---------            ----------- ------------ -------------
      Goldstone
        DSS 12 (34-m STD)  6371.997815  35.1186672   243.1945048
        DSS 13 (develop)   6372.117062  35.0665485   243.2051077
        DSS 14 (70-m)      6371.992867  35.2443514   243.1104584
        DSS 15 (34-m HEF)  6371.9463    35.2402863   243.1128186
        DSS 16 (26-m)      6371.9608    35.1601436   243.1264200
        DSS 18 (34-m STD)      UNK          UNK          UNK
 
      Canberra
        DSS 42 (34-m STD)  6371.675607 -35.2191850   148.9812546
        DSS 43 (70-m)      6371.688953 -35.2209308   148.9812540
        DSS 45 (34-m HEF)  6371.692    -35.21709     148.97757
        DSS 46 (26-m)      6371.675    -35.22360     148.98297
        DSS 48 (34-m STD)      UNK          UNK          UNK
 
      Madrid
        DSS 61 (34-m STD)  6370.027734  40.2388805   355.7509634
        DSS 63 (70-m)      6370.051015  40.2413495   355.7519776
        DSS 65 (34-m HEF)  6370.021370  40.2372843   355.7485968
        DSS 66 (26-m)      6370.036     40.2400714   355.7485976
 
 
    Measurement Parameters - DSN
    ============================
 
      Open-Loop System
      ----------------
        Output from the Open-Loop Receivers (OLRs), as sampled and
        recorded by the DSCC Spectrum Processing Subsystem (DSP), is
        a stream of 8- or 12-bit quantized voltage samples.  The
        nominal input to the Analog-to-Digital Converters (ADCs) is
        +/-10 volts, but the precise scaling between input voltages
        and output digitized samples is usually irrelevant for
        analysis; the digital data are generally referenced to a
        known noise or signal level within the data stream itself --
        for example, the thermal noise output of the radio receivers
        which has a known system noise temperature (SNT).  Raw
        samples comprise the data block in each DSP record; a header
        record (presently 83 16-bit words) contains ancillary
        information such as:
 
         time tag for the first sample in the data block
         RMS values of receiver signal levels and ADC outputs
         POCA frequency and drift rate
 
 
      Closed-Loop System
      ------------------
        Closed-loop data are recorded in Archival Tracking Data Files
        (ATDFs), as well as certain secondary products such as the
        Orbit Data File (ODF).  The ATDF Tracking Logical Record
        contains 117 entries including status information and
        measurements of ranging, Doppler, and signal strength.
 
 
    ACRONYMS AND ABBREVIATIONS - DSN
    ================================
      ACS      Antenna Control System
      ADC      Analog-to-Digital Converter
      AMS      Antenna Microwave System
      APA      Antenna Pointing Assembly
      ARA      Area Routing Assembly
      ATDF     Archival Tracking Data File
      AZ       Azimuth
      CMC      Complex Monitor and Control
      CONSCAN  Conical Scanning (antenna pointing mode)
      CRG      Coherent Reference Generator
      CUL      Clean-up Loop
      DANA     a type of frequency synthesizer
      dB       deciBel
      dBi      dB relative to isotropic
      dBm      dB relative to one milliwatt
      DCO      Digitally Controlled Oscillator
      DEC      Declination
      deg      degree
      DMC      DSCC Monitor and Control Subsystem
      DSCC     Deep Space Communications Complex
      DSN      Deep Space Network
      DSP      DSCC Spectrum Processing Subsystem
      DSS      Deep Space Station
      DTK      DSCC Tracking Subsystem
      E        east
      EL       Elevation
      FTS      Frequency and Timing Subsystem
      GCF      Ground Communications Facility
      GPS      Global Positioning System
      HA       Hour Angle
      HEF      High-Efficiency (as in 34-m HEF antennas)
      IF       Intermediate Frequency
      IVC      IF Selection Switch
      JPL      Jet Propulsion Laboratory
      K        Kelvin
      km       kilometer
      kW       kilowatt
      L-band   approximately 1668 MHz
      LAN      Local Area Network
      LCP      Left-Circularly Polarized
      LMC      Link Monitor and Control
      LNA      Low-Noise Amplifier
      LO       Local Oscillator
      m        meters
      MCA      Master Clock Assembly
      MCCC     Mission Control and Computing Center
      MDA      Metric Data Assembly
      MHz      Megahertz
      MMR      Multi-Mission Receiver
      MON      Monitor and Control System
      MSA      Mission Support Area
      N        north
      NAR      Noise Adding Radiometer
      NBOC     Narrow-Band Occultation Converter
      NIST     SPC 10 time relative to UTC
      NIU      Network Interface Unit
      NOCC     Network Operations and Control System
      NSS      NOCC Support System
      OCI      Operator Control Input
      ODF      Orbit Data File
      ODR      Original Data Record
      ODS      Original Data Stream
      OLR      Open Loop Receiver
      POCA     Programmable Oscillator Control Assembly
      PPM      Precision Power Monitor
      RA       Right Ascension
      REC      Receiver-Exciter Controller
      RCP      Right-Circularly Polarized
      RF       Radio Frequency
      RIC      RIV Controller
      RIV      Radio Science IF-VF Converter Assembly
      RMDCT    Radio Metric Data Conditioning Team
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
      SRA      Sequential Ranging Assembly
      SRC      Sub-Reflector Controller
      SSI      Spectral Signal Indicator
      STD      Standard (as in 34-m STD antennas)
      TID      Time Insertion and Distribution Assembly
      TSF      Tracking Synthesizer Frequency
      TWM      Traveling Wave Maser
      UNK      unknown
      UTC      Universal Coordinated Time
      VF       Video Frequency
      X-band   approximately 7800-8500 MHz
 

        