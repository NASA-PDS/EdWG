
 
      Instrument Overview
      ===================
        The instrument used in the Dynamic Science Experiment conducted
        during the Stardust spacecraft encounter with comet Wild 2 on
        January 2, 2004 was the Stardust spacecraft itself, or more
        specifically the spacecraft's Attitude Control System (ACS).
        During the encounter ACS provided a significant measure of the
        spacecraft's performance and the control system's reaction to
        particle impacts.
 
        Throughout the encounter the control system maintained a
        three-axis stabilized attitude. The controller also included
        the capability to command a roll (about the spacecraft X-axis)
        just before closest approach. Using an updated comet trajectory
        computed in flight software, the controller commanded a slew to
        keep the comet in view of the Navigation Camera. As the comet
        passed, the controller commanded a return slew.
 
        The spacecraft commanded two groups of thrusters for control.
        Four 1.0 lbf (nominal) thrusters were available for the
        bang-bang control and slews. Four 0.2 lbf (nominal) thrusters
        were used for limit cycling and small error correction. Four of
        each were available as spares. The larger thrusters were
        designated TCM thrusters; the smaller, RCS thrusters. RCS
        thrusters 1-4 and TCM thrusters 1-4 were used during encounter.
        RCS 5-8 and TCM 5-8 were not used.
 
 
      Scientific Objectives
      =====================
        The ACS provided data on attitude changes which result from
        particle impacts. Analysis of this information could be useful
        in diagnosing large particle impact events. For more
        information see Anderson et al 2003.
 
 
      Calibration
      ===========
        N/A.
 
 
      Operational Considerations
      ==========================
        N/A.
 
 
      Detectors
      =========
        The detectors used in this experiment included the ACS that
        measured source data for and computed spacecraft orientation
        and angular rate and ACS thrusters electronics used to record
        thruster firing times and durations.
 
 
      Electronics
      ===========
        N/A.
 
 
      Location
      ========
        This section contains information about ACS thruster locations
        and thrust vector directions, spacecraft center of mass
        location, and spacecraft moments of inertia.
 
          Spacecraft mass, kg:
 
            M    = 330.979
 
          Spacecraft products and moments of inertia with respect to
          (w.r.t.) the spacecraft coordinates translated to spacecraft
          center of mass, kg/meter^2:
 
            Ixx  =  87.6748
            Iyy  = 200.2580
            Izz  = 241.1340
            Ixy  =   0.2169
            Ixz  =   4.1547
            Iyz  =  -1.4881
 
          Spacecraft center of mass w.r.t. spacecraft reference frame,
          meters:
 
            CM   = [ -1.18277,    -0.000567,     0.0340397 ]
 
          Effective thrust direction unit vectors w.r.t. spacecraft
          reference frame (unit vector):
 
            RCS1 = [       0,       -0.2588,        0.9659 ]
            RCS2 = [       0,       -0.2588,        0.9659 ]
            RCS3 = [       0,        0.2588,        0.9659 ]
            RCS4 = [       0,        0.2588,        0.9659 ]
            RCS5 = [       0,       -0.2588,        0.9659 ]
            RCS6 = [       0,       -0.2588,        0.9659 ]
            RCS7 = [       0,        0.2588,        0.9659 ]
            RCS8 = [       0,        0.2588,        0.9659 ]
            TCM1 = [ -0.1736,        0.2549,        0.9513 ]
            TCM2 = [  0.1736,        0.2549,        0.9513 ]
            TCM3 = [  0.1736,       -0.2549,        0.9513 ]
            TCM4 = [ -0.1736,       -0.2549,        0.9513 ]
            TCM5 = [ -0.1736,        0.2549,        0.9513 ]
            TCM6 = [  0.1736,        0.2549,        0.9513 ]
            TCM7 = [  0.1736,       -0.2549,        0.9513 ]
            TCM8 = [ -0.1736,       -0.2549,        0.9513 ]
 
          Thruster location w.r.t. spacecraft reference frame, meters:
 
            RCS1 = [ -0.7176,        0.2606,       -0.5072 ]
            RCS2 = [  -1.662,        0.2606,       -0.5072 ]
            RCS3 = [  -1.662,       -0.2606,       -0.5072 ]
            RCS4 = [ -0.7176,       -0.2606,       -0.5072 ]
            RCS5 = [ -0.7691,        0.2606,       -0.5072 ]
            RCS6 = [  -1.611,        0.2606,       -0.5072 ]
            RCS7 = [  -1.611,       -0.2606,       -0.5072 ]
            RCS8 = [ -0.7691,       -0.2606,       -0.5072 ]
            TCM1 = [ -0.6132,         0.257,       -0.5159 ]
            TCM2 = [  -1.767,         0.257,       -0.5159 ]
            TCM3 = [  -1.767,        -0.257,       -0.5159 ]
            TCM4 = [ -0.6132,        -0.257,       -0.5159 ]
            TCM5 = [ -0.6647,         0.257,       -0.5159 ]
            TCM6 = [  -1.715,         0.257,       -0.5159 ]
            TCM7 = [  -1.715,        -0.257,       -0.5159 ]
            TCM8 = [ -0.6647,        -0.257,       -0.5159 ]
 
 
        This -Z view of the Stardust spacecraft illustrates locations
        of the thrusters:
 
            .-.
            | |---------------.---------------.--------------.
            | |               |               |              |
            | |               |               |              |
            | |               |   CIDA        |              | +Y Solar
            | |       +Y      |.-------.      |              |   Array
            | |          ^    /.---------.-.  |              |
            | |----------|----\`---------'-' -'--------------'
            `-'          || T1-T5-----------T6-T2     .-.
                         || |O O * *     * * O O|/| .'   `.
                      +Z || |   R1 R5   R6 R2   | |/       \
                 <-------x| |                   | o         |  Return
               +X         | |   R4 R8   R7 R3   | |\       /   Capsule
                          | |O O * *     * * O O|\| `.   .'
            .-.           | T4-T8-----------T7-T3     `-'
            | |---------------.-|     |---| |-.--------------.
            | |               | `-----'   `-' |              |
            | |              Periscope  NAVCAM|              | -Y Solar
            | |               |               |              |   Array
            | |               |               |              |
            | |               |               |              |
            | |---------------'---------------'--------------'
            `-'
 
                                                   O -- TCM Thrusters
                                                   * -- RSC Thrusters
 
 
      Operational Modes
      =================
        The spacecraft was 3-axis stabilized during the whole mission.
        During the comet Wild 2 encounter the spacecraft had its +X
        axis pointed to the incoming comet dust stream while keeping
        the spacecraft-to-comet vector in spacecraft the XZ plane to
        allow tracking of the nucleus by the navigation camera.
 
 
      Subsystems
      ==========
        The Stardust ACS subsystem included thrusters, IMU, star
        camera, and controlling electronics and software.
 
        Stardust performed attitude control and propulsive maneuvers
        using a redundant helium-fed mono-propellant (hydrazine)
        propulsion subsystem. This subsystem was comprised of one
        titanium propellant tank and a total of 16 thrusters (two
        strings of 8), all mounted on the lower deck of the spacecraft
        (opposite the high-gain antenna and solar panels - pointing
        toward the -Z axis of the spacecraft to avoid potential
        contamination of the aerogel collector located on the +Z size
        of the spacecraft). Eight of these were 0.2 lbf thrusters and
        were used primarily for attitude control. The other eight were
        1.0 lbf thrusters and were used for propulsive maneuvers.
 
 
      Measured Parameters
      ===================
        The parameters measured during this experiment included
        spacecraft orientation and angular rate and times and durations
        of ACS thruster firings.

        