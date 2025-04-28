
 
 
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
 
  Operational Modes:
  ===========================
    The INCA detector has the capability to be placed in either ion mode
    or neutral mode.  Ion mode indicates that the potential of the
    deflection plates is set to zero so that ions are also counted along
    with neutrals.  Neutral mode identifies that there is a potential
    applied to the plates that will cause the ions to deflect away from
    the entrance aperture and not be counted.  The efficiency of this
    process is strongly dependent upon the applied plate potential.  The
    applied plate potential is a configurable parameter within the system
    and is based upon the science goals, dust environment, and the
    expected plasma and high energy particle distributions. 
 
  Operational Considerations:
  ===========================
 
    The MIMI power consumption is nomially ~19.0 W.  Typical operations
    include the capability to sense 6-7 orders of magnitude in particle
    flux over a dynamic energy range for electrons of 30 KeV to 5 MeV and
    for ions from 3 KeV to 160 MeV. Data quality is affected by direct sun
    exposure into the instruments and INCA operations are tailored to
    reduce the possibility of direct dust particle impacts into the sensor
    aperture during ring crossings.
 
 
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
 
    The INCA sensor is separately mounted and nearly co-aligned with the
    remote sensing instruments, with a field of view of 120 degrees in
    latitude and 90 degrees in azimuth, centered on a vector rotated 9.5
    degrees toward the spacecraft +x axis from the -y axis. INCA makes two
    different types of measurements.  It obtains the directional
    distribution, energy spectra, and crude composition of magnetospheric
    ions between 7 keV/nuc and 500 keV/nuc and it makes remote images of
    the global distribution of the energetic neutral emission of hot
    plasmas in the Saturnian magnetosphere, measuring the composition and
    energy spectra of those energetic neutrals for each image pixel.
 
    Frames diagram
    --------------
 
    All MIMI telescope directions are described in terms of the
    spacecraft fixed frame.
    
    INCA is separately mounted and nearly co-aligned with the remote
    sensing instruments with a latitudinal field of view of 120 degrees
    and an azimuthal field of view of 90 degrees centered on a vector
    rotated 9.5 degrees toward the spacecraft +x axis from the -y axis.
 
    There are no otherwise specifically defined Cassini MIMI frames.
 
  Electronics:
  ============
 
    Signals from the sensors are first processed by the analog
    electronics and then by the digital processing unit (DPU). With 
    respect to INCA thebdata is shifted into appropriate bins based 
    upon the current spacecraft orientation and spin rates.
    
    The INCA instrument has the ability through the
    use of high voltage potentials applied to the aperture plates to
    deflect ions away from the entrance slit and instead image
    neutral particles.  When the high voltage supply is turned off
    then the instrument see both neutrals and ions.
 
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

        