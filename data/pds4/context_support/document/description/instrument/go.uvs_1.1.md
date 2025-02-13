
 
 
    Instrument Information
    ======================
      Instrument Id                  : UVS
      Instrument Host Id             : GO
      Instrument Name                : ULTRAVIOLET SPECTROMETER
      Instrument Type                : ULTRAVIOLET SPECTROMETER
 
 
    Instrument Description
    ======================
      The Galileo Ultraviolet Spectrometer investigation will use data
      obtained by two instruments.  The Ultraviolet Spectrometer (UVS)
      covers the wavelength range from 113 to 432 nm and was the original
      instrument selected for the Galileo Orbiter.  The Extreme
      Ultraviolet Spectrometer (EUV) was added to the Orbiter payload
      after the Challenger accident in 1986.  The UVS instrument is
      described in this document;  the EUV instrument will be discussed in
      a separate document.
 
      The UVS instrument consists of a Cassegrain telescope and an
      Ebert-Fastie scanning spectrometer.  Spectral scanning is
      accomplished using a fully programmable diffraction grating drive.
      Three separate photomultiplier detectors, located in the exit focal
      plane of the spectrometer, are used to cover the entire
      ultraviolet-near-visible spectrum from 113 to 432 nm.  Spectral
      scanning, instrument command and control, data formatting, and
      spacecraft interface are all normally controlled by a microprocessor
      within the instrument.  A hardware-controlled logic circuit, called
      Cold Start Mode, controls scanning at power on in the event normal
      commanding capability is inadvertently lost.  The UVS instrument
      components are summarized in Table 1 and detailed in subsequent
      sections of this document.
 
                                TABLE 1
                   Summary of Galileo UVS characteristics
      ---------------------------------------------------------------
      Telescope
              Focal length              250 mm
              Focal ratio               f/5
              Aperture                  50.3 mm x 52.8 mm
              Unobscured area           13.89 cm**2
 
      Spectrometer
              Focal length              125 mm
              Grating
                    Ruling              2400 lines / mm
                    Blaze angle         16.75 deg
 
      Detectors
             G channel                  EMR 510G-09 CsI photocathode
             F channel                  EMR 510F-06 CsTe photocathode
             N channel                  EMR 510N-06 KCsSB photocathode
 
      Nominal wavelength range
             G channel                  113.3 - 192.1 nm  second order
             F channel                  162.0 - 323.1 nm  first order
             N channel                  282.0 - 432.0 nm  first order
 
      Nominal resolution
             G channel                  0.67 nm
             F channel                  1.36 nm
             N channel                  1.27 nm
 
      Field of view
             G and N channels           0.1 x 1 deg
             F channel                  0.1 x 0.4 deg
 
      Exit slit solid angle
             G and N channels           3.05E-5 steradians
             F channel                  1.20E-5 steradians
 
      Instrument
             Mass                       5.2 kg
             Power consumption          2.4 W
             Heater power consumption   4 W
 
 
    Instrument Optics
    =================
      The optical design for the UVS telescope is a Dall-Kirkham
      configuration (elliptical primary mirror and spherical secondary
      mirror) with an effective focal length of 250 mm and a focal ratio
      of f/5.  In order to measure accurate limb profiles, the telescope
      has been equipped with an external sunshade and an extensive baffle
      system for rejection of off-axis scattered light.  The field of view
      is wavelength-dependent, being limited by the spectrometer entrance
      slit to 1 degree by 0.1 degree for two of the detectors (G channel -
      113 to 192 nm and N channel - 282 to 432 nm) and by one of the
      spectrometer exit slits to 0.4 degree by 0.1 degree for the third
      detector (F channel - 162 to 323 nm).  A bright object sensor (limb
      sensor) with a 1.5 degree full width half maximum (FWHM) field of
      view located below the telescope sunshade structure is used to
      protect the long wavelength detector during atmospheric limb
      observations.
 
 
    Spectrometer
    ============
      The spectrometer is a standard, 125 mm focal length, Ebert-Fastie
      design which uses a single spherical mirror as both collimator and
      camera and a plane diffraction grating.  A ruling density of 2400
      grooves per mm provides a first-order dispersion of 23.9 nm per mm
      and an average spectral resolution of 200 for a 0.43-mm-wide
      entrance slit (0.1 degree telescope field of view).
 
      Spectral scanning is accomplished by rotating a diffraction
      grating.  The UVS grating drive uses a moire fringe pattern,
      generated by overlaying two radially etched transmission gratings,
      to control the angular position of the grating.  One of the
      transmission gratings is fixed, and the other rotates with the
      diffraction grating housing.  The transmission gratings have a
      ruling of 1500 lines per 360 degree rotation resulting in a single
      cycle of 0.024 degree and a single phase increment step size of
      0.00375 degree.  Each grating step for the UVS is a sum of six phase
      increment steps or 0.0225 degree.  Thus a grating step results in a
      0.1-mm displacement of the spectrum in the spectrometer focal plane
      so that the spectrum is sampled on the average of 4 times per
      spectral resolution element.
 
      Three photomultiplier tubes, located behind three separate exit
      slits in the focal plane of the spectrometer record the spectrum in
      three overlapping wavelength ranges:  the far-ultraviolet detector
      (G channel) covers the wavelength range 113 to 192 nm,  the
      middle-ultraviolet detector (F channel) covers the wavelength range
      162 to 323 nm, and the near-ultraviolet-visible detector (N
      channel) covers the wavelength range 160 to 450 nm.  Each detector
      has its own high voltage power supply and pulse counting
      electronics, allowing for independent operation.  All three
      detectors are mounted in a single mechanical housing along with
      their high voltage power supplies and
      pulse-amplifier-discriminators.  The G and N photomultipliers are
      located directly behind their respective exit slits in the
      spectrometer housing.  Volume constraints require that the F
      photomultiplier be mounted above the slit plane and light is
      directed to it by a small two mirror periscope located behind the F
      channel exit slit.
 
 
    Instrument Detectors
    ====================
      Three EMR Photoelectric Corp. 510 photomultiplier tubes, located
      behind three separate exit slits in the focal plane of the
      spectrometer record the spectrum in three overlapping wavelength
      ranges.  Each detector has its own high voltage power supply and
      pulse counting electronics, allowing for independent operation.
      Photocathodes and windows for the detectors were chosen to optimize
      measurements in narrow spectral ranges.  The far-ultraviolet
      detector (G channel) is equipped with a magnesium fluoride window
      and a cesium iodide photocathode resulting in a solar blind detector
      with high sensitivity in the wavelength range 113 to 192 nm.  The
      middle-ultraviolet detector (F channel) is equipped with a quartz
      window to block radiation below 160 nm and a cesium telluride
      photocathode to suppress its response to radiation from wavelengths
      longer than 350 nm.  The near-ultraviolet-visible detector (N
      channel) is equipped with a quartz window and a bi-alkali
      photocathode and is sensitive to radiation in the wavelength range
      160 to 450 nm.  The Voyager instruments experienced high radiation
      noise, so additional aluminum shielding was added to the UVS
      instrument.
 
 
    Instrument Microprocessor and Electronics
    ======================================
      The UVS uses an RCA 1802 CMOS microprocessor for command parsing,
      spacecraft time recognition and synchronization, and instrument
      control.  In addition, the UVS design incorporates additional
      electronics called the Cold Start Logic (CSL) that places it into a
      cyclical F-G scan mode until microprocessor control is initiated by
      spacecraft command.  The instrument receives commands and spacecraft
      timing information via the Bus Adaptor and associated Direct Memory
      Access (DMA) logic.  The Bus Adaptor serves as the bi-directional
      interface between the Galileo spacecraft and the UVS.  Its circuitry
      serves to isolate the UVS electrically from the spacecraft and to
      allow for 8-bit information flow to and from the UVS.
 
 
    Science Objectives
    ==================
      The scientific objectives of the Galileo Ultraviolet Spectrometer
      (UVS) investigation include the following:
 
      (1)  THE INTERPLANETARY MEDIUM: By carrying out a systematic program
      of H and He measurements over the course of the mission, UVS will
      improve our knowledge of the interstellar wind (ISW) and of the
      processes that affect its passage through the solar system.
 
      (2)  VENUS:  The geometry of the Galileo flyby permits pole-to-pole
      and dawn-to-dusk measurements by the UVS of the abundance of SO2 in
      the cloud-top region, and of the abundance of H, O, C, and CO in the
      thermosphere.
 
      (3)  EARTH AND MOON:  The post-encounter passage near the subsolar
      point at long range allows the near-simultaneous measurement of
      pole-to-pole and dawn-to-dusk variations in the UV airglow and in
      reflected sunlight, allowing investigation of the global O/N2 ratio
      and the distribution of ozone.  It is also of interest to establish
      the Earth's UV albedo in the Schumann-Runge band region near and
      below 200 nm.  A search for a tenuous lunar atmosphere using the
      resonance emissions of H, O, and OH will address the question of the
      rate of bombardment of the Moon by small bodies, and of the fate of
      solar wind protons that strike the surface.  The flybys also allow
      the Earth-Moon system to be mapped, and these data contain an image
      from each encounter of the hydrogen geocorona from a unique sunward
      vantage point.
 
      (4)  ASTEROIDS:  The UVS measured the albedo of the asteroids Gaspra
      and Ida during flyby.  Spatial resolution on the asteroid surfaces
      was not possible, but their scattering properties as a function of
      phase angle were measured, and the presence of absorption features
      at wavelengths longer than 200 nm was determined.  At these and
      shorter wavelengths the asteroid's albedo may be directly compared
      to that of the Moon measured during the two Earth encounters.  The
      data returned from Gaspra and Ida were limited to a few spectra.
 
      (5)  JOVIAN CLOUDS AND HAZES:  The Galileo orbiting mission offers
      the opportunity to observe Jupiter's clouds and hazes repeatedly
      over a wide range of phase angle and wavelength.  Since its ability
      to examine small scattering angles is restricted by solar protection
      considerations, the contribution of UVS will be to determine the
      imaginary parts of the aerosols' refractive indices by obtaining the
      single-scattering albedo from photometric measurements.  It will
      sample the lower end of the aerosol size distribution due to its
      sensitivity down to 200 nm.  The distribution of aerosols with
      altitude will be measured in the stratosphere by measuring limb
      radiance profiles and in the troposphere by making nadir-to-limb
      scans.  Temporal variability in the properties of clouds and hazes
      will be investigated at time scales ranging from days to the
      duration of the mission.
 
      (6)  COMPOSITION AND CHEMISTRY OF THE JOVIAN STRATOSPHERE:  UVS will
      use reflectance spectroscopy during disc and limb scans to compile
      and inventory numerous hydrocarbons (such as methane, acetylene, and
      ethane) as a function of location and altitude.  UVS limb scans will
      yield stratospheric temperatures through the scale height of the
      signal from Rayleigh-scattered sunlight.
 
      (7)  JOVIAN THERMOSPHERE:  The thermosphere of Jupiter is
      characterized by unexpectedly high temperatures (of order 1100 K in
      the upper thermosphere) and by unexpectedly bright UV emissions from
      molecular hydrogen.  Lyman-alpha  emission from H shows an
      equatorial bulge that sometimes extends across the morning
      terminator.  None of these phenomena have been totally explained.  A
      careful study of spectral, horizontal, vertical, and diurnal and
      other time variations is an important objective for the Galileo UVS
      and EUV experiments, with the goal of gaining insight into these
      phenomena.
 
      (8)  JOVIAN AURORA:  Galileo's mostly equatorial orbits mean that
      the aurora will be observed near the northern or southern limbs,
      allowing excellent longitudinal resolution at the cost of lesser
      latitude resolution.  The spectral effects of atmospheric absorption
      will be enhanced.  Jupiter's rapid rotation will facilitate the
      determination of longitudinal dependencies of the emissions on each
      orbit.  The possibility of correlations between the aurora and
      conditions in the Io torus will be explored.  Galileo will also
      allow comparison of day-side and night-side auroral emissions.
 
      (9)  JOVIAN SATELLITES:  While close-range observations of Io by the
      UVS will be prevented by the radiation environment, Europa and the
      outer two Galilean satellites will be visited a few times in close
      encounters.  The Galileo UVS will measure and map the UV albedos of
      areas of these moons.  The measurements will be compared with those
      of the Moon and of the asteroids Gaspra and Ida.  The rich variety
      of surface terrain and materials will greatly expand our knowledge
      of the UV scattering properties of satellite surfaces.  The UVS will
      also look for evidence of tenuous and possibly sporadic atmospheres
      that might be produced by sublimation, sputtering by co-rotating
      plasma, or even eruptive events.
 
      (10) IO TORUS:  In conjunction with the EUV instrument, the UVS will
      measure the abundance and distribution of the neutral and ionized
      species existing in the Io torus.  Midnight/noon comparisons of the
      torus plasma will be possible.  The surface and atmospheric
      composition of Io and the nature and efficiency of escape and
      ionization processes, as well as the complex interaction of the
      ionized material with the magnetic and gravitational fields of
      Jupiter and with the rest of the magnetosphere, will be
      investigated.  The data are expected to reveal many dynamical
      aspects of the torus in addition to its composition.
 
      (11)  JOVIAN MAGNETOSPHERE:  There are many processes in the
      exosphere of Jupiter, on the constantly irradiated satellites, in
      the Io torus, and in the magnetosphere in general, that might
      provide sources of neutral atoms in the magnetosphere, including H
      and even OH in addition to oxygen and sulfur.  The UVS will search
      for such material at times when the radiation noise in the
      instrument is at a minimum.
 
      (12)  JOINT INVESTIGATIONS:  Collaborative studies are planned with
      the fields and particles investigators, with the goal to improve our
      understanding of the transportation of sulfur and oxygen ions from
      the Io plasma torus to their ultimate precipitation in the Jupiter
      auroral region.  Joint investigations with the Photopolarimeter
      Radiometer (PPR) experiment will help define the particulate
      properties of the Jupiter atmosphere, providing constraints on cloud
      particle size, shape, and composition.  Complementary UVS and PPR
      observations will also provide information about the spatial extent
      and altitude distributions of these clouds.  Properties of the
      satellite surfaces will be measured in cooperation with the Near
      Infrared Mapping Spectrometer (NIMS), the Solid State Imaging (SSI)
      instrument, and the PPR.  Scattering properties as well as
      ultraviolet absorbers, e.g., sulfur dioxide, will be measured to add
      leverage to our understanding of the Galilean satellites.
 
      (13) SHOEMAKER-LEVY 9:  The UVS obtained a unique 292 nm data set
      during the impact of the SL-9 fragment G, showing a brief 'flash'
      characterized by a brightness temperature near 8000K.
 
 
    Operational Considerations
    ==========================
      The UVS instrument has operated nominally since launch.
 
 
    Calibration Description
    =======================
      The Galileo UVS flight instrument  (Unit 0001) and engineering test
      instrument (Unit 0000) were calibrated on the ground before launch.
      Several documents and data files exist.  Inflight calibrations were
      also obtained.  The Principal Investigator requests that, until the
      end of the Galileo mission (EOM), any data users who wish
      calibration information beyond that provided in the literature
      should contact the UVS team.  Calibration documents include these
      references:
 
        1.  Galileo UVS Functional Requirement Document GLL-625-205,
            4-2034, Rev A.
 
        2.  'Galileo UVS Calibration Report, Preliminary Version',
            McClintock, W., March, 1989, Internal UVS Team document.
 
        3.  UVS/EUV instrument paper, Hord et al. (1992) [HORDETAL1992].
 
        4.  'Galileo UVS Calibration Report #2', McClintock, W., May
             1993, Internal UVS Team document.
 
      [HORDETAL1992] lists the types of calibrations done before launch.
      These include: instrument absolute sensitivity, telescope off-axis
      light rejection, spectrometer scattered light, instrument
      polarization, and spectral line shape and wavelength scale.
      Spacecraft interface measurements were also performed;  these
      included the limb sensor sensitivity and field of view and the
      alignment of the UVS optic axis.  Other calibrations included
      component calibration, such as the detector spatial response and
      sensitivity.
 
      The several inflight calibrations include cross-calibration
      activities between the UVS and EUV instruments during the
      Lyman-alpha All Sky mapping, Earth 1 and Earth 2 X-Cal observations,
      and several boresight observations of the platform teams during the
      cruise, Earth 1 and Earth 2 periods involving several stars.  Two
      UVS star calibrations are currently planned during the Orbital
      period.  Target stars have included: Alpha CMa, Eta UMa, Alpha Eri,
      Alpha Ori, and Alpha Leo.  The Earth's Moon was also used as a
      significant calibration observation during Earth 2.
 
 
    Instrument Modes
    ================
      The Galileo UVS has two operating modes: Cold Start and
      Microprocessor-controlled.  Microprocessor modes are different
      between pre-Jupiter, called Phase 1, operations and post-Jupiter
      operations, called Phase 2.  Generally there are also cruise and
      encounter modes discussed as well within the Phase 1 and Phase 2
      categories.  The instrument delivers 1008 bps to the Command and
      Data System (CDS) Bus in all modes.
 
      Cold Start is actually an automatic, or fail-safe, mode whereby
      hardware circuits control the instrument's grating, or scanning,
      operation.  Two full-wavelength spectral scans are performed using
      the F-channel detector in its standard wavelength range (162 to 323
      nm) and the G-channel detector over its standard wavelength range
      (113 to 192 nm).  One RIM of time, the standard Galileo 'frame',
      consists of fourteen spectra taken over 60.666 seconds.  Note two
      factors: 1) the grating moves in the up (ascending wavelength)
      direction during the first scan of a RIM and moves in the down
      (descending wavelength) direction for the second spectrum; 2) 84
      zeroes, representing one minor frame of 0.666 seconds, are produced
      by the instrument at the BEGINNING of each RIM.
 
      Microprocessor mode describes any time that the UVS microprocessor
      program is controlling the high voltage and/or grating operation of
      the instrument.  Originally designed for both recorded and real-time
      transmission operations, the microprocessor program was modified,
      slightly, for Phase 2 operations:  the major change for phase 2
      includes the use of a CDS buffer to sum pairs of spectra for various
      durations and then to dump the contents of the buffer to the
      real-time telemetry stream, with occasional backup to tape.
 
      PHASE 1
      -------
      The original Phase 1 microprocessor program, Version 5.1, allowed
      for full scan modes with one or two detectors being used during a
      scan pair, and for mini-scan modes where up to four selectable
      wavelength ranges from one detector could be scanned up and down
      during the 4.333 second scan period.  Two wavelength ranges were the
      maximum ever used in this mini-scan operation mode, however.  As
      noted above, the grating moves up and then down, even in mini-scan
      mode.  If two detectors were used in mini-scan mode then the
      detectors were changed only at RIM boundaries.
 
      During Venus, Earth 1 and Earth 2 the UVS made full rate real-time
      and recorded observations of these bodies.  They were generally full
      wavelength scanning observations.  Two mini-scan exceptions were the
      Venus observations and the Hydrogen line all-sky maps.
 
      PHASE 2
      -------
      Microprocessor Version 6.1 is used for all post-Jupiter UVS
      observations.  The two main distinctions of the Phase 2 UVS program
      from the Phase 1 are:  a)  whether the data are being recorded or
      are being summed (over time) by the CDS, and b) the movement of the
      grating drive when in mini-scan mode is different between V5.1 and
      V6.1 flight software.  In Phase 2 a Real Time Science (RTS) CDS
      routine was added to sum pairs of UVS spectra into a CDS internal
      buffer, called the Summation Buffer, in order to reduce the bits to
      ground.  There are three summation periods which are dependent on
      the downlink telemetry format.  The three periods are 29 RIMS, 59
      RIMS, and 1 RIM less than 24 hours.  In each case, one RIM is used
      to transfer and clear the buffer.  This RTS data format allows torus
      data to be obtained during the tape (cruise) playback periods.  In
      record mode the full UVS 1008 bps resolution is maintained on the
      tape.
 
      The order in which mini-scan wavelengths were sampled changed
      between Phase 1 and Phase 2.  In Phase 1 mini-scan mode, each
      mini-scan mode was performed for one spectrum and if a second, third
      or fourth different position was commanded then the next mode was
      performed in the next spectrum.  The next spectrum would contain the
      third and the next spectrum the fourth.  This 1-2-3-4 pattern would
      then repeat with the down wavelength pattern of 4-3-2-1.  A two
      position mini-scan would repeat 1-2-2-1.  In Phase 2, pairs of
      spectra always repeat in the up wavelength pattern.  The two
      position mini-scan becomes 1-2-1-2.  There are no third and fourth
      wavelengths in Phase 2.  This enables the CDS to sum consecutive
      pairs of UVS spectra in the Summation Buffer.  Phase 2 operations
      allow the second mini-scan to be executed with a different
      detector.
 
      In all cases, the detector and wavelength motion and direction are
      sensed within the UVS housekeeping data in the instrument 'fiducial'
      at the start of each spectrum.  The last byte of the microprocessor
      program contains the software version number (times 10).
 

        