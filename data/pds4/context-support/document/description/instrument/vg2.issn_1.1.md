
 
        INSTRUMENT: IMAGING SCIENCE SUBSYSTEM - NARROW ANGLE
        SPACECRAFT: VOYAGER 2
 
 
    Instrument Information
    ======================
      Instrument Id                  : ISSN
      Instrument Host Id             : VG2
      Pi Pds User Id                 : BASMITH
      Naif Data Set Id               : UNK
      Instrument Name                : IMAGING SCIENCE SUBSYSTEM -
                                       NARROW ANGLE
      Instrument Type                : VIDICON CAMERA
      Build Date                     : 1976-12-17
      Instrument Mass                : 22.060000
      Instrument Length              : 0.980000
      Instrument Width               : 0.250000
      Instrument Height              : 0.250000
      Instrument Serial Number       : SN05
      Instrument Manufacturer Name   : JET PROPULSION LABORATORY
 
 
    Instrument Description
    ======================
      The Voyager Imaging Science Subsystem (ISS) is a modified
      version of the slow scan vidicon camera designs that were used
      in the earlier Mariner flights.  The system consists of two
      cameras, a high resolution Narrow Angle (NA) camera and a lower
      resolution, more sensitive Wide Angle (WA) camera.  Unlike the
      other on board instruments, operation of the cameras is not
      autonomous, but is controlled by an imaging parameter table
      residing in one of the spacecraft computers, the Flight Data
      Subsystem (FDS) (Science and Mission Systems Handbook, 1987,
      JPL D-498, an internal JPL document available from JPL vellum
      files).
 
      The original mission was to Jupiter and Saturn.  Voyager
      surpassed expectations and Voyager 2 went on to encounter
      Uranus and Neptune.  As the Voyager mission progressed the
      objects photographed were further from the sun so they appear
      more faint even though longer exposures were used.  As the
      Voyager spacecrafts' distance from the Earth increases, the
      telecommunications capability at each encounter decreases.  The
      difference in capabilities from the Jupiter and Saturn
      encounters and that at Uranus and Neptune was considerable.
      The reduced telecommunications capability limits the number of
      data modes that imaging can use.  Because of the diminished
      brightness of the objects being photographed, longer exposure
      times were used, many beyond the stated maximum of 15.360
      seconds.  Longer exposure times were all 48-second increments
      added to the maximum.  In addition, the camera was slewed in
      order to avoid smeared imaging.  The light flood state (on/off)
      was independent of the instrument mode.
 
 
    Science Objectives
    ==================
      The overall objective of this experiment is exploratory
      reconnaissance of Jupiter, Saturn, Uranus, Neptune and their
      satellites and rings.  Such reconnaissance, at resolutions and
      phase angles unobtainable from Earth, provides much new data
      relevant to the atmospheric and/or surface properties of these
      bodies.  The experiment also has the following specific
      objectives: observe and characterize global circulation and
      meteorology; determine the horizontal and vertical structure of
      visible clouds; characterize the nature of any colored material
      which may be in clouds.
 
 
    Operational Considerations
    ==========================
      To make full scientific use of the image collection it is
      necessary to understand the radiometric and geometric
      characteristics of the camera system and perform corrections to
      the data.
 
      Each Voyager camera is unique in terms of its calibrated
      characteristics.  Each has intrinsic shading (spatially
      non-uniform output DNs from flat field target) and exhibits
      barrel distortions typical of TV cameras flown on previous
      planetary missions.  Because of these characteristics, the
      cameras were calibrated before launch.  The response of the
      pixels to known targets, illumination, exposures, etc.  was
      measured and Calibration Files were generated to remove
      radiometric and geometric distortions from the flight images.
      These Calibration Files and detailed information on their use
      are available through the Imaging Node.
 
 
    Calibration Description
    =======================
      The calibration program for the Voyager television cameras
      consisted of three parts: (1) component calibrations; ('Voyager
      Imaging Science Subsystem Calibration Report' July 31, 1978, M.
      Benesh and P.  Jepsen, D-618-802) (2) subsystem calibrations;
      and, (3) system calibrations.  In addition, provision was made
      for in-flight calibrations.  Component calibrations were
      carried out prior to camera assembly.  Important measurements
      include spectral transmittance of the lens and filters, actual
      exposure times and shading characteristics of the shutter, and
      pertinent electro-optical properties of the vidicon.  After the
      optics and sensor were assembled it was possible to run
      calibrations at the camera, or subsystem, level.  Particular
      activities accomplished during this period included radiometric
      calibrations, focal length measurement, determination of the
      modulation transfer function, measurement of the geometric
      distortion, and calibrations required for color reconstruction.
      System calibrations were conducted after the cameras were
      installed on the spacecraft.  Important tasks included
      measurement of the Field-Of-View alignment and verification of
      the flat-field light transfer characteristics.  Noise
      measurements were also made at the system level.
 
      A method for in-flight verification of the radiometric
      calibrations that were run on the ground is employed on the
      Narrow-Angle optics.  It is very similar to the scheme used on
      the Wide-Angle optics except that eight lamps are required.
      They are located just within the field of view around the
      periphery of the telescope aperture.  By either pulsing the
      lamps or leaving them on and varying the shutter exposure time
      a transfer curve may also be generated by using the calibration
      plaque.  The method is identical to that described for the
      wide-angle optics.  However, calibration data was collected but
      no new calibration files were generated during the Jupiter,
      Saturn, or Uranus encounters or their related cruise periods.
 
      Although the INSTRUMENT_PARAMETER_NAME has been provided as
      Radiance, the Voyager Experiment Data Record (EDR) data set has
      not been radiometrically corrected, and thus images do not
      represent radiance units.  In order to convert an image from
      Data Number (DN) to radiance units, the image must be
      calibrated.  Radiometric calibration files, and selected
      radiometrically corrected images are available through the
      Imaging Node.
 
 
    Section 'ISSN'
    ==============
      Total Fovs                     : 1
      Sample Bits                    : 8
 
 
      'ISSN' Detectors
      ----------------
        ISSN
 
 
      'ISSN' Electronics
      ------------------
        ISSN
 
 
      'ISSN' Filters
      --------------
        BLUE
        CLEAR
        CLEAR
        GREEN
        GREEN
        ORANGE
        ULTRAVIOLET
        VIOLET
 
 
      'ISSN' Section Optic IDs
      ------------------------
        ISS-NA
 
 
      In modes
      --------
        IM10
        IM11
        IM12
        IM13
        IM14
        IM15
        IM2
        IM26
        IM2A
        IM2C
        IM2W
        IM3
        IM4
        IM5
        IM6
        IM7
        IM8
        IM9
        IMK
        IMO
        IMQ
        OC3
        PB8
 
 
      'ISSN' Section FOV Shape 'SQUARE'
      ---------------------------------
        Section Id                     : ISSN
        Fovs                           : 1
        Horizontal Pixel Fov           : 0.000530
        Vertical Pixel Fov             : 0.000530
        Horizontal Fov                 : 0.424000
        Vertical Fov                   : 0.424000
 
 
      'ISSN' Section Parameter 'RADIANCE'
      -----------------------------------
        Radiance is the amount of energy per time per projected area
        per steradian.
 
        Instrument Parameter Name      : RADIANCE
        Sampling Parameter Name        : PIXEL
        Instrument Parameter Unit      : DIMENSIONLESS
        Noise Level                    : UNK
 
 
    Instrument Detector 'ISSN'
    ==========================
      Detector Type                  : VIDICON
      Detector Aspect Ratio          : 1.000000
      Minimum Wavelength             : 0.280000
      Maximum Wavelength             : 0.640000
      Nominal Operating Temperature  : 282.000000
 
 
      Description
      -----------
        The sensor used in the Voyager - Imaging Science Subsystem
        (ISS) camera system is a 25-mm diameter magnetic and
        deflection vidicon (number B41-003, General Electro-dynamics
        Company).  The vidicon storage surface (target) is selenium
        sulphur and can store a high resolution (1500 TV lines)
        picture for over 100 s at room temperature.  The active image
        area on the target is 11.14 x 11.14 mm.  Each frame consists
        of 800 lines with 800 picture elements (pixels) per line,
        i.e., 1 pixel =14 microns.  One frame requires 48 s for
        electronic readout.  In addition to the normal frame readout
        of 48 s (1:1), four extended frame-time modes of 2:1, 3:1,
        5:1, and 10:1 are available by command.  Following readout,
        light flooding is used to remove any residual image that
        might remain from the previous frame.  At the end of light
        flooding, 14 erase frames are used to stabilize and prepare
        the vidicon target for the next exposure sequence (VGR ISS
        Calibration Report, 1978, an internal JPL document available
        from JPL vellum files).
 
 
      Sensitivity
      -----------
        Calibration experiments show the gain map indicating higher
        sensitivity toward the top of the frame in a generally radial
        manner.  Dark-current ratio results indicate a mean within
        plus-or-minus 3% of the true linearity of the light transfer
        function.  The required accuracy of the light-transfer
        functions was plus-or-minus 5% of half-scale signal averaged
        over any randomly selected area of 10 contiguous pixels.
        This requirement was consistently met for all Imaging Science
        Subsystem (ISS) flight cameras.  The radiance of the used
        light cannons was supposed to be plus-or-minus 5% or better
        of the level to produce a half-scale signal.  This criterion
        was also met.  It is not clear whether the color spatial
        dependence is due to the vidicon, or whether the filters have
        varying transmissions.  In the latter case, the ratios would
        be independent of light level; and this has been observed to
        be the case for all flight cameras.  Moreover, vidicons have
        not shown scale variations of this magnitude in the past, so
        that it is easier to believe that they are due to the
        spectral filters rather than to the vidicons.  The color
        sensitivity is sufficient to require a separate decalibration
        file for each spectral filter, which has been done, but not
        gross enough to cause concern about the quality of the image
        itself (VGR ISS Calibration Report, 1978, an internal JPL
        document available from JPL vellum files).
 
 
    Instrument Electronics 'ISSN'
    =============================
 
      Description
      -----------
        The Imaging Science Subsystem (ISS) electronics consist of
        the vidicon support circuits and the signal chain.  The
        vidicon support circuits are the vertical and horizontal
        sweep circuits, and the various power supplies for the
        vidicon filament, and the focus and alignment coils.  The
        signal chain consists of the analog signal amplifiers,
        bandpass filters, and an eight bit analog-to-digital
        converter.  The digital output is sent to the Flight Data
        Subsystem (FDS) for editing.
 
 
    Instrument Filter '0 - CLEAR'
    =============================
      Filter Name                    : CLEAR
      Filter Type                    : ABSORPTION
      Minimum Wavelength             : 0.280000
      Maximum Wavelength             : 0.640000
      Center Filter Wavelength       : 0.460000
 
 
      Description
      -----------
        Spectral measurements at the manufacturer were taken on
        Beckman spectro-photometers, and verifications at Jet
        Propulsion Laboratory (JPL) were made with a Cary 14
        spectro-photometer.  Each test scan was run from 2000 to 7000
        Angstroms to check for eventual leaks outside the passband
        (VGR ISS Calibration Report, 1978, an internal JPL document
        available from JPL vellum files).  For spectral information
        on each filter, see Danielson, E.  G., et al.  Radiometric
        Performance of the Voyager Cameras, JGR, v.  86, Sept. 1981.
 
 
    Instrument Filter '1 - VIOLET'
    ==============================
      Filter Name                    : VIOLET
      Filter Type                    : INTERFERENCE
      Minimum Wavelength             : 0.350000
      Maximum Wavelength             : 0.450000
      Center Filter Wavelength       : 0.400000
 
 
      Description
      -----------
        Spectral measurements at the manufacturer were taken on
        Beckman spectro-photometers, and verifications at Jet
        Propulsion Laboratory (JPL) were made with a Cary 14
        spectro-photometer.  Each test scan was run from 2000 to 7000
        Angstroms to check for eventual leaks outside the passband
        (VGR ISS Calibration Report, 1978, an internal JPL document
        available from JPL vellum files).  For spectral information
        on each filter, see Danielson, E.  G., et al.  Radiometric
        Performance of the Voyager Cameras, JGR, v.  86, Sept. 1981.
 
 
    Instrument Filter '2 - BLUE'
    ============================
      Filter Name                    : BLUE
      Filter Type                    : INTERFERENCE
      Minimum Wavelength             : 0.430000
      Maximum Wavelength             : 0.530000
      Center Filter Wavelength       : 0.480000
 
 
      Description
      -----------
        Spectral measurements at the manufacturer were taken on
        Beckman spectro-photometers, and verifications at Jet
        Propulsion Laboratory (JPL) were made with a Cary 14
        spectro-photometer.  Each test scan was run from 2000 to 7000
        Angstroms to check for eventual leaks outside the passband
        (VGR ISS Calibration Report, 1978, an internal JPL document
        available from JPL vellum files).  For spectral information
        on each filter, see Danielson, E.  G., et al.  Radiometric
        Performance of the Voyager Cameras, JGR, v.  86, Sept. 1981.
 
 
    Instrument Filter '3 - ORANGE'
    ==============================
      Filter Name                    : ORANGE
      Filter Type                    : INTERFERENCE
      Minimum Wavelength             : 0.590000
      Maximum Wavelength             : 0.640000
      Center Filter Wavelength       : 0.615000
 
 
      Description
      -----------
        Spectral measurements at the manufacturer were taken on
        Beckman spectro-photometers, and verifications at Jet
        Propulsion Laboratory (JPL) were made with a Cary 14
        spectro-photometer.  Each test scan was run from 2000 to 7000
        Angstroms to check for eventual leaks outside the passband
        (VGR ISS Calibration Report, 1978, an internal JPL document
        available from JPL vellum files).  For spectral information
        on each filter, see Danielson, E.  G., et al.  Radiometric
        Performance of the Voyager Cameras, JGR, v.  86, Sept. 1981.
 
 
    Instrument Filter '4 - CLEAR'
    =============================
      Filter Name                    : CLEAR
      Filter Type                    : ABSORPTION
      Minimum Wavelength             : 0.280000
      Maximum Wavelength             : 0.640000
      Center Filter Wavelength       : 0.460000
 
 
      Description
      -----------
        Spectral measurements at the manufacturer were taken on
        Beckman spectro-photometers, and verifications at Jet
        Propulsion Laboratory (JPL) were made with a Cary 14
        spectro-photometer.  Each test scan was run from 2000 to 7000
        Angstroms to check for eventual leaks outside the passband
        (VGR ISS Calibration Report, 1978, an internal JPL document
        available from JPL vellum files).  For spectral information
        on each filter, see Danielson, E.  G., et al.  Radiometric
        Performance of the Voyager Cameras, JGR, v.  86, Sept. 1981.
 
 
    Instrument Filter '5 - GREEN'
    =============================
      Filter Name                    : GREEN
      Filter Type                    : INTERFERENCE
      Minimum Wavelength             : 0.530000
      Maximum Wavelength             : 0.640000
      Center Filter Wavelength       : 0.585000
 
 
      Description
      -----------
        Spectral measurements at the manufacturer were taken on
        Beckman spectro-photometers, and verifications at Jet
        Propulsion Laboratory (JPL) were made with a Cary 14
        spectro-photometer.  Each test scan was run from 2000 to 7000
        Angstroms to check for eventual leaks outside the passband
        (VGR ISS Calibration Report, 1978, an internal JPL document
        available from JPL vellum files).  For spectral information
        on each filter, see Danielson, E.  G., et al.  Radiometric
        Performance of the Voyager Cameras, JGR, v.  86, Sept. 1981.
 
 
    Instrument Filter '6 - GREEN'
    =============================
      Filter Name                    : GREEN
      Filter Type                    : INTERFERENCE
      Minimum Wavelength             : 0.530000
      Maximum Wavelength             : 0.640000
      Center Filter Wavelength       : 0.585000
 
 
      Description
      -----------
        Spectral measurements at the manufacturer were taken on
        Beckman spectro-photometers, and verifications at Jet
        Propulsion Laboratory (JPL) were made with a Cary 14
        spectro-photometer.  Each test scan was run from 2000 to 7000
        Angstroms to check for eventual leaks outside the passband
        (VGR ISS Calibration Report, 1978, an internal JPL document
        available from JPL vellum files).  For spectral information
        on each filter, see Danielson, E.  G., et al.  Radiometric
        Performance of the Voyager Cameras, JGR, v.  86, Sept. 1981.
 
 
    Instrument Filter '7 - ULTRAVIOLET'
    ===================================
      Filter Name                    : ULTRAVIOLET
      Filter Type                    : INTERFERENCE
      Minimum Wavelength             : 0.280000
      Maximum Wavelength             : 0.370000
      Center Filter Wavelength       : 0.325000
 
 
      Description
      -----------
        Spectral measurements at the manufacturer were taken on
        Beckman spectro-photometers, and verifications at Jet
        Propulsion Laboratory (JPL) were made with a Cary 14
        spectro-photometer.  Each test scan was run from 2000 to 7000
        Angstroms to check for eventual leaks outside the passband
        (VGR ISS Calibration Report, 1978, an internal JPL document
        available from JPL vellum files).  For spectral information
        on each filter, see Danielson, E.  G., et al.  Radiometric
        Performance of the Voyager Cameras, JGR, v.  86, Sept. 1981.
 
 
    Instrument Optics 'ISS-NA'
    ==========================
      Telescope Diameter             : 0.176500
      Telescope F Number             : 8.500000
      Telescope Focal Length         : 1.503490
      Telescope Resolution           : 0.000018
      Telescope Serial Number        : NAO-04
      Telescope T Number             : 11.830000
      Telescope T Number Error       : 0.090000
      Telescope Transmittance        : 0.600000
 
 
      Description
      -----------
        The Narrow-Angle camera optics is a 150mm focal length
        all-spherical, catadioptric cassegrain telescope (a modified
        MVM 1973 design) consisting of five elements plus an
        additional dust lens located between the shutter and the
        vidicon.  The f number is 8.5 (VGR ISS Calibration Report,
        1978, an internal JPL document available from JPL vellum
        files).
 
 
    Instrument Mode 'IM10'
    ======================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 1:1, centered frame, approx.
        160 pix/line (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM11'
    ======================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 5:1, centered frame, 800
        pix/line (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM12'
    ======================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 5:1, centered frame, approx.
        440 pix/line (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM13'
    ======================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 10:1, centered frame, 800
        pix/line (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM14'
    ======================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 1:1, centered frame, approx.
        80 pix/line (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM15'
    ======================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 2:1, centered frame, top read
        out in frame #1, bottom read out in frame #2, 800 pix/line
        (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM2'
    =====================
      Data Path Type                 : RECORDED DATA PLAYBACK
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 1:1, full frame image, 800
        pix/line (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM26'
    ======================
      Data Path Type                 : RECORDED DATA PLAYBACK
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 2:1, lines 271-536, 800
        pix/line (Neptune only)
 
 
    Instrument Mode 'IM2A'
    ======================
      Data Path Type                 : RECORDED DATA PLAYBACK
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 1:1, full frame, 800 pix/line
        (Uranus and Neptune only)
 
 
    Instrument Mode 'IM2C'
    ======================
      Data Path Type                 : RECORDED DATA PLAYBACK
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 5:1, full frame, 800
        pix/line, lines may be truncated (zero filled) on left or
        right - data dependent (Neptune only)
 
 
    Instrument Mode 'IM2W'
    ======================
      Data Path Type                 : RECORDED DATA PLAYBACK
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 1:1, full frame, 800
        pix/line, last 80 lines are zero (Neptune only)
 
 
    Instrument Mode 'IM3'
    =====================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 1:1, full frame, 800 pix/line
        (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM4'
    =====================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 1:1, centered frame, 608
        pix/line (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM5'
    =====================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 2:1, Top read out in frame
        #1, bottom read out in frame #2, 800 pix/line (Jupiter and
        Saturn only)
 
 
    Instrument Mode 'IM6'
    =====================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 1:1, centered frame, 440
        pix/line (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM7'
    =====================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 3:1, full frame, 800 pix/line
        (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM8'
    =====================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 1:1, centered frame, 272
        pix/line (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM9'
    =====================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 3:1, centered, approx.  480
        pix/line (Jupiter and Saturn only)
 
 
    Instrument Mode 'IMK'
    =====================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 10:1, centered frame, 800
        pix/line (Uranus and Neptune only)
 
 
    Instrument Mode 'IMO'
    =====================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 5:1, centered frame, 800
        pix/line (Uranus and Neptune only)
 
 
    Instrument Mode 'IMQ'
    =====================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 5:1, centered frame (Uranus
        only)
 
 
    Instrument Mode 'OC3'
    =====================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 3:1, lines 301-510, samples
        365-453 (Neptune only)
 
 
    Instrument Mode 'PB8'
    =====================
      Data Path Type                 : RECORDED DATA PLAYBACK
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSN
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 5:1 or 1:1, data dependent
        may be IM2A, IM2C, IM2W (Uranus and Neptune only)
 
 
    Mounted On Platform 'SCAN PLATFORM'
    ===================================
      Cone Offset Angle              : 0.000000
      Cross Cone Offset Angle        : 0.000000
      Twist Offset Angle             : 0.000000
 
 
      Description
      -----------
        The measurements recorded below are the coordinates
        representing the center of the Wide Angle Field Of View (FOV)
        in relation to the center of the Narrow Angle FOV.  As of
        5/26/88 the Voyager 2 scan platform offset values were
        updated and the removal of all extraneous offset values for
        VG1 and VG2 accomplished.  Only the most recently input
        values remain in the database for each spacecraft.  These
        values are effective for all periods of data inclusive from
        launch to present.  (June 7, 1989).

        