
 
      Instrument Overview
      ===================
      VSK-FREGAT combines a threechannel television (TV) camera with two
      short-focal-length channels  and one longer-focal-length channel.
      The camera has charge-coupled  device (CCD) detectors  with
      photosensitive and  memory  sections  and uses an 'electronic
      shutter' technique. At the entrance of the cameras  a mirror is
      placed.  When  closed  it  protects the telescopes  and  permits
      photometric calibration from internal radiation sources.
      Whenopened, it permits nadir viewing of Phobos, while in two
      intermediatepositions it allows panoramic viewing of Phobos,  Mars
      and navigation targets.
 
      PDS1 Instrument Parameters
      ==========================
 
      INSTRUMENT_NAME         = VSK-FREGAT
      INSTRUMENT_TYPE         = CAMERA
      PI_PDS_USER_ID          = G.AVANESOV
      NAIF_DATA_SET_ID        = NAIF_VSK
      BUILD_DATE              = 1988
      INSTRUMENT_MASS         = 36.15<KG>
      INSTRUMENT_HEIGHT       = 790<MM>
      INSTRUMENT_LENGTH       = 928<MM>
      INSTRUMENT_WIDTH        = 517<MM>
      INSTRUMENT_MANUFACTURER_NAME = IKI (USSR & BULGARIA), ZKI (GDR)
      INSTRUMENT_SERIAL_NUMBER = LK4
 
      Scientific Objectives Summary
      =============================
      The scientific objectives of this experiment were the following:
      1) MARS surveying -  investigation of rock  composition  of  the
      surface,  cloudiness,  dust   amount  in atmosphere; 2) NAVIGATION
      - updating of Phobos' and  Deimos' orbits, their rotation periods,
      updating the data on Phobos  shape, detailed imaging of  the
      hovering  region,  spacecraft navigation;   3)  PHOBOS
      investigations  -  surface structure  studies,  geological
      studies, topographic, morphometric and stereo mapping.
 
      Instrument Calibration Description
      ==================================
      On-ground  radiometric  and geometric calibration was  performed.
      Radiometric calibration  of  the CCD array included calibration of
      the dark signal  as  a function  of exposure time and temperature,
      the  pixel  responsivity  as  a  function of exposure time and
      temperature, and the CCD array modulation transfer function.
      Geometric calibration consisted of: camera's telescope focusing,
      and establishing the CCD matrix homeplace position mounting and
      mirror  positions' mounting. In flight calibration was performed,
      consisting of:  internal radiometric calibration, using internal
      radiation sources,  geometric  and absolute radiometric
      calibration, using Canopus and Jupiter imaging.
 
      Operational Considerations
      ==========================
      VSK  produced about  40  images of Phobos, which cover most of its
      surface except for that  obscured by Mars, and a few images of
      Mars. The consecutive image productionmode was used for the
      instrument; imaging parameters and number of frames were defined
      by  the session's  program.  The  radiance  was focused by the
      telescope  on  the  CCD  array.  The  analog read-out  from  CCD
      is transformed via an electronic block, which includes A-D
      conversion to digital data image frames, which are stored on
      MORION mass memory. The stored data were played back and
      transmitted  to  the  Earth  in special sessions.
 
      PDS1 Instrument Detector Parameters
      ===================================
      DETECTOR_ID             = CCD1
      DETECTOR_TYPE           = CCD-ARRAY
      MINIMUM_WAVELENGTH      = 0.45<MICROMETER>
      MAXIMUM_WAVELENGTH      = 1.0<MICROMETER>
      NOMINAL_OPERATING_TEMPERATURE = 243<K>
      DETECTOR_DESC           =
        Calimantan-Phobos  type  CCD array with size 520*580,
        consisting  of  a photosensitive section, memory sections and
        two output registers. The photosensitive section  is opened for
        radiance and the memory section is closed. Each section contains
        290 rows with 520 CCD elements. Pixel  size  is  18*24
        micrometers.
      SENSITIVITY_DESC        =
        The  CCD  matrix  middle integral sensitivity is not less then 1
        volt/lux.
 
      DETECTOR_ID             = CCD2
      DETECTOR_TYPE           = CCD-ARRAY
      MINIMUM_WAVELENGTH      = 0.45<MICROMETER>
      MAXIMUM_WAVELENGTH      = 1.0<MICROMETER>
      NOMINAL_OPERATING_TEMPERATURE = 243<K>
      DETECTOR_DESC           = See the DETECTOR_DESC for CCD1
      SENSITIVITY_DESC        =
        The  CCD  matrix  middle integral sensitivity is not less then 1
        volt/lux.
 
      DETECTOR_ID             = CCD3
      DETECTOR_TYPE           = CCD-ARRAY
      MINIMUM_WAVELENGTH      = 0.45<MICROMETER>
      MAXIMUM_WAVELENGTH      = 1.0<MICROMETER>
      NOMINAL_OPERATING_TEMPERATURE = 243<K>
      DETECTOR_DESC           = See the DETECTOR_DESC for CCD1
      SENSITIVITY_DESC        =
        The  CCD  matrix  middle integral sensitivity is not less then 1
        volt/lux.
 
      Instrument Electronics Description
      ==================================
      Electronic block provides thegain  and processing for the CCD
      analog read-out and its transformation to a digital  image frame.
      The  digital image  has  8  bits  per  pixel; all  are
      significant. The electronic block  also operates exposure time
      selection(available times: 1-32768 ms) and mirror position. After
      acquisition, the electronic block replaces  first and last rows
      pixels and first 15 pixels of each row by housekeeping data  in
      the image frame.
 
      PDS1 Filter Parameters
      ======================
      FILTER_NUMBER           = 1
      FILTER_NAME             = BLUE
      FILTER_TYPE             = COLOR_GLASS
      MINIMUM_WAVELENGTH      = 0.41<MICROMETER>
      CENTER_FILTER_WAVELENGTH = N/A
      MAXIMUM_WAVELENGTH      = 0.59<MICROMETER>
 
      FILTER_NUMBER           = 2
      FILTER_NAME             = CLEAR
      FILTER_TYPE             = CLEAR_GLASS
      MINIMUM_WAVELENGTH      = 0.41<MICROMETER>
      CENTER_FILTER_WAVELENGTH = N/A
      MAXIMUM_WAVELENGTH      = 1.06<MICROMETER>
 
      FILTER_NUMBER           = 3
      FILTER_NAME             = INFRARED
      FILTER_TYPE             = COLOR_GLASS
      MINIMUM_WAVELENGTH      = 0.76<MICROMETER>
      CENTER_FILTER_WAVELENGTH = N/A
      MAXIMUM_WAVELENGTH      = 1.10<MICROMETER>
 
      PDS Instrument Optics Parameters
      ================================
      TELESCOPE_ID            = CAM1
      TELESCOPE_FOCAL_LENGTH  = 18.5<MM>
      TELESCOPE_DIAMETER      = 7.4<MM>
      TELESCOPE_F_NUMBER      = 2.5
      TELESCOPE_RESOLUTION    = 595<ONE/MM>
      OPTICS_DESC             = The telescope contains the 7-lens
        objective, the protecting blenda and the filter.
 
      TELESCOPE_ID            = CAM2
      TELESCOPE_FOCAL_LENGTH  = 100.0<MM>
      TELESCOPE_DIAMETER      = 20.0<MM>
      TELESCOPE_F_NUMBER      = 5.0
      TELESCOPE_RESOLUTION    = 295<ONE/MM>
      OPTICS_DESC             = The telescope contains the 7-lenses
        objective, the protecting blenda and the filter.
 
      TELESCOPE_ID            = CAM3
      TELESCOPE_FOCAL_LENGTH  = 18.5<MM>
      TELESCOPE_DIAMETER      = 7.4<MM>
      TELESCOPE_F_NUMBER      = 2.5
      TELESCOPE_RESOLUTION    = 558<ONE/MM>
      OPTICS_DESC             = The telescope contains the 7-lenses
        objective, the protecting blenda and the filter.
 
      Instrument Mounting Description
      ===============================
      The TV block, consisting of 3 telescopes with mirrors and 3
      detectors, is mounted on the spacecraft holder without
      hermoprotection. The electronic block is mounted inside the
      spacecraft.
 
      PDS1 Instrument Section Parameters
      ==================================
      SECTION_ID              = CAMERA 1
        SCAN_MODE_ID            = 2 Mb/s
        DATA_RATE               = 8192<B/S>
        SAMPLE_BITS             = 8
        FOV_SHAPE_NAME          = RECTANGULAR
        FOVS                    = 1
        HORIZONTAL_FOV          = 27.6<DEGREE>
        VERTICAL_FOV            = 21.2<DEGREE>
        HORIZONTAL_PIXEL_FOV    = 3.3<ARCMIN>
        VERTICAL_PIXEL_FOV      = 4.5<ARCMIN>
 
        INSTRUMENT_PARAMETER_NAME = RADIANCE
        MINIMUM_INSTRUMENT_PARAMETER = 1.0e-09
        MAXIMUM_INSTRUMENT_PARAMETER = 1.0e-02
        NOISE_LEVEL             = 0.05<PERCENT>
        INSTRUMENT_PARAMETER_UNIT = WATT/(CM*CM*STERADIAN*MICRON)
        SAMPLING_PARAMETER_NAME = PIXEL
        MINIMUM_SAMPLING_PARAMETER = 0
        MAXIMUM_SAMPLING_PARAMETER = 255
        SAMPLING_PARAMETER_INTERVAL = 1
 
      SECTION_ID              = CAMERA 2
        SCAN_MODE_ID            = 2 Mb/s
        DATA_RATE               = 8192<B/S>
        SAMPLE_BITS             = 8
        FOV_SHAPE_NAME          = RECTANGULAR
        FOVS                    = 1
        HORIZONTAL_FOV          = 5.2<DEGREE>
        VERTICAL_FOV            = 4.0<DEGREE>
        HORIZONTAL_PIXEL_FOV    = 0.62<ARCMIN>
        VERTICAL_PIXEL_FOV      = 0.83<ARCMIN>
 
        INSTRUMENT_PARAMETER_NAME = RADIANCE
        MINIMUM_INSTRUMENT_PARAMETER = 1.0e-09
        MAXIMUM_INSTRUMENT_PARAMETER = 1.0e-02
        NOISE_LEVEL             = 0.05<PERCENT>
        INSTRUMENT_PARAMETER_UNIT = WATT/(CM*CM*STERADIAN*MICRON)
        SAMPLING_PARAMETER_NAME = PIXEL
        MINIMUM_SAMPLING_PARAMETER = 0
        MAXIMUM_SAMPLING_PARAMETER = 255
        SAMPLING_PARAMETER_INTERVAL = 1
 
      SECTION_ID              = CAMERA3
        SCAN_MODE_ID            = 2 Mb/s
        DATA_RATE               = 8192<B/S>
        SAMPLE_BITS             = 8
        FOV_SHAPE_NAME          = RECTANGULAR
        FOVS                    = 1
        HORIZONTAL_FOV          = 27.6<DEGREE>
        VERTICAL_FOV            = 21.2<DEGREE>
        HORIZONTAL_PIXEL_FOV    = 3.3<ARCMIN>
        VERTICAL_PIXEL_FOV      = 4.5<ARCMIN>
 
        INSTRUMENT_PARAMETER_NAME = RADIANCE
        MINIMUM_INSTRUMENT_PARAMETER = 1.0e-09
        MAXIMUM_INSTRUMENT_PARAMETER = 1.0e-02
        NOISE_LEVEL             = 0.05<PERCENT>
        INSTRUMENT_PARAMETER_UNIT = WATT/(CM*CM*STERADIAN*MICRON)
        SAMPLING_PARAMETER_NAME = PIXEL
        MINIMUM_SAMPLING_PARAMETER = 0
        MAXIMUM_SAMPLING_PARAMETER = 255
        SAMPLING_PARAMETER_INTERVAL = 1
 
      Instrument Mode Description
      ===========================
      The  consecutive image production mode was used for the
      instrument; imaging parameters and number of frames were defined
      by the session's program.

        