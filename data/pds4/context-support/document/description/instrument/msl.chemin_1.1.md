
 
  Scientific Objectives
  =====================
    CheMin is designed to perform mineralogical analyses of rocks and soils
    to pursue the identification and characterization of past habitable
    environments on Mars. Understanding the mineralogy of samples allows an
    assessment of the involvement of water in the formation, deposition and
    alteration of surface materials. CheMin can also help to identify
    mineral biosignatures and to determine if mineral indicators of energy
    sources for life have been present.
 
 
  Instrument Overview
  ===================
    The Chemistry and Mineralogy (CheMin) instrument located within the body
    of the Mars Science Laboratory establishes the mineralogy of powdered
    samples using x-ray diffraction spectroscopy.  CheMin consists of a
    funnel for receiving powdered samples, 27 reusable sample cells, an
    x-ray source, a cooled charge-coupled device (CCD) detector, and analog
    and digital electronics.  Software for onboard processing of data runs
    in the rover computer.  CheMin contains 5 internal calibration standards
    for instrument characterization and establishing performance trends.
 
 
    Principal Investigator
    ----------------------
      The CheMin principal investigator is David Blake, Ames Research Center.
 
 
  Samples
  =======
    The MSL rover robotic arm can acquire powdered samples by drilling rocks
    or scooping soils. These samples are sieved through a screen with 150
    micrometer holes prior to delivery to the CheMin funnel.  After opening
    the inlet cover, the funnel is vibrated with piezoelectric actuators
    during the delivery of samples. Approximately 75 cubic millimeters of
    material is delivered in one portion, but the individual sample cells
    need only 15 cubic millimeters for an analysis.  Multiple portions may
    be delivered to help clean previous samples from either the funnel or a
    reused cell.  Two types of sample cells are available on the sample
    wheel: 14 with mylar windows, and 13 with kapton windows.  Kapton is
    more durable (mechanically and chemically) than mylar but has a
    signature which may interfere with certain types of samples.  Sample
    cell selection is an operational choice.  Piezoelectric actuators are
    used to agitate the samples in the cells and present random crystal
    faces to the x-ray beam.  After a sample is analyzed, it will be dumped
    into the instrument sump, allowing the cell to be reused.
 
 
  X-ray source (XRS)
  ==================
    The x-ray tube has a cobalt anode producing characteristic x-rays at 6.9
    keV (K-alpha) and 7.6 keV (K-beta). The sample in the cell is exposed to
    this collimated x-ray beam, and diffracted and fluoresced x-rays are
    measured by the CCD detector. The x-ray tube is nominally operated at 28
    kV and requires approximately 15 minutes to ramp up before data
    collection and a similar amount of time to ramp down after use.
 
 
  Detectors
  =========
    X-rays are captured on a CCD cooled with a mechanical cryocooler. Frames
    recorded during an analysis are 600 pixels by 582 pixels, which is not
    quite the entire array, allowing frames to conveniently fit within
    available memory pages. The frequency of image collection is a
    commandable parameter, and will typically be one frame every ~15
    seconds. Each image records the location and energy of the incident
    x-ray, allowing the extraction of both diffraction and fluorescence data
    from the sample. The optimum operational temperature is below -60 C to
    eliminate dark current and charge transfer issues due to accumulated
    radiation damage. The ability to achieve the optimum detector
    temperature depends on the temperature of the instrument mounting
    interface.
 
 
  Electronics
  ===========
    The analog voltages corresponding to each pixel of the CCD are fed
    through commandable gain stages and converted to digital format for
    storage and processing.  Up to 2730 individual frames can be stored
    within CheMin, corresponding to over 11 hours of data collection,
    assuming a 15 second integration time.  Housekeeping data (temperatures,
    voltages, parameters, etc.) are periodically captured and stored for
    subsequent downlink whenever the instrument is powered.
 
 
  Software
  ========
    The individual CCD images collected during an analysis fill a data
    volume which is too large to downlink in its entirety.  For example, a 5
    hour integration consisting of 1200 frames is well over 800 MBytes. This
    large data volume is processed into smaller products which will fit into
    the downlink. These products are described in the Experiment Data Record
    (EDR) Software Interface Specification (SIS) and are produced for each
    'minor frame.'  The size of a minor frame is commandable and may consist
    of approximately 30 minutes of data.  In the 5 hour example, the data
    might be grouped into 10 minor frames, each consisting of 120 images (or
    30 minutes of data). The data processing software is located within the
    MSL rover compute element, not within CheMin itself: The data interface
    between the instrument and the rover is the transfer of raw image
    frames.
 
 
  Calibration
  ===========
    Five separate calibration standards are carried within CheMin.  Two
    beryl-quartz mixtures (beryl:quartz=88:12 and 97:3) are used to
    establish the 2-theta scale for the data and will be analyzed
    periodically to check the internal alignment. A synthetic ceramic
    designed to have a variety of fluorescence lines can be used to
    establish and track the energy scaling of the data. A natural amphibole
    (pargasite) with minor additional mineral phases has a number of closely
    spaced diffraction peaks and is useful for evaluating 2-theta
    resolution. An arcanite sample was also added to characterize instrument
    performance in the presence of a significant sulfur fluorescence
    background.
 
    Integral to the calibration approach is the CheMin Development Model
    (DM) which is similar to the flight instrument, but will reside in a
    terrestrial laboratory and provide extensive analyses of a variety of
    relevant samples.
 
 
  Operational Considerations
  ======================
    The primary considerations for commanding CheMin during surface
    operations are ambient temperature and available energy. The detector
    produces better data when it is colder, and its temperature is related
    to that of the instrument mounting interface.  Thus, the ideal time to
    run a CheMin analysis from a thermal perspective is generally
    immediately prior to sunrise on any given sol.  Receiving samples from
    the robotic arm do not require a cold detector and will most likely be
    performed in the daytime while the arm actuators are warmer. Depending
    upon the complexity of the sample and the signal to noise levels
    necessary to identify and quantify minor mineral phases, the total
    integration time will likely be 8 to 10 hours.  This analysis duration
    does not have to be continuous, as data from different sols can be
    combined on the ground to produce an analysis representing the total
    integration time. CheMin consumes approximately 60 Watts during an
    analysis, so the integration time on a given sol may be limited by the
    available energy. The MSL rover can go to 'sleep' after it initiates an
    analysis to minimize the energy usage. The rover needs to be awake to
    turn off CheMin after the analysis and to transfer and process the data
    for downlink.
 
 
  Ground Software
  ==============
    After downlink of the data products in the format described in the
    accompanying EDR SIS, ground software tools are used to monitor the
    health of the instrument, determine the mineralogy, and identify
    chemical contributors to the sample. The two-dimensional diffraction
    images are converted into one-dimensional plots of counts versus 2-theta
    and read by commercial fitting programs to determine the mineralogy of
    the sample. The energy dispersive histograms produced in onboard
    processing are used to characterize the elemental chemistry.

        