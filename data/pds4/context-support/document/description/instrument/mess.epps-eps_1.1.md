
           The Energetic Particle Spectrometer (EPS) is part of the MESSENGER 
           Energetic Particle and Plasma Spectrometer (EPPS) system, which 
           which also includes the Fast Imaging Plasma Spectrometer (FIPS).
           EPS covers the energy range of 25 to > 500 keV for electrons, 
           and 10 keV/nucleon to ~3 MeV total energy for ions. The desired
           throughput for FIPS charged particle and EPS event processing is 5
           kHz. The Johns Hopkins University/Applied Physics Laboratory
           constructed the EPS instrument.
 
           The EPS determines the distributions of the higher-energy
           magnetospheric ion and electrons, including the composition of the
           ions, to characterize the nature of the planetary field of Mercury.
           It does this by measuring the energy and velocity of the particles
           and then using a look-up table to determine the mass and therefore
           the species of particle. The measured species for the EPS include
           H, He, CNO, Fe, and electrons. Electrons are measured by solid-
           state detectors behind absorbing aluminum flashing.
 
           The EPS sensor consists of a 60-mm diameter, tuna-can-like
           cylinder, in which a start foil and stop foil, wrapped around
           opposite curved sides of the cylinder, constitute the TOF chamber.
           An incoming particle hits the start foil and scatters one or more
           electron, which is attracted to the start-anode ground.  The
           particle continues and hits the stop foil, scattering other
           electrons, which are then attracted to the stop-anode ground. The
           solid-state detectors outside of, but wrapped around the curved
           face of, the stop foil, then detect the particle and measure the
           energy state.
 
           The detectors are arranged so that each detector senses the events
           within a given range of incidence angles.  Each of the 6 detector
           modules is composed of 4 pixels: large and small ion and large and
           small electron. This provides 24 detector elements. At any one
           time, 12 of the 24 elements are used (6 ion and 6 electron
           detectors). Each of the 6 EPS detector modules also maintains its
           own spectrum via 64 16-bit bins. 63 bins will count the
           particle/energy combinations of interest, and 1 will count the
           remaining background events that do not fall in the particle/energy
           combinations of interest. The spectra are accumulated over a time
           set by ground command, after which they are compressed and reported
           in telemetry.
 
           The EPS system also includes 32 16-bit rate counters and 3 24-bit
           rate counters that are read by the EPPS software every n seconds (n
           specified by command). EPS status and housekeeping data such as
           voltages, currents, and temperatures are also periodically sampled.
 
           The EPPS instrument is described in full detail in
           Andrews, et al., 2007.
        