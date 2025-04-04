
 
 
  INSTRUMENT: INFRARED INTERFEROMETER SPECTROMETER
  SPACECRAFT: MARINER 9
 
 
  Instrument Information
  ======================
    Instrument Id                  : IRIS
    Instrument Host Id             : MR9
    PI Pds User Id                 : BJCONRATH
    Instrument Name                : INFRARED INTERFEROMETER
                                     SPECTROMETER
    Instrument Type                : INFRARED INTERFEROMETER
    Instrument Mass                : 22.3
    Instrument Serial Number       : IRIS M
    Instrument Manufacturer Name   : TEXAS INSTRUMENTS
 
 
  Instrument Description
  ======================
    The Mariner 9 Infrared Interferometer Spectrometer (IRIS)
    instrument is a Michelson interferometer with a circular
    aperture 4.3 cm in diameter.  The field of view is also
    circular, with an angular diameter of approximately 4.4 degrees.
    The effective spectral range of the interferometer is 200-2000
    cm**-1, and the apodized spectral resolution is 2.4 cm**-1.  The
    dwell time for each interferogram is 18.2 s.  An
    image-motion-compensating mirror, inclined at an angle of 45
    degrees to the axis of rotation, is part of the instrument;
    however, it was never used for motion compensation.  The beam
    splitter of the interferometer consists of a multilayer
    dielectric coating applied to a CsI substrate.  The moving
    mirror mounted on one end of a motor shaft is driven at a
    constant velocity of 0.0235 cm/s during the recording of an
    interferogram.  The fringe-control/reference interferometer uses
    the same moving mirror, beamsplitter and fixed mirror, but a
    different optical path than the IR signal, making use of the
    center of the beamsplitter.  The center of the beamsplitter is
    coated to perform well in the visible and near-infrared for the
    reference interferometer.  A 0.6929 micrometer neon line source
    is used for the reference interferometer with a photomultiplier
    detector.  The signal from this unit, along with a velocity
    transducer, provides feedback control of the main
    interferometer, and as an initiator for the analog to digital
    conversion process.  Synchronization of the data stream with the
    spacecraft clock is accomplished by a phased locked loop which
    slaves the mirror motion to the highly stable clock frequency.
    The main IR detector is a thermister bolometer operating at 250
    K with a bias voltage of 500 V.  The entrance window of the
    instrument is also CsI to permit operation to 200 cm**-1.  The
    window seals the interferometer from moisture and dust, and it
    supports an optical filter designed to reflect sunlight and
    thermal radiation below 2500 cm**-1.  The filter also protected
    the CsI window from atmospheric degradation during storage and
    launch.  Calibration is provided by alternatively viewing deep
    space and a built-in blackbody maintained at a temperature of
    296.4 K (see instrument calibration description) by rotation of
    the image motion compensation mirror.  The dynamic range of the
    instrument is 8000:1 with an NER (noise equivalent radiance) of
    0.5 x 10**-7 W cm**-2 sr**-1/cm**-1.
 
    The temperature of the instrument is passively and actively
    controlled to operate at a nominal temperature of 250.0 +/- 0.2
    K.  One surface of the instrument is not covered by thermal
    insulation; it acts as a passive radiator to deep space.  Active
    thermal control is maintained by the action of thermostatically
    controlled heaters.  The thermostat kept the IRIS optical module
    temperature constant to within +/- 0.2 K from the time of the
    initial cooldown prior to launch, through the transit phase, and
    during orbital operation at Mars [HANEL_ETAL_1972A,
    HANEL_ETAL_1972B, HANEL_ETAL_1972C].
 
 
  Scientific Objectives
  =====================
    The scientific objectives of the Mariner 9 Infrared
    Interferometer Spectrometer (IRIS) investigation include the
    following:
 
    (1) Determination of the carbon dioxide pressure at the surface.
    (2) Determination of the vertical temperature profile of the
        atmosphere.
    (3) Determination of the total amount of atmospheric water
        vapor.
    (4) Identification and determination of the abundances of other
        minor atmospheric constituents.
    (5) Determination of surface temperatures.
    (6) Determination of chemical or mineralogical composition and
        information of the physical structure of the surface layer,
        including polar deposits.
 
    These objectives are accomplished through the analysis of
    measurements of thermal emission spectra.
 
 
  Calibration
  ===========
    Calibration spectra were periodically recorded while observing
    either deep space or an on-board warm blackbody (T = 296.4 K).
    One pair of calibration spectra is generated for every 14
    spectra of Mars (7 spectra of Mars, on-board black-body, 7
    spectra of Mars, deep space, etc.).  Scaling of the raw Martian
    spectra to the calibration spectra specifies the Martian spectra
    in absolute radiometric units.  The calibration procedure for
    the Mariner 9 spectra is similar to that previously described
    for Nimbus 4, see HANEL_ETAL_1972D.  The excellent thermal
    stability of the Mariner 9 IRIS permitted the entire ensemble of
    1766 calibration pairs acquired during the Mariner mission to be
    averaged to provide a single set of calibration parameters.
    Consequently, the random error introduced into the individual
    target spectra from calibration is extremely small.
 
    The calibration is carried out independently for each wavenumber
    interval by using the equation I = B(Tw) * (C1 - C2) / A1 / (C3
    - C2), where C1 = the instantaneous spectral amplitude for Mars,
    C2 = the average of the spectral amplitudes for the cold
    calibration source (deep space), and C3 = the average of the
    spectral amplitudes for the warm calibration source (on-board
    reference blackbody).  B(Tw) is the Planck function for the
    temperature of the warm reference blackbody (Tw).  Tw is an
    average of eight transducer measurements made immediately before
    and after each interferogram.  A1 is the reciprocal value of the
    emissivity of the black paint used in the warm calibration
    source, an aluminum plate with 30 degree V-shaped grooves
    painted with 3M 401-C10 Black Velvet paint.  While this paint is
    relatively black over most of the instrument spectral range,
    small glass beads contained in it give rise to emittance
    variations of a few percent near 480 cm**-1 and 1100 cm**-1
    which are characteristic wave numbers of silicon dioxide.  The
    correction factor was derived from laboratory reflectance
    measurements on a duplicate blackbody, from similar measurements
    on the same type of paint, kindly made available by James
    Aronson (private communication), and finally from comparisons of
    the warm and cold calibrations of the interferometer while in
    orbit around Mars.  All three methods were in agreement;
    consequently, the emissivity correction of the warm calibration
    source has been applied to all spectra.  The emissivity of the
    reference 'blackbody' is listed below:
 
    Wave                          Wave
    Number         Emissivity     Number         Emissivity
    (cm**-1)       (cm**-1)
    370            1.00           1000           0.98
    375            1.00           1005           0.98
    380            1.00           1010           0.97
    385            1.00           1015           0.97
    390            1.00           1020           0.96
    395            0.99           1025           0.96
    400            0.99           1030           0.96
    405            0.99           1035           0.95
    410            0.99           1040           0.95
    415            0.99           1045           0.94
    420            0.98           1050           0.94
    425            0.98           1055           0.94
    430            0.98           1060           0.94
    435            0.97           1065           0.93
    440            0.97           1070           0.93
    445            0.96           1075           0.93
    450            0.96           1080           0.92
    455            0.95           1085           0.92
    460            0.95           1090           0.92
    465            0.95           1095           0.92
    470            0.95           1100           0.91
    475            0.95           1105           0.91
    480            0.96           1110           0.91
    485            0.97           1115           0.92
    490            0.98           1120           0.92
    495            0.99           1125           0.92
    500            0.99           1130           0.93
    505            0.99           1135           0.94
    510            1.00           1140           0.95
    515            1.00           1145           0.96
    520            1.00           1150           0.96
    .              .              1155           0.97
    .              .              1160           0.98
    .              .              1165           0.98
    945            1.00           1170           0.98
    950            1.00           1175           0.99
    955            1.00           1180           0.99
    960            0.99           1185           0.99
    965            0.99           1190           0.99
    970            0.99           1195           0.99
    975            0.99           1200           0.99
    980            0.99           1205           1.00
    985            0.99           1210           1.00
    990            0.98           1215           1.00
    995            0.98           1220           1.00
 
    The responsivity of the instrument and a spectral instrument
    temperature may also be derived from each calibration pair.  The
    noise equivalent spectral radiance (NESR), a measure of the
    random errors in the measurements, is calculated from the
    standard deviation of the individual instantaneous
    responsivities.  The derivation and description of all the
    instrumental parameters are discussed in detail in
    HANELETAL1972D. Reference, responsivity, noise, and instrument
    temperature spectra are included in the auxiliary data of the
    MARINER9-MARS-IRIS-3-RDR-V1.0 dataset.  Small, narrow spikes are
    present in the instrument NESR at the following locations:
 
    nu(cm-1)      f(Hz)         Probable Source
    ----------------------------------------------------
     356.          8.36         8-1/3 bps-telemetry rate
     713.         16.76         2 (8-1/3)
    1069.         25.12         4 (8-1/3)
    1203.         28.27         Unknown
    1426.         33.52         4 (8-1/3) & 33-1/3
    1782.         41.88         5 (8-1/3)
 
    The most probable sources of most of these spikes are transients
    caused by the engineering telemetry channels which have
    characteristic frequencies of 8-1/3 and 33-1/3 bps.  The source
    of the interference at 28.27 Hz is unknown.
 
    In addition to the radiometric calibration, a wave number
    correction has been applied to the data.  The finite solid
    angles of the primary and reference interferometers cause a
    small wave number shift and a distortion of the true wave number
    scale.  This well known effect, caused by the interference of
    on-axis and off-axis rays, has been corrected for empirically.
    A numerical fit of a Lorentzian function was made to determine
    the center wave number position nu_m and nu_t of the strongest
    carbon dioxide features in a measured and in a theoretical
    spectrum, respectively.  The correction adopted to provide the
    theoretical wave number scale is nu_t = (0.016187 + nu_m) /
    1.0010602.  This adjustment has been incorporated in the
    calculation of the wave number mesh for the calibrated
    radiances.
 
 
  Operational Considerations
  ==========================
    The Mariner 9 IRIS instrument operated normally throughout the
    mission.  As discussed in the Instrument Calibration
    Description, the excellent thermal stability of the Mariner 9
    IRIS permitted the entire ensemble of 1766 calibration pairs
    acquired during the Mariner mission to be averaged to provide a
    single set of calibration parameters.  Consequently, the random
    error introduced into the individual target spectra from the
    calibration is extremely small.  However, a detailed analysis of
    emission angle pairs of spectra has determined that there may be
    a very minor calibration error due to a small spike in one of
    the calibration interferograms.  Additionally, for spectra taken
    of areas with extremely low temperatures the NESR dominates at
    high wavenumbers causing the calculated brightness temperatures
    to increase with increasing wavenumber.
 
 
  Instrument Detectors
  ====================
    The detector of the infrared interferometer is a thermister
    bolometer operating at 250 K with a bias voltage of 500 V.
 
 
  Instrument Electronics
  ======================
    The bulk of the analog and all of the digital circuitry is in an
    electronics module located in the support base for the
    interferometer module.  The parity and summation electronics are
    in a separate box attached to the support base electronics
    module.  The primary and standby power supplies and the
    interface chassis are part of the Mariner octagonal spacecraft
    bus structure.  The electronics box contains timing and control
    elements, mirror drive circuitry, housekeeping monitors, thermal
    controllers, and analog-to-digital converters.
 
 
  Instrument Optics
  =================
    All mirrors of the interferometer are gold coated.  The fixed
    interferometer mirror is the entrance pupil for the optical
    system.  It has an effective circular aperture of 3.5 cm
    diameter.  An ellipsoidal mirror collects the energy from the
    interferometer and focuses it onto the infrared detector, a
    thermister bolometer, which serves as the exit pupil.
 
 
  Instrument Offset
  =================
    The instrument and the associated electronics modules are bolted
    to the scan platform.  The primary and standby power supplies
    and the interface chassis are part of the octagonal electronics
    rack of the spacecraft.  The instrument is approximately
    bore-sighted with the television camera, ultraviolet
    spectrometer and infrared radiometer.
 
 
  Instrument Parameters
  =====================
    Thermal Radiance (W cm-2 ster-1/cm-1).
 
 
  Instrument Modes
  ================
    The instrument possesses only one operating mode.  When turned
    on the instruments acquires one interferogram every 21 second
    data frame.
 

        