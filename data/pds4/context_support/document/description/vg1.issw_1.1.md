
 
 
        INSTRUMENT: IMAGING SCIENCE SUBSYSTEM - WIDE ANGLE
        SPACECRAFT: VOYAGER 1
 
 
    Instrument Information
    ======================
      Instrument Id                  : ISSW
      Instrument Host Id             : VG1
      Pi Pds User Id                 : BASMITH
      Naif Data Set Id               : UNK
      Instrument Name                : IMAGING SCIENCE SUBSYSTEM - WIDE
                                         ANGLE
      Instrument Type                : VIDICON CAMERA
      Build Date                     : 1976-12-17
      Instrument Mass                : 13.300000
      Instrument Length              : 0.550000
      Instrument Width               : 0.200000
      Instrument Height              : 0.200000
      Instrument Serial Number       : SN06
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
      Subsystem (FDS) (Voyager Science and Mission Systems Handbook,
      1987, JPL D-498, an internal JPL document available from JPL
      vellum files).
 
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
      To make full scientific use of the image collection, it is
      necessary to understand the radiometric and geometric
      characteristics of the camera system and perform corrections to
      data.
 
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
      consisted of three parts: (1) component calibrations ('Voyager
      Imaging Science Subsystem Calibration Report' July 31, 1978, M.
      Benesh and P.  Jepsen, D618-802); (2) subsystem calibrations;
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
 
      A method for in-flight calibration was also available.  It
      consisted of a flat reflective surface which is located about 2
      m from the camera.  A flat-field light transfer curve can be
      constructed by orienting the spacecraft so that the plaque is
      illuminated by the sun and by photographing it at the proper
      exposure times.
 
      However, calibration data was collected but no new calibration
      files were generated during the Jupiter, Saturn, or Uranus
      encounters or their related cruise periods.
 
      Although the INSTRUMENT_PARAMETER_NAME has been provided as
      Radiance, the Voyager Experiment Data Record (EDR) data set has
      not been radiometrically corrected, and thus images do not
      represent radiance units.  In order to convert an image from
      Data Number (DN) to radiance units, the image must be
      calibrated.  Radiometric calibration files, and selected
      radiometrically corrected images are available through the
      Imaging Node.
 
 
    Section 'ISSW'
    ==============
      Total Fovs                     : 1
      Sample Bits                    : 8
 
 
      'ISSW' Detectors
      ----------------
        ISSW
 
 
      'ISSW' Electronics
      ------------------
        ISSW
 
 
      'ISSW' Filters
      --------------
        BLUE
        CLEAR
        GREEN
        METHANE-JST
        METHANE-U
        ORANGE
        SODIUM-D
        VIOLET
 
 
      'ISSW' Section Optic IDs
      ------------------------
        ISS-WA
 
 
      In modes
      --------
        IM10
        IM11
        IM12
        IM13
        IM14
        IM15
        IM2
        IM3
        IM4
        IM5
        IM6
        IM7
        IM8
        IM9
 
 
      'ISSW' Section FOV Shape 'SQUARE'
      ---------------------------------
        Section Id                     : ISSW
        Fovs                           : 1
        Horizontal Pixel Fov           : 0.003960
        Vertical Pixel Fov             : 0.003960
        Horizontal Fov                 : 3.169000
        Vertical Fov                   : 3.169000
 
 
      'ISSW' Section Parameter 'RADIANCE'
      -----------------------------------
        Radiance is the amount of energy per time per projected area
        per steradian.
 
        Instrument Parameter Name      : RADIANCE
        Sampling Parameter Name        : PIXEL
        Instrument Parameter Unit      : DIMENSIONLESS
        Noise Level                    : UNK
 
 
    Instrument Detector 'ISSW'
    ==========================
      Detector Type                  : VIDICON
      Detector Aspect Ratio          : 1.000000
      Minimum Wavelength             : 0.280000
      Maximum Wavelength             : 0.640000
      Nominal Operating Temperature  : 282.000000
 
 
      Description
      -----------
        The sensor used in the Voyager Imaging Science Subsystem
        (ISS) camera system is a 25 mm diameter magnetic deflection
        vidicon (number B41-003, General Electro-dynamics Co.).  The
        vidicon storage surface (target) is selenium sulphur and can
        store a high resolution (1500 TV lines) picture for over 100
        s at room temperature.  The active image area on the target
        is 11.14 x 11.14 mm.  Each frame consists of 800 lines with
        800 picture elements (pixels) per line, i.e., 1 pixel =14
        microns.  One frame requires 48 s for electronic readout.  In
        addition to the normal frame readout of 48 s (1:1), four
        extended frame-time modes of 2:1, 3:1, 5:1, and 10:1 are
        available by command.  Following readout, light flooding is
        used to remove any residual image that might remain from the
        previous frame.  At the end of light flooding, 14 erase
        frames are used to stabilize and prepare the vidicon target
        for the next exposure sequence (VGR ISS Calibration Report,
        1978, an internal JPL document available from JPL vellum
        files).
 
 
      Sensitivity
      -----------
        Calibration experiments show the gain map indicating higher
        sensitivity toward the top of the frame in a radial manner.
        Dark-current ratio results indicate a mean within
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
 
 
    Instrument Electronics 'ISSW'
    =============================
 
      Description
      -----------
        The ISS electronics consist of the vidicon support circuits
        and the signal chain.  The vidicon support circuits are the
        vertical and horizontal sweep circuits, and the various power
        supplies for the vidicon filament, and the focus and
        alignment coils.  The signal chain consists of the analog
        signal amplifiers, bandpass filters, and an eight bit
        analog-to-digital converter.  The digital output is sent to
        the Flight Data Subsystem for editing.
 
 
    Instrument Filter '0 - METHANE-JST'
    ===================================
      Filter Name                    : METHANE-JST
      Filter Type                    : INTERFERENCE
      Minimum Wavelength             : 0.614000
      Maximum Wavelength             : 0.624000
      Center Filter Wavelength       : 0.619000
 
 
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
 
 
    Instrument Filter '1 - BLUE'
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
 
 
    Instrument Filter '2 - CLEAR'
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
 
 
    Instrument Filter '3 - VIOLET'
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
 
 
    Instrument Filter '4 - SODIUM-D'
    ================================
      Filter Name                    : SODIUM-D
      Filter Type                    : INTERFERENCE
      Minimum Wavelength             : 0.588000
      Maximum Wavelength             : 0.590000
      Center Filter Wavelength       : 0.589000
 
 
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
 
 
    Instrument Filter '6 - METHANE-U'
    =================================
      Filter Name                    : METHANE-U
      Filter Type                    : INTERFERENCE
      Minimum Wavelength             : 0.536000
      Maximum Wavelength             : 0.546000
      Center Filter Wavelength       : 0.540000
 
 
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
 
 
    Instrument Filter '7 - ORANGE'
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
 
 
    Instrument Optics 'ISS-WA'
    ==========================
      Telescope Diameter             : 0.057143
      Telescope F Number             : 3.500000
      Telescope Focal Length         : 0.200465
      Telescope Resolution           : 0.000140
      Telescope Serial Number        : WAO-06
      Telescope T Number             : 4.140000
      Telescope T Number Error       : 0.020000
      Telescope Transmittance        : 0.800000
 
 
      Description
      -----------
        The wide-angle camera optics is a 200 mm.  focal length six
        element lens of the Petzval-type.  It consists of five
        elements plus an additional dust lens, located between the
        shutter and the vidicon.  The f stop number is 3.5 (VGR ISS
        Calibration Report, 1978,an internal JPL document available
        from JPL vellum files)
 
 
    Instrument Mode 'IM10'
    ======================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSW
 
 
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
        ISSW
 
 
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
        ISSW
 
 
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
        ISSW
 
 
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
        ISSW
 
 
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
        ISSW
 
 
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
        ISSW
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 1:1, full frame image, 800
        pix/line (Jupiter and Saturn only)
 
 
    Instrument Mode 'IM3'
    =====================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : LOW
      Instrument Power Consumption   : 14.000000
 
 
      In sections
      -----------
        ISSW
 
 
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
        ISSW
 
 
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
        ISSW
 
 
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
        ISSW
 
 
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
        ISSW
 
 
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
        ISSW
 
 
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
        ISSW
 
 
      Description
      -----------
        Scan rate (minor frame:line) is 3:1, centered, approx.  480
        pix/line (Jupiter and Saturn only)
 
 
    Mounted On Platform 'SCAN PLATFORM'
    ===================================
      Cone Offset Angle              : 0.031500
      Cross Cone Offset Angle        : 0.024700
      Twist Offset Angle             : 0.275000
 
 
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
 

        