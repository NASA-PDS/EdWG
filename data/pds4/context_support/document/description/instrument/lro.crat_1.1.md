
 
  Abstract:
  =========
 
    The investigation hardware consists of a single, integrated sensor
    and electronics box with simple electronic and mechanical interfaces
    to the LRO spacecraft. The CRaTER sensor front-end design is based on
    standard stacked-detector, cosmic ray telescope systems that have been
    flown for decades, using detectors developed for other NASA flight
    programs. The analog electronics design is virtually identical to the
    robust and flight-proven design of the NASA/POLAR Imaging Proton
    Spectrometer that has been operating flawlessly on orbit since 1996.
    The digital processing unit is a simple and straightforward design
    also based on similar instruments with excellent spaceflight heritage.
    No new technology developments or supporting research are required for
    the final design, fabrication, and operation of this instrument..
 
    The text of this instrument description has been abstracted from the
    instrument paper [CHINETAL2007] and from a preliminary draft of the
    CRaTER Instrument Calibration Plan [KASPER2007].
 
  Scientific Objectives:
  ======================
 
    The Cosmic Ray Telescope for the Effects of Radiation (CRaTER) is
    designed to answer key questions to enable future human exploration of
    the Solar System, and to address one of the prime objectives of LRO.
    Specifically, CRaTER addresses an objective required by NASA's
    Exploration Initiative to safely return humans to the Moon; CRaTER is
    designed to achieve characterization of the global lunar radiation
    environment and its biological impacts and potential mitigation, as
    well as investigation of shielding capabilities and validation of other
    deep space radiation mitigation strategies involving materials. CRaTER
    will fill knowledge gaps regarding radiation effects, provide
    fundamental progress in knowledge of the Moon's radiation environment,
    and provide specific path-finding benefits for future planned human
    exploration. CRaTER's primary measurement goal is to measure directly
    the linear energy transfer (LET) spectra caused by space radiation
    penetrating shielding material. Such LET spectra are a missing link,
    currently derived by models which require experimental measurements to
    provide ground truth. CRaTER will provide this essential information
    about the lunar radiation environment.
 
    LET is defined as the mean energy absorbed locally, per unit path
    length, when an energetic particle traverses material. A LET
    spectrometer measures the amount of energy deposited in a detector of
    known thickness and material property when an energetic particle passes
    through it, usually without stopping. LET measurements behind various
    thicknesses and types of material are of great importance to spacecraft
    engineers and radiation health specialists. Such measurements are
    especially important to modelers who study the impacts of the
    penetrating radiation; LET is one of the most important inputs for
    predictive models of human health risks and radiation effects in
    electronic devices. While LET spectrometers do not necessarily resolve
    particle mass, LET measurements do include all the species, with the
    possible exception of neutrons, that are relevant to the energy
    deposited behind a known amount of spacecraft shielding. A LET
    spectrometer essentially provides the key direct measurement needed to
    bridge the gap between well measured cosmic ray intensities (that will
    be available from other spacecraft) and specific energy deposition
    behind shielding materials, exploration-enabling knowledge vital to the
    safety of humans working in the harsh space radiation environment.
    Accordingly, CRaTER is designed to measure this important quantity and
    thereby provide critical closure between measurements, theory, and
    modeling.
 
    CRaTER will measure LET spectra produced by incident galactic cosmic
    rays (GCRs) and solar energetic protons (SEPs). GCRs and SEPs with
    energies >10 MeV have sufficient energy to penetrate even moderate
    shielding. When they interact with matter, they leave behind energy,
    damaging the human tissue and electronic parts they pass through. GCRs
    and SEPs possess both short and long timescale variations (see Fig.
    10), some of which are predictable and others that are not presently
    predictable. GCRs are a slowly-varying and uniform source of cosmic
    radiation that bathes the solar system. SEPs are episodic and rare, but
    come in extreme bursts associated with intense solar magnetic activity.
    Both GCRs and SEPs pose serious risks to humans venturing above the
    relative safety of low-Earth orbit and the Earths powerful magnetic
    shield; areas including the Moon and the interplanetary space between
    Earth and Mars may be dangerous to humans.
 
    In order to achieve the LRO radiation mission requirement, CRaTER is
    designed to return the following required data products:
 
    * Measure and characterize that aspect of the deep space radiation
    environment, LET spectra of galactic and solar cosmic rays
    (particularly above 10 MeV), most critically important to the
    engineering and modeling communities to assure safe, long-term, human
    presence in space.
 
    * Investigate the effects of shielding by measuring LET spectra behind
    different amounts and types of areal density, including
    tissue-equivalent plastic.
 
    The CRaTER measurement concept is shown in the see-thru telescope
    drawing below (Fig. 11). The investigation hardware consists of a
    single, integrated telescope and electronics box with straightforward
    electronic and mechanical interfaces to the spacecraft. The
    zenith-nadir viewing telescope employs a stack of three pairs of
    detectors embedded within aluminum structure and tissue-equivalent
    plastic (TEP) to establish the LET spectra of cosmic radiation relevant
    for human health and electronics part concerns.
 
    Primary GCRs and SEPs enter the telescope through the zenith,
    deep-space entrance, depositing energy in the telescope stack through
    ionizing radiation and producing secondary particles through nuclear
    interactions. The primary and secondary particles interact with one or
    more of the six detectors through the stack: the thin (thick) detectors
    are optimized for high (low) LET interactions. Events with sufficient
    energy deposition in a detector cross a trigger threshold. Digital
    logic then compares multi-detection coincidences with predefined event
    masks to identify desirable events. Pulse height analysis is performed
    on every detector to measure LET at each point in the stack.
 
    The measurement team will use observations taken during the mission to
    construct LET spectra behind the different amounts of material,
    including TEP, as a function of particle environment (GCR vs. SEP;
    foreshock vs. magnetotail vs. solar wind; etc.). The team will also
    test models of radiation effects and shielding by verifying/validating
    deterministic models.
 
    Model predictions of energy transport of incident GCR and SEP spectra
    (available contemporaneously on other missions) through the CRaTER
    instrument will be compared to the measured LET spectra. Thus, CRaTER
    will provide not only direct measurements of LET in the lunar
    environment, but will also better constrain radiation effects models
    that are being used to assess the effects of other radiation
    environments, including in interplanetary space and at Mars.
 
  Calibration:
  ============
 
    The calibration of the CRaTER Flight Models is based on lessons learned
    from experiences with the Engineering Model: the relationship between
    the value returned by the detectors and the original energy deposited is
    essentially linear. Gains and offsets for each detector are determined
    with high precision by calibrating the instrument with a beam of high
    energy protons produced by the Northeast Proton Therapy Center (NPTC) of
    Massachusetts General Hospital (MGH) in Boston. A 300 MeV proton beam at
    MGH is degraded in energy using sheets of plastic until a beam is produced
    with large energy dispersion and a peak energy tuned to the response of
    a pair of thin and thick CRaTER detectors. The dispersed beam produces
    a characteristic track in energy deposition in the pair of detectors.
    The gains and offsets for each of the detectors is then determined by
    iteratively varying the free parameters of the instrument response until
    the measurements match the predictions of GEANT numerical simulations
    of the energy loss.
 
 
  Operational Modes:
  ===========================
 
    The CRaTER instrument has only two modes: powered up and powered down.
    There are no operational constraints on these modes. In particular,
    CRaTER can be powered up during the cruise phase of the mission, and
    will return scientifically useful data.
 
  Sensors:
  ==========
 
    The investigation hardware consists of a single, integrated sensor and
    electronics box with simple electronic and mechanical interfaces to the
    LRO spacecraft. The CRaTER sensor front-end design is based on standard
    stacked-detector, cosmic ray telescope systems that have been flown for
    decades, using detectors developed for other NASA flight programs. The
    analog electronics design is virtually identical to the robust and flight-
    proven design of the NASA/POLAR Imaging Proton Spectrometer that has been
    operating flawlessly on orbit since 1996. The digital processing unit is
    a simple and straightforward design also based on similar instruments
    with excellent spaceflight heritage. No new technology developments or
    supporting research are required for the final design, fabrication, and
    operation of this instrument.
 
 
    The CRaTER telescope consists of six ion-implanted silicon detectors,
    mounted on detector boards, and separated by pieces of tissue-
    equivalent plastic, hereinafter referred to as TEP. All six of the
    silicon detectors are 2 cm in diameter. Detectors 1, 3, and 5 are 140m
    thick; the others are 1000m thick. TEP (such as A-150 manufactured by
    Standard Imaging) simulates soft body tissue (muscle) and has been used
    for both ground-based as well as space-based (i.e., Space Station)
    experiments.
 
    Solid-state detectors use semi-conducting crystals (in CRaTERs case,
    silicon) with n-type (electron-rich, electron conducting) and p-type
    (electron-deficient, hole conducting) regions.
 
    When a reversed bias voltage is applied across the junction, the
    un-bonded electrons in the semiconductor are pushed away from the
    voltage source, while the holes are pulled towards it. This leaves a
    neutral area void of charge and current at the junction of the sectors,
    called the depletion region. As incoming radiation (e.g., a solar
    proton or cosmic ray particle) collides with the depletion region,
    electron-hole pairs are formed in the material (where a once bonded
    electron is freed from its atom, leaving a hole). The electron and the
    hole respond to the applied voltage, and a small current is created.
    This current can be detected and later analyzed.
 
    A cold environment greatly reduces the transmission of thermal
    signals. In addition, the solid state of the semiconducting material
    makes it easier to detect those signals attributable to freed
    electrons.
 
    Tissue equivalent plastic (or TEP) is a plastic recipe designed to
    simulate human tissue. It includes hydrogen and nitrogen
    percentages-by-composition that are similar to that found in human skin
    and muscle. Scientists can use the atomic-level effects that radiation
    has on the TEP to deduce what sort of similar effects may occur in
    humans.
 
  Electronics:
  ============
 
    The front-end analog electronics utilize charge amplifiers to collect
    signals from the six silicon detectors, amplify, and pulse-shape them
    for high-level processing. The backend digital electronics receives the
    six signals converts them in parallel to 12-bit digital quantities and,
    using a programmable coincidence mask, filters out the events of
    interest. Those events are then packed into standard CCSDS data packets
    and forwarded to the spacecraft data system for storage and eventual
    telemetry to the ground. A field programmable logic array contains all
    of the digital circuitry that receives commands from the spacecraft and
    handles telemetry packet formatting as well as collecting useful
    secondary science and analog housekeeping information. There is no
    processor or software within the instrument.
 
    The maximum event rate that the instrument can telemeter is limited to
    1200 events/second, enforced separately for every 1 second interval;
    excess events are discarded. The instrument has an internal deadtime of
    12 microseconds. Events are time-tagged to an accuracy of 1 second.

        