
 
  Instrument Overview
  ===================
 
    The MIRO instrument will provide both very sensitive continuum
    capability for temperature determination and extremely high-
    resolution spectroscopy for observation of molecular species.
    The MIRO instrument consists of two heterodyne radiometers, one
    at millimeter wavelengths (1.3 mm) and one at submillimeter
    wavelengths (0.5 mm). The millimeter and the sub-millmeter
    radiometers have continuum bandwidths of 0.5 GHz and 1.0 GHz
    respectively in addition, the submillimeter receiver has a total
    spectroscopic bandwidth of 180 MHz and a spectral resolution of
    44 kHz. In the spectroscopic mode, 4096 channels, each having a
    bandwidth of 44 kHz, are observed simultaneously.
 
  Instrument Summary
  ==================
 
    The performance parameters that govern the MIRO instrument
    design include system sensitivity, spatial resolution,
    radiometric accuracy (both absolute and relative), beam pattern
    and pointing accuracy, together with the mass, power, volume
    envelope, and environmental conditions available within the
    spacecraft.  The MIRO instrument performance characteristics
    are summarised in Table below.
 
 Equipment       Property               MM-Wave         SubMM-Wave
 
 Telescope     Primary Diameter          30 cm           30 cm
               Primary F/D                 1               1
               Sidelobes                -30 dB          -30 dB
               Spatial Resolution      24 arcmin       8 arcmin
               Footprint (at 2 km)       ~15 m           ~5 m
 
 Spectral      Freq Band              188.5-191.5GHz  547.5-580.5GHz
 Performance   1st IF Bandwidth          550MHz          11GHz
               1st IF Freq Rng          1-1.5GHz       5.5-16.5GHz
               Spectral Resolution        n/a            44 kHz
               Spectral Rng per line      n/a         nominally 20 MHz
               Accuracy                   n/a            10 kHz
 
 Spectrometer  Center Freq/Bandwidth      n/a           1350/180 MHz
               Number of channels         n/a              4096
 
 Radiometric   DSB Receiver Noise        800 K            3800 K
 Performance   Temperature
               SSB Spectroscopic Sens
               (300 KHz, 2 min)
                relative                  n/a            2 Krms
                absolute                  n/a            3 Krms
               Continuum Sens (1 sec):
                relative                 1 Krms          1 Krms
                absolute                 3 Krms          3 Krms
 
 Data Rates    Instantaneous Rate
               Continuum Mode                           <1 kbps
               Spectroscopic Mode                        2 kbps
               On-board Storage                          0.2 Gb (1)
 
 (1) One day's data volume, Mode 3, 100 Duty cycle, see Vol 6., Table
     6.3.1-1)
 
 Abbreviations used in above:
   Freq = Frequency
   Rng = Range
   Sens = Sensitivity
 
  MIRO Data Modes
  ===============
 
    The MIRO instrument has 6 major modes of operation and data-
    taking that reflect operational combinations of its two continuum
    radiometers and the spectrometer, engineering mode, millimeter
    continuum mode, submillimeter continuum mode, dual continuum
    mode, CTS/submillimeter continuum mode, and CTS/dual continuum
    mode.
    In addition, a special mode has been designed for planetary and
    asteroid flybys.  A number of data compression options are
    obtained in each mode by varying the data-taking rate (integration
    time per sample) and/or spectral resolution of the radiometers
    and spectrometer. The parameters for each mode are summarized
    below. For more details, see the MIRO User Manual (AD4 of the
    EAICD, RO-MIR-IF-0001_14), Volume 6.1.
 
      1. Engineering Mode
        In engineering mode the MIRO software is collecting
        engineering data from 56 internal sensors. The sampling of
        these sensors is at a 5 Hz rate. All engineering measurements
        are 12-bit A/D converted values. The engineering mode
        telemetry is sent to the spacecraft in the form of a
        housekeeping telemetry packet. One engineering telemetry
        packet is typically generated every 11 seconds.
 
      2. Millimeter Continuum Mode
        In millimeter continuum mode continuum data are collected from
        the millimeter radiometer at a 20 Hz. rate. All continuum data
        consist of 16-bit values. The millimeter continuum data are
        nominally packetized into science telemetry packets every 10
        seconds. A 'summing value' parameter can cause the MIRO
        software to sum either 1, 2, 5, 10 or 20 separate continuum
        values prior to putting them into the telemetry packet. This
        feature can reduce the data rate to as little as one
        millimeter continuum packet every 200 seconds.
 
      3. Submillimeter Continuum Mode
        Submillimeter continuum mode is identical to the millimeter
        continuum mode in data collection and packing, except that a
        different set of electronics is powered on.   Millimeter and
        submillimeter continuum data are contained in separate science
        telemetry packets, identified by a field in the source data
        header.
 
      4. Dual Continuum Mode
        In dual continuum mode the millimeter and submillimeter
        continuum are collected simultaneously.  When running in dual
        continuumvmode, the summing value parameter mentioned earlier
        is applied to both sets of data, causing equal amounts of
        millimeter and submillimeter data to be generated.
 
      5. CTS / Submillimeter Continuum Mode
        This mode adds the collection of chirp transform spectrometer
        (CTS) data. The CTS is programmed by the MIRO software to run
        for an initial sub-integration period of approximately 5
        seconds. An internal LO frequency generator is then switched
        and another 5 second period is observed. These pairs of
        observations are repeated with the respective results being
        summed over time. Selectable integration periods are 30, 60,
        90 and 120 seconds. The data from the two LO frequencies are
        then subtracted from each other to provide a single
        4096-element difference  spectrum. The 4096 data values can
        be further reduced by application of a smoothing function
        whereby data from several channels are combined and weighted
        to produce fewer final channels. Smoothing window sizes are 1,
        5, 7 and 9 channels. A mask is applied to the CTS data and
        only 12 bits of each resulting measurement are returned. CTS
        data collection and the LO frequency switching is
        coordinated with the collection of continuum data. Exactly 100
        continuum samples are taken during each CTS scan. Upon
        receipt of the data on the ground it is known at which LO
        frequency all of the continuum measurements were made at. If
        the CTS has just been powered on, an internal calibration of
        the CTS is performed. This consists of loading the 4 CTS sum
        of square tables with a linear ramping pattern. A 10,000 cycle
        integration is then performed and the resulting data read out.
        The data are then averaged to yield the mid-point of the
        table. The resulting mid-point values for each table are
        downlinked in telemetry packets for monitoring over time.
 
      6. CTS / Dual Continuum Mode
        This is the same as the CTS / SMM continuum mode except that
        the millimeter data are also collected.
 
      7. Asteroid Mode
        This special data-taking mode has been implemented for the
        asteroid and planetary encounters to enable MIRO to follow the
        rapid Doppler shift of spectral lines that may be visible. The
        primary characteristic of this mode is that LO frequency
        switching is turned off. The LO is set to either +5 MHz or - 5
        MHz from the nominal frequency prior to the encounter. At the
        specified encounter time, the LO frequency is switched _ 5 Mhz
        (opposite from the first setting) from the nominal frequency.
        Continuum data are collected at 20 Hz. Each set of CTS data
        consists of a single 5-second integration with all 32 bits
        returned for each 4096 channels.

        