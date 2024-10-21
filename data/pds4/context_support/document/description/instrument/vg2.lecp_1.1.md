
 
      INSTRUMENT: LOW ENERGY CHARGED PARTICLE
      SPACECRAFT: VOYAGER 2
 
      Instrument Information
      ======================
      Instrument Id                  : LECP
      Instrument Host Id             : VG2
      PI Pds User Id                 : KRIMIGIS
      PI Full Name                   : STAMITIOS M. KRIMIGIS
      Instrument Name                : LOW ENERGY CHARGED PARTICLE
      Instrument Type                : CHARGED PARTICLE ANALYZER
      Build Date                     : 1977-08-20
      Instrument Mass                : 6.652000
      Instrument Length              : UNK
      Instrument Width               : UNK
      Instrument Height              : UNK
      Instrument Serial Number       : 01
      Instrument Manufacturer Name   : JOHNS HOPKINS UNIVERSITY
                                       APPLIED PHYSICS LABORATORY
 
      Instrument Overview
      ===================
      The low energy charged particle experiment employs a set of
      many solid state detectors arranged to characterize, with
      various levels of energy, directional, and compositional
      discriminations, the in-situ charged particle environment of
      the spacecraft, both within interplanetary and planetary
      magnetospheric regions. Electrons can be characterized, with
      various electron rate energy channels, between 22 keV and
      greater than 10 meV (mode dependent). Ions, without mass
      species discriminations, can be characterized with various ion
      rate energy channels between 28 keV and greater than 152 keV
      (mode dependent). Rate data is telemetered as simple counts
      per accumulation time period. The different channels
      correspond to different onboard energy discrimination windows
      (for ions the discrimination values are mass species
      dependent, leading to some ambiguity). Above about 200
      keV/nucleon, the ions can be discriminated as to their mass
      species composition by the use of multiple parameter
      measurements. These measurements consist of the energies that
      individual particles deposit in more than one detector. This
      information is telemetered both as ion rate data, obtained by
      on-board species identification circuitry (with various
      channels representing various energy-species combinations),
      and as particle multiple parameters data, consisting of pulse-
      height-analysis values from each of the affected particle
      detectors for each analyzed particle. (A maximum of about 2 to
      5 particles per second can be analyzed in this fashion due to
      telemetry limitations. A priority scheme avoids saturation by
      one species group. there are three such groups defined: atomic
      number z = 1,2 each group in a rotating fashion.) Angular
      information is obtained through mechanical rotation of the
      detectors. The main detectors look within a single scan plane
      that is rotated 360 degrees, stopping at 8 different look
      sectors (one of the sectors is blocked to obtain a background
      measurement: sector 8). The lower energy detectors have full
      width viewcones of about 45 degrees. The scan plane is
      oriented such that a line that passes exactly between sectors
      8 and 1, and also exactly between sectors 4 and 5, is exactly
      parallel to the roll axis of the spacecraft (which nominally
      points at earth). When the roll orientation of the spacecraft
      is such that the star sensor is locked on canopus, the scan
      plane is tilted about 30 degrees out of the ecliptic plane,
      with sector 3 tilting towards north ecliptic (and also in the
      direction that is retrograde with respect to the planetary
      orbits). Sectors 1 and 8 point in the general direction of
      earth. The scan rate is variable between 48 seconds to 48
      minutes per 360 degree scan. There are some electron detectors
      (whose properties are not as well established as the others)
      that view out of the scan plane described here (see
      [KRIMIGISETAL1977]). Some of the data is subject to
      substantial contamination depending on the region under
      consideration. Before the data from this instrument can be
      used, it is vital that the contamination descriptions be
      examined ('CONTAMINATION_ DESC') for each contamination type
      ('CONTAMINATION_ID') and that the contaminations levels be
      determined ('DATA_QUALITY_ID' AND 'DATA_QUALITY_DESC'). While
      sector 8 is the background sector for most (and generally the
      most used) data channels, sector 4 is the background sector
      for some channels. Of those channels documented in this
      catalog, sector 4 is the background sector for channels: ESA0,
      ESB0, AB10, AB12, AB13, PSA1, PSA2, PSA3, PSB1, PSB2, and PSB3.
 
      Science Objectives
      ==================
      Characterize the energy spectra, angular distributions,
      species composition, spatial structures, and temporal
      variations of the hot plasmas, energetic particles, and
      particulate radiation that exist in the vicinity of the outer
      planets (Jupiter, Saturn, Uranus, and Neptune) and within the
      interplanetary environment. To study the mechanisms by which
      such particles are energized and transported throughout such
      systems. To study in particular the energization and transport
      processes associated with hot plasmas and particulate
      radiation in the vicinity of planetary bow shocks,
      magnetopauses, magnetotail plasma sheets, inner radiation
      zones, the auroral zones, etc., and to study the interaction
      of such media with planetary satellites and the planetary
      atmospheres and ionospheres.
 
      Operational Considerations
      ==========================
      Instrument operates continuously sampling data over uniform
      accumulation intervals. The accumulation intervals are
      different for the different channels of information (almost
      100 channels). The scan head of the LECP Instrument usually
      scans back-and-forth continuously (forward by 315 degrees and
      then back by 315 degrees). The scanning head pauses at 8
      different scan sectors for periods ranging between 6 seconds
      and 48 seconds (for the encounter time periods) and takes
      about 0.5 seconds to scan between the sectors. Specially
      scanning modes for Voyager 2 at Uranus and Neptune have been
      developed whereby 1 or 2 quick scans are performed followed by
      6 to 12 minutes of no scanning. Also, for Voyager 2 at Jupiter
      there was an extended period of no scanning. The roll
      orientation of the spacecraft is of crucial importance as to
      the type of data returned since that orientation determines
      the orientation of the scan plane of the LECP Instrument. That
      orientation also has safety consequences since a poor
      orientation could expose the LECP detectors to ring
      particulate damage.
 
      Calibration
      ===========
      The instrument was calibrated on the ground by placing it into
      beam chambers (e.g. Van DeGraf machines) and firing calibrated
      beams of known composition at it. Also, a radioactive source
      is positioned behind the 'sunshield' positioned at sector 8
      for in-flight calibration of some detector-electronic gains.
      Also, the instrument has a calibration mode whereby pulses of
      known strength are sent into the pre-amplifier chains
      following the detectors. Information about calibration can be
      found in: [KRIMIGSETAL1977], [KRIMIGISETAL1981],
      [ARMSTRONGETAL1981], and [HAMILTONETAL1981].
 
      'LECP' Detector
      ===============
      Total Fovs                     : 8
      Data Rate                      : 600
      Scan Mode Id                   : UNK
      Sample Bits                    : 10
 
      Detector Type                  : SOLID STATE
      Detector Aspect Ratio          : 0.000000
      Nominal Operating Temperature  : 273.000000
 
      The LECP Instrument consists of a variety (about 28) of 'Solid
      State Detectors' that are used individually and in
      combinations (using coincidence and anti-coincidence
      criterion) to detect and characterize nuclear particles. The
      detector thicknesses range from 2 to 2450 microns to cover a
      very broad range of particle energy and mass characteristic.
 
      Detectors count particles that have appropriate discriminated
      characteristics with an efficiency that approaches 1.
      Therefore the sensitivity is strictly a function of the
      geometric factors of the detectors (geometric factors
      associated with different data channels are documented
      elsewhere in this catalog) and the energy and species band-
      widths of the data channels (also documented elsewhere). The
      geometric factors have units of area X Steradians (CM^2 X
      STR).
 
      'LECP' Section Parameter 'ELECTRON RATE'
      ----------------------------------------
      Instrument Parameter Name      : ELECTRON RATE
      Sampling Parameter Name        : ENERGY PER NUCLEON
      Instrument Parameter Unit      : COUNTS/SECOND
      Minimum Instrument Parameter   : 0.000000
      Maximum Instrument Parameter   : 0.000000
      Minimum Sampling Parameter     : 0.022000
      Maximum Sampling Parameter     : 20.000000
      Noise Level                    : 0.000000
      Sampling Parameter Interval    : 0.000000
      Sampling Parameter Resolution  : 0.000000
      Sampling Parameter Unit        : MEV PER NUCLEON
 
      A measured parameter equaling the number of electrons hitting
      a particle detector per specified accumulation interval. The
      counted electrons may or may not be discriminated as to their
      energies (e.g. greater than E1, or between E1 and E2).
 
      'LECP' Section Parameter 'ION RATE'
      -----------------------------------
      Instrument Parameter Name      : ION RATE
      Sampling Parameter Name        : ATOMIC NUMBER
      Instrument Parameter Unit      : COUNTS/SECOND
      Minimum Instrument Parameter   : 0.000000
      Maximum Instrument Parameter   : 0.000000
      Minimum Sampling Parameter     : 1.000000
      Maximum Sampling Parameter     : 26.000000
      Noise Level                    : 0.000000
      Sampling Parameter Interval    : 0.000000
      Sampling Parameter Resolution  : 0.000000
      Sampling Parameter Unit        : ATOMIC NUMBER
 
      A measured parameter equaling the number of ions striking a
      particle detector per specified accumulation interval. The
      counted ions may or may not be discriminated as to their
      energies (e.g. energy/nucleon or energy/charge between E1 and
      E2 or greater than E1) and/or as to their ion composition
      (atomic number Z or mass number greater than Z1 or M1, or
      between Z1 and Z2 or M1 and M2).
 
      'LECP' Section Parameter 'PARTICLE MULTIPLE PARAMETERS'
      -------------------------------------------------------
      Instrument Parameter Name      : PARTICLE MULTIPLE PARAMETERS
      Sampling Parameter Name        : ATOMIC NUMBER
      Instrument Parameter Unit      : MEV X MEV
      Minimum Instrument Parameter   : 0.000000
      Maximum Instrument Parameter   : 0.000000
      Minimum Sampling Parameter     : 1.000000
      Maximum Sampling Parameter     : 26.000000
      Noise Level                    : 0.000000
      Sampling Parameter Interval    : 0.000000
      Sampling Parameter Resolution  : 0.000000
      Sampling Parameter Unit        : ATOMIC NUMBER
 
      A set of measured parameters which yield multiple pieces of
      information about each particle (generally ions) that Q enters
      the system. These pieces of information can, for example,
      consist of the energy deposited by a single particle in two or
      more separate detectors, or the time-of-flight between two
      different detectors plus the energy deposited in a third, etc..
      The multiple pieces of information can be used to perform mass,
      atomic number, and/or charge state discriminations on ions. The
      information can be discriminated on-board and telemetered in
      the form of ion rate channels, or the multiple information
      about each particle analyzed can be telemetered for obtaining
      the finest species discriminations.
 
      (the following table is excerpted from: [MAUKETAL1991])
 
           TABLE 1. Voyager 2 LECP Channel Characteristics
      ----------------------------------------------------------
                             Effective
                               Field
                                of        Energy
        Channel    Species,    View,     Passband,*  [epsilon]G,
      Designation     Z         deg     MeV/nucleon    cm^2 sr
      ----------------------------------------------------------
                         Ion/Proton Channels
            PL01    Z>=1        45      0.028-0.043   1.13x10^-1
            PL02    Z>=1        45      0.043-0.080   1.13x10^-1
            PL03    Z>=1        45      0.080-0.137   1.13x10^-1
            PL04    Z>=1        45      0.137-0.215   1.13x10^-1
            PL05    Z>=1        45      0.215-0.540   1.13x10^-1
            PL06    Z>=1        45      0.54-0.99     1.13x10^-1
            PL07    Z>=1        45      0.99-2.14     1.13x10^-1
            PL08    Z>=1        45      2.14-3.5      1.13x10^-1
              39    Z>=2        60      0.035-0.069**  9.7x10^-2
              38    Z>=6        60      0.069-0.20**   9.7x10^-2
              32    Z=1         60      0.33-0.61      2.6x10^-3
               1    Z=1         60      0.52-1.45      4.4x10^-1
              33    Z=2         60      0.23-0.48      9.7x10^-2
 
                    Electron Channels
       E[beta]01                45      0.022-0.035      6x10^-3
       E[beta]02                45      0.035-0.061      6x10^-3
       E[beta]03                45      0.061-0.112      6x10^-3
       E[beta]04                45      0.112-0.183    3.9x10^-3
       E[beta]05                45      0.183-0.5        2x10^-3
      E[gamma]06                45     >0.252          8.1x10^-3***
      E[gamma]07                45     >0.480          3.5x10^-3***
      E[gamma]08                45     >0.853          1.7x10^-4***
      E[gamma]09                45     >1.20
      ----------------------------------------------------------
         Note: this table shows only a subset (the most commonly
      used) of the channels available.
 
         * For Z>=1 channels, passband is given for protons only.
        ** Indicates oxygen passband.
       *** [epsilon]G for the difference between adjacent integral
           channels.
 
      Electronics
      ===========
      Timed accumulations of particle counts satisfying various
      analog pulse-height discrimination levels. Timed accumulations
      of particle counts satisfying simultaneous analog pulse-height
      discriminations for multiple detectors. Pulse-height analog-to-
      digital conversions from multiple, simultaneous detectors for
      direct telemetry.
 
      'LECP' Detector Operational Modes
      =================================
 
      FAR ENCOUNTER
      -------------
      Data Path Type                 : UNK
      Instrument Power Consumption   : 4.725000
 
      Used in the vicinity of planetary encounters. High intensity
      detectors turned off (A, B, DELTA, DELTA PRIME). (Affected
      channels are documented in detailed level catalog.) Bit Rate
      allocated 1/3 for Particle Multiple Parameters (PMP) data, also
      called Pulse Height Analysis data, and 2/3 for Rate data
      (counts/second). Full composition discrimination capabilities
      enabled (in both Rate and PMP forms). Angular scanning is
      typically 6.4 minutes per 360 degree scan but is often changed.
      Experiment Bit Rate is 600 bits per second. Electrons measured
      up to 0.5 MEV. minimum sample time is 0.4 sec.
 
      FAR ENCOUNTER STOW
      ------------------
      Data Path Type                   : UNK
      Instrument Power Consumption     : 4.725000
 
      This mode includes the Full Far Encounter Mode configuration
      with the exception that the angular scanning is halted so that
      the detectors are fixed looking into a non-standard direction.
      This direction is such that the detectors peek around a sun
      screen (which covers the sector 8 position of the scan plane)
      having the effect of protecting the low energy ion and
      electron detectors by reducing their geometric factors. For
      the one application of this mode the geometric factor was
      reduced by a factor of 26 for the low energy ions (Alpha
      detector) and by an as yet uncalibrated factor for the
      electrons (Beta and Gamma detectors).
 
      NEAR ENCOUNTER
      --------------
      Data Path Type                 : UNK
      Instrument Power Consumption   : 4.525000
 
      Sometimes used at the closest-in positions during a planetary
      encounter. The high intensity detectors are turned on (A, B,
      DELTA, DELTA PRIME). (Affected channels are documented in the
      detailed level catalog.) Particle Multiple Parameter (PMP)
      composition discrimination capabilities are turned off
      (including the rate channels derived from the multiple para-
      meter information). All data appears in rate (counts/second)
      form. Angular scanning is typically 6.4 minutes per 360
      degrees scan but is often changed. Scanning cyclics driven by
      the spacecraft computer are included. Experiment Bit Rate is
      600 bits per second. Electrons are measured up to greater than
      10 MEV. Minimum sample time is 0.4 sec.
 
      URANUS SCAN CYCLIC
      ------------------
      Data Path Type                   : UNK
      Instrument Power Consumption     : 4.725000
 
      Data accumulated as with the Far Encounter Mode. Angular
      scanning controlled by spacecraft. Two quick full angular
      scans are obtained using 6 second scanning and lasting for 96
      seconds total. In between these scan periods the sensors are
      held fixed looking in sector 7. The scan periods occur every
      12 minutes.
 
      Instrument Mounting
      ===================
      LECP Instrument is mounted on the science boom about half way
      between the boom's spacecraft anchor point and imaging scan
      platform. The mounting is such that the 360 degree scan plane
      of the LECP scanning head (not to be confused with the
      scanning of the imaging instruments) is coplanar with the
      spacecraft's roll axis. Also, on the Canopus star lock the
      LECP scan plane is about 30 degrees rotated away from the
      ecliptic plane. A line passing between sectors 1 and 8, and
      between sectors 4 and 5, is parallel to the spacecraft roll
      axis. Sectors 1 and 8 point in the general direction or earth,
      and with the Canopus lock, sector 3 points generally in the
      retrograde direction (referring to the direction with respect
      to the directions of motion of the orbiting planets) and about
      30 degrees north of the ecliptic.

        