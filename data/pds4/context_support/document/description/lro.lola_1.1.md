
 
INSTRUMENT OVERVIEW
===================
    The LOLA instrument was designed, built and tested by the NASA Goddard
    Space Flight Center (GSFC). The principal investigator is David E. Smith
    (GSFC), and the deputy PI is Maria Zuber (MIT). LOLA has two primary
    objectives.
 
    First, it will produce a high-resolution global topographic model and
    geodetic framework that will assist with precise targeting, safe landing,
    and surface mobility for future scientific and exploration activities.
    LOLA will also characterize the polar illumination environment and image
    the Moon's permanently-shadowed regions (PSRs) to identify possible
    locations of surface ice crystals in shadowed polar craters.
 
    To achieve these primary objectives, LOLA will make three measurements:
 
     1) the distance between the surface and the spacecraft,
     2) the spreading of the returned laser pulse, and
     3) the transmitted and returned laser energies.
 
    LOLA is a pulse detection, time-of-flight laser altimeter. LOLA transmits
    a 5-spot pattern that measures the precise distance to the lunar surface
    at multiple points simultaneously, thus providing 5 profiles across the
    lunar surface (Figure 1).  Each spot within the five-spot pattern has a
    diameter of five meters; the spots are 25 meters apart in the form of a
    cross canted by 26 degrees counterclockwise to provide five adjacent
    profiles.
 
    The 5-spot pattern enables the surface slope to be derived in the along-
    track and across track directions. LOLA's instrument design is similar to
    the designs of the Mars Orbiter Laser Altimeter (SMITHETAL2001B) and the
    Mercury Laser Altimeter (CAVANAUGHETAL2007), augmented by a novel
    diffractive optic element (DOE) (SMITHETAL2009).
 
    It has five beams and five receiver channels, the first of which is also
    fiber-optic-coupled to a Laser Ranging (LR) telescope mounted on the High-
    Gain Antenna. Because LOLA makes global observations, the LOLA altimetry
    data can be used to improve the spacecraft orbit and our knowledge of far
    side lunar gravity, which is currently extremely poorly known but is
    required for precise landing and low-altitude navigation. Timing of one-
    way pulses fired from Earth to the LR will also improve navigation and
    gravity determination.
 
    The five received laser pulses are time stamped with respect to the
    spacecraft mission elapsed time using a set of time-to-digital converters
    at <0.5 ns precision. LOLA measures the transmitted and received pulse
    energies by integrating the pulse waveforms. The on-board science
    algorithm, running on an embedded microprocessor, autonomously adjusts the
    receiver detection threshold levels, detector gain, and range window for
    the lunar surface returns.
 
  ----
 
      #4
               #5
         #1       ---- # shot 3
    #3
            #2
      @4
               @5
         @1       ---- @ shot 2
    @3
            @2
      *4
               *5
         *1       ---- * shot 1
    *3
            *2
 
 
    Figure 1. Spot pattern generated on lunar surface by three successive
    laser shots.
 
 
  INSTRUMENT HARDWARE
  ===================
    The main technical details regarding the instrument are given below.
 
    Mass:                   13 kg
    Power:                  33.5 W (at CDR 7/06)
    Telescopes:             Receiver                18x  Beam Expander
    ----------
    Objective               Sapphire                BK7G18/fused silica DOE
    Aperture Diameter (cm)  14                      3.24
    Focal length (cm):      50                      16.2
    Area:                   0.015 m^2               8.245 cm^2
    Field of view 1/e2      400 urad                100 urad
    Optics transmission     >70%                    >95%
    Bandpass filter:        lambda = 1064.45nm dlambda = 0.7nm FWHM
    LR Bandpass filter:     lambda = 532.15 nm dlambda = 0.3 nm
    Detector/preamplifier:  Si-Avalanche photodiode (APD)
    Detector diameter       0.7 (mm)
    Quantum efficiency      40%
    Noise equivalent power  0.05 pW/Hz1/2
    Electrical bandwidth    100 MHz
    Pulse timing            independent leading and trailing edge times from
                            TDC-S1 ASICs, combined with 5 MHz coarse count.
    Energy monitor          Gated charge-time measurement circuit with
                            digitizer.
 
    Performance:
    Timing resolution       <0.5 ns
    Clock freq. uncertainty <1eE-7
    Laser pulse epoch acc.  <3 ms
    Link margin, 50 km:     5.4 dB (P.D. ~85% at 100 km).
    Range measurement acc.  <0.1 m at 50 km.
    Transmitted energy      relative accuracy (shot to shot): 2% (1 sigma).
    Received energies Er    relative accuracy, 0.1fJ< Er <3 fJ: 12% (1 sigma).
    Laser Oscillators:      Two Cr:Nd:YAG slab cross-Porro resonators.
    Diodes:                 Two 2-bar arrays with thermoelectric cooler (TEC).
    Pumping:                60 A and 140-160 microsecond duration.
    Spatial mode:           TEM00
    Trigger:                Passive Cr4+:YAG q-switch
    Operating range:        5 degrees C to 28 degrees C.
    Pulse width and rate:   6 ns FWHM, 28 Hz.
    Pulse Energy:           2.7 +/- 0.3 mJ
    Wavelength:             1064.30 +/- 0.1 nm
    Beam divergence:        100 urad.
    Beam separation:        500 urad.
    Fiber optics:
    LR fiber-optic bundle parameters:
                            7 fibers, 400um core, 0.22NA, 1.28mm bundle
    Receiver Fiber:         200 um core, 0.22NA
 
  INSTRUMENT MODES
  ================
    The LOLA instrument has four modes, with the following hardware states:
 
    MODE          TELEMETRY     LASER              DETECTOR
    ----          ---------     -----              --------
    MEASUREMENT   HK, Science   Firing enabled,    Active-lunar return counts
                                28 Hz triggers
    STANDBY2      HK, Science   Firing enabled,    Active-LR and noise counts
                                no trigger pulses
    STANDBY1      HK, Science   Laser TEC active,  Active-LR and noise counts
                                capacitors not
                                charged
    OFF           Analog temps  Survival heaters   Inactive
                                enabled
 
    These modes are controlled by the following ground commands:
 
    Mnemonic            APID    Fn Code  Data (Check these bits)
    --------            ----    -------  ----
    LRO_LOLA_PWR         TBD    TBD      0=off; 1=on
    LOLA_LASER_ENABLE    104    2        bit 0 = 0, ON; bit 0 = 1, OFF
    LOLA_LASER_SELECT    104    2        bit 1 = 0, Laser 1;
                                         bit 1 = 1, Laser 2
    LOLA_LASER_FIRE      104    2        bit 2 = 0, Laser fire; bit 2 = 1,
                                                    Laser disable
    LOLA_TEC_ENABLE_1    104    2        bit 3 = 0, enable TEC; bit 3 = 1,
                                                    disable TEC
    LOLA_TEC_ENABLE_2    104    2        bit 4 = 0, enable TEC; bit 4 = 1,
                                                    disable TEC
    LOLA_RESET_ENABLE    104    2        bit 5 = 1
    LOLA_RESET           104    2        bit 6 = 1
    LOLA_ALG_ENABLE      104    2        bit 7 = 0, hold 80K85 prime reset;
                                                    bit 7 = 1, enable
    LOLA_DIAG_ALG_ENABLE 104    2        bit 8 = 0, hold 80K85 redundant
                                                    reset; bit 8 = 1, enable
    LOLA_EEPROM_PROTECT  104    2        bit 9 = 0, inhibit EEPROM writes;
                                                      bit 9 = 1, allow
 
    There are also commands to override thresholds, gains, and range gates
    that are nominally controlled by the FSW algorithm. The algorithm seeks to
    maximize the probability of detection under varying background noise
    conditions, by utilizing hardware noise counters in a fashion similar to
    that employed on the MOLA and MLA instruments. A variable range gate
    setting opens only during the window of time that returns are expected
    from the surface according to the FSW return histograms. To accomodate the
    large dynamic range of lunar return strength, a variable gain amplifier is
    implemented in hardware prior to the discriminator input. The gain is set
    according to tables of range setting - gain setting, one for each
    detector. Earth laser ranges are recorded by detector 1 during the 8 ms
    window preceding each laser fire, approximately 1-9 ms after the start of
    each 28-Hz cycle. The Earth window uses the same threshold and gain
    settings as for lunar ranges. Owing to higher background earth counts,
    especially during New Moon phases, the detector 1 thresholds are likely
    higher than those of the detector 2-5 channels.
 
  ---------------
 
    The data are downlinked to the Ground Data System in the Mission
    Operations Center and are transferred to the LOLA SOC at the end of each
    downlink pass. LOLA ground software assembles the telemetry files into EDR
    data tables, each covering a ~10-minute time period. A housekeeping
    telemetry data stream, which is a subset of the science telemetry, is sent
    to the LOLA SOC in realtime during tracking passes. The realtime
    housekeeping provides energy and signal processing information for the
    pulses generated by the LR component.
 
    The LOLA Measurement Team, Institution, and responsibilities
 
    David E. Smith     GSFC    Lunar coordinate system
    Maria T. Zuber     MIT     Exploration and altimetry
    Oded Aharonson     Caltech Surface roughness, rock sizes
    James W. Head      Brown   Landing sites, geology
    Frank G. Lemoine   GSFC    Orbit and gravity
    Gregory A. Neumann GSFC    Altimetry, radiometry
    Mark Robinson      ASU     Polar ice, landing sites
    Xiaoli Sun         GSFC    Instrument performance

        