
 
 
    INSTRUMENT: VIKING METEOROLOGY INSTRUMENT SYSTEM
    SPACECRAFT: VIKING LANDER 1
 
 
    Instrument Information
    ======================
      Instrument Id                  : MET
      Instrument Host Id             : VL1
      Pi Pds User Id                 : SLHESS
      Instrument Name                : VIKING METEOROLOGY INSTRUMENT
                                       SYSTEM
      Instrument Type                : IN SITU METEOROLOGY
      Build Date                     : UNK
      Instrument Mass                : UNK
      Instrument Length              : UNK
      Instrument Width               : UNK
      Instrument Height              : UNK
      Instrument Serial Number       : UNK
      Instrument Manufacturer Name   : UNK
 
 
    Instrument Description
    ======================
      The Viking Meteorology Instrument System (VMIS) aboard the
      Viking Landers was designed to measure atmospheric temperature,
      atmospheric pressure, wind speed, and wind direction.  The VMIS
      consists of three major assemblies:
 
      1) The Meteorology Sensor Array (MSA), which supports
      the wind and temperature sensors and provides a
      housing for the low-level electronics.
      2) The Meteorology Boom Assembly (MBA), which
      provides the means for positioning the MSA after
      landing.  Following deployment of the MBA, the MSA is
      positioned nominally 1.6 meters above the ground, 0.7
      meter above the top of the Lander body, and about 0.3
      meter horizontally outward from the closest portion
      of the Lander body.
      3) The Meteorology Electronic Assembly (MEA), which
      provides power to the sensors and conditions the
      signals from the sensors so that the proper interface
      with the Lander electronic system is maintained.
 
      The individual sensors are described below (see
      CHAMBERLAIN_ETAL1976):
 
      The ambient pressure sensor is located in the Lander body near
      the MEA and has an external pressure line running to a port on
      the bottom plate of the Lander body.  The sensor is a
      stretched-diaphragm-type variable reluctance transducer that
      operates over a range of 0 to 18 millibars.
 
      The ambient temperature sensor consists of three
      Chromel-Constantan thermocouples wired in parallel.  It is
      capable of measuring over the entire range of expected martian
      temperatures with an accuracy of about 1.5 degrees Celsius.
 
      The reference temperature sensor was a platinum resistance
      thermometer mounted between the wind speed elements (see
      below).
 
      Wind speed is measured by means of two hot film anemometers
      oriented orthogonal to each other and lying in the horizontal
      plane.  These hot film elements were maintained at a nominal
      overheat temperature of 100 degrees Celsius above the air
      temperature measured by the reference temperature sensor.  The
      power required to maintain each anemometer at the specified
      temperature was a function of the component of the wind speed
      orthogonal to the element.
 
      The wind speed sensors also measure wind direction, but with a
      fourfold ambiguity.  Selection of the proper quadrant is
      accomplished by a quadrant sensor, consisting of a heated
      cylindrical platinum core (maintained at a 100 degrees Celsius
      overheat) surrounded by four thermocouple junctions at equal
      angles and distance from the core.  Thermocouples on opposite
      sides of the post comprised a thermocouple pair which was
      connected in series, allowing for measurement of the
      temperature differences across each pair.  These differences
      resulted from the thermal wake in the lee of the heated center
      core.  The quadrant sensor values were functions, though not
      single-valued, of wind speed.  The redundant wind speed and
      directional information provided by both the wind speed and
      quadrant sensors was combined using a least squares technique
      to give the best estimates of wind speed and direction.
 
 
    Science Objectives
    ==================
      The scientific objectives of the Viking Meteorology Instrument
      System (VMIS) are:
 
      DETECTION OF MEDIUM- AND SMALL-SCALE SYSTEMS: The length scales
      associated with convective processes (thermals, dust devils)
      and mesoscale processes (fronts, small dust storms) are
      considerably greater than the length scales that can be
      measured by the Lander.  These atmospheric systems can be
      detected and studied by the VMIS only when they pass the
      Landers and then only if the VMIS is taking data at the time
      the system passes.  It is an objective of the VMIS to measure
      the passage of such systems and to study their structures.
 
      MEASUREMENT OF SYNOPTIC- AND PLANETARY-SCALE SYSTEMS: With just
      two observation points, it will not be possible to study the
      structure of atmospheric systems on a planetary scale.  It will
      be possible, however, to determine some parameters about the
      general circulation that can provide useful constraints on
      theory.  Examples are measurements of large-scale winds,
      diurnal variations, and annual variations of atmospheric
      conditions.
 
      DETERMINATION OF THE STRUCTURE OF THE TURBULENT BOUNDARY LAYER:
      An objective of the VMIS is to measure temperature, wind speed,
      and wind direction in the turbulent boundary layer to
      understand better the vertical transport of properties such as
      momentum and heat throughout the diurnal cycle.
 
      MEASUREMENT OF THE LOCAL ENVIORNMENT: It is an objective to
      determine the meteorological environment in which the Landers
      operate and how that environment varies diurnally, seasonally,
      and annually.
 
      SUPPORT OF OTHER EXPERIMENTS: Measurements made by VMIS may aid
      in the analysis of data obtained by other Lander experiments.
      For example, wind gusts can shake the Lander and cause spurious
      signals to be generated by the seismometer.  Measurements of
      wind speed and direction may aid in analyzing images of clouds
      (dust and condensate), and temperature data will aid in
      interpretation of observations of condensates.
 
 
    Operational Considerations
    ==========================
      Failure of the quadrant sensor on Lander 1 sol 45 (see
      HESS_ETAL_1977) precludes unambiguous determination of wind
      direction without modification to the analysis techniques and
      software used to generate the wind direction data.
 
 
    Calibration Description
    =======================
      The Viking Meteorology Instrument System (VMIS), including
      software, was subjected to an extensive test program at the
      Langley Research Center.  The instrument was tested over the
      anticipated range of Martian wind speeds (directions 0 to 360
      degrees) and at temperatures as low as 200 degrees Kelvin.  The
      data from these tests were reduced using the flight software,
      and the results were compared to facility parameters that were
      reduced independently.  These tests indicate that the VMIS
      (including software, but not accounting for Lander flow-field
      effects) has an accuracy of about 10% in wind speed, 10% in
      wind direction, and 1.5 degree Kelvin in temperature.
 
      The pressure transducers were calibrated to approximately 0.01
      to 0.02 millibars accuracy over the ranges expected for martian
      atmospheric pressure variation.  Calibrations to accuracies
      greater than allowed by the digitizing system were accomplished
      by test support instrumentation.  Repeatability from year to
      year of the daily average pressures indicates that the
      transducers have remained stable to significantly better than
      0.04 millibars throughout the mission, possibly maintaining
      stabilities on the order of 0.01 millibars.
 
      It should be noted that the Meteorology Boom Assembly was
      positioned on the Lander to minimize the effects of the
      Lander-induced flow field.  The Lander effect is about 10% in
      wind direction and 10% in wind speed and is a function of wind
      direction and possibly local terrain.  Turbulence and other
      effects will further contribute to instrument error.  However,
      the overall accuracy is not expected to be substantially
      different from that determined in the test program.
 
 
    Section 'MET'
    =============
      Total Fovs                     : -32678
      Data Rate                      : UNK
      Scan Mode Id                   : UNK
      Sample Bits                    : UNK
 
 
      'MET' Detectors
      ---------------
        AMBIENT TEMPERATURE
        PRESSURE
        REFERENCE TEMP
        WIND QUADRANT
        WIND SPEED
 
 
      'MET' Electronics
      -----------------
        MEA
 
 
      In modes
      --------
        NORMAL
 
 
      'MET' Section Parameter 'PRESSURE'
      ----------------------------------
        The force per unit area applied to a body.
 
        Instrument Parameter Name      : PRESSURE
        Sampling Parameter Name        : TIME
        Instrument Parameter Unit      : MILLIBAR
        Minimum Instrument Parameter   : UNK
        Maximum Instrument Parameter   : UNK
        Noise Level                    : UNK
        Sampling Parameter Unit        : SECOND
 
 
      'MET' Section Parameter 'TEMPERATURE'
      -------------------------------------
        The temperature of a system is a measure of the heat content
        of the system, and determines if a system is in thermal
        equilibrium with other systems.
 
        Instrument Parameter Name      : TEMPERATURE
        Sampling Parameter Name        : TIME
        Instrument Parameter Unit      : DEGREES CELSIUS
        Minimum Instrument Parameter   : UNK
        Maximum Instrument Parameter   : UNK
        Noise Level                    : UNK
        Sampling Parameter Unit        : SECOND
 
 
      'MET' Section Parameter 'WIND VELOCITY'
      ---------------------------------------
        The velocity of a parcel of atmosphere in motion relative to
        a reference location.
 
        Instrument Parameter Name      : WIND VELOCITY
        Sampling Parameter Name        : TIME
        Instrument Parameter Unit      : METERS/SECOND
        Minimum Instrument Parameter   : UNK
        Maximum Instrument Parameter   : UNK
        Noise Level                    : UNK
        Sampling Parameter Unit        : SECOND
 
 
    Instrument Detector 'AMBIENT TEMPERATURE'
    =========================================
      Detector Type                  : THERMOCOUPLE
      Nominal Operating Temperature  : UNK
 
 
      Description
      -----------
        The ambient temperature sensor consists of three
        Chromel-Constantan thermocouples wired in parallel.  It is
        capable of measuring over the entire range of expected
        martian temperatures with an accuracy of about 1.5 degrees
        Celsius.
 
 
      Sensitivity
      -----------
        UNK
 
 
    Instrument Detector 'PRESSURE'
    ==============================
      Detector Type                  : VARIABLE RELUCTANCE
      Nominal Operating Temperature  : UNK
 
 
      Description
      -----------
        The ambient pressure sensor is located in the Lander body
        near the Meteorology Electronics Assembly and has an external
        pressure line running to a port on the bottom plate of the
        Lander body.  The sensor is a stretched-diaphragm-type
        variable reluctance transducer that operates over a range of
        0 to 18 millibars.
 
 
      Sensitivity
      -----------
        UNK
 
 
    Instrument Detector 'REFERENCE TEMP'
    ====================================
      Detector Type                  : RESIST THERMOMETER
      Nominal Operating Temperature  : UNK
 
 
      Description
      -----------
        The reference temperature sensor was a platinum resistance
        thermometer mounted between the wind speed elements on the
        Meteorology Sensor Assembly.  It was susceptible to radiation
        and conduction errors and the effects of the thermal plume of
        the wind sensor assembly, but corrections for these have been
        applied.  The residual error is believed to be less than 4
        degrees Celsius.(see HESS_ETAL_1977).
 
 
      Sensitivity
      -----------
        UNK
 
 
    Instrument Detector 'WIND QUADRANT'
    ===================================
      Detector Type                  : THERMOCOUPLE
      Nominal Operating Temperature  : UNK
 
 
      Description
      -----------
        Selection of the proper quadrant for the wind direction is
        accomplished by a quadrant sensor, consisting of a heated
        cylindrical platinum core (maintained at a 100 degrees
        Celsius overheat) surrounded by four thermocouple junctions
        at equal angles and distance from the core.  Thermocouples on
        opposite sides of the post comprised a thermocouple pair
        which was connected in series, allowing for measurement of
        the temperature differences across each pair.  These
        differences resulted from the thermal wake in the lee of the
        heated center core.  The quadrant sensor values were
        functions, though not single-valued, of wind speed.  The
        redundant wind speed and directional information provided by
        both the wind speed and quadrant sensors was combined using a
        least squares technique to give the best estimates of wind
        speed and direction.
 
 
      Sensitivity
      -----------
        UNK
 
 
    Instrument Detector 'WIND SPEED'
    ================================
      Detector Type                  : HOT-FILM ANEMOMETER
      Nominal Operating Temperature  : UNK
 
 
      Description
      -----------
        Wind speed is measured by means of two hot film anemometers
        oriented orthogonal to each other and lying in the horizontal
        plane.  These hot film elements were maintained at a nominal
        overheat temperature of 100 degrees Celsius above the air
        temperature measured by the reference temperature sensor.
        The power required to maintain each anemometer at the
        specified temperature was a function of the component of the
        wind speed orthogonal to the element.  The wind speed sensors
        also measure wind direction, but with a fourfold ambiguity.
        This ambiguity was resolved using a quadrant sensor (see
        detector description for the WIND QUADRANT sensor).
 
 
      Sensitivity
      -----------
        UNK
 
 
    Instrument Electronics 'MEA'
    ============================
 
      Description
      -----------
        The Meteorology Electronic Assembly (MEA) which provides
        power to the meteorology sensors and conditions the signals
        from the sensors so that the proper interface with the Lander
        electronic system is maintained.  It also provides the
        digital electronics necessary for data storage.  The key
        sections of the MEA are:
 
        1) COMMAND PROCESSOR receives, stores, and executes 24-bit
        serial commands generated by the Lander Guidance Control and
        Sequencing Computer (GCSC).
 
        2) DATA SEQUENCER AND MASTER CLOCK receives the 288 kHz
        Lander clock signal from the GCSC and generates the necessary
        internal clock frequencies for data commutation, sequencing,
        and buffer storage.
 
        3) WIND SPEED CONTROL ELECTRONICS maintains the hot-film wind
        sensors and the quadrant heater at 100 degrees Celsius above
        the measured reference temperature.  Measurements are made of
        the sensor pulse width, pulse height, and resistance to
        permit the computation of sensor power dissipation and
        temperature.
 
        4) TEMPERATURE SENSOR ELECTRONICS for the ambient temperature
        thermocouple, the reference junction film, and the quadrant
        sensor thermocouples all employ chopper-stabilized amplifiers
        to minimize drift.  The output of the amplifiers is fed to an
        integrating analog-to-digital converter (ADC).
 
        5) ANALOG-TO-DIGITAL CONVERTER (ADC) is a 10-bit, dual-slope
        converter that samples the signals as directed by the data
        sequencer.  The ADC has a range of 0 to 5 volt input with a
        resolution of 0.05% of full scale.
 
        6) MEMORY acts as a data buffer between the MEA and the Data
        Acquisition and Processor Unit (DAPU).  It has a storage
        capacity of 290 16-bit data words.
 
        7) AMBIENT PRESSURE SENSOR used for the parachute entry
        portion of the mission is also used by the VMIS.  The sensor
        is a stretched-diaphragm-type variable reluctance transducer.
        The sensor is located near the MEA and has an external
        pressure line running to a port on the bottom plate of the
        Lander body.
 
 
    Instrument Mode 'NORMAL'
    ========================
      Data Path Type                 : REALTIME
      Gain Mode Id                   : UNK
      Instrument Power Consumption   : UNK
 
 
      In sections
      -----------
        MET
 
 
      Description
      -----------
        The onboard Lander software was designed to provide a high
        degree of flexibility in the manner in which meteorology data
        are taken.  Under ground command, the sampling rate, duration
        over which a given sampling rate is maintained, the serial
        sequence of sampling rates and duration, the time between
        sampling sequences, the times and frequencies of sampling
        initiation, and the total amount of data taken per martian
        day (sol) can be varied.  Prior to landing, preplanned
        sequences were loaded into each Lander.  These consisted of
        modules with durations of of about 9, 20, and 39 minutes
        spaced nominally 1.5 hours apart throughout the sol.
        Intervals between individual samples were 4 and 8 seconds for
        the 9 minute modules, 4 seconds for the 39 minute modules,
        and 2 seconds for the 20 minute modules.  One complete
        sequence consisted of 18 modules.  Sixteen of these were 9
        minutes long and two, spaced about 12 hours apart, were of
        longer duration (one being 39 minutes long, the other 20
        minutes long).  The 18 periods were spaced so as to occupy
        somewhat more than a sol.  As a result, the pattern of
        sequences stepped ahead about 1.5 hours each sol.  This
        survey mode was adopted in order to define the diurnal cycle
        while moving long sequences through the sol, thus permitting
        a study of fluctuation characteristics at all portions of the
        diurnal cycle.
 
        Later in the mission, extended periods of rapid sampling
        (about 1 second intervals) were included to study boundary
        layer characteristics at as high a sampling rate as the
        system would allow.  In addition, various alterations were
        made in sampling rates, durations, and measurement periods to
        determine an optimal pattern for sampling the martian
        atmosphere.  It became evident that the total science return
        would be maximized by taking samples nearly continuously but
        at rates slow enough to satisfy mission constraints on total
        meteorology data.  This approach was followed during much of
        the remainder of the mission, except when precluded by
        mission requirements.
 
 
    Mounted On Platform 'METEOROLOGY BOOM ASSEMBLY'
    ===============================================
 
      Description
      -----------
        The Meteorology Boom Assembly (MBA) consists of a deployable
        boom which supports the Meteorology Sensor Array (MSA) in a
        stowed position during the launch, cruise, and entry portions
        of the mission.  A short time after landing, a
        pyrotechnic-activated pin releases the boom, which deploys
        and latches in an extended position.  Following deployment of
        the MBA, the MSA is positioned nominally 1.6 meters above the
        ground, 0.7 meter above the top of the Lander body, and about
        0.3 meter horizontally outward from the closest portion of
        the Lander body.  The Meteorology Sensor Array (MSA) supports
        the wind and temperature sensors and provides a housing for
        the low-level electronics, while the ambient pressure sensor
        is mounted within the Lander body (near the Meteorology
        Electronic Assembly).
 
 

        