
 
  Instrument Overview
  ===================
    The Imager for Mars Pathfinder (IMP) Windsock Experiment
    consisted of three small devices on the ASI/Met mast that changed
    orientation in response to wind speed and direction.  IMP images
    show changing orientation of the windsocks compared with local
    vertical and the Martian surface, allowing wind velocity at three
    different heights to be measured.
 
    Three IMP windsock units were mounted on the ASI/Met mast at
    heights of 33.1, 62.4, and 91.6 cm above the solar panel.  Total
    mass of all three devices together, including mounting struts,
    was 39g.  The IMP windsocks functioned like conventional
    terrestrial windsocks in that deflection from vertical indicates
    wind speed, and azimuth of deflection indicates wind direction.
    Each windsock consisted of a hollow aluminum cone rigidly joined
    to an aluminum-sheathed steel counterweight spike, which together
    pivoted on a small, low-friction gimbal mount.  Each windsock
    assembly was less than 10 cm long and was mounted (flexibly) at
    the end of a support strut extending 10 cm from the ASI/Met mast.
    The final design was tested in the field and in a wind tunnel at
    one atmosphere, and at equivalent Martian atmospheric pressure in
    the ASU low-pressure wind tunnel at NASA-Ames, and found to be
    aerodynamically stable at all deflection angles and wind speeds.
    Each windsock unit was constructed of electrically conductive
    materials and was grounded to prevent accumulation of static
    charge from affecting windsock deflection.  Matte finishes on the
    aluminum cones and counterweight sheaths produced a very bright
    appearance in IMP images (conductive black paint was added to the
    cone interiors for contrast), so that sharp contrast between
    bright windsock components and darker scene backgrounds helped
    maintain integrity of the windsock appearance in compressed
    images.
 
    Wind speed u is related to windsock deflection theta by equating
    gravitational and aerodynamic torques acting on the windsock
 
                u = sqrt{[2 R(1) M g tan(theta)]/[R(2) A(d) rho]}
    [Equation 1]
 
    where R(1) = distance between pivot and center of mass, M =
    non-counter-balanced mass, g = acceleration of gravity, R(2) =
    distance between pivot and center of aerodynamic pressure, A(d) =
    effective aerodynamic cross-section, and rho = atmospheric
    density (a function of pressure, temperature, and molecular
    weight).  Counterweight length was adjusted until R(1)/R(2) was
    optimized for sensitivity to Martian wind speeds appropriate for
    investigation of aeolian processes.  In practice, it is not
    necessary to calculate R(1), R(2), M, and A(d) (which varies with
    theta) individually. Eq.  [1] allows windsock performance at the
    same deflection theta (thus same A(d)) in different
    atmosphere/gravity environments to be related.  If the windsock
    is deflected theta(1) degrees under two different conditions of
    wind speed, atmospheric density, and gravity, then eq.  [1]
    reduces to
 
                u = Constant(theta(1)) (sqrt(g/rho))
    [Equation 2]
 
    This means that if u is known at theta(1) for conditions g and
    rho, then u for other specified conditions of g and rho can be
    immediately calculated for the same deflection theta(1).  In the
    general case, once the windsock unit is calibrated for u vs.
    theta at conditions g and rho, then u vs.  theta for the same
    deflections can be predicted for other specified conditions of g
    and rho.  This relationship was exploited for calibration and
    derivation of wind speed on the Martian surface.
 
 
  Scientific Objectives
  =====================
    The IMP windsock experiment measured wind speed as a function of
    height close to the surface, where wind energy is transferred to
    potentially mobile materials such as sand and dust.  This
    capability allowed direct measurement of the wind speed profile
    on the Martian surface for the first time.  The objective of this
    experiment was to use this capability to analyze aeolian
    processes at the Pathfinder landing site.  Scientific goals
    included: (1) determination of z(0) (aerodynamic roughness) for
    the landing site and values of u* (wind friction speed); (2)
    monitoring potentially mobile materials (e.g.  drifts, rover
    tracks, airbag scars) in coordination with real-time windsock
    boundary-layer analysis; (3) relating changes observed at the
    landing site to z(0) and values of u*.
 
    Science Background
 
    The importance of aeolian activity on the surface of Mars has
    been well established by telescopic observation, analysis of
    spacecraft imagery, and experimental work.  Variability of
    Martian surface features has been recorded telescopically since
    the nineteenth century, although it was not fully appreciated
    until the advent of spacecraft exploration that variability of
    the planet's surface markings was due primarily to wind-related
    changes [MCLAUGHLIN1954; KUIPER1957; SAGAN&POLLACK1969].
    Regional dust storms can occur in many locations any time during
    the Martian year, while global, planet-encircling dust storms
    originate only during southern spring and summer
    [MARTIN&ZUREK1993].  A planet-encircling dust storm occurs about
    once every three Martian years, with significant interannual
    variation [HABERLE1986; ZUREK&MARTIN1993].  Such a storm was in
    progress when Mariner 9 arrived at Mars in 1971.  As the storm
    abated, surface features were observed that obviously derived
    from wind interactions with the surface, including time-variable
    bright and dark streaks associated with topographic obstructions,
    and dune fields [e.g., SAGANETAL1972; MCCAULEY1973].  Changes in
    variable feature characteristics during the period spanning the
    Mariner 6, 7, 9, and Viking missions indicate that albedo
    variations on Mars are due solely to aeolian effects (and
    sublimation/deposition of volatiles at the poles) [e.g.,
    VEVERKAETAL1974; VEVERKAETAL1977].  Viking Orbiter images
    revealed four major regions of dunes surrounding the north pole
    [CUTTSETAL1976; BREEDETAL1979; TSOARETAL1979; THOMAS1981;
    LANCASTER&GREELE1990].  Smaller deposits of dune-forming
    materials are common in high resolution Viking images, especially
    within craters and other topographic traps [e.g., BREEDETAL1979;
    THOMAS1981; THOMAS1984].  Barchan, star, transverse, and
    longitudinal dunes have been observed and their morphologies and
    orientations used to interpret regional wind patterns [e.g.,
    TSOARETAL1979; BREEDETAL1979; WARD&DOYLE1983;
    EDGETT&BLUMBERG1994; THOMAS&GIERASCH1995; LEE&THOMAS1995].  It is
    not clear whether any of these dune forms are currently active.
    Dune particles are presumably sand-sized [EDGETT&CHRISTENS1991]
    but their composition has not been determined.  Wind tunnel
    experiments indicate improbably strong winds are required for
    direct entrainment of dust-sized particles under Martian
    conditions [GREELEYETAL1980; GREELEY&IVERSEN1985], so the
    mechanism for raising massive quantities of dust during regional
    and global dust storms must be complex, perhaps involving
    saltation and traction of larger, more easily moved particles as
    a triggering mechanism, desorption of volatiles within a dusty
    surface layer, dust devils, and/or a thermally unstable boundary
    layer (reviewed by [GREELEYETAL1992B]).
 
    Accumulations of fine particles deposited and shaped by wind were
    observed at both Viking Lander sites [BINDERETAL1977;
    MUTCHETAL1977; SHARP&MALIN1984].  Orientations of drifts
    correlate reasonably well with highest wind speed directions
    inferred from wind streaks seen from orbit [SAGANETAL1977].
    However, changes to the landing sites during the mission were
    minor.  At the MMS (Mutch Memorial Station, or Viking Lander 1
    site) winds perhaps as high as 50 m/sec affected small artificial
    piles of soil and trenches, but did not perceptibly erode
    previously undisturbed materials; no wind-related morphological
    changes at all were observed at the Lander 2 site
    [ARVIDSONETAL1983; MOORE1985].  Two small mass-movements within
    drift material were recognized at the MMS [JONESETAL1979;
    GUINNESSETAL1982], suggesting that inactive drift material is not
    completely cemented in situ.  One of these mass-movements was
    modified subsequently during the sol 1742 dust storm [MOORE1986].
    Dust deposition and subsequent removal of dust by light winds
    occurred at both landing sites [GUINNESSETAL1982;
    ARVIDSONETAL1983].  The Viking Meteorology Experiment measured
    temperatures and wind speeds from a single location 1.6 m above
    the surface [HESSETAL1977; RYANETAL1978].  Modeling of heat and
    momentum fluxes within the near-surface boundary-layer was
    complicated by unknown aerodynamic roughness, z(0),
    [SUTTONETAL1978; HABERLEETAL1993B; TILLMANETAL1994], a limitation
    of meteorology data being available from only a single height.
    Under these circumstances values of wind friction speed, u*, were
    estimated using a range of assumed values of z(0).  The
    Pathfinder IMP windsock experiment, with three anemometers, has
    the potential to remove this ambiguity, providing an independent
    determination of u* directly from the wind speed profile and
    allowing more constrained modeling of the atmospheric boundary
    layer than previously.
 
 
  Aerodynamic Calibration
  =======================
    The three flight unit windsocks were calibrated at one atmosphere
    and at equivalent Martian atmosphere in the Arizona State
    University planetary geology wind-tunnel at NASA-Ames Research
    Center.  Besides determining the function relating deflection of
    each windsock to wind speed, the variation of this function with
    strut azimuth (e.g., the effect of direct wind 'shadowing' of the
    windsocks by the ASI/Met mast) was measured.
 
    An initial test investigated the effect of dust accumulation on
    calibration stability.  A windsock was first calibrated at one
    atmosphere pressure at speeds causing deflections from 5 to 85
    deg, then was subjected to thick, heavy blowing dust for one
    hour.  The windsock was coated with a patina of dust at the end
    of the run, but subsequent recalibration showed no change in
    performance.
 
    A turntable was used for examining the behavior of each windsock
    at a range of strut azimuths from the mast relative to the wind
    direction.  The adopted convention is that strut azimuth of 0 deg
    extends the windsock strut ahead of the mast, into the wind; 180
    deg azimuth extends the windsock strut directly downwind of the
    mast, placing the windsock in the mast wake.  Strut azimuth
    relative to the wind increases clockwise when viewed from
    overhead.  During experiments at one atmosphere pressure each
    flight unit was photographed simultaneously from horizontal and
    vertical directions at seven strut azimuths and seventeen wind
    speeds, and at five more strut azimuths at seven wind speeds.
    Similar experiments were performed at Martian equivalent
    atmospheric pressure for seven strut azimuths at an average of
    eleven wind speeds.  About 3000 photographs were obtained as part
    of the calibration process for the three flight units.  None of
    the 1500 vertical (from overhead) pictures revealed any tendency
    for the windsocks to yaw away from the center of the wind tunnel
    slip stream.  Processed negatives for each of the 1500 horizontal
    (from the side) photographs were projected to allow measurement
    of windsock deflection for each wind tunnel speed.  Some minor
    hysteresis (1-2 degrees of deflection at the lowest wind speeds)
    was encountered during early experiments, so all data were
    obtained at both incrementally increasing and decreasing wind
    speeds.  A 'dead zone' deflection (neutral, no wind) of 5-6
    degrees is typical for all three windsocks at all azimuths.
    Equations (1-2) relate performance between terrestrial
    calibrations at different conditions, and between all terrestrial
    calibrations and Martian conditions.  Predictions for Martian
    conditions from terrestrial one-atmosphere and low-pressure
    experiments plot similarly along the same curve for each flight
    windsock.  Windsock sensitivities for Martian atmosphere and
    gravity were from 5-40 m/sec.  This speed range was most relevant
    for studying winds strong enough to move loose particles
    potentially affected by wind.  This speed range was also
    complementary to the single ASI/Met wind sensor, which was
    optimized for precision measurement of winds <5 m/sec.  The most
    sensitive windsock is unit #1, located at the bottom position of
    the array, 0.331 m above the solar panel.  Flight windsock #2 was
    mounted in the middle position, 0.624 m above the solar panel.
    The least sensitive unit, flight windsock #3, was mounted in the
    top position at 0.916 m above the solar panel.
 
    Calibration data are in Appendix I.  None of the images from the
    vertical (downward-looking) camera are included, as inspection of
    these images showed no yaw from the wind tunnel centerline.
    Horizontal (side-looking) pictures are listed by film roll
    number.  Information for each exposure includes windsock flight
    unit number, date and time of exposure, strut azimuth into wind,
    temperature, and pressure.  If the calibration image was obtained
    at one atmosphere, wind tunnel fan speed in Hz is listed along
    with the corresponding laser-Doppler velocimeter wind speed at
    the time of exposure.  If the calibration image was obtained at
    Martian-equivalent pressure, only the wind speed from the
    laser-Doppler velocimeter is listed.  Windsock deflection from
    vertical was measured from every image in at least one trial, and
    these deflections are also included in Appendix I.  It is not
    practical for the PDS to distribute the original processed film
    negatives, but they can be examined for additional measurements,
    if required, by sending email to Dr.  Robert Sullivan at
    sullivan@cuspif.tn.cornell.edu, or regular mail to CRSR, Cornell
    University, Ithaca, NY 14853 (5/99).
 
    During calibration of the flight model IMP, over 650 IMP windsock
    images were obtained in a matrix of 36 strut azimuths (0 to 180
    deg in 5 deg increments) and 18 deflection angles.  A matrix of
    IMP windsock images with varied lighting and background scene
    entropies was also obtained in order to evaluate practical image
    compression limits.  These auxiliary calibration data showing
    windsocks at known orientations allow visual comparisons with
    flight image data obtained on Mars, although this is not
    necessary for data reduction.  As of this writing (5/99) it is
    uncertain whether these and other preflight IMP calibration
    images will be included in the IMP PDS distribution.
 
 
  Operational Considerations
  ==========================
    Four IMP sequences were dedicated to imaging the windsocks during
    mission operations: S0068, S0173, S0174, and S0175.
 
    (1) S0068.  This sequence was designed for use with the IMP in
    its stowed position, after deployment of the ASI/Met mast.  A
    great deal of IMP contingency data were obtained before the IMP
    was deployed to its full height, including a single activation of
    S0068 for imaging the windsock array.  S0068 involved 20 images
    that covered all three windsocks.  IMP pointing uncertainties
    were larger than expected, resulting in partial clipping of the
    windsocks.  Wind-related motion of the windsocks was detected,
    confirming their proper deployment with the ASI/Met mast.
 
    (2) S0173.  This 12-image sequence covered the entire windsock
    array.  This was the main sequence for collecting wind speed
    profile data once IMP was deployed to its full height.  The
    sequence was modified several times early in the mission to
    optimize compression ratio and adjust image cut-out window size
    to compensate for unexpected IMP pointing irregularities.
 
    (3) S0174.  This 3-image sequence was designed for use with the
    IMP in the stowed position, after deployment of the ASI/Met mast.
    The sequence involved looking only at the top windsock, to sample
    wind speed and direction without gathering wind profile data.
    The sequence was activated only once before IMP was deployed.
 
    (4) S0175.  This 6-image sequence was designed to look only at
    the top windsock, to sample wind speed and direction without
    gathering wind profile data.  The sequence was modified several
    times early in the mission to optimize compression ratio and
    adjust image cut-out window size to compensate for unexpected IMP
    pointing irregularities.
 
    All windsock imaging sequences involved rapid, repetitive imaging
    within a single sequence activation.  Repetitive imaging of the
    windsocks over a short time period is necessary for averaging
    short-term fluctuations in wind speed and direction to obtain
    more meaningful wind profile data.  One or more windsocks appear
    by happenstance in other images not intended for windsock
    analysis (sequences S0050, S0053, S0055, and S0166), but without
    rapidly repetitive coverage such images are not very useful for
    windsock analysis.
 
    Windsock images in sequences S0068, S0173, S0174, and S0175 were
    compressed and tightly subframed to conserve downlink.  However,
    the quality of early images from these sequences was adversely
    affected by (1) unexplained/unexpected poor performance of the
    onboard square-root compressor (which converted 12-bit image data
    to 8-bit data); and (2) unexpected IMP pointing irregularities
    which led to clipping of the subframed windsocks.  These problems
    were overcome by using only the onboard JPEG image compressor,
    and increasing the size of the subframe image areas containing
    the windsocks.
 
    Rover and IMP images show that substantial portions of the
    airbags were not completely drawn under the ASI/Met mast solar
    panel.  It is likely that unretracted airbag bulk caused
    aerodynamic interference with the bottom windsock from several
    wind directions.
 
    All IMP images from all windsock sequences (S0068, S0173, S0174,
    and S0175) are listed in Appendix II.  Images containing
    windsocks from sequences S0050, S0053, S0055, and S0166 are also
    listed.  Appendix II includes spacecraft clock time, SCLK, and
    local time of day (LST) for each image.
 
 
  Measured Parameters
  ===================
    The primary data for windsock analysis are IMP images of the
    windsocks.  Description and specifications of the IMP,
    performance of the IMP during mission operations, and
    characteristics of IMP image data are discussed elsewhere in the
    Mars Pathfinder PDS distribution.
 
    Recommended Procedure for Deriving Wind Speed and Direction
 
    IMP orientation relative to local Martian vertical can be
    calculated from IMP elevation angle and the overall lander tilt
    obtained during the mission from onboard accelerometers.  This
    makes windsock deflection theta from true local vertical and
    azimuth phi completely determinable by geometrically transforming
    two measurements in IMP images: (1) apparent foreshortening of
    the windsock; and (2) clock angle of the windsock in the plane of
    the image.  Windsock deflection from vertical can then be
    converted to wind speed u with equation [1] (using simultaneous
    ASI/Met temperature and pressure measurements to calculate
    density rho) and relevant wind tunnel calibration data.  Here is
    a recommended sequence of steps for obtaining wind speed and
    azimuth information from IMP windsock images:
 
    (1) Obtain IMP windsock images.  Consult Appendix II to identify
    and select windsock images from the IMP PDS distribution.
    Appendix II lists all windsock images obtained by activating
    sequences S0050, S0053, S0055, S0068, S0166, S0173, S0174, and
    S0175, with corresponding LST (local solar time) for each image.
    Use sequences S0068 (IMP stowed) and S0173 (IMP deployed) to
    obtain wind profile data using all three windsocks.  Use
    sequences S0174 and S0175 to obtain additional wind speed data
    from the top windsock only.  Other sequences captured the
    windsocks incidental to other purposes, but without rapidly
    repetitive imaging.
 
    (2) Measure the clock angle and foreshortening angle of each
    windsock.  The clock angle is the apparent orientation of the
    windsock in the image plane compared with the image frame
    boundaries.  The foreshortening angle of the windsock is how much
    the windsock is pointing into or out of the image plane.  The
    foreshortening angle of the windsock can be obtained by measuring
    the ratio between the apparent width of the cone base, which is
    independent of orientation, and a windsock length dimension.
    This apparent ratio is then compared with the true ratio of these
    physical dimensions of the windsock.  It is recommended that
    apparent ellipticity of the cone base be used for this purpose.
    This dimension is easier to discern in images than any involving
    the exact location of the counterweight tip, which generally is
    obscured by bright reflections that introduce more ambiguity.
    Consult Windsock.tiff in this PDS distribution for detailed
    information on physical dimensions of a windsock.  Counterweight
    length varied slightly among the flight units (for sensitivity
    tuning) compared with the dimension shown in Windsock.tiff, but
    averaged 0.034 m.
 
    (3) Transform the measured clock and foreshortening angles from
    (1-2) to ground azimuth and deflection-from-vertical angles.
    Trigonometric conversion can be implemented in several ways,
    depending on the needs of the end-user, who will probably want to
    automate this task suited to his/her own research objectives.  At
    the time of this writing (5/99), these are the values best known
    to the author for spacecraft dimensions and orientations: (a)
    azimuth of maximum downward tilt of the spacecraft = 52.8 deg
    clockwise from north; (b) magnitude of the maximum downward
    spacecraft tilt = 4.01 deg; (c) azimuth from the IMP to the
    windsocks, clockwise from north = 126.142 deg; (d) azimuth along
    the windsock struts from the mast to the windsock gimbal joints =
    36 deg clockwise from north (about 90 deg counterclockwise from
    the IMP-to-mast azimuth); (e) downward viewing elevation angle of
    top windsock from IMP = 7.3 deg; (f) distance between IMP and top
    windsock = 1.98 m; (g) downward viewing elevation angle of middle
    windsock from IMP = 16.4 deg; (h) distance between IMP and middle
    windsock = 2.04 m; (i) downward viewing elevation angle of bottom
    windsock from IMP = 23.3 deg; (j) distance between IMP and bottom
    windsock = 2.106 m.  These values may be updated elsewhere as
    part of a subsequent PDS release.
 
    (4) Determine atmospheric density when the windsock image was
    obtained.  Obtain ASI/Met temperature and pressure data from the
    PDS that are as nearly simultaneous as possible with the windsock
    image.  Use the windsock image SCLK and LST values provided in
    Appendix II to locate the most appropriate temperature and
    pressure values from ASI/Met data.  The LST values listed with
    ASI/Met data are only approximate, so use the SCLK values of IMP
    windsock images and ASI/Met data to locate periods of
    simultaneity between these data.  Calculate the atmospheric
    density, rho, using the relevant ASI/Met temperature and pressure
    data.
 
    (5) Determine the strut azimuth into the wind.  This information
    will be used for locating relevant calibration data.  The strut
    azimuth into the wind is obtained by comparing the windsock
    azimuth clockwise from north found in step (3) with the azimuth
    of the windsock strut (36 deg east of north, as specified in step
    3).
 
    (6) Obtain relevant calibration data.  Access the appropriate
    calibration chart, WS1calib.tif, WS2calib.tif, or WS3calib.tif
    included in this PDS distribution for windsock 1, 2, or 3,
    respectively.  Each chart shows what calibration data are
    available at twelve strut azimuths, at both one atmosphere and at
    Martian equivalent pressure.  Locate the azimuth segment from (5)
    on the calibration chart, and to determine what calibration data
    are available and the film roll it is located on.  The actual
    calibration data, including deflection, temperature, and
    pressure, are listed by film roll number in Appendix I.
    Deflection values in Appendix I include measurements made during
    both ascending and descending wind speeds; averaging of these
    deflections at each wind speed, where possible, is recommended.
 
    (7) Calculate wind speed.  Calculate wind speed, u, from the
    results of (3-4) and appropriate calibration data from (5-6),
    using equations [1-2] to relate parameters between Martian and
    (terrestrial) calibration environments that share the same
    deflection angle theta.  More calibration data were obtained at
    one atmosphere than at low pressure, so it is recommended that
    the one-atmosphere data be used for interpreting Martian data
    using equations [1-2].  This is especially so considering that
    there are more one-atmosphere calibration data at the smallest
    deflections, which were typical during the quiescent wind
    conditions at the landing site during Pathfinder mission
    operations.
 
 
  Additional Sources of Information
  =================================
    Inquiries for additional information about the Pathfinder IMP
    windsock experiment, windsock data in this PDS distribution, or
    the content of this document (apart from questions regarding PDS
    distribution generally) should be directed to Dr.  Robert
    Sullivan, CRSR, Cornell University, Ithaca, NY 14853 (5/99).
 
 
  Appendix I - IMP Windsock Calibration Data
  ==========================================
    FR = Film Roll: The number of the roll of film on which the
    windsock image appears.  There were eight rolls of film.
 
    FW = Flight Windsock: Flight windsock unit 1, 2, or 3.
 
    SA = Strut Azimuth: Strut azimuth of 0 deg extends the windsock
    strut ahead of the mast, into the wind; 180 deg azimuth extends
    the windsock strut directly downwind of the mast, placing the
    windsock in the mast wake.  Strut azimuth increases clockwise
    when viewed from overhead.
 
    ED = Exposure Date: Date of exposure of windsock picture.
 
    EH = Exposure Hour: Hour of exposure of windsock picture.
 
    EM = Exposure Min: Minute of exposure of windsock picture.
 
    AP = AM/PM: Morning or afternoon specification of exposure of
    windsock picture.
 
    T = Temperature (K): Approximate temperature of the atmosphere in
    degrees Kelvin.
 
    P = Pressure (mb): Atmospheric pressure in millibars.  Pressures
    for one-atmosphere exposures are approximated as 1015 mb.
 
    FS = Fan Speed (Hz): For one-atmosphere exposures only, the speed
    setting of the wind tunnel fan.
 
    U = Wind Speed (m/s): Wind speed in meters/second recorded by the
    laser-Doppler velocimeter.
 
    DA = Deflection Angle (deg): Deflection angle of the windsock
    from vertical measured from the picture.  The letter 'B'
    associated with a measurement means that the windsock was partly
    blocked in the picture by the mast or other apparatus.
 
    DA2 = Deflection Angle (trial 2) (deg): A second trial
    measurement, from the original film, of deflection of the
    windsock from vertical.
 
    DA3 = Deflection Angle (trial 3) (deg): A third trial
    measurement, from the original film, of deflection of the
    windsock from vertical.
 
    DA4 = Deflection Angle (trial 4) (deg): A fourth trial
    measurement, from the original film, of deflection of the
    windsock from vertical.
 
    FR FW SA    ED    EH EM AP  T     P    FS   U     DA    DA2  DA3 DA4
    -- -- -- -------- -- -- -- --- ------ --- ----- ------ ---- ---- ---
     1 1  ND 09/07/95  6 13 AM 293 1015.0  ND    ND   -0.5
     1 1  ND 09/07/95  6 13 AM 293 1015.0  ND    ND    0.0
     1 1  60 09/08/95  7 33 AM 293 1015.0  45  8.38   85.5 86.0
     1 1  60 09/08/95  7 34 AM 293 1015.0  32  6.09   81.0 80.0
     1 1  60 09/08/95  7 35 AM 293 1015.0  28  5.35   78.0 77.0
     1 1  60 09/08/95  7 36 AM 293 1015.0  24  4.61   72.0 72.0
     1 1  60 09/08/95  7 37 AM 293 1015.0  22  4.23   70.0 70.0
     1 1  60 09/08/95  7 38 AM 293 1015.0  20  3.85   65.5 66.0
     1 1  60 09/08/95  7 39 AM 293 1015.0  18  3.47   59.1 60.0
     1 1  60 09/08/95  7 40 AM 293 1015.0  16  3.08   51.6 52.0
     1 1  60 09/08/95  7 41 AM 293 1015.0  15  2.88   46.2 47.0
     1 1  60 09/08/95  7 42 AM 293 1015.0  14  2.69   43.5 44.0
     1 1  60 09/08/95  7 43 AM 293 1015.0  13  2.49   35.0 35.0
     1 1  60 09/08/95  7 44 AM 293 1015.0  12  2.29   28.5 28.0
     1 1  60 09/08/95  7 45 AM 293 1015.0  11  2.10   20.5 21.0
     1 1  60 09/08/95  7 46 AM 293 1015.0  10  1.90   18.1 19.0
     1 1  60 09/08/95  7 47 AM 293 1015.0   9  1.70   15.6 16.0
     1 1  60 09/08/95  7 48 AM 293 1015.0   8  1.50   13.5 14.0
     1 1  60 09/08/95  7 49 AM 293 1015.0   7  1.29   11.5 12.0
     1 1  60 09/08/95  7 50 AM 293 1015.0   6  1.09    9.0 10.0
     1 1  60 09/08/95  7 51 AM 293 1015.0   0  0.00    4.5  5.0
     1 1  60 09/08/95  7 55 AM 293 1015.0   6  1.09    6.5  7.0
     1 1  60 09/08/95  7 56 AM 293 1015.0   7  1.29    6.5  8.0
     1 1  60 09/08/95  7 57 AM 293 1015.0   8  1.50    9.0 10.0
     1 1  60 09/08/95  7 58 AM 293 1015.0   9  1.70   12.5 13.0
     1 1  60 09/08/95  7 59 AM 293 1015.0  10  1.90   15.0 16.0
     1 1  60 09/08/95  8  0 AM 293 1015.0  11  2.10   19.0 20.0
     1 1  60 09/08/95  8  1 AM 293 1015.0  12  2.29   26.1 26.0
     1 1  60 09/08/95  8  2 AM 293 1015.0  13  2.49   32.3 32.0
     1 1  60 09/08/95  8  3 AM 293 1015.0  14  2.69   42.5 42.0
     1 1  60 09/08/95  8  4 AM 293 1015.0  15  2.88   47.2 47.0
     1 1  60 09/08/95  8  5 AM 293 1015.0  16  3.08   53.0 53.0
     1 1  60 09/08/95  8  6 AM 293 1015.0  18  3.47   61.0 61.0
     1 1  60 09/08/95  8  7 AM 293 1015.0  20  3.85   65.0 65.0
     1 1  60 09/08/95  8  8 AM 293 1015.0  22  4.23   69.0 69.0
     1 1  60 09/08/95  8  9 AM 293 1015.0  24  4.61   72.5 73.0
     1 1  60 09/08/95  8 10 AM 293 1015.0  28  5.35   78.0 78.0
     1 1  60 09/08/95  8 11 AM 293 1015.0  32  6.09   80.0 80.0
     1 1  60 09/08/95  8 12 AM 293 1015.0  45  8.38   85.5 86.0
     1 1 180 09/08/95  8 13 AM 293 1015.0  45  8.38   68.0
     1 1 180 09/08/95  8 14 AM 293 1015.0  32  6.09   68.0
     1 1 180 09/08/95  8 15 AM 293 1015.0  28  5.35   68.5
     1 1 180 09/08/95  8 16 AM 293 1015.0  24  4.61   65.5
     1 1 180 09/08/95  8 17 AM 293 1015.0  22  4.23   60.5
     1 1 180 09/08/95  8 18 AM 293 1015.0  20  3.85   55.0
     1 1 180 09/08/95  8 19 AM 293 1015.0  18  3.47   48.0
     1 1 180 09/08/95  8 20 AM 293 1015.0  16  3.08   40.0
     1 1 180 09/08/95  8 21 AM 293 1015.0  15  2.88   34.6
     1 1 180 09/08/95  8 22 AM 293 1015.0  14  2.69   30.0
     1 1 180 09/08/95  8 23 AM 293 1015.0  13  2.49   20.0
     1 1 180 09/08/95  8 24 AM 293 1015.0  12  2.29   16.6
     1 1 180 09/08/95  8 25 AM 293 1015.0  11  2.10   13.4
     1 1 180 09/08/95  8 26 AM 293 1015.0  10  1.90   11.5
     1 1 180 09/08/95  8 27 AM 293 1015.0   9  1.70   10.0
     1 1 180 09/08/95  8 28 AM 293 1015.0   8  1.50    8.0
     1 1 180 09/08/95  8 29 AM 293 1015.0   7  1.29    6.0
     1 1 180 09/08/95  8 30 AM 293 1015.0   6  1.09    4.3
     1 1 180 09/08/95  8 31 AM 293 1015.0   0  0.00    1.5
     1 1 180 09/08/95  8 33 AM 293 1015.0   6  1.09    3.5
     1 1 180 09/08/95  8 34 AM 293 1015.0   7  1.29    5.0
     1 1 180 09/08/95  8 35 AM 293 1015.0   8  1.50    6.5
     1 1 180 09/08/95  8 36 AM 293 1015.0   9  1.70    8.0
     1 1 180 09/08/95  8 37 AM 293 1015.0  10  1.90   10.6
     1 1 180 09/08/95  8 38 AM 293 1015.0  11  2.10   13.0
     1 1 180 09/08/95  8 39 AM 293 1015.0  12  2.29   15.3
     1 1 180 09/08/95  8 40 AM 293 1015.0  13  2.49   19.0
     1 1 180 09/08/95  8 41 AM 293 1015.0  14  2.69   29.2
     1 1 180 09/08/95  8 42 AM 293 1015.0  15  2.88   34.5
     1 1 180 09/08/95  8 43 AM 293 1015.0  16  3.08   40.5
     1 1 180 09/08/95  8 44 AM 293 1015.0  18  3.47   48.5
     1 1 180 09/08/95  8 45 AM 293 1015.0  20  3.85   56.5
     1 1 180 09/08/95  8 46 AM 293 1015.0  22  4.23   62.0
     1 1 180 09/08/95  8 47 AM 293 1015.0  24  4.61   65.0
     1 1 180 09/08/95  8 48 AM 293 1015.0  28  5.35   68.5
     1 1 180 09/08/95  8 49 AM 293 1015.0  32  6.09   68.5
     1 1 180 09/08/95  8 50 AM 293 1015.0  45  8.38   69.0
     1 1 240 09/08/95  8 54 AM 293 1015.0  45  8.38   84.5
     1 1 240 09/08/95  8 55 AM 293 1015.0  32  6.09   80.0
     1 1 240 09/08/95  8 56 AM 293 1015.0  28  5.35   76.0
     1 1 240 09/08/95  8 57 AM 293 1015.0  24  4.61   71.5
     1 1 240 09/08/95  8 58 AM 293 1015.0  22  4.23   67.5
     1 1 240 09/08/95  8 59 AM 293 1015.0  20  3.85   62.5
     1 1 240 09/08/95  9  0 AM 293 1015.0  18  3.47   55.0
     1 1 240 09/08/95  9  1 AM 293 1015.0  16  3.08   47.3
     1 1 240 09/08/95  9  2 AM 293 1015.0  15  2.88   42.5
     1 1 240 09/08/95  9  3 AM 293 1015.0  14  2.69   37.0
     1 1 240 09/08/95  9  4 AM 293 1015.0  13  2.49   29.5
     1 1 240 09/08/95  9  5 AM 293 1015.0  12  2.29   24.0
     1 1 240 09/08/95  9  6 AM 293 1015.0  11  2.10   19.0
     1 1 240 09/08/95  9  7 AM 293 1015.0  10  1.90   15.5
     1 1 240 09/08/95  9  8 AM 293 1015.0   9  1.70   13.0
     1 1 240 09/08/95  9  9 AM 293 1015.0   8  1.50   10.5
     1 1 240 09/08/95  9 10 AM 293 1015.0   7  1.29    8.5
     1 1 240 09/08/95  9 11 AM 293 1015.0   6  1.09    5.5
     1 1 240 09/08/95  9 12 AM 293 1015.0   0  0.00    2.5
     1 1 240 09/08/95  9 14 AM 293 1015.0   0  0.00    1.5
     1 1 240 09/08/95  9 17 AM 293 1015.0   6  1.09    4.3
     1 1 240 09/08/95  9 18 AM 293 1015.0   7  1.29    5.5
     1 1 240 09/08/95  9 19 AM 293 1015.0   8  1.50    8.0
     1 1 240 09/08/95  9 20 AM 293 1015.0   9  1.70   12.0
     1 1 240 09/08/95  9 21 AM 293 1015.0  10  1.90   14.0
     1 1 240 09/08/95  9 22 AM 293 1015.0  11  2.10   17.5
     1 1 240 09/08/95  9 23 AM 293 1015.0  12  2.29   23.1
     1 1 240 09/08/95  9 24 AM 293 1015.0  13  2.49   27.5
     1 1 240 09/08/95  9 25 AM 293 1015.0  14  2.69   35.0
     1 1 240 09/08/95  9 26 AM 293 1015.0  15  2.88   42.4
     1 1 240 09/08/95  9 27 AM 293 1015.0  16  3.08   47.5
     1 1 240 09/08/95  9 28 AM 293 1015.0  18  3.47   56.0
     1 1 240 09/08/95  9 29 AM 293 1015.0  20  3.85   61.6
     1 1 240 09/08/95  9 30 AM 293 1015.0  22  4.23   66.9
     1 1 240 09/08/95  9 31 AM 293 1015.0  24  4.61   71.0
     1 1 240 09/08/95  9 32 AM 293 1015.0  28  5.35   76.0
     1 1 240 09/08/95  9 33 AM 293 1015.0  32  6.09   79.5
     1 1 240 09/08/95  9 34 AM 293 1015.0  45  8.38   83.5
     1 1 270 09/08/95  9 36 AM 293 1015.0  45  8.38   84.0
     1 1 270 09/08/95  9 37 AM 293 1015.0  32  6.09   80.0
     1 1 270 09/08/95  9 38 AM 293 1015.0  28  5.35   75.2
     1 1 270 09/08/95  9 39 AM 293 1015.0  24  4.61   71.0
     1 1 270 09/08/95  9 40 AM 293 1015.0  22  4.23   65.6
     1 1 270 09/08/95  9 41 AM 293 1015.0  20  3.85   63.0
     1 1 270 09/08/95  9 42 AM 293 1015.0  18  3.47   57.5
     1 1 270 09/08/95  9 43 AM 293 1015.0  16  3.08   51.0
     1 1 270 09/08/95  9 44 AM 293 1015.0  15  2.88   47.0
     1 1 270 09/08/95  9 45 AM 293 1015.0  14  2.69   38.4
     1 1 270 09/08/95  9 46 AM 293 1015.0  13  2.49   32.0
     1 1 270 09/08/95  9 47 AM 293 1015.0  12  2.29   25.0
     1 1 270 09/08/95  9 48 AM 293 1015.0  11  2.10   19.5
     1 1 270 09/08/95  9 49 AM 293 1015.0  10  1.90   16.0
     1 1 270 09/08/95  9 50 AM 293 1015.0   9  1.70   13.4
     1 1 270 09/08/95  9 51 AM 293 1015.0   8  1.50   11.0
     1 1 270 09/08/95  9 52 AM 293 1015.0   7  1.29    8.0
     1 1 270 09/08/95  9 53 AM 293 1015.0   6  1.09    6.2
     1 1 270 09/08/95  9 54 AM 293 1015.0   0  0.00    2.2
     1 1 270 09/08/95  9 58 AM 293 1015.0   6  1.09    4.2
     1 1 270 09/08/95  9 59 AM 293 1015.0   7  1.29    5.5
     1 1 270 09/08/95 10  0 AM 293 1015.0   8  1.50   10.4
     1 1 270 09/08/95 10  1 AM 293 1015.0   9  1.70   12.6
     1 1 270 09/08/95 10  2 AM 293 1015.0  10  1.90   15.0
     1 1 270 09/08/95 10  3 AM 293 1015.0  11  2.10   19.0
     1 1 270 09/08/95 10  4 AM 293 1015.0  12  2.29   21.5
     1 1 270 09/08/95 10  5 AM 293 1015.0  13  2.49   30.4
     1 1 270 09/08/95 10  6 AM 293 1015.0  14  2.69   39.5
     1 1 270 09/08/95 10  7 AM 293 1015.0  15  2.88   45.4
     1 1 270 09/08/95 10  8 AM 293 1015.0  16  3.08   50.7
     1 1 270 09/08/95 10  9 AM 293 1015.0  18  3.47   55.8
     1 1 270 09/08/95 10 10 AM 293 1015.0  20  3.85   63.3
     1 1 270 09/08/95 10 11 AM 293 1015.0  22  4.23   68.5
     1 1 270 09/08/95 10 12 AM 293 1015.0  24  4.61   72.0
     1 1 270 09/08/95 10 13 AM 293 1015.0  28  5.35   75.7
     1 1 270 09/08/95 10 14 AM 293 1015.0  32  6.09   78.8
     1 1 270 09/08/95 10 15 AM 293 1015.0  45  8.38   85.0
     1 1   0 09/08/95 10 18 AM 293 1015.0  45  8.38   70.5
     1 1   0 09/08/95 10 19 AM 293 1015.0  32  6.09   70.5
     1 1   0 09/08/95 10 20 AM 293 1015.0  28  5.35   71.0
     1 1   0 09/08/95 10 21 AM 293 1015.0  24  4.61   70.5
     1 1   0 09/08/95 10 22 AM 293 1015.0  22  4.23   67.5
     1 1   0 09/08/95 10 23 AM 293 1015.0  20  3.85   63.5
     1 1   0 09/08/95 10 24 AM 293 1015.0  18  3.47   57.3
     1 1   0 09/08/95 10 25 AM 293 1015.0  16  3.08   50.0
     1 1   0 09/08/95 10 26 AM 293 1015.0  15  2.88   46.0
     1 1   0 09/08/95 10 27 AM 293 1015.0  14  2.69   39.5
     1 1   0 09/08/95 10 28 AM 293 1015.0  13  2.49   34.5
     1 1   0 09/08/95 10 29 AM 293 1015.0  12  2.29   25.0
     1 1   0 09/08/95 10 30 AM 293 1015.0  11  2.10   20.5
     1 1   0 09/08/95 10 31 AM 293 1015.0  10  1.90   16.5
     1 1   0 09/08/95 10 32 AM 293 1015.0   9  1.70   10.0
     1 1   0 09/08/95 10 33 AM 293 1015.0   8  1.50   10.7
     1 1   0 09/08/95 10 34 AM 293 1015.0   7  1.29    9.7
     1 1   0 09/08/95 10 35 AM 293 1015.0   6  1.09    6.2
     1 1   0 09/08/95 10 36 AM 293 1015.0   0  0.00    3.5
     1 1   0 09/08/95 10 41 AM 293 1015.0   6  1.09    5.5
     1 1   0 09/08/95 10 42 AM 293 1015.0   7  1.29    7.5
     1 1   0 09/08/95 10 43 AM 293 1015.0   8  1.50   10.0
     1 1   0 09/08/95 10 44 AM 293 1015.0   9  1.70   12.6
     1 1   0 09/08/95 10 45 AM 293 1015.0  10  1.90   16.2
     1 1   0 09/08/95 10 46 AM 293 1015.0  11  2.10   18.2
     1 1   0 09/08/95 10 47 AM 293 1015.0  12  2.29   25.0
     1 1   0 09/08/95 10 48 AM 293 1015.0  13  2.49   36.5
     1 1   0 09/08/95 10 49 AM 293 1015.0  14  2.69   41.4
     1 1   0 09/08/95 10 50 AM 293 1015.0  15  2.88   45.4
     1 1   0 09/08/95 10 51 AM 293 1015.0  16  3.08   50.5
     1 1   0 09/08/95 10 52 AM 293 1015.0  18  3.47   58.2
     1 1   0 09/08/95 10 53 AM 293 1015.0  20  3.85   63.0
     1 1   0 09/08/95 10 54 AM 293 1015.0  22  4.23   67.4
     1 1   0 09/08/95 10 55 AM 293 1015.0  24  4.61   70.5
     1 1   0 09/08/95 10 56 AM 293 1015.0  28  5.35   71.0
     1 1   0 09/08/95 10 57 AM 293 1015.0  32  6.09   70.4
     1 1   0 09/08/95 10 58 AM 293 1015.0  45  8.38   71.0
     1 1 210 09/08/95 11  6 AM 293 1015.0  45  8.38   84.5
     1 1 210 09/08/95 11  7 AM 293 1015.0  32  6.09   80.0
     1 1 210 09/08/95 11  8 AM 293 1015.0  28  5.35   76.0
     1 1 210 09/08/95 11  9 AM 293 1015.0  24  4.61   70.0
     1 1 210 09/08/95 11 10 AM 293 1015.0  22  4.23   66.0
     1 1 210 09/08/95 11 11 AM 293 1015.0  20  3.85   60.5
     1 1 210 09/08/95 11 12 AM 293 1015.0  18  3.47   56.0
     1 1 210 09/08/95 11 13 AM 293 1015.0  16  3.08   47.5
     1 1 210 09/08/95 11 14 AM 293 1015.0  15  2.88   44.0
     1 1 210 09/08/95 11 15 AM 293 1015.0  14  2.69   39.5
     1 1 210 09/08/95 11 16 AM 293 1015.0  13  2.49   33.0
     1 1 210 09/08/95 11 17 AM 293 1015.0  12  2.29   25.5
     1 1 210 09/08/95 11 18 AM 293 1015.0  11  2.10   19.0
     1 1 210 09/08/95 11 19 AM 293 1015.0  10  1.90   14.0
     1 1 210 09/08/95 11 20 AM 293 1015.0   9  1.70   12.0
     1 1 210 09/08/95 11 21 AM 293 1015.0   8  1.50   10.0
     1 1 210 09/08/95 11 22 AM 293 1015.0   7  1.29    7.5
     1 1 210 09/08/95 11 23 AM 293 1015.0   6  1.09    6.4
     1 1 210 09/08/95 11 25 AM 293 1015.0   0  0.00    1.0
     2 1  ND 09/08/95  1 44 PM 293 1015.0  ND    ND    2.5
     2 1 210 09/08/95  1 55 PM 293 1015.0   6  1.09    4.0
     2 1 210 09/08/95  1 56 PM 293 1015.0   7  1.29    5.5
     2 1 210 09/08/95  1 57 PM 293 1015.0   8  1.50    8.5
     2 1 210 09/08/95  1 58 PM 293 1015.0   9  1.70   11.0
     2 1 210 09/08/95  1 59 PM 293 1015.0  10  1.90   13.5
     2 1 210 09/08/95  2  0 PM 293 1015.0  11  2.10   16.5
     2 1 210 09/08/95  2  1 PM 293 1015.0  12  2.29   24.0
     2 1 210 09/08/95  2  2 PM 293 1015.0  13  2.49   28.0
     2 1 210 09/08/95  2  3 PM 293 1015.0  14  2.69   35.0
     2 1 210 09/08/95  2  4 PM 293 1015.0  15  2.88   41.0
     2 1 210 09/08/95  2  5 PM 293 1015.0  16  3.08   48.0
     2 1 210 09/08/95  2  6 PM 293 1015.0  18  3.47   57.0
     2 1 210 09/08/95  2  7 PM 293 1015.0  20  3.85   61.0
     2 1 210 09/08/95  2  8 PM 293 1015.0  22  4.23   66.0
     2 1 210 09/08/95  2  9 PM 293 1015.0  24  4.61   71.0
     2 1 210 09/08/95  2 10 PM 293 1015.0  28  5.35   75.0
     2 1 210 09/08/95  2 11 PM 293 1015.0  32  6.09   79.0
     2 1 210 09/08/95  2 12 PM 293 1015.0  45  8.38   83.5
     2 1 300 09/08/95  2 17 PM 293 1015.0   0  0.00    4.0
     2 1 330 09/08/95  2 21 PM 293 1015.0   0  0.00    4.0
     2 1  30 09/08/95  2 26 PM 293 1015.0   0  0.00    7.0
     2 1  90 09/08/95  2 30 PM 293 1015.0   0  0.00 B117.5
     2 1 120 09/08/95  2 33 PM 293 1015.0   0  0.00    5.0
     2 1 150 09/08/95  2 38 PM 293 1015.0   0  0.00    5.5
     2 2  60 09/08/95  3  3 PM 293 1015.0  45  8.38   84.0 84.0
     2 2  60 09/08/95  3  4 PM 293 1015.0  32  6.09   80.0 80.0
     2 2  60 09/08/95  3  5 PM 293 1015.0  28  5.35   76.5 76.0
     2 2  60 09/08/95  3  6 PM 293 1015.0  24  4.61   70.0 71.0
     2 2  60 09/08/95  3  7 PM 293 1015.0  22  4.23   68.5 68.0
     2 2  60 09/08/95  3  8 PM 293 1015.0  20  3.85   62.5 63.0
     2 2  60 09/08/95  3  9 PM 293 1015.0  18  3.47   56.5 57.0
     2 2  60 09/08/95  3 10 PM 293 1015.0  16  3.08   51.0 50.0
     2 2  60 09/08/95  3 11 PM 293 1015.0  15  2.88   45.5 45.0
     2 2  60 09/08/95  3 12 PM 293 1015.0  14  2.69   40.5 39.0
     2 2  60 09/08/95  3 13 PM 293 1015.0  13  2.49   30.0 30.0
     2 2  60 09/08/95  3 14 PM 293 1015.0  12  2.29   19.0 25.0
     2 2  60 09/08/95  3 15 PM 293 1015.0  11  2.10   19.5 20.0
     2 2  60 09/08/95  3 16 PM 293 1015.0  10  1.90   16.0 17.0
     2 2  60 09/08/95  3 17 PM 293 1015.0   9  1.70   14.0 14.0
     2 2  60 09/08/95  3 18 PM 293 1015.0   8  1.50   12.0 12.0
     2 2  60 09/08/95  3 20 PM 293 1015.0   6  1.09    7.0  8.0
     2 2  60 09/08/95  3 21 PM 293 1015.0   0  0.00    4.0  3.0
     2 2  60 09/08/95  3 31 PM 293 1015.0   6  1.09    4.5  5.0
     2 2  60 09/08/95  3 32 PM 293 1015.0   7  1.29    6.0  7.0
     2 2  60 09/08/95  3 33 PM 293 1015.0   8  1.50    9.0  9.0
     2 2  60 09/08/95  3 34 PM 293 1015.0   9  1.70   11.5 12.0
     2 2  60 09/08/95  3 35 PM 293 1015.0  10  1.90   14.0 14.0
     2 2  60 09/08/95  3 36 PM 293 1015.0  11  2.10   18.5 18.0
     2 2  60 09/08/95  3 37 PM 293 1015.0  12  2.29   22.5
     2 2  60 09/08/95  3 38 PM 293 1015.0  13  2.49   28.0
     2 2  60 09/08/95  3 39 PM 293 1015.0  14  2.69   40.0
     2 2  60 09/08/95  3 40 PM 293 1015.0  15  2.88   44.0
     2 2  60 09/08/95  3 41 PM 293 1015.0  16  3.08   48.5
     2 2  60 09/08/95  3 42 PM 293 1015.0  18  3.47   54.0
     2 2  60 09/08/95  3 43 PM 293 1015.0  20  3.85   63.5
     2 2  60 09/08/95  3 44 PM 293 1015.0  22  4.23   68.5
     2 2  60 09/08/95  3 45 PM 293 1015.0  24  4.61   72.0
     2 2  60 09/08/95  3 46 PM 293 1015.0  28  5.35   78.0
     2 2  60 09/08/95  3 47 PM 293 1015.0  32  6.09   80.0
     2 2  60 09/08/95  3 48 PM 293 1015.0  45  8.38   85.0
     2 2 180 09/08/95  3 57 PM 293 1015.0  45  8.38   69.0
     2 2 180 09/08/95  3 58 PM 293 1015.0  32  6.09   69.0
     2 2 180 09/08/95  3 59 PM 293 1015.0  28  5.35   68.0
     2 2 180 09/08/95  4  0 PM 293 1015.0  24  4.61   63.0
     2 2 180 09/08/95  4  1 PM 293 1015.0  22  4.23   58.5
     2 2 180 09/08/95  4  2 PM 293 1015.0  20  3.85   53.5
     2 2 180 09/08/95  4  3 PM 293 1015.0  18  3.47   46.5
     2 2 180 09/08/95  4  4 PM 293 1015.0  16  3.08   38.0
     2 2 180 09/08/95  4  5 PM 293 1015.0  15  2.88   34.5
     2 2 180 09/08/95  4  6 PM 293 1015.0  14  2.69   25.5
     2 2 180 09/08/95  4  7 PM 293 1015.0  13  2.49   18.5
     2 2 180 09/08/95  4  8 PM 293 1015.0  12  2.29   14.5
     2 2 180 09/08/95  4  9 PM 293 1015.0  11  2.10   14.0
     2 2 180 09/08/95  4 11 PM 293 1015.0  10  1.90    8.0
     2 2 180 09/08/95  4 12 PM 293 1015.0   9  1.70    9.0
     2 2 180 09/08/95  4 13 PM 293 1015.0   8  1.50    7.0
     2 2 180 09/08/95  4 14 PM 293 1015.0   7  1.29    4.5
     2 2 180 09/08/95  4 15 PM 293 1015.0   6  1.09    3.0
     2 2 180 09/08/95  4 16 PM 293 1015.0   0  0.00    1.0
     2 2 180 09/08/95  4 24 PM 293 1015.0   6  1.09    2.0
     2 2 180 09/08/95  4 25 PM 293 1015.0   7  1.29    4.0
     2 2 180 09/08/95  4 26 PM 293 1015.0   8  1.50    6.0
     2 2 180 09/08/95  4 27 PM 293 1015.0   9  1.70    8.0
     2 2 180 09/08/95  4 28 PM 293 1015.0  10  1.90   11.0
     2 2 180 09/08/95  4 29 PM 293 1015.0  11  2.10   11.5
     2 2 180 09/08/95  4 30 PM 293 1015.0  12  2.29   17.5
     2 2 180 09/08/95  4 31 PM 293 1015.0  13  2.49   17.5
     2 2 180 09/08/95  4 32 PM 293 1015.0  14  2.69   27.5
     2 2 180 09/08/95  4 33 PM 293 1015.0  15  2.88   34.5
     2 2 180 09/08/95  4 34 PM 293 1015.0  16  3.08   34.0
     2 2 180 09/08/95  4 35 PM 293 1015.0  18  3.47   44.0
     2 2 180 09/08/95  4 36 PM 293 1015.0  20  3.85   53.0
     2 2 180 09/08/95  4 37 PM 293 1015.0  22  4.23   59.0
     2 2 180 09/08/95  4 38 PM 293 1015.0  24  4.61   64.0
     2 2 180 09/08/95  4 39 PM 293 1015.0  28  5.35   69.0
     2 2 180 09/08/95  4 40 PM 293 1015.0  32  6.09   70.0
     2 2 180 09/08/95  4 41 PM 293 1015.0  45  8.38   69.0
     2 2 210 09/08/95  4 45 PM 293 1015.0  45  8.38   86.5
     2 2 210 09/08/95  4 46 PM 293 1015.0  32  6.09   80.0
     2 2 210 09/08/95  4 47 PM 293 1015.0  28  5.35   77.0
     2 2 210 09/08/95  4 48 PM 293 1015.0  24  4.61   71.0
     2 2 210 09/08/95  4 49 PM 293 1015.0  22  4.23   67.0
     2 2 210 09/08/95  4 50 PM 293 1015.0  20  3.85   62.0
     2 2 210 09/08/95  4 51 PM 293 1015.0  18  3.47   55.5
     2 2 210 09/08/95  4 52 PM 293 1015.0  16  3.08   48.0
     2 2 210 09/08/95  4 53 PM 293 1015.0  15  2.88   43.0
     2 2 210 09/08/95  4 54 PM 293 1015.0  14  2.69   38.0
     2 2 210 09/08/95  4 55 PM 293 1015.0  13  2.49   29.0
     2 2 210 09/08/95  4 56 PM 293 1015.0  12  2.29   24.5
     2 2 210 09/08/95  4 57 PM 293 1015.0  11  2.10   18.0
     2 2 210 09/08/95  4 58 PM 293 1015.0  10  1.90   14.5
     2 2 210 09/08/95  4 59 PM 293 1015.0   9  1.70   11.0
     2 2 210 09/08/95  5  0 PM 293 1015.0   8  1.50    9.0
     2 2 210 09/08/95  5  1 PM 293 1015.0   7  1.29    7.5
     2 2 210 09/08/95  5  2 PM 293 1015.0   6  1.09    6.0
     2 2 210 09/08/95  5  3 PM 293 1015.0   0  0.00    0.5
     2 2 210 09/08/95  5  7 PM 293 1015.0   6  1.09    2.5
     2 2 210 09/08/95  5  8 PM 293 1015.0   7  1.29    5.0
     2 2 210 09/08/95  5  9 PM 293 1015.0   8  1.50    7.0
     2 2 210 09/08/95  5 10 PM 293 1015.0   9  1.70   10.5
     2 2 210 09/08/95  5 11 PM 293 1015.0  10  1.90   12.0
     2 2 210 09/08/95  5 12 PM 293 1015.0  11  2.10   16.0
     2 2 210 09/08/95  5 13 PM 293 1015.0  12  2.29   23.0
     2 2 210 09/08/95  5 14 PM 293 1015.0  13  2.49   28.0
     2 2 210 09/08/95  5 15 PM 293 1015.0  14  2.69   34.0
     2 2 210 09/08/95  5 16 PM 293 1015.0  15  2.88   41.5
     2 2 210 09/08/95  5 17 PM 293 1015.0  16  3.08   47.0
     2 2 210 09/08/95  5 18 PM 293 1015.0  18  3.47   53.0
     2 2 210 09/08/95  5 19 PM 293 1015.0  20  3.85   61.0
     2 2 210 09/08/95  5 20 PM 293 1015.0  22  4.23   67.0
     2 2 210 09/08/95  5 21 PM 293 1015.0  24  4.61   70.5
     2 2 210 09/08/95  5 22 PM 293 1015.0  28  5.35   78.0
     2 2 210 09/08/95  5 23 PM 293 1015.0  32  6.09   80.0
     2 2 210 09/08/95  5 24 PM 293 1015.0  45  8.38   85.5
     2 2  ND 09/08/95  8 42 PM 293 1015.0  ND    ND    2.0
     2 2  ND 09/08/95  8 42 PM 293 1015.0  ND    ND    2.0
     2 2  ND 09/08/95  8 42 PM 293 1015.0  ND    ND    2.0
     2 2  ND 09/08/95  8 42 PM 293 1015.0  ND    ND    2.0
     2 2  ND 09/08/95  8 42 PM 293 1015.0  ND    ND    2.0
     2 2 240 09/08/95  8 47 PM 293 1015.0  45  8.38   85.5
     2 2 240 09/08/95  8 48 PM 293 1015.0  32  6.09   81.0
     2 2 240 09/08/95  8 49 PM 293 1015.0  28  5.35   77.0
     2 2 240 09/08/95  8 50 PM 293 1015.0  24  4.61   70.0
     2 2 240 09/08/95  8 51 PM 293 1015.0  22  4.23   66.5
     2 2 240 09/08/95  8 52 PM 293 1015.0  20  3.85   62.0
     2 2 240 09/08/95  8 53 PM 293 1015.0  18  3.47   55.0
     2 2 240 09/08/95  8 54 PM 293 1015.0  16  3.08   47.5
     2 2 240 09/08/95  8 55 PM 293 1015.0  15  2.88   44.0
     2 2 240 09/08/95  8 56 PM 293 1015.0  14  2.69   40.0
     2 2 240 09/08/95  8 57 PM 293 1015.0  13  2.49   30.0
     2 2 240 09/08/95  8 58 PM 293 1015.0  12  2.29   25.0
     2 2 240 09/08/95  8 59 PM 293 1015.0  11  2.10   19.0
     2 2 240 09/08/95  9  0 PM 293 1015.0  10  1.90   16.0
     2 2 240 09/08/95  9  1 PM 293 1015.0   9  1.70   13.0
     2 2 240 09/08/95  9  2 PM 293 1015.0   8  1.50   10.5
     2 2 240 09/08/95  9  3 PM 293 1015.0   7  1.29    8.5
     2 2 240 09/08/95  9  4 PM 293 1015.0   6  1.09    7.0
     2 2 240 09/08/95  9  5 PM 293 1015.0   0  0.00    2.0
     2 2 240 09/08/95  9 17 PM 293 1015.0   6  1.09    4.0
     2 2 240 09/08/95  9 18 PM 293 1015.0   7  1.29    7.0
     2 2 240 09/08/95  9 19 PM 293 1015.0   8  1.50    8.5
     2 2 240 09/08/95  9 20 PM 293 1015.0   9  1.70   11.5
     2 2 240 09/08/95  9 21 PM 293 1015.0  10  1.90   15.0
     2 2 240 09/08/95  9 22 PM 293 1015.0  11  2.10   18.0
     2 2 240 09/08/95  9 23 PM 293 1015.0  12  2.29   24.0
     2 2 240 09/08/95  9 24 PM 293 1015.0  13  2.49   28.0
     2 2 240 09/08/95  9 25 PM 293 1015.0  14  2.69   35.0
     2 2 240 09/08/95  9 26 PM 293 1015.0  15  2.88   43.0
     2 2 240 09/08/95  9 27 PM 293 1015.0  16  3.08   47.5
     2 2 240 09/08/95  9 28 PM 293 1015.0  18  3.47   54.5
     2 2 240 09/08/95  9 29 PM 293 1015.0  20  3.85   61.5
     2 2 240 09/08/95  9 30 PM 293 1015.0  22  4.23   66.0
     2 2 240 09/08/95  9 31 PM 293 1015.0  24  4.61   70.5
     2 2 240 09/08/95  9 32 PM 293 1015.0  28  5.35   76.0
     2 2 240 09/08/95  9 33 PM 293 1015.0  32  6.09   80.0
     2 2 240 09/08/95  9 34 PM 293 1015.0  45  8.38   85.5
     2 2 270 09/08/95  9 36 PM 293 1015.0  45  8.38   84.0
     2 2 270 09/08/95  9 37 PM 293 1015.0  32  6.09   80.0
     2 2 270 09/08/95  9 38 PM 293 1015.0  28  5.35   76.5
     2 2 270 09/08/95  9 39 PM 293 1015.0  24  4.61   72.0
     2 2 270 09/08/95  9 40 PM 293 1015.0  22  4.23   67.0
     2 2 270 09/08/95  9 41 PM 293 1015.0  20  3.85   63.0
     2 2 270 09/08/95  9 42 PM 293 1015.0  18  3.47   57.0
     2 2 270 09/08/95  9 43 PM 293 1015.0  16  3.08   48.5
     2 2 270 09/08/95  9 44 PM 293 1015.0  15  2.88   46.0
     2 2 270 09/08/95  9 45 PM 293 1015.0  14  2.69   39.5
     2 2 270 09/08/95  9 46 PM 293 1015.0  13  2.49   33.0
     2 2 270 09/08/95  9 47 PM 293 1015.0  12  2.29   27.0
     2 2 270 09/08/95  9 48 PM 293 1015.0  11  2.10   21.0
     2 2 270 09/08/95  9 49 PM 293 1015.0  10  1.90   18.0
     2 2 270 09/08/95  9 50 PM 293 1015.0   9  1.70   14.0
     2 2 270 09/08/95  9 51 PM 293 1015.0   8  1.50   11.0
     2 2 270 09/08/95  9 52 PM 293 1015.0   7  1.29    8.0
     2 2 270 09/08/95  9 53 PM 293 1015.0   6  1.09    7.0
     2 2 270 09/08/95  9 54 PM 293 1015.0   0  0.00    2.0
     2 2 270 09/08/95 10  3 PM 293 1015.0   6  1.09    6.5
     2 2 270 09/08/95 10  5 PM 293 1015.0   7  1.29    7.5
     2 2 270 09/08/95 10  6 PM 293 1015.0   8  1.50   10.0
     2 2 270 09/08/95 10  7 PM 293 1015.0   9  1.70   14.0
     2 2 270 09/08/95 10  8 PM 293 1015.0  10  1.90   16.5
     2 2 270 09/08/95 10  9 PM 293 1015.0  11  2.10   20.5
     2 2 270 09/08/95 10 10 PM 293 1015.0  12  2.29   27.5
     2 2 270 09/08/95 10 11 PM 293 1015.0  13  2.49   33.0
     2 2 270 09/08/95 10 12 PM 293 1015.0  14  2.69   41.0
     2 2 270 09/08/95 10 13 PM 293 1015.0  15  2.88   46.0
     2 2 270 09/08/95 10 14 PM 293 1015.0  16  3.08   50.0
     2 2 270 09/08/95 10 15 PM 293 1015.0  18  3.47   58.0
     2 2 270 09/08/95 10 16 PM 293 1015.0  20  3.85   64.0
     2 2 270 09/08/95 10 17 PM 293 1015.0  22  4.23   67.5
     2 2 270 09/08/95 10 18 PM 293 1015.0  24  4.61   72.0
     2 2 270 09/08/95 10 19 PM 293 1015.0  24  4.61   71.0
     2 2 270 09/08/95 10 20 PM 293 1015.0  28  5.35   76.5
     2 2 270 09/08/95 10 21 PM 293 1015.0  32  6.09   79.5
     2 2 270 09/08/95 10 22 PM 293 1015.0  45  8.38   84.5
     3 2  ND 09/09/95  7 55 AM 293 1015.0  ND    ND    2.0
     3 2   0 09/09/95  8 17 AM 293 1015.0  45  8.38   70.0 71.0
     3 2   0 09/09/95  8 18 AM 293 1015.0  32  6.09   70.6 71.0
     3 2   0 09/09/95  8 19 AM 293 1015.0  28  5.35   70.8 71.0
     3 2   0 09/09/95  8 20 AM 293 1015.0  24  4.61   71.0 70.5
     3 2   0 09/09/95  8 21 AM 293 1015.0  22  4.23   66.0 66.5
     3 2   0 09/09/95  8 22 AM 293 1015.0  20  3.85   63.4 62.5
     3 2   0 09/09/95  8 23 AM 293 1015.0  18  3.47   56.0 56.5
     3 2   0 09/09/95  8 24 AM 293 1015.0  16  3.08   49.0 49.5
     3 2   0 09/09/95  8 25 AM 293 1015.0  15  2.88   44.0 44.0
     3 2   0 09/09/95  8 26 AM 293 1015.0  14  2.69   40.5 40.5
     3 2   0 09/09/95  8 27 AM 293 1015.0  13  2.49   34.4 34.0
     3 2   0 09/09/95  8 28 AM 293 1015.0  12  2.29   22.3 22.0
     3 2   0 09/09/95  8 29 AM 293 1015.0  11  2.10   20.0 20.0
     3 2   0 09/09/95  8 30 AM 293 1015.0  10  1.90   15.9 19.0
     3 2   0 09/09/95  8 31 AM 293 1015.0   9  1.70   13.5 13.0
     3 2   0 09/09/95  8 32 AM 293 1015.0   8  1.50   10.0 10.0
     3 2   0 09/09/95  8 33 AM 293 1015.0   7  1.29    8.0  8.5
     3 2   0 09/09/95  8 34 AM 293 1015.0   6  1.09    7.2  7.5
     3 2   0 09/09/95  8 35 AM 293 1015.0   0  0.00    2.5  3.0
     3 2   0 09/09/95  8 42 AM 293 1015.0   6  1.09    6.5  6.5
     3 2   0 09/09/95  8 43 AM 293 1015.0   7  1.29    7.5  8.0
     3 2   0 09/09/95  8 44 AM 293 1015.0   8  1.50   10.0 10.0
     3 2   0 09/09/95  8 45 AM 293 1015.0   9  1.70   13.0 12.5
     3 2   0 09/09/95  8 46 AM 293 1015.0  10  1.90   16.0 16.0
     3 2   0 09/09/95  8 47 AM 293 1015.0  11  2.10   19.0 19.5
     3 2   0 09/09/95  8 48 AM 293 1015.0  12  2.29   22.3 22.5
     3 2   0 09/09/95  8 49 AM 293 1015.0  13  2.49   33.5 33.0
     3 2   0 09/09/95  8 50 AM 293 1015.0  14  2.69   40.3 40.0
     3 2   0 09/09/95  8 51 AM 293 1015.0  15  2.88   45.0 45.5
     3 2   0 09/09/95  8 52 AM 293 1015.0  16  3.08   49.0 50.0
     3 2   0 09/09/95  8 53 AM 293 1015.0  18  3.47   57.5 56.5
     3 2   0 09/09/95  8 54 AM 293 1015.0  20  3.85   62.4 62.5
     3 2   0 09/09/95  8 55 AM 293 1015.0  22  4.23   66.5 66.0
     3 2   0 09/09/95  8 56 AM 293 1015.0  24  4.61   70.0 69.5
     3 2   0 09/09/95  8 57 AM 293 1015.0  28  5.35   71.3 71.0
     3 2   0 09/09/95  8 58 AM 293 1015.0  32  6.09   71.0 71.0
     3 2   0 09/09/95  8 59 AM 293 1015.0  45  8.38   70.5 71.0
     3 2  30 09/09/95  9  1 AM 293 1015.0   0  0.00    5.0  5.0
     3 2  90 09/09/95  9  6 AM 293 1015.0   0  0.00 B114.0
     3 2 120 09/09/95  9  9 AM 293 1015.0   0  0.00    1.5  2.0
     3 2 150 09/09/95  9 16 AM 293 1015.0   0  0.00    1.5  1.5
     3 2 300 09/09/95  9 19 AM 293 1015.0   0  0.00    4.0  4.5
     3 2 330 09/09/95  9 21 AM 293 1015.0   0  0.00    5.5  5.0
     3 3  ND 09/09/95  9 33 AM 293 1015.0   0  0.00    1.5  2.0
     3 3  60 09/09/95  9 40 AM 293 1015.0  45  8.38   84.0 84.0 84.0
     3 3  60 09/09/95  9 41 AM 293 1015.0  32  6.09   78.5 79.0 78.0
     3 3  60 09/09/95  9 42 AM 293 1015.0  28  5.35   76.1 75.0 75.5
     3 3  60 09/09/95  9 43 AM 293 1015.0  24  4.61   70.5 70.0 70.0
     3 3  60 09/09/95  9 44 AM 293 1015.0  22  4.23   66.0 66.0 65.5
     3 3  60 09/09/95  9 45 AM 293 1015.0  20  3.85   61.2 62.0 61.0
     3 3  60 09/09/95  9 46 AM 293 1015.0  18  3.47   54.1 55.0 54.0
     3 3  60 09/09/95  9 47 AM 293 1015.0  16  3.08   48.0 48.0 48.0
     3 3  60 09/09/95  9 48 AM 293 1015.0  15  2.88   43.5 44.0 44.0
     3 3  60 09/09/95  9 49 AM 293 1015.0  14  2.69   38.5 38.0 38.0
     3 3  60 09/09/95  9 50 AM 293 1015.0  13  2.49   31.0 31.0 31.0
     3 3  60 09/09/95  9 51 AM 293 1015.0  12  2.29  25.0 25.0 25.0 25.0
     3 3  60 09/09/95  9 52 AM 293 1015.0  11  2.10  20.0 20.0 20.0 20.5
     3 3  60 09/09/95  9 53 AM 293 1015.0  10  1.90   16.5 17.0 17.0
     3 3  60 09/09/95  9 54 AM 293 1015.0   9  1.70   14.0 15.0 15.0
     3 3  60 09/09/95  9 55 AM 293 1015.0   8  1.50   12.0 12.0 12.0
     3 3  60 09/09/95  9 56 AM 293 1015.0   7  1.29   10.5 11.0 11.0
     3 3  60 09/09/95  9 57 AM 293 1015.0   6  1.09    8.5  9.0  9.0
     3 3  60 09/09/95  9 58 AM 293 1015.0   0  0.00    4.0  5.0  5.0
     3 3  60 09/09/95 10  0 AM 293 1015.0   6  1.09    6.0  6.0  6.5
     3 3  60 09/09/95 10  1 AM 293 1015.0   7  1.29    7.0  8.0  7.0
     3 3  60 09/09/95 10  2 AM 293 1015.0   8  1.50   10.0  9.0  9.5
     3 3  60 09/09/95 10  3 AM 293 1015.0   9  1.70   12.0 12.0 12.0
     3 3  60 09/09/95 10  4 AM 293 1015.0  10  1.90   14.5 15.0 15.0
     3 3  60 09/09/95 10  5 AM 293 1015.0  11  2.10   19.0 18.0 18.5
     3 3  60 09/09/95 10  6 AM 293 1015.0  12  2.29  24.0 24.0 24.0 24.5
     3 3  60 09/09/95 10  7 AM 293 1015.0  13  2.49   29.6 30.0 30.0
     3 3  60 09/09/95 10  8 AM 293 1015.0  14  2.69   36.5 37.0 37.0
     3 3  60 09/09/95 10  9 AM 293 1015.0  15  2.88   43.0 43.0 43.0
     3 3  60 09/09/95 10 10 AM 293 1015.0  16  3.08   47.0 47.0 47.0
     3 3  60 09/09/95 10 11 AM 293 1015.0  18  3.47   56.5 56.0 55.5
     3 3  60 09/09/95 10 12 AM 293 1015.0  20  3.85  61.5 62.0 61.5 62.0
     3 3  60 09/09/95 10 13 AM 293 1015.0  22  4.23   66.0 66.0 66.0
     3 3  60 09/09/95 10 14 AM 293 1015.0  24  4.61   70.5 70.0 70.0
     3 3  60 09/09/95 10 15 AM 293 1015.0  28  5.35   75.0 75.0 74.5
     3 3  60 09/09/95 10 16 AM 293 1015.0  32  6.09   79.3 79.0 78.0
     3 3  60 09/09/95 10 17 AM 293 1015.0  45  8.38   84.0 84.0 83.5
     3 3 180 09/09/95 10 18 AM 293 1015.0  45  8.38   70.0
     3 3 180 09/09/95 10 19 AM 293 1015.0  32  6.09   69.0
     3 3 180 09/09/95 10 20 AM 293 1015.0  28  5.35   68.0
     3 3 180 09/09/95 10 21 AM 293 1015.0  24  4.61   62.5
     3 3 180 09/09/95 10 22 AM 293 1015.0  22  4.23   56.5 57.0
     3 3 180 09/09/95 10 23 AM 293 1015.0  20  3.85   52.0
     3 3 180 09/09/95 10 24 AM 293 1015.0  18  3.47   44.5
     3 3 180 09/09/95 10 25 AM 293 1015.0  16  3.08   33.4
     3 3 180 09/09/95 10 26 AM 293 1015.0  15  2.88   28.5
     3 3 180 09/09/95 10 27 AM 293 1015.0  14  2.69   29.0
     3 3 180 09/09/95 10 28 AM 293 1015.0  13  2.49   17.5
     3 3 180 09/09/95 10 29 AM 293 1015.0  12  2.29   15.0 15.0
     3 3 180 09/09/95 10 30 AM 293 1015.0  11  2.10   13.0 13.0
     3 3 180 09/09/95 10 31 AM 293 1015.0  10  1.90   10.0 10.5
     3 3 180 09/09/95 10 32 AM 293 1015.0   9  1.70    8.4  9.0
     3 3 180 09/09/95 10 33 AM 293 1015.0   8  1.50    6.3  7.0  6.0
     3 3 180 09/09/95 10 34 AM 293 1015.0   7  1.29    5.3  5.5  3.0
     3 3 180 09/09/95 10 35 AM 293 1015.0   6  1.09    2.5  3.0  0.0
     3 3 180 09/09/95 10 36 AM 293 1015.0   0  0.00   -0.5  0.0  3.5
     3 3 180 09/09/95 10 37 AM 293 1015.0   6  1.09    3.5  4.0  5.0
     3 3 180 09/09/95 10 38 AM 293 1015.0   7  1.29    5.0  5.5  6.5
     3 3 180 09/09/95 10 39 AM 293 1015.0   8  1.50    6.5  7.0  8.5
     3 3 180 09/09/95 10 40 AM 293 1015.0   9  1.70    8.0 10.0
     3 3 180 09/09/95 10 41 AM 293 1015.0  10  1.90   10.0 12.0
     3 3 180 09/09/95 10 42 AM 293 1015.0  11  2.10   12.0 15.0
     3 3 180 09/09/95 10 43 AM 293 1015.0  12  2.29   14.5
     3 3 180 09/09/95 10 44 AM 293 1015.0  13  2.49   19.4
     3 3 180 09/09/95 10 45 AM 293 1015.0  14  2.69   23.5
     3 3 180 09/09/95 10 46 AM 293 1015.0  15  2.88   32.0
     3 3 180 09/09/95 10 47 AM 293 1015.0  16  3.08   36.0
     3 3 180 09/09/95 10 48 AM 293 1015.0  18  3.47   42.5
     3 3 180 09/09/95 10 49 AM 293 1015.0  20  3.85   53.5
     3 3 180 09/09/95 10 50 AM 293 1015.0  22  4.23   56.0
     3 3 180 09/09/95 10 51 AM 293 1015.0  24  4.61   62.1
     3 3 180 09/09/95 10 52 AM 293 1015.0  28  5.35   68.0
     3 3 180 09/09/95 10 53 AM 293 1015.0  32  6.09   70.0
     3 3 180 09/09/95 10 54 AM 293 1015.0  45  8.38   69.3
     3 3 180 09/09/95 10 54 AM 293 1015.0  45  8.38   69.5
     3 3 210 09/09/95 10 56 AM 293 1015.0  45  8.38   84.5
     3 3 210 09/09/95 10 57 AM 293 1015.0  32  6.09   79.0
     3 3 210 09/09/95 10 58 AM 293 1015.0  28  5.35   75.0
     3 3 210 09/09/95 10 59 AM 293 1015.0  24  4.61   69.0
     3 3 210 09/09/95 11  0 AM 293 1015.0  22  4.23   65.0
     3 3 210 09/09/95 11  1 AM 293 1015.0  20  3.85   59.5
     3 3 210 09/09/95 11  2 AM 293 1015.0  18  3.47   51.5
     3 3 210 09/09/95 11  3 AM 293 1015.0  16  3.08   45.0
     3 3 210 09/09/95 11  4 AM 293 1015.0  15  2.88   38.5
     3 3 210 09/09/95 11  5 AM 293 1015.0  14  2.69   32.7
     3 3 210 09/09/95 11  6 AM 293 1015.0  13  2.49   26.0
     3 3 210 09/09/95 11  7 AM 293 1015.0  12  2.29   19.0
     3 3 210 09/09/95 11  8 AM 293 1015.0  11  2.10   15.5
     3 3 210 09/09/95 11  9 AM 293 1015.0  10  1.90   13.5
     3 3 210 09/09/95 11 10 AM 293 1015.0   9  1.70   11.0
     3 3 210 09/09/95 11 11 AM 293 1015.0   8  1.50    8.5
     3 3 210 09/09/95 11 12 AM 293 1015.0   7  1.29    7.0
     3 3 210 09/09/95 11 13 AM 293 1015.0   6  1.09    4.7
     3 3 210 09/09/95 11 14 AM 293 1015.0   0  0.00    1.5
     3 3 210 09/09/95 11 16 AM 293 1015.0   6  1.09    3.4
     3 3 210 09/09/95 11 17 AM 293 1015.0   7  1.29    5.5
     3 3 210 09/09/95 11 18 AM 293 1015.0   8  1.50    7.0
     3 3 210 09/09/95 11 19 AM 293 1015.0   9  1.70   10.4
     3 3 210 09/09/95 11 20 AM 293 1015.0  10  1.90   12.7
     3 3 210 09/09/95 11 21 AM 293 1015.0  11  2.10   16.5
     3 3 210 09/09/95 11 22 AM 293 1015.0  12  2.29   21.0
     3 3 210 09/09/95 11 23 AM 293 1015.0  13  2.49   25.5
     3 3 210 09/09/95 11 24 AM 293 1015.0  14  2.69   33.0
     3 3 210 09/09/95 11 25 AM 293 1015.0  15  2.88   38.5
     3 3 210 09/09/95 11 26 AM 293 1015.0  16  3.08   45.1
     3 3 210 09/09/95 11 26 AM 293 1015.0  16  3.08   45.1
     3 3 210 09/09/95 11 27 AM 293 1015.0  18  3.47   52.8
     3 3 210 09/09/95 11 28 AM 293 1015.0  20  3.85   60.3
     3 3 210 09/09/95 11 29 AM 293 1015.0  22  4.23   65.0
     3 3 210 09/09/95 11 30 AM 293 1015.0  24  4.61   69.0
     3 3 210 09/09/95 11 31 AM 293 1015.0  28  5.35   74.5
     3 3 210 09/09/95 11 32 AM 293 1015.0  32  6.09   79.5
     3 3 210 09/09/95 11 33 AM 293 1015.0  45  8.38   84.0
     3 3 210 09/09/95 11 34 AM 293 1015.0  16  3.08   46.0
     3 3 240 09/09/95 11 35 AM 293 1015.0  45  8.38   84.5
     3 3 240 09/09/95 11 36 AM 293 1015.0  32  6.09   79.0
     3 3 240 09/09/95 11 37 AM 293 1015.0  28  5.35   76.0
     3 3 240 09/09/95 11 38 AM 293 1015.0  24  4.61   69.0
     3 3 240 09/09/95 11 39 AM 293 1015.0  22  4.23   65.0
     3 3 240 09/09/95 11 40 AM 293 1015.0  20  3.85   59.7 60.0
     3 3 240 09/09/95 11 41 AM 293 1015.0  18  3.47   51.0
     3 3 240 09/09/95 11 42 AM 293 1015.0  16  3.08   46.0
     3 3 240 09/09/95 11 43 AM 293 1015.0  15  2.88   37.0
     3 3 240 09/09/95 11 44 AM 293 1015.0  14  2.69   30.0
     3 3 240 09/09/95 11 45 AM 293 1015.0  13  2.49   26.0
     3 3 240 09/09/95 11 46 AM 293 1015.0  12  2.29   20.3
     3 3 240 09/09/95 11 47 AM 293 1015.0  11  2.10   16.0
     3 3 240 09/09/95 11 48 AM 293 1015.0  10  1.90   13.3
     3 3 240 09/09/95 11 49 AM 293 1015.0   9  1.70   10.0
     3 3 240 09/09/95 11 50 AM 293 1015.0   8  1.50    8.5
     3 3 240 09/09/95 11 51 AM 293 1015.0   7  1.29    7.0  7.0
     3 3 240 09/09/95 11 52 AM 293 1015.0   6  1.09    5.5  6.0
     3 3 240 09/09/95 11 53 AM 293 1015.0   0  0.00    1.5  6.0
     3 3 240 09/09/95 11 55 AM 293 1015.0   6  1.09    4.0  4.5
     3 3 240 09/09/95 11 56 AM 293 1015.0   7  1.29    5.7  6.0
     3 3 240 09/09/95 11 57 AM 293 1015.0   8  1.50    8.0  8.0
     3 3 240 09/09/95 11 58 AM 293 1015.0   9  1.70   10.0 11.0
     3 3 240 09/09/95 11 59 AM 293 1015.0  10  1.90   14.5 14.0
     3 3 240 09/09/95 12  0 PM 293 1015.0  11  2.10   16.0
     3 3 240 09/09/95 12  1 PM 293 1015.0  12  2.29   20.5
     3 3 240 09/09/95 12  2 PM 293 1015.0  13  2.49   24.4
     3 3 240 09/09/95 12  3 PM 293 1015.0  14  2.69   31.2
     3 3 240 09/09/95 12  4 PM 293 1015.0  15  2.88   41.5
     3 3 240 09/09/95 12  5 PM 293 1015.0  16  3.08   39.7
     3 3 240 09/09/95 12  6 PM 293 1015.0  18  3.47   53.5
     3 3 240 09/09/95 12  7 PM 293 1015.0  20  3.85   58.7 58.5
     3 3 240 09/09/95 12  8 PM 293 1015.0  22  4.23   64.7
     3 3 240 09/09/95 12  9 PM 293 1015.0  24  4.61   69.0
     3 3 240 09/09/95 12 10 PM 293 1015.0  28  5.35   75.0
     3 3 240 09/09/95 12 11 PM 293 1015.0  32  6.09   79.5
     3 3 240 09/09/95 12 12 PM 293 1015.0  45  8.38   84.5
     3 3 300 09/09/95 12 14 PM 293 1015.0   0  0.00    4.0  5.0
     3 3 330 09/09/95 12 16 PM 293 1015.0   0  0.00    5.0  5.0
     3 3  30 09/09/95 12 18 PM 293 1015.0   0  0.00    4.0  4.5
     3 3  90 09/09/95 12 20 PM 293 1015.0   0  0.00 B118.1
     3 3 120 09/09/95 12 22 PM 293 1015.0   0  0.00    3.0  3.0
     3 3 150 09/09/95 12 23 PM 293 1015.0   0  0.00    3.3  2.5
     4 3  ND 09/09/95  2 49 PM 293 1015.0  ND    ND    0.0
     4 3 270 09/09/95  2 55 PM 293 1015.0  45  8.38   84.0
     4 3 270 09/09/95  2 56 PM 293 1015.0  32  6.09   79.5
     4 3 270 09/09/95  2 57 PM 293 1015.0  28  5.35   77.0
     4 3 270 09/09/95  2 58 PM 293 1015.0  24  4.61   70.0
     4 3 270 09/09/95  2 59 PM 293 1015.0  22  4.23   65.0
     4 3 270 09/09/95  3  0 PM 293 1015.0  20  3.85   61.0
     4 3 270 09/09/95  3  1 PM 293 1015.0  18  3.47   51.0
     4 3 270 09/09/95  3  2 PM 293 1015.0  16  3.08   47.0
     4 3 270 09/09/95  3  3 PM 293 1015.0  15  2.88   42.5
     4 3 270 09/09/95  3  4 PM 293 1015.0  14  2.69   35.0
     4 3 270 09/09/95  3  5 PM 293 1015.0  13  2.49   28.0
     4 3 270 09/09/95  3  6 PM 293 1015.0  12  2.29   21.0
     4 3 270 09/09/95  3  7 PM 293 1015.0  11  2.10   18.0
     4 3 270 09/09/95  3  8 PM 293 1015.0  10  1.90   15.0
     4 3 270 09/09/95  3  9 PM 293 1015.0   9  1.70   12.0
     4 3 270 09/09/95  3 10 PM 293 1015.0   8  1.50    9.0
     4 3 270 09/09/95  3 11 PM 293 1015.0   7  1.29    6.0
     4 3 270 09/09/95  3 12 PM 293 1015.0   6  1.09    6.0
     4 3 270 09/09/95  3 13 PM 293 1015.0   0  0.00    1.0
     4 3 270 09/09/95  3 15 PM 293 1015.0   6  1.09    5.0
     4 3 270 09/09/95  3 16 PM 293 1015.0   7  1.29    6.0
     4 3 270 09/09/95  3 17 PM 293 1015.0   8  1.50    8.0
     4 3 270 09/09/95  3 18 PM 293 1015.0   9  1.70   10.0
     4 3 270 09/09/95  3 19 PM 293 1015.0  10  1.90   14.0
     4 3 270 09/09/95  3 20 PM 293 1015.0  11  2.10   17.0
     4 3 270 09/09/95  3 21 PM 293 1015.0  12  2.29   22.0
     4 3 270 09/09/95  3 22 PM 293 1015.0  13  2.49   26.5
     4 3 270 09/09/95  3 23 PM 293 1015.0  14  2.69   34.5
     4 3 270 09/09/95  3 24 PM 293 1015.0  15  2.88   41.0
     4 3 270 09/09/95  3 25 PM 293 1015.0  16  3.08   46.5
     4 3 270 09/09/95  3 26 PM 293 1015.0  18  3.47   54.5
     4 3 270 09/09/95  3 27 PM 293 1015.0  20  3.85   59.0
     4 3 270 09/09/95  3 28 PM 293 1015.0  22  4.23   66.0
     4 3 270 09/09/95  3 29 PM 293 1015.0  24  4.61   70.0
     4 3 270 09/09/95  3 30 PM 293 1015.0  28  5.35   75.0
     4 3 270 09/09/95  3 31 PM 293 1015.0  32  6.09   78.0
     4 3 270 09/09/95  3 32 PM 293 1015.0  45  8.38   84.0
     4 3   0 09/09/95  3 34 PM 293 1015.0  45  8.38   70.0
     4 3   0 09/09/95  3 35 PM 293 1015.0  32  6.09   70.0
     4 3   0 09/09/95  3 36 PM 293 1015.0  28  5.35   70.0
     4 3   0 09/09/95  3 37 PM 293 1015.0  24  4.61   68.0
     4 3   0 09/09/95  3 38 PM 293 1015.0  22  4.23   65.0
     4 3   0 09/09/95  3 39 PM 293 1015.0  20  3.85   60.0
     4 3   0 09/09/95  3 40 PM 293 1015.0  18  3.47   54.0
     4 3   0 09/09/95  3 41 PM 293 1015.0  16  3.08   46.0
     4 3   0 09/09/95  3 43 PM 293 1015.0  15  2.88   41.0
     4 3   0 09/09/95  3 44 PM 293 1015.0  14  2.69   38.0
     4 3   0 09/09/95  3 45 PM 293 1015.0  13  2.49   28.0
     4 3   0 09/09/95  3 46 PM 293 1015.0  12  2.29   20.0
     4 3   0 09/09/95  3 47 PM 293 1015.0  11  2.10   17.0
     4 3   0 09/09/95  3 48 PM 293 1015.0  10  1.90   15.0
     4 3   0 09/09/95  3 49 PM 293 1015.0   9  1.70   12.0
     4 3   0 09/09/95  3 50 PM 293 1015.0   8  1.50   10.0
     4 3   0 09/09/95  3 51 PM 293 1015.0   7  1.29    8.0
     4 3   0 09/09/95  3 52 PM 293 1015.0   6  1.09    6.0
     4 3   0 09/09/95  3 53 PM 293 1015.0   0  0.00    2.0
     4 3   0 09/09/95  3 54 PM 293 1015.0   6  1.09    5.0
     4 3   0 09/09/95  3 55 PM 293 1015.0   7  1.29    8.5
     4 3   0 09/09/95  3 56 PM 293 1015.0   8  1.50   10.0
     4 3   0 09/09/95  3 57 PM 293 1015.0   9  1.70   12.0
     4 3   0 09/09/95  3 58 PM 293 1015.0  10  1.90   15.0
     4 3   0 09/09/95  3 59 PM 293 1015.0  11  2.10   17.5
     4 3   0 09/09/95  4  0 PM 293 1015.0  12  2.29   20.0
     4 3   0 09/09/95  4  1 PM 293 1015.0  13  2.49   27.0
     4 3   0 09/09/95  4  2 PM 293 1015.0  14  2.69   36.0
     4 3   0 09/09/95  4  3 PM 293 1015.0  15  2.88   39.0
     4 3   0 09/09/95  4  4 PM 293 1015.0  16  3.08   44.0
     4 3   0 09/09/95  4  5 PM 293 1015.0  18  3.47   52.5
     4 3   0 09/09/95  4  6 PM 293 1015.0  20  3.85   59.0
     4 3   0 09/09/95  4  7 PM 293 1015.0  22  4.23   65.0
     4 3   0 09/09/95  4  8 PM 293 1015.0  24  4.61   69.0
     4 3   0 09/09/95  4  9 PM 293 1015.0  28  5.35   70.0
     4 3   0 09/09/95  4 10 PM 293 1015.0  32  6.09   71.0
     4 3   0 09/09/95  4 11 PM 293 1015.0  45  8.38   69.0
     5 1  ND 09/12/95  6 19 AM 293    0.0 N/A    ND    2.0
     5 1  ND 09/12/95  6 20 AM 293    0.0 N/A    ND    1.5
     5 1  60 09/12/95  7 16 AM 290   14.9 N/A  9.85    7.0  8.0
     5 1  60 09/12/95  7 17 AM 290   14.8 N/A 13.49   11.0 12.0
     5 1  60 09/12/95  7 23 AM 290   14.6 N/A 16.38   19.0 18.0
     5 1  60 09/12/95  7 25 AM 290   14.7 N/A 24.61   42.5 42.0
     5 1  60 09/12/95  7 26 AM 290   14.8 N/A 28.70   58.0 56.5
     5 1  60 09/12/95  7 27 AM 290   15.0 N/A 32.02   65.0 64.0
     5 1  60 09/12/95  7 29 AM 290   15.3 N/A 37.58   71.5 71.5
     5 1  60 09/12/95  7 31 AM 290   14.9 N/A 30.60   63.0 62.5
     5 1  60 09/12/95  7 32 AM 290   14.3 N/A 24.09   41.0 41.0
     5 1  60 09/12/95  7 33 AM 290   14.0 N/A 19.32   25.5 26.0
     5 1  60 09/12/95  7 34 AM 290   14.0 N/A 10.86   11.0 11.0
     5 1  60 09/12/95  7 35 AM 290   14.0 N/A  2.44    4.0  6.0
     5 1  60 09/12/95  7 36 AM 290   14.3 N/A  7.47    5.0  6.5
     5 1  60 09/12/95  7 37 AM 290   14.5 N/A 11.83    8.0 10.0
     5 1  60 09/12/95  7 38 AM 290   14.8 N/A 24.87   42.0 42.5
     5 1  60 09/12/95  7 39 AM 290   15.1 N/A 27.17   54.0 53.5
     5 1  60 09/12/95  7 40 AM 290   15.2 N/A 30.77   63.0 62.0
     5 1  60 09/12/95  7 41 AM 290   15.2 N/A 41.59   76.0 75.0
     5 1  60 09/12/95  7 42 AM 290   15.2 N/A 27.70   55.0 56.0
     5 1  60 09/12/95  7 43 AM 290   14.9 N/A 24.09   42.0 42.5
     5 1  60 09/12/95  7 44 AM 290   14.9 N/A 21.00   30.0 31.0
     5 1  60 09/12/95  7 45 AM 290   14.8 N/A 18.75   25.0 25.5
     5 1  60 09/12/95  7 46 AM 290   14.8 N/A 15.61   17.0 18.0
     5 1  60 09/12/95  7 47 AM 290   14.6 N/A 12.44   11.0 12.0
     5 1  60 09/12/95  7 48 AM 290   14.8 N/A  9.32    8.0 10.0
     5 1  60 09/12/95  7 49 AM 290   14.9 N/A  5.99    5.5  7.5
     5 1  60 09/12/95  7 50 AM 290   15.1 N/A 11.62    7.5  9.5
     5 1  60 09/12/95  7 51 AM 290   15.1 N/A 16.36   16.0 18.0
     5 1  60 09/12/95  7 52 AM 290   15.2 N/A 18.03   22.0 22.5
     5 1  60 09/12/95  7 53 AM 290   15.4 N/A 20.21   27.0 28.5
     5 1  60 09/12/95  7 54 AM 290   15.2 N/A 22.52   35.0 34.5
     5 1  60 09/12/95  7 55 AM 290   15.0 N/A 25.88   51.0 51.0
     5 1  60 09/12/95  7 56 AM 290   14.9 N/A 20.28   30.0 29.5
     5 1  60 09/12/95  7 57 AM 290   14.7 N/A 17.63   21.0 22.5
     5 1  60 09/12/95  7 58 AM 290   14.7 N/A 13.34   12.5 13.0
     5 1  60 09/12/95  7 59 AM 290   14.9 N/A 10.13   10.0 11.0
     5 1  60 09/12/95  8  0 AM 290   15.0 N/A  7.90    8.0  9.5
     5 1 180 09/12/95 12  8 PM 290   15.0 N/A 14.93    5.0
     5 1 180 09/12/95 12  9 PM 290   14.9 N/A 17.62    9.0
     5 1 180 09/12/95 12 10 PM 290   14.8 N/A 22.60   16.5
     5 1 180 09/12/95 12 11 PM 290   14.7 N/A 28.51   29.0
     5 1 180 09/12/95 12 12 PM 290   14.8 N/A 30.84   41.0
     5 1 180 09/12/95 12 13 PM 290   14.8 N/A 33.21   49.0
     5 1 180 09/12/95 12 14 PM 290   14.9 N/A 35.56   55.0
     5 1 180 09/12/95 12 15 PM 290   15.1 N/A 40.87   64.0
     5 1 180 09/12/95 12 16 PM 290   15.1 N/A 38.27   60.0
     5 1 180 09/12/95 12 17 PM 290   14.9 N/A 34.74   54.0
     5 1 180 09/12/95 12 18 PM 290   14.8 N/A 31.08   42.0
     5 1 180 09/12/95 12 19 PM 290   14.8 N/A 28.49   29.5
     5 1 180 09/12/95 12 20 PM 290   14.8 N/A 25.47   20.0
     5 1 180 09/12/95 12 21 PM 290   14.8 N/A 21.26   15.0
     5 1 180 09/12/95 12 22 PM 290   14.7 N/A 19.42   15.0
     5 1 180 09/12/95 12 23 PM 290   14.6 N/A 15.95   12.0
     5 1 180 09/12/95 12 24 PM 290   14.7 N/A 12.68    7.0
     5 1 180 09/12/95 12 25 PM 290   14.7 N/A  8.17    5.0
     5 1 180 09/12/95 12 26 PM 290   14.7 N/A  5.36    5.0
     5 1   0 09/12/95 12 28 PM 290   14.7 N/A 14.32    9.0
     5 1   0 09/12/95 12 29 PM 290   14.8 N/A 19.80   25.0
     5 1   0 09/12/95 12 30 PM 290   15.0 N/A 21.37   31.0
     5 1   0 09/12/95 12 31 PM 290   14.8 N/A 24.80   43.0
     5 1   0 09/12/95 12 32 PM 290   14.5 N/A 28.88   54.0
     5 1   0 09/12/95 12 33 PM 290   14.4 N/A 31.93   59.0
     5 1   0 09/12/95 12 34 PM 290   14.3 N/A 35.71   65.0
     5 1   0 09/12/95 12 35 PM 290   14.3 N/A 39.30   70.0
     5 1   0 09/12/95 12 37 PM 290   14.7 N/A 35.07   65.0
     5 1   0 09/12/95 12 38 PM 290   14.8 N/A 30.94   59.0
     5 1   0 09/12/95 12 39 PM 290   14.9 N/A 28.40   52.5
     5 1   0 09/12/95 12 40 PM 290   14.9 N/A 21.79   33.0
     5 1   0 09/12/95 12 41 PM 290   14.8 N/A 18.43   26.0
     5 1   0 09/12/95 12 42 PM 290   14.7 N/A 15.60   19.0
     5 1   0 09/12/95 12 43 PM 290   14.9 N/A 12.21   14.0
     5 1   0 09/12/95 12 44 PM 290   15.1 N/A  9.65   12.0
     5 1   0 09/12/95 12 45 PM 290   15.1 N/A  6.00    9.5
     5 1   0 09/12/95 12 46 PM 290   15.3 N/A  1.50    6.0
     5 1 240 09/12/95 12 49 PM 290   14.9 N/A 11.69    7.0
     5 1 240 09/12/95  2 52 PM 290   14.9 N/A 10.95    6.5
     5 1 240 09/12/95  2 53 PM 290   14.6 N/A 14.72    8.5
     5 1 240 09/12/95  2 54 PM 290   14.5 N/A 18.29   15.0
     5 1 240 09/12/95  2 55 PM 290   14.3 N/A 22.67   28.0
     5 1 240 09/12/95  2 56 PM 290   14.1 N/A 25.65   38.0
     5 1 240 09/12/95  2 57 PM 290   14.1 N/A 28.01   50.0
     5 1 240 09/12/95  2 58 PM 290   14.1 N/A 31.67   60.0
     5 1 240 09/12/95  2 59 PM 290   14.1 N/A 35.03   65.0
     5 1 240 09/12/95  3  0 PM 290   14.3 N/A 41.10   73.0
     5 1 240 09/12/95  3  1 PM 290   14.5 N/A 46.89   78.0
     5 1 240 09/12/95  3  2 PM 290   14.6 N/A 38.47   71.0
     5 1 240 09/12/95  3  3 PM 290   14.6 N/A 32.96   63.5
     5 1 240 09/12/95  3  4 PM 290   14.6 N/A 29.22   55.0
     5 1 240 09/12/95  3  5 PM 290   14.4 N/A 25.41   44.0
     5 1 240 09/12/95  3  6 PM 290   14.5 N/A 23.16   33.0
     5 1 240 09/12/95  3  7 PM 290   14.5 N/A 17.94   21.0
     5 1 240 09/12/95  3  8 PM 290   14.5 N/A 13.75   14.0
     5 1 240 09/12/95  3  9 PM 290   14.4 N/A  9.32    8.0
     5 1 240 09/12/95  3 10 PM 290   14.3 N/A  3.54    5.0
     5 1 270 09/12/95  3 13 PM 290   14.1 N/A 12.12    7.5
     5 1 270 09/12/95  3 14 PM 290   14.2 N/A 15.65   11.5
     5 1 270 09/12/95  3 15 PM 290   14.2 N/A 18.50   21.0
     5 1 270 09/12/95  3 16 PM 290   14.3 N/A 25.49   42.0
     5 1 270 09/12/95  3 17 PM 290   14.4 N/A 27.02   47.5
     5 1 270 09/12/95  3 18 PM 290   14.6 N/A 30.75   57.5
     5 1 270 09/12/95  3 19 PM 290   14.8 N/A 33.34   63.5
     5 1 270 09/12/95  3 20 PM 290   15.0 N/A 41.30   74.0
     5 1 270 09/12/95  3 21 PM 290   15.3 N/A 53.01   80.0
     5 1 270 09/12/95  3 23 PM 290   15.4 N/A 40.99   74.0
     5 1 270 09/12/95  3 24 PM 290   15.2 N/A 34.31   67.0
     5 1 270 09/12/95  3 25 PM 290   14.8 N/A 31.02   60.0
     5 1 270 09/12/95  3 26 PM 290   14.8 N/A 26.38   48.0
     5 1 270 09/12/95  3 30 PM 290    0.0 N/A  0.00    2.0
     5 1 270 09/12/95  4  3 PM 290   14.3 N/A 29.53   55.0
     5 1 270 09/12/95  4  4 PM 290   14.0 N/A 26.06   45.0
     5 1 270 09/12/95  4  5 PM 290   14.1 N/A 24.17   38.0
     5 1 270 09/12/95  4  7 PM 290   14.0 N/A 20.42   24.0
     5 1 270 09/12/95  4  8 PM 290   13.9 N/A 16.14   15.5
     5 1 270 09/12/95  4  9 PM 290   14.3 N/A 12.68    8.5
     5 1 270 09/12/95  4 10 PM 290   14.5 N/A  9.38    7.0
     5 1 270 09/12/95  4 11 PM 290   14.7 N/A  6.59    5.0
     5 2  60 09/13/95  6 30 AM 290    0.0 N/A  0.00    1.0
     5 2  60 09/13/95  7 20 AM 290   14.6 N/A  9.74    4.5  6.5
     5 2  60 09/13/95  7 21 AM 290   14.8 N/A 11.65    6.5  8.0
     5 2  60 09/13/95  7 22 AM 290   14.9 N/A 13.07   10.0 10.0
     5 2  60 09/13/95  7 23 AM 290   15.0 N/A 16.64   17.5 19.0
     5 2  60 09/13/95  7 24 AM 290   15.0 N/A 20.34   26.0 27.0
     5 2  60 09/13/95  7 25 AM 290   14.9 N/A 23.36   34.0 35.0
     5 2  60 09/13/95  7 26 AM 290   15.0 N/A 26.55   50.0 50.0
     5 2  60 09/13/95  7 27 AM 290   14.9 N/A 29.10   56.0 56.0
     5 2  60 09/13/95  7 28 AM 290   14.8 N/A 32.44   63.0 63.0
     5 2  60 09/13/95  7 29 AM 290   14.8 N/A 35.41   68.0 68.5
     5 2  60 09/13/95  7 30 AM 290   14.9 N/A 44.04   75.0 75.0
     5 2  60 09/13/95  7 31 AM 290   15.0 N/A 40.83   74.5 73.5
     5 2  60 09/13/95  7 32 AM 290   14.9 N/A 34.17   67.0 66.5
     5 2  60 09/13/95  7 33 AM 290   14.9 N/A 31.57   61.5 61.5
     5 2  60 09/13/95  7 34 AM 290   14.8 N/A 24.30   38.0 38.0
     5 2  60 09/13/95  7 35 AM 290   14.6 N/A 22.03   28.0 30.0
     5 2  60 09/13/95  7 36 AM 290   14.9 N/A 19.99   26.0 26.0
     5 2  60 09/13/95  7 37 AM 290   15.0 N/A 18.25   22.5 22.5
     5 2  60 09/13/95  7 38 AM 290   14.9 N/A 12.25   10.0 10.5
     5 2  60 09/13/95  7 39 AM 290   14.9 N/A 10.41    8.0  9.0
     5 2  60 09/13/95  7 40 AM 290   14.8 N/A  8.68    6.5  7.0
     5 2  60 09/13/95  7 41 AM 290   14.8 N/A  5.90    4.5  5.5
     5 2 180 09/13/95  7 44 AM 290   14.8 N/A  6.42    3.0
     5 2 180 09/13/95  7 45 AM 290   14.7 N/A  9.78    4.0
     5 2 180 09/13/95  7 46 AM 290   14.7 N/A 13.14    6.0
     5 2 180 09/13/95  7 47 AM 290   14.7 N/A 15.55   10.0
     5 2 180 09/13/95  7 48 AM 290   14.8 N/A 18.71   12.0
     5 2 180 09/13/95  7 49 AM 290   14.8 N/A 21.49   14.0
     5 2 180 09/13/95  7 50 AM 290   14.9 N/A 25.79   21.0
     5 2 180 09/13/95  7 51 AM 290   15.1 N/A 28.62   32.5
     5 2 180 09/13/95  9  5 AM 290   14.8 N/A 27.31   24.5
     5 2 180 09/13/95  9  7 AM 290   14.9 N/A 28.65   33.0
     5 2 180 09/13/95  9  8 AM 290   15.0 N/A 30.25   40.0
     5 2 180 09/13/95  9  9 AM 290   15.0 N/A 32.08   46.0
     5 2 180 09/13/95  9 10 AM 290   15.0 N/A 35.95   56.0
     5 2 180 09/13/95  9 12 AM 290   15.4 N/A 43.97   68.0
     5 2 180 09/13/95  9 13 AM 290   15.1 N/A 36.98   59.5
     5 2 180 09/13/95  9 14 AM 290   15.0 N/A 32.80   47.0
     5 2 180 09/13/95  9 15 AM 290   14.9 N/A 28.73   36.0
     5 2 180 09/13/95  9 16 AM 290   14.9 N/A 26.62   24.0
     5 2 180 09/13/95  9 17 AM 290   14.7 N/A 19.86   14.0
     5 2 180 09/13/95  9 19 AM 290   15.0 N/A 16.40   12.0
     5 2 180 09/13/95  9 20 AM 290   15.0 N/A 14.90   10.0
     5 2 180 09/13/95  9 21 AM 290   14.9 N/A 12.57    6.0
     5 2 180 09/13/95  9 22 AM 290   14.7 N/A  8.79    4.0
     5 2 180 09/13/95  9 23 AM 290   14.9 N/A  4.39    2.0
     5 2   0 09/13/95 10 11 AM 290   14.6 N/A  6.20    4.0
     5 2   0 09/13/95 10 12 AM 290   14.6 N/A  8.72    7.0
     5 2   0 09/13/95 10 13 AM 290   14.6 N/A 12.41   10.0
     5 2   0 09/13/95 10 14 AM 290   14.7 N/A 15.07   15.0
     5 2   0 09/13/95 10 15 AM 290   14.7 N/A 17.75   20.0
     5 2   0 09/13/95 10 16 AM 290   14.8 N/A 20.70   27.0
     5 2   0 09/13/95 10 17 AM 290   15.0 N/A 22.85   36.0
     5 2   0 09/13/95 10 18 AM 290   14.8 N/A 24.61   42.5
     5 2   0 09/13/95 10 19 AM 290   14.7 N/A 27.59   50.0
     5 2   0 09/13/95 10 20 AM 290   14.8 N/A 30.31   57.0
     5 2   0 09/13/95 10 21 AM 290   14.8 N/A 33.75   63.0
     5 2   0 09/13/95 10 22 AM 290   14.9 N/A 37.68   69.0
     5 2   0 09/13/95 10 23 AM 290   14.9 N/A 35.37   66.0
     5 2   0 09/13/95 10 24 AM 290   14.9 N/A 32.46   63.0
     5 2   0 09/13/95 10 25 AM 290   14.8 N/A 29.06   54.5
     5 2   0 09/13/95 10 26 AM 290   14.8 N/A 25.90   46.0
     5 2   0 09/13/95 10 27 AM 290   14.9 N/A 22.17   33.0
     5 2   0 09/13/95 10 28 AM 290   14.9 N/A 19.87   27.5
     5 2   0 09/13/95 10 29 AM 290   14.9 N/A 15.71   21.5
     5 2   0 09/13/95 10 30 AM 290   14.8 N/A 11.68   15.5
     5 2   0 09/13/95 10 31 AM 290   14.9 N/A  7.98   12.0
     5 2   0 09/13/95 10 32 AM 290   15.1 N/A  2.85   11.0
     5 2 240 09/13/95 11 30 AM 290   14.9 N/A  9.54    3.5
     5 2 240 09/13/95 11 31 AM 290   15.1 N/A 15.26   11.0
     5 2 240 09/13/95 11 32 AM 290   14.9 N/A 18.97   20.0
     5 2 240 09/13/95 11 33 AM 290   14.7 N/A 21.92   27.0
     5 2 240 09/13/95 11 34 AM 290   14.6 N/A 24.70   34.0
     5 2 240 09/13/95 11 35 AM 290   14.6 N/A 26.28   46.0
     5 2 240 09/13/95 11 36 AM 290   14.6 N/A 28.56   52.0
     5 2 240 09/13/95 11 37 AM 290   14.5 N/A 31.84   61.0
     5 2 240 09/13/95 11 38 AM 290   14.6 N/A 35.50   67.0
     5 2 240 09/13/95 11 39 AM 290   14.7 N/A 42.11   74.0
     5 2 240 09/13/95 11 40 AM 290   14.7 N/A 36.85   69.0
     5 2 240 09/13/95 11 41 AM 290   14.5 N/A 31.09   60.5
     5 2 240 09/13/95 11 43 AM 290   14.6 N/A 27.26   52.0
     5 2 240 09/13/95 11 44 AM 290   14.7 N/A 24.98   45.0
     5 2 240 09/13/95 11 45 AM 290   14.7 N/A 22.86   34.0
     5 2 240 09/13/95 11 46 AM 290   14.7 N/A 19.36   25.0
     5 2 240 09/13/95 11 47 AM 290   14.7 N/A 14.15   16.0
     5 2 240 09/13/95 11 48 AM 290   14.6 N/A 13.42   13.5
     5 2 240 09/13/95 11 49 AM 290   14.6 N/A  7.91    9.0
     5 2 240 09/13/95 11 50 AM 290   14.5 N/A  3.52    4.5
     5 2 270 09/13/95 11 53 AM 290   14.9 N/A  9.72    7.0
     5 2 270 09/13/95 11 54 AM 290   15.0 N/A 12.16    9.5
     5 2 270 09/13/95 11 55 AM 290   14.8 N/A 13.75   11.5
     5 2 270 09/13/95 11 56 AM 290   14.5 N/A 16.28   19.0
     5 2 270 09/13/95 11 57 AM 290   14.5 N/A 18.10   21.0
     5 2 270 09/13/95 11 58 AM 290   14.4 N/A 21.17   30.0
     5 2 270 09/13/95 11 59 AM 290   14.4 N/A 24.29   37.0
     5 2 270 09/13/95 12  0 AM 290   14.5 N/A 26.74   48.0
     5 2 270 09/13/95 12  1 PM 290   14.6 N/A 29.60   57.0
     5 2 270 09/13/95 12  2 PM 290   14.7 N/A 35.21   67.0
     5 2 270 09/13/95 12  3 PM 290   14.7 N/A 42.55   74.0
     5 2 270 09/13/95 12  4 PM 290   14.7 N/A 35.94   68.5
     5 2 270 09/13/95 12  5 PM 290   14.7 N/A 31.12   61.0
     5 2 270 09/13/95 12  6 PM 290   14.9 N/A 26.94   50.0
     5 2 270 09/13/95 12  7 PM 290   14.9 N/A 25.66   47.0
     5 2 270 09/13/95 12  8 PM 290   14.9 N/A 23.56   38.5
     5 2 270 09/13/95 12  9 PM 290   15.0 N/A 19.94   29.0
     5 2 270 09/13/95 12 10 PM 290   15.0 N/A 16.70   19.5
     5 2 270 09/13/95 12 11 PM 290   14.9 N/A 14.64   15.0
     5 2 270 09/13/95 12 12 PM 290   14.9 N/A 11.95    9.5
     5 2 270 09/13/95 12 13 PM 290   14.9 N/A 10.21    8.0
     5 2 270 09/13/95 12 14 PM 290   14.9 N/A  5.57    7.0
     6 3  ND 09/14/95  6 24 AM 293 1015.0  ND    ND    0.5
     6 3  60 09/14/95  7 17 AM 290   14.7 N/A 11.02    8.5  8.0
     6 3  60 09/14/95  7 18 AM 290   14.8 N/A 13.14    9.5 10.0
     6 3  60 09/14/95  7 19 AM 290   14.8 N/A 14.94   13.0 13.0
     6 3  60 09/14/95  7 20 AM 290   14.9 N/A 18.32   21.0 21.0
     6 3  60 09/14/95  7 21 AM 290   15.0 N/A 20.88   27.0 27.0
     6 3  60 09/14/95  7 22 AM 290   15.0 N/A 24.29   36.0 35.5
     6 3  60 09/14/95  7 23 AM 290   15.0 N/A 25.63   43.0 43.0
     6 3  60 09/14/95  7 24 AM 290   15.0 N/A 27.31   49.5 50.0
     6 3  60 09/14/95  7 25 AM 290   15.0 N/A 29.82   55.5 56.0
     6 3  60 09/14/95  7 26 AM 290   14.9 N/A 35.77   65.5 66.0
     6 3  60 09/14/95  7 27 AM 290   14.9 N/A 40.64   71.0 71.5
     6 3  60 09/14/95  7 28 AM 290   15.0 N/A 37.01   67.5 68.0
     6 3  60 09/14/95  7 29 AM 290   14.9 N/A 35.27   65.0 65.5
     6 3  60 09/14/95  7 30 AM 290   14.9 N/A 31.92   60.0 60.5
     6 3  60 09/14/95  7 31 AM 290   14.9 N/A 27.70   50.0 51.5
     6 3  60 09/14/95  7 32 AM 290   14.9 N/A 26.47   45.0 46.0
     6 3  60 09/14/95  7 33 AM 290   14.8 N/A 23.67   35.5 35.0
     6 3  60 09/14/95  7 34 AM 290   14.8 N/A 20.62   27.0 27.5
     6 3  60 09/14/95  7 35 AM 290   14.9 N/A 17.31   20.0 20.0
     6 3  60 09/14/95  7 36 AM 290   14.9 N/A 14.73   13.0 13.5
     6 3  60 09/14/95  7 37 AM 290   14.9 N/A 10.98   11.0 11.0
     6 3  60 09/14/95  7 38 AM 290   14.9 N/A  7.18    7.0  7.5
     6 3 180 09/14/95  7 40 AM 290   14.9 N/A  8.65    2.0
     6 3 180 09/14/95  7 41 AM 290   14.9 N/A 13.40    7.0
     6 3 180 09/14/95  7 42 AM 290   14.9 N/A 17.06    9.5
     6 3 180 09/14/95  7 43 AM 290   15.1 N/A 19.42   12.5
     6 3 180 09/14/95  7 44 AM 290   14.9 N/A 24.25   16.5
     6 3 180 09/14/95  7 45 AM 290   14.8 N/A 26.26   19.0
     6 3 180 09/14/95  7 46 AM 290   14.9 N/A 27.99   27.5
     6 3 180 09/14/95  7 47 AM 290   14.8 N/A 29.85   36.0
     6 3 180 09/14/95  7 48 AM 290   14.9 N/A 32.66   47.5
     6 3 180 09/14/95  7 49 AM 290   15.0 N/A 35.03   54.5
     6 3 180 09/14/95  7 50 AM 290   14.9 N/A 38.79   59.0
     6 3 180 09/14/95  7 51 AM 290   14.9 N/A 43.13   67.5
     6 3 180 09/14/95  7 52 AM 290   15.0 N/A 38.20   58.0
     6 3 180 09/14/95  7 53 AM 290   15.0 N/A 34.02   49.0
     6 3 180 09/14/95  7 54 AM 290   15.0 N/A 31.42   39.0
     6 3 180 09/14/95  7 55 AM 290   15.2 N/A 29.28   39.0
     6 3 180 09/14/95  7 56 AM 290   15.0 N/A 27.55   23.0
     6 3 180 09/14/95  7 57 AM 290   14.9 N/A 26.24   20.0
     6 3 180 09/14/95  7 58 AM 290   14.9 N/A 23.76   13.0
     6 3 180 09/14/95  7 59 AM 290   14.8 N/A 20.05   12.5
     6 3 180 09/14/95  8  0 AM 290   14.9 N/A 17.55   10.0
     6 3 180 09/14/95  8  1 AM 290   15.0 N/A 13.67    6.0
     6 3 180 09/14/95  8  2 AM 290   14.9 N/A  8.90    2.5
     6 3   0 09/14/95  8 30 AM 290   14.9 N/A  6.49    4.5
     6 3   0 09/14/95  8 31 AM 290   14.8 N/A  9.23    6.5
     6 3   0 09/14/95  8 32 AM 290   14.8 N/A 13.44   10.5
     6 3   0 09/14/95  8 33 AM 290   14.8 N/A 16.43   16.0
     6 3   0 09/14/95  8 34 AM 290   14.8 N/A 18.93   21.5
     6 3   0 09/14/95  8 35 AM 290   14.8 N/A 22.66   32.0
     6 3   0 09/14/95  8 36 AM 290   14.8 N/A 24.54   39.0
     6 3   0 09/14/95  8 37 AM 290   14.9 N/A 26.42   46.5
     6 3   0 09/14/95  8 38 AM 290   14.9 N/A 29.63   54.0
     6 3   0 09/14/95  8 39 AM 290   14.8 N/A 32.45   60.0
     6 3   0 09/14/95  8 40 AM 290   14.8 N/A 37.04   67.0
     6 3   0 09/14/95  8 41 AM 290   14.8 N/A 36.55   66.0
     6 3   0 09/14/95  8 42 AM 290   14.8 N/A 33.66   62.0
     6 3   0 09/14/95  8 43 AM 290   14.8 N/A 31.02   57.0
     6 3   0 09/14/95  8 44 AM 290   14.8 N/A 26.98   47.0
     6 3   0 09/14/95  8 45 AM 290   14.8 N/A 24.26   38.0
     6 3   0 09/14/95  8 46 AM 290   14.8 N/A 21.90   30.5
     6 3   0 09/14/95  8 47 AM 290   14.8 N/A 19.72   24.0
     6 3   0 09/14/95  8 48 AM 290   14.7 N/A 18.06   20.0
     6 3   0 09/14/95  8 49 AM 290   14.7 N/A 14.89   14.0
     6 3   0 09/14/95  8 50 AM 290   14.7 N/A 10.76    8.0
     6 3   0 09/14/95  8 51 AM 290   14.7 N/A  8.49    6.0
     6 3   0 09/14/95  8 52 AM 290   14.7 N/A  3.33    3.5
     6 3 240 09/14/95  8 55 AM 290   14.8 N/A  8.03    3.0
     6 3 240 09/14/95  8 56 AM 290   14.9 N/A 10.69    5.0
     6 3 240 09/14/95  8 58 AM 290   15.1 N/A 12.25    6.0
     6 3 240 09/14/95  8 59 AM 290   14.9 N/A 14.99   11.0
     6 3 240 09/14/95 10 34 AM 290   14.8 N/A 13.21    8.0
     6 3 240 09/14/95 10 35 AM 290   14.8 N/A 15.96   12.0
     6 3 240 09/14/95 10 36 AM 290   14.8 N/A 18.83   18.5
     6 3 240 09/14/95 10 37 AM 290   14.7 N/A 21.18   25.2
     6 3 240 09/14/95 10 38 AM 290   14.8 N/A 24.71   34.0
     6 3 240 09/14/95 10 39 AM 290   14.8 N/A 27.47   47.0
     6 3 240 09/14/95 10 40 AM 290   14.9 N/A 31.54   59.0
     6 3 240 09/14/95 10 41 AM 290   14.9 N/A 34.32   64.0
     6 3 240 09/14/95 10 42 AM 290   15.0 N/A 39.78   72.0
     6 3 240 09/14/95 10 43 AM 290   14.9 N/A 43.48   75.0
     6 3 240 09/14/95 10 44 AM 290   14.9 N/A 41.08   72.5
     6 3 240 09/14/95 10 45 AM 290   14.7 N/A 37.15   67.5
     6 3 240 09/14/95 10 46 AM 290   14.8 N/A 32.38   60.0
     6 3 240 09/14/95 10 47 AM 290   14.8 N/A 29.81   53.5
     6 3 240 09/14/95 10 48 AM 290   14.8 N/A 25.32   37.5
     6 3 240 09/14/95 10 49 AM 290   14.7 N/A 23.30   31.0
     6 3 240 09/14/95 10 50 AM 290   14.7 N/A 21.46   26.4
     6 3 240 09/14/95 10 51 AM 290   14.8 N/A 19.56   21.5
     6 3 240 09/14/95 10 52 AM 290   14.8 N/A 15.58   12.7
     6 3 240 09/14/95 10 53 AM 290   14.7 N/A 13.78    9.5
     6 3 240 09/14/95 10 54 AM 290   14.7 N/A  9.96    5.5
     6 3 240 09/14/95 10 55 AM 290   14.6 N/A  3.54    3.0
     6 3 270 09/14/95 11 27 AM 290   15.0 N/A  9.44    4.5
     6 3 270 09/14/95 11 28 AM 290   15.0 N/A 11.60    5.5
     6 3 270 09/14/95 11 29 AM 290   14.9 N/A 15.20   10.6
     6 3 270 09/14/95 11 30 AM 290   14.9 N/A 17.54   17.0
     6 3 270 09/14/95 11 31 AM 290   14.9 N/A 20.00   23.0
     6 3 270 09/14/95 11 32 AM 290   14.9 N/A 24.26   35.5
     6 3 270 09/14/95 11 33 AM 290   15.0 N/A 27.12   48.0
     6 3 270 09/14/95 11 34 AM 290   15.0 N/A 30.53   56.5
     6 3 270 09/14/95 11 35 AM 290   15.0 N/A 37.08   68.5
     6 3 270 09/14/95 11 36 AM 290   15.1 N/A 41.83   73.0
     6 3 270 09/14/95 11 37 AM 290   15.1 N/A 38.50   70.4
     6 3 270 09/14/95 11 38 AM 290   15.1 N/A 34.80   65.0
     6 3 270 09/14/95 11 39 AM 290   15.1 N/A 32.12   59.5
     6 3 270 09/14/95 11 40 AM 290   15.0 N/A 27.28   49.5
     6 3 270 09/14/95 11 41 AM 290   14.9 N/A 26.28   42.5
     6 3 270 09/14/95 11 42 AM 290   14.9 N/A 22.24   29.0
     6 3 270 09/14/95 11 43 AM 290   14.8 N/A 20.77   26.5
     6 3 270 09/14/95 11 44 AM 290   14.8 N/A 17.74   19.0
     6 3 270 09/14/95 11 45 AM 290   14.8 N/A 13.13   10.0
     6 3 270 09/14/95 11 46 AM 290   14.8 N/A  9.16    5.5
     6 3 270 09/14/95 11 47 AM 290   14.8 N/A  7.72    4.0
     6 3 210 09/14/95 11 50 AM 290   15.0 N/A  8.27    2.5
     6 3 210 09/14/95 11 51 AM 290   14.8 N/A 10.92    6.0
     6 3 210 09/14/95 11 52 AM 290   14.7 N/A 13.96    7.5
     6 3 210 09/14/95 11 53 AM 290   14.6 N/A 16.31   12.5
     6 3 210 09/14/95 11 54 AM 290   14.6 N/A 20.68   22.5
     6 3 210 09/14/95 11 55 AM 290   14.6 N/A 23.67   30.0
     6 3 210 09/14/95 11 56 AM 290   14.6 N/A 26.02   37.0
     6 3 210 09/14/95 11 57 AM 290   14.7 N/A 28.20   44.1
     6 3 210 09/14/95 11 58 AM 290   14.8 N/A 31.55   58.5
     6 3 210 09/14/95 11 59 AM 290   14.9 N/A 34.53   63.5
     6 3 210 09/14/95 12  0 AM 290   14.9 N/A 39.07   70.0
     6 3 210 09/14/95 12  1 PM 290   14.8 N/A 44.59   75.0
     6 3 210 09/14/95 12  2 PM 290   14.8 N/A 36.23   66.5
     6 3 210 09/14/95 12  3 PM 290   14.9 N/A 31.40   57.8
     6 3 210 09/14/95 12  4 PM 290   14.7 N/A 27.91   43.5
     6 3 210 09/14/95 12  5 PM 290   14.8 N/A 26.05   36.0
     6 3 210 09/14/95 12  6 PM 290   14.8 N/A 22.26   28.0
     6 3 210 09/14/95 12  7 PM 290   14.8 N/A 20.41   22.5
     6 3 210 09/14/95 12  8 PM 290   14.8 N/A 18.72   19.5
     6 3 210 09/14/95 12  9 PM 290   14.8 N/A 15.85   13.0
     6 3 210 09/14/95 12 10 PM 290   14.7 N/A 13.96    9.0
     6 3 210 09/14/95 12 11 PM 290   15.0 N/A 11.05    6.5
     6 3 210 09/14/95 12 12 PM 290   15.0 N/A  8.73    4.5
     6 3 210 09/14/95 12 13 PM 290   15.2 N/A  4.49    2.5
     6 3  30 09/14/95 12 17 PM 290   15.0 N/A  7.51    5.5
     6 3  30 09/14/95 12 18 PM 290   15.2 N/A 11.69   10.0
     6 3  30 09/14/95 12 19 PM 290   15.1 N/A 14.21   11.5
     6 3  30 09/14/95 12 20 PM 290   14.9 N/A 18.28   20.5
     6 3  30 09/14/95 12 21 PM 290   14.8 N/A 20.50   26.3
     6 3  30 09/14/95 12 22 PM 290   14.7 N/A 22.96   33.5
     6 3  30 09/14/95 12 23 PM 290   14.7 N/A 26.36   45.5
     6 3  30 09/14/95 12 24 PM 290   14.7 N/A 29.09   53.0
     6 3  30 09/14/95 12 25 PM 290   14.8 N/A 32.45   59.5
     6 3  30 09/14/95 12 26 PM 290   14.9 N/A 35.37   64.5
     6 3  30 09/14/95 12 27 PM 290   15.0 N/A 39.42   70.7
     6 3  30 09/14/95 12 28 PM 290   15.1 N/A 42.94   74.0
     6 3  30 09/14/95 12 29 PM 290   15.0 N/A 39.94   70.5
     6 3  30 09/14/95 12 30 PM 290   14.9 N/A 33.94   63.5
     6 3  30 09/14/95 12 31 PM 290   14.9 N/A 31.07   58.4
     6 3  30 09/14/95 12 32 PM 290   14.7 N/A 27.54   49.5
     6 3  30 09/14/95 12 33 PM 290   14.8 N/A 24.35   40.4
     6 3  30 09/14/95 12 34 PM 290   14.8 N/A 21.97   31.0
     6 3  30 09/14/95 12 35 PM 290   14.8 N/A 20.09   26.5
     6 3  30 09/14/95 12 36 PM 290   14.7 N/A 16.51   18.0
     6 3  30 09/14/95 12 37 PM 290   14.7 N/A 14.01   12.5
     6 3  30 09/14/95 12 38 PM 290   14.7 N/A 12.21   10.5
     6 3  30 09/14/95 12 39 PM 290   14.7 N/A  9.06    6.5
     6 3  30 09/14/95 12 40 PM 290   14.7 N/A  5.50    4.1
     6 3  30 09/14/95  3 17 PM 293 1015.0  45  8.38   83.5
     6 3  30 09/14/95  3 18 PM 293 1015.0  32  6.09   78.5
     6 3  30 09/14/95  3 19 PM 293 1015.0  28  5.35   75.4
     6 3  30 09/14/95  3 20 PM 293 1015.0  24  4.61   68.4
     6 3  30 09/14/95  3 21 PM 293 1015.0  22  4.23   65.9
     6 3  30 09/14/95  3 22 PM 293 1015.0  20  3.85   60.5
     6 3  30 09/14/95  3 23 PM 293 1015.0  18  3.47   54.0
     6 3  30 09/14/95  3 24 PM 293 1015.0  16  3.08   47.0
     6 3  30 09/14/95  3 25 PM 293 1015.0  15  2.88   42.5
     6 3  30 09/14/95  3 26 PM 293 1015.0  14  2.69   35.8
     6 3  30 09/14/95  3 27 PM 293 1015.0  13  2.49   29.0
     6 3  30 09/14/95  3 28 PM 293 1015.0  12  2.29   23.0
     6 3  30 09/14/95  3 29 PM 293 1015.0  11  2.10   19.0
     6 3  30 09/14/95  3 30 PM 293 1015.0  10  1.90   15.5
     6 3  30 09/14/95  3 31 PM 293 1015.0   9  1.70   13.5
     6 3  30 09/14/95  3 32 PM 293 1015.0   8  1.50   11.0
     6 3  30 09/14/95  3 33 PM 293 1015.0   7  1.29   10.0
     6 3  30 09/14/95  3 34 PM 293 1015.0   6  1.09    8.5
     6 3  30 09/14/95  3 35 PM 293 1015.0   0  0.00    6.0
     6 3  30 09/14/95  3 36 PM 293 1015.0   6  1.09    6.4
     6 3  30 09/14/95  3 37 PM 293 1015.0   7  1.29    7.5
     6 3  30 09/14/95  3 38 PM 293 1015.0   8  1.50    9.5
     6 3  30 09/14/95  3 39 PM 293 1015.0   9  1.70   10.6
     6 3  30 09/14/95  3 40 PM 293 1015.0  10  1.90   14.0
     6 3  30 09/14/95  3 41 PM 293 1015.0  11  2.10   17.5
     6 3  30 09/14/95  3 42 PM 293 1015.0  12  2.29   20.0
     6 3  30 09/14/95  3 43 PM 293 1015.0  13  2.49   28.5
     6 3  30 09/14/95  3 44 PM 293 1015.0  14  2.69   33.5
     6 3  30 09/14/95  3 45 PM 293 1015.0  15  2.88   40.5
     6 3  30 09/14/95  3 46 PM 293 1015.0  16  3.08   46.0
     6 3  30 09/14/95  3 47 PM 293 1015.0  18  3.47   53.0
     6 3  30 09/14/95  3 48 PM 293 1015.0  20  3.85   61.0
     6 3  30 09/14/95  3 49 PM 293 1015.0  22  4.23   65.5
     6 3  30 09/14/95  3 50 PM 293 1015.0  24  4.61   68.5
     6 3  30 09/14/95  3 51 PM 293 1015.0  28  5.35   75.0
     6 3  30 09/14/95  3 52 PM 293 1015.0  32  6.09   77.0
     6 3  30 09/14/95  3 53 PM 293 1015.0  45  8.38   83.9
     7 3  ND 09/15/95 11 42 PM 293 1015.0  ND    ND    5.0
     7 3  ND 09/15/95 11 42 PM 293 1015.0  ND    ND    5.0
     7 3  90 09/15/95 12 38 AM 293 1015.0  12  2.29   23.5
     7 3  90 09/15/95 12 39 AM 293 1015.0  11  2.10   20.0
     7 3  90 09/15/95 12 40 AM 293 1015.0  10  1.90 B127.5
     7 3  90 09/15/95 12 41 AM 293 1015.0   9  1.70 B125.0
     7 3  90 09/15/95 12 42 AM 293 1015.0   8  1.50 B122.5
     7 3  90 09/15/95 12 43 AM 293 1015.0   7  1.29 B121.0
     7 3  90 09/15/95 12 44 AM 293 1015.0   6  1.09 B118.5
     7 3  90 09/15/95 12 45 AM 293 1015.0   0  0.00 B115.0
     7 3  90 09/15/95 12 46 AM 293 1015.0   6  1.09 B116.5
     7 3  90 09/15/95 12 47 AM 293 1015.0   7  1.29 B118.5
     7 3  90 09/15/95 12 48 AM 293 1015.0   8  1.50 B121.0
     7 3  90 09/15/95 12 49 AM 293 1015.0   9  1.70 B123.0
     7 3  90 09/15/95 12 50 AM 293 1015.0  10  1.90 B127.5
     7 3  90 09/15/95 12 51 AM 293 1015.0  11  2.10 B129.3
     7 3  90 09/15/95 12 52 AM 293 1015.0  12  2.29 B134.0
     7 3 120 09/15/95 12 53 AM 293 1015.0  12  2.29   24.7
     7 3 120 09/15/95 12 54 AM 293 1015.0  11  2.10   19.5
     7 3 120 09/15/95 12 55 AM 293 1015.0  10  1.90   16.5
     7 3 120 09/15/95 12 56 AM 293 1015.0   9  1.70   13.0
     7 3 120 09/15/95 12 57 AM 293 1015.0   8  1.50   10.5
     7 3 120 09/15/95 12 58 AM 293 1015.0   7  1.29    8.2
     7 3 120 09/15/95 12 59 AM 293 1015.0   6  1.09    7.5
     7 3 120 09/15/95  1  0 AM 293 1015.0   0  0.00    4.5
     7 3 120 09/15/95  1  1 AM 293 1015.0   6  1.09    5.5
     7 3 120 09/15/95  1  2 AM 293 1015.0   7  1.29    6.5
     7 3 120 09/15/95  1  3 AM 293 1015.0   8  1.50    9.5
     7 3 120 09/15/95  1  4 AM 293 1015.0   9  1.70   10.4
     7 3 120 09/15/95  1  5 AM 293 1015.0  10  1.90   14.5
     7 3 120 09/15/95  1  6 AM 293 1015.0  11  2.10   18.0
     7 3 120 09/15/95  1  7 AM 293 1015.0  12  2.29   22.0
     7 3 150 09/15/95  1  8 AM 293 1015.0  12  2.29   22.5
     7 3 150 09/15/95  1  9 AM 293 1015.0  11  2.10   18.2
     7 3 150 09/15/95  1 10 AM 293 1015.0  10  1.90   16.5
     7 3 150 09/15/95  1 11 AM 293 1015.0   9  1.70   13.0
     7 3 150 09/15/95  1 12 AM 293 1015.0   8  1.50   11.0
     7 3 150 09/15/95  1 13 AM 293 1015.0   7  1.29    8.5
     7 3 150 09/15/95  1 14 AM 293 1015.0   6  1.09    6.6
     7 3 150 09/15/95  1 15 AM 293 1015.0   0  0.00    4.0
     7 3 150 09/15/95  1 16 AM 293 1015.0   6  1.09    5.4
     7 3 150 09/15/95  1 17 AM 293 1015.0   7  1.29    5.6
     7 3 150 09/15/95  1 18 AM 293 1015.0   8  1.50    8.5
     7 3 150 09/15/95  1 19 AM 293 1015.0   9  1.70   12.0
     7 3 150 09/15/95  1 20 AM 293 1015.0  10  1.90   13.4
     7 3 150 09/15/95  1 21 AM 293 1015.0  11  2.10   17.0
     7 3 150 09/15/95  1 22 AM 293 1015.0  12  2.29   22.6
     7 3 300 09/15/95  1 23 AM 293 1015.0  12  2.29   24.7
     7 3 300 09/15/95  1 24 AM 293 1015.0  11  2.10   19.0
     7 3 300 09/15/95  1 25 AM 293 1015.0  10  1.90   16.5
     7 3 300 09/15/95  1 26 AM 293 1015.0   9  1.70   15.2
     7 3 300 09/15/95  1 27 AM 293 1015.0   8  1.50   11.2
     7 3 300 09/15/95  1 28 AM 293 1015.0   7  1.29    9.5
     7 3 300 09/15/95  1 29 AM 293 1015.0   6  1.09    7.0
     7 3 300 09/15/95  1 30 AM 293 1015.0   0  0.00    4.5
     7 3 300 09/15/95  1 31 AM 293 1015.0   6  1.09    6.0
     7 3 300 09/15/95  1 32 AM 293 1015.0   7  1.29    7.5
     7 3 300 09/15/95  1 33 AM 293 1015.0   8  1.50    9.2
     7 3 300 09/15/95  1 34 AM 293 1015.0   9  1.70   12.2
     7 3 300 09/15/95  1 35 AM 293 1015.0  10  1.90   14.0
     7 3 300 09/15/95  1 36 AM 293 1015.0  11  2.10   17.5
     7 3 300 09/15/95  1 37 AM 293 1015.0  12  2.29   22.5
     7 3 330 09/15/95  1 38 AM 293 1015.0  12  2.29   25.5
     7 3 330 09/15/95  1 39 AM 293 1015.0  11  2.10   19.5
     7 3 330 09/15/95  1 40 AM 293 1015.0  10  1.90   17.0
     7 3 330 09/15/95  1 41 AM 293 1015.0   9  1.70   14.0
     7 3 330 09/15/95  1 42 AM 293 1015.0   8  1.50   12.0
     7 3 330 09/15/95  1 43 AM 293 1015.0   7  1.29    9.7
     7 3 330 09/15/95  1 44 AM 293 1015.0   6  1.09    7.0
     7 3 330 09/15/95  1 45 AM 293 1015.0   0  0.00    5.0
     7 3 330 09/15/95  1 46 AM 293 1015.0   6  1.09    6.5
     7 3 330 09/15/95  1 47 AM 293 1015.0   7  1.29    7.0
     7 3 330 09/15/95  1 48 AM 293 1015.0   8  1.50    9.5
     7 3 330 09/15/95  1 49 AM 293 1015.0   9  1.70   12.2
     7 3 330 09/15/95  1 50 AM 293 1015.0  10  1.90   16.5
     7 3 330 09/15/95  1 51 AM 293 1015.0  11  2.10   19.2
     7 3 330 09/15/95  1 52 AM 293 1015.0  12  2.29   25.5
     7 3 330 09/15/95  1 52 AM 293 1015.0  12  2.29   25.5
     7 3 330 09/15/95  1 53 AM 293 1015.0   6  1.09   19.0
     7 2  90 09/15/95  2 26 AM 293 1015.0  12  2.29   24.0
     7 2  90 09/15/95  2 27 AM 293 1015.0  11  2.10 B129.0
     7 2  90 09/15/95  2 28 AM 293 1015.0  10  1.90 B126.7
     7 2  90 09/15/95  2 29 AM 293 1015.0   9  1.70 B124.7
     7 2  90 09/15/95  2 30 AM 293 1015.0   8  1.50 B120.5
     7 2  90 09/15/95  2 31 AM 293 1015.0   7  1.29 B119.0
     7 2  90 09/15/95  2 32 AM 293 1015.0   6  1.09 B116.0
     7 2  90 09/15/95  2 33 AM 293 1015.0   0  0.00 B113.0
     7 2  90 09/15/95  2 34 AM 293 1015.0   6  1.09 B116.0
     7 2  90 09/15/95  2 35 AM 293 1015.0   7  1.29 B118.0
     7 2  90 09/15/95  2 36 AM 293 1015.0   8  1.50 B121.5
     7 2  90 09/15/95  2 37 AM 293 1015.0   9  1.70 B123.0
     7 2  90 09/15/95  2 38 AM 293 1015.0  10  1.90 B126.0
     7 2  90 09/15/95  2 39 AM 293 1015.0  11  2.10 B130.0
     7 2  90 09/15/95  2 40 AM 293 1015.0  12  2.29 B134.5
     7 2 120 09/15/95  2 41 AM 293 1015.0  12  2.29   24.5
     7 2 120 09/15/95  2 42 AM 293 1015.0  11  2.10   17.5
     7 2 120 09/15/95  2 43 AM 293 1015.0  10  1.90   14.5
     7 2 120 09/15/95  2 44 AM 293 1015.0   9  1.70   12.0
     7 2 120 09/15/95  2 45 AM 293 1015.0   8  1.50   10.5
     7 2 120 09/15/95  2 46 AM 293 1015.0   7  1.29    7.5
     7 2 120 09/15/95  2 47 AM 293 1015.0   6  1.09    6.0
     7 2 120 09/15/95  2 48 AM 293 1015.0   0  0.00    2.5
     7 2 120 09/15/95  2 49 AM 293 1015.0   6  1.09    4.5
     7 2 120 09/15/95  2 50 AM 293 1015.0   7  1.29    6.5
     7 2 120 09/15/95  2 51 AM 293 1015.0   8  1.50    9.0
     7 2 120 09/15/95  2 52 AM 293 1015.0   9  1.70   11.5
     7 2 120 09/15/95  2 53 AM 293 1015.0  10  1.90   12.5
     7 2 120 09/15/95  2 54 AM 293 1015.0  11  2.10   17.0
     7 2 120 09/15/95  2 55 AM 293 1015.0  12  2.29   24.5
     7 2 150 09/15/95  2 56 AM 293 1015.0  12  2.29   24.0
     7 2 150 09/15/95  2 57 AM 293 1015.0  11  2.10   17.5
     7 2 150 09/15/95  2 58 AM 293 1015.0  10  1.90   14.0
     7 2 150 09/15/95  3  0 AM 293 1015.0   9  1.70   11.6
     7 2 150 09/15/95  3  1 AM 293 1015.0   8  1.50    9.0
     7 2 150 09/15/95  3  2 AM 293 1015.0   7  1.29    7.5
     7 2 150 09/15/95  3  3 AM 293 1015.0   6  1.09    5.5
     7 2 150 09/15/95  3  4 AM 293 1015.0   0  0.00    2.5
     7 2 150 09/15/95  3  5 AM 293 1015.0   6  1.09    4.5
     7 2 150 09/15/95  3  6 AM 293 1015.0   7  1.29    7.0
     7 2 150 09/15/95  3  7 AM 293 1015.0   8  1.50    7.5
     7 2 150 09/15/95  3  8 AM 293 1015.0   9  1.70   12.5
     7 2 150 09/15/95  3  9 AM 293 1015.0  10  1.90   14.5
     7 2 150 09/15/95  3 10 AM 293 1015.0  11  2.10   18.5
     7 2 150 09/15/95  3 11 AM 293 1015.0  12  2.29   23.5
     7 2 300 09/15/95  3 12 AM 293 1015.0  12  2.29   27.5
     7 2 300 09/15/95  3 13 AM 293 1015.0  11  2.10   21.5
     7 2 300 09/15/95  3 14 AM 293 1015.0  10  1.90   17.0
     7 2 300 09/15/95  3 15 AM 293 1015.0   9  1.70   13.5
     7 2 300 09/15/95  3 16 AM 293 1015.0   8  1.50   13.5
     7 2 300 09/15/95  3 17 AM 293 1015.0   7  1.29    9.0
     7 2 300 09/15/95  3 18 AM 293 1015.0   6  1.09    6.8
     7 2 300 09/15/95  3 19 AM 293 1015.0   0  0.00    6.0
     7 2 300 09/15/95  3 20 AM 293 1015.0   6  1.09    7.0
     7 2 300 09/15/95  3 21 AM 293 1015.0   7  1.29    8.5
     7 2 300 09/15/95  3 22 AM 293 1015.0   8  1.50   11.4
     7 2 300 09/15/95  3 23 AM 293 1015.0   9  1.70   13.5
     7 2 300 09/15/95  3 24 AM 293 1015.0  10  1.90   16.5
     7 2 300 09/15/95  3 25 AM 293 1015.0  11  2.10   21.0
     7 2 300 09/15/95  3 26 AM 293 1015.0  12  2.29   27.0
     7 2 330 09/15/95  3 27 AM 293 1015.0  15  2.88   46.0
     7 2 330 09/15/95  3 28 AM 293 1015.0  12  2.29   29.0
     7 2 330 09/15/95  3 29 AM 293 1015.0  11  2.10   21.5
     7 2 330 09/15/95  3 30 AM 293 1015.0  10  1.90   17.5
     7 2 330 09/15/95  3 31 AM 293 1015.0   9  1.70    9.5
     7 2 330 09/15/95  3 32 AM 293 1015.0   8  1.50   12.0
     7 2 330 09/15/95  3 33 AM 293 1015.0   7  1.29   10.0
     7 2 330 09/15/95  3 34 AM 293 1015.0   6  1.09    8.5
     7 2 330 09/15/95  3 35 AM 293 1015.0   0  0.00    5.0
     7 2 330 09/15/95  3 36 AM 293 1015.0   6  1.09    6.5
     7 2 330 09/15/95  3 37 AM 293 1015.0   7  1.29    8.0
     7 2 330 09/15/95  3 38 AM 293 1015.0   8  1.50   12.2
     7 2 330 09/15/95  3 39 AM 293 1015.0   9  1.70   15.4
     7 2 330 09/15/95  3 40 AM 293 1015.0  10  1.90   17.0
     7 2 330 09/15/95  3 41 AM 293 1015.0  11  2.10   21.2
     7 2 330 09/15/95  3 42 AM 293 1015.0  12  2.29   28.5
     7 1  90 09/15/95  4  8 AM 293 1015.0  12  2.29 B137.4
     7 1  90 09/15/95  4  9 AM 293 1015.0  11  2.10 B131.5
     7 1  90 09/15/95  4 10 AM 293 1015.0  10  1.90 B128.0
     7 1  90 09/15/95  4 11 AM 293 1015.0   9  1.70 B125.2
     7 1  90 09/15/95  4 12 AM 293 1015.0   8  1.50 B124.0
     7 1  90 09/15/95  4 13 AM 293 1015.0   7  1.29 B121.0
     7 1  90 09/15/95  4 14 AM 293 1015.0   6  1.09 B119.0
     7 1  90 09/15/95  4 15 AM 293 1015.0   0  0.00 B115.0
     7 1  90 09/15/95  4 16 AM 293 1015.0   6  1.09 B115.5
     7 1  90 09/15/95  4 17 AM 293 1015.0   7  1.29 B118.0
     7 1  90 09/15/95  4 18 AM 293 1015.0   8  1.50 B122.0
     7 1  90 09/15/95  4 19 AM 293 1015.0   9  1.70 B125.0
     7 1  90 09/15/95  4 20 AM 293 1015.0  10  1.90 B128.2
     7 1  90 09/15/95  4 21 AM 293 1015.0  11  2.10 B131.5
     7 1  90 09/15/95  4 22 AM 293 1015.0  12  2.29 B137.0
     7 1 120 09/15/95  4 23 AM 293 1015.0  12  2.29   27.0
     7 1 120 09/15/95  4 24 AM 293 1015.0  11  2.10   24.0
     7 1 120 09/15/95  4 25 AM 293 1015.0  10  1.90   18.5
     7 1 120 09/15/95  4 26 AM 293 1015.0   9  1.70   15.6
     7 1 120 09/15/95  4 27 AM 293 1015.0   8  1.50   13.0
     7 1 120 09/15/95  4 28 AM 293 1015.0   7  1.29   10.3
     7 1 120 09/15/95  4 29 AM 293 1015.0   6  1.09    8.5
     7 1 120 09/15/95  4 30 AM 293 1015.0   0  0.00    4.5
     7 1 120 09/15/95  4 31 AM 293 1015.0   6  1.09    5.0
     7 1 120 09/15/95  4 32 AM 293 1015.0   7  1.29    7.0
     7 1 120 09/15/95  4 33 AM 293 1015.0   8  1.50    9.5
     7 1 120 09/15/95  4 34 AM 293 1015.0   9  1.70   12.4
     7 1 120 09/15/95  4 35 AM 293 1015.0  10  1.90   14.5
     7 1 120 09/15/95  4 36 AM 293 1015.0  11  2.10   20.0
     7 1 120 09/15/95  4 37 AM 293 1015.0  12  2.29   25.0
     7 1 150 09/15/95  4 38 AM 293 1015.0  12  2.29   29.5
     7 1 150 09/15/95  4 39 AM 293 1015.0  11  2.10   24.5
     7 1 150 09/15/95  4 40 AM 293 1015.0  10  1.90   19.5
     7 1 150 09/15/95  4 41 AM 293 1015.0   9  1.70   17.0
     7 1 150 09/15/95  4 42 AM 293 1015.0   8  1.50   14.4
     8 1  ND 09/15/95  6 36 AM 293 1015.0  ND    ND    3.8
     8 1  30 09/15/95  7 30 AM 290   14.7 N/A 11.92    9.5
     8 1  30 09/15/95  7 31 AM 290   14.7 N/A 13.82   12.0
     8 1  30 09/15/95  7 32 AM 290   14.7 N/A 16.09   17.2
     8 1  30 09/15/95  7 33 AM 290   14.7 N/A 18.97   24.2
     8 1  30 09/15/95  7 34 AM 290   14.8 N/A 21.00   32.2
     8 1  30 09/15/95  7 35 AM 290   14.8 N/A 23.83   39.3
     8 1  30 09/15/95  7 36 AM 290   14.7 N/A 26.09   49.0
     8 1  30 09/15/95  7 37 AM 290   14.7 N/A 28.27   55.0
     8 1  30 09/15/95  7 38 AM 290   14.8 N/A 31.62   62.5
     8 1  30 09/15/95  7 39 AM 290   14.8 N/A 33.57   65.8
     8 1  30 09/15/95  7 40 AM 290   14.9 N/A 40.35   74.0
     8 1  30 09/15/95  7 41 AM 290   14.9 N/A 43.64   76.4
     8 1  30 09/15/95  7 42 AM 290   14.9 N/A 39.08   73.5
     8 1  30 09/15/95  7 43 AM 290   14.8 N/A 36.35   69.4
     8 1  30 09/15/95  7 44 AM 290   14.9 N/A 33.35   66.5
     8 1  30 09/15/95  7 45 AM 290   15.0 N/A 30.40   62.2
     8 1  30 09/15/95  7 46 AM 290   15.0 N/A 28.81   59.0
     8 1  30 09/15/95  7 47 AM 290   14.9 N/A 21.12   35.4
     8 1  30 09/15/95  7 48 AM 290   14.8 N/A 18.66   28.0
     8 1  30 09/15/95  7 49 AM 290   14.8 N/A 17.35   25.3
     8 1  30 09/15/95  7 50 AM 290   14.8 N/A 15.40   22.3
     8 1  30 09/15/95  7 51 AM 290   14.8 N/A 12.08   14.3
     8 1  30 09/15/95  7 52 AM 290   14.8 N/A  8.74   12.3
     8 1  30 09/15/95  7 53 AM 290   14.8 N/A  2.31    9.7
     8 1 210 09/15/95  7 55 AM 290   14.7 N/A  8.90    3.5
     8 1 210 09/15/95  7 56 AM 290   14.7 N/A 11.98    6.0
     8 1 210 09/15/95  7 57 AM 290   14.7 N/A 15.31   11.7
     8 1 210 09/15/95  7 58 AM 290   14.7 N/A 18.71   21.7
     8 1 210 09/15/95  7 59 AM 290   14.7 N/A 20.88   27.0
     8 1 210 09/15/95  8  0 AM 290   14.8 N/A 24.61   37.1
     8 1 210 09/15/95  8  1 AM 290   15.0 N/A 27.08   50.0
     8 1 210 09/15/95  8  2 AM 290   15.0 N/A 29.37   55.9
     8 1 210 09/15/95  8  3 AM 290   15.0 N/A 34.00   64.5
     8 1 210 09/15/95  8  4 AM 290   15.1 N/A 38.10   69.0
     8 1 210 09/15/95  8  5 AM 290   15.1 N/A 45.82   76.5
     8 1 210 09/15/95  8  6 AM 290   15.1 N/A 41.88   74.5
     8 1 210 09/15/95  8  7 AM 290   15.0 N/A 38.05   70.5
     8 1 210 09/15/95  8  8 AM 290   14.8 N/A 33.62   65.0
     8 1 210 09/15/95  8  9 AM 290   14.8 N/A 29.61   57.5
     8 1 210 09/15/95  8 10 AM 290   14.8 N/A 26.97   51.7
     8 1 210 09/15/95  8 11 AM 290   14.8 N/A 24.55   39.0
     8 1 210 09/15/95  8 12 AM 290   14.7 N/A 21.76   30.7
     8 1 210 09/15/95  8 13 AM 290   14.8 N/A 20.02   28.1
     8 1 210 09/15/95  8 14 AM 290   14.9 N/A 17.89   23.2
     8 1 210 09/15/95  8 15 AM 290   15.0 N/A 15.92   18.5
     8 1 210 09/15/95  8 16 AM 290   15.0 N/A 12.54   12.5
     8 1 210 09/15/95  8 17 AM 290   15.0 N/A  9.89    8.5
     8 1 210 09/15/95  8 18 AM 290   15.0 N/A  5.15    4.5
     8 2  30 09/15/95  9 36 AM 290   14.8 N/A  8.03    4.5
     8 2  30 09/15/95  9 37 AM 290   14.6 N/A  9.97    6.5
     8 2  30 09/15/95  9 38 AM 290   14.5 N/A 12.54    9.2
     8 2  30 09/15/95  9 39 AM 290   14.5 N/A 15.41   13.8
     8 2  30 09/15/95  9 40 AM 290   14.5 N/A 16.78   17.0
     8 2  30 09/15/95  9 41 AM 290   14.7 N/A 19.23   23.0
     8 2  30 09/15/95  9 42 AM 290   14.7 N/A 21.27   28.0
     8 2  30 09/15/95  9 43 AM 290   14.8 N/A 24.28   39.4
     8 2  30 09/15/95  9 44 AM 290   14.9 N/A 26.53   48.5
     8 2  30 09/15/95  9 45 AM 290   14.8 N/A 29.91   58.0
     8 2  30 09/15/95  9 46 AM 290   15.0 N/A 32.47   62.0
     8 2  30 09/15/95  9 47 AM 290   14.9 N/A 36.84   69.5
     8 2  30 09/15/95  9 48 AM 290   14.9 N/A 39.93   72.0
     8 2  30 09/15/95  9 49 AM 290   15.0 N/A 45.73   77.0
     8 2  30 09/15/95  9 50 AM 290   15.0 N/A 38.73   71.3
     8 2  30 09/15/95  9 51 AM 290   15.0 N/A 34.73   66.4
     8 2  30 09/15/95  9 52 AM 290   14.9 N/A 31.73   61.7
     8 2  30 09/15/95  9 53 AM 290   14.8 N/A 28.69   55.0
     8 2  30 09/15/95  9 54 AM 290   14.8 N/A 26.21   47.5
     8 2  30 09/15/95  9 55 AM 290   14.7 N/A 23.64   38.5
     8 2  30 09/15/95  9 56 AM 290   14.7 N/A 22.07   32.0
     8 2  30 09/15/95  9 57 AM 290   14.7 N/A 19.76   27.3
     8 2  30 09/15/95  9 58 AM 290   14.7 N/A 17.15   19.3
     8 2  30 09/15/95  9 59 AM 290   14.7 N/A 14.26   13.5
     8 2  30 09/15/95 10  0 AM 290   14.7 N/A 10.94   10.0
     8 2  30 09/15/95 10  1 AM 290   14.6 N/A  7.41    7.0
     8 2 210 09/15/95 10  3 AM 290   15.0 N/A 10.50    5.0
     8 2 210 09/15/95 10  4 AM 290   15.0 N/A 12.87    7.0
     8 2 210 09/15/95 10  5 AM 290   15.0 N/A 15.25   11.5
     8 2 210 09/15/95 10  6 AM 290   15.0 N/A 17.53   15.5
     8 2 210 09/15/95 10  7 AM 290   15.0 N/A 20.85   24.5
     8 2 210 09/15/95 10  8 AM 290   14.9 N/A 24.13   32.5
     8 2 210 09/15/95 10  9 AM 290   14.8 N/A 26.41   42.0
     8 2 210 09/15/95 10 10 AM 290   14.8 N/A 29.89   57.0
     8 2 210 09/15/95 10 11 AM 290   14.8 N/A 33.40   63.5
     8 2 210 09/15/95 10 12 AM 290   14.9 N/A 39.03   71.0
     8 2 210 09/15/95 10 13 AM 290   15.0 N/A 45.84   77.0
     8 2 210 09/15/95 10 14 AM 290   14.9 N/A 42.16   75.0
     8 2 210 09/15/95 10 15 AM 290   14.9 N/A 37.14   69.7
     8 2 210 09/15/95 10 16 AM 290   14.8 N/A 33.41   64.5
     8 2 210 09/15/95 10 17 AM 290   14.9 N/A 29.48   56.6
     8 2 210 09/15/95 10 18 AM 290   15.0 N/A 25.79   44.5
     8 2 210 09/15/95 10 19 AM 290   15.0 N/A 23.40   36.0
     8 2 210 09/15/95 10 20 AM 290   15.0 N/A 21.47   30.5
     8 2 210 09/15/95 10 21 AM 290   15.0 N/A 18.46   23.0
     8 2 210 09/15/95 10 22 AM 290   14.9 N/A 16.35   17.3
     8 2 210 09/15/95 10 23 AM 290   14.9 N/A 13.29   11.5
     8 2 210 09/15/95 10 24 AM 290   15.0 N/A  9.69    7.5
     8 2 210 09/15/95 10 25 AM 290   14.9 N/A  5.97    4.3
     8 2  30 09/15/95  1  4 PM 293 1015.0  45  8.38   83.7
     8 2  30 09/15/95  1  5 PM 293 1015.0  32  6.09   80.0
     8 2  30 09/15/95  1  6 PM 293 1015.0  28  5.35   76.0
     8 2  30 09/15/95  1  7 PM 293 1015.0  24  4.61   71.3
     8 2  30 09/15/95  1  8 PM 293 1015.0  22  4.23   66.5
     8 2  30 09/15/95  1  9 PM 293 1015.0  20  3.85   62.0
     8 2  30 09/15/95  1 10 PM 293 1015.0  18  3.47   56.5
     8 2  30 09/15/95  1 11 PM 293 1015.0  16  3.08   48.5
     8 2  30 09/15/95  1 12 PM 293 1015.0  15  2.88   43.0
     8 2  30 09/15/95  1 13 PM 293 1015.0  14  2.69   37.3
     8 2  30 09/15/95  1 14 PM 293 1015.0  13  2.49   30.7
     8 2  30 09/15/95  1 15 PM 293 1015.0  12  2.29   25.4
     8 2  30 09/15/95  1 16 PM 293 1015.0  11  2.10   20.0
     8 2  30 09/15/95  1 17 PM 293 1015.0  10  1.90   16.0
     8 2  30 09/15/95  1 18 PM 293 1015.0   9  1.70   12.5
     8 2  30 09/15/95  1 19 PM 293 1015.0   8  1.50   11.4
     8 2  30 09/15/95  1 20 PM 293 1015.0   7  1.29    9.0
     8 2  30 09/15/95  1 21 PM 293 1015.0   6  1.09    7.2
     8 2  30 09/15/95  1 22 PM 293 1015.0   0  0.00    4.0
     8 2  30 09/15/95  1 23 PM 293 1015.0   6  1.09    5.0
     8 2  30 09/15/95  1 24 PM 293 1015.0   7  1.29    8.0
     8 2  30 09/15/95  1 25 PM 293 1015.0   8  1.50    9.7
     8 2  30 09/15/95  1 26 PM 293 1015.0   9  1.70   13.0
     8 2  30 09/15/95  1 27 PM 293 1015.0  10  1.90   15.5
     8 2  30 09/15/95  1 28 PM 293 1015.0  11  2.10   18.7
     8 2  30 09/15/95  1 29 PM 293 1015.0  12  2.29   26.0
     8 2  30 09/15/95  1 30 PM 293 1015.0  13  2.49   30.0
     8 2  30 09/15/95  1 31 PM 293 1015.0  14  2.69   37.5
     8 2  30 09/15/95  1 32 PM 293 1015.0  15  2.88   43.5
     8 2  30 09/15/95  1 33 PM 293 1015.0  16  3.08   48.5
     8 2  30 09/15/95  1 34 PM 293 1015.0  18  3.47   56.0
     8 2  30 09/15/95  1 35 PM 293 1015.0  20  3.85   61.5
     8 2  30 09/15/95  1 36 PM 293 1015.0  22  4.23   66.0
     8 2  30 09/15/95  1 37 PM 293 1015.0  24  4.61   69.5
     8 2  30 09/15/95  1 38 PM 293 1015.0  28  5.35   75.5
     8 2  30 09/15/95  1 39 PM 293 1015.0  32  6.09   79.5
     8 2  30 09/15/95  1 40 PM 293 1015.0  45  8.38   83.5
     8 1  30 09/15/95  2  0 PM 293 1015.0  45  8.38   85.2
     8 1  30 09/15/95  2  1 PM 293 1015.0  32  6.09   80.4
     8 1  30 09/15/95  2  2 PM 293 1015.0  28  5.35   77.5
     8 1  30 09/15/95  2  3 PM 293 1015.0  24  4.61   72.5
     8 1  30 09/15/95  2  4 PM 293 1015.0  22  4.23   68.5
     8 1  30 09/15/95  2  5 PM 293 1015.0  20  3.85   65.0
     8 1  30 09/15/95  2  6 PM 293 1015.0  18  3.47   59.0
     8 1  30 09/15/95  2  7 PM 293 1015.0  16  3.08   51.2
     8 1  30 09/15/95  2  8 PM 293 1015.0  15  2.88   47.5
     8 1  30 09/15/95  2  9 PM 293 1015.0  14  2.69   39.4
     8 1  30 09/15/95  2 10 PM 293 1015.0  13  2.49   32.0
     8 1  30 09/15/95  2 11 PM 293 1015.0  12  2.29   27.5
     8 1  30 09/15/95  2 12 PM 293 1015.0  11  2.10   22.0
     8 1  30 09/15/95  2 13 PM 293 1015.0  10  1.90   19.0
     8 1  30 09/15/95  2 14 PM 293 1015.0   9  1.70   17.5
     8 1  30 09/15/95  2 15 PM 293 1015.0   8  1.50   14.0
     8 1  30 09/15/95  2 16 PM 293 1015.0   7  1.29   11.3
     8 1  30 09/15/95  2 17 PM 293 1015.0   6  1.09   10.0
     8 1  30 09/15/95  2 18 PM 293 1015.0   0  0.00    5.0
     8 1  30 09/15/95  2 19 PM 293 1015.0   6  1.09    5.5
     8 1  30 09/15/95  2 20 PM 293 1015.0   7  1.29    8.0
     8 1  30 09/15/95  2 21 PM 293 1015.0   8  1.50   10.5
     8 1  30 09/15/95  2 22 PM 293 1015.0   9  1.70   13.5
     8 1  30 09/15/95  2 23 PM 293 1015.0  10  1.90   16.0
     8 1  30 09/15/95  2 24 PM 293 1015.0  11  2.10   20.0
     8 1  30 09/15/95  2 25 PM 293 1015.0  12  2.29   27.0
     8 1  30 09/15/95  2 26 PM 293 1015.0  13  2.49   33.1
     8 1  30 09/15/95  2 27 PM 293 1015.0  14  2.69   41.0
     8 1  30 09/15/95  2 28 PM 293 1015.0  15  2.88   46.2
     8 1  30 09/15/95  2 29 PM 293 1015.0  16  3.08   51.0
     8 1  30 09/15/95  2 30 PM 293 1015.0  18  3.47   59.6
     8 1  30 09/15/95  2 31 PM 293 1015.0  20  3.85   63.5
     8 1  30 09/15/95  2 32 PM 293 1015.0  22  4.23   68.0
     8 1  30 09/15/95  2 33 PM 293 1015.0  24  4.61   72.0
     8 1  30 09/15/95  2 34 PM 293 1015.0  28  5.35   77.0
     8 1  30 09/15/95  2 35 PM 293 1015.0  32  6.09   80.5
     8 1  30 09/15/95  2 36 PM 293 1015.0  45  8.38   85.0
     8 1 300 09/15/95  2 39 PM 293 1015.0  12  2.29   25.4
     8 1 300 09/15/95  2 40 PM 293 1015.0  11  2.10   20.2
     8 1 300 09/15/95  2 41 PM 293 1015.0  10  1.90   17.3
     8 1 300 09/15/95  2 42 PM 293 1015.0   9  1.70   14.2
     8 1 300 09/15/95  2 43 PM 293 1015.0   8  1.50   11.5
     8 1 300 09/15/95  2 44 PM 293 1015.0   7  1.29    9.5
     8 1 300 09/15/95  2 45 PM 293 1015.0   6  1.09    7.6
     8 1 300 09/15/95  2 46 PM 293 1015.0   0  0.00    3.6
     8 1 300 09/15/95  2 47 PM 293 1015.0   6  1.09    4.0
     8 1 300 09/15/95  2 48 PM 293 1015.0   7  1.29    6.0
     8 1 300 09/15/95  2 49 PM 293 1015.0   8  1.50    8.5
     8 1 300 09/15/95  2 50 PM 293 1015.0   9  1.70   12.5
     8 1 300 09/15/95  2 51 PM 293 1015.0  10  1.90   15.5
     8 1 300 09/15/95  2 52 PM 293 1015.0  11  2.10   20.5
     8 1 300 09/15/95  2 53 PM 293 1015.0  12  2.29   24.3
     8 1 330 09/15/95  2 54 PM 293 1015.0  12  2.29   28.0
     8 1 330 09/15/95  2 55 PM 293 1015.0  11  2.10   20.0
     8 1 330 09/15/95  2 56 PM 293 1015.0  10  1.90   18.5
     8 1 330 09/15/95  2 57 PM 293 1015.0   9  1.70   15.5
     8 1 330 09/15/95  2 58 PM 293 1015.0   8  1.50   13.0
     8 1 330 09/15/95  2 59 PM 293 1015.0   7  1.29    9.5
     8 1 330 09/15/95  3  0 PM 293 1015.0   6  1.09    8.0
     8 1 330 09/15/95  3  1 PM 293 1015.0   0  0.00    4.0
     8 1 330 09/15/95  3  2 PM 293 1015.0   6  1.09    5.5
     8 1 330 09/15/95  3  3 PM 293 1015.0   7  1.29    8.0
     8 1 330 09/15/95  3  4 PM 293 1015.0   8  1.50   12.0
     8 1 330 09/15/95  3  5 PM 293 1015.0   9  1.70   13.5
     8 1 330 09/15/95  3  6 PM 293 1015.0  10  1.90   16.0
     8 1 330 09/15/95  3  7 PM 293 1015.0  11  2.10   20.0
     8 1 330 09/15/95  3  8 PM 293 1015.0  12  2.29   27.0
 
  Appendix II - IMP Windsock Images
  =================================
    IMP SEQUENCE S0050
                   PRODUCT_ID                 SCLK          LST
     IMP_EDR-1249063386-REGULAR-0050190005 1249063386 SOL 27 10:47:03
     IMP_EDR-1249063441-REGULAR-0050190007 1249063441 SOL 27 10:47:57
     IMP_EDR-1249063496-REGULAR-0050190009 1249063496 SOL 27 10:48:50
     IMP_EDR-1249063551-REGULAR-0050190011 1249063551 SOL 27 10:49:44
     IMP_EDR-1249063606-REGULAR-0050190013 1249063606 SOL 27 10:50:38
     IMP_EDR-1249063661-REGULAR-0050190015 1249063661 SOL 27 10:51:31
     IMP_EDR-1249063716-REGULAR-0050190017 1249063716 SOL 27 10:52:25
     IMP_EDR-1249063771-REGULAR-0050190019 1249063771 SOL 27 10:53:18
 
    IMP SEQUENCE S0053
                   PRODUCT_ID                 SCLK          LST
     IMP_EDR-1249062972-REGULAR-0053100002 1249062972 SOL 27 10:40:20
 
    IMP SEQUENCE S0055
                   PRODUCT_ID                 SCLK          LST
     IMP_EDR-1248983843-REGULAR-0055490008 1248983843 SOL 26 13:16:40
     IMP_EDR-1248983843-REGULAR-0055490009 1248983843 SOL 26 13:16:40
 
    IMP SEQUENCE S0068
                   PRODUCT_ID                 SCLK          LST
     IMP_EDR-1246853290-REGULAR-0068060003 1246853290 SOL 2 13:13:39
     IMP_EDR-1246853300-REGULAR-0068060005 1246853300 SOL 2 13:13:49
     IMP_EDR-1246853309-REGULAR-0068060007 1246853309 SOL 2 13:13:57
     IMP_EDR-1246853319-REGULAR-0068060009 1246853319 SOL 2 13:14:07
     IMP_EDR-1246853329-REGULAR-0068060011 1246853329 SOL 2 13:14:17
     IMP_EDR-1246853340-REGULAR-0068060013 1246853340 SOL 2 13:14:28
     IMP_EDR-1246853351-REGULAR-0068060015 1246853351 SOL 2 13:14:38
     IMP_EDR-1246853361-REGULAR-0068060017 1246853361 SOL 2 13:14:48
     IMP_EDR-1246853371-REGULAR-0068060019 1246853371 SOL 2 13:14:58
     IMP_EDR-1246853381-REGULAR-0068060021 1246853381 SOL 2 13:15:08
     IMP_EDR-1246853400-REGULAR-0068060023 1246853400 SOL 2 13:15:26
     IMP_EDR-1246853410-REGULAR-0068060025 1246853410 SOL 2 13:15:36
     IMP_EDR-1246853421-REGULAR-0068060027 1246853421 SOL 2 13:15:46
     IMP_EDR-1246853432-REGULAR-0068060029 1246853432 SOL 2 13:15:57
     IMP_EDR-1246853442-REGULAR-0068060031 1246853442 SOL 2 13:16:07
     IMP_EDR-1246853452-REGULAR-0068060033 1246853452 SOL 2 13:16:17
     IMP_EDR-1246853462-REGULAR-0068060035 1246853462 SOL 2 13:16:26
     IMP_EDR-1246853472-REGULAR-0068060037 1246853472 SOL 2 13:16:36
     IMP_EDR-1246853482-REGULAR-0068060039 1246853482 SOL 2 13:16:46
     IMP_EDR-1246853492-REGULAR-0068060041 1246853492 SOL 2 13:16:56
 
    IMP SEQUENCE S0166
                   PRODUCT_ID                 SCLK          LST
     IMP_EDR-1247462013-REGULAR-0166020051 1247462013 SOL 9 09:48:43
     IMP_EDR-1247462029-REGULAR-0166020121 1247462029 SOL 9 09:48:58
     IMP_EDR-1247462043-REGULAR-0166020191 1247462043 SOL 9 09:49:12
     IMP_EDR-1247462064-REGULAR-0166020261 1247462064 SOL 9 09:49:32
     IMP_EDR-1247462081-REGULAR-0166020331 1247462081 SOL 9 09:49:49
     IMP_EDR-1247462100-REGULAR-0166020401 1247462100 SOL 9 09:50:08
     IMP_EDR-1247462122-REGULAR-0166020471 1247462122 SOL 9 09:50:29
     IMP_EDR-1247462138-REGULAR-0166020541 1247462138 SOL 9 09:50:45
     IMP_EDR-1247462157-REGULAR-0166020611 1247462157 SOL 9 09:51:03
     IMP_EDR-1247462179-REGULAR-0166020681 1247462179 SOL 9 09:51:24
     IMP_EDR-1247462195-REGULAR-0166020751 1247462195 SOL 9 09:51:40
     IMP_EDR-1247462210-REGULAR-0166020821 1247462210 SOL 9 09:51:55
     IMP_EDR-1247462234-REGULAR-0166020891 1247462234 SOL 9 09:52:18
     IMP_EDR-1247462251-REGULAR-0166020961 1247462251 SOL 9 09:52:34
     IMP_EDR-1247462269-REGULAR-0166021031 1247462269 SOL 9 09:52:52
 
    IMP SEQUENCE S0173
                   PRODUCT_ID                 SCLK          LST
     IMP_EDR-1246935023-REGULAR-0173020003 1246935023 SOL 3 11:19:34
     IMP_EDR-1246935029-REGULAR-0173020005 1246935029 SOL 3 11:19:40
     IMP_EDR-1246935036-REGULAR-0173020007 1246935036 SOL 3 11:19:47
     IMP_EDR-1246935052-REGULAR-0173020009 1246935052 SOL 3 11:20:02
     IMP_EDR-1246935059-REGULAR-0173020011 1246935059 SOL 3 11:20:09
     IMP_EDR-1246935066-REGULAR-0173020013 1246935066 SOL 3 11:20:16
     IMP_EDR-1246935077-REGULAR-0173020015 1246935077 SOL 3 11:20:27
     IMP_EDR-1246935084-REGULAR-0173020017 1246935084 SOL 3 11:20:34
     IMP_EDR-1246935091-REGULAR-0173020019 1246935091 SOL 3 11:20:40
     IMP_EDR-1246935107-REGULAR-0173020021 1246935107 SOL 3 11:20:56
     IMP_EDR-1246935113-REGULAR-0173020023 1246935113 SOL 3 11:21:02
     IMP_EDR-1246935120-REGULAR-0173020025 1246935120 SOL 3 11:21:09
     IMP_EDR-1246938495-REGULAR-0173020003 1246938495 SOL 3 12:15:54
     IMP_EDR-1246938501-REGULAR-0173020005 1246938501 SOL 3 12:16:00
     IMP_EDR-1246938508-REGULAR-0173020007 1246938508 SOL 3 12:16:06
     IMP_EDR-1246938525-REGULAR-0173020009 1246938525 SOL 3 12:16:23
     IMP_EDR-1246938532-REGULAR-0173020011 1246938532 SOL 3 12:16:30
     IMP_EDR-1246938539-REGULAR-0173020013 1246938539 SOL 3 12:16:37
     IMP_EDR-1246938551-REGULAR-0173020015 1246938551 SOL 3 12:16:48
     IMP_EDR-1246938558-REGULAR-0173020017 1246938558 SOL 3 12:16:55
     IMP_EDR-1246938566-REGULAR-0173020019 1246938566 SOL 3 12:17:03
     IMP_EDR-1246938582-REGULAR-0173020021 1246938582 SOL 3 12:17:18
     IMP_EDR-1246938588-REGULAR-0173020023 1246938588 SOL 3 12:17:24
     IMP_EDR-1246938595-REGULAR-0173020025 1246938595 SOL 3 12:17:31
     IMP_EDR-1247825263-REGULAR-0173050003 1247825263 SOL 13 12:01:34
     IMP_EDR-1247825270-REGULAR-0173050005 1247825270 SOL 13 12:01:41
     IMP_EDR-1247825277-REGULAR-0173050007 1247825277 SOL 13 12:01:48
     IMP_EDR-1247825292-REGULAR-0173050009 1247825292 SOL 13 12:02:02
     IMP_EDR-1247825299-REGULAR-0173050011 1247825299 SOL 13 12:02:09
     IMP_EDR-1247825305-REGULAR-0173050013 1247825305 SOL 13 12:02:15
     IMP_EDR-1247825318-REGULAR-0173050015 1247825318 SOL 13 12:02:28
     IMP_EDR-1247825324-REGULAR-0173050017 1247825324 SOL 13 12:02:33
     IMP_EDR-1247825331-REGULAR-0173050019 1247825331 SOL 13 12:02:40
     IMP_EDR-1247825343-REGULAR-0173050021 1247825343 SOL 13 12:02:52
     IMP_EDR-1247825349-REGULAR-0173050023 1247825349 SOL 13 12:02:58
     IMP_EDR-1247825356-REGULAR-0173050025 1247825356 SOL 13 12:03:05
     IMP_EDR-1247914686-REGULAR-0173050003 1247914686 SOL 14 12:12:14
     IMP_EDR-1247914693-REGULAR-0173050005 1247914693 SOL 14 12:12:21
     IMP_EDR-1247914699-REGULAR-0173050007 1247914699 SOL 14 12:12:27
     IMP_EDR-1247914711-REGULAR-0173050009 1247914711 SOL 14 12:12:39
     IMP_EDR-1247914718-REGULAR-0173050011 1247914718 SOL 14 12:12:45
     IMP_EDR-1247914725-REGULAR-0173050013 1247914725 SOL 14 12:12:52
     IMP_EDR-1247914736-REGULAR-0173050015 1247914736 SOL 14 12:13:03
     IMP_EDR-1247914743-REGULAR-0173050017 1247914743 SOL 14 12:13:10
     IMP_EDR-1247914750-REGULAR-0173050019 1247914750 SOL 14 12:13:17
     IMP_EDR-1247914762-REGULAR-0173050021 1247914762 SOL 14 12:13:28
     IMP_EDR-1247914768-REGULAR-0173050023 1247914768 SOL 14 12:13:34
     IMP_EDR-1247914775-REGULAR-0173050025 1247914775 SOL 14 12:13:41
     IMP_EDR-1248003068-REGULAR-0173050003 1248003068 SOL 15 12:06:01
     IMP_EDR-1248003074-REGULAR-0173050005 1248003074 SOL 15 12:06:07
     IMP_EDR-1248003081-REGULAR-0173050007 1248003081 SOL 15 12:06:14
     IMP_EDR-1248003096-REGULAR-0173050009 1248003096 SOL 15 12:06:28
     IMP_EDR-1248003102-REGULAR-0173050011 1248003102 SOL 15 12:06:34
     IMP_EDR-1248003108-REGULAR-0173050013 1248003108 SOL 15 12:06:40
     IMP_EDR-1248003119-REGULAR-0173050015 1248003119 SOL 15 12:06:51
     IMP_EDR-1248003126-REGULAR-0173050017 1248003126 SOL 15 12:06:58
     IMP_EDR-1248003132-REGULAR-0173050019 1248003132 SOL 15 12:07:04
     IMP_EDR-1248003147-REGULAR-0173050021 1248003147 SOL 15 12:07:18
     IMP_EDR-1248003153-REGULAR-0173050023 1248003153 SOL 15 12:07:24
     IMP_EDR-1248003160-REGULAR-0173050025 1248003160 SOL 15 12:07:31
     IMP_EDR-1248268697-REGULAR-0173050003 1248268697 SOL 18 11:55:12
     IMP_EDR-1248268704-REGULAR-0173050005 1248268704 SOL 18 11:55:19
     IMP_EDR-1248268711-REGULAR-0173050007 1248268711 SOL 18 11:55:26
     IMP_EDR-1248268729-REGULAR-0173050009 1248268729 SOL 18 11:55:43
     IMP_EDR-1248268736-REGULAR-0173050011 1248268736 SOL 18 11:55:50
     IMP_EDR-1248268744-REGULAR-0173050013 1248268744 SOL 18 11:55:58
     IMP_EDR-1248268756-REGULAR-0173050015 1248268756 SOL 18 11:56:10
     IMP_EDR-1248268763-REGULAR-0173050017 1248268763 SOL 18 11:56:16
     IMP_EDR-1248268770-REGULAR-0173050019 1248268770 SOL 18 11:56:23
     IMP_EDR-1248268787-REGULAR-0173050021 1248268787 SOL 18 11:56:40
     IMP_EDR-1248268794-REGULAR-0173050023 1248268794 SOL 18 11:56:47
     IMP_EDR-1248268801-REGULAR-0173050025 1248268801 SOL 18 11:56:53
     IMP_EDR-1248358199-REGULAR-0173050003 1248358199 SOL 19 12:07:09
     IMP_EDR-1248358206-REGULAR-0173050005 1248358206 SOL 19 12:07:16
     IMP_EDR-1248358212-REGULAR-0173050007 1248358212 SOL 19 12:07:22
     IMP_EDR-1248358228-REGULAR-0173050009 1248358228 SOL 19 12:07:37
     IMP_EDR-1248358234-REGULAR-0173050011 1248358234 SOL 19 12:07:43
     IMP_EDR-1248358242-REGULAR-0173050013 1248358242 SOL 19 12:07:51
     IMP_EDR-1248358254-REGULAR-0173050015 1248358254 SOL 19 12:08:03
     IMP_EDR-1248358260-REGULAR-0173050017 1248358260 SOL 19 12:08:09
     IMP_EDR-1248358267-REGULAR-0173050019 1248358267 SOL 19 12:08:15
     IMP_EDR-1248358282-REGULAR-0173050021 1248358282 SOL 19 12:08:30
     IMP_EDR-1248358289-REGULAR-0173050023 1248358289 SOL 19 12:08:37
     IMP_EDR-1248358296-REGULAR-0173050025 1248358296 SOL 19 12:08:44
     IMP_EDR-1248446970-REGULAR-0173050003 1248446970 SOL 20 12:07:15
     IMP_EDR-1248446977-REGULAR-0173050005 1248446977 SOL 20 12:07:21
     IMP_EDR-1248446983-REGULAR-0173050007 1248446983 SOL 20 12:07:27
     IMP_EDR-1248447006-REGULAR-0173050009 1248447006 SOL 20 12:07:50
     IMP_EDR-1248447013-REGULAR-0173050011 1248447013 SOL 20 12:07:56
     IMP_EDR-1248447019-REGULAR-0173050013 1248447019 SOL 20 12:08:02
     IMP_EDR-1248447031-REGULAR-0173050015 1248447031 SOL 20 12:08:14
     IMP_EDR-1248447039-REGULAR-0173050017 1248447039 SOL 20 12:08:22
     IMP_EDR-1248447046-REGULAR-0173050019 1248447046 SOL 20 12:08:29
     IMP_EDR-1248447062-REGULAR-0173050021 1248447062 SOL 20 12:08:44
     IMP_EDR-1248447068-REGULAR-0173050023 1248447068 SOL 20 12:08:50
     IMP_EDR-1248447075-REGULAR-0173050025 1248447075 SOL 20 12:08:57
     IMP_EDR-1248536085-REGULAR-0173050003 1248536085 SOL 21 12:12:55
     IMP_EDR-1248536092-REGULAR-0173050005 1248536092 SOL 21 12:13:02
     IMP_EDR-1248536098-REGULAR-0173050007 1248536098 SOL 21 12:13:08
     IMP_EDR-1248536110-REGULAR-0173050009 1248536110 SOL 21 12:13:19
     IMP_EDR-1248536117-REGULAR-0173050011 1248536117 SOL 21 12:13:26
     IMP_EDR-1248536123-REGULAR-0173050013 1248536123 SOL 21 12:13:32
     IMP_EDR-1248536135-REGULAR-0173050015 1248536135 SOL 21 12:13:44
     IMP_EDR-1248536142-REGULAR-0173050017 1248536142 SOL 21 12:13:50
     IMP_EDR-1248536149-REGULAR-0173050019 1248536149 SOL 21 12:13:57
     IMP_EDR-1248536160-REGULAR-0173050021 1248536160 SOL 21 12:14:08
     IMP_EDR-1248536167-REGULAR-0173050023 1248536167 SOL 21 12:14:15
     IMP_EDR-1248536174-REGULAR-0173050025 1248536174 SOL 21 12:14:22
     IMP_EDR-1248624154-REGULAR-0173050003 1248624154 SOL 22 12:01:37
     IMP_EDR-1248624161-REGULAR-0173050005 1248624161 SOL 22 12:01:44
     IMP_EDR-1248624167-REGULAR-0173050007 1248624167 SOL 22 12:01:50
     IMP_EDR-1248624183-REGULAR-0173050009 1248624183 SOL 22 12:02:05
     IMP_EDR-1248624190-REGULAR-0173050011 1248624190 SOL 22 12:02:12
     IMP_EDR-1248624196-REGULAR-0173050013 1248624196 SOL 22 12:02:18
     IMP_EDR-1248624208-REGULAR-0173050015 1248624208 SOL 22 12:02:30
     IMP_EDR-1248624215-REGULAR-0173050017 1248624215 SOL 22 12:02:36
     IMP_EDR-1248624222-REGULAR-0173050019 1248624222 SOL 22 12:02:43
     IMP_EDR-1248624237-REGULAR-0173050021 1248624237 SOL 22 12:02:58
     IMP_EDR-1248624244-REGULAR-0173050023 1248624244 SOL 22 12:03:05
     IMP_EDR-1248624250-REGULAR-0173050025 1248624250 SOL 22 12:03:10
     IMP_EDR-1248712932-REGULAR-0173050003 1248712932 SOL 23 12:01:49
     IMP_EDR-1248712939-REGULAR-0173050005 1248712939 SOL 23 12:01:56
     IMP_EDR-1248712945-REGULAR-0173050007 1248712945 SOL 23 12:02:02
     IMP_EDR-1248712961-REGULAR-0173050009 1248712961 SOL 23 12:02:17
     IMP_EDR-1248712967-REGULAR-0173050011 1248712967 SOL 23 12:02:23
     IMP_EDR-1248712974-REGULAR-0173050013 1248712974 SOL 23 12:02:30
     IMP_EDR-1248712986-REGULAR-0173050015 1248712986 SOL 23 12:02:42
     IMP_EDR-1248712993-REGULAR-0173050017 1248712993 SOL 23 12:02:49
     IMP_EDR-1248712999-REGULAR-0173050019 1248712999 SOL 23 12:02:54
     IMP_EDR-1248713015-REGULAR-0173050021 1248713015 SOL 23 12:03:10
     IMP_EDR-1248713021-REGULAR-0173050023 1248713021 SOL 23 12:03:16
     IMP_EDR-1248713028-REGULAR-0173050025 1248713028 SOL 23 12:03:23
     IMP_EDR-1248801768-REGULAR-0173050003 1248801768 SOL 24 12:02:58
     IMP_EDR-1248801775-REGULAR-0173050005 1248801775 SOL 24 12:03:05
     IMP_EDR-1248801781-REGULAR-0173050007 1248801781 SOL 24 12:03:10
     IMP_EDR-1248801789-REGULAR-0173050009 1248801789 SOL 24 12:03:18
     IMP_EDR-1248801797-REGULAR-0173050011 1248801797 SOL 24 12:03:26
     IMP_EDR-1248801815-REGULAR-0173050013 1248801815 SOL 24 12:03:43
     IMP_EDR-1248801835-REGULAR-0173050015 1248801835 SOL 24 12:04:03
     IMP_EDR-1248801852-REGULAR-0173050017 1248801852 SOL 24 12:04:19
     IMP_EDR-1248801863-REGULAR-0173050019 1248801863 SOL 24 12:04:30
     IMP_EDR-1248801874-REGULAR-0173050021 1248801874 SOL 24 12:04:41
     IMP_EDR-1248801881-REGULAR-0173050023 1248801881 SOL 24 12:04:48
     IMP_EDR-1248801887-REGULAR-0173050025 1248801887 SOL 24 12:04:54
     IMP_EDR-1248979181-REGULAR-0173060003 1248979181 SOL 26 12:01:03
     IMP_EDR-1248979188-REGULAR-0173060005 1248979188 SOL 26 12:01:09
     IMP_EDR-1248979195-REGULAR-0173060007 1248979195 SOL 26 12:01:16
     IMP_EDR-1248979210-REGULAR-0173060009 1248979210 SOL 26 12:01:31
     IMP_EDR-1248979217-REGULAR-0173060011 1248979217 SOL 26 12:01:38
     IMP_EDR-1248979224-REGULAR-0173060013 1248979224 SOL 26 12:01:44
     IMP_EDR-1248979235-REGULAR-0173060015 1248979235 SOL 26 12:01:55
     IMP_EDR-1248979242-REGULAR-0173060017 1248979242 SOL 26 12:02:02
     IMP_EDR-1248979249-REGULAR-0173060019 1248979249 SOL 26 12:02:09
     IMP_EDR-1248979265-REGULAR-0173060021 1248979265 SOL 26 12:02:24
     IMP_EDR-1248979271-REGULAR-0173060023 1248979271 SOL 26 12:02:30
     IMP_EDR-1248979278-REGULAR-0173060025 1248979278 SOL 26 12:02:37
     IMP_EDR-1249068553-REGULAR-0173060003 1249068553 SOL 27 12:10:53
     IMP_EDR-1249068561-REGULAR-0173060005 1249068561 SOL 27 12:11:00
     IMP_EDR-1249068569-REGULAR-0173060007 1249068569 SOL 27 12:11:08
     IMP_EDR-1249068586-REGULAR-0173060009 1249068586 SOL 27 12:11:25
     IMP_EDR-1249068593-REGULAR-0173060011 1249068593 SOL 27 12:11:32
     IMP_EDR-1249068601-REGULAR-0173060013 1249068601 SOL 27 12:11:39
     IMP_EDR-1249068614-REGULAR-0173060015 1249068614 SOL 27 12:11:52
     IMP_EDR-1249068621-REGULAR-0173060017 1249068621 SOL 27 12:11:59
     IMP_EDR-1249068629-REGULAR-0173060019 1249068629 SOL 27 12:12:07
     IMP_EDR-1249068646-REGULAR-0173060021 1249068646 SOL 27 12:12:23
     IMP_EDR-1249068653-REGULAR-0173060023 1249068653 SOL 27 12:12:30
     IMP_EDR-1249068660-REGULAR-0173060025 1249068660 SOL 27 12:12:37
     IMP_EDR-1249156792-REGULAR-0173060003 1249156792 SOL 28 12:02:20
     IMP_EDR-1249156799-REGULAR-0173060005 1249156799 SOL 28 12:02:27
     IMP_EDR-1249156806-REGULAR-0173060007 1249156806 SOL 28 12:02:34
     IMP_EDR-1249156821-REGULAR-0173060009 1249156821 SOL 28 12:02:48
     IMP_EDR-1249156828-REGULAR-0173060011 1249156828 SOL 28 12:02:55
     IMP_EDR-1249156835-REGULAR-0173060013 1249156835 SOL 28 12:03:02
     IMP_EDR-1249156847-REGULAR-0173060015 1249156847 SOL 28 12:03:13
     IMP_EDR-1249156854-REGULAR-0173060017 1249156854 SOL 28 12:03:20
     IMP_EDR-1249156861-REGULAR-0173060019 1249156861 SOL 28 12:03:27
     IMP_EDR-1249156876-REGULAR-0173060021 1249156876 SOL 28 12:03:42
     IMP_EDR-1249156883-REGULAR-0173060023 1249156883 SOL 28 12:03:49
     IMP_EDR-1249156890-REGULAR-0173060025 1249156890 SOL 28 12:03:55
     IMP_EDR-1249333745-REGULAR-0173060003 1249333745 SOL 30 11:52:57
     IMP_EDR-1249333752-REGULAR-0173060005 1249333752 SOL 30 11:53:03
     IMP_EDR-1249333759-REGULAR-0173060007 1249333759 SOL 30 11:53:10
     IMP_EDR-1249333775-REGULAR-0173060009 1249333775 SOL 30 11:53:26
     IMP_EDR-1249333781-REGULAR-0173060011 1249333781 SOL 30 11:53:32
     IMP_EDR-1249333788-REGULAR-0173060013 1249333788 SOL 30 11:53:38
     IMP_EDR-1249333801-REGULAR-0173060015 1249333801 SOL 30 11:53:51
     IMP_EDR-1249333808-REGULAR-0173060017 1249333808 SOL 30 11:53:58
     IMP_EDR-1249333816-REGULAR-0173060019 1249333816 SOL 30 11:54:06
     IMP_EDR-1249333833-REGULAR-0173060021 1249333833 SOL 30 11:54:22
     IMP_EDR-1249333841-REGULAR-0173060023 1249333841 SOL 30 11:54:30
     IMP_EDR-1249333848-REGULAR-0173060025 1249333848 SOL 30 11:54:37
     IMP_EDR-1249512793-REGULAR-0173060003 1249512793 SOL 32 12:17:25
     IMP_EDR-1249512800-REGULAR-0173060005 1249512800 SOL 32 12:17:32
     IMP_EDR-1249512807-REGULAR-0173060007 1249512807 SOL 32 12:17:39
     IMP_EDR-1249512823-REGULAR-0173060009 1249512823 SOL 32 12:17:54
     IMP_EDR-1249512829-REGULAR-0173060011 1249512829 SOL 32 12:18:00
     IMP_EDR-1249512836-REGULAR-0173060013 1249512836 SOL 32 12:18:07
     IMP_EDR-1249512848-REGULAR-0173060015 1249512848 SOL 32 12:18:19
     IMP_EDR-1249512855-REGULAR-0173060017 1249512855 SOL 32 12:18:26
     IMP_EDR-1249512862-REGULAR-0173060019 1249512862 SOL 32 12:18:32
     IMP_EDR-1249512877-REGULAR-0173060021 1249512877 SOL 32 12:18:47
     IMP_EDR-1249512885-REGULAR-0173060023 1249512885 SOL 32 12:18:55
     IMP_EDR-1249512892-REGULAR-0173060025 1249512892 SOL 32 12:19:02
     IMP_EDR-1249599812-REGULAR-0173060003 1249599812 SOL 33 11:48:57
     IMP_EDR-1249599820-REGULAR-0173060005 1249599820 SOL 33 11:49:05
     IMP_EDR-1249599827-REGULAR-0173060007 1249599827 SOL 33 11:49:12
     IMP_EDR-1249599843-REGULAR-0173060009 1249599843 SOL 33 11:49:28
     IMP_EDR-1249599849-REGULAR-0173060011 1249599849 SOL 33 11:49:33
     IMP_EDR-1249599856-REGULAR-0173060013 1249599856 SOL 33 11:49:40
     IMP_EDR-1249599868-REGULAR-0173060015 1249599868 SOL 33 11:49:52
     IMP_EDR-1249599875-REGULAR-0173060017 1249599875 SOL 33 11:49:59
     IMP_EDR-1249599881-REGULAR-0173060019 1249599881 SOL 33 11:50:04
     IMP_EDR-1249599898-REGULAR-0173060021 1249599898 SOL 33 11:50:21
     IMP_EDR-1249599906-REGULAR-0173060023 1249599906 SOL 33 11:50:29
     IMP_EDR-1249599913-REGULAR-0173060025 1249599913 SOL 33 11:50:36
     IMP_EDR-1249688397-REGULAR-0173070003 1249688397 SOL 34 11:46:01
     IMP_EDR-1249688403-REGULAR-0173070005 1249688403 SOL 34 11:46:07
     IMP_EDR-1249688410-REGULAR-0173070007 1249688410 SOL 34 11:46:14
     IMP_EDR-1249688425-REGULAR-0173070009 1249688425 SOL 34 11:46:28
     IMP_EDR-1249688431-REGULAR-0173070011 1249688431 SOL 34 11:46:34
     IMP_EDR-1249688438-REGULAR-0173070013 1249688438 SOL 34 11:46:41
     IMP_EDR-1249688449-REGULAR-0173070015 1249688449 SOL 34 11:46:52
     IMP_EDR-1249688455-REGULAR-0173070017 1249688455 SOL 34 11:46:57
     IMP_EDR-1249688462-REGULAR-0173070019 1249688462 SOL 34 11:47:04
     IMP_EDR-1249688476-REGULAR-0173070021 1249688476 SOL 34 11:47:18
     IMP_EDR-1249688483-REGULAR-0173070023 1249688483 SOL 34 11:47:25
     IMP_EDR-1249688489-REGULAR-0173070025 1249688489 SOL 34 11:47:31
     IMP_EDR-1249776875-REGULAR-0173070003 1249776875 SOL 35 11:41:13
     IMP_EDR-1249776882-REGULAR-0173070005 1249776882 SOL 35 11:41:20
     IMP_EDR-1249776889-REGULAR-0173070007 1249776889 SOL 35 11:41:27
     IMP_EDR-1249776904-REGULAR-0173070009 1249776904 SOL 35 11:41:41
     IMP_EDR-1249776911-REGULAR-0173070011 1249776911 SOL 35 11:41:48
     IMP_EDR-1249776918-REGULAR-0173070013 1249776918 SOL 35 11:41:55
     IMP_EDR-1249776929-REGULAR-0173070015 1249776929 SOL 35 11:42:06
     IMP_EDR-1249776936-REGULAR-0173070017 1249776936 SOL 35 11:42:12
     IMP_EDR-1249776943-REGULAR-0173070019 1249776943 SOL 35 11:42:19
     IMP_EDR-1249776959-REGULAR-0173070021 1249776959 SOL 35 11:42:35
     IMP_EDR-1249776965-REGULAR-0173070023 1249776965 SOL 35 11:42:41
     IMP_EDR-1249776972-REGULAR-0173070025 1249776972 SOL 35 11:42:47
     IMP_EDR-1249865641-REGULAR-0173070003 1249865641 SOL 36 11:40:57
     IMP_EDR-1249865648-REGULAR-0173070005 1249865648 SOL 36 11:41:04
     IMP_EDR-1249865656-REGULAR-0173070007 1249865656 SOL 36 11:41:12
     IMP_EDR-1249865672-REGULAR-0173070009 1249865672 SOL 36 11:41:28
     IMP_EDR-1249865679-REGULAR-0173070011 1249865679 SOL 36 11:41:34
     IMP_EDR-1249865686-REGULAR-0173070013 1249865686 SOL 36 11:41:41
     IMP_EDR-1249865698-REGULAR-0173070015 1249865698 SOL 36 11:41:53
     IMP_EDR-1249865705-REGULAR-0173070017 1249865705 SOL 36 11:42:00
     IMP_EDR-1249865712-REGULAR-0173070019 1249865712 SOL 36 11:42:06
     IMP_EDR-1249865728-REGULAR-0173070021 1249865728 SOL 36 11:42:22
     IMP_EDR-1249865735-REGULAR-0173070023 1249865735 SOL 36 11:42:29
     IMP_EDR-1249865742-REGULAR-0173070025 1249865742 SOL 36 11:42:36
     IMP_EDR-1249954450-REGULAR-0173070003 1249954450 SOL 37 11:41:31
     IMP_EDR-1249954457-REGULAR-0173070005 1249954457 SOL 37 11:41:37
     IMP_EDR-1249954464-REGULAR-0173070007 1249954464 SOL 37 11:41:44
     IMP_EDR-1249954480-REGULAR-0173070009 1249954480 SOL 37 11:42:00
     IMP_EDR-1249954487-REGULAR-0173070011 1249954487 SOL 37 11:42:07
     IMP_EDR-1249954514-REGULAR-0173070013 1249954514 SOL 37 11:42:33
     IMP_EDR-1249954529-REGULAR-0173070015 1249954529 SOL 37 11:42:47
     IMP_EDR-1249954539-REGULAR-0173070017 1249954539 SOL 37 11:42:57
     IMP_EDR-1249954554-REGULAR-0173070019 1249954554 SOL 37 11:43:12
     IMP_EDR-1249954570-REGULAR-0173070021 1249954570 SOL 37 11:43:27
     IMP_EDR-1249954576-REGULAR-0173070023 1249954576 SOL 37 11:43:33
     IMP_EDR-1249954583-REGULAR-0173070025 1249954583 SOL 37 11:43:40
     IMP_EDR-1250042854-REGULAR-0173070003 1250042854 SOL 38 11:35:38
     IMP_EDR-1250042861-REGULAR-0173070005 1250042861 SOL 38 11:35:45
     IMP_EDR-1250042868-REGULAR-0173070007 1250042868 SOL 38 11:35:51
     IMP_EDR-1250042884-REGULAR-0173070009 1250042884 SOL 38 11:36:07
     IMP_EDR-1250042890-REGULAR-0173070011 1250042890 SOL 38 11:36:13
     IMP_EDR-1250042897-REGULAR-0173070013 1250042897 SOL 38 11:36:20
     IMP_EDR-1250042909-REGULAR-0173070015 1250042909 SOL 38 11:36:31
     IMP_EDR-1250042916-REGULAR-0173070017 1250042916 SOL 38 11:36:38
     IMP_EDR-1250042922-REGULAR-0173070019 1250042922 SOL 38 11:36:44
     IMP_EDR-1250042938-REGULAR-0173070021 1250042938 SOL 38 11:36:59
     IMP_EDR-1250042945-REGULAR-0173070023 1250042945 SOL 38 11:37:06
     IMP_EDR-1250042951-REGULAR-0173070025 1250042951 SOL 38 11:37:12
     IMP_EDR-1250043442-REGULAR-0173070003 1250043442 SOL 38 11:45:10
     IMP_EDR-1250043449-REGULAR-0173070005 1250043449 SOL 38 11:45:17
     IMP_EDR-1250043456-REGULAR-0173070007 1250043456 SOL 38 11:45:24
     IMP_EDR-1250043471-REGULAR-0173070009 1250043471 SOL 38 11:45:38
     IMP_EDR-1250043478-REGULAR-0173070011 1250043478 SOL 38 11:45:45
     IMP_EDR-1250043485-REGULAR-0173070013 1250043485 SOL 38 11:45:52
     IMP_EDR-1250043496-REGULAR-0173070015 1250043496 SOL 38 11:46:03
     IMP_EDR-1250043503-REGULAR-0173070017 1250043503 SOL 38 11:46:09
     IMP_EDR-1250043510-REGULAR-0173070019 1250043510 SOL 38 11:46:16
     IMP_EDR-1250043526-REGULAR-0173070021 1250043526 SOL 38 11:46:32
     IMP_EDR-1250043532-REGULAR-0173070023 1250043532 SOL 38 11:46:38
     IMP_EDR-1250043539-REGULAR-0173070025 1250043539 SOL 38 11:46:44
     IMP_EDR-1250131954-REGULAR-0173070003 1250131954 SOL 39 11:40:55
     IMP_EDR-1250131961-REGULAR-0173070005 1250131961 SOL 39 11:41:02
     IMP_EDR-1250131968-REGULAR-0173070007 1250131968 SOL 39 11:41:09
     IMP_EDR-1250131985-REGULAR-0173070009 1250131985 SOL 39 11:41:25
     IMP_EDR-1250131993-REGULAR-0173070011 1250131993 SOL 39 11:41:33
     IMP_EDR-1250132000-REGULAR-0173070013 1250132000 SOL 39 11:41:40
     IMP_EDR-1250132012-REGULAR-0173070015 1250132012 SOL 39 11:41:51
     IMP_EDR-1250132020-REGULAR-0173070017 1250132020 SOL 39 11:41:59
     IMP_EDR-1250132027-REGULAR-0173070019 1250132027 SOL 39 11:42:06
     IMP_EDR-1250132042-REGULAR-0173070021 1250132042 SOL 39 11:42:21
     IMP_EDR-1250132049-REGULAR-0173070023 1250132049 SOL 39 11:42:27
     IMP_EDR-1250132056-REGULAR-0173070025 1250132056 SOL 39 11:42:34
     IMP_EDR-1250219047-REGULAR-0173070003 1250219047 SOL 40 11:13:46
     IMP_EDR-1250219108-REGULAR-0173070017 1250219108 SOL 40 11:14:45
     IMP_EDR-1250219115-REGULAR-0173070019 1250219115 SOL 40 11:14:52
     IMP_EDR-1250219130-REGULAR-0173070021 1250219130 SOL 40 11:15:07
     IMP_EDR-1250219137-REGULAR-0173070023 1250219137 SOL 40 11:15:13
     IMP_EDR-1250219144-REGULAR-0173070025 1250219144 SOL 40 11:15:20
     IMP_EDR-1250219635-REGULAR-0173070003 1250219635 SOL 40 11:23:18
     IMP_EDR-1250219641-REGULAR-0173070005 1250219641 SOL 40 11:23:24
     IMP_EDR-1250219648-REGULAR-0173070007 1250219648 SOL 40 11:23:31
     IMP_EDR-1250219664-REGULAR-0173070009 1250219664 SOL 40 11:23:46
     IMP_EDR-1250219671-REGULAR-0173070011 1250219671 SOL 40 11:23:53
     IMP_EDR-1250219677-REGULAR-0173070013 1250219677 SOL 40 11:23:59
     IMP_EDR-1250219689-REGULAR-0173070015 1250219689 SOL 40 11:24:11
     IMP_EDR-1250219696-REGULAR-0173070017 1250219696 SOL 40 11:24:17
     IMP_EDR-1250219703-REGULAR-0173070019 1250219703 SOL 40 11:24:24
     IMP_EDR-1250219718-REGULAR-0173070021 1250219718 SOL 40 11:24:39
     IMP_EDR-1250219725-REGULAR-0173070023 1250219725 SOL 40 11:24:46
     IMP_EDR-1250219731-REGULAR-0173070025 1250219731 SOL 40 11:24:52
     IMP_EDR-1250224269-REGULAR-0173070003 1250224269 SOL 40 12:38:29
     IMP_EDR-1250224276-REGULAR-0173070005 1250224276 SOL 40 12:38:35
     IMP_EDR-1250224282-REGULAR-0173070007 1250224282 SOL 40 12:38:41
     IMP_EDR-1250224294-REGULAR-0173070009 1250224294 SOL 40 12:38:53
     IMP_EDR-1250224301-REGULAR-0173070011 1250224301 SOL 40 12:39:00
     IMP_EDR-1250224308-REGULAR-0173070013 1250224308 SOL 40 12:39:06
     IMP_EDR-1250224319-REGULAR-0173070015 1250224319 SOL 40 12:39:17
     IMP_EDR-1250224326-REGULAR-0173070017 1250224326 SOL 40 12:39:24
     IMP_EDR-1250224333-REGULAR-0173070019 1250224333 SOL 40 12:39:31
     IMP_EDR-1250224345-REGULAR-0173070021 1250224345 SOL 40 12:39:43
     IMP_EDR-1250224351-REGULAR-0173070023 1250224351 SOL 40 12:39:48
     IMP_EDR-1250224358-REGULAR-0173070025 1250224358 SOL 40 12:39:55
     IMP_EDR-1250308440-REGULAR-0173070003 1250308440 SOL 41 11:23:40
     IMP_EDR-1250308447-REGULAR-0173070005 1250308447 SOL 41 11:23:47
     IMP_EDR-1250308453-REGULAR-0173070007 1250308453 SOL 41 11:23:53
     IMP_EDR-1250308469-REGULAR-0173070009 1250308469 SOL 41 11:24:08
     IMP_EDR-1250308476-REGULAR-0173070011 1250308476 SOL 41 11:24:15
     IMP_EDR-1250308482-REGULAR-0173070013 1250308482 SOL 41 11:24:21
     IMP_EDR-1250308494-REGULAR-0173070015 1250308494 SOL 41 11:24:32
     IMP_EDR-1250308501-REGULAR-0173070017 1250308501 SOL 41 11:24:39
     IMP_EDR-1250308508-REGULAR-0173070019 1250308508 SOL 41 11:24:46
     IMP_EDR-1250308524-REGULAR-0173070021 1250308524 SOL 41 11:25:02
     IMP_EDR-1250308530-REGULAR-0173070023 1250308530 SOL 41 11:25:08
     IMP_EDR-1250308537-REGULAR-0173070025 1250308537 SOL 41 11:25:14
     IMP_EDR-1250309668-REGULAR-0173070003 1250309668 SOL 41 11:43:35
     IMP_EDR-1250309674-REGULAR-0173070005 1250309674 SOL 41 11:43:41
     IMP_EDR-1250309681-REGULAR-0173070007 1250309681 SOL 41 11:43:48
     IMP_EDR-1250309697-REGULAR-0173070009 1250309697 SOL 41 11:44:03
     IMP_EDR-1250309704-REGULAR-0173070011 1250309704 SOL 41 11:44:10
     IMP_EDR-1250309710-REGULAR-0173070013 1250309710 SOL 41 11:44:16
     IMP_EDR-1250309722-REGULAR-0173070015 1250309722 SOL 41 11:44:28
     IMP_EDR-1250309729-REGULAR-0173070017 1250309729 SOL 41 11:44:35
     IMP_EDR-1250309736-REGULAR-0173070019 1250309736 SOL 41 11:44:41
     IMP_EDR-1250309751-REGULAR-0173070021 1250309751 SOL 41 11:44:56
     IMP_EDR-1250309758-REGULAR-0173070023 1250309758 SOL 41 11:45:03
     IMP_EDR-1250309765-REGULAR-0173070025 1250309765 SOL 41 11:45:10
     IMP_EDR-1250397375-REGULAR-0173070003 1250397375 SOL 42 11:26:16
     IMP_EDR-1250397382-REGULAR-0173070005 1250397382 SOL 42 11:26:23
     IMP_EDR-1250397389-REGULAR-0173070007 1250397389 SOL 42 11:26:30
     IMP_EDR-1250397405-REGULAR-0173070009 1250397405 SOL 42 11:26:45
     IMP_EDR-1250397412-REGULAR-0173070011 1250397412 SOL 42 11:26:52
     IMP_EDR-1250397418-REGULAR-0173070013 1250397418 SOL 42 11:26:58
     IMP_EDR-1250397431-REGULAR-0173070015 1250397431 SOL 42 11:27:11
     IMP_EDR-1250397437-REGULAR-0173070017 1250397437 SOL 42 11:27:17
     IMP_EDR-1250397444-REGULAR-0173070019 1250397444 SOL 42 11:27:23
     IMP_EDR-1250397460-REGULAR-0173070021 1250397460 SOL 42 11:27:39
     IMP_EDR-1250397467-REGULAR-0173070023 1250397467 SOL 42 11:27:46
     IMP_EDR-1250397473-REGULAR-0173070025 1250397473 SOL 42 11:27:52
     IMP_EDR-1250398877-REGULAR-0173070003 1250398877 SOL 42 11:50:38
     IMP_EDR-1250398884-REGULAR-0173070005 1250398884 SOL 42 11:50:45
     IMP_EDR-1250398890-REGULAR-0173070007 1250398890 SOL 42 11:50:51
     IMP_EDR-1250398906-REGULAR-0173070009 1250398906 SOL 42 11:51:06
     IMP_EDR-1250398913-REGULAR-0173070011 1250398913 SOL 42 11:51:13
     IMP_EDR-1250398920-REGULAR-0173070013 1250398920 SOL 42 11:51:20
     IMP_EDR-1250398931-REGULAR-0173070015 1250398931 SOL 42 11:51:31
     IMP_EDR-1250398938-REGULAR-0173070017 1250398938 SOL 42 11:51:38
     IMP_EDR-1250398945-REGULAR-0173070019 1250398945 SOL 42 11:51:44
     IMP_EDR-1250398961-REGULAR-0173070021 1250398961 SOL 42 11:52:00
     IMP_EDR-1250398968-REGULAR-0173070023 1250398968 SOL 42 11:52:07
     IMP_EDR-1250398974-REGULAR-0173070025 1250398974 SOL 42 11:52:13
     IMP_EDR-1250574244-REGULAR-0173070003 1250574244 SOL 44 11:15:29
     IMP_EDR-1250574251-REGULAR-0173070005 1250574251 SOL 44 11:15:36
     IMP_EDR-1250574258-REGULAR-0173070007 1250574258 SOL 44 11:15:42
     IMP_EDR-1250574274-REGULAR-0173070009 1250574274 SOL 44 11:15:58
     IMP_EDR-1250574281-REGULAR-0173070011 1250574281 SOL 44 11:16:05
     IMP_EDR-1250574287-REGULAR-0173070013 1250574287 SOL 44 11:16:11
     IMP_EDR-1250574299-REGULAR-0173070015 1250574299 SOL 44 11:16:22
     IMP_EDR-1250574306-REGULAR-0173070017 1250574306 SOL 44 11:16:29
     IMP_EDR-1250574313-REGULAR-0173070019 1250574313 SOL 44 11:16:36
     IMP_EDR-1250574328-REGULAR-0173070021 1250574328 SOL 44 11:16:50
     IMP_EDR-1250574335-REGULAR-0173070023 1250574335 SOL 44 11:16:57
     IMP_EDR-1250574341-REGULAR-0173070025 1250574341 SOL 44 11:17:03
     IMP_EDR-1251020035-REGULAR-0173070017 1251020035 SOL 49 11:47:10
     IMP_EDR-1251020042-REGULAR-0173070019 1251020042 SOL 49 11:47:17
     IMP_EDR-1251020057-REGULAR-0173070021 1251020057 SOL 49 11:47:31
     IMP_EDR-1251020064-REGULAR-0173070023 1251020064 SOL 49 11:47:38
     IMP_EDR-1251020070-REGULAR-0173070025 1251020070 SOL 49 11:47:44
     IMP_EDR-1251021245-REGULAR-0173070003 1251021245 SOL 49 12:06:48
     IMP_EDR-1251021252-REGULAR-0173070005 1251021252 SOL 49 12:06:55
     IMP_EDR-1251021259-REGULAR-0173070007 1251021259 SOL 49 12:07:01
     IMP_EDR-1251021274-REGULAR-0173070009 1251021274 SOL 49 12:07:16
     IMP_EDR-1251021281-REGULAR-0173070011 1251021281 SOL 49 12:07:23
     IMP_EDR-1251021288-REGULAR-0173070013 1251021288 SOL 49 12:07:30
     IMP_EDR-1251021299-REGULAR-0173070015 1251021299 SOL 49 12:07:40
     IMP_EDR-1251021306-REGULAR-0173070017 1251021306 SOL 49 12:07:47
     IMP_EDR-1251021313-REGULAR-0173070019 1251021313 SOL 49 12:07:54
     IMP_EDR-1251021329-REGULAR-0173070021 1251021329 SOL 49 12:08:09
     IMP_EDR-1251021335-REGULAR-0173070023 1251021335 SOL 49 12:08:15
     IMP_EDR-1251021342-REGULAR-0173070025 1251021342 SOL 49 12:08:22
     IMP_EDR-1251021823-REGULAR-0173070003 1251021823 SOL 49 12:16:10
     IMP_EDR-1251021829-REGULAR-0173070005 1251021829 SOL 49 12:16:16
     IMP_EDR-1251021836-REGULAR-0173070007 1251021836 SOL 49 12:16:23
     IMP_EDR-1251021852-REGULAR-0173070009 1251021852 SOL 49 12:16:39
     IMP_EDR-1251021858-REGULAR-0173070011 1251021858 SOL 49 12:16:44
     IMP_EDR-1251021865-REGULAR-0173070013 1251021865 SOL 49 12:16:51
     IMP_EDR-1251021877-REGULAR-0173070015 1251021877 SOL 49 12:17:03
     IMP_EDR-1251021884-REGULAR-0173070017 1251021884 SOL 49 12:17:10
     IMP_EDR-1251021890-REGULAR-0173070019 1251021890 SOL 49 12:17:15
     IMP_EDR-1251021906-REGULAR-0173070021 1251021906 SOL 49 12:17:31
     IMP_EDR-1251021913-REGULAR-0173070023 1251021913 SOL 49 12:17:38
     IMP_EDR-1251021919-REGULAR-0173070025 1251021919 SOL 49 12:17:44
     IMP_EDR-1251022440-REGULAR-0173070003 1251022440 SOL 49 12:26:11
     IMP_EDR-1251022446-REGULAR-0173070005 1251022446 SOL 49 12:26:17
     IMP_EDR-1251022453-REGULAR-0173070007 1251022453 SOL 49 12:26:23
     IMP_EDR-1251022469-REGULAR-0173070009 1251022469 SOL 49 12:26:39
     IMP_EDR-1251022476-REGULAR-0173070011 1251022476 SOL 49 12:26:46
     IMP_EDR-1251022482-REGULAR-0173070013 1251022482 SOL 49 12:26:52
     IMP_EDR-1251022494-REGULAR-0173070015 1251022494 SOL 49 12:27:03
     IMP_EDR-1251022501-REGULAR-0173070017 1251022501 SOL 49 12:27:10
     IMP_EDR-1251022524-REGULAR-0173070021 1251022524 SOL 49 12:27:33
     IMP_EDR-1251108808-REGULAR-0173070003 1251108808 SOL 50 11:47:15
     IMP_EDR-1251108814-REGULAR-0173070005 1251108814 SOL 50 11:47:21
     IMP_EDR-1251108821-REGULAR-0173070007 1251108821 SOL 50 11:47:28
     IMP_EDR-1251108836-REGULAR-0173070009 1251108836 SOL 50 11:47:42
     IMP_EDR-1251108842-REGULAR-0173070011 1251108842 SOL 50 11:47:48
     IMP_EDR-1251286350-REGULAR-0173070003 1251286350 SOL 52 11:46:24
     IMP_EDR-1251286357-REGULAR-0173070005 1251286357 SOL 52 11:46:31
     IMP_EDR-1251286363-REGULAR-0173070007 1251286363 SOL 52 11:46:37
     IMP_EDR-1251286379-REGULAR-0173070009 1251286379 SOL 52 11:46:52
     IMP_EDR-1251286386-REGULAR-0173070011 1251286386 SOL 52 11:46:59
     IMP_EDR-1251286392-REGULAR-0173070013 1251286392 SOL 52 11:47:05
     IMP_EDR-1251286404-REGULAR-0173070015 1251286404 SOL 52 11:47:17
     IMP_EDR-1251286411-REGULAR-0173070017 1251286411 SOL 52 11:47:24
     IMP_EDR-1251286418-REGULAR-0173070019 1251286418 SOL 52 11:47:30
     IMP_EDR-1251286433-REGULAR-0173070021 1251286433 SOL 52 11:47:45
     IMP_EDR-1251286440-REGULAR-0173070023 1251286440 SOL 52 11:47:52
     IMP_EDR-1251286447-REGULAR-0173070025 1251286447 SOL 52 11:47:59
     IMP_EDR-1251287623-REGULAR-0173070003 1251287623 SOL 52 12:07:03
     IMP_EDR-1251287630-REGULAR-0173070005 1251287630 SOL 52 12:07:10
     IMP_EDR-1251287637-REGULAR-0173070007 1251287637 SOL 52 12:07:17
     IMP_EDR-1251287652-REGULAR-0173070009 1251287652 SOL 52 12:07:31
     IMP_EDR-1251287659-REGULAR-0173070011 1251287659 SOL 52 12:07:38
     IMP_EDR-1251287666-REGULAR-0173070013 1251287666 SOL 52 12:07:45
     IMP_EDR-1251287677-REGULAR-0173070015 1251287677 SOL 52 12:07:56
     IMP_EDR-1251287684-REGULAR-0173070017 1251287684 SOL 52 12:08:03
     IMP_EDR-1251287691-REGULAR-0173070019 1251287691 SOL 52 12:08:09
     IMP_EDR-1251287706-REGULAR-0173070021 1251287706 SOL 52 12:08:24
     IMP_EDR-1251287713-REGULAR-0173070023 1251287713 SOL 52 12:08:31
     IMP_EDR-1251287720-REGULAR-0173070025 1251287720 SOL 52 12:08:38
     IMP_EDR-1251372789-REGULAR-0173070003 1251372789 SOL 53 11:08:16
     IMP_EDR-1251372796-REGULAR-0173070005 1251372796 SOL 53 11:08:22
     IMP_EDR-1251372802-REGULAR-0173070007 1251372802 SOL 53 11:08:28
     IMP_EDR-1251461932-REGULAR-0173070003 1251461932 SOL 54 11:14:21
     IMP_EDR-1251461938-REGULAR-0173070005 1251461938 SOL 54 11:14:26
     IMP_EDR-1251461945-REGULAR-0173070007 1251461945 SOL 54 11:14:33
     IMP_EDR-1251461960-REGULAR-0173070009 1251461960 SOL 54 11:14:48
     IMP_EDR-1251461966-REGULAR-0173070011 1251461966 SOL 54 11:14:54
     IMP_EDR-1251461972-REGULAR-0173070013 1251461972 SOL 54 11:15:00
     IMP_EDR-1251461983-REGULAR-0173070015 1251461983 SOL 54 11:15:10
     IMP_EDR-1251461990-REGULAR-0173070017 1251461990 SOL 54 11:15:17
     IMP_EDR-1251461996-REGULAR-0173070019 1251461996 SOL 54 11:15:23
     IMP_EDR-1251462011-REGULAR-0173070021 1251462011 SOL 54 11:15:37
     IMP_EDR-1251462018-REGULAR-0173070023 1251462018 SOL 54 11:15:44
     IMP_EDR-1251462024-REGULAR-0173070025 1251462024 SOL 54 11:15:50
     IMP_EDR-1251463757-REGULAR-0173070003 1251463757 SOL 54 11:43:57
     IMP_EDR-1251463763-REGULAR-0173070005 1251463763 SOL 54 11:44:03
     IMP_EDR-1251463770-REGULAR-0173070007 1251463770 SOL 54 11:44:10
     IMP_EDR-1251463786-REGULAR-0173070009 1251463786 SOL 54 11:44:25
     IMP_EDR-1251463793-REGULAR-0173070011 1251463793 SOL 54 11:44:32
     IMP_EDR-1251463799-REGULAR-0173070013 1251463799 SOL 54 11:44:38
     IMP_EDR-1251463811-REGULAR-0173070015 1251463811 SOL 54 11:44:49
     IMP_EDR-1251463818-REGULAR-0173070017 1251463818 SOL 54 11:44:56
     IMP_EDR-1251463825-REGULAR-0173070019 1251463825 SOL 54 11:45:03
     IMP_EDR-1251463840-REGULAR-0173070021 1251463840 SOL 54 11:45:18
     IMP_EDR-1251463847-REGULAR-0173070023 1251463847 SOL 54 11:45:24
     IMP_EDR-1251463854-REGULAR-0173070025 1251463854 SOL 54 11:45:31
     IMP_EDR-1251465028-REGULAR-0173070003 1251465028 SOL 54 12:04:26
     IMP_EDR-1251465035-REGULAR-0173070005 1251465035 SOL 54 12:04:33
     IMP_EDR-1251465042-REGULAR-0173070007 1251465042 SOL 54 12:04:40
     IMP_EDR-1251465058-REGULAR-0173070009 1251465058 SOL 54 12:04:55
     IMP_EDR-1251465065-REGULAR-0173070011 1251465065 SOL 54 12:05:02
     IMP_EDR-1251465071-REGULAR-0173070013 1251465071 SOL 54 12:05:08
     IMP_EDR-1251465083-REGULAR-0173070015 1251465083 SOL 54 12:05:20
     IMP_EDR-1251465090-REGULAR-0173070017 1251465090 SOL 54 12:05:27
     IMP_EDR-1251465097-REGULAR-0173070019 1251465097 SOL 54 12:05:33
     IMP_EDR-1251465112-REGULAR-0173070021 1251465112 SOL 54 12:05:48
     IMP_EDR-1251465119-REGULAR-0173070023 1251465119 SOL 54 12:05:55
     IMP_EDR-1251465126-REGULAR-0173070025 1251465126 SOL 54 12:06:02
     IMP_EDR-1251552620-REGULAR-0173070003 1251552620 SOL 55 11:45:16
     IMP_EDR-1251552626-REGULAR-0173070005 1251552626 SOL 55 11:45:22
     IMP_EDR-1251552633-REGULAR-0173070007 1251552633 SOL 55 11:45:29
     IMP_EDR-1251552649-REGULAR-0173070009 1251552649 SOL 55 11:45:44
     IMP_EDR-1251552655-REGULAR-0173070011 1251552655 SOL 55 11:45:50
     IMP_EDR-1251552662-REGULAR-0173070013 1251552662 SOL 55 11:45:57
     IMP_EDR-1251552674-REGULAR-0173070015 1251552674 SOL 55 11:46:09
     IMP_EDR-1251552681-REGULAR-0173070017 1251552681 SOL 55 11:46:15
     IMP_EDR-1251552687-REGULAR-0173070019 1251552687 SOL 55 11:46:21
     IMP_EDR-1251552703-REGULAR-0173070021 1251552703 SOL 55 11:46:37
     IMP_EDR-1251552710-REGULAR-0173070023 1251552710 SOL 55 11:46:43
     IMP_EDR-1251552716-REGULAR-0173070025 1251552716 SOL 55 11:46:49
     IMP_EDR-1251639621-REGULAR-0173070003 1251639621 SOL 56 11:16:33
     IMP_EDR-1251639628-REGULAR-0173070005 1251639628 SOL 56 11:16:40
     IMP_EDR-1251639635-REGULAR-0173070007 1251639635 SOL 56 11:16:47
     IMP_EDR-1251639651-REGULAR-0173070009 1251639651 SOL 56 11:17:02
     IMP_EDR-1251639657-REGULAR-0173070011 1251639657 SOL 56 11:17:08
     IMP_EDR-1251639664-REGULAR-0173070013 1251639664 SOL 56 11:17:15
     IMP_EDR-1251639676-REGULAR-0173070015 1251639676 SOL 56 11:17:26
     IMP_EDR-1251639683-REGULAR-0173070017 1251639683 SOL 56 11:17:33
     IMP_EDR-1251639689-REGULAR-0173070019 1251639689 SOL 56 11:17:39
     IMP_EDR-1251639705-REGULAR-0173070021 1251639705 SOL 56 11:17:55
     IMP_EDR-1251639712-REGULAR-0173070023 1251639712 SOL 56 11:18:01
     IMP_EDR-1251639718-REGULAR-0173070025 1251639718 SOL 56 11:18:07
     IMP_EDR-1251641371-REGULAR-0173070003 1251641371 SOL 56 11:44:56
     IMP_EDR-1251641378-REGULAR-0173070005 1251641378 SOL 56 11:45:03
     IMP_EDR-1251641385-REGULAR-0173070007 1251641385 SOL 56 11:45:10
     IMP_EDR-1251641400-REGULAR-0173070009 1251641400 SOL 56 11:45:24
     IMP_EDR-1251641407-REGULAR-0173070011 1251641407 SOL 56 11:45:31
     IMP_EDR-1251641414-REGULAR-0173070013 1251641414 SOL 56 11:45:38
     IMP_EDR-1251641426-REGULAR-0173070015 1251641426 SOL 56 11:45:50
     IMP_EDR-1251641434-REGULAR-0173070017 1251641434 SOL 56 11:45:58
     IMP_EDR-1251641441-REGULAR-0173070019 1251641441 SOL 56 11:46:04
     IMP_EDR-1251641458-REGULAR-0173070021 1251641458 SOL 56 11:46:21
     IMP_EDR-1251641466-REGULAR-0173070023 1251641466 SOL 56 11:46:29
     IMP_EDR-1251641472-REGULAR-0173070025 1251641472 SOL 56 11:46:35
     IMP_EDR-1251644844-REGULAR-0173070003 1251644844 SOL 56 12:41:17
     IMP_EDR-1251644851-REGULAR-0173070005 1251644851 SOL 56 12:41:23
     IMP_EDR-1251644857-REGULAR-0173070007 1251644857 SOL 56 12:41:29
     IMP_EDR-1251644873-REGULAR-0173070009 1251644873 SOL 56 12:41:45
     IMP_EDR-1251644880-REGULAR-0173070011 1251644880 SOL 56 12:41:52
     IMP_EDR-1251644887-REGULAR-0173070013 1251644887 SOL 56 12:41:58
     IMP_EDR-1251644898-REGULAR-0173070015 1251644898 SOL 56 12:42:09
     IMP_EDR-1251644905-REGULAR-0173070017 1251644905 SOL 56 12:42:16
     IMP_EDR-1251644912-REGULAR-0173070019 1251644912 SOL 56 12:42:23
     IMP_EDR-1251644927-REGULAR-0173070021 1251644927 SOL 56 12:42:37
     IMP_EDR-1251644934-REGULAR-0173070023 1251644934 SOL 56 12:42:44
     IMP_EDR-1251644941-REGULAR-0173070025 1251644941 SOL 56 12:42:51
     IMP_EDR-1251816822-REGULAR-0173070003 1251816822 SOL 58 11:10:51
     IMP_EDR-1251816829-REGULAR-0173070005 1251816829 SOL 58 11:10:58
     IMP_EDR-1251816835-REGULAR-0173070007 1251816835 SOL 58 11:11:04
     IMP_EDR-1251816851-REGULAR-0173070009 1251816851 SOL 58 11:11:19
     IMP_EDR-1251816858-REGULAR-0173070011 1251816858 SOL 58 11:11:26
     IMP_EDR-1251816864-REGULAR-0173070013 1251816864 SOL 58 11:11:32
     IMP_EDR-1251816876-REGULAR-0173070015 1251816876 SOL 58 11:11:43
     IMP_EDR-1251816883-REGULAR-0173070017 1251816883 SOL 58 11:11:50
     IMP_EDR-1251816889-REGULAR-0173070019 1251816889 SOL 58 11:11:56
     IMP_EDR-1251816905-REGULAR-0173070021 1251816905 SOL 58 11:12:12
     IMP_EDR-1251816912-REGULAR-0173070023 1251816912 SOL 58 11:12:18
     IMP_EDR-1251816918-REGULAR-0173070025 1251816918 SOL 58 11:12:24
     IMP_EDR-1251996545-REGULAR-0173070003 1251996545 SOL 60 11:46:09
     IMP_EDR-1251996552-REGULAR-0173070005 1251996552 SOL 60 11:46:16
     IMP_EDR-1251996559-REGULAR-0173070007 1251996559 SOL 60 11:46:23
     IMP_EDR-1251996575-REGULAR-0173070009 1251996575 SOL 60 11:46:39
     IMP_EDR-1251996581-REGULAR-0173070011 1251996581 SOL 60 11:46:44
     IMP_EDR-1251996588-REGULAR-0173070013 1251996588 SOL 60 11:46:51
     IMP_EDR-1251996600-REGULAR-0173070015 1251996600 SOL 60 11:47:03
     IMP_EDR-1252085328-REGULAR-0173070003 1252085328 SOL 61 11:46:12
     IMP_EDR-1252085335-REGULAR-0173070005 1252085335 SOL 61 11:46:18
     IMP_EDR-1252085342-REGULAR-0173070007 1252085342 SOL 61 11:46:25
     IMP_EDR-1252085358-REGULAR-0173070009 1252085358 SOL 61 11:46:40
     IMP_EDR-1252085364-REGULAR-0173070011 1252085364 SOL 61 11:46:46
     IMP_EDR-1252085371-REGULAR-0173070013 1252085371 SOL 61 11:46:53
     IMP_EDR-1252085383-REGULAR-0173070015 1252085383 SOL 61 11:47:05
     IMP_EDR-1252085389-REGULAR-0173070017 1252085389 SOL 61 11:47:10
     IMP_EDR-1252085396-REGULAR-0173070019 1252085396 SOL 61 11:47:17
     IMP_EDR-1252085412-REGULAR-0173070021 1252085412 SOL 61 11:47:33
     IMP_EDR-1252085419-REGULAR-0173070023 1252085419 SOL 61 11:47:39
     IMP_EDR-1252085425-REGULAR-0173070025 1252085425 SOL 61 11:47:45
     IMP_EDR-1252086622-REGULAR-0173070003 1252086622 SOL 61 12:07:06
     IMP_EDR-1252086629-REGULAR-0173070005 1252086629 SOL 61 12:07:13
     IMP_EDR-1252086636-REGULAR-0173070007 1252086636 SOL 61 12:07:20
     IMP_EDR-1252086652-REGULAR-0173070009 1252086652 SOL 61 12:07:35
     IMP_EDR-1252086658-REGULAR-0173070011 1252086658 SOL 61 12:07:41
     IMP_EDR-1252086665-REGULAR-0173070013 1252086665 SOL 61 12:07:48
     IMP_EDR-1252086677-REGULAR-0173070015 1252086677 SOL 61 12:08:00
     IMP_EDR-1252086684-REGULAR-0173070017 1252086684 SOL 61 12:08:06
     IMP_EDR-1252086691-REGULAR-0173070019 1252086691 SOL 61 12:08:13
     IMP_EDR-1252086706-REGULAR-0173070021 1252086706 SOL 61 12:08:28
     IMP_EDR-1252086713-REGULAR-0173070023 1252086713 SOL 61 12:08:35
     IMP_EDR-1252086720-REGULAR-0173070025 1252086720 SOL 61 12:08:41
     IMP_EDR-1252172465-REGULAR-0173070003 1252172465 SOL 62 11:19:37
     IMP_EDR-1252172472-REGULAR-0173070005 1252172472 SOL 62 11:19:44
     IMP_EDR-1252172478-REGULAR-0173070007 1252172478 SOL 62 11:19:50
     IMP_EDR-1252172493-REGULAR-0173070009 1252172493 SOL 62 11:20:05
     IMP_EDR-1252172517-REGULAR-0173070015 1252172517 SOL 62 11:20:28
     IMP_EDR-1252172524-REGULAR-0173070017 1252172524 SOL 62 11:20:35
     IMP_EDR-1252172530-REGULAR-0173070019 1252172530 SOL 62 11:20:41
     IMP_EDR-1252172545-REGULAR-0173070021 1252172545 SOL 62 11:20:55
     IMP_EDR-1252172552-REGULAR-0173070023 1252172552 SOL 62 11:21:02
     IMP_EDR-1252172558-REGULAR-0173070025 1252172558 SOL 62 11:21:08
     IMP_EDR-1252175373-REGULAR-0173070003 1252175373 SOL 62 12:06:48
     IMP_EDR-1252175380-REGULAR-0173070005 1252175380 SOL 62 12:06:54
     IMP_EDR-1252175387-REGULAR-0173070007 1252175387 SOL 62 12:07:01
     IMP_EDR-1252175403-REGULAR-0173070009 1252175403 SOL 62 12:07:17
     IMP_EDR-1252175409-REGULAR-0173070011 1252175409 SOL 62 12:07:23
     IMP_EDR-1252175416-REGULAR-0173070013 1252175416 SOL 62 12:07:29
     IMP_EDR-1252175428-REGULAR-0173070015 1252175428 SOL 62 12:07:41
     IMP_EDR-1252175435-REGULAR-0173070017 1252175435 SOL 62 12:07:48
     IMP_EDR-1252175442-REGULAR-0173070019 1252175442 SOL 62 12:07:55
     IMP_EDR-1252175457-REGULAR-0173070021 1252175457 SOL 62 12:08:09
     IMP_EDR-1252175464-REGULAR-0173070023 1252175464 SOL 62 12:08:16
     IMP_EDR-1252175470-REGULAR-0173070025 1252175470 SOL 62 12:08:22
     IMP_EDR-1252260447-REGULAR-0173070003 1252260447 SOL 63 11:06:43
     IMP_EDR-1252260453-REGULAR-0173070005 1252260453 SOL 63 11:06:49
     IMP_EDR-1252260460-REGULAR-0173070007 1252260460 SOL 63 11:06:55
     IMP_EDR-1252260476-REGULAR-0173070009 1252260476 SOL 63 11:07:11
     IMP_EDR-1252260482-REGULAR-0173070011 1252260482 SOL 63 11:07:17
     IMP_EDR-1252260501-REGULAR-0173070015 1252260501 SOL 63 11:07:35
     IMP_EDR-1252260507-REGULAR-0173070017 1252260507 SOL 63 11:07:41
     IMP_EDR-1252260514-REGULAR-0173070019 1252260514 SOL 63 11:07:48
     IMP_EDR-1252260530-REGULAR-0173070021 1252260530 SOL 63 11:08:04
     IMP_EDR-1252260536-REGULAR-0173070023 1252260536 SOL 63 11:08:09
     IMP_EDR-1252260543-REGULAR-0173070025 1252260543 SOL 63 11:08:16
     IMP_EDR-1252262885-REGULAR-0173070003 1252262885 SOL 63 11:46:07
     IMP_EDR-1252262891-REGULAR-0173070005 1252262891 SOL 63 11:46:13
     IMP_EDR-1252440262-REGULAR-0173070003 1252440262 SOL 65 11:43:12
     IMP_EDR-1252440269-REGULAR-0173070005 1252440269 SOL 65 11:43:19
     IMP_EDR-1252440275-REGULAR-0173070007 1252440275 SOL 65 11:43:25
     IMP_EDR-1252440291-REGULAR-0173070009 1252440291 SOL 65 11:43:41
     IMP_EDR-1252440298-REGULAR-0173070011 1252440298 SOL 65 11:43:47
     IMP_EDR-1252440304-REGULAR-0173070013 1252440304 SOL 65 11:43:53
     IMP_EDR-1252440316-REGULAR-0173070015 1252440316 SOL 65 11:44:05
     IMP_EDR-1252440323-REGULAR-0173070017 1252440323 SOL 65 11:44:12
     IMP_EDR-1252440330-REGULAR-0173070019 1252440330 SOL 65 11:44:19
     IMP_EDR-1252440345-REGULAR-0173070021 1252440345 SOL 65 11:44:33
     IMP_EDR-1252440352-REGULAR-0173070023 1252440352 SOL 65 11:44:40
     IMP_EDR-1252440358-REGULAR-0173070025 1252440358 SOL 65 11:44:46
     IMP_EDR-1252441504-REGULAR-0173070003 1252441504 SOL 65 12:03:21
     IMP_EDR-1252441511-REGULAR-0173070005 1252441511 SOL 65 12:03:28
     IMP_EDR-1252441518-REGULAR-0173070007 1252441518 SOL 65 12:03:35
     IMP_EDR-1252441534-REGULAR-0173070009 1252441534 SOL 65 12:03:50
     IMP_EDR-1252441541-REGULAR-0173070011 1252441541 SOL 65 12:03:57
     IMP_EDR-1252441548-REGULAR-0173070013 1252441548 SOL 65 12:04:04
     IMP_EDR-1252441559-REGULAR-0173070015 1252441559 SOL 65 12:04:15
     IMP_EDR-1252441566-REGULAR-0173070017 1252441566 SOL 65 12:04:22
     IMP_EDR-1252441573-REGULAR-0173070019 1252441573 SOL 65 12:04:28
     IMP_EDR-1252441589-REGULAR-0173070021 1252441589 SOL 65 12:04:44
     IMP_EDR-1252441595-REGULAR-0173070023 1252441595 SOL 65 12:04:50
     IMP_EDR-1252441602-REGULAR-0173070025 1252441602 SOL 65 12:04:57
     IMP_EDR-1252529044-REGULAR-0173070003 1252529044 SOL 66 11:43:15
     IMP_EDR-1252529052-REGULAR-0173070005 1252529052 SOL 66 11:43:23
     IMP_EDR-1252529060-REGULAR-0173070007 1252529060 SOL 66 11:43:31
     IMP_EDR-1252529077-REGULAR-0173070009 1252529077 SOL 66 11:43:47
     IMP_EDR-1252529084-REGULAR-0173070011 1252529084 SOL 66 11:43:54
     IMP_EDR-1252529090-REGULAR-0173070013 1252529090 SOL 66 11:44:00
     IMP_EDR-1252529102-REGULAR-0173070015 1252529102 SOL 66 11:44:12
     IMP_EDR-1252529109-REGULAR-0173070017 1252529109 SOL 66 11:44:18
     IMP_EDR-1252529116-REGULAR-0173070019 1252529116 SOL 66 11:44:25
     IMP_EDR-1252529132-REGULAR-0173070021 1252529132 SOL 66 11:44:41
     IMP_EDR-1252529140-REGULAR-0173070023 1252529140 SOL 66 11:44:49
     IMP_EDR-1252529147-REGULAR-0173070025 1252529147 SOL 66 11:44:55
     IMP_EDR-1252530287-REGULAR-0173070003 1252530287 SOL 66 12:03:25
     IMP_EDR-1252530293-REGULAR-0173070005 1252530293 SOL 66 12:03:31
     IMP_EDR-1252530300-REGULAR-0173070007 1252530300 SOL 66 12:03:38
     IMP_EDR-1252530316-REGULAR-0173070009 1252530316 SOL 66 12:03:53
     IMP_EDR-1252530323-REGULAR-0173070011 1252530323 SOL 66 12:04:00
     IMP_EDR-1252530329-REGULAR-0173070013 1252530329 SOL 66 12:04:06
     IMP_EDR-1252530341-REGULAR-0173070015 1252530341 SOL 66 12:04:18
     IMP_EDR-1252530348-REGULAR-0173070017 1252530348 SOL 66 12:04:24
     IMP_EDR-1252530355-REGULAR-0173070019 1252530355 SOL 66 12:04:31
     IMP_EDR-1252530370-REGULAR-0173070021 1252530370 SOL 66 12:04:46
     IMP_EDR-1252530377-REGULAR-0173070023 1252530377 SOL 66 12:04:53
     IMP_EDR-1252530384-REGULAR-0173070025 1252530384 SOL 66 12:04:59
     IMP_EDR-1252617824-REGULAR-0173070003 1252617824 SOL 67 11:43:17
     IMP_EDR-1252617831-REGULAR-0173070005 1252617831 SOL 67 11:43:24
     IMP_EDR-1252617837-REGULAR-0173070007 1252617837 SOL 67 11:43:29
     IMP_EDR-1252617853-REGULAR-0173070009 1252617853 SOL 67 11:43:45
     IMP_EDR-1252617860-REGULAR-0173070011 1252617860 SOL 67 11:43:52
     IMP_EDR-1252617866-REGULAR-0173070013 1252617866 SOL 67 11:43:58
     IMP_EDR-1252617878-REGULAR-0173070015 1252617878 SOL 67 11:44:09
     IMP_EDR-1252617885-REGULAR-0173070017 1252617885 SOL 67 11:44:16
     IMP_EDR-1252617892-REGULAR-0173070019 1252617892 SOL 67 11:44:23
     IMP_EDR-1252617907-REGULAR-0173070021 1252617907 SOL 67 11:44:37
     IMP_EDR-1252617914-REGULAR-0173070023 1252617914 SOL 67 11:44:44
     IMP_EDR-1252617921-REGULAR-0173070025 1252617921 SOL 67 11:44:51
     IMP_EDR-1252619068-REGULAR-0173070003 1252619068 SOL 67 12:03:27
     IMP_EDR-1252619075-REGULAR-0173070005 1252619075 SOL 67 12:03:34
     IMP_EDR-1252619082-REGULAR-0173070007 1252619082 SOL 67 12:03:41
     IMP_EDR-1252619098-REGULAR-0173070009 1252619098 SOL 67 12:03:57
     IMP_EDR-1252619104-REGULAR-0173070011 1252619104 SOL 67 12:04:03
     IMP_EDR-1252619111-REGULAR-0173070013 1252619111 SOL 67 12:04:09
     IMP_EDR-1252619123-REGULAR-0173070015 1252619123 SOL 67 12:04:21
     IMP_EDR-1252619130-REGULAR-0173070017 1252619130 SOL 67 12:04:28
     IMP_EDR-1252619136-REGULAR-0173070019 1252619136 SOL 67 12:04:34
     IMP_EDR-1252619152-REGULAR-0173070021 1252619152 SOL 67 12:04:49
     IMP_EDR-1252619159-REGULAR-0173070023 1252619159 SOL 67 12:04:56
     IMP_EDR-1252619165-REGULAR-0173070025 1252619165 SOL 67 12:05:02
     IMP_EDR-1252706642-REGULAR-0173070003 1252706642 SOL 68 11:43:55
     IMP_EDR-1252706649-REGULAR-0173070005 1252706649 SOL 68 11:44:02
     IMP_EDR-1252706655-REGULAR-0173070007 1252706655 SOL 68 11:44:08
     IMP_EDR-1252706671-REGULAR-0173070009 1252706671 SOL 68 11:44:23
     IMP_EDR-1252706678-REGULAR-0173070011 1252706678 SOL 68 11:44:30
     IMP_EDR-1252706684-REGULAR-0173070013 1252706684 SOL 68 11:44:36
     IMP_EDR-1252706696-REGULAR-0173070015 1252706696 SOL 68 11:44:48
     IMP_EDR-1252706703-REGULAR-0173070017 1252706703 SOL 68 11:44:54
     IMP_EDR-1252706710-REGULAR-0173070019 1252706710 SOL 68 11:45:01
     IMP_EDR-1252706725-REGULAR-0173070021 1252706725 SOL 68 11:45:16
     IMP_EDR-1252706732-REGULAR-0173070023 1252706732 SOL 68 11:45:23
     IMP_EDR-1252706739-REGULAR-0173070025 1252706739 SOL 68 11:45:29
     IMP_EDR-1252707543-REGULAR-0173070003 1252707543 SOL 68 11:58:32
     IMP_EDR-1252707550-REGULAR-0173070005 1252707550 SOL 68 11:58:39
     IMP_EDR-1252707557-REGULAR-0173070007 1252707557 SOL 68 11:58:46
     IMP_EDR-1252707572-REGULAR-0173070009 1252707572 SOL 68 11:59:00
     IMP_EDR-1252707579-REGULAR-0173070011 1252707579 SOL 68 11:59:07
     IMP_EDR-1252707586-REGULAR-0173070013 1252707586 SOL 68 11:59:14
     IMP_EDR-1252707598-REGULAR-0173070015 1252707598 SOL 68 11:59:25
     IMP_EDR-1252707604-REGULAR-0173070017 1252707604 SOL 68 11:59:31
     IMP_EDR-1252707611-REGULAR-0173070019 1252707611 SOL 68 11:59:38
     IMP_EDR-1252707627-REGULAR-0173070021 1252707627 SOL 68 11:59:54
     IMP_EDR-1252707634-REGULAR-0173070023 1252707634 SOL 68 12:00:01
     IMP_EDR-1252707640-REGULAR-0173070025 1252707640 SOL 68 12:00:06
     IMP_EDR-1252795455-REGULAR-0173070003 1252795455 SOL 69 11:44:36
     IMP_EDR-1252795462-REGULAR-0173070005 1252795462 SOL 69 11:44:42
     IMP_EDR-1252795469-REGULAR-0173070007 1252795469 SOL 69 11:44:49
     IMP_EDR-1252795484-REGULAR-0173070009 1252795484 SOL 69 11:45:04
     IMP_EDR-1252795491-REGULAR-0173070011 1252795491 SOL 69 11:45:11
     IMP_EDR-1252795498-REGULAR-0173070013 1252795498 SOL 69 11:45:17
     IMP_EDR-1252795509-REGULAR-0173070015 1252795509 SOL 69 11:45:28
     IMP_EDR-1252795516-REGULAR-0173070017 1252795516 SOL 69 11:45:35
     IMP_EDR-1252795523-REGULAR-0173070019 1252795523 SOL 69 11:45:42
     IMP_EDR-1252795539-REGULAR-0173070021 1252795539 SOL 69 11:45:57
     IMP_EDR-1252795545-REGULAR-0173070023 1252795545 SOL 69 11:46:03
     IMP_EDR-1252795552-REGULAR-0173070025 1252795552 SOL 69 11:46:10
     IMP_EDR-1252796698-REGULAR-0173070003 1252796698 SOL 69 12:04:45
     IMP_EDR-1252796705-REGULAR-0173070005 1252796705 SOL 69 12:04:52
     IMP_EDR-1252796711-REGULAR-0173070007 1252796711 SOL 69 12:04:58
     IMP_EDR-1252796727-REGULAR-0173070009 1252796727 SOL 69 12:05:14
     IMP_EDR-1252796734-REGULAR-0173070011 1252796734 SOL 69 12:05:20
     IMP_EDR-1252796740-REGULAR-0173070013 1252796740 SOL 69 12:05:26
     IMP_EDR-1252796752-REGULAR-0173070015 1252796752 SOL 69 12:05:38
     IMP_EDR-1252796759-REGULAR-0173070017 1252796759 SOL 69 12:05:45
     IMP_EDR-1252796766-REGULAR-0173070019 1252796766 SOL 69 12:05:52
     IMP_EDR-1252796781-REGULAR-0173070021 1252796781 SOL 69 12:06:06
     IMP_EDR-1252796788-REGULAR-0173070023 1252796788 SOL 69 12:06:13
     IMP_EDR-1252796795-REGULAR-0173070025 1252796795 SOL 69 12:06:20
     IMP_EDR-1252884177-REGULAR-0173070003 1252884177 SOL 70 11:43:41
     IMP_EDR-1252884184-REGULAR-0173070005 1252884184 SOL 70 11:43:48
     IMP_EDR-1252884192-REGULAR-0173070007 1252884192 SOL 70 11:43:55
     IMP_EDR-1252884209-REGULAR-0173070009 1252884209 SOL 70 11:44:12
     IMP_EDR-1252884217-REGULAR-0173070011 1252884217 SOL 70 11:44:20
     IMP_EDR-1252884224-REGULAR-0173070013 1252884224 SOL 70 11:44:27
     IMP_EDR-1252884237-REGULAR-0173070015 1252884237 SOL 70 11:44:39
     IMP_EDR-1252884244-REGULAR-0173070017 1252884244 SOL 70 11:44:46
     IMP_EDR-1252884252-REGULAR-0173070019 1252884252 SOL 70 11:44:54
     IMP_EDR-1252884269-REGULAR-0173070021 1252884269 SOL 70 11:45:10
     IMP_EDR-1252884277-REGULAR-0173070023 1252884277 SOL 70 11:45:18
     IMP_EDR-1252884284-REGULAR-0173070025 1252884284 SOL 70 11:45:25
     IMP_EDR-1252885417-REGULAR-0173070003 1252885417 SOL 70 12:03:48
     IMP_EDR-1252885424-REGULAR-0173070005 1252885424 SOL 70 12:03:55
     IMP_EDR-1252885431-REGULAR-0173070007 1252885431 SOL 70 12:04:01
     IMP_EDR-1252885446-REGULAR-0173070009 1252885446 SOL 70 12:04:16
     IMP_EDR-1252885453-REGULAR-0173070011 1252885453 SOL 70 12:04:23
     IMP_EDR-1252885460-REGULAR-0173070013 1252885460 SOL 70 12:04:30
     IMP_EDR-1252885471-REGULAR-0173070015 1252885471 SOL 70 12:04:40
     IMP_EDR-1252885478-REGULAR-0173070017 1252885478 SOL 70 12:04:47
     IMP_EDR-1252885485-REGULAR-0173070019 1252885485 SOL 70 12:04:54
     IMP_EDR-1252885497-REGULAR-0173070021 1252885497 SOL 70 12:05:06
     IMP_EDR-1252885504-REGULAR-0173070023 1252885504 SOL 70 12:05:12
     IMP_EDR-1252885511-REGULAR-0173070025 1252885511 SOL 70 12:05:19
     IMP_EDR-1253061894-REGULAR-0173070003 1253061894 SOL 72 11:46:15
     IMP_EDR-1253061901-REGULAR-0173070005 1253061901 SOL 72 11:46:21
     IMP_EDR-1253061908-REGULAR-0173070007 1253061908 SOL 72 11:46:28
     IMP_EDR-1253061924-REGULAR-0173070009 1253061924 SOL 72 11:46:44
     IMP_EDR-1253061930-REGULAR-0173070011 1253061930 SOL 72 11:46:50
     IMP_EDR-1253061937-REGULAR-0173070013 1253061937 SOL 72 11:46:56
     IMP_EDR-1253061949-REGULAR-0173070015 1253061949 SOL 72 11:47:08
     IMP_EDR-1253061956-REGULAR-0173070017 1253061956 SOL 72 11:47:15
     IMP_EDR-1253061963-REGULAR-0173070019 1253061963 SOL 72 11:47:22
     IMP_EDR-1253061978-REGULAR-0173070021 1253061978 SOL 72 11:47:36
     IMP_EDR-1253061985-REGULAR-0173070023 1253061985 SOL 72 11:47:43
     IMP_EDR-1253061991-REGULAR-0173070025 1253061991 SOL 72 11:47:49
     IMP_EDR-1253063137-REGULAR-0173070003 1253063137 SOL 72 12:06:24
     IMP_EDR-1253063145-REGULAR-0173070005 1253063145 SOL 72 12:06:32
     IMP_EDR-1253063152-REGULAR-0173070007 1253063152 SOL 72 12:06:39
     IMP_EDR-1253063169-REGULAR-0173070009 1253063169 SOL 72 12:06:56
     IMP_EDR-1253063176-REGULAR-0173070011 1253063176 SOL 72 12:07:02
     IMP_EDR-1253063183-REGULAR-0173070013 1253063183 SOL 72 12:07:09
     IMP_EDR-1253063195-REGULAR-0173070015 1253063195 SOL 72 12:07:21
     IMP_EDR-1253063203-REGULAR-0173070017 1253063203 SOL 72 12:07:29
     IMP_EDR-1253063210-REGULAR-0173070019 1253063210 SOL 72 12:07:35
     IMP_EDR-1253063227-REGULAR-0173070021 1253063227 SOL 72 12:07:52
     IMP_EDR-1253063234-REGULAR-0173070023 1253063234 SOL 72 12:07:59
     IMP_EDR-1253063240-REGULAR-0173070025 1253063240 SOL 72 12:08:05
     IMP_EDR-1253328236-REGULAR-0173070003 1253328236 SOL 75 11:46:15
     IMP_EDR-1253328243-REGULAR-0173070005 1253328243 SOL 75 11:46:22
     IMP_EDR-1253328249-REGULAR-0173070007 1253328249 SOL 75 11:46:28
     IMP_EDR-1253328265-REGULAR-0173070009 1253328265 SOL 75 11:46:43
     IMP_EDR-1253328272-REGULAR-0173070011 1253328272 SOL 75 11:46:50
     IMP_EDR-1253500702-REGULAR-0173070015 1253500702 SOL 77 10:23:36
     IMP_EDR-1253500708-REGULAR-0173070017 1253500708 SOL 77 10:23:42
     IMP_EDR-1253500715-REGULAR-0173070019 1253500715 SOL 77 10:23:49
     IMP_EDR-1253501604-REGULAR-0173070011 1253501604 SOL 77 10:38:14
     IMP_EDR-1253501610-REGULAR-0173070013 1253501610 SOL 77 10:38:20
     IMP_EDR-1253501622-REGULAR-0173070015 1253501622 SOL 77 10:38:31
     IMP_EDR-1253501665-REGULAR-0173070025 1253501665 SOL 77 10:39:13
     IMP_EDR-1253949684-REGULAR-0173070003 1253949684 SOL 82 11:46:01
     IMP_EDR-1253949691-REGULAR-0173070005 1253949691 SOL 82 11:46:07
     IMP_EDR-1253949697-REGULAR-0173070007 1253949697 SOL 82 11:46:13
     IMP_EDR-1253949713-REGULAR-0173070009 1253949713 SOL 82 11:46:29
     IMP_EDR-1253949720-REGULAR-0173070011 1253949720 SOL 82 11:46:36
     IMP_EDR-1253949726-REGULAR-0173070013 1253949726 SOL 82 11:46:41
     IMP_EDR-1253949738-REGULAR-0173070015 1253949738 SOL 82 11:46:53
     IMP_EDR-1253949745-REGULAR-0173070017 1253949745 SOL 82 11:47:00
     IMP_EDR-1253949752-REGULAR-0173070019 1253949752 SOL 82 11:47:07
     IMP_EDR-1253949767-REGULAR-0173070021 1253949767 SOL 82 11:47:21
     IMP_EDR-1253949774-REGULAR-0173070023 1253949774 SOL 82 11:47:28
     IMP_EDR-1253949781-REGULAR-0173070025 1253949781 SOL 82 11:47:35
 
    IMP SEQUENCE S0174
                   PRODUCT_ID                 SCLK          LST
     IMP_EDR-1246849948-REGULAR-0174010003 1246849948 SOL 2 12:19:26
     IMP_EDR-1246849955-REGULAR-0174010005 1246849955 SOL 2 12:19:33
     IMP_EDR-1246849962-REGULAR-0174010007 1246849962 SOL 2 12:19:40
 
    IMP SEQUENCE S0175
                   PRODUCT_ID                 SCLK          LST
     IMP_EDR-1246933297-REGULAR-0175020003 1246933297 SOL 3 10:51:34
     IMP_EDR-1246933304-REGULAR-0175020005 1246933304 SOL 3 10:51:41
     IMP_EDR-1246933311-REGULAR-0175020007 1246933311 SOL 3 10:51:48
     IMP_EDR-1246940282-REGULAR-0175020003 1246940282 SOL 3 12:44:53
     IMP_EDR-1246940288-REGULAR-0175020005 1246940288 SOL 3 12:44:59
     IMP_EDR-1246940295-REGULAR-0175020007 1246940295 SOL 3 12:45:06
     IMP_EDR-1247547207-REGULAR-0175020003 1247547207 SOL 10 08:50:47
     IMP_EDR-1247547213-REGULAR-0175020005 1247547213 SOL 10 08:50:53
     IMP_EDR-1247547220-REGULAR-0175020007 1247547220 SOL 10 08:51:00
     IMP_EDR-1247551234-REGULAR-0175020003 1247551234 SOL 10 09:56:07
     IMP_EDR-1247551241-REGULAR-0175020005 1247551241 SOL 10 09:56:13
     IMP_EDR-1247551247-REGULAR-0175020007 1247551247 SOL 10 09:56:19
     IMP_EDR-1247644526-REGULAR-0175020003 1247644526 SOL 11 11:09:33
     IMP_EDR-1247644533-REGULAR-0175020005 1247644533 SOL 11 11:09:40
     IMP_EDR-1247644540-REGULAR-0175020007 1247644540 SOL 11 11:09:46
     IMP_EDR-1247724767-REGULAR-0175030003 1247724767 SOL 12 08:51:16
     IMP_EDR-1247724774-REGULAR-0175030005 1247724774 SOL 12 08:51:23
     IMP_EDR-1247724780-REGULAR-0175030007 1247724780 SOL 12 08:51:28
     IMP_EDR-1247724787-REGULAR-0175030009 1247724787 SOL 12 08:51:35
     IMP_EDR-1247724793-REGULAR-0175030011 1247724793 SOL 12 08:51:41
     IMP_EDR-1247724800-REGULAR-0175030013 1247724800 SOL 12 08:51:48
     IMP_EDR-1247724806-REGULAR-0175030015 1247724806 SOL 12 08:51:54
     IMP_EDR-1247724813-REGULAR-0175030017 1247724813 SOL 12 08:52:01
     IMP_EDR-1247724819-REGULAR-0175030019 1247724819 SOL 12 08:52:06
     IMP_EDR-1247724826-REGULAR-0175030021 1247724826 SOL 12 08:52:13
     IMP_EDR-1247728777-REGULAR-0175030003 1247728777 SOL 12 09:56:19
     IMP_EDR-1247728783-REGULAR-0175030005 1247728783 SOL 12 09:56:25
     IMP_EDR-1247728790-REGULAR-0175030007 1247728790 SOL 12 09:56:32
     IMP_EDR-1247728796-REGULAR-0175030009 1247728796 SOL 12 09:56:37
     IMP_EDR-1247728803-REGULAR-0175030011 1247728803 SOL 12 09:56:44
     IMP_EDR-1247728809-REGULAR-0175030013 1247728809 SOL 12 09:56:50
     IMP_EDR-1247728816-REGULAR-0175030015 1247728816 SOL 12 09:56:57
     IMP_EDR-1247728822-REGULAR-0175030017 1247728822 SOL 12 09:57:03
     IMP_EDR-1247728829-REGULAR-0175030019 1247728829 SOL 12 09:57:10
     IMP_EDR-1247728835-REGULAR-0175030021 1247728835 SOL 12 09:57:15
     IMP_EDR-1247735692-REGULAR-0175030003 1247735692 SOL 12 11:48:30
     IMP_EDR-1247735699-REGULAR-0175030005 1247735699 SOL 12 11:48:36
     IMP_EDR-1247735706-REGULAR-0175030007 1247735706 SOL 12 11:48:43
     IMP_EDR-1247735713-REGULAR-0175030009 1247735713 SOL 12 11:48:50
     IMP_EDR-1247735719-REGULAR-0175030011 1247735719 SOL 12 11:48:56
     IMP_EDR-1247735726-REGULAR-0175030013 1247735726 SOL 12 11:49:03
     IMP_EDR-1247735732-REGULAR-0175030015 1247735732 SOL 12 11:49:09
     IMP_EDR-1247735739-REGULAR-0175030017 1247735739 SOL 12 11:49:15
     IMP_EDR-1247735745-REGULAR-0175030019 1247735745 SOL 12 11:49:21
     IMP_EDR-1247735752-REGULAR-0175030021 1247735752 SOL 12 11:49:28
     IMP_EDR-1247744397-REGULAR-0175030003 1247744397 SOL 12 14:09:43
     IMP_EDR-1247744404-REGULAR-0175030005 1247744404 SOL 12 14:09:50
     IMP_EDR-1247744410-REGULAR-0175030007 1247744410 SOL 12 14:09:55
     IMP_EDR-1247744417-REGULAR-0175030009 1247744417 SOL 12 14:10:02
     IMP_EDR-1247744424-REGULAR-0175030011 1247744424 SOL 12 14:10:09
     IMP_EDR-1247744430-REGULAR-0175030013 1247744430 SOL 12 14:10:15
     IMP_EDR-1247744437-REGULAR-0175030015 1247744437 SOL 12 14:10:22
     IMP_EDR-1247744443-REGULAR-0175030017 1247744443 SOL 12 14:10:27
     IMP_EDR-1247744450-REGULAR-0175030019 1247744450 SOL 12 14:10:34
     IMP_EDR-1247744456-REGULAR-0175030021 1247744456 SOL 12 14:10:40
     IMP_EDR-1247752862-REGULAR-0175030003 1247752862 SOL 12 16:27:02
     IMP_EDR-1247752869-REGULAR-0175030005 1247752869 SOL 12 16:27:09
     IMP_EDR-1247752875-REGULAR-0175030007 1247752875 SOL 12 16:27:15
     IMP_EDR-1247752881-REGULAR-0175030009 1247752881 SOL 12 16:27:21
     IMP_EDR-1247752888-REGULAR-0175030011 1247752888 SOL 12 16:27:27
     IMP_EDR-1247752894-REGULAR-0175030013 1247752894 SOL 12 16:27:33
     IMP_EDR-1247752901-REGULAR-0175030015 1247752901 SOL 12 16:27:40
     IMP_EDR-1247752908-REGULAR-0175030017 1247752908 SOL 12 16:27:47
     IMP_EDR-1247752914-REGULAR-0175030019 1247752914 SOL 12 16:27:53
     IMP_EDR-1247752920-REGULAR-0175030021 1247752920 SOL 12 16:27:59
     IMP_EDR-1247836490-REGULAR-0175040003 1247836490 SOL 13 15:03:42
     IMP_EDR-1247836496-REGULAR-0175040005 1247836496 SOL 13 15:03:48
     IMP_EDR-1247836503-REGULAR-0175040007 1247836503 SOL 13 15:03:54
     IMP_EDR-1247836509-REGULAR-0175040009 1247836509 SOL 13 15:04:00
     IMP_EDR-1247836516-REGULAR-0175040011 1247836516 SOL 13 15:04:07
     IMP_EDR-1247836522-REGULAR-0175040013 1247836522 SOL 13 15:04:13
     IMP_EDR-1247841644-REGULAR-0175040003 1247841644 SOL 13 16:27:19
     IMP_EDR-1247841650-REGULAR-0175040005 1247841650 SOL 13 16:27:24
     IMP_EDR-1247841657-REGULAR-0175040007 1247841657 SOL 13 16:27:31
     IMP_EDR-1247841663-REGULAR-0175040009 1247841663 SOL 13 16:27:37
     IMP_EDR-1247841669-REGULAR-0175040011 1247841669 SOL 13 16:27:43
     IMP_EDR-1247841675-REGULAR-0175040013 1247841675 SOL 13 16:27:49
     IMP_EDR-1247902318-REGULAR-0175040003 1247902318 SOL 14 08:51:36
     IMP_EDR-1247902324-REGULAR-0175040005 1247902324 SOL 14 08:51:42
     IMP_EDR-1247902331-REGULAR-0175040007 1247902331 SOL 14 08:51:48
     IMP_EDR-1247902337-REGULAR-0175040009 1247902337 SOL 14 08:51:54
     IMP_EDR-1247902344-REGULAR-0175040011 1247902344 SOL 14 08:52:01
     IMP_EDR-1247902350-REGULAR-0175040013 1247902350 SOL 14 08:52:07
     IMP_EDR-1247906002-REGULAR-0175040003 1247906002 SOL 14 09:51:22
     IMP_EDR-1247906009-REGULAR-0175040005 1247906009 SOL 14 09:51:28
     IMP_EDR-1247906016-REGULAR-0175040007 1247906016 SOL 14 09:51:35
     IMP_EDR-1247906022-REGULAR-0175040009 1247906022 SOL 14 09:51:41
     IMP_EDR-1247906028-REGULAR-0175040011 1247906028 SOL 14 09:51:47
     IMP_EDR-1247906035-REGULAR-0175040013 1247906035 SOL 14 09:51:54
     IMP_EDR-1247914807-REGULAR-0175040003 1247914807 SOL 14 12:14:12
     IMP_EDR-1247914813-REGULAR-0175040005 1247914813 SOL 14 12:14:18
     IMP_EDR-1247914820-REGULAR-0175040007 1247914820 SOL 14 12:14:25
     IMP_EDR-1247914826-REGULAR-0175040009 1247914826 SOL 14 12:14:31
     IMP_EDR-1247914833-REGULAR-0175040011 1247914833 SOL 14 12:14:37
     IMP_EDR-1247914840-REGULAR-0175040013 1247914840 SOL 14 12:14:44
     IMP_EDR-1247921537-REGULAR-0175040003 1247921537 SOL 14 14:03:23
     IMP_EDR-1247921543-REGULAR-0175040005 1247921543 SOL 14 14:03:29
     IMP_EDR-1247921550-REGULAR-0175040007 1247921550 SOL 14 14:03:35
     IMP_EDR-1247921556-REGULAR-0175040009 1247921556 SOL 14 14:03:41
     IMP_EDR-1247921562-REGULAR-0175040011 1247921562 SOL 14 14:03:47
     IMP_EDR-1247921568-REGULAR-0175040013 1247921568 SOL 14 14:03:53
     IMP_EDR-1247930684-REGULAR-0175040003 1247930684 SOL 14 16:31:46
     IMP_EDR-1247930690-REGULAR-0175040005 1247930690 SOL 14 16:31:52
     IMP_EDR-1247930696-REGULAR-0175040007 1247930696 SOL 14 16:31:58
     IMP_EDR-1247930703-REGULAR-0175040009 1247930703 SOL 14 16:32:04
     IMP_EDR-1247930709-REGULAR-0175040011 1247930709 SOL 14 16:32:10
     IMP_EDR-1247930715-REGULAR-0175040013 1247930715 SOL 14 16:32:16
     IMP_EDR-1247991093-REGULAR-0175040003 1247991093 SOL 15 08:51:45
     IMP_EDR-1247991100-REGULAR-0175040005 1247991100 SOL 15 08:51:52
     IMP_EDR-1247991106-REGULAR-0175040007 1247991106 SOL 15 08:51:58
     IMP_EDR-1247991113-REGULAR-0175040009 1247991113 SOL 15 08:52:05
     IMP_EDR-1247991119-REGULAR-0175040011 1247991119 SOL 15 08:52:11
     IMP_EDR-1247991125-REGULAR-0175040013 1247991125 SOL 15 08:52:16
     IMP_EDR-1247994772-REGULAR-0175040003 1247994772 SOL 15 09:51:26
     IMP_EDR-1247994779-REGULAR-0175040005 1247994779 SOL 15 09:51:33
     IMP_EDR-1247994787-REGULAR-0175040007 1247994787 SOL 15 09:51:41
     IMP_EDR-1247994793-REGULAR-0175040009 1247994793 SOL 15 09:51:47
     IMP_EDR-1247994799-REGULAR-0175040011 1247994799 SOL 15 09:51:53
     IMP_EDR-1247994806-REGULAR-0175040013 1247994806 SOL 15 09:51:59
     IMP_EDR-1248002793-REGULAR-0175040003 1248002793 SOL 15 12:01:34
     IMP_EDR-1248002800-REGULAR-0175040005 1248002800 SOL 15 12:01:40
     IMP_EDR-1248002806-REGULAR-0175040007 1248002806 SOL 15 12:01:46
     IMP_EDR-1248002813-REGULAR-0175040009 1248002813 SOL 15 12:01:53
     IMP_EDR-1248002819-REGULAR-0175040011 1248002819 SOL 15 12:01:59
     IMP_EDR-1248002826-REGULAR-0175040013 1248002826 SOL 15 12:02:06
     IMP_EDR-1248010316-REGULAR-0175040003 1248010316 SOL 15 14:03:36
     IMP_EDR-1248010322-REGULAR-0175040005 1248010322 SOL 15 14:03:42
     IMP_EDR-1248010329-REGULAR-0175040007 1248010329 SOL 15 14:03:49
     IMP_EDR-1248010335-REGULAR-0175040009 1248010335 SOL 15 14:03:55
     IMP_EDR-1248010342-REGULAR-0175040011 1248010342 SOL 15 14:04:01
     IMP_EDR-1248010348-REGULAR-0175040013 1248010348 SOL 15 14:04:07
     IMP_EDR-1248019458-REGULAR-0175040003 1248019458 SOL 15 16:31:55
     IMP_EDR-1248019464-REGULAR-0175040005 1248019464 SOL 15 16:32:00
     IMP_EDR-1248019471-REGULAR-0175040007 1248019471 SOL 15 16:32:07
     IMP_EDR-1248019477-REGULAR-0175040009 1248019477 SOL 15 16:32:13
     IMP_EDR-1248019483-REGULAR-0175040011 1248019483 SOL 15 16:32:19
     IMP_EDR-1248019489-REGULAR-0175040013 1248019489 SOL 15 16:32:25
     IMP_EDR-1248276661-REGULAR-0175040003 1248276661 SOL 18 14:04:24
     IMP_EDR-1248276669-REGULAR-0175040005 1248276669 SOL 18 14:04:32
     IMP_EDR-1248276675-REGULAR-0175040007 1248276675 SOL 18 14:04:38
     IMP_EDR-1248276682-REGULAR-0175040009 1248276682 SOL 18 14:04:44
     IMP_EDR-1248276689-REGULAR-0175040011 1248276689 SOL 18 14:04:51
     IMP_EDR-1248276696-REGULAR-0175040013 1248276696 SOL 18 14:04:58
     IMP_EDR-1248285807-REGULAR-0175040003 1248285807 SOL 18 16:32:46
     IMP_EDR-1248285813-REGULAR-0175040005 1248285813 SOL 18 16:32:52
     IMP_EDR-1248285820-REGULAR-0175040007 1248285820 SOL 18 16:32:59
     IMP_EDR-1248285827-REGULAR-0175040009 1248285827 SOL 18 16:33:06
     IMP_EDR-1248285833-REGULAR-0175040011 1248285833 SOL 18 16:33:12
     IMP_EDR-1248285839-REGULAR-0175040013 1248285839 SOL 18 16:33:17
     IMP_EDR-1248346194-REGULAR-0175040003 1248346194 SOL 19 08:52:24
     IMP_EDR-1248346200-REGULAR-0175040005 1248346200 SOL 19 08:52:30
     IMP_EDR-1248346207-REGULAR-0175040007 1248346207 SOL 19 08:52:37
     IMP_EDR-1248346213-REGULAR-0175040009 1248346213 SOL 19 08:52:43
     IMP_EDR-1248346220-REGULAR-0175040011 1248346220 SOL 19 08:52:49
     IMP_EDR-1248346226-REGULAR-0175040013 1248346226 SOL 19 08:52:55
     IMP_EDR-1248349890-REGULAR-0175040003 1248349890 SOL 19 09:52:22
     IMP_EDR-1248349896-REGULAR-0175040005 1248349896 SOL 19 09:52:27
     IMP_EDR-1248349903-REGULAR-0175040007 1248349903 SOL 19 09:52:34
     IMP_EDR-1248349909-REGULAR-0175040009 1248349909 SOL 19 09:52:40
     IMP_EDR-1248349916-REGULAR-0175040011 1248349916 SOL 19 09:52:47
     IMP_EDR-1248349922-REGULAR-0175040013 1248349922 SOL 19 09:52:53
     IMP_EDR-1248374559-REGULAR-0175040003 1248374559 SOL 19 16:32:33
     IMP_EDR-1248374565-REGULAR-0175040005 1248374565 SOL 19 16:32:39
     IMP_EDR-1248374571-REGULAR-0175040007 1248374571 SOL 19 16:32:45
     IMP_EDR-1248374578-REGULAR-0175040009 1248374578 SOL 19 16:32:52
     IMP_EDR-1248374584-REGULAR-0175040011 1248374584 SOL 19 16:32:58
     IMP_EDR-1248374591-REGULAR-0175040013 1248374591 SOL 19 16:33:04
     IMP_EDR-1248434969-REGULAR-0175040003 1248434969 SOL 20 08:52:33
     IMP_EDR-1248434976-REGULAR-0175040005 1248434976 SOL 20 08:52:40
     IMP_EDR-1248434982-REGULAR-0175040007 1248434982 SOL 20 08:52:46
     IMP_EDR-1248434989-REGULAR-0175040009 1248434989 SOL 20 08:52:53
     IMP_EDR-1248434995-REGULAR-0175040011 1248434995 SOL 20 08:52:59
     IMP_EDR-1248435002-REGULAR-0175040013 1248435002 SOL 20 08:53:06
     IMP_EDR-1248438647-REGULAR-0175040003 1248438647 SOL 20 09:52:13
     IMP_EDR-1248438653-REGULAR-0175040005 1248438653 SOL 20 09:52:19
     IMP_EDR-1248438660-REGULAR-0175040007 1248438660 SOL 20 09:52:26
     IMP_EDR-1248438667-REGULAR-0175040009 1248438667 SOL 20 09:52:33
     IMP_EDR-1248438673-REGULAR-0175040011 1248438673 SOL 20 09:52:39
     IMP_EDR-1248438679-REGULAR-0175040013 1248438679 SOL 20 09:52:45
     IMP_EDR-1248454227-REGULAR-0175040003 1248454227 SOL 20 14:04:58
     IMP_EDR-1248454234-REGULAR-0175040005 1248454234 SOL 20 14:05:05
     IMP_EDR-1248454240-REGULAR-0175040007 1248454240 SOL 20 14:05:11
     IMP_EDR-1248454247-REGULAR-0175040009 1248454247 SOL 20 14:05:18
     IMP_EDR-1248454253-REGULAR-0175040011 1248454253 SOL 20 14:05:24
     IMP_EDR-1248454260-REGULAR-0175040013 1248454260 SOL 20 14:05:30
     IMP_EDR-1248523758-REGULAR-0175040003 1248523758 SOL 21 08:52:56
     IMP_EDR-1248523764-REGULAR-0175040005 1248523764 SOL 21 08:53:02
     IMP_EDR-1248523771-REGULAR-0175040007 1248523771 SOL 21 08:53:09
     IMP_EDR-1248523777-REGULAR-0175040009 1248523777 SOL 21 08:53:15
     IMP_EDR-1248523783-REGULAR-0175040011 1248523783 SOL 21 08:53:21
     IMP_EDR-1248523790-REGULAR-0175040013 1248523790 SOL 21 08:53:28
     IMP_EDR-1248527398-REGULAR-0175040003 1248527398 SOL 21 09:51:59
     IMP_EDR-1248527405-REGULAR-0175040005 1248527405 SOL 21 09:52:06
     IMP_EDR-1248527412-REGULAR-0175040007 1248527412 SOL 21 09:52:13
     IMP_EDR-1248527418-REGULAR-0175040009 1248527418 SOL 21 09:52:19
     IMP_EDR-1248527425-REGULAR-0175040011 1248527425 SOL 21 09:52:26
     IMP_EDR-1248527431-REGULAR-0175040013 1248527431 SOL 21 09:52:32
     IMP_EDR-1248542966-REGULAR-0175040003 1248542966 SOL 21 14:04:33
     IMP_EDR-1248542972-REGULAR-0175040005 1248542972 SOL 21 14:04:38
     IMP_EDR-1248542979-REGULAR-0175040007 1248542979 SOL 21 14:04:45
     IMP_EDR-1248542985-REGULAR-0175040009 1248542985 SOL 21 14:04:51
     IMP_EDR-1248542992-REGULAR-0175040011 1248542992 SOL 21 14:04:58
     IMP_EDR-1248542998-REGULAR-0175040013 1248542998 SOL 21 14:05:04
     IMP_EDR-1248610182-REGULAR-0175040003 1248610182 SOL 22 08:14:57
     IMP_EDR-1248610189-REGULAR-0175040005 1248610189 SOL 22 08:15:04
     IMP_EDR-1248610195-REGULAR-0175040007 1248610195 SOL 22 08:15:10
     IMP_EDR-1248610202-REGULAR-0175040009 1248610202 SOL 22 08:15:17
     IMP_EDR-1248610209-REGULAR-0175040011 1248610209 SOL 22 08:15:24
     IMP_EDR-1248610215-REGULAR-0175040013 1248610215 SOL 22 08:15:29
     IMP_EDR-1248617559-REGULAR-0175040003 1248617559 SOL 22 10:14:38
     IMP_EDR-1248617566-REGULAR-0175040005 1248617566 SOL 22 10:14:45
     IMP_EDR-1248617572-REGULAR-0175040007 1248617572 SOL 22 10:14:50
     IMP_EDR-1248617579-REGULAR-0175040009 1248617579 SOL 22 10:14:57
     IMP_EDR-1248617585-REGULAR-0175040011 1248617585 SOL 22 10:15:03
     IMP_EDR-1248617591-REGULAR-0175040013 1248617591 SOL 22 10:15:09
     IMP_EDR-1248631752-REGULAR-0175040003 1248631752 SOL 22 14:04:52
     IMP_EDR-1248631758-REGULAR-0175040005 1248631758 SOL 22 14:04:58
     IMP_EDR-1248631765-REGULAR-0175040007 1248631765 SOL 22 14:05:05
     IMP_EDR-1248631772-REGULAR-0175040009 1248631772 SOL 22 14:05:12
     IMP_EDR-1248631778-REGULAR-0175040011 1248631778 SOL 22 14:05:18
     IMP_EDR-1248631785-REGULAR-0175040013 1248631785 SOL 22 14:05:25
     IMP_EDR-1248640885-REGULAR-0175040003 1248640885 SOL 22 16:33:02
     IMP_EDR-1248640891-REGULAR-0175040005 1248640891 SOL 22 16:33:08
     IMP_EDR-1248640897-REGULAR-0175040007 1248640897 SOL 22 16:33:14
     IMP_EDR-1248640904-REGULAR-0175040009 1248640904 SOL 22 16:33:21
     IMP_EDR-1248640910-REGULAR-0175040011 1248640910 SOL 22 16:33:26
     IMP_EDR-1248640916-REGULAR-0175040013 1248640916 SOL 22 16:33:32
     IMP_EDR-1248701308-REGULAR-0175040003 1248701308 SOL 23 08:53:15
     IMP_EDR-1248701316-REGULAR-0175040005 1248701316 SOL 23 08:53:23
     IMP_EDR-1248701322-REGULAR-0175040007 1248701322 SOL 23 08:53:29
     IMP_EDR-1248701329-REGULAR-0175040009 1248701329 SOL 23 08:53:35
     IMP_EDR-1248701335-REGULAR-0175040011 1248701335 SOL 23 08:53:41
     IMP_EDR-1248701342-REGULAR-0175040013 1248701342 SOL 23 08:53:48
     IMP_EDR-1248707344-REGULAR-0175040003 1248707344 SOL 23 10:31:10
     IMP_EDR-1248707351-REGULAR-0175040005 1248707351 SOL 23 10:31:17
     IMP_EDR-1248707357-REGULAR-0175040007 1248707357 SOL 23 10:31:23
     IMP_EDR-1248707364-REGULAR-0175040009 1248707364 SOL 23 10:31:30
     IMP_EDR-1248707370-REGULAR-0175040011 1248707370 SOL 23 10:31:35
     IMP_EDR-1248707377-REGULAR-0175040013 1248707377 SOL 23 10:31:42
     IMP_EDR-1248720516-REGULAR-0175040003 1248720516 SOL 23 14:04:51
     IMP_EDR-1248720523-REGULAR-0175040005 1248720523 SOL 23 14:04:58
     IMP_EDR-1248720529-REGULAR-0175040007 1248720529 SOL 23 14:05:04
     IMP_EDR-1248720536-REGULAR-0175040009 1248720536 SOL 23 14:05:10
     IMP_EDR-1248720543-REGULAR-0175040011 1248720543 SOL 23 14:05:17
     IMP_EDR-1248720549-REGULAR-0175040013 1248720549 SOL 23 14:05:23
     IMP_EDR-1248729659-REGULAR-0175040003 1248729659 SOL 23 16:33:10
     IMP_EDR-1248729665-REGULAR-0175040005 1248729665 SOL 23 16:33:16
     IMP_EDR-1248729671-REGULAR-0175040007 1248729671 SOL 23 16:33:22
     IMP_EDR-1248729678-REGULAR-0175040009 1248729678 SOL 23 16:33:29
     IMP_EDR-1248729684-REGULAR-0175040011 1248729684 SOL 23 16:33:35
     IMP_EDR-1248729690-REGULAR-0175040013 1248729690 SOL 23 16:33:41
     IMP_EDR-1248790069-REGULAR-0175040003 1248790069 SOL 24 08:53:10
     IMP_EDR-1248790075-REGULAR-0175040005 1248790075 SOL 24 08:53:16
     IMP_EDR-1248790082-REGULAR-0175040007 1248790082 SOL 24 08:53:23
     IMP_EDR-1248790088-REGULAR-0175040009 1248790088 SOL 24 08:53:29
     IMP_EDR-1248790095-REGULAR-0175040011 1248790095 SOL 24 08:53:36
     IMP_EDR-1248790101-REGULAR-0175040013 1248790101 SOL 24 08:53:42
     IMP_EDR-1248809291-REGULAR-0175040003 1248809291 SOL 24 14:05:00
     IMP_EDR-1248809298-REGULAR-0175040005 1248809298 SOL 24 14:05:07
     IMP_EDR-1248809305-REGULAR-0175040007 1248809305 SOL 24 14:05:14
     IMP_EDR-1248809311-REGULAR-0175040009 1248809311 SOL 24 14:05:20
     IMP_EDR-1248809318-REGULAR-0175040011 1248809318 SOL 24 14:05:26
     IMP_EDR-1248809325-REGULAR-0175040013 1248809325 SOL 24 14:05:33
     IMP_EDR-1248818434-REGULAR-0175040003 1248818434 SOL 24 16:33:20
     IMP_EDR-1248818440-REGULAR-0175040005 1248818440 SOL 24 16:33:25
     IMP_EDR-1248818446-REGULAR-0175040007 1248818446 SOL 24 16:33:31
     IMP_EDR-1248818453-REGULAR-0175040009 1248818453 SOL 24 16:33:38
     IMP_EDR-1248818459-REGULAR-0175040011 1248818459 SOL 24 16:33:44
     IMP_EDR-1248818465-REGULAR-0175040013 1248818465 SOL 24 16:33:50
     IMP_EDR-1248898071-REGULAR-0175040003 1248898071 SOL 25 14:05:14
     IMP_EDR-1248898077-REGULAR-0175040005 1248898077 SOL 25 14:05:20
     IMP_EDR-1248898084-REGULAR-0175040007 1248898084 SOL 25 14:05:27
     IMP_EDR-1248898090-REGULAR-0175040009 1248898090 SOL 25 14:05:33
     IMP_EDR-1248898097-REGULAR-0175040011 1248898097 SOL 25 14:05:40
     IMP_EDR-1248898104-REGULAR-0175040013 1248898104 SOL 25 14:05:46
     IMP_EDR-1248907210-REGULAR-0175040003 1248907210 SOL 25 16:33:30
     IMP_EDR-1248907216-REGULAR-0175040005 1248907216 SOL 25 16:33:35
     IMP_EDR-1248907223-REGULAR-0175040007 1248907223 SOL 25 16:33:42
     IMP_EDR-1248907229-REGULAR-0175040009 1248907229 SOL 25 16:33:48
     IMP_EDR-1248907235-REGULAR-0175040011 1248907235 SOL 25 16:33:54
     IMP_EDR-1248907242-REGULAR-0175040013 1248907242 SOL 25 16:34:01
     IMP_EDR-1248964423-REGULAR-0175050003 1248964423 SOL 26 08:01:38
     IMP_EDR-1248964429-REGULAR-0175050005 1248964429 SOL 26 08:01:44
     IMP_EDR-1248964436-REGULAR-0175050007 1248964436 SOL 26 08:01:51
     IMP_EDR-1248964442-REGULAR-0175050009 1248964442 SOL 26 08:01:56
     IMP_EDR-1248964449-REGULAR-0175050011 1248964449 SOL 26 08:02:03
     IMP_EDR-1248964455-REGULAR-0175050013 1248964455 SOL 26 08:02:09
     IMP_EDR-1248971769-REGULAR-0175050003 1248971769 SOL 26 10:00:48
     IMP_EDR-1248971775-REGULAR-0175050005 1248971775 SOL 26 10:00:54
     IMP_EDR-1248971782-REGULAR-0175050007 1248971782 SOL 26 10:01:01
     IMP_EDR-1248971788-REGULAR-0175050009 1248971788 SOL 26 10:01:07
     IMP_EDR-1248971795-REGULAR-0175050011 1248971795 SOL 26 10:01:13
     IMP_EDR-1248971801-REGULAR-0175050013 1248971801 SOL 26 10:01:19
     IMP_EDR-1248986569-REGULAR-0175050003 1248986569 SOL 26 14:00:54
     IMP_EDR-1248986576-REGULAR-0175050005 1248986576 SOL 26 14:01:00
     IMP_EDR-1248986583-REGULAR-0175050007 1248986583 SOL 26 14:01:07
     IMP_EDR-1248986589-REGULAR-0175050009 1248986589 SOL 26 14:01:13
     IMP_EDR-1248986596-REGULAR-0175050011 1248986596 SOL 26 14:01:20
     IMP_EDR-1248986603-REGULAR-0175050013 1248986603 SOL 26 14:01:27
     IMP_EDR-1248995851-REGULAR-0175050003 1248995851 SOL 26 16:31:28
     IMP_EDR-1248995857-REGULAR-0175050005 1248995857 SOL 26 16:31:34
     IMP_EDR-1248995864-REGULAR-0175050007 1248995864 SOL 26 16:31:41
     IMP_EDR-1248995870-REGULAR-0175050009 1248995870 SOL 26 16:31:47
     IMP_EDR-1248995876-REGULAR-0175050011 1248995876 SOL 26 16:31:53
     IMP_EDR-1248995883-REGULAR-0175050013 1248995883 SOL 26 16:31:59
     IMP_EDR-1249056398-REGULAR-0175050003 1249056398 SOL 27 08:53:42
     IMP_EDR-1249056405-REGULAR-0175050005 1249056405 SOL 27 08:53:48
     IMP_EDR-1249056411-REGULAR-0175050007 1249056411 SOL 27 08:53:54
     IMP_EDR-1249056418-REGULAR-0175050009 1249056418 SOL 27 08:54:01
     IMP_EDR-1249056424-REGULAR-0175050011 1249056424 SOL 27 08:54:07
     IMP_EDR-1249056431-REGULAR-0175050013 1249056431 SOL 27 08:54:14
     IMP_EDR-1249060839-REGULAR-0175050003 1249060839 SOL 27 10:05:44
     IMP_EDR-1249060846-REGULAR-0175050005 1249060846 SOL 27 10:05:51
     IMP_EDR-1249060853-REGULAR-0175050007 1249060853 SOL 27 10:05:58
     IMP_EDR-1249060860-REGULAR-0175050009 1249060860 SOL 27 10:06:05
     IMP_EDR-1249060867-REGULAR-0175050011 1249060867 SOL 27 10:06:12
     IMP_EDR-1249060873-REGULAR-0175050013 1249060873 SOL 27 10:06:17
     IMP_EDR-1249075616-REGULAR-0175050003 1249075616 SOL 27 14:05:27
     IMP_EDR-1249075622-REGULAR-0175050005 1249075622 SOL 27 14:05:33
     IMP_EDR-1249075629-REGULAR-0175050007 1249075629 SOL 27 14:05:40
     IMP_EDR-1249075636-REGULAR-0175050009 1249075636 SOL 27 14:05:47
     IMP_EDR-1249075642-REGULAR-0175050011 1249075642 SOL 27 14:05:53
     IMP_EDR-1249075649-REGULAR-0175050013 1249075649 SOL 27 14:06:00
     IMP_EDR-1249084734-REGULAR-0175050003 1249084734 SOL 27 16:33:22
     IMP_EDR-1249084741-REGULAR-0175050005 1249084741 SOL 27 16:33:29
     IMP_EDR-1249084747-REGULAR-0175050007 1249084747 SOL 27 16:33:35
     IMP_EDR-1249084753-REGULAR-0175050009 1249084753 SOL 27 16:33:41
     IMP_EDR-1249084760-REGULAR-0175050011 1249084760 SOL 27 16:33:48
     IMP_EDR-1249084766-REGULAR-0175050013 1249084766 SOL 27 16:33:54
     IMP_EDR-1249145024-REGULAR-0175050003 1249145024 SOL 28 08:51:26
     IMP_EDR-1249145030-REGULAR-0175050005 1249145030 SOL 28 08:51:31
     IMP_EDR-1249145037-REGULAR-0175050007 1249145037 SOL 28 08:51:38
     IMP_EDR-1249145043-REGULAR-0175050009 1249145043 SOL 28 08:51:44
     IMP_EDR-1249145050-REGULAR-0175050011 1249145050 SOL 28 08:51:51
     IMP_EDR-1249145057-REGULAR-0175050013 1249145057 SOL 28 08:51:58
     IMP_EDR-1249149619-REGULAR-0175050003 1249149619 SOL 28 10:05:58
     IMP_EDR-1249149626-REGULAR-0175050005 1249149626 SOL 28 10:06:05
     IMP_EDR-1249149634-REGULAR-0175050007 1249149634 SOL 28 10:06:13
     IMP_EDR-1249149642-REGULAR-0175050009 1249149642 SOL 28 10:06:21
     IMP_EDR-1249149652-REGULAR-0175050011 1249149652 SOL 28 10:06:30
     IMP_EDR-1249149661-REGULAR-0175050013 1249149661 SOL 28 10:06:39
     IMP_EDR-1249164397-REGULAR-0175050003 1249164397 SOL 28 14:05:42
     IMP_EDR-1249164404-REGULAR-0175050005 1249164404 SOL 28 14:05:49
     IMP_EDR-1249164411-REGULAR-0175050007 1249164411 SOL 28 14:05:56
     IMP_EDR-1249164417-REGULAR-0175050009 1249164417 SOL 28 14:06:02
     IMP_EDR-1249164424-REGULAR-0175050011 1249164424 SOL 28 14:06:09
     IMP_EDR-1249164430-REGULAR-0175050013 1249164430 SOL 28 14:06:14
     IMP_EDR-1249173537-REGULAR-0175050003 1249173537 SOL 28 16:33:59
     IMP_EDR-1249173544-REGULAR-0175050005 1249173544 SOL 28 16:34:05
     IMP_EDR-1249173550-REGULAR-0175050007 1249173550 SOL 28 16:34:11
     IMP_EDR-1249173556-REGULAR-0175050009 1249173556 SOL 28 16:34:17
     IMP_EDR-1249173563-REGULAR-0175050011 1249173563 SOL 28 16:34:24
     IMP_EDR-1249173569-REGULAR-0175050013 1249173569 SOL 28 16:34:30
     IMP_EDR-1249233948-REGULAR-0175050003 1249233948 SOL 29 08:54:00
     IMP_EDR-1249233955-REGULAR-0175050005 1249233955 SOL 29 08:54:06
     IMP_EDR-1249233961-REGULAR-0175050007 1249233961 SOL 29 08:54:12
     IMP_EDR-1249233968-REGULAR-0175050009 1249233968 SOL 29 08:54:19
     IMP_EDR-1249233974-REGULAR-0175050011 1249233974 SOL 29 08:54:25
     IMP_EDR-1249233981-REGULAR-0175050013 1249233981 SOL 29 08:54:32
     IMP_EDR-1249327182-REGULAR-0175050003 1249327182 SOL 30 10:06:29
     IMP_EDR-1249327189-REGULAR-0175050005 1249327189 SOL 30 10:06:35
     IMP_EDR-1249327195-REGULAR-0175050007 1249327195 SOL 30 10:06:41
     IMP_EDR-1249327201-REGULAR-0175050009 1249327201 SOL 30 10:06:47
     IMP_EDR-1249327208-REGULAR-0175050011 1249327208 SOL 30 10:06:54
     IMP_EDR-1249327214-REGULAR-0175050013 1249327214 SOL 30 10:07:00
     IMP_EDR-1249520151-REGULAR-0175050003 1249520151 SOL 32 14:16:40
     IMP_EDR-1249520158-REGULAR-0175050005 1249520158 SOL 32 14:16:47
     IMP_EDR-1249520165-REGULAR-0175050007 1249520165 SOL 32 14:16:53
     IMP_EDR-1249520171-REGULAR-0175050009 1249520171 SOL 32 14:16:59
     IMP_EDR-1249520178-REGULAR-0175050011 1249520178 SOL 32 14:17:06
     IMP_EDR-1249520185-REGULAR-0175050013 1249520185 SOL 32 14:17:13
     IMP_EDR-1249528637-REGULAR-0175050003 1249528637 SOL 32 16:34:20
     IMP_EDR-1249528644-REGULAR-0175050005 1249528644 SOL 32 16:34:26
     IMP_EDR-1249528650-REGULAR-0175050007 1249528650 SOL 32 16:34:32
     IMP_EDR-1249528656-REGULAR-0175050009 1249528656 SOL 32 16:34:38
     IMP_EDR-1249528663-REGULAR-0175050011 1249528663 SOL 32 16:34:45
     IMP_EDR-1249528670-REGULAR-0175050013 1249528670 SOL 32 16:34:52
     IMP_EDR-1249595005-REGULAR-0175050003 1249595005 SOL 33 10:30:58
     IMP_EDR-1249595011-REGULAR-0175050005 1249595011 SOL 33 10:31:04
     IMP_EDR-1249595018-REGULAR-0175050007 1249595018 SOL 33 10:31:11
     IMP_EDR-1249595025-REGULAR-0175050009 1249595025 SOL 33 10:31:18
     IMP_EDR-1249595031-REGULAR-0175050011 1249595031 SOL 33 10:31:24
     IMP_EDR-1249595038-REGULAR-0175050013 1249595038 SOL 33 10:31:31
     IMP_EDR-1249606128-REGULAR-0175050003 1249606128 SOL 33 13:31:25
     IMP_EDR-1249606134-REGULAR-0175050005 1249606134 SOL 33 13:31:31
     IMP_EDR-1249606141-REGULAR-0175050007 1249606141 SOL 33 13:31:38
     IMP_EDR-1249606148-REGULAR-0175050009 1249606148 SOL 33 13:31:44
     IMP_EDR-1249606154-REGULAR-0175050011 1249606154 SOL 33 13:31:50
     IMP_EDR-1249606161-REGULAR-0175050013 1249606161 SOL 33 13:31:57
     IMP_EDR-1249610751-REGULAR-0175050003 1249610751 SOL 33 14:46:25
     IMP_EDR-1249610758-REGULAR-0175050005 1249610758 SOL 33 14:46:32
     IMP_EDR-1249610764-REGULAR-0175050007 1249610764 SOL 33 14:46:37
     IMP_EDR-1249610771-REGULAR-0175050009 1249610771 SOL 33 14:46:44
     IMP_EDR-1249610777-REGULAR-0175050011 1249610777 SOL 33 14:46:50
     IMP_EDR-1249610784-REGULAR-0175050013 1249610784 SOL 33 14:46:57
     IMP_EDR-1249678356-REGULAR-0175050003 1249678356 SOL 34 09:03:08
     IMP_EDR-1249678362-REGULAR-0175050005 1249678362 SOL 34 09:03:13
     IMP_EDR-1249678369-REGULAR-0175050007 1249678369 SOL 34 09:03:20
     IMP_EDR-1249678376-REGULAR-0175050009 1249678376 SOL 34 09:03:27
     IMP_EDR-1249678382-REGULAR-0175050011 1249678382 SOL 34 09:03:33
     IMP_EDR-1249678389-REGULAR-0175050013 1249678389 SOL 34 09:03:40
     IMP_EDR-1249683783-REGULAR-0175050003 1249683783 SOL 34 10:31:10
     IMP_EDR-1249683790-REGULAR-0175050005 1249683790 SOL 34 10:31:17
     IMP_EDR-1249683796-REGULAR-0175050007 1249683796 SOL 34 10:31:23
     IMP_EDR-1249683803-REGULAR-0175050009 1249683803 SOL 34 10:31:29
     IMP_EDR-1249683809-REGULAR-0175050011 1249683809 SOL 34 10:31:35
     IMP_EDR-1249683815-REGULAR-0175050013 1249683815 SOL 34 10:31:41
     IMP_EDR-1249694900-REGULAR-0175050003 1249694900 SOL 34 13:31:23
     IMP_EDR-1249694907-REGULAR-0175050005 1249694907 SOL 34 13:31:30
     IMP_EDR-1249694913-REGULAR-0175050007 1249694913 SOL 34 13:31:36
     IMP_EDR-1249694920-REGULAR-0175050009 1249694920 SOL 34 13:31:43
     IMP_EDR-1249694926-REGULAR-0175050011 1249694926 SOL 34 13:31:49
     IMP_EDR-1249694933-REGULAR-0175050013 1249694933 SOL 34 13:31:55
     IMP_EDR-1249699968-REGULAR-0175050003 1249699968 SOL 34 14:53:36
     IMP_EDR-1249699975-REGULAR-0175050005 1249699975 SOL 34 14:53:43
     IMP_EDR-1249699982-REGULAR-0175050007 1249699982 SOL 34 14:53:50
     IMP_EDR-1249699988-REGULAR-0175050009 1249699988 SOL 34 14:53:56
     IMP_EDR-1249699995-REGULAR-0175050011 1249699995 SOL 34 14:54:03
     IMP_EDR-1249700001-REGULAR-0175050013 1249700001 SOL 34 14:54:08
     IMP_EDR-1249766832-REGULAR-0175060003 1249766832 SOL 35 08:58:18
     IMP_EDR-1249766838-REGULAR-0175060005 1249766838 SOL 35 08:58:24
     IMP_EDR-1249766845-REGULAR-0175060007 1249766845 SOL 35 08:58:30
     IMP_EDR-1249766851-REGULAR-0175060009 1249766851 SOL 35 08:58:36
     IMP_EDR-1249766858-REGULAR-0175060011 1249766858 SOL 35 08:58:43
     IMP_EDR-1249766864-REGULAR-0175060013 1249766864 SOL 35 08:58:49
     IMP_EDR-1249772242-REGULAR-0175060003 1249772242 SOL 35 10:26:04
     IMP_EDR-1249772248-REGULAR-0175060005 1249772248 SOL 35 10:26:09
     IMP_EDR-1249772255-REGULAR-0175060007 1249772255 SOL 35 10:26:16
     IMP_EDR-1249772261-REGULAR-0175060009 1249772261 SOL 35 10:26:22
     IMP_EDR-1249772268-REGULAR-0175060011 1249772268 SOL 35 10:26:29
     IMP_EDR-1249772274-REGULAR-0175060013 1249772274 SOL 35 10:26:35
     IMP_EDR-1249783374-REGULAR-0175060003 1249783374 SOL 35 13:26:32
     IMP_EDR-1249783382-REGULAR-0175060005 1249783382 SOL 35 13:26:39
     IMP_EDR-1249783389-REGULAR-0175060007 1249783389 SOL 35 13:26:46
     IMP_EDR-1249783396-REGULAR-0175060009 1249783396 SOL 35 13:26:53
     IMP_EDR-1249783404-REGULAR-0175060011 1249783404 SOL 35 13:27:01
     IMP_EDR-1249783410-REGULAR-0175060013 1249783410 SOL 35 13:27:07
     IMP_EDR-1249788001-REGULAR-0175060003 1249788001 SOL 35 14:41:35
     IMP_EDR-1249788007-REGULAR-0175060005 1249788007 SOL 35 14:41:41
     IMP_EDR-1249788014-REGULAR-0175060007 1249788014 SOL 35 14:41:48
     IMP_EDR-1249788021-REGULAR-0175060009 1249788021 SOL 35 14:41:55
     IMP_EDR-1249788027-REGULAR-0175060011 1249788027 SOL 35 14:42:01
     IMP_EDR-1249788034-REGULAR-0175060013 1249788034 SOL 35 14:42:07
     IMP_EDR-1249855597-REGULAR-0175060003 1249855597 SOL 36 08:58:09
     IMP_EDR-1249855604-REGULAR-0175060005 1249855604 SOL 36 08:58:16
     IMP_EDR-1249855611-REGULAR-0175060007 1249855611 SOL 36 08:58:23
     IMP_EDR-1249855618-REGULAR-0175060009 1249855618 SOL 36 08:58:30
     IMP_EDR-1249855625-REGULAR-0175060011 1249855625 SOL 36 08:58:37
     IMP_EDR-1249855632-REGULAR-0175060013 1249855632 SOL 36 08:58:43
     IMP_EDR-1249861010-REGULAR-0175060003 1249861010 SOL 36 10:25:50
     IMP_EDR-1249861017-REGULAR-0175060005 1249861017 SOL 36 10:25:57
     IMP_EDR-1249861024-REGULAR-0175060007 1249861024 SOL 36 10:26:03
     IMP_EDR-1249861031-REGULAR-0175060009 1249861031 SOL 36 10:26:10
     IMP_EDR-1249861037-REGULAR-0175060011 1249861037 SOL 36 10:26:16
     IMP_EDR-1249861044-REGULAR-0175060013 1249861044 SOL 36 10:26:23
     IMP_EDR-1249871551-REGULAR-0175060003 1249871551 SOL 36 13:16:50
     IMP_EDR-1249871558-REGULAR-0175060005 1249871558 SOL 36 13:16:57
     IMP_EDR-1249871565-REGULAR-0175060007 1249871565 SOL 36 13:17:03
     IMP_EDR-1249871571-REGULAR-0175060009 1249871571 SOL 36 13:17:09
     IMP_EDR-1249871578-REGULAR-0175060011 1249871578 SOL 36 13:17:16
     IMP_EDR-1249871585-REGULAR-0175060013 1249871585 SOL 36 13:17:23
     IMP_EDR-1249876740-REGULAR-0175060003 1249876740 SOL 36 14:41:00
     IMP_EDR-1249876747-REGULAR-0175060005 1249876747 SOL 36 14:41:07
     IMP_EDR-1249876753-REGULAR-0175060007 1249876753 SOL 36 14:41:13
     IMP_EDR-1249876760-REGULAR-0175060009 1249876760 SOL 36 14:41:20
     IMP_EDR-1249876766-REGULAR-0175060011 1249876766 SOL 36 14:41:26
     IMP_EDR-1249876773-REGULAR-0175060013 1249876773 SOL 36 14:41:33
     IMP_EDR-1249944372-REGULAR-0175060003 1249944372 SOL 37 08:58:09
     IMP_EDR-1249944379-REGULAR-0175060005 1249944379 SOL 37 08:58:16
     IMP_EDR-1249944385-REGULAR-0175060007 1249944385 SOL 37 08:58:22
     IMP_EDR-1249944392-REGULAR-0175060009 1249944392 SOL 37 08:58:29
     IMP_EDR-1249944399-REGULAR-0175060011 1249944399 SOL 37 08:58:36
     IMP_EDR-1249944406-REGULAR-0175060013 1249944406 SOL 37 08:58:43
     IMP_EDR-1249960913-REGULAR-0175060003 1249960913 SOL 37 13:26:21
     IMP_EDR-1249960919-REGULAR-0175060005 1249960919 SOL 37 13:26:27
     IMP_EDR-1249960926-REGULAR-0175060007 1249960926 SOL 37 13:26:34
     IMP_EDR-1249960933-REGULAR-0175060009 1249960933 SOL 37 13:26:41
     IMP_EDR-1249960939-REGULAR-0175060011 1249960939 SOL 37 13:26:47
     IMP_EDR-1249960946-REGULAR-0175060013 1249960946 SOL 37 13:26:53
     IMP_EDR-1249965515-REGULAR-0175060003 1249965515 SOL 37 14:41:01
     IMP_EDR-1249965522-REGULAR-0175060005 1249965522 SOL 37 14:41:07
     IMP_EDR-1249965528-REGULAR-0175060007 1249965528 SOL 37 14:41:13
     IMP_EDR-1249965535-REGULAR-0175060009 1249965535 SOL 37 14:41:20
     IMP_EDR-1249965542-REGULAR-0175060011 1249965542 SOL 37 14:41:27
     IMP_EDR-1249965549-REGULAR-0175060013 1249965549 SOL 37 14:41:34
     IMP_EDR-1250033147-REGULAR-0175060003 1250033147 SOL 38 08:58:10
     IMP_EDR-1250033154-REGULAR-0175060005 1250033154 SOL 38 08:58:16
     IMP_EDR-1250033161-REGULAR-0175060007 1250033161 SOL 38 08:58:23
     IMP_EDR-1250033167-REGULAR-0175060009 1250033167 SOL 38 08:58:29
     IMP_EDR-1250033174-REGULAR-0175060011 1250033174 SOL 38 08:58:36
     IMP_EDR-1250033181-REGULAR-0175060013 1250033181 SOL 38 08:58:43
     IMP_EDR-1250039096-REGULAR-0175060003 1250039096 SOL 38 10:34:40
     IMP_EDR-1250039103-REGULAR-0175060005 1250039103 SOL 38 10:34:47
     IMP_EDR-1250039110-REGULAR-0175060007 1250039110 SOL 38 10:34:54
     IMP_EDR-1250039117-REGULAR-0175060009 1250039117 SOL 38 10:35:00
     IMP_EDR-1250039123-REGULAR-0175060011 1250039123 SOL 38 10:35:06
     IMP_EDR-1250039130-REGULAR-0175060013 1250039130 SOL 38 10:35:13
     IMP_EDR-1250048731-REGULAR-0175060003 1250048731 SOL 38 13:10:58
     IMP_EDR-1250048738-REGULAR-0175060005 1250048738 SOL 38 13:11:05
     IMP_EDR-1250048745-REGULAR-0175060007 1250048745 SOL 38 13:11:12
     IMP_EDR-1250048751-REGULAR-0175060009 1250048751 SOL 38 13:11:17
     IMP_EDR-1250048758-REGULAR-0175060011 1250048758 SOL 38 13:11:24
     IMP_EDR-1250048765-REGULAR-0175060013 1250048765 SOL 38 13:11:31
     IMP_EDR-1250059328-REGULAR-0175060003 1250059328 SOL 38 16:02:52
     IMP_EDR-1250059335-REGULAR-0175060005 1250059335 SOL 38 16:02:59
     IMP_EDR-1250059341-REGULAR-0175060007 1250059341 SOL 38 16:03:05
     IMP_EDR-1250059347-REGULAR-0175060009 1250059347 SOL 38 16:03:11
     IMP_EDR-1250059354-REGULAR-0175060011 1250059354 SOL 38 16:03:18
     IMP_EDR-1250059360-REGULAR-0175060013 1250059360 SOL 38 16:03:24
     IMP_EDR-1250121916-REGULAR-0175060003 1250121916 SOL 39 08:58:12
     IMP_EDR-1250121923-REGULAR-0175060005 1250121923 SOL 39 08:58:19
     IMP_EDR-1250121930-REGULAR-0175060007 1250121930 SOL 39 08:58:25
     IMP_EDR-1250121936-REGULAR-0175060009 1250121936 SOL 39 08:58:31
     IMP_EDR-1250121943-REGULAR-0175060011 1250121943 SOL 39 08:58:38
     IMP_EDR-1250121950-REGULAR-0175060013 1250121950 SOL 39 08:58:45
     IMP_EDR-1250127341-REGULAR-0175060003 1250127341 SOL 39 10:26:12
     IMP_EDR-1250127347-REGULAR-0175060005 1250127347 SOL 39 10:26:18
     IMP_EDR-1250127354-REGULAR-0175060007 1250127354 SOL 39 10:26:25
     IMP_EDR-1250127361-REGULAR-0175060009 1250127361 SOL 39 10:26:32
     IMP_EDR-1250127368-REGULAR-0175060011 1250127368 SOL 39 10:26:38
     IMP_EDR-1250127374-REGULAR-0175060013 1250127374 SOL 39 10:26:44
     IMP_EDR-1250138460-REGULAR-0175060003 1250138460 SOL 39 13:26:27
     IMP_EDR-1250138467-REGULAR-0175060005 1250138467 SOL 39 13:26:34
     IMP_EDR-1250138474-REGULAR-0175060007 1250138474 SOL 39 13:26:41
     IMP_EDR-1250138480-REGULAR-0175060009 1250138480 SOL 39 13:26:47
     IMP_EDR-1250138487-REGULAR-0175060011 1250138487 SOL 39 13:26:54
     IMP_EDR-1250138494-REGULAR-0175060013 1250138494 SOL 39 13:27:01
     IMP_EDR-1250143244-REGULAR-0175060003 1250143244 SOL 39 14:44:04
     IMP_EDR-1250143251-REGULAR-0175060005 1250143251 SOL 39 14:44:11
     IMP_EDR-1250143258-REGULAR-0175060007 1250143258 SOL 39 14:44:18
     IMP_EDR-1250143264-REGULAR-0175060009 1250143264 SOL 39 14:44:23
     IMP_EDR-1250143271-REGULAR-0175060011 1250143271 SOL 39 14:44:30
     IMP_EDR-1250143278-REGULAR-0175060013 1250143278 SOL 39 14:44:37
     IMP_EDR-1250210695-REGULAR-0175060003 1250210695 SOL 40 08:58:16
     IMP_EDR-1250210702-REGULAR-0175060005 1250210702 SOL 40 08:58:23
     IMP_EDR-1250210709-REGULAR-0175060007 1250210709 SOL 40 08:58:30
     IMP_EDR-1250210715-REGULAR-0175060009 1250210715 SOL 40 08:58:36
     IMP_EDR-1250210722-REGULAR-0175060011 1250210722 SOL 40 08:58:43
     IMP_EDR-1250210729-REGULAR-0175060013 1250210729 SOL 40 08:58:50
     IMP_EDR-1250216405-REGULAR-0175060003 1250216405 SOL 40 10:30:54
     IMP_EDR-1250216411-REGULAR-0175060005 1250216411 SOL 40 10:31:00
     IMP_EDR-1250216418-REGULAR-0175060007 1250216418 SOL 40 10:31:07
     IMP_EDR-1250216425-REGULAR-0175060009 1250216425 SOL 40 10:31:14
     IMP_EDR-1250216432-REGULAR-0175060011 1250216432 SOL 40 10:31:20
     IMP_EDR-1250216439-REGULAR-0175060013 1250216439 SOL 40 10:31:27
     IMP_EDR-1250227237-REGULAR-0175060003 1250227237 SOL 40 13:26:37
     IMP_EDR-1250227244-REGULAR-0175060005 1250227244 SOL 40 13:26:44
     IMP_EDR-1250227250-REGULAR-0175060007 1250227250 SOL 40 13:26:50
     IMP_EDR-1250227257-REGULAR-0175060009 1250227257 SOL 40 13:26:57
     IMP_EDR-1250227264-REGULAR-0175060011 1250227264 SOL 40 13:27:04
     IMP_EDR-1250227270-REGULAR-0175060013 1250227270 SOL 40 13:27:10
     IMP_EDR-1250388246-REGULAR-0175060003 1250388246 SOL 42 08:58:18
     IMP_EDR-1250388253-REGULAR-0175060005 1250388253 SOL 42 08:58:25
     IMP_EDR-1250388260-REGULAR-0175060007 1250388260 SOL 42 08:58:32
     IMP_EDR-1250388267-REGULAR-0175060009 1250388267 SOL 42 08:58:38
     IMP_EDR-1250388273-REGULAR-0175060011 1250388273 SOL 42 08:58:44
     IMP_EDR-1250388280-REGULAR-0175060013 1250388280 SOL 42 08:58:51
     IMP_EDR-1250394191-REGULAR-0175060003 1250394191 SOL 42 10:34:37
     IMP_EDR-1250394198-REGULAR-0175060005 1250394198 SOL 42 10:34:44
     IMP_EDR-1250394205-REGULAR-0175060007 1250394205 SOL 42 10:34:51
     IMP_EDR-1250394211-REGULAR-0175060009 1250394211 SOL 42 10:34:57
     IMP_EDR-1250394218-REGULAR-0175060011 1250394218 SOL 42 10:35:03
     IMP_EDR-1250394225-REGULAR-0175060013 1250394225 SOL 42 10:35:10
     IMP_EDR-1250565791-REGULAR-0175060003 1250565791 SOL 44 08:58:21
     IMP_EDR-1250565797-REGULAR-0175060005 1250565797 SOL 44 08:58:27
     IMP_EDR-1250565804-REGULAR-0175060007 1250565804 SOL 44 08:58:34
     IMP_EDR-1250565810-REGULAR-0175060009 1250565810 SOL 44 08:58:40
     IMP_EDR-1250565817-REGULAR-0175060011 1250565817 SOL 44 08:58:46
     IMP_EDR-1250565823-REGULAR-0175060013 1250565823 SOL 44 08:58:52
     IMP_EDR-1250572070-REGULAR-0175060003 1250572070 SOL 44 10:40:13
     IMP_EDR-1250572077-REGULAR-0175060005 1250572077 SOL 44 10:40:20
     IMP_EDR-1250572084-REGULAR-0175060007 1250572084 SOL 44 10:40:26
     IMP_EDR-1250572091-REGULAR-0175060009 1250572091 SOL 44 10:40:33
     IMP_EDR-1250572097-REGULAR-0175060011 1250572097 SOL 44 10:40:39
     IMP_EDR-1250572131-REGULAR-0175060013 1250572131 SOL 44 10:41:12
     IMP_EDR-1251009970-REGULAR-0175060005 1251009970 SOL 49 09:03:53
     IMP_EDR-1251009977-REGULAR-0175060007 1251009977 SOL 49 09:04:00
     IMP_EDR-1251009984-REGULAR-0175060009 1251009984 SOL 49 09:04:07
     IMP_EDR-1251009991-REGULAR-0175060011 1251009991 SOL 49 09:04:14
     IMP_EDR-1251009998-REGULAR-0175060013 1251009998 SOL 49 09:04:21
     IMP_EDR-1251014884-REGULAR-0175060003 1251014884 SOL 49 10:23:36
     IMP_EDR-1251098729-REGULAR-0175060003 1251098729 SOL 50 09:03:45
     IMP_EDR-1251098735-REGULAR-0175060005 1251098735 SOL 50 09:03:51
     IMP_EDR-1251098742-REGULAR-0175060007 1251098742 SOL 50 09:03:57
     IMP_EDR-1251098748-REGULAR-0175060009 1251098748 SOL 50 09:04:03
     IMP_EDR-1251098755-REGULAR-0175060011 1251098755 SOL 50 09:04:10
     IMP_EDR-1251098761-REGULAR-0175060013 1251098761 SOL 50 09:04:16
     IMP_EDR-1251105114-REGULAR-0175060003 1251105114 SOL 50 10:47:19
     IMP_EDR-1251105120-REGULAR-0175060005 1251105120 SOL 50 10:47:25
     IMP_EDR-1251105127-REGULAR-0175060007 1251105127 SOL 50 10:47:32
     IMP_EDR-1251105133-REGULAR-0175060009 1251105133 SOL 50 10:47:38
     IMP_EDR-1251105139-REGULAR-0175060011 1251105139 SOL 50 10:47:44
     IMP_EDR-1251105146-REGULAR-0175060013 1251105146 SOL 50 10:47:51
     IMP_EDR-1251276337-REGULAR-0175060003 1251276337 SOL 52 09:03:58
     IMP_EDR-1251276343-REGULAR-0175060005 1251276343 SOL 52 09:04:04
     IMP_EDR-1251276350-REGULAR-0175060007 1251276350 SOL 52 09:04:11
     IMP_EDR-1251276356-REGULAR-0175060009 1251276356 SOL 52 09:04:17
     IMP_EDR-1251276363-REGULAR-0175060011 1251276363 SOL 52 09:04:24
     IMP_EDR-1251276369-REGULAR-0175060013 1251276369 SOL 52 09:04:29
     IMP_EDR-1251284838-REGULAR-0175060003 1251284838 SOL 52 11:21:53
     IMP_EDR-1251284845-REGULAR-0175060005 1251284845 SOL 52 11:21:59
     IMP_EDR-1251284851-REGULAR-0175060007 1251284851 SOL 52 11:22:05
     IMP_EDR-1251284858-REGULAR-0175060009 1251284858 SOL 52 11:22:12
     IMP_EDR-1251284865-REGULAR-0175060011 1251284865 SOL 52 11:22:19
     IMP_EDR-1251284872-REGULAR-0175060013 1251284872 SOL 52 11:22:26
     IMP_EDR-1251292013-REGULAR-0175060003 1251292013 SOL 52 13:18:01
     IMP_EDR-1251292020-REGULAR-0175060005 1251292020 SOL 52 13:18:08
     IMP_EDR-1251292026-REGULAR-0175060007 1251292026 SOL 52 13:18:14
     IMP_EDR-1251292033-REGULAR-0175060009 1251292033 SOL 52 13:18:21
     IMP_EDR-1251292040-REGULAR-0175060011 1251292040 SOL 52 13:18:27
     IMP_EDR-1251292046-REGULAR-0175060013 1251292046 SOL 52 13:18:33
     IMP_EDR-1251365107-REGULAR-0175060003 1251365107 SOL 53 09:03:45
     IMP_EDR-1251365113-REGULAR-0175060005 1251365113 SOL 53 09:03:51
     IMP_EDR-1251365120-REGULAR-0175060007 1251365120 SOL 53 09:03:58
     IMP_EDR-1251365126-REGULAR-0175060009 1251365126 SOL 53 09:04:04
     IMP_EDR-1251365133-REGULAR-0175060011 1251365133 SOL 53 09:04:10
     IMP_EDR-1251365139-REGULAR-0175060013 1251365139 SOL 53 09:04:16
     IMP_EDR-1251371696-REGULAR-0175060003 1251371696 SOL 53 10:50:32
     IMP_EDR-1251371706-REGULAR-0175060005 1251371706 SOL 53 10:50:42
     IMP_EDR-1251371714-REGULAR-0175060007 1251371714 SOL 53 10:50:49
     IMP_EDR-1251371721-REGULAR-0175060009 1251371721 SOL 53 10:50:56
     IMP_EDR-1251371727-REGULAR-0175060011 1251371727 SOL 53 10:51:02
     IMP_EDR-1251371734-REGULAR-0175060013 1251371734 SOL 53 10:51:09
     IMP_EDR-1251453690-REGULAR-0175060003 1251453690 SOL 54 09:00:38
     IMP_EDR-1251453696-REGULAR-0175060005 1251453696 SOL 54 09:00:44
     IMP_EDR-1251453703-REGULAR-0175060007 1251453703 SOL 54 09:00:51
     IMP_EDR-1251453709-REGULAR-0175060009 1251453709 SOL 54 09:00:57
     IMP_EDR-1251453716-REGULAR-0175060011 1251453716 SOL 54 09:01:04
     IMP_EDR-1251453722-REGULAR-0175060013 1251453722 SOL 54 09:01:10
     IMP_EDR-1251469421-REGULAR-0175060003 1251469421 SOL 54 13:15:42
     IMP_EDR-1251469427-REGULAR-0175060005 1251469427 SOL 54 13:15:48
     IMP_EDR-1251469434-REGULAR-0175060007 1251469434 SOL 54 13:15:55
     IMP_EDR-1251469441-REGULAR-0175060009 1251469441 SOL 54 13:16:01
     IMP_EDR-1251469447-REGULAR-0175060011 1251469447 SOL 54 13:16:07
     IMP_EDR-1251469454-REGULAR-0175060013 1251469454 SOL 54 13:16:14
     IMP_EDR-1251547988-REGULAR-0175060003 1251547988 SOL 55 10:30:13
     IMP_EDR-1251547995-REGULAR-0175060005 1251547995 SOL 55 10:30:19
     IMP_EDR-1251548001-REGULAR-0175060007 1251548001 SOL 55 10:30:25
     IMP_EDR-1251548008-REGULAR-0175060009 1251548008 SOL 55 10:30:32
     IMP_EDR-1251548014-REGULAR-0175060011 1251548014 SOL 55 10:30:38
     IMP_EDR-1251548020-REGULAR-0175060013 1251548020 SOL 55 10:30:44
     IMP_EDR-1251558247-REGULAR-0175060003 1251558247 SOL 55 13:16:30
     IMP_EDR-1251558254-REGULAR-0175060005 1251558254 SOL 55 13:16:37
     IMP_EDR-1251558261-REGULAR-0175060007 1251558261 SOL 55 13:16:44
     IMP_EDR-1251558267-REGULAR-0175060009 1251558267 SOL 55 13:16:50
     IMP_EDR-1251558274-REGULAR-0175060011 1251558274 SOL 55 13:16:57
     IMP_EDR-1251558281-REGULAR-0175060013 1251558281 SOL 55 13:17:04
     IMP_EDR-1251563770-REGULAR-0175060003 1251563770 SOL 55 14:46:06
     IMP_EDR-1251563776-REGULAR-0175060005 1251563776 SOL 55 14:46:12
     IMP_EDR-1251563783-REGULAR-0175060007 1251563783 SOL 55 14:46:19
     IMP_EDR-1251563790-REGULAR-0175060009 1251563790 SOL 55 14:46:26
     IMP_EDR-1251563796-REGULAR-0175060011 1251563796 SOL 55 14:46:31
     IMP_EDR-1251563803-REGULAR-0175060013 1251563803 SOL 55 14:46:38
     IMP_EDR-1251631260-REGULAR-0175060003 1251631260 SOL 56 09:00:55
     IMP_EDR-1251631267-REGULAR-0175060005 1251631267 SOL 56 09:01:02
     IMP_EDR-1251631274-REGULAR-0175060007 1251631274 SOL 56 09:01:09
     IMP_EDR-1251631281-REGULAR-0175060009 1251631281 SOL 56 09:01:15
     IMP_EDR-1251631288-REGULAR-0175060011 1251631288 SOL 56 09:01:22
     IMP_EDR-1251631294-REGULAR-0175060013 1251631294 SOL 56 09:01:28
     IMP_EDR-1251636773-REGULAR-0175060003 1251636773 SOL 56 10:30:21
     IMP_EDR-1251636780-REGULAR-0175060005 1251636780 SOL 56 10:30:28
     IMP_EDR-1251636787-REGULAR-0175060007 1251636787 SOL 56 10:30:35
     IMP_EDR-1251636793-REGULAR-0175060009 1251636793 SOL 56 10:30:40
     IMP_EDR-1251636800-REGULAR-0175060011 1251636800 SOL 56 10:30:47
     IMP_EDR-1251636807-REGULAR-0175060013 1251636807 SOL 56 10:30:54
     IMP_EDR-1251647028-REGULAR-0175060003 1251647028 SOL 56 13:16:42
     IMP_EDR-1251647035-REGULAR-0175060005 1251647035 SOL 56 13:16:49
     IMP_EDR-1251647041-REGULAR-0175060007 1251647041 SOL 56 13:16:55
     IMP_EDR-1251647048-REGULAR-0175060009 1251647048 SOL 56 13:17:02
     IMP_EDR-1251647055-REGULAR-0175060011 1251647055 SOL 56 13:17:09
     IMP_EDR-1251647061-REGULAR-0175060013 1251647061 SOL 56 13:17:14
     IMP_EDR-1251720056-REGULAR-0175060003 1251720056 SOL 57 09:01:21
     IMP_EDR-1251720063-REGULAR-0175060005 1251720063 SOL 57 09:01:28
     IMP_EDR-1251720070-REGULAR-0175060007 1251720070 SOL 57 09:01:35
     IMP_EDR-1251720077-REGULAR-0175060009 1251720077 SOL 57 09:01:42
     IMP_EDR-1251720083-REGULAR-0175060011 1251720083 SOL 57 09:01:48
     IMP_EDR-1251720090-REGULAR-0175060013 1251720090 SOL 57 09:01:54
     IMP_EDR-1251808801-REGULAR-0175060003 1251808801 SOL 58 09:00:51
     IMP_EDR-1251808808-REGULAR-0175060005 1251808808 SOL 58 09:00:58
     IMP_EDR-1251808815-REGULAR-0175060007 1251808815 SOL 58 09:01:05
     IMP_EDR-1251808822-REGULAR-0175060009 1251808822 SOL 58 09:01:12
     IMP_EDR-1251808828-REGULAR-0175060011 1251808828 SOL 58 09:01:18
     IMP_EDR-1251808835-REGULAR-0175060013 1251808835 SOL 58 09:01:24
     IMP_EDR-1251815302-REGULAR-0175060003 1251815302 SOL 58 10:46:11
     IMP_EDR-1251815309-REGULAR-0175060005 1251815309 SOL 58 10:46:18
     IMP_EDR-1251815315-REGULAR-0175060007 1251815315 SOL 58 10:46:24
     IMP_EDR-1251815322-REGULAR-0175060009 1251815322 SOL 58 10:46:31
     IMP_EDR-1251815329-REGULAR-0175060011 1251815329 SOL 58 10:46:38
     IMP_EDR-1251815336-REGULAR-0175060013 1251815336 SOL 58 10:46:45
     IMP_EDR-1251897708-REGULAR-0175060003 1251897708 SOL 59 09:02:58
     IMP_EDR-1251897714-REGULAR-0175060005 1251897714 SOL 59 09:03:04
     IMP_EDR-1251897721-REGULAR-0175060007 1251897721 SOL 59 09:03:11
     IMP_EDR-1251986490-REGULAR-0175060003 1251986490 SOL 60 09:03:03
     IMP_EDR-1251986497-REGULAR-0175060005 1251986497 SOL 60 09:03:10
     IMP_EDR-1251986503-REGULAR-0175060007 1251986503 SOL 60 09:03:15
     IMP_EDR-1251986510-REGULAR-0175060009 1251986510 SOL 60 09:03:22
     IMP_EDR-1251986516-REGULAR-0175060011 1251986516 SOL 60 09:03:28
     IMP_EDR-1251986523-REGULAR-0175060013 1251986523 SOL 60 09:03:35
     IMP_EDR-1251991413-REGULAR-0175060003 1251991413 SOL 60 10:22:54
     IMP_EDR-1251991420-REGULAR-0175060005 1251991420 SOL 60 10:23:01
     IMP_EDR-1251991426-REGULAR-0175060007 1251991426 SOL 60 10:23:07
     IMP_EDR-1251991433-REGULAR-0175060009 1251991433 SOL 60 10:23:14
     IMP_EDR-1251991439-REGULAR-0175060011 1251991439 SOL 60 10:23:20
     IMP_EDR-1251991445-REGULAR-0175060013 1251991445 SOL 60 10:23:25
     IMP_EDR-1252075274-REGULAR-0175060003 1252075274 SOL 61 09:03:08
     IMP_EDR-1252075280-REGULAR-0175060005 1252075280 SOL 61 09:03:14
     IMP_EDR-1252075287-REGULAR-0175060007 1252075287 SOL 61 09:03:21
     IMP_EDR-1252075293-REGULAR-0175060009 1252075293 SOL 61 09:03:27
     IMP_EDR-1252075300-REGULAR-0175060011 1252075300 SOL 61 09:03:34
     IMP_EDR-1252075306-REGULAR-0175060013 1252075306 SOL 61 09:03:39
     IMP_EDR-1252080196-REGULAR-0175060003 1252080196 SOL 61 10:22:59
     IMP_EDR-1252080203-REGULAR-0175060005 1252080203 SOL 61 10:23:06
     IMP_EDR-1252080209-REGULAR-0175060007 1252080209 SOL 61 10:23:12
     IMP_EDR-1252080215-REGULAR-0175060009 1252080215 SOL 61 10:23:17
     IMP_EDR-1252080222-REGULAR-0175060011 1252080222 SOL 61 10:23:24
     IMP_EDR-1252080228-REGULAR-0175060013 1252080228 SOL 61 10:23:30
     IMP_EDR-1252090957-REGULAR-0175060003 1252090957 SOL 61 13:17:25
     IMP_EDR-1252090964-REGULAR-0175060005 1252090964 SOL 61 13:17:32
     IMP_EDR-1252090971-REGULAR-0175060007 1252090971 SOL 61 13:17:39
     IMP_EDR-1252090978-REGULAR-0175060009 1252090978 SOL 61 13:17:46
     IMP_EDR-1252090984-REGULAR-0175060011 1252090984 SOL 61 13:17:52
     IMP_EDR-1252090991-REGULAR-0175060013 1252090991 SOL 61 13:17:58
     IMP_EDR-1252164055-REGULAR-0175060003 1252164055 SOL 62 09:03:12
     IMP_EDR-1252164062-REGULAR-0175060005 1252164062 SOL 62 09:03:19
     IMP_EDR-1252164068-REGULAR-0175060007 1252164068 SOL 62 09:03:24
     IMP_EDR-1252164075-REGULAR-0175060009 1252164075 SOL 62 09:03:31
     IMP_EDR-1252164081-REGULAR-0175060011 1252164081 SOL 62 09:03:37
     IMP_EDR-1252164088-REGULAR-0175060013 1252164088 SOL 62 09:03:44
     IMP_EDR-1252170426-REGULAR-0175060003 1252170426 SOL 62 10:46:33
     IMP_EDR-1252170432-REGULAR-0175060005 1252170432 SOL 62 10:46:39
     IMP_EDR-1252170439-REGULAR-0175060007 1252170439 SOL 62 10:46:45
     IMP_EDR-1252170445-REGULAR-0175060009 1252170445 SOL 62 10:46:51
     IMP_EDR-1252170452-REGULAR-0175060011 1252170452 SOL 62 10:46:58
     IMP_EDR-1252170458-REGULAR-0175060013 1252170458 SOL 62 10:47:04
     IMP_EDR-1252252837-REGULAR-0175060003 1252252837 SOL 63 09:03:16
     IMP_EDR-1252252844-REGULAR-0175060005 1252252844 SOL 63 09:03:23
     IMP_EDR-1252252850-REGULAR-0175060007 1252252850 SOL 63 09:03:29
     IMP_EDR-1252252857-REGULAR-0175060009 1252252857 SOL 63 09:03:35
     IMP_EDR-1252252863-REGULAR-0175060011 1252252863 SOL 63 09:03:41
     IMP_EDR-1252252870-REGULAR-0175060013 1252252870 SOL 63 09:03:48
     IMP_EDR-1252259208-REGULAR-0175060003 1252259208 SOL 63 10:46:37
     IMP_EDR-1252259214-REGULAR-0175060005 1252259214 SOL 63 10:46:43
     IMP_EDR-1252259221-REGULAR-0175060007 1252259221 SOL 63 10:46:50
     IMP_EDR-1252259228-REGULAR-0175060009 1252259228 SOL 63 10:46:56
     IMP_EDR-1252259234-REGULAR-0175060011 1252259234 SOL 63 10:47:02
     IMP_EDR-1252259241-REGULAR-0175060013 1252259241 SOL 63 10:47:09
     IMP_EDR-1252341423-REGULAR-0175060003 1252341423 SOL 64 09:00:08
     IMP_EDR-1252341429-REGULAR-0175060005 1252341429 SOL 64 09:00:14
     IMP_EDR-1252341436-REGULAR-0175060007 1252341436 SOL 64 09:00:21
     IMP_EDR-1252341442-REGULAR-0175060009 1252341442 SOL 64 09:00:27
     IMP_EDR-1252341449-REGULAR-0175060011 1252341449 SOL 64 09:00:34
     IMP_EDR-1252341455-REGULAR-0175060013 1252341455 SOL 64 09:00:40
     IMP_EDR-1252346359-REGULAR-0175060003 1252346359 SOL 64 10:20:10
     IMP_EDR-1252346366-REGULAR-0175060005 1252346366 SOL 64 10:20:16
     IMP_EDR-1252346372-REGULAR-0175060007 1252346372 SOL 64 10:20:22
     IMP_EDR-1252346379-REGULAR-0175060009 1252346379 SOL 64 10:20:29
     IMP_EDR-1252346386-REGULAR-0175060011 1252346386 SOL 64 10:20:36
     IMP_EDR-1252346393-REGULAR-0175060013 1252346393 SOL 64 10:20:42
     IMP_EDR-1252357094-REGULAR-0175060003 1252357094 SOL 64 13:14:13
     IMP_EDR-1252357100-REGULAR-0175060005 1252357100 SOL 64 13:14:19
     IMP_EDR-1252357107-REGULAR-0175060007 1252357107 SOL 64 13:14:25
     IMP_EDR-1252357113-REGULAR-0175060009 1252357113 SOL 64 13:14:31
     IMP_EDR-1252357120-REGULAR-0175060011 1252357120 SOL 64 13:14:38
     IMP_EDR-1252357127-REGULAR-0175060013 1252357127 SOL 64 13:14:45
     IMP_EDR-1252445891-REGULAR-0175060003 1252445891 SOL 65 13:14:31
     IMP_EDR-1252445897-REGULAR-0175060005 1252445897 SOL 65 13:14:37
     IMP_EDR-1252445904-REGULAR-0175060007 1252445904 SOL 65 13:14:44
     IMP_EDR-1252445911-REGULAR-0175060009 1252445911 SOL 65 13:14:51
     IMP_EDR-1252445917-REGULAR-0175060011 1252445917 SOL 65 13:14:56
     IMP_EDR-1252445924-REGULAR-0175060013 1252445924 SOL 65 13:15:03
     IMP_EDR-1252518988-REGULAR-0175060003 1252518988 SOL 66 09:00:16
     IMP_EDR-1252518995-REGULAR-0175060005 1252518995 SOL 66 09:00:23
     IMP_EDR-1252519001-REGULAR-0175060007 1252519001 SOL 66 09:00:29
     IMP_EDR-1252519008-REGULAR-0175060009 1252519008 SOL 66 09:00:35
     IMP_EDR-1252519014-REGULAR-0175060011 1252519014 SOL 66 09:00:41
     IMP_EDR-1252519021-REGULAR-0175060013 1252519021 SOL 66 09:00:48
     IMP_EDR-1252524663-REGULAR-0175060003 1252524663 SOL 66 10:32:19
     IMP_EDR-1252524670-REGULAR-0175060005 1252524670 SOL 66 10:32:26
     IMP_EDR-1252524677-REGULAR-0175060007 1252524677 SOL 66 10:32:33
     IMP_EDR-1252524683-REGULAR-0175060009 1252524683 SOL 66 10:32:39
     IMP_EDR-1252524690-REGULAR-0175060011 1252524690 SOL 66 10:32:46
     IMP_EDR-1252524697-REGULAR-0175060013 1252524697 SOL 66 10:32:53
     IMP_EDR-1252534687-REGULAR-0175060005 1252534687 SOL 66 13:14:47
     IMP_EDR-1252534693-REGULAR-0175060007 1252534693 SOL 66 13:14:53
     IMP_EDR-1252534700-REGULAR-0175060009 1252534700 SOL 66 13:15:00
     IMP_EDR-1252534707-REGULAR-0175060011 1252534707 SOL 66 13:15:07
     IMP_EDR-1252534714-REGULAR-0175060013 1252534714 SOL 66 13:15:14
     IMP_EDR-1252607770-REGULAR-0175060003 1252607770 SOL 67 09:00:18
     IMP_EDR-1252607777-REGULAR-0175060005 1252607777 SOL 67 09:00:25
     IMP_EDR-1252607783-REGULAR-0175060007 1252607783 SOL 67 09:00:31
     IMP_EDR-1252607790-REGULAR-0175060009 1252607790 SOL 67 09:00:38
     IMP_EDR-1252607796-REGULAR-0175060011 1252607796 SOL 67 09:00:44
     IMP_EDR-1252607803-REGULAR-0175060013 1252607803 SOL 67 09:00:51
     IMP_EDR-1252612703-REGULAR-0175060003 1252612703 SOL 67 10:20:12
     IMP_EDR-1252612710-REGULAR-0175060005 1252612710 SOL 67 10:20:19
     IMP_EDR-1252612716-REGULAR-0175060007 1252612716 SOL 67 10:20:25
     IMP_EDR-1252612723-REGULAR-0175060009 1252612723 SOL 67 10:20:32
     IMP_EDR-1252612730-REGULAR-0175060011 1252612730 SOL 67 10:20:39
     IMP_EDR-1252612737-REGULAR-0175060013 1252612737 SOL 67 10:20:46
     IMP_EDR-1252623459-REGULAR-0175060003 1252623459 SOL 67 13:14:41
     IMP_EDR-1252623466-REGULAR-0175060005 1252623466 SOL 67 13:14:48
     IMP_EDR-1252623472-REGULAR-0175060007 1252623472 SOL 67 13:14:54
     IMP_EDR-1252623479-REGULAR-0175060009 1252623479 SOL 67 13:15:01
     IMP_EDR-1252623485-REGULAR-0175060011 1252623485 SOL 67 13:15:07
     IMP_EDR-1252623492-REGULAR-0175060013 1252623492 SOL 67 13:15:13
     IMP_EDR-1252696563-REGULAR-0175060003 1252696563 SOL 68 09:00:28
     IMP_EDR-1252696570-REGULAR-0175060005 1252696570 SOL 68 09:00:35
     IMP_EDR-1252696577-REGULAR-0175060007 1252696577 SOL 68 09:00:42
     IMP_EDR-1252696584-REGULAR-0175060009 1252696584 SOL 68 09:00:49
     IMP_EDR-1252696591-REGULAR-0175060011 1252696591 SOL 68 09:00:55
     IMP_EDR-1252696597-REGULAR-0175060013 1252696597 SOL 68 09:01:01
     IMP_EDR-1252701676-REGULAR-0175060003 1252701676 SOL 68 10:23:22
     IMP_EDR-1252701682-REGULAR-0175060005 1252701682 SOL 68 10:23:27
     IMP_EDR-1252701689-REGULAR-0175060007 1252701689 SOL 68 10:23:34
     IMP_EDR-1252701696-REGULAR-0175060009 1252701696 SOL 68 10:23:41
     IMP_EDR-1252701703-REGULAR-0175060011 1252701703 SOL 68 10:23:48
     IMP_EDR-1252701711-REGULAR-0175060013 1252701711 SOL 68 10:23:56
     IMP_EDR-1252712245-REGULAR-0175060003 1252712245 SOL 68 13:14:48
     IMP_EDR-1252712252-REGULAR-0175060005 1252712252 SOL 68 13:14:55
     IMP_EDR-1252712259-REGULAR-0175060007 1252712259 SOL 68 13:15:02
     IMP_EDR-1252712265-REGULAR-0175060009 1252712265 SOL 68 13:15:08
     IMP_EDR-1252712272-REGULAR-0175060011 1252712272 SOL 68 13:15:15
     IMP_EDR-1252712278-REGULAR-0175060013 1252712278 SOL 68 13:15:20
     IMP_EDR-1252785413-REGULAR-0175060003 1252785413 SOL 69 09:01:42
     IMP_EDR-1252785420-REGULAR-0175060005 1252785420 SOL 69 09:01:49
     IMP_EDR-1252785426-REGULAR-0175060007 1252785426 SOL 69 09:01:54
     IMP_EDR-1252785433-REGULAR-0175060009 1252785433 SOL 69 09:02:01
     IMP_EDR-1252785440-REGULAR-0175060011 1252785440 SOL 69 09:02:08
     IMP_EDR-1252785447-REGULAR-0175060013 1252785447 SOL 69 09:02:15
     IMP_EDR-1252790272-REGULAR-0175060003 1252790272 SOL 69 10:20:31
     IMP_EDR-1252790279-REGULAR-0175060005 1252790279 SOL 69 10:20:38
     IMP_EDR-1252790286-REGULAR-0175060007 1252790286 SOL 69 10:20:45
     IMP_EDR-1252790293-REGULAR-0175060009 1252790293 SOL 69 10:20:51
     IMP_EDR-1252790299-REGULAR-0175060011 1252790299 SOL 69 10:20:57
     IMP_EDR-1252790306-REGULAR-0175060013 1252790306 SOL 69 10:21:04
     IMP_EDR-1252801082-REGULAR-0175060003 1252801082 SOL 69 13:15:52
     IMP_EDR-1252801096-REGULAR-0175060007 1252801096 SOL 69 13:16:06
     IMP_EDR-1252801102-REGULAR-0175060009 1252801102 SOL 69 13:16:12
     IMP_EDR-1252801109-REGULAR-0175060011 1252801109 SOL 69 13:16:18
     IMP_EDR-1252801115-REGULAR-0175060013 1252801115 SOL 69 13:16:24
     IMP_EDR-1252874195-REGULAR-0175060003 1252874195 SOL 70 09:01:52
     IMP_EDR-1252874202-REGULAR-0175060005 1252874202 SOL 70 09:01:59
     IMP_EDR-1252874209-REGULAR-0175060007 1252874209 SOL 70 09:02:06
     IMP_EDR-1252874216-REGULAR-0175060009 1252874216 SOL 70 09:02:12
     IMP_EDR-1252874223-REGULAR-0175060011 1252874223 SOL 70 09:02:19
     IMP_EDR-1252874230-REGULAR-0175060013 1252874230 SOL 70 09:02:26
     IMP_EDR-1252879059-REGULAR-0175060003 1252879059 SOL 70 10:20:40
     IMP_EDR-1252879066-REGULAR-0175060005 1252879066 SOL 70 10:20:46
     IMP_EDR-1252879072-REGULAR-0175060007 1252879072 SOL 70 10:20:52
     IMP_EDR-1252879079-REGULAR-0175060009 1252879079 SOL 70 10:20:59
     IMP_EDR-1252879086-REGULAR-0175060011 1252879086 SOL 70 10:21:06
     IMP_EDR-1252879093-REGULAR-0175060013 1252879093 SOL 70 10:21:13
     IMP_EDR-1252889803-REGULAR-0175060003 1252889803 SOL 70 13:14:57
     IMP_EDR-1252889810-REGULAR-0175060005 1252889810 SOL 70 13:15:03
     IMP_EDR-1252889817-REGULAR-0175060007 1252889817 SOL 70 13:15:10
     IMP_EDR-1252889824-REGULAR-0175060009 1252889824 SOL 70 13:15:17
     IMP_EDR-1252889830-REGULAR-0175060011 1252889830 SOL 70 13:15:23
     IMP_EDR-1252889837-REGULAR-0175060013 1252889837 SOL 70 13:15:30
     IMP_EDR-1252974627-REGULAR-0175060003 1252974627 SOL 71 12:10:47
     IMP_EDR-1252974634-REGULAR-0175060005 1252974634 SOL 71 12:10:54
     IMP_EDR-1252974640-REGULAR-0175060007 1252974640 SOL 71 12:10:59
     IMP_EDR-1252974647-REGULAR-0175060009 1252974647 SOL 71 12:11:06
     IMP_EDR-1252974654-REGULAR-0175060011 1252974654 SOL 71 12:11:13
     IMP_EDR-1252974660-REGULAR-0175060013 1252974660 SOL 71 12:11:19
     IMP_EDR-1253056769-REGULAR-0175060003 1253056769 SOL 72 10:23:07
     IMP_EDR-1253056776-REGULAR-0175060005 1253056776 SOL 72 10:23:13
     IMP_EDR-1253056783-REGULAR-0175060007 1253056783 SOL 72 10:23:20
     IMP_EDR-1253056790-REGULAR-0175060009 1253056790 SOL 72 10:23:27
     IMP_EDR-1253056796-REGULAR-0175060011 1253056796 SOL 72 10:23:33
     IMP_EDR-1253056803-REGULAR-0175060013 1253056803 SOL 72 10:23:40
     IMP_EDR-1253067526-REGULAR-0175060003 1253067526 SOL 72 13:17:36
     IMP_EDR-1253067533-REGULAR-0175060005 1253067533 SOL 72 13:17:43
     IMP_EDR-1253067539-REGULAR-0175060007 1253067539 SOL 72 13:17:49
     IMP_EDR-1253067546-REGULAR-0175060009 1253067546 SOL 72 13:17:56
     IMP_EDR-1253067553-REGULAR-0175060011 1253067553 SOL 72 13:18:02
     IMP_EDR-1253067560-REGULAR-0175060013 1253067560 SOL 72 13:18:09
     IMP_EDR-1253145551-REGULAR-0175060003 1253145551 SOL 73 10:23:09
     IMP_EDR-1253145558-REGULAR-0175060005 1253145558 SOL 73 10:23:15
     IMP_EDR-1253145565-REGULAR-0175060007 1253145565 SOL 73 10:23:22
     IMP_EDR-1253145572-REGULAR-0175060009 1253145572 SOL 73 10:23:29
     IMP_EDR-1253145578-REGULAR-0175060011 1253145578 SOL 73 10:23:35
     IMP_EDR-1253145585-REGULAR-0175060013 1253145585 SOL 73 10:23:42
     IMP_EDR-1253229416-REGULAR-0175060003 1253229416 SOL 74 09:03:33
     IMP_EDR-1253229422-REGULAR-0175060005 1253229422 SOL 74 09:03:38
     IMP_EDR-1253229429-REGULAR-0175060007 1253229429 SOL 74 09:03:45
     IMP_EDR-1253229436-REGULAR-0175060009 1253229436 SOL 74 09:03:52
     IMP_EDR-1253229443-REGULAR-0175060011 1253229443 SOL 74 09:03:59
     IMP_EDR-1253229449-REGULAR-0175060013 1253229449 SOL 74 09:04:05
     IMP_EDR-1253234338-REGULAR-0175060003 1253234338 SOL 74 10:23:14
     IMP_EDR-1253234344-REGULAR-0175060005 1253234344 SOL 74 10:23:20
     IMP_EDR-1253234351-REGULAR-0175060007 1253234351 SOL 74 10:23:27
     IMP_EDR-1253234358-REGULAR-0175060009 1253234358 SOL 74 10:23:34
     IMP_EDR-1253234365-REGULAR-0175060011 1253234365 SOL 74 10:23:41
     IMP_EDR-1253234371-REGULAR-0175060013 1253234371 SOL 74 10:23:46
     IMP_EDR-1253245087-REGULAR-0175060003 1253245087 SOL 74 13:17:36
     IMP_EDR-1253245094-REGULAR-0175060005 1253245094 SOL 74 13:17:43
     IMP_EDR-1253245100-REGULAR-0175060007 1253245100 SOL 74 13:17:49
     IMP_EDR-1253245107-REGULAR-0175060009 1253245107 SOL 74 13:17:56
     IMP_EDR-1253245113-REGULAR-0175060011 1253245113 SOL 74 13:18:01
     IMP_EDR-1253245120-REGULAR-0175060013 1253245120 SOL 74 13:18:08
     IMP_EDR-1253412031-REGULAR-0175060003 1253412031 SOL 76 10:25:23
     IMP_EDR-1253412037-REGULAR-0175060005 1253412037 SOL 76 10:25:29
     IMP_EDR-1253412045-REGULAR-0175060007 1253412045 SOL 76 10:25:36
     IMP_EDR-1253412052-REGULAR-0175060009 1253412052 SOL 76 10:25:43
     IMP_EDR-1253412060-REGULAR-0175060011 1253412060 SOL 76 10:25:51
     IMP_EDR-1253412067-REGULAR-0175060013 1253412067 SOL 76 10:25:58
     IMP_EDR-1253584546-REGULAR-0175060003 1253584546 SOL 78 09:03:39
     IMP_EDR-1253584553-REGULAR-0175060005 1253584553 SOL 78 09:03:45
     IMP_EDR-1253584559-REGULAR-0175060007 1253584559 SOL 78 09:03:51
     IMP_EDR-1253584566-REGULAR-0175060009 1253584566 SOL 78 09:03:58
     IMP_EDR-1253584573-REGULAR-0175060011 1253584573 SOL 78 09:04:05
     IMP_EDR-1253584580-REGULAR-0175060013 1253584580 SOL 78 09:04:12
     IMP_EDR-1253589468-REGULAR-0175060003 1253589468 SOL 78 10:23:21
     IMP_EDR-1253589475-REGULAR-0175060005 1253589475 SOL 78 10:23:28
     IMP_EDR-1253589482-REGULAR-0175060007 1253589482 SOL 78 10:23:35
     IMP_EDR-1253589488-REGULAR-0175060009 1253589488 SOL 78 10:23:41
     IMP_EDR-1253589495-REGULAR-0175060011 1253589495 SOL 78 10:23:47
     IMP_EDR-1253589502-REGULAR-0175060013 1253589502 SOL 78 10:23:54
     IMP_EDR-1253678234-REGULAR-0175060003 1253678234 SOL 79 10:23:06
     IMP_EDR-1253678242-REGULAR-0175060005 1253678242 SOL 79 10:23:14
     IMP_EDR-1253678249-REGULAR-0175060007 1253678249 SOL 79 10:23:21
     IMP_EDR-1253678256-REGULAR-0175060009 1253678256 SOL 79 10:23:28
     IMP_EDR-1253678262-REGULAR-0175060011 1253678262 SOL 79 10:23:33
     IMP_EDR-1253678269-REGULAR-0175060013 1253678269 SOL 79 10:23:40
     IMP_EDR-1253762078-REGULAR-0175060003 1253762078 SOL 80 09:03:08
     IMP_EDR-1253762085-REGULAR-0175060005 1253762085 SOL 80 09:03:15
     IMP_EDR-1253762091-REGULAR-0175060007 1253762091 SOL 80 09:03:21
     IMP_EDR-1253762098-REGULAR-0175060009 1253762098 SOL 80 09:03:28
     IMP_EDR-1253762104-REGULAR-0175060011 1253762104 SOL 80 09:03:34
     IMP_EDR-1253762110-REGULAR-0175060013 1253762110 SOL 80 09:03:39
     IMP_EDR-1253767011-REGULAR-0175060003 1253767011 SOL 80 10:23:01
     IMP_EDR-1253767019-REGULAR-0175060005 1253767019 SOL 80 10:23:08
     IMP_EDR-1253767026-REGULAR-0175060007 1253767026 SOL 80 10:23:15
     IMP_EDR-1253767033-REGULAR-0175060009 1253767033 SOL 80 10:23:22
     IMP_EDR-1253767040-REGULAR-0175060011 1253767040 SOL 80 10:23:29
     IMP_EDR-1253767047-REGULAR-0175060013 1253767047 SOL 80 10:23:36
     IMP_EDR-1253850922-REGULAR-0175060003 1253850922 SOL 81 09:04:08
     IMP_EDR-1253850928-REGULAR-0175060005 1253850928 SOL 81 09:04:14
     IMP_EDR-1253850935-REGULAR-0175060007 1253850935 SOL 81 09:04:21
     IMP_EDR-1253850941-REGULAR-0175060009 1253850941 SOL 81 09:04:26
     IMP_EDR-1253850948-REGULAR-0175060011 1253850948 SOL 81 09:04:33
     IMP_EDR-1253850954-REGULAR-0175060013 1253850954 SOL 81 09:04:39
     IMP_EDR-1253855795-REGULAR-0175060003 1253855795 SOL 81 10:23:03
     IMP_EDR-1253855801-REGULAR-0175060005 1253855801 SOL 81 10:23:08
     IMP_EDR-1253855808-REGULAR-0175060007 1253855808 SOL 81 10:23:15
     IMP_EDR-1253855815-REGULAR-0175060009 1253855815 SOL 81 10:23:22
     IMP_EDR-1253855822-REGULAR-0175060011 1253855822 SOL 81 10:23:29
     IMP_EDR-1253855828-REGULAR-0175060013 1253855828 SOL 81 10:23:35
     IMP_EDR-1253939627-REGULAR-0175060003 1253939627 SOL 82 09:02:53
     IMP_EDR-1253939633-REGULAR-0175060005 1253939633 SOL 82 09:02:58
     IMP_EDR-1253939640-REGULAR-0175060007 1253939640 SOL 82 09:03:05
     IMP_EDR-1253939646-REGULAR-0175060009 1253939646 SOL 82 09:03:11
     IMP_EDR-1253939653-REGULAR-0175060011 1253939653 SOL 82 09:03:18
     IMP_EDR-1253939659-REGULAR-0175060013 1253939659 SOL 82 09:03:24
     IMP_EDR-1253944570-REGULAR-0175060007 1253944570 SOL 82 10:23:03
     IMP_EDR-1253944583-REGULAR-0175060011 1253944583 SOL 82 10:23:16
     IMP_EDR-1253944590-REGULAR-0175060013 1253944590 SOL 82 10:23:23
     IMP_EDR-1254028415-REGULAR-0175060005 1254028415 SOL 83 09:02:58
     IMP_EDR-1254028422-REGULAR-0175060007 1254028422 SOL 83 09:03:05
     IMP_EDR-1254028428-REGULAR-0175060009 1254028428 SOL 83 09:03:11
     IMP_EDR-1254028435-REGULAR-0175060011 1254028435 SOL 83 09:03:17
     IMP_EDR-1254028441-REGULAR-0175060013 1254028441 SOL 83 09:03:23
     IMP_EDR-1254033342-REGULAR-0175060003 1254033342 SOL 83 10:22:46
     IMP_EDR-1254033348-REGULAR-0175060005 1254033348 SOL 83 10:22:52
     IMP_EDR-1254033355-REGULAR-0175060007 1254033355 SOL 83 10:22:59
     IMP_EDR-1254033362-REGULAR-0175060009 1254033362 SOL 83 10:23:06
     IMP_EDR-1254033369-REGULAR-0175060011 1254033369 SOL 83 10:23:13
     IMP_EDR-1254033375-REGULAR-0175060013 1254033375 SOL 83 10:23:18
     IMP_EDR-1254044094-REGULAR-0175060003 1254044094 SOL 83 13:17:11
     IMP_EDR-1254044101-REGULAR-0175060005 1254044101 SOL 83 13:17:17
     IMP_EDR-1254044107-REGULAR-0175060007 1254044107 SOL 83 13:17:23
     IMP_EDR-1254044114-REGULAR-0175060009 1254044114 SOL 83 13:17:30
     IMP_EDR-1254044121-REGULAR-0175060011 1254044121 SOL 83 13:17:37
     IMP_EDR-1254044127-REGULAR-0175060013 1254044127 SOL 83 13:17:43

        