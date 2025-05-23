
 
 
  Instrument Overview
  ===================
    The High Resolution Imaging Science Experiment (HiRISE) is one of
    the remote sensing instruments on the Mars Reconnaissance Orbiter
    (MRO) spacecraft that acquires orbital observations of the Martian
    surface during a two earth-year primary mapping phase.  MRO,
    successfully launched in August 2005, arrived at Mars in March
    2006.  Following orbit insertion the spacecraft went into an
    aerobraking period to achieve a 250 x 315 kilometer near-polar
    orbit suitable for the Primary Science Phase (PSP) mapping that
    started in November 2006.  Since the start of PSP HiRISE has been
    continuously operating acquiring 5-20 observations per day.
 
    The HiRISE camera is a pushbroom imaging system featuring a 0.5 m
    aperture telescope with a 12 m focal effective length and 14 CCD
    detectors capable of generating images of up to 20,000 cross-scan
    observation pixels (exclusive of overlap pixels) and 65,000
    unbinned scan lines. The HiRISE instrument capabilities include
    the acquisition of: (1) observations of the Mars surface from
    orbit with a ground sampling dimension between 25 and 32 cm/pixel,
    depending on the orbital altitude, along with an intrinsic point
    spread function of 1.4 pixels (full width at half maximum assuming
    no spacecraft jitter) and high signal-to-noise ratio (SNR), (2)
    high-resolution topographic data from stereo observations with a
    vertical precision of ~0.2 m over areas of ~5x5 pixels (~1.5 m),
    and (3) observations in 3 colors with high radiometric fidelity. A
    key instrument design feature includes Charge Couple Device (CCD)
    detectors with up to 128 lines of Time Delay and Integration (TDI)
    to create high (>100:1) SNR in the Red filter bandpass anywhere on
    Mars. At the nominal 300 km MRO orbital altitude the instrument
    can acquire image swaths of approximately 6 kilometers cross-orbit
    and 20 kilometers along-orbit.
 
 
  Scientific Objectives
  =====================
    The high-level science objectives of MRO are to 1) characterize
    the current climate and mechanisms of climate change, 2) determine
    the nature of complex layered terrain, 3) identify water-related
    landforms, 4) search for sites showing evidence for aqueous and/or
    hydrothermal activity, and 5) identify and characterize sites with
    the highest potential for landed science and sample return by
    future missions. Given these objectives, the key HiRISE
    capabilities in order of priority are:
 
    1) Achieve the best possible spatial resolution and detection of
    surface features. With a ground sampling dimension between 25 and
    32 cm/pixel along with a narrow point-spread function (PSF) and
    high signal to noise ratio (SNR) we can detect most 1-meter-scale
    objects or landforms with dimensions of 2 meters. The HiRISE PSF
    is less then 2 pixels wide at half max when spacecraft jitter is
    negligible.
 
    2) Achieve high-resolution topographic data from stereo images and
    Digital Elevation Models (DEMs). HiRISE can achieve a vertical
    precison of ~0.2 m over areas of ~5x5 pixels (~1.5 meters).
 
    3) Acquire observations in three colors with high radiometric
    fidelity, for photometric studies such as identification of
    color/albedo units and photoclinometry.
 
 
  Calibration and Measured Parameters
  ===================================
    The radiometric calibration-correction procedure is described here
    at a high level. A detailed description will be provided in a
    future HiRISE calibration paper. The radiometric calibration
    correction is performed on each individual HiRISE channel file
    (EDR) correcting for instrument offset, dark current, gain, then
    converting to I/F reflectance.
 
    The first step in the calibration, carried out by the ISIS
    (Integrated      Software for Imagers and Spectrometers,
    http:/isis.astrogeology.usgs.gov/hical) hiclean program, corrects
    for instrument dark current and offset.  The hiclean program uses
    the ancillary calibration data (dark and mask pixels) that
    accompany the science data to compute corrections in both the
    column (sample) and row (line) directions. The mask pixels,
    positioned at the start of the instrument output, provide dark
    current information for each column.  The dark pixels, positioned
    at the end  of each image row, capture the time dependent dark
    current and offset instrument drift.
 
    The ISIS  program then applies an intra-channel B0 (additive dark
    current matrix) and A0 (multiplicative gain matrix) correction for
    each column in the image array. The hical then converts the pixel
    values to I/F (intensity/flux, I/F = 1 for a 100% ideal lambertian
    reflector viewed normal to the surface) as described below:
 
    For:
      H  = dark current and offset corrected image, output of hiclean
      B0 = intra-channel dark current correction (TDI & BIN dependent)
      A0 = intra-channel gain correction (TDI and BIN dependent)
      G  = global gain correction, normalizes CCD/channels
      L  = observation line time
      I  = I/F conversion factor at Sun-Target distance of 1.5 AU
      AU = Mars-to-Sun distance (AU) at time of observation
      Z  = radiometrically corrected image in I/F units
 
    The correction is:
 
    Z = ([H-(B0?L)]/L)?A0?G*I*(1.5/AU)2
 
    Instrument instabilities result in radiometric mismatches
    requiring additional corrections for the varying column-to-column,
    channel-to- channel, and CCD-to-CCD sensitivities. Residual
    column-to-column variations are corrected by first computing the
    mean value for each   column in an image array. The mean-value
    one-dimensional array is then high-pass filtered to eliminate low-
    frequency information due to scene content.  The result of the
    high pass filter is then subtracted from the image array. CCD
    channels are adjusted to radiometrically match at the seam where
    the two channels come together. The CCDs are then radiometrically
    matched one to the other by matching the overlapping areas of
    adjacent CCDs.
 
 
  Detectors
  =========
    The HiRISE focal plane system consists of 14 independently
    commanded CCD arrays housed in a focal plane substrate of
    aluminum-graphite composite material collocated with CCD
    Processing and Memory Modules (CPMM). Each CCD has 2048 pixels
    (12x12 ?m) in the cross-scan direction and 128 TDI elements
    (stages) in the along-orbit direction. The 14 staggered CCDs
    overlap by 48 pixels at each end (except the outside ends).
 
 
  Electronics
  ===========
    The CCD Processing and Memory Module (CPMM) electronics minimizes
    the number of active and passive components that contribute to
    noise. The analog signal processing chain between the CCD output
    amplifier and the 80 Mega Samples per Second 14 bit (pixel value
    range 0-16,383) Analog to Digital (A/D) converters have been
    designed so that they add less noise than the CCD while being
    radiation tolerant and reasonably low power. Each of the 14 CPMM's
    uses a radiation-hardened Xilinx Virtex 300E Field Programmable
    Gate Array (FPGA) to perform the control, signal processing,
    lookup table compression, data storage, maintenance, and external
    Input/Output. The FPGA is Static Random Access Memory (SRAM) based
    using a Flash Serial Programmable Read Only Memory (SPROM) for
    configuration upon power-up. The SPROM and FPGA are reconfigurable
    so design changes can be applied.
 
 
  Filters
  =======
    HiRISE is a three-color imaging system acquiring observational
    data in blue-green (band center: 500 nm, bandwidth: 200 nm), red
    (band center: 700 nm, bandwidth 300 nm), and near infrared (band
    center: 900 nm, bandwidth 200 nm).
 
 
  Optics
  ======
    The HiRISE design is an all-reflective three mirror astigmatic
    telescope with lightweight Zerodur optics and a graphite-composite
    structure. The Cassegrain design with relay optic and two fold
    mirrors is optimized for diffraction-limited performance.
 
 
  Instrument Modes and Operational Conisderations
  ===============================================
    The 14 CCD detector arrays can be independently commanded offering
    flexibility for how a HiRISE image observation can be acquired.
    Power requirements on the HiRISE instrument allow all 14 CCD
    detectors to be simultaneously operated. Not all 14 CCDs need to
    simultaneously operate to acquire an observation. Depending on the
    type of observation the color filter CCDs may not need to
    participate in the observation, for example if color data is not
    required to satisfy the observational intent.  If a narrower
    cross-orbit swath is desired, the observation may have fewer red-
    filter CCDs operating.
 
    Several data compression methods can be employed to optimize data
    return. The first compression method uses pixel binning where
    adjacent pixels in an image are summed equally in the cross-scan
    and down-scan pixel dimensions (permitted values: unbinned, 2, 3,
    4, 8, 16). Binning reduces data volume and increases the pixel
    SNR, a useful option in low illumination viewing conditions.
    Different binning modes can be specified for each CCD. A typical
    HiRISE red-filter observation might acquire unbinned image data
    for the CCDs in the central portion of the observation where the
    primary target of interest is located while the peripheral CCDs
    may be binned to create a context for the primary target. With
    this flexibility, HiRISE operations can make optimal use of the
    available data-return volume.
 
    A second data compression method converts the 14-bit data stream
    (16-     bit/pixel storage) to 8-bit pixels thereby reducing the
    returned data volume of an observation by half. The conversion to
    8-bit pixels employs look-up tables (LUT) translating the 14-bit
    values to 8-bit. There are 28 onboard command-selectable LUTs
    available. Additionally, an on-the-fly LUT can be defined using
    commanded instrument parameters. Linear and non-linear (square
    root) methods can be used to define the LUT.
 
    A third data compression method employs a lossless data
    compression system not part of the HiRISE instrument hardware.
    MRO's Solid State Recorder (SSR) receives and stores data from the
    HiRISE instrument. A Fast and Efficient Lossless Image Compression
    System (FELICS) FPGA board is located on the interface between the
    HiRISE instrument and the SSR to enable compression of the image
    data before storage on the SSR and subsequent data transmission
    back to Earth.  The FELICS algorithm is expected to offer
    compression ratios ranging 1.7:1 to 2.0:1. FELICS compression is
    applied only to 8-bit pixel data thereby requiring the LUT
    translation to be additionally used.
 
    Additional commanding parameters specify the number of post-binned
    image lines, TDI stages, and the line exposure duration. The
    number of post-binned image lines defines the areal extent of an
    observation in the down-orbit direction while the number of
    commanded CCDs defines the cross-orbit areal extent. The number of
    lines is limited by the instrument buffer space available for
    storing image data (63,000 unbinned lines for 14-bit data, 126,000
    lines for 8-bit data).
 
    The number of TDI stages specifies how many TDI down-scan sensors
    to integrate while acquiring an image observation (permitted
    values are 8, 32, 64, and 128).  The binning mode, viewing
    conditions, and spacecraft jitter are considerations when
    determining the optimal number of TDI stages. TDI stages
    improperly selected may cause image saturation or images with poor
    SNR. High-albedo targets acquired under bright lighting conditions
    may cause image saturation for 128 TDI stages. Conversely,
    observations with low lighting conditions, such as polar
    observations, might use a larger number of TDI stages to increase
    the SNR. If large pixel binning were commanded then the number of
    TDI stages would be reduced to prevent image saturation. Finally,
    the number of TDI stages impacts the effect of spacecraft jitter
    on the point-spread function (PSF) of the image pixels. Effects of
    spacecraft jitter are reduced for fewer TDI stages but also reduce
    SNR.
 
    The line time specifies the time between the generation of
    successive lines. The adjustment of this parameter matches the TDI
    readout with the boresight groundtrack velocity. Line time is the
    same for all CCDs for a given observation.

        