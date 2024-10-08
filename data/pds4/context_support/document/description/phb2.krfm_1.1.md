
 
    Instrument Overview
    ===================
    The KRFM instrument includes optics of the radiometer and
    spectrophotometer detectors, electronics, a power supply unit, a
    system for instrument control and protection. The radiometer records
    thermal radiation of the surface in 6 subranges from 5 to 50 micron.
    It serves to study the thermal physical properties (a thermal
    inertia parameter, and with its help - the regolith fracturing
    characteristics, rock outcrop on the surface, as well as heat
    capacity, heat conduction, regolith density dynamics of the surface
    temperature condition. The spectrophotometer has a range of 300-
    700nm subdivided into 9 intervals. The instrument is used to acquire
    the data on the regolith reflection properties in the near
    ultraviolet and visible ranges. The radiometer includes a two-mirror
    objective (Cassegrain system, its diameter is 115 mm, the focal
    length 230mm), a rotating mirror and a pyroelectric detector system.
    The rotating mirror can be set in one of the three positions with
    the step-by-step motor. It directs the radiation to the objective
    alternately from the outer space, from the black body model with the
    estimated temperature, and  from the object studied. The pyrodevice
    system incorporates a beam split hexahedral pyramid, a beam
    modulator, an optoelectronic synch pulse detector and 6 pyrodevices
    with the interference light filters. The spectrophotometer has an
    objective (its diameter is 14 mm, the focal length 37.5mm), a
    diaphragm to provide the given field of view, a collimater, a
    dispersing prism, a second objective, a multicomponent
    photodetector, a light beam modulator, an optoelectronic synch pulse
    detector and a calibration device.
 
    PDS1 Instrument Parameters
    ==========================
    PI_PDS_USER_ID          = L.KSANFOMALITY
    NAIF_DATA_SET_ID        = SLAXOR
    BUILD_DATE              = 1988
    INSTRUMENT_MASS         = 12.2<KG>
    INSTRUMENT_HEIGHT       = 0.42<M>
    INSTRUMENT_LENGTH       = 0.38<M>
    INSTRUMENT_WIDTH        = 0.36<M>
    INSTRUMENT_MANUFACTURER_NAME = GOSSTANDARD USSR
    INSTRUMENT_SERIAL_NUMBER = 05
 
    Scientific Objectives Summmary
    ==============================
    The scientific objectives of this experiment were as follows: in the
    spectral range 6 - 50 mm - the study of thermal physical properties
    and surface structure of Phobos and Mars - a physical mapping of the
    surface geomorphological features  (rocks , fractured soil, dust) -
    search for sites of endogenous heat release and permafrost regions
    on the mars surface - diurnal and seasonal thermal dynamics of mars
    surface and diurnal dynamics of Phobos - bolometric albedo of Phobos
    and Mars in the spectral range 320 - 600 nm - the photometric
    measurements in the near ultraviolet and visible spectral ranges
    (albedo measurements) - mineralogical composition of the Phobos and
    Mars surfaces derived from their reflection spectra - study of the
    aerosol phenomena characteristics in the Martian atmosphere.
 
    Instrument Calibration Description
    ==================================
    The radiometer diagonal mirror is turned during 20 s with a 6 min
    period toward the black body model, whose temperature is controlled.
    Then the mirror is turned during the same time toward the 'Cosmos'
    tube. To increase an accuracy of measurements radiation cooling of
    the black body model is envisaged. The temperature in the modulator
    and light detector chamber is also transmitted via the TV channel,
    the total number of thermal detectors is 4. The photometer uses the
    calibration device-light-emitting diode which operated during
    calibration and sends light pulses to the light detectors at
    frequency of 40 Hz. The time of the calibration is identical with
    that of the radiometer. In the ground-based processing of the
    experiment results some problems were revealed.  The protocols of
    the ground-based calibration poorly agreed with the acquired data,
    though the results of measurements were stable. An extra check
    showed that in the ground-based calibrations there can be systematic
    errors. For this reason a decision was made to use the earlier
    obtained of ground-based and airborne data for the Mars regions
    studied in order to refine the photometerreal sensitivity.
 
    Operational Considerations
    ==========================
    The reflected solar and intrinsic thermal radiation of the celestial
    body is recorded and transformed to electrical signals proportional
    to the flux. After the synch detectors generate the respective
    signals they are sent to the switches, edited with a microprocessor
    program, and sent to the unit for data exchange between the
    spacecraft and menury (Data scope is 8 Mbit per 1 measurement
    session).
 
    PDS1 Instrument Detector Parameters
    ===================================
    DETECTOR_ID             = RADIOMETER CH 1
    DETECTOR_TYPE           = PYROELECTRIC
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 4.8<MM>
    MAXIMUM_WAVELENGTH      = 6.4<MM>
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = The threshold sensitivity is 240 K.
 
    DETECTOR_ID             = RADIOMETER CH 2
    DETECTOR_TYPE           = PYROELECTRIC
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 6.1<MM>
    MAXIMUM_WAVELENGTH      = 7.8<MM>
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = The threshold sensitivity is 225 K.
 
    DETECTOR_ID             = RADIOMETER CH 3
    DETECTOR_TYPE           = PYROELECTRIC
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 7.2<MM>
    MAXIMUM_WAVELENGTH      = 9.3<MM>
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = The threshold sensitivity is 215 K.
 
    DETECTOR_ID             = RADIOMETER CH 4
    DETECTOR_TYPE           = PYROELECTRIC
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 9.2<MM>
    MAXIMUM_WAVELENGTH      = 13.6<MM>
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = The threshold sensitivity is 110 K.
 
    DETECTOR_ID             = RADIOMETER CH 5
    DETECTOR_TYPE           = PYROELECTRIC
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 14.3<MM>
    MAXIMUM_WAVELENGTH      = 15.9<MM>
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = The threshold sensitivity is 120 K.
 
    DETECTOR_ID             = RADIOMETER CH 6
    DETECTOR_TYPE           = PYROELECTRIC
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 16.5<MM>
    MAXIMUM_WAVELENGTH      = 49.0<MM>
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = The threshold sensitivity is 80 K.
 
    DETECTOR_ID             = PHOTOMETER CH 1
    DETECTOR_TYPE           = PHOTODIODE
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 0.315<MM>
    MAXIMUM_WAVELENGTH      = N/A
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = Threshold sensitivity 10E-14 W/Hz**0.5
 
    DETECTOR_ID             = PHOTOMETER CH 2
    DETECTOR_TYPE           = PHOTODIODE
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 0.328<MM>
    MAXIMUM_WAVELENGTH      = N/A
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = Threshold sensitivity 10E-14 W/Hz**0.5
 
    DETECTOR_ID             = PHOTOMETER CH 3
    DETECTOR_TYPE           = PHOTODIODE
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 0.346<MM>
    MAXIMUM_WAVELENGTH      = N/A
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = Threshold sensitivity 10E-14 W/Hz**0.5
 
    DETECTOR_ID             = PHOTOMETER CH 4
    DETECTOR_TYPE           = PHOTODIODE
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 0.363<MM>
    MAXIMUM_WAVELENGTH      = N/A
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = Threshold sensitivity 10E-14 W/Hz**0.5
 
    DETECTOR_ID             = PHOTOMETER CH 5
    DETECTOR_TYPE           = PHOTODIODE
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 0.410<MM>
    MAXIMUM_WAVELENGTH      = N/A
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = Threshold sensitivity 10E-14 W/Hz**0.5
 
    DETECTOR_ID             = PHOTOMETER CH 6
    DETECTOR_TYPE           = PHOTODIODE
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 0.445<MM>
    MAXIMUM_WAVELENGTH      = N/A
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = Threshold sensitivity 10E-14 W/Hz**0.5
 
    DETECTOR_ID             = PHOTOMETER CH 7
    DETECTOR_TYPE           = PHOTODIODE
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 0.488<MM>
    MAXIMUM_WAVELENGTH      = N/A
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = Threshold sensitivity 10E-14 W/Hz**0.5
 
    DETECTOR_ID             = PHOTOMETER CH 8
    DETECTOR_TIPE           = PHOTODIODE
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 0.550<MM>
    MAXIMUM_WAVELENGTH      = N/A
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = Threshold sensitivity 10E-14 W/Hz**0.5
 
    DETECTOR_ID             = PHOTOMETER CH 9
    DETECTOR_TYPE           = PHOTODIODE
    DETECTOR_ASPECT_RATIO   = 1.0
    MINIMUM_WAVELENGTH      = 0.600<MM>
    MAXIMUM_WAVELENGTH      = N/A
    NOMINAL_OPERATING_TEMPERATURE = 293<K>
    SENSITIVITY_DESC        = Threshold sensitivity 10E-14 W/Hz**0.5
 
    Instrument Electronics
    ======================
    The electronics unit consist of 9 photometer channels and 6
    radiometer channels, system of control for the photometer, modulator
    and radiometer mirror turning, units of analog-to digital converter
    commands,power supply, protection and temperature measurements
 
    PDS1 Instrument Optics Parameters
    =================================
    TELESCOPE_ID            = RADIOMETER TELESCOPE
    TELESCOPE_FOCAL_LENGTH  = 0.23<M>
    TELESCOPE_DIAMETER      = 0.115<M>
    TELESCOPE_F_NUMBER      = 1:2
    TELESCOPE_RESOLUTION    = 8.7e-03<RAD>
    TELESCOPE_TRANSMITTANCE = 0.32
 
    TELESCOPE_ID            = PHOTOMETER TELESCOPE
    TELESCOPE_FOCAL_LENGTH  = 0.0375<M>
    TELESCOPE_DIAMETER      = 0.014<M>
    TELESCOPE_F_NUMBER      = 1:2.7
    TELESCOPE_RESOLUTION    = 4.4e-03<RAD>
    TELESCOPE_TRANSMITTANCE = 0.78
 
    Instrument Mounting Description
    ===============================
    The instrument is a monoblock unit, includes optics and radiometer
    detectors at the top, and  a pressurized bay at the bottom. Options
    are mounted on the rigid base. The pressurized bay includes  a
    photometer, electronics, a command receiver, a power supply and
    protection unit . The KRFM optical optical axes are oriented along
    the x-axis.
 
    PDS1 Instrument Section Parameters
    ==================================
    SECTION_ID              = RADIOMETER
      DATA_RATE               = 8192<B/S>
      SAMPLE_BITS             = 12
      TOTAL_FOVS              = 0.5<DEGREE>
      INSTRUMENT_PARAMETER_NAME = LIGHT FLUX
      INSTRUMENT_PARAMETER_UNIT = WATT/(METER*METER)/STERADIAN
 
    SECTION_ID              = PHOTOMETER
      DATA_RATE               = 8192<B/S>
      SAMPLE_BITS             = 12
      TOTAL_FOVS              = 0.25<DEGREE>
      INSTRUMENT_PARAMETER_NAME = HEAT FLUX
      INSTRUMENT_PARAMETER_UNIT = WATT/(METER*METER)/STERADIAN
 
    Instrument Mode Description
    ===========================
    The heat and light flux measurements with an interrogation rate of
    1 s (normal) or 30 s (was not normally used).

        