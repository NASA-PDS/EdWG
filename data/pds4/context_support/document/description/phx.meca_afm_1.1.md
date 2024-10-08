
 
 
  Instrument Overview
  ===================
 
    The MECA instrument suite is a component of the Mars '07 Phoenix
    investigation, which will also return data from a Thermal and
    Evolved Gas Analyzer (TEGA), three cameras, and a meteorology
    suite (MET). Phoenix is motivated by the goals of (1) studying the
    history of water in all its phases, and (2) searching for
    habitable zones. Samples of surface and subsurface soil and ice
    will be delivered to MECA and TEGA from a trench excavated by a
    Robot Arm (RA), while MECA's Thermal and Electrical Conductivity
    Probe (TECP) will be deployed in soil and air by the Robot Arm.
    The Robot Arm Camera (RAC) will document the morphology of the
    trench walls, while the Surface Stereo Imager (SSI) and the Mars
    Descent Imager (MARDI) establish a geological context. Throughout
    the mission, MET will monitor polar weather and local water
    transport.
 
    The MECA instrument suite is composed of an Atomic Force
    Microscope (AFM), a Thermal Electrical Conductivity Probe (TECP)
    and a Wet Chemistry Laboratory (WCL). This data set description
    catalog file will describe the AFM. A complete description of the
    AFM can be found in [HECHTETAL2008].
 
 
  Scientific Objectives
  =====================
    The Atomic Force Microscope (AFM) is part of the MECA Microscopy
    Station, which comprises a Sample Wheel and Translation Stage
    (SWTS), an optical microscope (OM), and the AFM. The MECA AFM is
    located between the OM and the SWTS inside the darkened MECA
    enclosure on the spacecraft deck. It scans a small region (from
    1-65 micron square) on any of 69 substrates, each 3-mm in
    diameter, positioned along the rim of the SWTS. The chief
    scientific objectives of the AFM are to analyze small dust and
    soil particles in terms of their size, size distribution, shape,
    and texture. The AFM is particularly well suited to analyze
    particles carried by the wind, which are believed to be in the
    size range 1-3 microns.
 
 
  Calibration
  ===========
    Calibration of the AFM instrument is discussed in the AFM
    Calibration Report, which can be found in the Calibration
    folder of the MECA Non-imagng data archive.
 
 
  Operational Considerations and Operational Modes
  ================================================
    Prior to AFM scanning, OM images are acquired to document the
    substrates and provide context for the AFM scans. OM data is
    described in the Phoenix camera SIS, along with the RAC and SSI,
    and is outside the scope of this document. The reader is also
    referred to that document for more detailed description of the
    SWTS and its substrates.
 
    The AFM is contributed by a Swiss-led consortium spearheaded by
    the University of Neuchatel. Run by a dedicated microcontroller,
    the AFM uses one of an array of eight micromachined cantilevers
    with sharp tips to obtain topographs (sometimes called 'scans'
    or 'images') of up to a 65x65 micrometer area of the sample. Within this
    constraint the scan can be of any size,but the AFM can only
    address a narrow horizontal stripe of each substrate. Since
    the sample wheel can be rotated (but not elevated) prior to
    initiation of scanning, the AFM can access a thin band
    approximately 1/3 of the way up from the bottom of the
    corresponding OM image. Note that the x and y axes of the MECA AFM
    image are rotated by +45 degrees relative to the OM images.
 
    The 69 substrates on the SWTS are divided into ten sets of six
    (a weak and a strong magnet, two 'microbuckets', a textured
    substrate, and a sticky silicone pad) and nine utility or
    calibration targets. Using the SWTS, these can be coated with a
    thin layer of dust or soil, and then rotated to the vertical
    scanning position where they can be imaged by the optical
    microscope. Of the six substrates in each set, two are
    specifically designed for AFM use in that they resist the tendency
    for particles to become dislodged and to adhere to the AFM tip.
    Such particle adhesion can degrade the scans in question and the
    quality of the tip in general. One of these substrates is a
    uniform piece of silicone that remains pliant under martian
    conditions. The second is a custom micro-machined silicon
    substrate with pits and posts that hold particles of an
    appropriate scale for AFM scanning. Two of the remaining four
    substrates are magnets that may, under certain circumstances, be
    appropriate for AFM scanning. The final two substrates are deep
    'buckets' that would not normally be accessible to the AFM.
 
  Detectors
  =========
    MECA's AFM comprises three major components, a microfabricated
    probe-chip, an electro-magnetic scanner-actuator and single board
    control electronics. The probe-chip features 8 cantilevers,
    numbered 0-7. The chip is mounted with two orthogonal tilt angles
    of 10 degrees relative to the sample to ensure that only one tip
    contacts the sample at a time. In case of contamination or
    malfunction of this front-most tip, the defective cantilever and
    its support beam can be cleaved off by a special tool on the
    sample wheel, after which the next one in the array becomes
    active. The force constant of the levers varies between 9 and
    13 N/m.
 
    Each of the 8 MECA cantilevers features an integrated
    piezo-electric stress sensor, which is used to measure its pure
    deflection (static mode) or its vibration amplitude, frequency and
    phase (dynamic mode). In static mode the deflection signal is
    proportional to the force, while in dynamic mode the shift of the
    resonance frequency is a measure of the force gradient. Dynamic
    mode minimizes the interactions between tip and surface and is
    less likely to result in particles being moved around or dislodged
    during the scan. In either mode, these signals are used to
    regulate the distance between the tip and the sample in the
    z-direction by means of a proportional-integral feedback loop.
 
    The z-axis servo signal (referred to has height) represents the
    sample topography as the tip is rastered across the surface in the
    x (fast) and y (slow) directions. (Though the resulting topograph
    is sometimes referred to as an image, it bears little resemblance
    to an optical image until it is transformed and processed.)
    Imperfect feedback or an out-of-range condition can result in
    residual bending of the cantilever in static mode, or a phase
    shift of the oscillation in dynamic mode. This error signal may
    optionally be recorded in a second data channel. Since each line
    in the raster scan begins at the same point on the x-axis, both
    primary and error signals may be recorded either on the forward
    or the backward legs of the scan (or, typically, both). Thus a
    single raster scan can produce up to four arrays of data:
    Forward (height), forward (error), backward (height), and backward
    (error), each of which can be displayed in image format.
 
    Several of the status values returned in MECA telemetry refer to
    the configuration and status of the AFM digital feedback loop.
    The piezoresistors on the cantilevers are addressed by a
    multiplexer, which links them to a temperature-compensated
    Wheatsone bridge. For static mode imaging the value of the bridge
    is directly compared to a setpoint. For dynamic mode imaging a
    frequency modulation technique is applied that maintains the
    resonant frequency of the cantilever at a setpoint while
    stabilizing the amplitude. The measured parameters are the
    phase-shift between the excitation of the cantilever and the
    measured signal from the Wheatstone bridge, maintained by a phase
    locked loop. The array geometry is designed to spread the resonant
    frequencies of the levers between 30 and 40 kHz in order to avoid
    cross-talk during dynamic operation (these shift slightly with
    temperature).
 
  Operational Modes
  =================
    To operate the microscopy station, soil samples are deposited by
    the RA (or dust from the air) onto a segment of the SWTS ring that
    has been extended such that exactly one set of 6 substrates
    protrudes from a horizontal slot in the MECA enclosure. Excess
    material is removed by passing the substrates under a blade
    positioned 0.2 mm above the surface, after which the samples are
    rotated from their horizontal load positions into their vertical
    imaging positions for imaging by the OM and AFM. The SWTS is also
    used for focusing and AFM coarse positioning.
 
    Attempting to scan excessively steep or ragged surfaces with the
    AFM will result in scans that are largely out of range, and could
    conceivably damage the tip. Further, bandwidth and time constraints
    severely limit the number of scans that can be acquired and
    returned to Earth. These considerations dictate a two-day imaging
    strategy for each set of microscopy samples. On the first day a
    sample is delivered, then characterized by the optical microscope.
    AFM calibration scans are also acquired. These images are evaluated
    on the ground and targets for AFM scanning are selected. On the
    second day the targeted areas are imaged again with the optical
    microscope, and then scanned with the AFM.
 
    It must be emphasized that an AFM scan is acquired by rastering a
    physical tool across a surface. As a result, line-to-line noise
    and artifacts may be significantly different than point-to-point
    artifacts along the scan direction. Moreover, outside the range of
    authority of the cantilever (approximately 65 x 65 micrometers
    laterally and 13 micrometers in height) the topograph does not go
    'out of focus' but simply saturates, while anywhere within its
    range of authority it is equally 'in focus.' The topograph itself
    reflects the interaction between a tip of finite size and a
    non-uniform surface, and therefore convolves physical
    characteristics of both the probe and the target. Thus, while an
    AFM topograph may look like an image product, the processing
    required bears little in common with the processing of an actual
    optical image.

        