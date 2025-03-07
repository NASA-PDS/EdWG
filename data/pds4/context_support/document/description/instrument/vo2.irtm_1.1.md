
 
 
        INSTRUMENT: INFRARED THERMAL MAPPER
        SPACECRAFT: VIKING ORBITER 2
 
 
    Instrument Information
    ======================
      Instrument Id                  : IRTM
      Instrument Host Id             : VO2
      Pi Pds User Id                 : HKIEFFER
      Instrument Name                : UNK
      Instrument Type                : RADIOMETER
      Build Date                     : 1974
      Instrument Mass                : 8.400000
      Instrument Length              : 0.330000
      Instrument Width               : 0.267000
      Instrument Height              : 0.178000
      Instrument Serial Number       : 005
      Instrument Manufacturer Name   : SANTA BARBARA RESEARCH CENTER
 
 
    Instrument Description
    ======================
      The IRTM contains four small Cassegrainian telescopes which
      each image the same, seven circular areas.  There is a total of
      twenty-eight channels in four surface and one atmospheric
      thermal band from 6 micrometer to 30 micrometer and a broad
      solar reflectance band.  All channels are sampled
      simultaneously, using the spacecraft scanning capability to map
      the radiance over small and large areas of the planet.  All
      channels use thermopile detectors; spectral passbands are
      determined by a combination of interference filters, detector
      lens materials, antireflection coatings, and reststrahlen
      optics.  The scan modes are described in the PDS INSTRUMENT
      MODE DESCRIPTION.
 
 
    Science Objectives
    ==================
      The objective of the Viking Orbiter infrared thermal mapper
      (IRTM) is to measure the thermal emission of the Martian
      surface and atmosphere and total reflected sunlight with high
      spatial and flux resolution.
 
 
    Operational Considerations
    ==========================
      Most low and moderate resolution IRTM data were acquired
      through using 'box scans'.  These were commonly acquired
      between 1-6 hours from periapsis, and utilized the scan
      platform to slew back and forth in cone angle (in the direction
      the IRTM chevron points) with small offsets in the same
      direction between these oscillating slews.  Ignoring spacecraft
      motion, this pattern would generate bi-directional evenly
      spaced scans with the seven IRTM detectors.  Spacecraft motion
      during the scan sequence, typically of 10-40 minutes duration,
      created some distortion in this otherwise uniform pattern.
      Typical resulting scans across the planetary surface are shown
      in Figure 3 of Kieffer et al., 1976.  These scans were usually
      designed to extend slightly off the limb of the planet on at
      least one side.  These 'planet port' off-planet data provided
      the best estimates of the zero radiance response of the
      instrument.  When the spacecraft was near periapsis, the
      apparent motion of the planetary surface relative to the
      spacecraft was too rapid to allow oscillating slews.  At these
      times, the instrument would simply 'stare' in one direction and
      use the spacecraft motion to sweep the detector pattern across
      the surface.  These observations were usually acquired in
      Normal Mode, but occasionally Fixed Planet was used.  At
      irregular times through the mission, 'phase function'
      observations were made.  These involved using the two axis scan
      platform to follow one point on the ground as the spacecraft
      went from horizon to horizon relative to this surface point.
      In actuality, this sequence was acquired using a small number
      of discrete scan platform moves, allowing the instrument to
      'stare' across a short stripe centered on the target point
      between slews.  Such 'phase function' observations typically
      yielded about 10 different viewing geometries within a single
      sequence.  These observations were particularly useful in
      determining the influence of the atmosphere.  In preparation of
      the IRTM data set, all observations which were more than 1 1/2
      degrees apparent angle above the nearest limb of the planet
      were deleted.
 
      Geometry Errors Due to Uncertain Timing: Early and late during
      the Viking mission, orbital solutions based on the tracking
      telemetry were determined every few days.  During VO-1
      revolution 175-603 and VO-2 revolutions 118-521, orbital
      solutions were often separated by a week or more.  Because
      there is significant irregularity in the Martian gravitional
      field, these irregularities could slowly influence the orbit of
      the Viking spacecraft in unpredictable ways.  The primary
      influence was in the period of the orbit, resulting in
      uncertainty as to exactly where the spacecraft was along its
      orbit at any specific time.  These uncertainties were as large
      as 75 seconds in the worst case.  Far from periapsis, these
      timing uncertainties were not of major significance because the
      spacecraft velocities were low and the projected fields of
      views on the planet were large.  However, near periapsis, the
      IRTM field of view could move across the surface equivalent to
      its full width in as little as one second.  Thus, when there
      was a large timing error, the computed ground intercept
      locations could be in error by many fields of view.  In the
      worst case, these positions may be in error by up to 200 km.
      When the magnitude of this problem was discovered, the SEDR
      (geometry calculations) for the imaging instrument was rerun
      with revised orbit solutions.  However, it was impractical to
      regenerate the IRTM SEDR and these errors have not been
      corrected.  There was an attempt by the navigational team to
      estimate the magnitude of the timing error for both Viking
      spacecraft for those revolutions through the affected part of
      the Viking mission.  This is described in the 1980 April 14
      memo by Frank Palluconi, which contains estimates of the
      magnitude of the error for each revolution.  Hugh Kieffer has a
      copy (the sole surviving copy?) of this memo.  A direct
      determination of the timing offset can be made from the IRTM
      data alone in those instances when thermal patterns can be
      unambiguously identified with surface features.  Since the
      dominant geometric error is in time, maps of thermal patterns
      (typically as contours of observed temperature minus the
      calculated standard model temperature) can be slid across the
      cartographic map parallel to the subspacecraft track (if the
      instrument was in fixed planet mode, this is simply sliding the
      IRTM trace along its own path) until the thermal and
      cartographic features are aligned.  Because there are small
      gaps in the IRTM coverage every 64 ICKs, the amount the IRTM
      pattern must be shifted to agree with the surface morphology
      can be scaled directly into a timing offset in seconds.  This
      has been done for a variety of high resolution scans across
      Arsia Mons (by Jim Zimbelman) and for many scans across Valles
      Marineris (by David Paige and Hugh Kieffer).  A set of known
      offsets is slowly accumulating.  Hugh Kieffer has a copy (the
      sole surviving copy?) of the memo discussing this problem.
 
 
    Calibration Description
    =======================
      Relative spectral response of all channels was measured end to
      end using a Perkin-Elmer 16 U monochrometer with appropriate
      gratings and order filters.  A globar at 1400 K was used in the
      2-25 micrometer range; shortward of 2.0 micrometers a tungsten
      source at 2700 K was used.  The reference detector was a
      thermocouple for all but the 0.4-1.1 micrometer range, where a
      calibrated silicon photodiode was used.  Out-of-band
      measurements were made by replacing the spectrometer grating
      with a plane mirror and ir materials having known cutoff and
      cuton wavelengths.  Flux calibration of the IRTM was performed
      under a simulated space environment using a vacuum chamber
      operated typically at a pressure of 1.E-6 Torr.  The IRTM was
      operated by means of a console which simulated the interfaces
      and functions of the spacecraft FDS.  A minicomputer was used
      to provide all operational sequences and modes.  Data were
      recorded on magnetic tape for subsequent computer processing.
      The calibration fixture consisted of two identical blackbodies,
      one located in front of the space port and maintained at liquid
      nitrogen temperature and the other in front of the planet port
      and adjustable in temperature from 77 K to 350K; eleven
      settings from 140 K to 330 K were used.  Blackbody temperatures
      were measured with platinum resistance thermometers having an
      absolute accuracy of +/- 0.1 degrees C.  traceable to the
      National Bureau of Standards.  The digitizer used in the test
      console provided ten times the resolution of the FDS digitizer,
      thus making the digitizing uncertainty during calibration
      insignificant compared to the noise.  The calibration data thus
      produced are IRTM output in digitization level (DN) as a
      function of blackbody temperature.  Radiometrically measured
      internal reference surface temperatures showed close agreement
      (+/- 0.5 degrees C.) with those measured independently with a
      thermister.  The IRTM temperature was controlled by regulating
      the temperature of a mounting base plate and the thermal shield
      inside the vacuum chamber.  Calibration was performed at 10
      degrees C.  spacing across the range of operating temperatures
      expected during flight.  Typical IRTM channel response to scene
      brightness temperatures is shown in Fig.  8 of CHASE_ETAL_1978.
      The one-sample noise on the thermal channels is less than 1 DN
      except for the 15 micrometer channel where it is about 2.5 DN.
      The dynamic ranges of the surface thermal bands are based on
      temperatures expected for the Martian surface.  The 300 K
      maximum chosen for the A telescope might be exceeded by midday
      summer temperatures, but temperatures above the 310-K limit of
      the B telescope should not be exceeded unless active volcanic
      areas were found; temperatures to 320 K and 330 K could be
      measured by the 9 micrometer and 7 micrometer bands.  The 15
      micrometer band dynamic range was set quite large as its
      resolution is noise limited rather than digitization limited.
      Telescope D channels were calibrated using a different method.
      The radiance source was a mercury-xenon lamp and narrowband
      filter centered at 0.896 micrometer with a bandwidth of 425 nm.
      The in-band radiance of the lamp was known by direct comparison
      with a standard lamp acquired from the National Bureau of
      Standards, using a silicon photodiode as a transfer standard.
      The relative spectral response measurements then allowed
      extension of the one-point absolute calibration to the entire
      passband.  Gains for the D channels were set to give full scale
      for 75% of the diffuse reflection of solar irradiance at Mars
      average distance from the sun.  Using integrals of the Planck
      function and the measured spectral response, the flux response
      of the IRTM is found to be close to linear in the thermal
      channels.  The best fit quadratic functions, normalized to full
      scale, typically had constant and quadratic coefficients of
      0.002 and 0.02, respectively.  The solar band channels, which
      had much higher absolute flux levels at full scale, showed a
      decrease in response at high signal levels corresponding to a
      quadratic coefficient of 0.07.  With the IRTM in the vacuum
      chamber, the instrument response was measured at four lamp
      currents.  An additional series of wide band measurements
      utilizing a NBS standard lamp and a barium sulfate diffusing
      screen, in which only the lamp-screen distance was changed, was
      used to determine in detail the solar band nonlinearity.
      During spacecraft thermal-vacuum testing and in flight, a small
      drift of about 1-min duration was found to be induced when the
      scan mirror moved to the reference position in normal mode.
      This appears to be caused by the decrease in radiative heat
      loss from the instrument when the telescopes do not view space.
      The shape of this postreference drift was accurately determined
      during normal mode sequences when the spacecraft was well away
      from Mars, and this effect is removed in the data reduction.
      The change of the thermal state of the IRTM caused by large
      scan platform slew or planetary radiation near periapsis can
      introduce significant drifts of the zero-flux level.  These
      shifts have a time constant of 1-2 min or longer, and their
      magnitude increases with inband wavelength and preamplifier
      gain.  It is probably due primarily to very small temperature
      gradients induced in the detector packages as the general
      instrument temperature changes.  A significant design feature
      of the IRTM is that the space DN level of each channel is
      measured immediately prior to and after the restore which
      occurs each minute in normal mode.  A linear interpolation
      between these zero-flux DN levels is used in data
      decalibration.  The remaining quadratic and higher order drift
      is generally negligible.
 
 
    Section 'IRTM'
    ==============
      Total Fovs                     : 7
      Data Rate                      : 250.000000
      Sample Bits                    : 10
 
 
      'IRTM' Detectors
      ----------------
        A
 
 
      'IRTM' Electronics
      ------------------
        IRTM
 
 
      'IRTM' Filters
      --------------
        SOLAR UV-22
        T11
        T15
        T20
        T7
        T9
 
 
      'IRTM' Section Optic IDs
      ------------------------
        A
        B
        C
        D
 
 
      In modes
      --------
        FIXED PLANET
        FIXED REFERENCE
        FIXED SPACE
        MODIFIED NORMAL
        NORMAL
 
 
      'IRTM' Section FOV Shape 'CIRCULAR'
      -----------------------------------
        Section Id                     : IRTM
        Fovs                           : 7
        Horizontal Pixel Fov           : 0.292000
        Vertical Pixel Fov             : 0.292000
        Horizontal Fov                 : 2.402000
        Vertical Fov                   : 1.347000
 
 
      'IRTM' Section Parameter 'RADIANCE A'
      -------------------------------------
        The A telescope measured wavelengths between 16 and 30
        microns.  This parameter is the radiance in that band.
 
        Instrument Parameter Name      : RADIANCE A
        Sampling Parameter Name        : TIME
        Instrument Parameter Unit      : WATT_METER**-2_MICROMETER**-1
        Minimum Instrument Parameter   : 0.000000
        Maximum Instrument Parameter   : 0.002030
        Noise Level                    : 0.000001
        Sampling Parameter Interval    : 1.120000
        Sampling Parameter Resolution  : 1.120000
        Sampling Parameter Unit        : SECOND
 
 
      'IRTM' Section Parameter 'RADIANCE B'
      -------------------------------------
        The B telescope measured wavelengths between 10 and 13
        microns.  This parameter is the radiance in that band.
 
        Instrument Parameter Name      : RADIANCE B
        Sampling Parameter Name        : TIME
        Instrument Parameter Unit      : WATT_METER**-2_MICROMETER**-1
        Minimum Instrument Parameter   : 0.000000
        Maximum Instrument Parameter   : 0.003120
        Noise Level                    : 0.000001
        Sampling Parameter Interval    : 1.120000
        Sampling Parameter Resolution  : 1.120000
        Sampling Parameter Unit        : SECOND
 
 
      'IRTM' Section Parameter 'RADIANCE C1'
      --------------------------------------
        The C1 set of 3 detectors (out of 7 in the C telescope) were
        limited by filtering to wavelengths between 6 and 8 microns.
        This parameter is the radiance in that band.
 
        Instrument Parameter Name      : RADIANCE C1
        Sampling Parameter Name        : TIME
        Instrument Parameter Unit      : WATT_METER**-2_MICROMETER**-1
        Minimum Instrument Parameter   : 0.000000
        Maximum Instrument Parameter   : 0.003190
        Noise Level                    : 0.000001
        Sampling Parameter Interval    : 1.120000
        Sampling Parameter Resolution  : 1.120000
        Sampling Parameter Unit        : SECOND
 
 
      'IRTM' Section Parameter 'RADIANCE C2'
      --------------------------------------
        The C2 set of 3 detectors (out of 7 in the C telescope) were
        limited by filtering to wavelengths between 8 and 10 microns.
        This parameter is the radiance in that band.
 
        Instrument Parameter Name      : RADIANCE C2
        Sampling Parameter Name        : TIME
        Instrument Parameter Unit      : WATT_METER**-2_MICROMETER**-1
        Minimum Instrument Parameter   : 0.000000
        Maximum Instrument Parameter   : 0.001980
        Noise Level                    : 0.000001
        Sampling Parameter Interval    : 1.120000
        Sampling Parameter Resolution  : 1.120000
        Sampling Parameter Unit        : SECOND
 
 
      'IRTM' Section Parameter 'RADIANCE C3'
      --------------------------------------
        The C3 detector/filter combination within the C telescope
        responded to wavelengths between 14.5 and 15.5 microns.  This
        parameter is the radiance in that band.
 
        Instrument Parameter Name      : RADIANCE C3
        Sampling Parameter Name        : TIME
        Instrument Parameter Unit      : WATT_METER**-2_MICROMETER**-1
        Minimum Instrument Parameter   : 0.000000
        Maximum Instrument Parameter   : 0.006340
        Noise Level                    : 0.000003
        Sampling Parameter Interval    : 1.120000
        Sampling Parameter Resolution  : 1.120000
        Sampling Parameter Unit        : SECOND
 
 
      'IRTM' Section Parameter 'RADIANCE D'
      -------------------------------------
        The D telescope measured wavelengths between 0.3 and 3.0
        microns.  This parameter is the radiance in that band.
 
        Instrument Parameter Name      : RADIANCE D
        Sampling Parameter Name        : TIME
        Instrument Parameter Unit      : WATT_METER**-2_MICROMETER**-1
        Minimum Instrument Parameter   : 0.000000
        Maximum Instrument Parameter   : 135.840000
        Noise Level                    : 0.030000
        Sampling Parameter Interval    : 1.120000
        Sampling Parameter Resolution  : 1.120000
        Sampling Parameter Unit        : SECOND
 
 
    Instrument Detector 'A'
    =======================
      Detector Type                  : THERMOPILE ARRAY
      Detector Aspect Ratio          : 1.000000
      Minimum Wavelength             : 0.300000
      Maximum Wavelength             : 100.000000
      Nominal Operating Temperature  : 275.000000
 
 
      Description
      -----------
        The seven-element thin-film antimony-bismuth thermopile array
        used in the IRTM is shown in Fig.  7 of CHASE_ETAL_1978.  The
        chevron arrangement was based on the need for uniform
        coverage irrespective of scan platform orientation; it also
        allowed the detectors to all be approximately the same
        distance from the telescope optic axis.  In this application
        thermopiles were found to be better than other thermal
        detectors because they operate to dc and exhibit no 1/f
        noise.  Thus, no optical chopper is needed.  Also, no bias
        supply, another potential source of 1/f noise, is needed.
        Cooled quantum detectors were not practical, considering the
        duration and weight constraints of the Viking Mission.  The
        array was made by evaporating the various components onto a
        sapphire film using photoetched masks for dimensional
        control.  The film, about 200 nm thick, is supported by a
        sapphire disk.  The film was made by anodizing aluminum foil
        and etching away the aluminum.  The black circular dots in
        the figure are the sensitive areas overlaid with bismuth
        oxide smoke which has good ir absorptivity but low thermal
        mass.  Characteristics
 
              Active area               7.E-4 cm**2
              Number of junctions   6
              Resistance                13.E3 ohm
              Time constant             80-100 msec
              Responsivity              130 V/Watt
              Detectivity (D*)  2.E8 cm_Hz**0.5_W**-1
 
        To obtain full sensitivity the detectors must be evacuated.
        Therefore, during ground testing the detector packages were
        pumped down through a permanently attached manifold.  At
        other times the detector packages were backfilled with xenon
        to protect the detectors while still allowing gross
        sensitivity checks.  To avoid exposure to moisture during the
        long period prior to launch when the IRTM was mounted on the
        spacecraft and could not be sealed, the manifold was kept at
        a slight positive pressure by a continuous flow of high
        purity nitrogen.  The manifold was opened to space by launch
        vehicle separation.
 
 
      Sensitivity
      -----------
        The detectivity is 2.E8 CM_HZ**0.5_W**-1
 
 
    Instrument Electronics 'IRTM'
    =============================
 
      Description
      -----------
        The signal channels use a synchronous demodulation scheme to
        provide good stability and to avoid 1/f noise in the preamp.
        The input FET chopper is a full-wave type operating at 471
        Hz.  This and the center-tapped thermopile allow voltage
        doubling of the detector signal and noise and thus reduce the
        preamp noise contribution which otherwise would be
        significant.  The differential input connection, while
        suffering a square root (2) noise disadvantage compared to
        single-ended input, provides excellent common mode rejection
        of chopper spikes and other input noise.  Temperature
        dependence of the thermopile, about -0.5%/degree C., is
        compensated by a thermister network external to the hybrid
        package.  Preamp gain is adjustable with an external
        resistor.  Following the half-wave synchronous demodulator is
        an integrate, hold, and reset circuit with an integrate time
        of 981 msec.  The integrator serves as a low pass filter
        while the hold feature ensures spatial simultaneity of
        corresponding detectors in each telescope.  After completion
        of sampling by the multiplexer, all channel hold circuits are
        reset to ensure independence of data samples.  The IRTM
        analog signals, which have a range of +/- 6V, are digitized
        by the analog-to-pulse width converter and flight data
        subsystem (FDS) counter into +/- 2**9 levels, yielding 1023
        data numbers (DN) which are nearly linear with radiance in
        each channel.  The IRTM multiplexer consists of sixty-eight
        FET switches and a buffer signal amplifier.  In addition to
        thirty-two data channels (twenty-eight active and four
        spare), thirty-two channels of engineering data are also
        sample.  These include eight temperature measurements from
        thermisters located at four locations on the reference plate,
        the electronics module, and each of the three ir detector
        packages (telescopes A, B, C).  Three power supply voltages
        and the pre-dc restore voltage of twenty-one channels
        (telescopes A, B, and C) are monitored.  The pre-dc restore
        monitors are diagnostic to determine the presence of large
        thermal or detector offsets.  The scan mirror is driven by a
        four-position stepper motor through a 50/1 gear reduction.  A
        motor drive pulse duration of 40 msec allows a 90 degree
        mirror rotation in 2 sec.  The mirror position is sensed by a
        two-bit encoder on the motor shaft; the contacts at the three
        desired positions are about half of the width of 1.8 degree
        mirror step.  The motor stepping is controlled by the FDS
        using a comparison of the encoder readout with the desired
        position originating either from the FDS normal mode clock or
        direct ground command; the motor cannot be directly
        commanded.  In addition to the restore which occurs
        automatically in the normal model when the mirror reaches the
        space position, restores can be ground commanded when the
        IRTM is in the fixed planet or fixed space mode; in either
        case housekeeping data are multiplexed into the data stream
        during the 1-sec restore period.  Whenever the mirror reaches
        the reference position, the calibration lamp is turned on for
        the next two integration periods.  The lamp is at full
        radiance throughout the second integration period, which is
        used for gain determination of the D telescope channels.  In
        the fixed reference mode, science and housekeeping data are
        sampled alternatively.
 
 
    Instrument Filter 'A - T20'
    ===========================
      Filter Name                    : T20
      Filter Type                    : RESTSTRAHLEN
      Minimum Wavelength             : 17.700000
      Maximum Wavelength             : 30.000000
      Center Filter Wavelength       : 21.000000
 
 
      Description
      -----------
        Relative spectral response of all channels was measured end
        to end using a Perkin-Elmer 16 U monochrometer with
        appropriate gratings and order filters.  A globar at 1400 K
        was used in the 2-25 micrometer range; shortward of 2.0
        micrometers a tungsten source at 2700 K was used.  The
        reference detector was a thermocouple for all but the 0.4-1.1
        micrometer range, where a calibrated silicon photodiode was
        used.  Out-of-band measurements were made by replacing the
        spectrometer grating with a plane mirror and ir materials
        having known cutoff and cuton wavelengths.  Flux calibration
        of the IRTM was performed under a simulated space environment
        using a vacuum chamber operated typically at a pressure of
        1.E-6 Torr.  The IRTM was operated by means of a console
        which simulated the interfaces and functions of the
        spacecraft FDS.  A minicomputer was used to provide all
        operational sequences and modes.  Data were recorded on
        magnetic tape for subsequent computer processing.  The
        calibration fixture consisted of two identical blackbodies,
        one located in front of the space port and maintained at
        liquid nitrogen temperature and the other in front of the
        plant port and adjustable in temperature from 77 K to 350K;
        eleven settings from 140 K to 330 K were used.  Blackbody
        temperatures were measured with platinum resistance
        thermometers having an absolute accuracy of +/- 0.1 degrees
        C.  traceable to the National Bureau of Standards.  The
        digitizer used in the test console provided ten times the
        resolution of the FDS digitizer, thus making the digitizing
        uncertainty during calibration insignificant compared to the
        noise.  The calibration data thus produced are IRTM output in
        digitization level (DN) as a function of blackbody
        temperature.  Radiometrically measured internal reference
        surface temperatures showed close agreement (+/- 0.5 degrees
        C.) with those measured independently with a thermister.  The
        IRTM temperature was controlled by regulating the temperature
        of a mounting base plate and the thermal shield inside the
        vacuum chamber.  Calibration was performed at 10 degrees C.
        spacing across the range of operating temperatures expected
        during flight.  Typical IRTM channel response to scene
        brightness temperatures is shown in Fig.  8 of
        CHASE_ETAL_1978.  The one-sample noise on the thermal
        channels is less than 1 DN except for the 15 micrometer
        channel where it is about 2.5 DN.  The dynamic ranges of the
        surface thermal bands are based on temperatures expected for
        the Martian surface.  The 300 K maximum chosen for the A
        telescope might be exceeded by midday summer temperatures,
        but temperatures above the 310-K limit of the B telescope
        should not be exceeded unless active volcanic areas were
        found; temperatures to 320 K and 330 K could be measured by
        the 9 micrometer and 7 micrometer bands.  The 15 micrometer
        band dynamic range was set quite large as its resolution is
        noise limited rather than digitization limited.
 
 
    Instrument Filter 'B - T11'
    ===========================
      Filter Name                    : T11
      Filter Type                    : MULTILAYER INTERFERENCE
      Minimum Wavelength             : 9.800000
      Maximum Wavelength             : 12.500000
      Center Filter Wavelength       : 11.200000
 
 
      Description
      -----------
        Relative spectral response of all channels was measured end
        to end using a Perkin-Elmer 16 U monochrometer with
        appropriate gratings and order filters.  A globar at 1400 K
        was used in the 2-25 micrometer range; shortward of 2.0
        micrometers a tungsten source at 2700 K was used.  The
        reference detector was a thermocouple for all but the 0.4-1.1
        micrometer range, where a calibrated silicon photodiode was
        used.  Out-of-band measurements were made by replacing the
        spectrometer grating with a plane mirror and ir materials
        having known cutoff and cuton wavelengths.  Flux calibration
        of the IRTM was performed under a simulated space environment
        using a vacuum chamber operated typically at a pressure of
        1.E-6 Torr.  The IRTM was operated by means of a console
        which simulated the interfaces and functions of the
        spacecraft FDS.  A minicomputer was used to provide all
        operational sequences and modes.  Data were recorded on
        magnetic tape for subsequent computer processing.  The
        calibration fixture consisted of two identical blackbodies,
        one located in front of the space port and maintained at
        liquid nitrogen temperature and the other in front of the
        plant port and adjustable in temperature from 77 K to 350K;
        eleven settings from 140 K to 330 K were used.  Blackbody
        temperatures were measured with platinum resistance
        thermometers having an absolute accuracy of +/- 0.1 degrees
        C.  traceable to the National Bureau of Standards.  The
        digitizer used in the test console provided ten times the
        resolution of the FDS digitizer, thus making the digitizing
        uncertainty during calibration insignificant compared to the
        noise.  The calibration data thus produced are IRTM output in
        digitization level (DN) as a function of blackbody
        temperature.  Radiometrically measured internal reference
        surface temperatures showed close agreement (+/- 0.5 degrees
        C.) with those measured independently with a thermister.  The
        IRTM temperature was controlled by regulating the temperature
        of a mounting base plate and the thermal shield inside the
        vacuum chamber.  Calibration was performed at 10 degrees C.
        spacing across the range of operating temperatures expected
        during flight.  Typical IRTM channel response to scene
        brightness temperatures is shown in Fig.  8 of
        CHASE_ETAL_1978.  The one-sample noise on the thermal
        channels is less than 1 DN except for the 15 micrometer
        channel where it is about 2.5 DN.  The dynamic ranges of the
        surface thermal bands are based on temperatures expected for
        the Martian surface.  The 300 K maximum chosen for the A
        telescope might be exceeded by midday summer temperatures,
        but temperatures above the 310-K limit of the B telescope
        should not be exceeded unless active volcanic areas were
        found; temperatures to 320 K and 330 K could be measured by
        the 9 micrometer and 7 micrometer bands.  The 15 micrometer
        band dynamic range was set quite large as its resolution is
        noise limited rather than digitization limited.
 
 
    Instrument Filter 'C1 - T7'
    ===========================
      Filter Name                    : T7
      Filter Type                    : MULTILAYER INTERFERENCE
      Minimum Wavelength             : 6.100000
      Maximum Wavelength             : 8.300000
      Center Filter Wavelength       : 7.200000
 
 
      Description
      -----------
        Relative spectral response of all channels was measured end
        to end using a Perkin-Elmer 16 U monochrometer with
        appropriate gratings and order filters.  A globar at 1400 K
        was used in the 2-25 micrometer range; shortward of 2.0
        micrometers a tungsten source at 2700 K was used.  The
        reference detector was a thermocouple for all but the 0.4-1.1
        micrometer range, where a calibrated silicon photodiode was
        used.  Out-of-band measurements were made by replacing the
        spectrometer grating with a plane mirror and ir materials
        having known cutoff and cuton wavelengths.  Flux calibration
        of the IRTM was performed under a simulated space environment
        using a vacuum chamber operated typically at a pressure of
        1.E-6 Torr.  The IRTM was operated by means of a console
        which simulated the interfaces and functions of the
        spacecraft FDS.  A minicomputer was used to provide all
        operational sequences and modes.  Data were recorded on
        magnetic tape for subsequent computer processing.  The
        calibration fixture consisted of two identical blackbodies,
        one located in front of the space port and maintained at
        liquid nitrogen temperature and the other in front of the
        plant port and adjustable in temperature from 77 K to 350K;
        eleven settings from 140 K to 330 K were used.  Blackbody
        temperatures were measured with platinum resistance
        thermometers having an absolute accuracy of +/- 0.1 degrees
        C.  traceable to the National Bureau of Standards.  The
        digitizer used in the test console provided ten times the
        resolution of the FDS digitizer, thus making the digitizing
        uncertainty during calibration insignificant compared to the
        noise.  The calibration data thus produced are IRTM output in
        digitization level (DN) as a function of blackbody
        temperature.  Radiometrically measured internal reference
        surface temperatures showed close agreement (+/- 0.5 degrees
        C.) with those measured independently with a thermister.  The
        IRTM temperature was controlled by regulating the temperature
        of a mounting base plate and the thermal shield inside the
        vacuum chamber.  Calibration was performed at 10 degrees C.
        spacing across the range of operating temperatures expected
        during flight.  Typical IRTM channel response to scene
        brightness temperatures is shown in Fig.  8 of
        CHASE_ETAL_1978.  The one-sample noise on the thermal
        channels is less than 1 DN except for the 15 micrometer
        channel where it is about 2.5 DN.  The dynamic ranges of the
        surface thermal bands are based on temperatures expected for
        the Martian surface.  The 300 K maximum chosen for the A
        telescope might be exceeded by midday summer temperatures,
        but temperatures above the 310-K limit of the B telescope
        should not be exceeded unless active volcanic areas were
        found; temperatures to 320 K and 330 K could be measured by
        the 9 micrometer and 7 micrometer bands.  The 15 micrometer
        band dynamic range was set quite large as its resolution is
        noise limited rather than digitization limited.
 
 
    Instrument Filter 'C2 - T9'
    ===========================
      Filter Name                    : T9
      Filter Type                    : MULTILAYER INTERFERENCE
      Minimum Wavelength             : 8.300000
      Maximum Wavelength             : 9.800000
      Center Filter Wavelength       : 9.000000
 
 
      Description
      -----------
        Relative spectral response of all channels was measured end
        to end using a Perkin-Elmer 16 U monochrometer with
        appropriate gratings and order filters.  A globar at 1400 K
        was used in the 2-25 micrometer range; shortward of 2.0
        micrometers a tungsten source at 2700 K was used.  The
        reference detector was a thermocouple for all but the 0.4-1.1
        micrometer range, where a calibrated silicon photodiode was
        used.  Out-of-band measurements were made by replacing the
        spectrometer grating with a plane mirror and ir materials
        having known cutoff and cuton wavelengths.  Flux calibration
        of the IRTM was performed under a simulated space environment
        using a vacuum chamber operated typically at a pressure of
        1.E-6 Torr.  The IRTM was operated by means of a console
        which simulated the interfaces and functions of the
        spacecraft FDS.  A minicomputer was used to provide all
        operational sequences and modes.  Data were recorded on
        magnetic tape for subsequent computer processing.  The
        calibration fixture consisted of two identical blackbodies,
        one located in front of the space port and maintained at
        liquid nitrogen temperature and the other in front of the
        plant port and adjustable in temperature from 77 K to 350K;
        eleven settings from 140 K to 330 K were used.  Blackbody
        temperatures were measured with platinum resistance
        thermometers having an absolute accuracy of +/- 0.1 degrees
        C.  traceable to the National Bureau of Standards.  The
        digitizer used in the test console provided ten times the
        resolution of the FDS digitizer, thus making the digitizing
        uncertainty during calibration insignificant compared to the
        noise.  The calibration data thus produced are IRTM output in
        digitization level (DN) as a function of blackbody
        temperature.  Radiometrically measured internal reference
        surface temperatures showed close agreement (+/- 0.5 degrees
        C.) with those measured independently with a thermister.  The
        IRTM temperature was controlled by regulating the temperature
        of a mounting base plate and the thermal shield inside the
        vacuum chamber.  Calibration was performed at 10 degrees C.
        spacing across the range of operating temperatures expected
        during flight.  Typical IRTM channel response to scene
        brightness temperatures is shown in Fig.  8 of
        CHASE_ETAL_1978.  The one-sample noise on the thermal
        channels is less than 1 DN except for the 15 micrometer
        channel where it is about 2.5 DN.  The dynamic ranges of the
        surface thermal bands are based on temperatures expected for
        the Martian surface.  The 300 K maximum chosen for the A
        telescope might be exceeded by midday summer temperatures,
        but temperatures above the 310-K limit of the B telescope
        should not be exceeded unless active volcanic areas were
        found; temperatures to 320 K and 330 K could be measured by
        the 9 micrometer and 7 micrometer bands.  The 15 micrometer
        band dynamic range was set quite large as its resolution is
        noise limited rather than digitization limited.
 
 
    Instrument Filter 'C3 - T15'
    ============================
      Filter Name                    : T15
      Filter Type                    : MULTILAYER INTERFERENCE
      Minimum Wavelength             : 14.560000
      Maximum Wavelength             : 15.410000
      Center Filter Wavelength       : 15.000000
 
 
      Description
      -----------
        Relative spectral response of all channels was measured end
        to end using a Perkin-Elmer 16 U monochrometer with
        appropriate gratings and order filters.  A globar at 1400 K
        was used in the 2-25 micrometer range; shortward of 2.0
        micrometers a tungsten source at 2700 K was used.  The
        reference detector was a thermocouple for all but the 0.4-1.1
        micrometer range, where a calibrated silicon photodiode was
        used.  Out-of-band measurements were made by replacing the
        spectrometer grating with a plane mirror and ir materials
        having known cutoff and cuton wavelengths.  Flux calibration
        of the IRTM was performed under a simulated space environment
        using a vacuum chamber operated typically at a pressure of
        1.E-6 Torr.  The IRTM was operated by means of a console
        which simulated the interfaces and functions of the
        spacecraft FDS.  A minicomputer was used to provide all
        operational sequences and modes.  Data were recorded on
        magnetic tape for subsequent computer processing.  The
        calibration fixture consisted of two identical blackbodies,
        one located in front of the space port and maintained at
        liquid nitrogen temperature and the other in front of the
        plant port and adjustable in temperature from 77 K to 350K;
        eleven settings from 140 K to 330 K were used.  Blackbody
        temperatures were measured with platinum resistance
        thermometers having an absolute accuracy of +/- 0.1 degrees
        C.  traceable to the National Bureau of Standards.  The
        digitizer used in the test console provided ten times the
        resolution of the FDS digitizer, thus making the digitizing
        uncertainty during calibration insignificant compared to the
        noise.  The calibration data thus produced are IRTM output in
        digitization level (DN) as a function of blackbody
        temperature.  Radiometrically measured internal reference
        surface temperatures showed close agreement (+/- 0.5 degrees
        C.) with those measured independently with a thermister.  The
        IRTM temperature was controlled by regulating the temperature
        of a mounting base plate and the thermal shield inside the
        vacuum chamber.  Calibration was performed at 10 degrees C.
        spacing across the range of operating temperatures expected
        during flight.  Typical IRTM channel response to scene
        brightness temperatures is shown in Fig.  8 of
        CHASE_ETAL_1978.  The one-sample noise on the thermal
        channels is less than 1 DN except for the 15 micrometer
        channel where it is about 2.5 DN.  The dynamic ranges of the
        surface thermal bands are based on temperatures expected for
        the Martian surface.  The 300 K maximum chosen for the A
        telescope might be exceeded by midday summer temperatures,
        but temperatures above the 310-K limit of the B telescope
        should not be exceeded unless active volcanic areas were
        found; temperatures to 320 K and 330 K could be measured by
        the 9 micrometer and 7 micrometer bands.  The 15 micrometer
        band dynamic range was set quite large as its resolution is
        noise limited rather than digitization limited.
 
 
    Instrument Filter 'D - SOLAR UV-22'
    ===================================
      Filter Name                    : SOLAR UV-22
      Filter Type                    : MULTILAYER INTERFERENCE
      Minimum Wavelength             : 0.300000
      Maximum Wavelength             : 3.000000
      Center Filter Wavelength       : 1.600000
 
 
      Description
      -----------
        Relative spectral response of all channels was measured end
        to end using a Perkin-Elmer 16 U monochrometer with
        appropriate gratings and order filters.  A globar at 1400 K
        was used in the 2-25 micrometer range; shortward of 2.0
        micrometers a tungsten source at 2700 K was used.  The
        reference detector was a thermocouple for all but the 0.4-1.1
        micrometer range, where a calibrated silicon photodiode was
        used.  Out-of-band measurements were made by replacing the
        spectrometer grating with a plane mirror and ir materials
        having known cutoff and cuton wavelengths.  Flux calibration
        of the IRTM was performed under a simulated space environment
        using a vacuum chamber operated typically at a pressure of
        1.E-6 Torr.  The IRTM was operated by means of a console
        which simulated the interfaces and functions of the
        spacecraft FDS.  A minicomputer was used to provide all
        operational sequences and modes.  Data were recorded on
        magnetic tape for subsequent computer processing.  The
        calibration fixture consisted of two identical blackbodies,
        one located in front of the space port and maintained at
        liquid nitrogen temperature and the other in front of the
        planet port and adjustable in temperature from 77 K to 350K;
        eleven settings from 140 K to 330 K were used.  Blackbody
        temperatures were measured with platinum resistance
        thermometers having an absolute accuracy of +/- 0.1 degrees
        C.  traceable to the National Bureau of Standards.  The
        digitizer used in the test console provided ten times the
        resolution of the FDS digitizer, thus making the digitizing
        uncertainty during calibration insignificant compared to the
        noise.  The calibration data thus produced are IRTM output in
        digitization level (DN) as a function of blackbody
        temperature.  Radiometrically measured internal reference
        surface temperatures showed close agreement (+/- 0.5 degrees
        C.) with those measured independently with a thermister.  The
        IRTM temperature was controlled by regulating the temperature
        of a mounting base plate and the thermal shield inside the
        vacuum chamber.  Calibration was performed at 10 degrees C.
        spacing across the range of operating temperatures expected
        during flight.  Typical IRTM channel response to scene
        brightness temperatures is shown in Fig.  8 of
        CHASE_ETAL_1978.  The one-sample noise on the thermal
        channels is less than 1 DN except for the 15 micrometer
        channel where it is about 2.5 DN.  The dynamic ranges of the
        surface thermal bands are based on temperatures expected for
        the Martian surface.  The 300 K maximum chosen for the A
        telescope might be exceeded by midday summer temperatures,
        but temperatures above the 310-K limit of the B telescope
        should not be exceeded unless active volcanic areas were
        found; temperatures to 320 K and 330 K could be measured by
        the 9 micrometer and 7 micrometer bands.  The 15 micrometer
        band dynamic range was set quite large as its resolution is
        noise limited rather than digitization limited.
 
 
    Instrument Optics 'A'
    =====================
      Telescope Diameter             : 0.058000
      Telescope F Number             : 3.500000
      Telescope Focal Length         : 0.203000
      Telescope Resolution           : 0.005100
      Telescope T Number             : UNK
      Telescope Transmittance        : UNK
 
 
      Description
      -----------
        The A telescope (17.7-24 micrometer) is shown schematically
        in Fig.  3 of CHASE_ETAL_1978.  It is an f/3.5, 20.3-cm focal
        length Cassegrainian design with an aperture diameter of
        5.8-cm., spherical surfaces, and, except for mirror
        materials, is identical to the B and C telescopes.  By using
        relatively slow fore optics, degradation of filter sharpness
        normally caused by operating an interference filter in a low
        f-number beam is negligible.  The focal plane contains a
        field-defining aperture plate with seven 0.107-cm diameter
        holes arranged in a chevron pattern.  The fields of view thus
        defined are nested with those of the MAWD and imaging systems
        (Fig.  4 of CHASE_ETAL_1978).  Behind each hole in the field
        stop plate is a lens which produces a 0.0254-cm diam image of
        the telescope aperture on the detector, which itself is about
        the same size.  The final optical speed at the detector is
        f/1.  Optical materials used in the four telescopes are shown
        in Table II, and the resulting spectral response is shown in
        Fig.  5 of CHASE_ETAL_1978.  Mirrors are made of hot-pressed
        uncoated zinc oxide for both primary and secondary mirrors.
        The reststrahlen reflection properties of ZnO are the major
        factors in the A telescope spectral response.  Minimizing
        extrafield sensitivity (EFS) was an important aspect of the
        optical design since on previous Mariner radiometers EFS
        contribution seriously compromised observations of scenes
        near large temperature contrasts (points near the planetary
        limb and polar caps).  During instrumentation development,
        IRTM image quality was determined in two angular regions.  In
        the near-field region, a laboratory collimator and ir source
        were used to measure the 2-D spatial response out to 16-mrad
        diam (three fields of view).  Point source field of view
        measurements in this region are shown in Fig.  6 of
        CHASE_ETAL_1978.  For far field measurements, sensitivity
        constraints dictated an approach in which the fraction of
        energy within a given angular annulus is measured.  A 30.5-cm
        diam, concentric grooved, blackbody plate with a series of
        restricting apertures was used at several distances (30.5-cm,
        140-cm, and 610-cm) to define angular response regions from
        about one field of view out to 1-rad diam.  That is, with the
        telescope focused at 610-cm, a disk 3.17-cm in diameter at
        that distance defines one half-response field of view (5.2
        mrad).  The source was held at 95 degrees C.  by a
        heater/regulator and integral water jacket.  To prevent
        difficulties with atmospheric transmission, the entire
        apparatus was contained in a polyethylene bag flushed with
        dry N2.  The EFS problem was more severe for the longer
        wavelength A telescope than the others, possibly owing to the
        higher reflectance at longer wavelengths of the black paint
        used inside the telescope.  Tests using this apparatus led to
        several telescope modifications designed to reduce EFS (see
        Fig.  3 of CHASE_ETAL_1978): (1) A postfocal baffle was
        placed between the field lens and the detectors to confine
        energy to the sensitive area of the detectors.  (2) A spider
        baffle, added to the outer edges of the secondary mirror
        support spider, was designed to reduce reflection off the
        sides of the spider legs.  (3) A cone baffle coated with CTL
        15 black paint was placed on the central dead spot of the
        secondary mirror.  This was designed to prevent focal plane
        reflections from falling on the detectors.  Of these three
        modifications, only the cone baffle gave significant
        improvement, although all three were incorporated in the
        design.  These results of the final EFS measurements are
        shown in Fig.  6 of CHASE_ETAL_1978.  The calculated response
        due to diffraction and the measured values are shown.  The
        integrated EFS response between 12 mrad and 1-rad diam was
        about 4%.  Of this, about 1/2 is due to diffraction effects.
        The effect of response outside of the nominal field of view
        can be estimated directly from data obtained on scans across
        the hot (subsolar) planetary limb.  Assuming that the
        response is circularly symmetric, and all evidence indicates
        this to be closely followed, the signature of a half space
        would also be symmetric.  A plot of fractional energy derived
        from a Viking 1 IRTM scan across the sunlit limb of Mars is
        shown in Fig.  6 of CHASE_ETAL_1978.  The alignment was
        determined using a 20.3-cm (8-in.) collimator to illuminate
        all four telescopes with a small source of high temperature
        blackbody radiation.  Measurements were taken simultaneously
        in twenty-eight channels over a 1.5-mrad square grid pattern.
        For each channel, a parabolic ellipsoid was fit to data where
        the measured intensity was more than 10% of the peak
        intensity in that channel.  The alignment of each telescope
        was ascertained by combining the center of response so
        determined for the seven channels in the telescope.  This
        procedure allowed for the alignment of the four telescopes to
        be determined with an estimated precision of 0.1 mrad.  The
        back of the secondary mirror of the B telescope was
        aluminized and used as the alignment reference for this
        procedure and for instrument alignment on the spacecraft.
        The instrument pointing direction was verified in the same
        manner just prior to planetary encounter using Mars as a
        5-mrad diam source and using the science platform motion to
        generate a 5-mrad spaced grid.  The in-flight alignment is
        shown in Fig.  4 of CHASE_ETAL_1978.
 
 
    Instrument Optics 'B'
    =====================
      Telescope Diameter             : 0.058000
      Telescope F Number             : 3.500000
      Telescope Focal Length         : 0.203000
      Telescope Resolution           : 0.005100
      Telescope T Number             : UNK
      Telescope Transmittance        : UNK
 
 
      Description
      -----------
        The A telescope (17.7-24 micrometer) is shown schematically
        in Fig.  3 of CHASE_ETAL_1978.  It is an f/3.5, 20.3-cm focal
        length Cassegrainian design with an aperture diameter of
        5.8-cm., spherical surfaces, and, except for mirror
        materials, is identical to the B and C telescopes.  By using
        relatively slow fore optics, degradation of filter sharpness
        normally caused by operating an interference filter in a low
        f-number beam is negligible.  The focal plane contains a
        field-defining aperture plate with seven 0.107-cm diameter
        holes arranged in a chevron pattern.  The fields of view thus
        defined are nested with those of the MAWD and imaging systems
        (Fig.  4 of CHASE_ETAL_1978).  Behind each hole in the field
        stop plate is a lens which produces a 0.0254-cm diam image of
        the telescope aperture on the detector, which itself is about
        the same size.  The final optical speed at the detector is
        f/1.  Optical materials used in the four telescopes are shown
        in Table II, and the resulting spectral response is shown in
        Fig.  5 of CHASE_ETAL_1978.  The B mirror is made of
        aluminized and SiO overcoated fused silica.  The spectral
        bandpass of the ir channel is determined by interference
        bandpass filter and an AR coated detector lense.  The
        out-of-band response for the B telescope is less than 0.1% of
        full scale for an object of 1.E-6 the radiance of a 5800-K
        blackbody, the level expected for reflectance from the
        subsolar region of Mars.  Minimizing extrafield sensitivity
        (EFS) was an important aspect of the optical design since on
        previous Mariner radiometers EFS contribution seriously
        compromised observations of scenes near large temperature
        contrasts (points near the planetary limb and polar caps).
        During instrumentation development, IRTM image quality was
        determined in two angular regions.  In the near-field region,
        a laboratory collimator and ir source were used to measure
        the 2-D spatial response out to 16-mrad diam (three fields of
        view).  Point source field of view measurements in this
        region are shown in Fig.  6 of CHASE_ETAL_1978.  For far
        field measurements, sensitivity constraints dictated an
        approach in which the fraction of energy within a given
        angular annulus is measured.  A 30.5-cm diam, concentric
        grooved, blackbody plate with a series of restricting
        apertures was used at several distances (30.5-cm, 140-cm, and
        610-cm) to define angular response regions from about one
        field of view out to 1-rad diam.  That is, with the telescope
        focused at 610-cm, a disk 3.17-cm in diameter at that
        distance defines one half-response field of view (5.2 mrad).
        The source was held at 95 degrees C.  by a heater/regulator
        and integral water jacket.  To prevent difficulties with
        atmospheric transmission, the entire apparatus was contained
        in a polyethylene bag flushed with dry N2.  Tests using this
        apparatus led to several telescope modifications designed to
        reduce EFS (see Fig.  3 of CHASE_ETAL_1978): (1) A postfocal
        baffle was placed between the field lens and the detectors to
        confine energy to the sensitive area of the detectors.  (2) A
        spider baffle, added to the outer edges of the secondary
        mirror support spider, was designed to reduce reflection off
        the sides of the spider legs.  (3) A cone baffle coated with
        CTL 15 black paint was placed on the central dead spot of the
        secondary mirror.  This was designed to prevent focal plane
        reflections from falling on the detectors.  Of these three
        modifications, only the cone baffle gave significant
        improvement, although all three were incorporated in the
        design.  These results of the final EFS measurements are
        shown in Fig.  6 of CHASE_ETAL_1978.  The calculated response
        due to diffraction and the measured values are shown.  The
        integrated EFS response between 12 mrad and 1-rad diam was
        about 4%.  Of this, about 1/2 is due to diffraction effects.
        The effect of response outside of the nominal field of view
        can be estimated directly from data obtained on scans across
        the hot (subsolar) planetary limb.  Assuming that the
        response is circularly symmetric, and all evidence indicates
        this to be closely followed, the signature of a half space
        would also be symmetric.  A plot of fractional energy derived
        from a Viking 1 IRTM scan across the sunlit limb of Mars is
        shown in Fig.  6 of CHASE_ETAL_1978.  The alignment was
        determined using a 20.3-cm (8-in.) collimator to illuminate
        all four telescopes with a small source of high temperature
        blackbody radiation.  Measurements were taken simultaneously
        in twenty-eight channels over a 1.5-mrad square grid pattern.
        For each channel, a parabolic ellipsoid was fit to data where
        the measured intensity was more than 10% of the peak
        intensity in that channel.  The alignment of each telescope
        was ascertained by combining the center of response so
        determined for the seven channels in the telescope.  This
        procedure allowed by the alignment of the four telescopes to
        be determined with an estimated precision of 0.1 mrad.  The
        back of the secondary mirror of the B telescope was
        aluminized and used as the alignment reference for this
        procedure and for instrument alignment on the spacecraft.
        The instrument pointing direction was verified in the same
        manner just prior to planetary encounter using Mars as a
        5-mrad diam source and using the science platform motion to
        generate a 5-mrad spaced grid.  The in-flight alignment is
        shown in Fig.  4 of CHASE_ETAL_1978.
 
 
    Instrument Optics 'C'
    =====================
      Telescope Diameter             : 0.058000
      Telescope F Number             : 3.500000
      Telescope Focal Length         : 0.203000
      Telescope Resolution           : 0.005100
      Telescope T Number             : UNK
      Telescope Transmittance        : UNK
 
 
      Description
      -----------
        The A telescope (17.7-24 micrometer) is shown schematically
        in Fig.  3 of CHASE_ETAL_1978.  It is an f/3.5, 20.3-cm focal
        length Cassegrainian design with an aperture diameter of
        5.8-cm., spherical surfaces, and, except for mirror
        materials, is identical to the B and C telescopes.  The focal
        plane contains a field-defining aperture plate with seven
        0.107-cm diameter holes arranged in a chevron pattern.  The
        fields of view thus defined are nested with those of the MAWD
        and imaging systems (Fig.  4 of CHASE_ETAL_1978).  Behind
        each hole in the field stop plate is a lens which produces a
        0.0254-cm diam image of the telescope aperture on the
        detector, which itself is about the same size.  The final
        optical speed at the detector is f/1.  Optical materials used
        in the four telescopes are shown in Table II, and the
        resulting spectral response is shown in Fig.  5 of
        CHASE_ETAL_1978.  Mirrors are made of aluminized and SiO
        overcoated fused silica except for the A telescope, which
        uses hot-pressed uncoated zinc oxide for both primary and
        secondary mirrors.  The spectral bandpass of the other ir
        channels is determined by interference bandpass filters and
        AR coated detector lenses.  The out-of-band response for the
        B and C telescopes is less than 0.1% of full scale for an
        object of 1.E-6 the radiance of a 5800-K blackbody, the level
        expected for reflectance from the subsolar region of Mars.
        The A band has less than 0.1% response for wavelengths less
        than 16 micrometer, and wavelengths longer than 30 micrometer
        are limited by the Irtran 6 field lens.  Minimizing
        extrafield sensitivity (EFS) was an important aspect of the
        optical design since on previous Mariner radiometers EFS
        contribution seriously compromised observations of scenes
        near large temperature contrasts (points near the planetary
        limb and polar caps).  During instrumentation development,
        IRTM image quality was determined in two angular regions.  In
        the near-field region, a laboratory collimator and ir source
        were used to measure the 2-D spatial response out to 16-mrad
        diam (three fields of view).  Point source field of view
        measurements in this region are shown in Fig.  6 of
        CHASE_ETAL_1978.  For far field measurements, sensitivity
        constraints dictated an approach in which the fraction of
        energy within a given angular annulus is measured.  A 30.5-cm
        diam, concentric grooved, blackbody plate with a series of
        restricting apertures was used at several distances (30.5-cm,
        140-cm, and 610-cm) to define angular response regions from
        about one field of view out to 1-rad diam.  That is, with the
        telescope focused at 610-cm, a disk 3.17-cm in diameter at
        that distance defines one half-response field of view (5.2
        mrad).  The source was held at 95 degrees C.  by a
        heater/regulator and integral water jacket.  To prevent
        difficulties with atmospheric transmission, the entire
        apparatus was contained in a polyethylene bag flushed with
        dry N2.  Tests using this apparatus led to several telescope
        modifications designed to reduce EFS (see Fig.  3 of
        CHASE_ETAL_1978): (1) A postfocal baffle was placed between
        the field lens and the detectors to confine energy to the
        sensitive area of the detectors.  (2) A spider baffle, added
        to the outer edges of the secondary mirror support spider,
        was designed to reduce reflection off the sides of the spider
        legs.  (3) A cone baffle coated with CTL 15 black paint was
        placed on the central dead spot of the secondary mirror.
        This was designed to prevent focal plane reflections from
        falling on the detectors.  Of these three modifications, only
        the cone baffle gave significant improvement, although all
        three were incorporated in the design.  These results of the
        final EFS measurements are shown in Fig.  6 of
        CHASE_ETAL_1978.  The calculated response due to diffraction
        and the measured values are shown.  The integrated EFS
        response between 12 mrad and 1-rad diam was about 4%.  Of
        this, about 1/2 is due to diffraction effects.  The effect of
        response outside of the nominal field of view can be
        estimated directly from data obtained on scans across the hot
        (subsolar) planetary limb.  Assuming that the response is
        circularly symmetric, and all evidence indicates this to be
        closely followed, the signature of a half space would also be
        symmetric.  A plot of fractional energy derived from a Viking
        1 IRTM scan across the sunlit limb of Mars is shown in Fig.
        6 of CHASE_ETAL_1978.  The alignment was determined using a
        20.3-cm (8-in.) collimator to illuminate all four telescopes
        with a small source of high temperature blackbody radiation.
        Measurements were taken simultaneously in twenty-eight
        channels over a 1.5-mrad square grid pattern.  For each
        channel, a parabolic ellipsoid was fit to data where the
        measured intensity was more than 10% of the peak intensity in
        that channel.  The alignment of each telescope was
        ascertained by combining the center of response so determined
        for the seven channels in the telescope.  This procedure
        allowed by the alignment of the four telescopes to be
        determined with an estimated precision of 0.1 mrad.  The back
        of the secondary mirror of the B telescope was aluminized and
        used as the alignment reference for this procedure and for
        instrument alignment on the spacecraft.  The instrument
        pointing direction was verified in the same manner just prior
        to planetary encounter using Mars as a 5-mrad diam source and
        using the science platform motion to generate a 5-mrad spaced
        grid.  The in-flight alignment is shown in Fig.  4 of
        CHASE_ETAL_1978.
 
 
    Instrument Optics 'D'
    =====================
      Telescope Diameter             : 0.037000
      Telescope F Number             : 5.500000
      Telescope Focal Length         : 0.203000
      Telescope Resolution           : UNK
      Telescope T Number             : UNK
      Telescope Transmittance        : UNK
 
 
      Description
      -----------
        The D telescope has a reduced aperture of 3.7 cm and a focal
        length of f/5.5.  By using relatively slow fore optics,
        degradation of filter sharpness normally caused by operating
        an interference filter in a low f-number beam is negligible.
        The focal plane contains a field-defining aperture plate with
        seven 0.107-cm diam holes arranged in a chevron pattern.  The
        fields of view thus defined are nested with those of the MAWD
        and imaging systems (Fig.  4 of CHASE_ETAL_1978).  Behind
        each hole in the field stop plate is a lens which produces a
        0.0254-cm diam image of the telescope aperture on the
        detector, which itself is about the same size.  The final
        optical speed at the detector is f/1.  Optical materials used
        in the four telescopes are shown in Table II, and the
        resulting spectral response is shown in Fig.  5 of
        CHASE_ETAL_1978.  Mirrors are made of aluminized and SiO
        overcoated fused silica except for the A telescope, which
        uses hot-pressed uncoated zinc oxide for both primary and
        secondary mirrors.  The spectral bandpass of the other ir
        channels is determined by interference bandpass filters and
        AR coated detector lenses.  The transmission elements of the
        D telescope insure that it is thermally blind.  Special
        coatings on the D telescope mirrors were used to obtain a
        reasonably gray response to solar radiation.  Minimizing
        extrafield sensitivity (EFS) was an important aspect of the
        optical design since on previous Mariner radiometers EFS
        contribution seriously compromised observations of scenes
        near large temperature contrasts (points near the planetary
        limb and polar caps).  During instrumentation development,
        IRTM image quality was determined in two angular regions.  In
        the near-field region, a laboratory collimator and ir source
        were used to measure the 2-D spatial response out to 16-mrad
        diam (three fields of view).  Point source field of view
        measurements in this region are shown in Fig.  6 of
        CHASE_ETAL_1978.  For far field measurements, sensitivity
        constraints dictated an approach in which the fraction of
        energy within a given angular annulus is measured.  A 30.5-cm
        diam, concentric grooved, blackbody plate with a series of
        restricting apertures was used at several distances (30.5-cm,
        140-cm, and 610-cm) to define angular response regions from
        about one field of view out to 1-rad diam.  That is, with the
        telescope focused at 610-cm, a disk 3.17-cm in diameter at
        that distance defines one half-response field of view (5.2
        mrad).  The source was held at 95 degrees C.  by a
        heater/regulator and integral water jacket.  To prevent
        difficulties with atmospheric transmission, the entire
        apparatus was contained in a polyethylene bag flushed with
        dry N2.  The EFS problem was more severe for the longer
        wavelength A telescope than the others, possibly owing to the
        higher reflectance at longer wavelengths of the black paint
        used inside the telescope.  Tests using this apparatus led to
        several telescope modifications designed to reduce EFS (see
        Fig.  3 of CHASE_ETAL_1978): (1) A postfocal baffle was
        placed between the field lens and the detectors to confine
        energy to the sensitive area of the detectors.  (2) A spider
        baffle, added to the outer edges of the secondary mirror
        support spider, was designed to reduce reflection off the
        sides of the spider legs.  (3) A cone baffle coated with CTL
        15 black paint was placed on the central dead spot of the
        secondary mirror.  This was designed to prevent focal plane
        reflections from falling on the detectors.  Of these three
        modifications, only the cone baffle gave significant
        improvement, although all three were incorporated in the
        design.  These results of the final EFS measurements are
        shown in Fig.  6 of CHASE_ETAL_1978.  The calculated response
        due to diffraction and the measured values are shown.  The
        integrated EFS response between 12 mrad and 1-rad diam was
        about 4%.  Of this, about 1/2 is due to diffraction effects.
        The effect of response outside of the nominal field of view
        can be estimated directly from data obtained on scans across
        the hot (subsolar) planetary limb.  Assuming that the
        response is circularly symmetric, and all evidence indicates
        this to be closely followed, the signature of a half space
        would also be symmetric.  A plot of fractional energy derived
        from a Viking 1 IRTM scan across the sunlit limb of Mars is
        shown in Fig.  6 of CHASE_ETAL_1978.  The alignment was
        determined using a 20.3-cm (8-in.) collimator to illuminate
        all four telescopes with a small source of high temperature
        blackbody radiation.  Measurements were taken simultaneously
        in twenty-eight channels over a 1.5-mrad square grid pattern.
        For each channel, a parabolic ellipsoid was fit to data where
        the measured intensity was more than 10% of the peak
        intensity in that channel.  The alignment of each telescope
        was ascertained by combining the center of response so
        determined for the seven channels in the telescope.  This
        procedure allowed by the alignment of the four telescopes to
        be determined with an estimated precision of 0.1 mrad.  The
        instrument pointing direction was verified in the same manner
        just prior to planetary encounter using Mars as a 5-mrad diam
        source and using the science platform motion to generate a
        5-mrad spaced grid.  The in-flight alignment is shown in Fig.
        4 of CHASE_ETAL_1978.
 
 
    Instrument Mode 'FIXED PLANET'
    ==============================
      Instrument Power Consumption : 6.000000
 
 
      In sections
      -----------
        IRTM
 
 
      Description
      -----------
        Other than power on or power off, the only command options
        for the IRTM controlled the motion of the scan mirror.  This
        mirror could be commanded to 3 positions, separated by 90
        degrees; PLANET, SPACE, and REFERENCE.  In the PLANET
        position, data were acquired in all 28 channels.  In SPACE,
        the zero-radiance level was reset to near the bottom of the
        dynamic range.  In the REFERENCE position, gain calibration
        data was obtained using both a grooved blackbody at ambient
        instrument temperatureand a small lamp and hemispherical
        diffuser for the solar telescope.  The REFERENCE position was
        also the 'safe' position, used when the instrument was turned
        off.  In the FIXED PLANET mode, the first 0,2, or 4 ICKs
        could be housekeeping data while the mirror was in motion to
        the planet position.  Thereafter the instrument reported
        planet data untill the next command was received.
 
 
    Instrument Mode 'FIXED REFERENCE'
    =================================
      Instrument Power Consumption : 6.000000
 
 
      In sections
      -----------
        IRTM
 
 
      Description
      -----------
        Other than power on or power off, the only command options
        for the IRTM controlled the motion of the scan mirror.  This
        mirror could be commanded to 3 positions, separated by 90
        degrees; PLANET, SPACE, and REFERENCE.  In the PLANET
        position, data were acquired in all 28 channels.  In SPACE,
        the zero-radiance level was reset to near the bottom of the
        dynamic range.  In the REFERENCE position, gain calibration
        data was obtained using both a grooved blackbody at ambient
        instrument temperatureand a small lamp and hemispherical
        diffuser for the solar telescope.  The REFERENCE position was
        also the 'safe' position, used when the instrument was turned
        off.
 
        In the FIXED REFERENCE mode, the mirror was commanded to the
        reference position; 0 to 5 ICKS of housekeeping data were
        possible while the mirror was in motion.  Thereafter, the
        instrument reported radiance readings or housekeeping data on
        alternate ICKs untill the next command was received.
 
 
    Instrument Mode 'FIXED SPACE'
    =============================
      Instrument Power Consumption : 6.000000
 
 
      In sections
      -----------
        IRTM
 
 
      Description
      -----------
        Other than power on or power off, the only command options
        for the IRTM controlled the motion of the scan mirror.  This
        mirror could be commanded to 3 positions, separated by 90
        degrees; PLANET, SPACE, and REFERENCE.  In the PLANET
        position, data were acquired in all 28 channels.  In SPACE,
        the zero-radiance level was reset to near the bottom of the
        dynamic range.  In the REFERENCE position, gain calibration
        data was obtained using both a grooved blackbody at ambient
        instrument temperatureand a small lamp and hemispherical
        diffuser for the solar telescope.  The REFERENCE position was
        also the 'safe' position, used when the instrument was turned
        off.  In the FIXED SPACE mode, the mirror was commanded to
        the space position from wherever it had been, with 2 ICKs of
        housekeeping data if the mirror was not already in the space
        position.  Thereafter the instrument reported space data
        until another command was received.
 
 
    Instrument Mode 'MODIFIED NORMAL'
    =================================
      Instrument Power Consumption : 6.000000
 
 
      In sections
      -----------
        IRTM
 
 
      Description
      -----------
        Other than power on or power off, the only command options
        for the IRTM controlled the motion of the scan mirror.  This
        mirror could be commanded to 3 positions, separated by 90
        degrees; PLANET, SPACE, and REFERENCE.  In the PLANET
        position, data were acquired in all 28 channels.  In SPACE,
        the zero-radiance level was reset to near the bottom of the
        dynamic range.  In the REFERENCE position, gain calibration
        data was obtained using both a grooved blackbody at ambient
        instrument temperatureand a small lamp and hemispherical
        diffuser for the solar telescope.  The REFERENCE position was
        also the 'safe' position, used when the instrument was turned
        off.
 
        A MODIFIED normal mode was also available, in which the only
        space view was the first of the cycle, followed by 243 ICKs
        of planet data.  In NORMAL mode, ICKs 1 and 2 were
        housekeeping data while the mirror moved to space.  ICK 3 was
        the space level before reset.  During ICK 4, the electronics
        for all channels were reset so that the sensed radiance
        (meant to be the cosmic background level of essentially zero
        radiance) yielded a data number (DN) of a few.  There was a
        filter on the reset so that the voltage change was only about
        2/3 of the way to the space radiance level; this smoothed out
        the zero setting, but also meant that several cycles were
        required to recover from a serious drift.  ICK 5 was still in
        the space position and yielded the DN response to space.  Ick
        6 and 7 were housekeeping data while the mirror moved to the
        reference position.  ICK 8 and 9 were the DN response to the
        reference surface; only the second reading was used in
        calibration of the solar channel to allow the lamp filament
        to warm up completely.  ICKs 10 through 13 were housekeeping
        data while the mirror moved to the planet position.  The 57
        ICKs 14-64 were planet data.  The 7 ICK cycle to space, with
        reset of the zero-radiance DN level in all channels, was
        repeated each 64 ICKs, beginning on ICKs 65, 129, and 193,
        with motion directly back to the planet position for another
        57 ICKs of planet data.
 
 
    Instrument Mode 'NORMAL'
    ========================
      Instrument Power Consumption : 6.000000
 
 
      In sections
      -----------
        IRTM
 
 
      Description
      -----------
        Other than power on or power off, the only command options
        for the IRTM controlled the motion of the scan mirror.  This
        mirror could be commanded to 3 positions, separated by 90
        degrees; PLANET, SPACE, and REFERENCE.  In the PLANET
        position, data were acquired in all 28 channels.  In SPACE,
        the zero-radiance level was reset to near the bottom of the
        dynamic range.  In the REFERENCE position, gain calibration
        data was obtained using both a grooved blackbody at ambient
        instrument temperature and a small lamp and hemispherical
        diffuser for the solar telescope.  The REFERENCE position was
        also the 'safe' position, used when the instrument was turned
        off.
 
        The NORMAL mode sequenced the pointing to PLANET most of the
        time, with pointing to SPACE at intervals of 64 ICKs, and to
        REFERENCE at intervals of 256 ICKs.  ICK is a one syllable
        acronym for 'incremental counter keeper' and represents 1.12
        second duration, the basic time interval of IRTM operation.
        It required 2 ICKs for the mirror to move 90 degrees and
        settle; whenever the mirror was in motion the downlink data
        contained housekeeping information about instrument status
        and detector voltage levels.
 
        In NORMAL mode, ICKs 1 and 2 were housekeeping data while the
        mirror moved to space.  ICK 3 was the space level before
        reset.  During ICK 4, the electronics for all channels were
        reset so that the sensed radiance (meant to be the cosmic
        background level of essentially zero radiance) yielded a data
        number (DN) of a few.  There was a filter on the reset so
        that the voltage change was only about 2/3 of the way to the
        space radiance level; this smoothed out the zero setting, but
        also meant that several cycles were required to recover from
        a serious drift.  ICK 5 was still in the space position and
        yielded the DN response to space.  Ick 6 and 7 were
        housekeeping data while the mirror moved to the reference
        position.  ICK 8 and 9 were the DN response to the reference
        surface; only the second reading was used in calibration of
        the solar channel to allow the lamp filament to warm up
        completely.  ICKs 10 through 13 were housekeeping data while
        the mirror moved to the planet position.  The 57 ICKs 14-64
        were planet data.  The 7 ICK cycle to space, with reset of
        the zero-radiance DN level in all channels, was repeated each
        64 ICKs, beginning on ICKs 65, 129, and 193, with motion
        directly back to the planet position for another 57 ICKs of
        planet data.
 
 
    Mounted On Platform 'SCAN PLATFORM'
    ===================================
      Cone Offset Angle              : 0.040000
      Cross Cone Offset Angle        : -0.060000
 
 
      Description
      -----------
        OFFSET ANGLE SCALED FROM FIGURE 4 OF CHASE_ETAL_1978; these
        were determined by scans across Mars during approach, when
        the angular diameter of the planet was 1.93 and 4.79
        milliradians (VO-1)
 

        