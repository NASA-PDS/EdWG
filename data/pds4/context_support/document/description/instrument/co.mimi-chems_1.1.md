
 
 
    The text of this instrument description has been abstracted from the
    instrument paper [KRIMIGISETAL2004]:
 
    Krimigis, S.M., Magnetosphere Imaging Instrument (MIMI) on the
    Cassini Mission to Saturn/Titan, in Space Science Reviews, Springer
    Science and Business Media, B.V., formerly Kluwer Academic
    Publishers B.V., Vol. 114, No. 1-4, pp. 233-329, December 2004.
 
 
  Calibration:
  ============
 
    Calibration processes are accomplished via both flight software
    and ground processing software.  Flight software is used primarily
    to accommodate variations in measurements due to spacecraft motion.
    Ground based calibration is accomplished through a combination of
    calibration data values (see COMIMI_0000) coupled with various
    algorithms to generate particle flux from measured count rates.
 
 Operational Considerations:
  ===========================
 
    The MIMI power consumption is nomially ~19.0 W.  Typical operations
    include the capability to sense 6-7 orders of magnitude in particle
    flux over a dynamic energy range for electrons of 30 KeV to 5 MeV and
    for ions from 3 KeV to 160 MeV. Data quality is affected by direct sun
    exposure into the instruments.


  Sensors:
  ==========
 
    The MIMI experiment consists of three independent sensors: Charge
    Energy Mass Spectrometer (CHEMS), Ion Neutral Camera (INCA), and Low
    Energy Magnetospheric Measurements (LEMMS).  Each sensor has specific
    targeted energies and populations to be examined and collectively
    provide the ability to fully characterize the energetic charged and
    neutral particle population in the Saturnian Magnetosphere as well as
    the Solar Wind, the Jovian Magnetosphere, and the Earth Magnetosphere.
 
    Each sensor is a combination of geometric components, silicon
    detectors, micrpchannel plates, and electronics/software components
    that give them the ability to fully answer the missions scientific
    objectives. When the spacecraft is spinning the MIMI sensors obtain
    measurements over a full four pi steradians.  The different MIMI
    sensors share common electronics and provide complimentary
    measurements of energetic plasma distributions, composition, and
    energy spectrum, and the interaction of that plasma with the extended
    atmosphere and moons of Saturn.
 
    The CHEMS sensor is mounted on the particles and fields instrument
    pallet with a field of view of approximately 160 degrees in latitude
    (bisected by the spacecraft x-y plane) by 4 degrees in azimuth
    centered on the spacecraft -x axis. CHEMS measures ions from
    approximately 3 to 220 KeV/e.
 
    Frames diagram
    --------------
 
    All MIMI telescope directions are described in terms of the
    spacecraft fixed frame.
    CHEMS latitudinal field of view of 160 degrees is bisected by the
    spacecraft x-y plane and its azimuthal field of view of 4 degrees
    is centered on the spacecraft -x axis.

    There are no otherwise specifically defined Cassini MIMI frames.
 
  Electronics:
  ============
 
    Signals from the sensors are first processed by the analog
    electronics and then by the digital processing unit (DPU). Analog
    data are placed into the digital system and with respect to CHEMS
    minimal processing is done.  
    
    The CHEMS sensor has a variable high voltage
    potential to determine selection of particle based upon energy
    and to then subsequently place particles into energy, mass, and/or
    mass/charge bins. 
 
    The DPU unit's primary function is to catalog incoming particle
    measurements based upon underlying logic and to count events in
    accumulation bins.  The DPU also packages the data along with the
    instrument housekeeping data (instrument states) and then integrated
    into telemetry for broadcast to ground station.
    
    Parameters that control the high voltage supplies, the selection
    of priority counters etc, are expected to be updated periodically
    under normal operating conditions.
 
    Data compression and sampling techniques are used to maximize data
    return within the bandwidth allocated to the experiment.

        