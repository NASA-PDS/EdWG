
 
 
  Instrument Overview
  ===================
 
    The MECA instrument suite is a component of the Mars '07 Phoenix
    investigation, which will also return data from a Thermal and
    Evolved Gas Analyzer (TEGA), three cameras, and a meteorology
    suite (MET). Phoenix is motivated by the goals of (1) studying the
    history of water in all its phases, and (2) searching for
    habitable zones. Samples of surface and subsurface soil and ice
    will be delivered to MECA and TEGA from a trench excavated by a
    Robot Arm (RA), while MECA's Thermal and Electrical Conductivity
    Probe (TECP) will be deployed in soil and air by the Robot Arm.
    The Robot Arm Camera (RAC) will document the morphology of the
    trench walls, while the Surface Stereo Imager (SSI) and the Mars
    Descent Imager (MARDI) establish a geological context. Throughout
    the mission, MET will monitor polar weather and local water
    transport.
 
    The MECA instrument suite is composed of an Atomic Force
    Microscope (AFM), a Thermal Electrical Conductivity Probe (TECP)
    and a Wet Chemistry Laboratory (WCL). This data set description
    catalog file will describe the WCL. A complete description of the
    WCL can be found in [KOUNAVESETAL2008].
 
 
  Scientific Objectives
  =====================
    As part of the overall Phoenix science goals, the specific
    objective of the WCL is to characterize the aqueous
    chemical properties of soil samples as delivered by the Lander's
    robotic arm from the surface and at least two depths. To fulfill
    this goal, each WCL cell will determine:
 
        (1) hydrogen ion activity (pH),
        (2) redox potential (Eh/ORP),
        (3) solution electrical conductivity (EC),
        (4) concentration of selected soluble inorganic ionic
            species, and
        (5) possible redox couples and/or electrochemically
            mediated reactions.
 
 
  Calibration
  ===========
     Calibration of the WCL instrument is discussed in the WCL
     Calibration Report, which can be found in the Calibration
     folder of the MECA Non-imaging data archive.
 
     Most WCL sensors will have three separate calibration steps
     prior to their use on Mars. Each individual electrochemical
     sensor was first calibrated prior to integration into the beaker
     by laboratory measurement in several standard solutions using
     commercial electronics. The second calibration was performed with
     the same solutions after beaker integration, using flight-like
     analog electronics and a laboratory digital controller. The
     exceptions were the bromide and iodide sensors, which could not
     be tested after integration without contaminating the chloride
     sensor. The final two-point calibration will occur on Mars. In
     general, the ion selective electrodes exhibit classic logarithmic
     Nernstian behavior over the specified measurement range.
     Error analysis indicated that the best results for calculating
     unknown sample concentrations are obtained by using the average
     slope obtained from all the preflight calibrations anchored at
     the TS21 point.
 
 
  Operational Considerations and Operational Modes
  ================================================
    MECA's wet chemistry laboratory (WCL) comprises four single-use
    modules, each consisting of a beaker assembly and an actuator
    assembly. The modules mix soil samples with a leaching solution
    in a pressure vessel for electrochemical analysis. The scientific
    objective of the WCL is to determine the total pH, redox
    properties, and concentration of the principal aqueously solvated
    components of the acquired soil samples.
 
 
  Detectors
  =========
    Chemical data is returned by 26 distinct sensors, some redundant,
    lining the walls of each beaker. These measure: Temperature;
    pH (3); conductivity; oxidation-reduction potential; the anions
    chloride (2), bromide, and iodide; cations sodium, potassium,
    calcium, magnesium; and barium, used in a sulfate titration. Also
    included are electrodes for cyclic voltammetry, anodic stripping
    voltammetry, and chronopotentiometry (3). Lithium electrodes (2)
    are used as a reference relative to the known concentration of
    lithium salts in the solution. Sensors for nitrate, ammonium,
    dissolved oxygen and carbon dioxide, which for various reasons
    do not provide a quantitative measure of soil composition, are
    used only for context. A heater is imbedded in the base of the
    beaker to maintain water temperature during operation.
 
    Each WCL actuator assembly (AA) includes a tank containing 26
    ml of a calibration and leaching solution, a sample loading drawer
    with a capacity of ~1.0 cm3, temperature and pressure sensors,
    heaters, a stirring mechanism, and a device to dispense up to five
    small crucibles into the solution. The AA is responsible for soil,
    water, and solid reagent addition as well as stirring and two-zone
    internal heating (tank and drawer). Telemetry returned by the AA
    includes internal cell pressure, water storage tank and sampling
    drawer temperatures, and certain limit switch positions.
 
 
  Electronics
  ===========
    Pre-amplifier circuitry for the electrochemical sensors is
    embedded in the beaker walls. Analog to digital conversion
    (12-bit) is performed on a heavily-multiplexed Analog Board which
    interfaces to an FPGA on the primary MECA control and measurement
    electronics (CME) board. The FPGA also generates waveforms for the
    voltammetric and potentiometric sensors, performs temperature
    control, and operates actuators. Also returned in telemetry is a
    reading from an external temperature sensor located on the base of
    the microscopy sample stage.
 
  Operational Modes
  =================
    Each WCL experiment lasts two days (Sol A and Sol B), not
    necessarily sequential. After an initial post-landing checkout,
    preparation for a chemical experiment starts with melting the
    frozen leaching/calibration solution in the storage tank and
    delivering it to the beaker by actuating a puncture mechanism.
    Sensors are calibrated in that solution, and then calibrated again
    after addition of a crucible containing small quantities of
    specific salts. The combined ion concentration from the initial
    solution and from the crucible, less than 10-4 molar for most
    ions, establishes the detection floor. The final step is to open
    the sampling drawer and receive a sample from the robotic arm. The
    total sample volume is estimated with an accuracy of 0.25 cc
    (maximum 1 cc) from images acquired by the robot arm camera. For
    the remainder of the day, the concentration of major anions and
    cations are monitored as well as key indicators such as pH, redox
    potential, conductivity, and cyclic voltammetry, stirring when
    appropriate and maintaining a constant temperature of 5C. At the
    end of the day the solution is allowed to freeze in the beaker.
 
    A second day (Sol B) of measurement begins with thawing of the
    solution in the beaker, determining the sensor baseline, and
    adding an acid-containing crucible to lower the pH. Monitoring
    continues as on the first day. The final activity is the
    sequential addition of three crucibles of barium chloride. A
    sulfate titration is performed by monitoring the barium and
    chloride levels as the crucible contents slowly dissolve.

        