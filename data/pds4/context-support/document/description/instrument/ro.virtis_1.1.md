
 
 
  Instrument Overview
  ===================
   VIRTIS stands for Visible Infra Red Thermal Imaging
   Spectrometer, and is part of the ROSETTA orbiter payload. The
   VIRTIS instrument [CORADINIETAL2007] combines a double capability:
   (1) high-resolution visible and infrared imaging in the 0.25-5
   micron range at moderate spectral resolution (VIRTIS-M channel)
   and (2) high-resolution spectroscopy in the 2-5 micron range
   (VIRTIS-H channel). The two channels observe the same areas in
   combined modes to take full advantage of their complementarities.
   VIRTIS-M (named -M in the following) is characterised by a single
   optical head consisting of a Shafer telescope combined with an
   Offner imaging spectrometer and by two bidimensional FPAs: the
   VIS (0.25-1 micron) and IR (1-5 micron). VIRTIS-H (-H) is a
   high-resolution infrared cross-dispersed spectrometer using a
   prism and a grating. The 2-5 micron spectrum is dispersed in 9
   orders on a focal-plane detector array.
 
 
   Technical Description
   =====================
      The instrument is divided into 4 separate modules: the
      Optics Module - which houses the two -M and -H optical
      heads and the Stirling cycle cryocoolers used to cool the
      IR detectors to 70 K -, the two Proximity Electronics
      Modules (PEM) required to drive the two optical heads,
      the Main Electronics Module - which contains the Data
      Handling and Support Unit, for the data storage and
      processing, the power supply and control electronics of
      the cryocoolers and the power supply for the overall
      instrument.
 
   Proximity Electronics Modules Description
   -----------------------------------------
      Each optical head requires specific electronics to drive the
      CCD, the two IRFPAs, the covers, the thermal control; the
      PEMs are two small boxes interfaced directly to the S/C and
      placed in the vicinity of the Optics Module to minimize
      interference noise.
 
   Optics Module Description
   -------------------------
      The -M imaging spectrometer and the -H echelle spectrometer
      optical heads are located inside the Optics Module, which in
      turn is divided into two regions thermally insulated from each
      other by means of MultiLayer Insulation (MLI): the Cold Box
      and the Pallet. The Pallet is mechanically and thermally
      connected to the SpaceCraft; inside the Pallet are located the
      two Stirling cycle cryocoolers. The heat produced by the
      cryocoolers compressors (a maximum of  24 W in closed loop
      mode) is dissipated to the spacecraft. The Cold Box contains
      the two optical heads and its main function is to act as a
      thermal buffer between the Optical Heads, working at 130 K,
      and the external environment (the S/C temperature ranges from
      250 to 320 K). The Cold Box is mechanically connected to the
      Pallet through 8 Titanium rods, whose number and size were
      selected to minimize conductive heat loads and to avoid
      distorsion upon cooling from room temperature. The structural
      part of the cold box is a ledge which is supported by the 8
      titanium rods; on the ledge the two optical heads are
      mechanically fixed. Thermal insulation of the Cold Box is
      improved by means of MLI, while thermal dissipation from the
      Cold Box is achieved by means of a two stage passive radiator:
      the first stage keeps the Cold Box temperature in the range
      120-140 K, while the second stage is splitted in two parts,
      one for each optical head, and allows to reach the required
      130 K. Another important component of the instrument are the
      two covers; they provide a double function: protection against
      dust contamination, internal calibration by means of an
      internally reflecting surface finish. They use a step motor and
      their operation is controlled by the PEMs.
 
    VIRTIS-M Description
    --------------------
      The VIRTIS-M optical head perfectly matches a Shafer telescope
      to an Offner grating spectrometer to disperse a line image
      across two FPAs. The Shafer telescope produces an anastigmatic
      image, while Coma is eliminated by putting the aperture stop
      near the center of curvature of the primary mirror and thus
      making the telescope monocentric. The result is a telescope
      system that relies only on spherical mirrors yet remains
      diffraction limited over an appreciable spectrum and field: at
      +/- 1.8 degrees the spot diameters are less than 6 microns in
      diameter, which is 7 times smaller than the slit width.
      The Offner grating spectrometer allows to cover the visible
      and IR ranges by realising, on a single grating substrate,
      two concentric separate regions having different groove
      densities: the central one, approximately covering 30% of the
      grating area is devoted to the visible spectrum, while the
      external region is used for the IR range. The IR region has a
      larger area as the reflected infrared solar irradiance is quite
      low and is not adequately compensated by the infrared emissions
      of the cold comet.
      The visible region of the grating is laminar with rectangular
      grooves profile, and the groove density is 268 grooves/mm.
      Moreover, to compensate for the low solar energy and low CCD
      quantum efficiency in the ultra-violet and near infrared
      regions, two different groove depths have been used to modify
      the spectral efficiency of the grating. The resulting
      efficiency improves the instrument's dynamic range by
      increasing the S/N at the extreme wavelengths and preventing
      saturation in the central wavelengths.
      Since the infrared channel does not require as high a
      resolution as the visible channel, the lower MTF caused by the
      visible zone's obscuration of the infrared pupil is acceptable;
      the groove density is 54 grooves/mm. In any case, the spot
      diagrams for all visible and infrared wavelengths at all field
      positions are within the dimension of a 40 microns pixel. For
      the infrared zones, a blazed groove profile is used that results
      in a peak efficiency at 5 micron to compensate for the low
      signal levels expected at this wavelength.
 
    VIRTIS-H Description
    --------------------
      In -H the light is collected by an  off-axis parabola and then
      collimated by another  off-axis  parabola before  entering a
      cross-dispersing prism made by  Lithium Fluoride. After exiting
      the prism the light is diffracted by a flat reflection grating
      which disperses in a direction perpendicular to the prism
      dispersion. The prism allows the low groove density grating,
      which is the echelle element of the spectrometer, to achieve
      very high spectral resolution by  separating orders 9 through
      13 across a two-dimensional detector array: the spectral
      resolution varies in each order between 1200 and 3500. Since
      the -H is not an imaging channel, it is only required to achieve
      good optical performance at the zero field position. The focal
      length of the objective is set by the required IFOV and the
      number of pixels allowed for summing. While the telescope is
      F/1.6, the objective is F/1.67 and requires five pixels to be
      summed in the spatial direction to achieve a 1 mrad2 IFOV (5 x
      .45 mrad x .45 mrad).
 
    Main Electronics Module Description
    -----------------------------------
      The Main Electronics is physically separated from the Optics
      Module. It houses the Power supply for all the experiment, the
      cooler electronics, the Spacecraft interface electronics, for
      telemetry and telecommanding, the interfaces with the Optics
      Module subsystems, and the DHSU (Data Handling and Support
      Unit) which is the electronics for the data handling,
      processing and for the instrument control.
      The data processing and the data handling activities into the
      DHSU are performed using an on-line philosophy. The data are
      processed and transferred to the spacecraft in real time. The
      mass memory (SSR) of the spacecraft is used to store or buffer
      a large data volume. The Main Electronics contains no
      additional hardware component for data processing and
      compression. All data processing is performed by software.
 
 
 
  Scientific requirements and activity in the mission phases
  ==========================================================
 
 
     A summary of the scientific requirements needed to define the
     characteristics of VIRTIS is given hereafter.
     Nucleus science objectives:
     1- Identification of different ices and ice mixtures and
        determination of their spatial distribution. This must be
        done in spite of the very low albedo ( <  0.1), due to dark
        inclusions present in the ice and the resulting weak ice
        spectral features, as well as at large distances from the Sun
        during some phases of the mission.
     2- Identification of the carbonaceous materials that probably are
        mixed with water ice, even in low percentages (<20%). The
        associated spectral features will be very subdued and their
        identification, from their shape and centre, will require
        high S/N (>100).  It will be important also to determine the
        overall continuum slopes of the spectra, for the  presence of
        organic compounds will redden the spectra in diagnostic ways
        between 0.4 and 1.1 ?m and into the IR as well.
    3-  Determination of the physical microstructure and nature
        of the surface grains by measuring the spectrophotometric
        phase curve with a relative radiometric accuracy of about 1-%.
        Identification of the silicates, hydrates and other minerals
        which are expected to be found. Strong but broad absorption
        features should be observed from the visible (0.25-1.0 micron)
        to the near IR (1.0-5.0 micron), so a spectral resolution of
        100 is adequate.
    4-  Determination of the spatial distribution of the various
        mineralogical types and their mixtures using both the
        spectral features and the overall brightness.  Local
        fluctuations of the reflectivity and spectral features
        related to small scale compositional differences are
        expected. For global mapping of the nucleus, a spatial
        resolution of a few tens of metres is needed.
    5-  Detection and monitoring of active areas on the comet
        surface (cryo-volcanism) to understand the physical processes
        operating and to identify the material types associated.
        Determination of the composition of ices on the nucleus
        surface. With the exception of H2O, condensed molecules
        display diagnostic narrow (as well as broad) absorption bands
        in the reflected component (1-3 micron). S/N  higher than 100
        and a minimum resolving power of 1000 is needed to resolve
        the bands fully. The -H FOV must be within the field of view
        of one -M frame (accuracy of few arcminutes) to allow combined
        operation at both high spatial  and spectral resolution.
 
  Coma science objectives:
 
    1-  Determination of the global distribution of gas and dust
        in the inner coma. Radiometric accuracy of 10% absolute and
        1% relative with a resolving power of 100 are required.
    2-  Identification and mapping of the strong molecular
        emissions in the near ultraviolet and visible portions of the
        spectrum. These include the main water dissociation product
        OH (0.28 and 0.31 micron), CN, C3, NH, CH and CO+ ions, and
        the neutral radicals CN and C2. The combination of high
        spatial resolution with moderate spectral resolution will
        allow correlation of the evolution of radicals with that of
        their parent molecules.
    3-  Mapping of the composition and evolution of gas and dust
        jets in the coma and comparison  with the mineralogical
        composition and spatial morphology of active regions on the
        surface of the nucleus.
    4-  Determination of  the composition of the dust grains in the
        coma by observing emission features in the fundamental bands
        between 2.5-5 micron. These emissions will be observed mainly
        at the end of the mission, at distances from the Sun of less
        than 2 AU.
    5-  Identification of the gas molecules. The 2-5 micron range
        corresponds to the maximum efficiency of molecular resonant
        fluorescence at fundamental rotational/vibrational bands. A
        major objective is to identify the hydrocarbon emission in
        the  3-4 micron range. Such identification requires a
        resolving power of the order of 2000 at 3.5 micron.
    6-  Assessment of the coma thermodynamic with the
        determination  and mapping the rotational temperatures for the
        individual lines of H2O with an accuracy of 1 K and a nominal
        S/N of 200.
    7-  Detection of early gaseous activity: Spectra will be
        obtained at long integration times, starting before the
        mapping phase, to search for CO emission as an indicator of
        beginning activity. Determination of ortho/para ratio for H2O.
        Long integration should allow a determination of the OPR with
        a S/N ratio of 50 to discriminate among different scenarios
        of comet formation.
    8-  Determination of isotopic ratios for selected molecules,
        such as 13CO, H217O, H218O or HDO.
 
 
 
 
  Calibration measurements
  ========================
 
       Before the integration of the VIRTIS experiment aboard Rosetta,
       a full calibration of the instrument was performed to
       completely characterize the instrumental performances.
       The fundamental calibrations necessary to correctly retrieve
       the scientific information from VIRTIS data are:
    1- Geometric calibration: measurement of IFOV, FOV and in field
       distorsions;
    2- Spectral calibration: correlation between spectral dispersion
       axis of the focal planes with wavelength;
    3- Spatial calibration: evaluation of the flat-field matrices
       necessary to homogenize the focal planes responses;
    4- Radiometric calibration: determination of the Instrument
       Transfer Function (ITF), that allows to convert digital numbers
       (DN) in physical units of spectral radiance (W m-2 micron-1
       sterad-1).
       These quantities, continuously checked during the flight at
       each switch on of the experiment, are used in the data
       pipeline before the scientific analysis.
 
 
 
 
  Principal Investigator
  ======================
 
    Angioletta Coradini
    Istituto Nazionale di Astrofisica, Rome

        