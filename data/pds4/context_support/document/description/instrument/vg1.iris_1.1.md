
 
 
    INSTRUMENT: INFRARED INTERFEROMETER SPECTROMETER AND RADIOMETER
          HOST: VOYAGER 1
 
 
    Instrument Information
    ======================
      Instrument Id                  : IRIS
      Instrument Host Id             : VG1
      Instrument Name                : INFRARED INTERFEROMETER
                                        SPECTROMETER AND RADIOMETER
      Instrument Type                : INFRARED INTERFEROMETER
 
 
    Instrument Description
    ======================
      The Voyager IRIS instrument consists of a Michelson
      interferometer for measurements in the thermal infrared and a
      single channel radiometer that operates in the visible and near
      infrared.  The two components of the instrument share a 50 cm
      Cassegrain telescope with an effective focal length of 303.5
      cm.  The angular field of view is 0.25 degree.  Light passing
      through the telescope is divided into two beams by a dichroic
      mirror, with that longer than about 2.5 micrometers going to
      the infrared interferometer and radiation between 0.33 and 2
      micrometers going to the radiometer.  The effective spectral
      range of the interferometer is 180-2500 cm**-1 (4-55
      micrometers) and the apodized spectral resolution is 4.3
      cm**-1.  The beam splitter of the interferometer consists of a
      multilayer dielectric coating applied to a cesium iodide
      substrate.  The moving mirror is mounted on one end of a motor
      shaft; the moving mirror of an auxiliary reference
      interferometer is attached to the other end of the shaft.  A
      0.5852 micrometer neon line source is used for the reference
      interferometer; the signal from this unit is used by a phase
      comparator and digital sampling circuit to control the motor
      speed and to quantize the analog signal from the main IR
      detector.  The latter is a low impedance, Schwartz-type
      thermopile with a noise equivalent power (NEP) of about 2E-10
      Watt/Hz**1/2.
 
      The spectral response of the radiometer, which is designed to
      measure the broadband reflected solar radiation, is controlled
      by the dichroic mirror and an additional coating on the
      radiometer side of the mirror.  The radiometer detector is an
      eighteen-junction thermopile with an NEP of 4E-10 Watt/Hz**1/2.
      A sapphire window is placed in front of the detector to reject
      unwanted long-wave radiation that may result from temperature
      gradients within the instrument.  The signal from the
      radiometer detector is fed to a low noise, low-drift dc
      amplifier with a time constant of approximately 2.7 seconds,
      and then to three different output circuits.  The first circuit
      integrates the radiometer signal over the 45.6 seconds it takes
      to record an interferogram, thus providing the average of the
      reflected sunlight during the time the infrared spectrum is
      recorded.  The second and third circuits provide the analog
      signal from the radiometer as well as the signal amplified by a
      factor of 8.  These latter channels are sampled every 6 seconds
      and digitized.  The timing of the samples, and their
      relationship to events in a single-frame read out of an image
      are given in Table 1.
 
                     Table 1. IRIS and ISS Events
 
            Event                         ISS line count
            ____________________________  ___________________
            ISS frame start               0 (0 seconds)
            IRIS frame start              167
            IRIS interferogram start      179
            IRIS radiometer samples       217,317,...,717,
                                          and 017, 117 of
                                          the following frame
            IRIS pointing information #1  350
            IRIS interferogram peak       375 +/- 5
            IRIS pointing information #2  750
            ISS shutter close             767
            ISS frame end                 800(48 seconds)
 
 
      In order to visualize the effects of quantization uncertainties
      directly, it is sometimes useful to convert the radiometer
      watts at the detector back into data numbers (DN).  The
      relationships are:
 
            For Voyager 1:
 
               Sampled data (normal gain):
                  DNn = (WADn * 1e+08 - 2.51937) / 3.39426
               Sampled data (high gain):
                  DNh = (WADh * 1e+09 - 1.55472) / 4.26206
               Integrated data:
                  DNi = WADi / 1.42145 * 1e+09
 
            For Voyager 2:
 
               Sampled data (normal gain):
                  DNn = (WADn * 1e+08 - 6.33020) / 3.40070
               Sampled data (high gain):
                  DNh = (WADh * 1e+09 + 6.57589) / 4.24459
               Integrated data:
                  DNi = WADi / 1.42047 * 1e+09
 
 
      Pairs of baseline levels are averaged at the beginning and at
      the end of the 45.6 second integrations, occasionally resulting
      in half-integral DN values for the integrated radiometer data.
 
      Despite the stability of the calibration data (see below), a
      small systematic error may remain.  Comparison of spatially
      resolved IRIS observations of Jupiter and Saturn shows that
      reflectivities derived from Voyager 1 and Voyager 2 IRIS
      instruments are in the ratio 0.883:1.  An investigation was
      made of albedos of various objects (Jupiter, Io, Ganymede,
      Callisto, and Saturn), as determined using the two instruments.
      When compared to groundbased determinations, no systematic
      differences were apparent for either instrument, within the
      uncertainties.  Thus, a systematic error on the order of 10%
      may exist in the calibration of one or both of the IRIS
      instruments' radiometer systems.
 
      The temperature of the instrument is passively and actively
      controlled to operate at 200 +/- 0.5 K with a maximum drift of
      +/- 0.1 K/day.  A thermal radiator mounted on the
      interferometer cools the instrument by radiating to deep space.
      Three sets of proportionally controlled heaters provide fine
      thermal control for the primary telescope mirror, secondary
      mirror, and the interferometer.  It is necessary to maintain
      temperature differences between the three components to less
      than 0.1 K.  In addition, high-powered 'flash-off' heaters are
      available for increasing the instrument temperature by
      approximately 70 K.  These are controlled by command.  These
      have been used to warm the instrument during cruise periods to
      reverse a gradual change in the elastic properties of a
      silicone compound in the Michelson motor dampers and
      beam-splitter mounts.
 
 
    Science Objectives
    ==================
      The scientific objectives of the Voyager Infrared
      Interferometer Spectrometer (IRIS) investigation include the
      following:
 
     (1)  Identification and determination of the abundances of
          gaseous atmospheric constituents;
     (2)  Determination of the helium abundance of the
          atmospheres of the giant planets;
     (3)  Determination of the energy balances of the giant
          planets through measurements of their total thermal
          emissions and Bond albedos;
     (4)  Determination of the three dimensional thermal
          structure of the atmospheres of the giant planets and
          Titan;
     (5)  Inference of information on atmospheric dynamics;
     (6)  Inference of the infrared optical properties of
          clouds and hazes;
     (7)  Determination of the temperature, composition, and
          structure of the surfaces of satellites without
          atmospheres;
     (8)  Determination of the thermal characteristics of
          Saturn's rings.
 
      These objectives are accomplished through the analysis of
      measurements of thermal emission spectra and broad band
      reflected solar energy.
 
 
    Operational Considerations
    ==========================
      The IRIS instruments on Voyager 1 and 2 operated normally
      throughout the mission.  The infrared interferometers of both
      instruments experienced a temporal decrease in responsivity,
      believed to be due to a gradual stiffening in silicon compounds
      used in the mirror mounts and motor dampers.  However, this was
      partially reversed by using the flash off heaters to raise the
      temperature of the instrument periodically during cruise
      between encounters.
 
 
    Calibration Description
    =======================
      In-flight calibration of the data from the interferometer is
      accomplished using periodic observations of deep space along
      with a precise knowledge of the instrument cavity temperature.
      Use of the instrument temperature itself as a calibration point
      was necessitated because the large size of the telescope made
      the use of an on-board blackbody target impractical.
 
      The calibration is carried out for each wavenumber interval
      independently using I = B*(Tinst)*(C2 C1)/C2 where I is the
      calibrated planetary radiance, B*(Tinst) is the Planck radiance
      at the instrument temperature Tinst, and C2 and C1 are the
      spectral amplitudes measured while observing the planet and
      deep space, respectively.  This calibration technique requires
      that the interferometer and all elements within its field of
      view, including the telescope mirrors, apertures, and baffles,
      be at precisely the same temperature.  This condition is
      insured through the use of thermostatically controlled heaters.
      To minimize systematic errors from possible small changes in
      the instrument responsivity, the calibration must be updated as
      a function of time during the encounter.
 
      During an encounter, the deep space spectra for each day were
      averaged and a time corresponding to the average time was
      assigned to each average.  In addition to the daily averages, a
      grand average of all deep space spectra was calculated.  For
      each day a ratio spectrum consisting of the daily average power
      spectrum divided by the grand average power spectrum was used
      to scale the grand average instrument response to obtain the
      daily response.  Individual spectra were then calibrated using
      a linear interpolation.  The calibrated spectral radiances are
      expressed in Watt/cm**2/sr/cm**-1.
 
      Radiometer calibration consists of a verification of instrument
      stability by repeated determinations of t(target plate), based
      on observations of a diffusely scattering target plate mounted
      on the spacecraft.  The calibration conversion to Watts at the
      detector takes into account the detector response and
      electrical gains.  Observations of the target plate were
      carried out before and after each encounter with the exception
      of after the Voyager 2 Saturn encounter when jamming of the
      instrument scan platform caused the maneuver to be aborted.
 
      The long term behavior of the target calibration data for the
      two IRIS radiometers is presented in the following tables.  The
      observed target signal, corrected for offsets, and normalized
      for changes in heliocentric distance, has remained constant
      within quantization uncertainties throughout the mission.  In
      the absence of compensating changes in the target plate and the
      instrument, this implies excellent radiometer stability.  The
      arithmetic average of all target measurements, with a 1.5%
      uncertainty, is adopted as the normalized target signal for
      purposes of absolute calibration: 30960 +/- 460 DNi x AU**2;
      this differs slightly from the published value 31152 +/- 312
      DNi x AU**2 [PEARL&CONRATH1991].  The target signals for the
      integrating, x8 sampling, and x1 sampling radiometer data are
      in the ratio 24:8:1.
 
    Table 2. Target plate calibrations - integrating radiometer
             (integrating:high_gain:normal_gain=24:8:1)
 
                                 VG1 Jupiter     VG1 Jupiter
    Calibration Quantity         Pre-encounter   Post-encounter
    ____________________________ _______________ _______________
    Space before (DN)            9.5 +/- 1.0     17.0 +/- 1.5
    Space After (DN)             9.0 +/- 0.5     16.0 +/- 0.5
    Space weighted mean (DN) [1] 9.1 +/- 0.4     16.1 +/- 0.5
    Raw target (DN) [2]          1157.5 +/- 5.8  1029.5 +/- 5.1
    Adjusted target (DN) [3]     1148.4 +/- 5.8  1013.4 +/- 5.2
    Distance to Sun (10e+8 km)   7.67024         8.10236
    DN x AU**2                   30190. +/- 150. 29730. +/- 150.
 
 
                                 VG1 Saturn      VG1 Saturn
    Calibration Quantity         Pre-encounter   Post-encounter
    ____________________________ _______________ _______________
    Space before (DN)            19.5 +/- 0.5    16.25 +/- 0.25
    Space After (DN)             17.5 +/- 0.5    16.5 +/- 0.5
    Space weighted mean (DN) [1] 18.5 +/- 1.0    16.3 +/- 0.2
    Raw target (DN) [2]          415.5 +/- 2.1   328.5 +/- 1.6
    Adjusted target (DN) [3]     397.0 +/- 2.3   312.2 +/- 1.7
    Distance to Sun (10e+8 km)   12.93381        14.66979
    DN x AU**2                   29680. +/- 170. 30020. +/- 160.
 
 
                                 VG2 Jupiter     VG2 Jupiter
    Calibration Quantity         Pre-encounter   Post-encounter
    ____________________________ _______________ _______________
    Space before (DN)            59 +/- 2        49.0 +/- 0.5
    Space After (DN)             51 +/- 2        48.0 +/- 0.5
    Space weighted mean (DN) [1] 55 +/- 4        48.5 +/- 1.0
    Raw target (DN) [2]          1315.0 +/- 6.6  992.5 +/- 5.0
    Adjusted target (DN) [3]     1260.0 +/- 7.7  944.0 +/- 5.1
    Distance to Sun (10e+8 km)   7.43461         8.60397
    DN x AU**2 [4]               31120. +/- 190. 31230. +/- 170.
 
 
                                 VG2 Saturn      VG2 Saturn
    Calibration Quantity         Pre-encounter   Post-encounter
    ____________________________ _______________ _______________
    Space before (DN)            51.0 +/- 1.0          [5]
    Space After (DN)             47.0 +/- 1.5          [5]
    Space weighted mean (DN) [1] 49.0 +/- 2.0          [5]
    Raw target (DN) [2]          455.5 +/- 2.3         [5]
    Adjusted target (DN) [3]     406.5 +/- 3.0         [5]
    Distance to Sun (10e+8 km)   13.08739              [5]
    DN x AU**2 [4]               31110. +/- 230.       [5]
 
 
                                 VG2 Uranus      VG2 Uranus
    Calibration Quantity         Pre-encounter   Post-encounter
    ____________________________ _______________ _______________
    Space before (DN)            52.0 +/- 0.5    53.0 +/- 0.5
    Space After (DN)             51.5 +/- 1.0    53.0 +/- 0.5
    Space weighted mean (DN) [1] 51.9 +/- 0.4    53.0 +/- 0.5
    Raw target (DN) [2]          143.5 +/- 0.7   138.0 +/- 0.7
    Adjusted target (DN) [3]     91.6 +/- 0.8    85.0 +/- 0.9
    Distance to Sun (10e+8 km)   27.34484        28.88645
    DN x AU**2 [4]               30610. +/- 280. 31690. +/- 320.
 
 
                                 VG2 Neptune     VG2 Neptune
    Calibration Quantity         Pre-encounter   Post-encounter
    ____________________________ _______________ _______________
    Space before (DN)            53.0 +/- 0.5    52.5 +/- 0.5
    Space After (DN)             53.0 +/- 0.5    52.5 +/- 1.0
    Space weighted mean (DN) [1] 53.0 +/- 0.5    52.5 +/- 0.4
    Raw target (DN) [2]          95.8 +/- 0.5    86.3 +/- 0.8
    Adjusted target (DN) [3]     42.8 +/- 0.7    33.8 +/- 0.9
    Distance to Sun (10e+8 km)   39.6584         45.2993
    DN x AU**2 [4]               30040. +/- 500. 30940. +/- 800.
 
    ____________________________________________________________
    Notes:
    [1] Where the difference between pre-encounter and
        post-encounter measurements of space exceeds the random
        baseline variation, the average is taken as the
        arithmetic mean, with the difference as the uncertainty.
    [2] Considers the larger of 0.5% (estimated maximum possible
        nonlinearity) or the baseline variation as the
        uncertainty.
    [3] All uncertainties are considered uncorrelated in
        calculation of the adjusted target signal.
    [4] For Voyager 2 only, the adopted mean value of 30960 +/-
        460 is entered for all cases in the calibration files.
    [5] For Voyager 2 Saturn post-encounter, the instrument
        platform jammed so the calibration maneuver was aborted.
 
 
      Because the spectral transmission of the radiometer is not flat
      across the bandwidth, further calibration requires knowledge of
      the relative spectrum of each object observed.  The absolute
      reflectance of the Voyager 1 and 2 target plates are 0.502 +/-
      0.018 and 0.497 +/- 0.018, respectively.  A detailed
      description of a technique for calibrating the radiometer is
      given in [HANELETAL1981A].
 
 
    Instrument Detectors
    ====================
      The detector of the broadband reflected solar radiometer is an
      eighteen-junction thermopile with a 3 second thermal time
      constant and is operated at a temperature of 200 K.  The
      thermopile used with the broadband radiometer has a noise
      equivalent power of 4E-10 Watt/Hz**1/2.
 
      The detector of the infrared interferometer is a low-impedance
      Schwartz-type four-junction thermopile with a thermal time
      constant of 12 millisecond.  and is operated at a temperature
      of 200 K.  The thermopile used with the interferometer has a
      noise equivalent power of approximately 2E-10 Watt/Hz**1/2.
 
 
    Instrument Electronics
    ======================
      The bulk of the analog and all of the digital circuitry is
      located in an electronics module separate form the
      interferometer module.  The power supply is located in still
      another box.  Only elements that had to be close to detectors
      to minimize noise, such as the sensors for temperature
      measurements and controls, were located in the optics module.
      The electronics box contains timing and control elements,
      mirror drive circuitry, housekeeping monitors, thermal
      controllers, analog-to-digital converters, and spacecraft
      interface circuits.  The power module contains one primary and
      two auxiliary power supplies that convert spacecraft primary ac
      into dc voltages required to operate the instrument.  One of
      the auxiliary supplies is always on to maintain the instrument
      at the proper temperature.  The primary power supply is on only
      when the instrument is on during tests, calibrations and
      observation periods during planetary encounters.  Because of
      the requirement to pass through the Jovian radiation
      environment, hardened electronics components were used where
      possible.  The bulk of the instrument electronics consists of
      radiation-hardened integrated circuits.  A description of the
      electronics, along with a block diagram, is given in
      [HANELETAL1980A].
 
 
    Instrument Optics
    =================
      The Cassegrain telescope has a parabolic primary mirror 50 cm
      in diameter with a 7.62 cm hyperbolic secondary mirror, and an
      effective focal length of 303.5 cm and an F number of 6.07.  A
      dichroic mirror divides the beam from the telescope into two
      separate beams, one going to the infrared interferometer and
      the other to the broadband reflected solar radiometer.  The
      telescope mirrors and support structure, like most of the other
      mechanical parts of the instrument, are made of optical-grade
      beryllium.  The primary mirror is gold coated over a nickel
      plating.  The secondary mirror has an aluminum coating over the
      nickel plating, and this in turn is overcoated with silicon
      monoxide for protection.
 
 
    Instrument Offset
    =================
      The instrument and the associated electronics and power supply
      modules are bolted to the scan platform.  The telescope is
      approximately bore-sighted with the wide and narrow angle
      television cameras, and with the PPS and UVS instruments.
 
 
    Instrument Parameters
    =====================
      The following instrument parameters are measured.
 
      Sampled Visible Radiance - Series of 8 radiometer samples taken
      during a 48 second data frame with the high gain channel.  The
      quantity given is power at the detector in Watts.  (-1.0
      indicates data off the planet).
 
      Integrated Visable Radiance - The broadband, reflected solar
      radiometer signal integrated over the 45.6 seconds that IRIS
      data are taken within the 48 second data frame.  The quantity
      given is power at the detector in Watts.
 
      Thermal Radiance - Radiance (W cm-2 ster-1) within a 4.3 cm-1
      spectral interval.
 
 
    Instrument Modes
    ================
      The instrument possesses only one operating mode.  When turned
      on the instruments acquires one interferogram every 48 second
      data frame.  In addition data from the reflected solar
      radiometer are also obtained every data frame.  The latter
      consist of a measurement integrated over 45.6 seconds as well
      as 8 samples of both high and normal gain measurements
      distributed at 6 second intervals throughout the data frame.
 
 

        