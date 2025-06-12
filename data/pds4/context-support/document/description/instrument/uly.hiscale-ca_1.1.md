
 
 
  Instrument Overview
  ===================
    (adapted from: Lanzerotti, et al. 1992)
 
 The Composition Aperture system (CA; sometimes referred to 
 in the Ulysses project as the "WART") uses a multiparameter 
 detection technique to provide measurements of ion composition 
 in an energy range similar to those of HISCALE LEMS/LEFS. The 
 foil thickness, detector thicknesses, and electronic thresholds 
 were selected to enable the separation of low energy electron
 and ion fluxes at high sensitivity by comparing detector
 responses.
 
 The Composition Aperature telescope is referred to as CA 60, where
 the number indicates the inclination of the telescope axis
 with respect to the spacecraft spin axis.
 The BC detector pairs consist
 of two equal 200 micrometer thick, totally depleted silicon surface
 barrier detectors. The D detector is a thin (5 micrometer) silicon
 detector of the epitaxial type.

 The CA telescope uses detectors D and C as
 an ([Delta]E vs E) telescope, with the B detector operating
 in anticoincidence. The geometrical factor for the DCB
 combination is 0.24 cm^2sr. The logic and discrete energy
 channels for the CA telescope are shown in Table 3.
 Information from the discrete ion composition channels
 listed in Table 3 is used in a priority scheme to identify
 those individual particle events whose energy loss signals
 in detectors D and Care to be pulse-height-analysed (see
 below) and included in the telemetry data stream.
 A rotating four-level priority scheme, shown in Table
 4, is used to balance the CA system response to light and
 heavy ion species.

 The priority scheme uses the species group analyzed
 in the immediate previous event in a given sector to
 establish the relative priorities among the four species
 groups for the current sector. Thus, if there were an irongroup
 event analyzed in the immediate previous spin, the
 fourth column of Table 4 would be operative and shows
 that the priority order for analysis, from the highest to the
 lowest priority, would be an event in the oxygen group,
 the iron group, helium, and protons. Thus, the priority
 scheme insures that a large number of relatively "rare"
 ion species will be presented for analysis.
 In addition to the discrete telescope logic channels
 that are listed Tables 1-3, the singles counting rates in
 the individual detectors are monitored and telemetered
 in a multiplexed mode (Tab. 2). These rates are used
 as engineering monitors of the instrument performance.
 These rates can also be used, if required, to make pulsepileup
 corrections to the coincidence rates.
 
 TABLE 3. Ion composition.
 
 Accum. time(s)
 Channel      Logic                Passband [a]        Sectors   @ 1024 bit/s
 CA 60[b]   W1      Cl D1 C2 D2        0.35-1.0 MeV protons        8            3
 W2      C2 D1 D4 D2 S1     1.0-2.0 MeV protons         8            3
 W3      Cl(D2+S1) C3 D3    0.35-1.0 Me V /nuc. He      8            3
 W4      C3 D1 Sl C4 D3     1.0-5.0 MeV /nuc. He        8            3
 W5      C2 D3 C4 D4        ~ 0.3-1.7 MeV/nuc. C,N,O    8            3
 W6      C4 D2 S2 D4 S3     ~ 1.7-10 MeV/nuc. Fe        8            3
 W7      C2 D4 C4           ~0.2-1.0 MeV /nuc. Fe       8            3
 W8      C4 D3 S3           ~1.0-15 MeV /nuc. Fe        8            3
 Z2                         >=0.5 MeV, Z>=2             4            6
 Z2A                        >~10.0 MeV, Z>=14           4            6
 Z3                         >~2.8 MeV, Z>=6             4            6
 Z4                         >~9.0 MeV, Z>=10            4            6
 
 
 [a] The passbands given here are provisional and subject to refinement as in-flight 
 calibrations arc completed.
 [b] Geometrical factor ~0.24 cm^2 sr
 
 
    References
    ----------
      HISCALE References (cited in Armstrong & Sahi, 1996)
 
      Curtis, D.W., ISPM/Ulysses LAN Data Processing Software
      Status, Dec. 1986.
 
      Gold R.E., LAN Accelerator Calibration Test Plan, August
      1991.
 
      Guynn D.R.  Jr., LAN Experiment Data System Performance and
      Interface Specification, June 1992.
 
      Kohl, J.W., J.H.  Crawford, Calibration of Solar Polar Energy
      Model LAN-2B Detector Head at GSFC Low Energy Accelerator,
      July 1986.
 
      Simnett, G.M., R.E.  Gold, The RTG Background in the LAN
      Experiment and the Shielding Required to Control It, April
      1980.
 
      Tappin, S.J., HSIO-HiScale I/O Library, June 1991.
 
      Ximenez de Ferran S., Ulysses Spin Reference Pulse, May
      1985.
        