
 
 
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
    catalog file will describe the TECP. A complete description of the
    TECP can be found in [ZENTETAL2008].
 
 
 
  Scientific Objectives
  =====================
    The scientific objectives of the TECP are:
 
    To provide ground-truth for orbital surface thermal measurements
    and input parameters for thermal models by directly measuring the
    thermal properties of Martian regolith.
 
    To measure the concentration and nature of water in martian
    regolith in solid, 'non-frozen,' liquid, and vapor states.
 
    To determine changes in the reservoirs of water when soil is
    freshly exposed.
 
    To characterize the movement of water in and out of the soil by
    measuring atmospheric humidity, temperature, and wind speed above
    the surface.
 
  Calibration
  ===========
    Calibration of the TECP instrument is discussed in the TECP
    Calibration Report, which can be found in the Calibration
    folder of the MECA Non-imaging data archive.
 
 
  Operational Considerations and Operational Modes
  ================================================
    An end-effector on the Phoenix Robotic Arm, the TECP is a probe
    of soil physical properties including temperature, thermal
    conductivity and diffusivity, electrical conductivity and
    permittivity, as well as atmospheric temperature, humidity, and
    wind speed. These measurements are made with four conical needles,
    three of which contain electrical heaters and thermometers, and a
    hygrometer sensor mounted separately in the body of the TECP.
 
  Detectors
  =========
    Three of the four parallel needles contain a thermocouple and a
    heater. The two needle pairs are used as electrodes for regolith
    electrical properties measurements. The same needles also serve as
    heating elements and thermometers for regolith thermal properties
    and wind speed measurements. The needles can be inserted into the
    soil for thermal and electrical measurements or positioned above
    the surface for atmospheric temperature, and wind speed
    measurements. Regolith thermal properties (including temperature,
    thermal conductivity, thermal diffusivity, volumetric heat
    capacity, and thermal inertia) as well as wind speed are derived
    from the heating and cooling behavior of the needles before and
    after a known amount of heat is added. Regolith electrical
    properties, including electrical conductivity and dielectric
    permittivity, are measured with capacitance and resistance sensors
    coupled to the regolith through the sensing needles. Atmospheric
    water vapor concentration is measured with a calibrated capacitance
    hygrometer mounted near a temperature sensor on the TECP printed
    circuit board, but exposed to the atmosphere through a particulate
    filter.
 
    The humidity sensor determines the capacitance of the thin film
    hygrometer, which is a calibrated function of the relative
    humidity at the film surface. By measuring the film temperature
    with the adjacent temperature sensor, the result can be converted
    to absolute humidity. Under the assumption that gradients in
    vapor pressure are small, external relative humidity can be
    determined by comparison of the TECP result with the MET
    temperature sensors.
 
  Electronics
  ===========
    Measurement electronics are contained in the body of the TECP,
    and include a 12 bit A/D converter, two phase detectors, three
    resistance bridges, and a digital shift register. The A/D
    converter and shift register communicate through a serial
    interface to an FPGA on the primary MECA control and measurement
    electronics (CME) board.
 
  Operational Modes
  =================
    TECP will measure the temperature, thermal conductivity and
    volumetric heat capacity of the regolith. It will also detect and
    quantify the population of mobile H2O molecules in the regolith
    throughout the polar summer, by measuring the electrical
    conductivity of the regolith, as well as the dielectric
    permittivity. In the vapor phase, TECP is capable of measuring the
    atmospheric H2O vapor abundance, as well as augment the wind
    velocity measurements from the meteorology instrumentation. TECP
    is mounted near the end of the 2.3 m Robotic Arm, and can be
    placed either in the regolith material or held aloft in the
    atmosphere.
 
    TECP thermal and electrical properties measurement quality depends
    on proper needle placement by the RA. Non-linear insertion,
    partial insertion, and lateral movement all affect data quality
    negatively. Thermal properties measurements can also be negatively
    impacted by non steady state thermal conditions, and the TECP
    should therefore be allowed to equilibrate to its thermal
    environment before making thermal properties measurements.
 
    There are no requirements for TECP to measure wind velocity.
    However, application of a protocol similar to the thermal
    properties experiments has shown some promise in characterizing
    wind speeds, particularly in high-wind regimes where the wind-sock
    associated with the Meteorology package is not capable of
    measuring wind as well. The procedure involves heating needle one
    for a period up to 70 seconds, and then following the cooling
    curve for another 90 seconds. Preliminary analysis of the heating
    and cooling data acquired at Mars-like pressures in a wind tunnel
    at the University of Michigan suggest that both peak temperatures
    and the cooling time constant are sensitive to wind velocity.
    Characterization of the TECP response to wind velocity is ongoing,
    and the determination of whether or not to try wind velocity
    measurements on the Martian surface will be made once those
    analyses are complete.

        