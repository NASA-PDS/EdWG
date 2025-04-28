
 
########################################################################
########################################################################
REQUIRED READING:
- Horanyi et al.  (2007) [HORANYIETAL2007]
########################################################################
########################################################################
 
 
      The SDC description was was adapted from
 
        http://lasp.colorado.edu/sdc/
 
      Horanyi et al. (2007) [HORANYIETAL2007], and
      Weaver et al. (2007) [WEAVERETAL2007]
 
 
  INSTRUMENT OVERVIEW
  ===================
 
    INTRODUCTION
    ------------
      As the name implies, a dust counter is an instrument that counts
      particles of dust.  There are various ways of making one work, but
      in the end, the instrument usally collects information on mass,
      velocity, density, size, or some combination of those four.
 
      The Student Dust Counter has 3 main goals.  The first is to map the
      dust density distribution in the solar system.  Dust is not spread
      evenly throughout space; instead, it varies in density throughout
      the Solar System.  The first goal would be to get an accurate map of
      how this dust density varies.
 
      The second goal of the Student Dust Counter is to understand the
      dust particle size distribution and how it varies throughout the
      Solar System.
 
      The third main goal is to determine how fast the Kuiper Belt
      produces dust.  The small, icy bodies in the Kuiper Belt are
      constantly colliding and causing little bits of each other to chip
      off.  These little bits in turn hit each other and slowly grind into
      dust, in a somewhat similar fashion to how sand on a beach is
      created.  The SDC team hopes to be able to find out how fast this is
      happening.
 
 
    SPECIFICATIONS
    --------------
      NAME:                    SDC (Student Dust Counter)
      DESCRIPTION:             Dust Counter
      PRINCIPAL INVESTIGATOR:  Mihaly Horanyi, U. Colorado
      MASS RANGE:              4 picogram - 4 nanogram
      FIELD OF VIEW:           ~ 180 deg
      ANGULAR RESOLUTION:      N/A
      MASS RESOLUTION:         approx factor of 2 in mass
 
 
    Final Name
    ----------
      After 6 months of successful operations in space the SDC instrument
      was renamed, and the dedication reads:
 
      New Horizons, the first mission to Pluto and the Kuiper Belt, is
      proud to announce that the student instrument (SDC) aboard our
      spacecraft is hereby named 'The Venetia Burney Student Dust Counter'
      in honor of Ms. Venetia Burney Phair, who at age of eleven nominated
      the name Pluto for our solar system's ninth planet.  May 'Venetia'
      inspire a new generation of students to explore our solar system, to
      make discoveries which challenge the imagination, and to pursue
      learning all through their lives.
 
      In this archive, the name Student Dust Counter and the acronym SDC
      will continue to be used.
 
 
  Scientific Objectives
  =====================
    The Student Dust Counter (SDC) will count and measure the sizes of
    dust particles along New Horizons' entire trajectory, which covers
    regions of interplanetary space never before sampled.  Such dust
    particles are created by comets shedding material and Kuiper Belt
    Objects colliding with one another.  The SDC is managed and was built
    primarily by students at the University of Colorado in Boulder, with
    supervision from professional space scientists.
 
 
  Calibration
  ===========
    See Horanyi et al. (2007) [HORANYIETAL2007], especially sections 3.4.3
    and 3.5.
 
 
  Operational Considerations
  ==========================
    SDC was designed to take advantage of the quiet state of the
    spacecraft during cruise phase.  Various active spacecraft operations
    cause mechanical shocks that are picked up by the polyvinylidene
    fluoride (PVDF) sensors and registered by SDC as science events.  This
    is particularly true during three-axis pointing and active spin mode
    when the spacecraft frequently fires short bursts of the attitude
    thrusters.  Level four data reduction (section 4 of Horanyi et al.
    (2007) [HORANYIETAL2007]) is used to filter out any hits that appear
    within a second of any thruster firing, thereby allowing science
    recovery between firings.  However because the thruster induced events
    are often frequent enough to violate the autonomy rule B (section
    3.4.2 of Horanyi et al. (2007) [HORANYIETAL2007]), during spacecraft
    manuvers many SDC detector channels switch off for prolonged periods.
    During the first six months of flight, there are several periods, some
    weeks or months long, where SDC was completely off.
 
 
  Detector
  ========
    The SDC's sensors are thin, permanently polarized PVDF plastic films
    that generate an electrical signal when dust particles penetrate their
    surface.  The SDC has a total sensitive surface area of ~0.1 m^2,
    comprising 12 separate film patches, each 14.2 cm x 6.5 cm, mounted
    onto the top surface of a support panel.  In addition, there are two
    reference sensor patches mounted on the backside of the detector
    support panel, protected from any dust impacts.  These reference
    sensors, identical to the top surface sensors, are used to monitor the
    various background noise levels, from mechanical vibrations or cosmic
    ray hits.
 
 
  Electronics & Construction
  ==========================
    The Student Dust Counter comprises three major pieces:
 
    The Detector Assembly is 18 inches x 12 inches (46cm x 30cm).  This is
    the piece of equipment that is mounted on the outside of the
    spacecraft and is exposed to the dust particles.  The detector is
    thermally isolated from the New Horizons Spacecraft and lies outside
    its Thermal Blanket.
 
    The Electronics Box is approximately 5.4 inches x 8.25 inches x 1.825
    inches (13.7cm x 20.96cm x 4.64cm).  This is the brains of the Dust
    Counter; when a hit occurs on the detector the electronics box will
    decipher the data and determine the mass and speed of the dust
    particle.  The electronics box is actually located within the
    spacecraft and is thermally and electronically bonded to the New
    Horizons Spacecraft.
 
    The Intra-Harness is the 'bridge' between the detector assembly and
    the electronics box.  It serves a similar purpose as the cable which
    allows your home computer to communicate with your printer.
 
    The space environment through which the New Horizons Mission will be
    traveling contains a large variety of conditions which can negatively
    affect spacecraft materials.  The dust collector must be made of a
    substance which is not affected by changes in the temperature,
    radiation environment, or quantity of high-energy particles
    surrounding it.
 
    To meet these challenges, a simple, reliable substance called
    PolyVinyliDene Fluoride (PVDF) has been chosen.  When PVDF is
    manufactured, it is polarized.  This means all of the molecules in the
    material are aligned so that they are pointing in the same direction.
 
    When a dust particle impacts on the detector, it randomly aligns some
    of these previously organized molecules.  This depolarization
    generates an electric signal which is then detected.  The pulse height
    of the signal indicates the mass of the dust particle using the
    relative velocity of the spacecraft.
 
 
  Operating Modes
  ===============
    Data taking and Calibration.  See Horanyi et al. (2007)
    [HORANYIETAL2007] for details.
 
 
  Measured Parameters
  ===================
    The SDC measures and/or records four parameters for each
    Interplanetary Dust Particle (IDP) impact event:  charge (generated by
    each event); time; count; sensor (channel) number.
 
    Masses and velocities of IDPs may be inferred from the measured charge
    of events detected by the SDC sensors.

        