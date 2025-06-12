
           The Energetic Particle Spectrometer (EPS) is part of the MESSENGER 
           Energetic Particle and Plasma Spectrometer (EPPS) system, which 
           which also includes the Fast Imaging Plasma Spectrometer (FIPS).
           FIPS covers the energy/ charge range of < 50 eV/q to 20 keV/q. The 
           desired throughput for FIPS charged particle and EPS event processing 
           is 5 kHz. The FIPS instrument was constructed by the University of 
           Michigan Space Physics Research Laboratory.
 
           The FIPS sensor is designed to measure the distributions and
           composition of magnetosphere ions, as well as to characterize the
           nature of the planetary magnetic field of Mercury.  It will do this
           by measuring the mass per charge, the energy per charge, and
           incident angles for particles entering the sensor.  The particle
           intensity is also calculated from the event rate information.  FIPS
           generates a single 48-bit raw event packet format, which includes a
           1-bit header that identifies the event as a proton event or a
           non-proton event; an 11-bit time-of-flight (TOF) value; as well as
           Wedge, Strip, and ZigZag values (each 12 bits in size). In addition,
           the FIPS system generates counter and housekeeping information that
           the EPPS software can access via the I2C bus interface.
 
           The FIPS consists of an electrostatic analyzer (ESA), located at the
           entrance to the sensor, a post-acceleration chamber between the
           output of the ESA and the carbon foil, and a time-of-flight
           telescope.  The ESA at the entrance to the FIPS acts as a wide-angle
           lens for ions.  It only allows ions with a specific energy/charge
           band to enter through its output plane.  This band is stepped once
           per second by changing the deflection voltage of the ESA.  A
           measurement cycle consists of 64 deflection voltage steps in nominal
           mode or 8 in burst mode.  Associated with each step in a scan is a
           voltage setting, a threshold, a settling time, and a duration or
           time interval after which the next voltage step is performed.  Ions
           exit the output plane of the ESA and are then accelerated in the
           post- acceleration chamber.  This acceleration is done to boost
           low-energy ions to penetrate the carbon foil.  The acceleration also
           helps to reduce energy straggling and angular scattering - effects
           that cause degradation in mass resolution and imaging.  The carbon
           foil serves as the source for secondary electrons, which are
           scattered out by the penetration ions.  After penetrating the foil,
           the particle resides within the TOF chamber where velocity and
           incoming angle are computed.  Velocity is determined by the time
           difference between the generation of secondary electrons in the
           start foil and a stop surface, and angle is determined by spatially
           imaging the position of the generation of the start secondary
           electrons.  From the velocity, energy per charge, and the
           post-acceleration potential, it is then possible to calculate the
           mass per charge.  The measured species for the FIPS range from H to
           Fe.
 
           The FIPS instrument provides a single serial stream of event data to
           the EPPS system at rates of up to 50000 events per second.  The EPPS
           software maintains a mass distribution spectrum for the FIPS
           instrument. This spectrum consists of a collection of 256 bins (each
           24 bits wide) that count the number of events corresponding to mass-
           per-charge values. In addition, the software maintains a set of 5
           element energy spectra.  Each FIPS spectrum corresponds to a
           specified mass-per-charge range and consists of 64 24-bit bins.  For
           events whose mass-per-charge values fall within one of the selected
           ranges, an energy value is computed and used to determine which bin
           within the corresponding spectrum to increment. The spectra are
           accumulated over an integral number of voltage scans, after which
           they are compressed and output in telemetry.  FIPS also records 5
           heavy-ion energy-summed images (called velocity distributions) for
           each of the same 5 mass-per-charge values plus one for protons.  A
           commanded number of raw events will be recorded at each scan level.
 
           The EPPS instrument is described in full detail in
           Andrews, et al., 2007.
        