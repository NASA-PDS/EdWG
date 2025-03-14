
 
 
TABLE OF CONTENTS
----------------------------------
= Spacecraft Overview
= Mission Requirements and Constraints
= Platform Definition
= Subsystem Accommodation
= Rosetta Spacecraft Frames
= Structure Design
  - Solar Array
  - Reaction Wheels
  - Propellant Tanks
  - Helium Tanks
  - Thrusters
  - High Gain Antenna
  - Gyros
= Mechanisms Design
  - Solar Array Drive Mechanism (SADM)
  - Solar Array Deployment Mechanisms
  - HGA Antenna Pointing Mechanism (APM)
  - Experiment Boom Mechanisms
  - Louvres
= Thermal Control Design
  - Thermal Control Concept
  - Thermal control design
  - General Heater Control Concept
  - Micrometeoroid and Cometary Dust Protection
= Propulsion Design
  - Operation
= Telecommunication Design
 - High Gain Antenna Major Assembly
 - High Gain Antenna Frame
 - Medium Gain Antenna
   - MGAS
   - MGAX
= Power Design
  - Power Conditioning Unit (PCU)
  - Payload Power Distribution Unit (PL-PDU)
  - Subsystems Power Distribution Unit (SS-PDU)
  - Batteries
  - Solar Array Generator
  - Mechanical Design of the Solar Panels
  - Rosetta Solar Array Frames
= Power Constraints in Deep Space
= Harness Design
= Avionics Design
  - Data Management Subsystem (DMS)
    - Solid State Mass Memory (SSMM)
  - Attitude and Orbit Control Measurement System (AOCMS)
  - Avionics external interface
= Avionics modes
  - Stand-By Mode
  - Sun Acquisition Mode
  - Safe/Hold Mode
  - Normal Mode
  - Thruster Transition Mode
  - Orbit Control Mode
  - Asteroid Fly-By Mode
  - Near Sun Hibernation Mode
  - Spin-up Mode
  - Sun Keeping Mode
= System Level Modes
  - Pre-launch Mode
  - Activation Mode
  - Active Cruise Mode
  - Deep Space Hibernation Mode
  - Near Sun Hibernation Mode
  - Asteroid Fly-by Mode
  - Near Comet Mode
  - Safe Mode
  - Survival Mode
= Ground Segment
  - New Norcia
  - Cebreros
  - Kouru
  - NASA DSN
= Acronyms
 
 
Spacecraft Overview
=====================================================================
 
Please note: The ROSETTA spacecraft was originally designed for a
mission to the comet Wirtanen. Due to a delay of the launch a new
comet (Churyumow-Gerasimenko) had been selected. The compliance of
the design was checked and where necessary adapted for this new
mission. Therefore in the following all the details and
characteristics for this new mission are used (like min and max
distance to Sun).
 
The Rosetta design is based on a box-type central structure, 2.8 m x
2.1 m x 2.0 m, on which all subsystems and payload equipment are
mounted.  The two solar panels have a combined area of 64 m2 (32.7m
tip to tip), with each extending panel measuring 14 m in length.
 
The 'top' of the spacecraft accommodates the payload instruments, and
the 'base' of the spacecraft the subsystems. The spacecraft can be
physically separated into two main modules:
 
    * A Payload Support Module (PSM)
    * A Bus Support Module (BSM)
 
The Lander is attached to the rear face (-X), opposite the two-axes
steerable high-gain antenna (HGA). The two solar wings extend from
the side faces(+/-Y). The instrument panel points almost always
towards the comet, while the antennas and solar arrays point towards
the Sun and Earth (at such great distances the Earth is relatively
speaking in the same direction). The spacecraft attitude concept is
such that the side and back panels are shaded throughout all nominal
mission phases, offering a good location for radiators and louvres.
This will normally be facing away from the comet, minimising the
effects of cometary dust.
 
The spacecraft is built around a vertical thrust tube, whose diameter
corresponds to the 1194 mm Ariane-5 interface. This tube contains two
large, equally sized, propellant tanks, the upper one containing
fuel, and the lower one containing the (heavier) oxidiser.  At launch
the total amount of stored propellant was roughly 1670 kg.
 
A coarse overview on the spacecraft main characteristics is
summarised hereafter:
 
Total launch mass requirement:  3065 kg
Propellant mass:                1718 kg
Overall size (xyz)
        Launch configuration:   225x256x318 cm
        SA deployed:            32.7 m tip-to-tip
power provided by SA:           440 W at max dist from sun (5.3 AU)
energy provided by 3 Batteries: 500 Wh
data management:                operation of s/c according to an on-
                                board master schedule and real-time
                                via ground-link
 
 
Mission Requirements and Constraints
=====================================================================
 
In the following, the stringent mission requirements are summarised
and related to their consequences on the spacecraft system design.
 
The ambitious scientific goals of the ROSETTA mission require:
 
* a large number of complex scientific instruments, to be
accommodated on one side of the spacecraft, that shall, in the
operational phase, permanently face the comet. During cruise the
instruments shall be served for survival.
* one Surface Science Package (SSP), to be accommodated, suitable for
cruise survival and proper, independent ejection from the orbiter
(spacecraft). In addition, the orbiter shall provide the capability
for SSP data relay to Earth.
* a complex spacecraft navigation at low altitude orbits around an
irregular celestial body with weak, asymmetric, rotating gravity
field, rendered by dust and gas jets. These primary mission
requirements are design driving for most of the spacecraft layout and
performance features, as:
* data rate (DMS, TTC)
* pointing accuracy (AOCMS, Structure)
* thermal layout
* closed loop target tracking (AOCMS, NAV Camera), derived
requirements from asteroid fly-by
* small-delta-v manoeuvre accuracy (RCS)
 
Other mission requirements, that relate to the interplanetary cruise
phases rather than to the scientific objectives, drive mainly the
power supply, propulsion, autonomy, reliability and
telecommunication:
 
For achieving the escape energy (C3=11.8 km^2/s^2) to the
interplanetary injection, an Ariane 5 Launch (delayed ignition) is
required, that constrains the maximum S/C wet mass and defines the
available S/C envelope in Launch configuration.
 
The total mission delta-v of more than 2100 m/s requires a propulsion
system with over 1700 kg bi-propellant.
 
The environmental loads (radiation, micro meteoroids impacts) over
the mission duration of nearly 12 years is very demanding w.r.t.
shielding, reliability and life time of the S/C components.
 
The large S/C to Earth distance throughout most mission phases makes
a communication link via an on-board high gain antenna (HGA)
mandatory. The spacecraft must provide an autonomous HGA Earth-
pointing capability using star sensor attitude information and on-
board stored ephemeris table. TC link via spherical LGA coverage, and
TC/TM links via an MGA shall be possible as backup for a loss of the
HGA link.
 
The wide range of S/C to Sun distances (0.88 to 5.33 AU) drive the
thermal control and the size of the solar generator.
 
The long signal propagation time (TWTL up to 100 minutes), and the
extended hibernation phases (2.5 years the longest one), and the many
solar conjunctions/oppositions (the longest in active phases is 7
weeks) require a high degree of on-board autonomy, with corresponding
FDIR concepts.
 
 
Platform Definition
=====================================================================
 
The ROSETTA platform is designed to fulfill the need to accommodate
the payload (including fixed, deployable and ejectable experiment
packages), high gain antenna, solar arrays and propellant mass in a
particular geometrical relationship (mass properties and spacecraft
viewing geometry) and with the specified modularity (Bus Support
Module and Payload Support Module incorporating Lander Interface
Panel). The thermal environment also drives the configuration such
that high dissipation units must be mounted on the side walls with
thermal louvres providing trimming for changing external conditions
during the mission.
 
The design of the platform's electrical architecture is driven by the
need to meet specific power requirements at aphelion (the solar array
sizing case) and to incorporate maximum power point tracking.
Additional factors such as the uncertainty in the performance of the
Low Intensity Low Temperature solar cell technology have also
influenced the design.
 
The telecommunications design is driven by the need to be compatible
with ESA's 15m and 32m ground stations and the 34m and 70m DSN
stations. This has produced requirements for dual S/X band and
variable rate capability, together with an articulated High Gain
Antenna to maximise data transfer during the payload operations, and
a fixed Medium Gain Antenna to act as backup for the HGA in case of
failure.
 
 
Subsystem Accommodation
=====================================================================
 
The majority of the subsystem equipments are accommodated together
within the BSM. The electronic units are located mostly on the Y
panels so that their thermal dissipations are closely coupled to the
louvred radiators on the sidewalls. So far as practical, functionally
related groups are located close together for harness, integration
and testability reasons. Where possible, equipments are positioned
towards the +X half of the S/C to counterbalance the mass of the
Lander on the opposite side.
 
Some subsystem equipments are deliberately located on the PSM. These
include the PDU and RTU for the payload, the NAVCAMS, two of the SAS
units and the +Z LGA. The PDU and RTU are located closer to the
payload instruments to reduce harness complexity and mass, and the
NAVCAMs and SASs and +Z LGA are located on the PSM for field of view
reasons. Other subsystem equipments have been located on the PSM
sidewalls as a result of BSM equipment/harness growth, or thermal
limitations. These comprise the STR electronics and SSMM as well as
the USO.
 
The RCS subsystem comprises tanks, thrusters and the associated
valves and pipework. The main tanks are accommodated within the
central tube while the helium pressurisation tanks are mounted on the
internal deck. Most of the valves and pipework are located on the +X
BSM, panel which becomes permanently attached to the BSM once RCS
assembly is completed. Sixteen of the twenty-four thrusters are
located at the four lower corners of the BSM. The remaining
thrusters are located in 4 groups near the top corners of the S/C.
They are installed as part of the BSM, but are attached to the PSM
after PSM/BSM mating.
 
The Star Trackers are mounted on the -X shearwalls. The STR B is
rotated by additional 10 degrees towards the -Z direction compared to
STR A to avoid the VIRTIS radiator rim to be seen in its field of
view. This location of the STRs is both thermally stable and
mechanically close to the -X PSM panel which accommodates the
instruments requiring high pointing accuracy. The reaction wheels are
located on the internal deck which provides them with a thermo-
elastically stable location.
 
A 2.2m diameter HGA is stowed face-outwards for launch against the
S/C +X face (so it would be partially usable even in the event of a
deployment failure). After deployment, the HGA can be rotated in two
axes around a pivot point on a tripod assembly some distance clear of
the lower corner of the S/C. This provides the HGA with greater than
hemispherical pointing range. The two MGAs are fixed mounted on the
S/C +X face, oriented in the +Xs/c direction, as this is the most
useful direction for a fixed MGA. The LGAs are located at the +Z and
-Z ends of the S/C but angled at 30 degs to the Z axis. This
accommodation provides spherical coverage with minimum need for
switching.
 
The solar array comprises two 5-panel wings folded against the
Spacecraft Y axis for launch. Because the arrays are sized to operate
at aphelion, the outwards facing outer panel can also generate useful
power before array deployment.
 
Two Sun Acquisition Sensors are located on the solar arrays and
another two on the S/C body. Their design and location of these also
allow them to serve as fine Sun sensors.
 
 
Rosetta Spacecraft Frame
=====================================================================
 
   Rosetta spacecraft frame is defined as follows:
 
      -  +Z axis is perpendicular to the launch vehicle interface
         plane and points toward the payload side;
      -  +X axis is perpendicular to the HGA mounting plane and
         points toward HGA;
      -  +Y axis completes the frame is right-handed.
      -  the origin of this frame is the launch vehicle interface
         point.
 
   These diagrams illustrate the ROS_SPACECRAFT frame:
 
   +X s/c side (HGA side) view:
   ----------------------------
                                   ^
                                   | toward comet
                                   |
 
                              Science Deck
                            ._____________.
  .__  _______________.     |             |     .______________  ___.
  |  \ \               \    |             |    /               \ \  |
  |  / /                \   |  +Zsc       |   /                / /  |
  |  \ \                 `. |      ^      | .'                 \ \  |
  |  / /                 | o|      |      |o |                 / /  |
  |  \ \                 .' |      |      | `.                 \ \  |
  |  / /                /   |      |      |   \                / /  |
  .__\ \_______________/    |  +Xsc|      |    \_______________\ \__.
    -Y Solar Array          .______o-------> +Ysc   +Y Solar Array
                                ._____.
                              .'       `.
                             /           \
                            .   `.   .'   .          +Xsc is out of
                            |     `o'     |             the page
                            .      |      .
                             \     |     /
                              `.       .'
                           HGA  ` --- '
 
 
   +Z s/c side (science deck side) view:
   -------------------------------------
                                 _____
                                /     \  Lander
                               |       |
                            ._____________.
                            |             |
                            |             |
                            |  +Zsc       | +Ysc
  o==/ /==================o |      o------->o==================/ /==o
    -Y Solar Array          |      |      |        +Y Solar Array
                            |      |      |
                            .______|______.
                             `.   |   .'
                                .--V +Xsc
                         HGA  .'       `.
                             /___________\
                                 `.|.'                 +Zsc is out
                                                      of the page
 
 
Structure Design
=====================================================================
The ROSETTA platform structure consists of two modules, the Bus
Support Module and the Payload Support Module (BSM and PSM). Mounted
to the BSM is the Lander Interface Panel (LIP), which can be handled
separately for the Lander integration.
 
The spacecraft structural design is based on a version with a central
cylinder accommodating the two propellant tanks. The general
dimensions are dictated on one hand by the need to accommodate the
two large tanks, to provide sufficient mounting area for the payload
and subsystems and the Lander, as well as being able to accommodate
two large solar arrays, and on the other hand by the requirement to
fit within the Ariane 5 fairing.
 
The spine of the structure is the central tube, to which the
honeycomb panels are mounted. The spacecraft box is closed by lateral
panels, which are connected to the central tube by load carrying
vertical shear webs and an internal deck.
 
The Bus Support Module (BSM) accommodates most of the platform and
avionic equipment.
 
The Payload Support Module (PSM) is accommodating all science
equipment. The PSM structure consists of the PSM +z-panel, the PSM -x
panel, the PSM +y/-y panels and the Lander Interface Panel (LIP).
 
Most instrument sensors are located on a single face, the +Z panel,
with the exception of VIRTIS and OSIRIS mounted on the -X panel to
allow for the accommodation of their cold radiators, Alice mounted on
PSM -X and COSIMA mounted on the PSM -Y panel. The P/L electronics
are mounted on the +Y and -Y side of this module for heat radiation
via Louvers.
 
Special supports are provided by the structure for:
 
Solar Array
-----------
They provide stiff and accurately positioned points for the solar
array hold down points and for solar arrays drive mechanisms.
 
Reaction Wheels
---------------
The brackets provide stiff wheel support with alignment capability.
All 4 RW brackets are mounted together between the +X shear wall and
the central deck building one compact bracket unit which provides
high stiffness and stability.
 
Propellant Tanks
----------------
The two tanks are mounted via a circumferential ring of flanges to a
reinforced adapter ring on the tube with titanium screws.
 
Helium Tanks
------------
The two helium tanks are mounted on the main deck of the BSM. They
are attached by an equatorial fixation in the middle of the tank
through internal deck holes.
 
Thrusters
---------
Thrusters on the side of the spacecraft are mounted on lateral panel
extensions with aluminium machined brackets ensuring the angular
position of the thrusters. Thrusters underneath the spacecraft (-Z
pointing thrusters) are mounted on brackets on the corners of the
+/-Y panels.
 
High Gain Antenna
-----------------
The HGA is stowed against the +X panel, in areas stiffened by the
+/-Y panels and the HGA support tripod. After launch, the HGA is
deployed and is connected to the S/C by the support tripod only. The
axis Antenna Pointing Mechanisms, fixed on the tripod, are located
close to the edge of the HGA.
 
Gyros
-----
A single bracket provides stiff gyro support and alignment capability
and orientates the 3 IMUs in the requested angular orientation. The
bracket is mounted on the -Y BSM panel for thermal dissipation
reasons.
 
 
Mechanisms Design
=====================================================================
 
The ROSETTA mechanisms comprise the following major equipments:
* Solar Array Drive Mechanism (SADM)
* Solar Array Deployment Mechanisms
* HGA Antenna Pointing Mechanism (APM)
* HGA Holddown & Release Mechanism (HRM)
* Experiment Booms & HRMs
* Louvres (mechanical elements)
 
 
Solar Array Drive Mechanism (SADM)
----------------------------------
The SADM performs the positioning of the Solar Array w.r.t. the Sun
by rotation of the panels around the spacecraft Y-axis. There are two
identical SADMs on both sides of the spacecraft, which can be
individually controlled. The control authority rests with the AOCMS
subsystem, which always 'knows' the actual attitude and Sun direction
and is therefore in the position to determine the required
orientation of the solar panels. The positioning commands are routed
from the AOCMS I/F Unit via the SADE (SADM-Electronics) to the SADM.
 
The Solar Array rotation is limited to plus and minus 180 degrees to
the reference position. The array zero position is defined in the
section 'Power Design: Solar Array Generator' below.
 
The Solar Array Drive Mechanism baseline design comprises the
following major components:
* Housing structure from aluminium alloy
* Main bearing, pre-loaded angular contact roller bearing
* Drive unit consisting of a redundantly wound stepper motor, gear-
  reduction unit, anti-backlash pinion, and final stage gear ring
* Redundant position transducer and electronics, harness and
  connectors.
* Mechanical end-stop for +/-180 deg travel limit with redundant
  micro-switches (4 in all)
* Redundant electrical power and signal harnesses, and connectors
* Twist capsule unit, allowing +/-180 deg electrical circuit transfer
* Thermistor for temperature reading, with harness.
 
The SADM drive unit employs a 'pancake' configuration with one single
X-type ballbearing to provide high moment stiffness and strength
within a compact axial envelope. The central output shaft is of
hollow construction, providing sufficient space to accommodate the
power and signal transfer harness and a twist capsule allowing +/-180
degrees rotation of the harness. The drive unit contains a position
transducer and a drive train.
 
The Solar Arrays Drive Electronic is intended to manage two Solar
Array Drives that can be rotated so as to get the maximum energy from
the solar cell panels.
 
 
Solar Array Deployment Mechanisms
----------------------------------
The baseline are 2 solar arrays, each with a full silicon 5-panel
wing, with panel sizes as used in the ARA MK3 5-panel qualification
wing (about 5.3 m2 per panel).
 
During launch the wings are stowed against the sidewalls of the
satellite. They are kept in this position by means of 6 hold-down
mechanisms per wing.
 
Approximately 3 hours after launch, the satellite is pointed towards
the Sun and the wings are deployed to their fully deployed position.
They are released for full deployment by 'cutting' Kevlar restraint
cables by means of thermal knives (actually degrading of the Kevlar
by heat).
 
The deployment system makes use of spring driven hinges and is
equipped with a damper, that limits the deployment speed of the wing.
Thus, the deployment shocks on SADM hinge and inter-panel hinges are
kept relatively low.
 
The Rosetta wing is further equipped with:
* ESD protection on front and rear side,
* Solar Array sun acquisition sensor,
* Solar Array performance strings
 
 
HGA Antenna Pointing Mechanism (APM)
------------------------------------
The APM is a two-axes mechanism which allows motion of the HGA in
both azimuth and elevation. The control authority rests with the
AOCMS subsystem, which always 'knows' the actual attitude and Earth
direction and is therefore in the position to determine the required
orientation of the antenna. The positioning commands are routed from
the AOCMS I/F Unit via the APM-E (APM-Electronics) to the APMM. HGA
elevation rotation is physically limited to +30deg/ -165deg from the
reference position (after deployment). Before and during deployment
the range is -207deg and +30deg.
 
HGA azimuth rotation is physically limited to +80deg / -260deg from
the reference position.
 
The main functions of the APM are:
 
* Allow accurate and stable pointing of the antenna dish through
controlled rotation about azimuth and elevation axes.
* Minimise stresses on the waveguides by acting as load transfer path
between the HGA and the spacecraft.
 
It consists of three main components:
* The motor drive units (APM-M) and RF Ancillary Equipment (Rotary
  Joint)
* The support structure (APM-SS).
* The electronic control of these units (APM-E).
 
The APM-M is mounted between the antenna dish and the APM-SS.
 
For thermal reasons the elements of the APM-M and APM-SS and the
Antenna HDRMs are covered with MLI.
 
 
Experiment Boom Mechanisms
---------------------------
Two deployable experiment booms support a number of different
lightweight sensors from the plasma package which need to be deployed
clear of the S/C body. These booms are deployed at beginning of the
mission after Launch.
 
Each boom consists of a 76 mm dia CFRP tube. The lower boom is
approximately 1.3 m long and the upper boom 2m.
 
The boom deployment is performed by means of a motor driven unit. The
deployment mechanism consists of:
 
* Hinge, Motor Gear Unit, Coupling system, Latching system and
  Position switches.
 
The Hold down and release mechanisms, one per boom, has the following
characteristics:
* Three Titanium blades to allow relative displacement in the boom
  centreline direction. This reduces the mechanical and thermo-
  elastic I/F forces.
* The separation device is the Hi-Shear low shock Separation Nut
  SN9422-M8
 
 
Louvres
--------
The Rosetta Thermal Control Subsystem contains 14 louvers with 2
different set points which are located on the S/C Y walls in front of
white painted radiators. The louvers are designed, manufactured and
qualified by SENER.
 
The mechanisms of the 16 blade louver are the 8 temperature dependent
bi-metal springs (actuators), which supply the fundamental function
of the louver. The actuators are driving the louver blades to its end
stops for the defined fully open / fully closed temperature set
points.
 
 
Thermal Control Design
=====================================================================
 
Thermal Control Concept
-----------------------
 
The thermal control design is driven on one side by the low heater
power availability together with the low solar intensity in the cold
case, and on the other side by the hot cases characterised by high
dissipation of the operational units and high external heat loads.
 
The thermal control concept mainly utilises conventional passive
components supported by active units like heaters and controlled
radiative areas, using well proven methods and classical elements.
 
This concept can be characterised as follows :
 
* Heat flows from and to the external environment are minimised using
  high performance Multi-Layer Insulation (MLI).
* Most unit heat is rejected through dedicated white paint radiator,
  actively controlled by louvers, located on very low Sun-illuminated
  +/-Y panels.
* High internal emissivity compartments reduce structural temperature
  gradients.
* Individually controlled instruments and appendages (booms, antennas
  ,...) are mounted thermally decoupled from the structure.
* High temperature MLI is used in the vicinity of thrusters.
* Optimised heaters, dedicated to operational, and hibernation modes,
  are monitored and controlled to judiciously compensate the heat
  deficit during cold environment phases.
 
 
Thermal control design
-----------------------
The thermal control subsystem (TCS) design is optimised for the
enveloping design cases of the end of life comet operations and the
aphelion hibernation. From the overall mission point of view the deep
space hibernation heater power request is the most critical thermal
design case. This heater power request is dependent on the radiator
sizing which need to be performed for worst case end of mission
conditions. The very strong heater power limitation implies that to
a certain extent constraints in the operation and/or attitude need to
be accepted for hot case.
 
The TCS uses a combination of selected surface finishes, heaters,
multi-layer insulation (MLI) and louvres to control the units in the
allowable temperature ranges. The units are mostly mounted on the
main +/- Y panels of the spacecraft (and +Z for experiments), with
interface fillers to enhance the conductive link to the panel for the
collectively controlled units. The individually controlled
experiments are thermally decoupled from the structure.
 
Generated heat by the collectively controlled units is then rejected
via conduction into the panel and subsequent radiation from the
external surface of the panel to space. These surfaces are covered
with louvers over white painted radiators minimising any absorbed
heat inputs and heat losses in cold mission phases. The louvers are
selected as baseline being the best solution (investigated during
phase B) for flexibility, qualification status and reliability.
 
VIRTIS and OSIRIS cameras are located at the top of the -X (anti-sun
face) so that their radiator may view deep space. The top floor is
extended over the top as a sunshield to prevent any direct solar
illumination of these instruments, while the sun angle on the -Z side
has to be limited to 80 degrees for the same reason.
 
Any external structural surface not required as a radiator, (or
experiment aperture) is covered with a high performance MLI blanket.
The bottom of the bus module, which is not enclosed with a structural
panel, is covered with a high performance MLI blanket used also as an
EMC screen. In the areas around thrusters, a high temperature version
of the MLI are implemented. All blankets are adequately grounded and
vented.
 
The bi-propellant propulsion subsystem needs to be maintained between
0 to +45 degrees throughout the mission. This is far warmer than some
units, particularly when the spacecraft is in deep space hibernation
mode. The tanks and RCS are therefore well isolated from the rest of
the spacecraft to allow their specific thermal control.
 
The antennae and experiment booms are passively thermally controlled
by the use of appropriate thermo-optical surface finishes and MLI.
The mechanism for the HGA has similar appropriate passive control but
also needs heaters to prevent the mechanism from freezing. It is
thermally decoupled from the rest of the spacecraft to allow its
dedicated thermal control.
 
The chosen solution for thermal control subsystem design uses well
known and proven technologies and concepts.
 
 
General Heater Control Concept
-------------------------------
The operation of the TCS shall enable to maintain all spacecraft
units within the required temperature range throughout the entire
mission coping with all possible spacecraft orientations and unit
mode operations.
 
The thermal heater concept uses the following major control features:
 
* Thermistor controlled (software) heater circuits, which are used to
maintain platform, avionics and payload units within operating limits
when these units are operating.
 
* The S/W heater design includes 3 control thermistors sited next to
each other and uses the middle temperature reading to control the
heater switching. This method is used in order to maximise the
reliability of thermistor controlling temperature.
 
* Thermistors will be also used to monitor the temperature at each
unit's temperature reference point (TRP) and at the System Interface
Temperature Points (STP).
 
* Thermostat controlled (hardware) heater circuits, which are used to
maintain platform, avionics and payload units within their non-
operating (or switch-on) limits when these units are non-operating.
These operate autonomously during satellite hibernation and Safe
modes to ensure thermal control.
 
* The hardware heater circuits will be controlled by one thermostat
(cold guard) connected in redundant circuit. The prime circuits
without any thermostat will be powered as long as the relevant LCL is
defined to be enabled. In the prime circuit a thermostat (hot guard)
is included to prevent from overheating. In the event of a failure in
the prime circuit the redundant circuit is automatically switched on
when the temperature falls because it is permanently enabled.
 
* The lower set points for the thermostats (cold guard) are at the
lower nonoperating limits of units. The hysteresis of the thermostats
is chosen to 35 degrees Celsius to limit the number of switching
cycles for the long Rosetta mission. The higher set points of the
prime thermostats (hot guard) is oriented to the upper operational
temperature limit, but will still have an appropriate margin to that
limit.
 
* Main and redundant heaters will be in separate foil heaters. It is
necessary to define reserved unpainted areas on all units, which
would nominally be black painted, specifically for the mounting of
heaters.
 
All software and hardware heaters circuits will comprise a simple
series connection of heaters with no parallel connections. The heater
concept assumes prime and redundant heater elements in different
mats. The heaters will be mounted directly onto units as this
maximises the efficiency of the heating.
 
The sizing of the autonomous H/W heater circuits are based upon the
following criteria:
 
* Payload heaters shall be designed to maintain non-operating
temperature limits at 5.33AU or switch-on limits at 3.25AU,
whichever gives the greater heater power requirement,
 
* Platform and Avionics units OFF in hibernation have heaters
designed to maintain non-operating temperature limits at 5.33AU
or switch-on limits at 4.5AU, whichever is the greater power
requirement,
 
* Platform and Avionics units ON during hibernation have heaters
designed to maintain operating temperature limits at 5.33 AU.
 
The suppliers of individually controlled (I/C) units shall
size their S/W and H/W heaters by themselves and may install them
where they wish in order to control their unit temperatures.
 
 
Micrometeoroid and Cometary Dust Protection
--------------------------------------------
The micrometeoroid protection used for Rosetta is composed of 2
layers of betacloth and a spacer. This protection is only applied to
the exposed +Z and -Z central tube areas of the propellant tanks as
the spacecraft honeycomb structure will form an effective shield
elsewhere.
 
The first betacloth layer is underneath the outermost layer of the
S/C MLI acting as a bumper. To reach the agreed probability of no
micrometeroid impacts in 998 out of 1000 strikes, a separation of 50mm
to the second betacloth layer (on top of the tank MLI) is needed. The
micrometeoroid protection is part of the overall MLI design.
 
The cometary dust will have a velocity similar to that of Rosetta and
so hypervelocity impacts are not an issue. Of more concern is the
coating of the spacecraft surfaces by the cometary dust. Grounding of
the external surfaces prevents differential charging but the whole
spacecraft may be charged to some potential.
 
 
Propulsion Design
=====================================================================
The propulsion subsystem is based on a pressure fed bipropellant type
using MMH (MonoMethylHydrazine) and NTO (Nitrogen TetrOxide). It is
capable to operate in both regulated and in blow-down mode and
provides a delta v of more than 2100 m/s plus attitude control. It is
able to operate in three axis and in spin stabilised mode (about the
x-axis) provided that the spin rate does not exceed 1 rpm. The
subsystem provides a high degree of redundancy in order to cope with
the special requirements of the ROSETTA mission.
 
The materials used in the propulsion subsystem are proven to be
compatible with the propellants and their vapours the wetted area
being mainly made of titanium or suitable stainless steel alloys.
 
The components and most of the pipework are installed on the
spacecraft -X panel by means of supporting brackets made of material
with low thermal conductance.
 
The subsystem has 24 10 N thruster for attitude and orbit control.
They are located such that they can provide pure forces and pure
torques to the spacecraft. The 24 thrusters are grouped in pairs on
the brackets, one of each pair being the main and one the redundant
thruster. The subsystem allows the operation of 8 thrusters
simultaneously.
 
The subsystem will be maintained within the temperature limits of the
components. The mixture ratio may be adjusted by tank temperature
(i.e. pressure) manipulation in order to enhance thruster
performance.
 
 
Operation
----------
The propulsion subsystem will be operated in regulated mode as well
as in blow down mode. The pressurisation strategy must take into
account various constraints as the available propellant, the minimum
inlet pressures for the thrusters, the maximum allowable pressures in
the propellant tanks etc. Calculations have been performed to
demonstrate the capability of the subsystem to fulfil the mission
requirements in terms of delta-v provision under the various
constraints and also with respect to the requirement for additional
20% fuel.
 
 
Telecommunication Design
=====================================================================
 
The Tracking, Telemetry and Command (TT & C) communications with the
Earth over the complete Rosetta mission is ensured by three antenna
concepts, operating at various stages throughout the overall
programme, combined with a number of electrical units performing
certain functions. The Telecommunication Subsystem is required to
interface with the ESA ground segment in normal operational mode and
with the NASA Deep Space Network during emergency mode.
 
The TT & C subsystem comprises a number of equipment's whose
descriptions appear below:
 
* Two Transponders interfacing with the S-Band RF Distribution Unit
(RFDU), with the High Power Amplifiers - in this case Travelling Wave
Tube Amplifiers (TWTA's) -, and with the Data Management System
(DMS). The Transponders modulate and transmit the Telemetry stream
coming from both parts of the redundant Data Management System either
in S or X-Band or both simultaneously without any interference and
transpond the ranging signal in S and X-Band. The Transponders
provide hot redundancy for the receiving functions and cold
redundancy for transmitting functions. The receivers can receive
telecommands in S-Band or X-Band (selectable per command), but not
simultaneously in both frequency bands. The configuration is such
that both receivers can receive, demodulate and send the telecommand
signal to the DMS simultaneously. The transmitters are also able to
receive the telemetry stream from both parts of the redundant DMS.
Each transponder is capable of operating in a coherent or non-
coherent mode depending on the lock status of the receiver.
 
* An RF Distribution Unit (RFDU) providing an S-Band transmit/receive
switching function between the antennas and the two Transponder units
via two diplexers.
 
* Two TWTA's providing >28W of power at X-Band to the MGA or HGA via
the Waveguide Interface Unit (WIU). The input to the TWTA HPA's is
supplied by the Transponder X-Band modulators via a 3dB passive
hybrid.
 
* A Waveguide Interface Unit (WIU) comprising of diplexers, two
transfer switches and high power isolators so that it is possible to
switch between antennas without turning off the TWTA.
 
* The transmit frequency (and receiver rest frequency) can also be
derived from an external Ultra Stable Oscillator (USO) on request by
Telecommand which may be used any time during the mission. This USO
has a superior performance compared to the Transponder internal
oscillator such that it is used for one-way ranging as part of the
Radio Science Investigations (RSI).
 
* Two Low Gain Antennas (LGA) providing a quasi omni directional
coverage for any attitude of the satellite which may be used for:
 
      a)the near earth mission phase at S-Band for uplink telecommand
        and downlink telemetry.
 
      b)the telecommand Up Link at S-Band during emergency and
        nominal communications over large ranges up to 6.25 AU.
 
* A 2.2m High Gain Antenna (HGA) providing the primary communication
for Uplink at S/X-band and Downlink at S/X-Band.
 
* Two Medium Gain Antennas (MGA) providing emergency Up and Downlink
default communication after sun pointing mode of the S/C is reached.
The S-Band MGA is realised as a flat patch antenna whereas the X-
Band MGA is a offset-type 0.31m reflector antenna. The MGAs also
perform some mission communications functions at various phases
throughout their lifetime due to their much larger coverage area.
 
 
High Gain Antenna Major Assembly
---------------------------------
The transmission of the high rate scientific data of the ROSETTA
spacecraft to earth is depending reliable operation of the High Gain
Antenna major assembly, which is therefore a critical element for
the mission success. The most important requirements for this
assembly are:
  * High reliability
  * conform to specified pointing requirements
  * minimize mechanical disturbances
  * comply to antenna gain requirements
 
The HGA Major Assembly comprises:
  * HRM Hold-down and Release Mechanism for the HGA dish during
    launch with three release points
  * Two axes APM Antenna Pointing Mechanism (HGAPM) mounted on
    a tripoid to offset the antenna from the +X panel
  * A Cassegrain (X-Band) quasiparaboloid highgain Antenna (HGA)
    with a dichoric subreflector and S-band primary feed
  * Antenna Pointing Mechanism Electronics (APME)
  * Waveguide (WG) and Rotary Joints (RJ) for the RF transmission
 
High Gain Antenna Frame
--------------------------------------
 
The Rosetta High Gain Antenna is attached to the +X side of the s/c
bus by a gimbal providing two degrees of freedom and it articulates
during flight to track Earth. Therefore, the Rosetta HGA frame,
ROS_HGA, is defined with its orientation given relative to the
ROS_SPACECRAFT frame.
 
The ROS_HGA frame is defined as follows:
   -  +Z axis is in the antenna boresight direction;
   -  +X axis points from the gimbal toward the antenna dish
      symmetry axis;
   -  +Y axis completes the right hand frame;
   -  the origin of the frame is located at the geometric center of
      the HGA dish outer rim circle.
 
The rotation from the spacecraft frame to the HGA frame can be
constructed using gimbal angles from telemetry by first rotating
by elevation angle about +Y axis, then rotating by azimuth about
+Z axis, and then rotating by +90 degrees about +Y axis to finally
align +Z axis with the HGA boresight.
 
   This diagram illustrates the ROS_HGA frame:
 
   +X s/c side (HGA side) view:
   ----------------------------
                                   ^
                                   | toward comet
                                   |
 
                               Science Deck
                            ._____________.
  .__  _______________.     |             |     .______________  ___.
  |  \ \               \    |             |    /               \ \  |
  |  / /                \   |  +Zsc       |   /                / /  |
  |  \ \                 `. |      ^      | .'                 \ \  |
  |  / /                 | o|      |      |o |                 / /  |
  |  \ \                 .' |      |      | `.                 \ \  |
  |  / /                /   |      |      |   \                / /  |
  .__\ \_______________/    |  +Xsc|      |    \_______________\ \__.
    -Y Solar Array          .______o-------> +Ysc   +Y Solar Array
                                .__o__.
                              .'       `.
                             /           \
                            .   `.   .'   .           +Zhga and HGA
                            |     `o-------> +Yhga    boresight are
                            .      |      .           out of the page
                             \     |     /
                              `.   |   .'
                           HGA  ` -|- '
                                   V +Xhga
 
 
Medium Gain Antenna (MGA)
-------------------------
The MGA design has been split into two physically separated antennae
parts:
  * the MGAS operating in -S-Band frequencies,
  * the MGAX operating in -X-Band frequencies,
 
MGA S-band (MGAS)
- - - - - - - - -
The antenna design for the S-Band subsystem consists of an array of
patch antenna elements providing a circularly symmetrical radiation
pattern. The maximum gain obtainable for this array surface area
(300mm x 300mm) ranges between 14.1 and 14.7 dBi in the receive and
transmit frequency bandwidths.
 
The MGAS assembly can be sub-divided into two parts, the RF active
part (radiators plus distribution network) and the support structure
(platform plus stand-offs).
 
The array elements are arranged in a hexagonal lattice to provide the
required symmetry to the antenna pattern. Six elements are used to
meet the required specification.
 
MGA X-band (MGAX)
- - - - - - - - -
The configuration of the X-band MGA (MGAX) is a single offset
parabolic reflector illuminated by a circular polarised conical horn.
Reflector dimensions are selected to reach a desired minimum gain and
to lead to a simple feeder design. This leads to an aperture diameter
of about 310mm and a focal length of 186mm (F/D = 0.6). With these
values a large reflector subtended angle is obtained which ensures
small feeder dimensions and a compact antenna design.
 
The MGAX antenna assembly is composed of two sub-assemblies, a
reflector and a feeder, and of a platform which supports both these
sub-assemblies and provides the interface to the Rosetta spacecraft.
The total envelope of the antenna is length=600mm, width=320mm,
height=320mm.
 
The thermal protection for the antenna consists of:
* White paint on the radiant face (PYROLAC 120 FD + P128)
* Thermal blankets on the rear face of reflector, feeder, supports
  and platform.
 
Low Gain Antenna (LGA)
----------------------
Two classical S-band Low Gain Antennae (LGA) of a conical quadrifilar
helix antenna type are implemented on the satellite in opposite
direction to achieve an omnidirectional coverage. One is located at
the +Z-panel in the near of the edge to the +X panel and thus is
orientated towards the comet during the comet mission phase. The
other one is mounted on the opposite face.
 
 
Ultra Stable Oscillator
------------------------
An Ultra Stable Oscillator is implemented within the TTC subsystem
providing the required frequency stability (Allan Variance, 3s,
2.0e-13 at 38.2808642 MHz) for the RSI instrument. This USO will be
used by the TTC subsystem whenever needed and is available for RSI
measurements as well. Should the USO fail, each transponder will use
it's own oscillator (TCX0), but with less stability and not harming
the performance.
 
 
Power Design
=====================================================================
The Power Subsystem (PSS) conditions, regulates and distributes all
the electrical power required by the spacecraft throughout all phases
of the mission. Distribution involves the switching and protection of
power lines to all users, including the Avionics units and the
Payload instruments, and includes equipment power, thermal power and
keep-alive-lines. The PSS also switches, protects and distributes
power for the pyrotechnics and the thermal knives of the various
release mechanisms of the spacecraft.
 
Main power source for Rosetta is provided by the Solar Array
Subsystem from silicon solar cells mounted on 2 identical solar array
wings, which are deployed from the +Y and -Y faces of the spacecraft
and can be rotated to track the sun. The solar cells on the outer
panel of each wing are outward facing when in the launch (stowed)
configuration in order to provide power input to the PSS for loads
and battery recharge following separation from the launcher and prior
to array deployment.
 
Batteries provide power for launch and post-separation support until
the solar arrays are fully deployed and sun aligned, and thereafter
will support the main power bus as necessary to supply peak loads and
special situations during Safe Mode where the sun might not be fully
oriented towards the sun. One special feature of the power supply is
the Maximum Power Point Tracker (MPPT), which will operate the solar
array in its maximum power point in case of power shortage. During
almost all time of the mission, except for short periods of peak
power demands, the PCU will operate in nominal mode, i.e. the PCU
takes only the power required by the satellite from the solar array.
The delta power will remain in the solar array. Because of this
feature the actual performance of the array can only be assessed by
utilising 'performance strings' which operate some cells in short
circuit current mode and others in open circuit voltage mode. From
the data obtained from these cells the performance of the solar
generator can be determined.
 
Batteries are also the main power source for the pyrotechnics,
although pyrotechnic power is also available from the main bus as a
back-up in case there is no battery power.
 
The subsystem is designed in accordance to the ESA Power Standard
PSS-02-10.
 
Power Conditioning Unit (PCU)
-----------------------------
* Produces a fully regulated 28V single power bus from solar array
  and battery inputs.
* Main bus voltage control including triple redundant error
  amplifiers
* Separate hot redundant array power regulators for each array wing.
* Separate hot redundant Maximum Power Point Trackers (MPPT) for
  each array wing
* Separate Battery Discharge Regulator (BDR) for each battery.
* Separate Battery Charge Regulator (BCR) for each battery.
* Array performance monitor.
* TM/TC interface.
* Some automatic functions to support power bus management.
 
Payload Power Distribution Unit (PL-PDU)
----------------------------------------
* Dedicated to payload power distribution.
* Fully redundant unit.
* Main bus power outlets are all switched and protected by Latching
  Current Limiters (LCL).
* LCLs have current measurement and input under-voltage protection.
* 7 LCL power rating classes covering 5.5W to 135W (nominal load
  capability).
* Provision of Keep Alive Lines (KALs) for experiments.
* Pyrotechnic power protection and distribution, including firing
  current measurement and storage.
* Distributes power to the Thermal Control Subsystem hardware and
  software controlled heaters.
* Individual on/off switching for each software controlled heater
  circuit.
* TM/TC interface.
 
Subsystems Power Distribution Unit (SS-PDU)
-------------------------------------------
* Dedicated to Platform and Avionics power distribution.
* Fully redundant unit.
* Fold-back Current Limiters (FCL) for non-switchable loads
  (Receivers and CDMUs).
* All other main bus power outlets are switched and protected by
  Latching Current Limiters (LCL).
* FCLs and LCLs have current measurement and FCLs have input under-
  voltage protection.
* LCL classes and power ratings as for PL-PDU.
* Pyrotechnic power protection and distribution, including firing
  current measurement and storage.
* Thermal Knives (TKs) power distribution (for Solar Array panels
  release).
* Distributes power to the Thermal Control Subsystem combined
  hardware -  software controlled heaters.
* Individual on/off switching for each software controlled heater
  circuit.
* TM/TC interface.
 
Batteries
----------
* 3 batteries each comprising 6 series and 11 parallel connected Li-
  Ion 1.5 Ah cells (corresponds to 16.5 Ah per battery).
* Power and monitoring connections to PCU.
* Power connections also to the PDUs for the pyrotechnics.
* Cells arrangement and wiring to minimise magnetic moment.
* 1 thermistors per battery for battery charge/discharge control.
* A combination of relay/heater mat in order to discharge the
  batteries for capacitance verification.
 
Solar Array Generator
----------------------
The orbit of the S/C has an extremely wide variation of Spacecraft-
Earth-Sun angles and distances, hence it is mandatory to include an
electrical design based on LILT (Low Intensity Low Temperature) solar
cell technology.
 
The structural parts/units (deployment system, substrates, hold-down
& release system) are identical to the qualified ARA MK3 design of
Fokker Space.
 
The geometry and mechanical interface definition of the Rosetta
baseline Solar Array design is identical to the 5-panel qualification
wing.
 
The electrical architecture (cells, strings, sections & harness lay-
out) is uniquely designed for Rosetta. Electro static discharge (ESD)
protection design is qualified for the ARA MK3 type solar array.
 
The baseline are 2 solar arrays, each with a full silicon 5-panel
wing, with panel sizes as used in the ARA MK3 5-panel qualification
wing (about 5.3 m2 per panel).
 
                          x-------x
   x---.---.---.---.---x  |       |  x---.---.---.---.---x
   |   |   |   |   |   |--|   x   |--|   |   |   |   |   |
   x---'---'---'---'---x  |       |  x---'---'---'---'---x
                          x-------x
 
Mechanical Design of the Solar Panels
--------------------------------------
The basic skin design of the panels of the solar arrays consists of
two layers [0/90degres] M55J/950-1 CFRP prepreg (thickness per layer
0.06 mm) in closed lay-up. The panel substrate dimensions are 2.25 x
2.736 m2. The front side skin will use a 50^m Kapton foil to isolate
the solar cell network from the conductive CFRP layers. The Kapton
foil is co-cured with the CFRP layers.
 
The panel core consists of Aluminium honeycomb with a core height of
22 mm. Local circular reinforcement plugs ('subassembly panels') are
used to provide the holddown areas with extra strength, stiffness and
fatigue resistance.
 
The hold-down and release system uses a tie-down element (Kevlar
cable) under high preload which will be degraded by heat of the
thermal knife for release. The hold-down, SADM and yoke snubber
locations for Rosetta are fully identical to the ARA MK3
qualification hardware definition.
 
The stowed wing has a height of <239 mm at the wing tips (the gap
between inner panel and sidewall is increased from nominal 70 mm by
about 30mm by means of a dedicated bracket, the inter panel gap is 12
mm, and the panel substrate thickness is 22 mm).
 
The deployment mechanism concept relies on spring-driven hinges. The
spring characteristics are chosen such that the energy supply is
enough for the full range up to 5 maximum sized panels, while
maintaining the required deployment safety factors. In order to
reduce the shock loads on the SADM and inter-panel hinges, a damper
is introduced in the deployment system.
 
A stiff synchronisation system is applied to prevent a very non-
synchronous deployment, resulting in unpredictable high deployment
latch-up shocks at the interpanel hinges.
 
The V-yoke length is 1103 mm when measured from SADM hinge-line to
yoke/inner panel hinge-line. The yoke length used within the ARAFOM
5-panel QM wing programme is identical.
 
The arms of the V-shaped yoke consist of M46J CFRP filament wound
with a circular cross section (inner diameter 43 mm; nominal wall
thickness 0.9 mm) with reinforcements at the ends of the yoke tubes.
 
Rosetta Solar Array Frames
--------------------------------------
The Rosetta solar arrays can be articulated (each having one degree
of freedom), the solar Array frames, ROS_SA+Y and ROS_SA-Y, are
defined with their orientation given relative to the ROS_SPACECRAFT
frame.
 
Both array frames are defined as follows :
 
      -  +Y axis is parallel to the longest side of the array,
         positively oriented from the end of the wing toward the
         gimbal;
 
      -  +Z axis is normal to the solar array plane, the solar cells
         on the +Z side;
 
      -  +X axis is defined such that (X,Y,Z) is right handed;
 
      -  the origin of the frame is located at the geometric center
         of the gimbal.
 
The axis of rotation is parallel to the Y axis of the spacecraft and
solar array frames.
 
At zero (reference) position the array wing is aligned such that the
array surface is in the spacecraft Y-Z plane, with the face (cells)
aligned such that the array normal is parallel to the +X axis of the
spacecraft. This means that in stowed configuration (i.e. launch
configuration) the array position of the array on the +Y panel is -90
degrees and on the -Y panel +90 degrees.
 
This diagram illustrates the ROS_SA+Y and ROS_SA-Y frames:
 
+X s/c side (HGA side) view:
----------------------------
                                   ^
                                    | toward comet
                                    |
 
                               Science Deck  +Xsa+y0
                             ._____________.^+Xsa+y
   .__  _______________.     |             ||    .______________  ___.
   |  \ \               \    |             ||   /               \ \  |
   |  / /                \   |  +Zsc       ||  /                / /  |
   |  \ \                 `. |      ^      ||.+Zsa+y0           \ \  |
   |  / /           +Zsa-y0 o-----> | <-----o  Zsa+y            / /  |
   |  \ \           +Zsa-y.'|+Ysa-y0|+Ysa+y0 `.                 \ \  |
   |  / /                /  ||+Ysa-y|+Ysa+y|   \                / /  |
   .__\ \_______________/   ||      |      |    \_______________\ \__.
     -Y Solar Array         |.______o-------> +Ysc   +Y Solar Array
                            v  +Xsc o__.
                     +Xsa-y0   .'       `.
                     +Xsa-y   /           \
                             .   `.   .'   . +Zsa+y0, +Zsa+y, +Zsa-y0,
                             |     `o'     | and +Zsa-y are out of
                             .      |      .       the page
                              \     |     /
                               `.       .'   Active solar cell is
                            HGA  ` --- '      facing the viewer
 
 
Power Constraints in Deep Space
=====================================================================
 
In the phases with Sun distances above approximately 4.0 AU the
decreasing solar array power forces the use of economical strategies
for certain operations. Thereby the situation after the deep space
hibernation phase is much more severe. From radiation degradation
analysis it has been derived that after DSHM at 4.5 AU about 65 W
less solar array power will be available compared to 4.5 AU before
DSHM. This corresponds to about 13% of the power needed at that
distance.
 
In the deep space phases the general operational concept is the
following:
 
  * minimise the overall power consumption by switching off all
  equipment not directly needed during the current operation
 
  * additionally, for certain operations with high extra power
  demand, perform a power sharing strategy by switching off some TCS
  heaters; as a consequence this puts a time limit on such operations
 
  * operate equipment like RWs and SSMM in reduced power mode
 
  * for autonomous operations, which are not directly under ground
  control, like in Safe Mode, the ground can set a Low Power Flag as
  invocation parameter in the call of the Safe Mode OBCP (which is
  loaded in the System Init Table) at the appropriate time in the
  mission, according to the current Sun distance. This flag will be
  checked by the OBCP; if the flag is set, the Safe Mode downlink
  will be performed in power sharing strategy and the SSMM is set
  into stand-by mode (memory modules remain powered, but memory
  controllers are switched off).
 
As a safety precaution the battery discharge alarm shall remain
enabled all the time. This will allow for nominal short (< 4 min)
peak power demands to be satisfied by the batteries, e.g. for RW
offloading, but will trigger a system alarm and transition to Safe
Mode in case of a creeping battery discharge due to a wrong power
configuration e.g. because of a missed command. If for such a case a
processor reconfiguration is not desired, it is possible to use the
monitoring of the MEA Voltage to trigger transition into Safe Mode
before the battery discharge alarm triggers (see Handling of On-board
Monitoring, [RO-DSS-TN-1155]).
 
 
Harness Design
=====================================================================
The harness performs the electrical connection between all
electrical and electronic equipment in the ROSETTA spacecraft. It
provides distribution and separation of power supplies, signals,
scientific data lines, pyrotechnic firing pulses, and all connections
to the umbilical, safe/arm brackets/connectors and test connectors.
 
The harness consists of the following subassemblies:
* Payload Support Module Harness
* Bus Support Module Harness
* Harness to the Lander I/F
Furthermore the harness / cables are divided into three harness EMC
classes: power, signal and data, and the pyro harness. Their routing
is physically separated. In addition to the appropriate twisting and
shielding techniques this minimises the probability of electrical
cross talking of critical lines.
 
The harness design follows a distributed single point grounding
scheme. Redundant functions have their own connectors and are routed
in separate bundles and in a different way as far as practical.
 
All connectors supplying power have female contacts.
 
To achieve a complete Faraday cage around the harness each of the
harnesses has its own overall shield made of aluminium tape with an
overlap of at least 50 % for harnesses within the spacecraft and a
double shield for harnesses outside the spacecraft. As fixation
points for the harness aluminium bases (Ty-bases) are bonded to the
structure with a two component conductive glue. The distance of the
Ty-bases is selected such that the harness withstands all specified
environmental conditions.
 
To avoid interruptions of the shield between the connector and the
overall shield, redundant connection wires are used between connector
case and harness overall shield. In case of pyro-lines and sensible
interfaces conductive connector boots are implemented.
 
To prevent contamination the harness was baked-out in a thermal
vacuum chamber prior to integration.
 
 
Avionics Design
=====================================================================
 
The ROSETTA Avionics consists of the Data Management Subsystem (DMS)
and the Attitude and Orbit Control and Measurement Subsystem (AOCMS)
functions.
 
 
Data Management Subsystem (DMS)
-----------------------------------------------
The data management subsystem is in charge of telecommand
distribution to other spacecraft subsystems and payload, of
telemetry data collection from spacecraft subsystems and payload and
formatting, and of overall supervision of spacecraft and payload
functions and health.
 
The DMS is based on a standard OBDH bus architecture enhanced by high
rate IEEE 1355 serial data link between the different Avionics
processors and the SSMM, STR and CAM. The OBDH bus is the data route
for data acquisition and commands distribution via the RTUs. Payload
Instruments are accessed via a dedicated Payload RTU. Subsystems are
accessed via a dedicated Subsystem RTU.
 
DMS includes 4 identical Processor Modules (PM) located in 2 CDMUs.
Any of the processor modules can perform either the DMS or the AOCMS
processing. The PM selected for the DMS function acts as the bus
master. It is also in charge of Platform subsystem management (TTC,
Power, Thermal). The one selected as the AOCMS computer is in charge
of all sensors, actuators, HGA & SA drive electronics. TCdecoder and
Transfer Frame Generator (TFG) are included in each CDMU.
 
Telemetry can be downlinked via the TFG using the real time channel
(VC0) or in form of retrievals from the SSMM (VC1).
 
Solid State Mass Memory (SSMM)
- - - - - - - - - - - - - - - -
The Solid State Mass Memory (SSMM) is used like a 'Hard Disk Storage'
including 25 Gbit of memory. It contains a data compression module
which allows lossy (for CAM image) and loss-less (for HK and science
data) compression of data to be stored. It is able of file management
capability. It stores CAM images, science and telemetry packets as
well as software data for the AOCMS and DMS computer.
 
It is coupled to:
* the 4 processors via an IEEE 1355 link,
* the TFGs of the 2 CDMUs via a serial link,
* VIRTIS, OSIRIS and the Navigation Camera via a high data rate
serial link (IEEE 1355)
* the High Power Command Module (HPCM) selecting the valid PM
 
The lossy compression method (WAVELET) will be used for image data
compression of the NAVCAM or STR. The degree of compression can be
set by filter parameters from ground. The compression of OSIRIS and
VIRTIS image data could also be performed inside the SSMM. Present
baseline however is that these two instruments do not request data
compression from the system.
 
The SSMM SW runs on a Digital Signal Processor. The SSMM SW is made
of:
 
* The Init Mode Software
The Init mode software ensures the boot up of the SSMM and the
establishment of the communication with the DMS SW. It allows the
loading of the operational SW from EEPROM to RAM, and its starting.
 
* The Operational Software
The operational SW manages the files located in the Memory Modules of
SSMM, and the Data Compression Function that performs Rice lossless
and Wavelet lossy data compression.
 
The functionality of the SSMM can be summarised with the three points
below.
* Store on-board data in files. The on-board data can be both
scientific data and software images in files.
* Transmit the data stored in SSMM files to either an on-board User
or to the ground.
* Compress the stored files using both lossy and lossless compression
algorithms.
 
The Rosetta Solid State Mass Memory (SSMM) functionally consists of
the following modules:
* 2 Memory Controllers (MC)
* 3 Memory Modules (MM)
* 2 Power Converters, which supplies power to the memory controller
and memory module boards.
 
The Memory Controllers are responsible for all data transfer to and
from the Mass Memory, compression of data in the mass memory and
basic housekeeping functions (collection of telemetry packets,
configuration of the SSMM etc.). The Memory Controllers work in cold
redundancy.
 
The three Memory Modules are where the files are stored. The modules
can be turned on and off independently, giving the possibility to
increase and decrease the storage capacity of the SSMM. The Memory
Controllers access the Memory Modules via a memory module bus. Both
the Memory Controllers can access all three Memory Modules.
 
 
Attitude and Orbit Control Measurement System (AOCMS)
-----------------------------------------------------
 
The AOCMS is in charge of attitude and orbit measurement and control
and is in charge with sensors and actuators for autonomous attitude
determination and control as well as pre-programmed manoeuvring.
 
The AOCMS uses a decentralised architecture built around the AOCMS
Interface Unit (AIU) linked to all sensors / actuators and to the
Processor Modules included in the CDMUs:
 
* the AOCMS sensors: 2 Navigation Cameras (CAM) and 2 Star Trackers
(STR) having a common electronics unit, 4 Sun Acquisition Sensors
(SAS) and 3 Inertial Measurement Packages (3 IMP, each including 3
gyros + 3 acceleros),
 
* the AOCMS actuators: the Reaction Wheel Assembly (RWA), and
belonging to the Platform the Reaction Control System (RCS), the High
Gain Antenna Pointing Mechanism (HGAPM), and the 2 Solar Array Drive
Mechanisms (SADM).
 
AOCMS PM communication with AOCMS sensors (IMP, SAS, STR, CAM) and
actuators (RWA, RCS), and with pointing mechanism electronics
(SADE and HGAPE) is performed through the AIU. Functional AOCMS data
which need to be put in the Telemetry and sent to the ground are
given packetised by the AOCMS processor and sent to the DMS processor
for futher downlink to ground and storage in the SSMM.
 
The DMS PM permanently checks the AOCMS health by monitoring that the
AOCMS PM does not stop to communicate with DMS PM. This is done by
checking the correct reception of the so-called 'essential' AOCMS HK
packet every one second.
 
The AIU is the central data acquisition and distribution unit which
allows access to the sensors and actuators with different type of
interfaces. It includes RS 422, IEEE 1355 and MACS Bus interfaces as
well as analog and discrete digital interfaces for commanding and
data acquisition.
 
The AIU includes furthermore a 12 bit A/D converter in order to
convert analog signals from the pressure transducers (temperature and
pressure) precise enough for the fuel level prediction on-board of
Rosetta late in the mission, when the fuel level is critical.
 
The major AOCMS components are the following:
 * AOCMS Interface Unit (AIU): it interfaces to all AOCMS sensors and
actuators
 
* The Sun Acquisition Sensors (SAS): they are internally redundant
and are used for Sun Acquisition and pointing. They provide full sky
coverage and ensure a permanent sensing of the Sun direction vector.
 
* The Inertial Measurement Packages (IMP): The IMP function provides
roll rate and velocity measurements along 3 orthogonal axes.
 
* 4 Reaction Wheels: they are arranged in the Reaction Wheel Assembly
(RWA) and the Reaction Control System (RCS), in a tetrahedral
configuration about the S/C Y-axis in order to enhance the torque and
momentum capacity about that axis for the asteroid fly-by.
 
* 2 Autonomous Star Trackers: they contain an Autonomous Star Pattern
Recognition function and provide autonomously to the AOCMS an
estimated attitude quaternion and stellar measurements data.
 
* 2 Navigation Cameras (A&B) are used in the AOCMS control loop
during the Asteroid Near Fly-by Phase. The navigation cameras can
also directly send image data to the SSMM through a high data rate
link.
 
* Pointing mechanisms (through target pointing angles) and propulsion
thruster valves are commanded by the AOCMS through the AIU links.
 
 
Avionics external interface
----------------------------------------------
 
The Avionics system has the following external interface to other
subsystems of the Rosetta spacecraft:
 
* Interface with the Ground through TTC Subsystem:
  Ground Telecommands (TC) are checked, decoded and executed
  internally or sent to other subsystems, Telemetry (TM) data
  generated on-board are collected, formatted (if needed) and sent to
  Ground through TTC S/S, either in real time or in play-back after
  storage in SSMM, on ground request.
 
* Interface with Platform and Payload:
  The Avionics provides the experiments and Platform equipment with a
  hardware command capability (power On/Off commands, heater On/Off
  commands...),
 
  The Avionics provides experiments with a time synchronisation
  capability, so that the Ground can later on correlate results
  coming from different experiments,
 
  The Avionics uses for attitude and communication control purpose as
  well as for power generation Platform equipment: Reaction Control
  System (RCS), High Gain Antenna and Solar Array Pointing Mechanisms
  (HGAPM, SADM)
 
  Housekeeping data and experiment science data are collected
  on-board to be sent to Ground in real time TM, or to be stored for
  play-back downlink,
 
  The Avionics S/W provides experiments and Platform with a
  processing capability, in form of application programs (AP) or
  On-board Control Procedures (OBCP), coded and implemented by the
  Avionics/OBCP contractor, but specified by the users to allow
  montoring/surveillance, thermal control, experiment or mechanism
  management.
 
 
Avionics modes
=====================================================================
 
The Avionics modes derived from the AOCMS modes are the following:
 
Stand-By Mode
--------------
The SBM is used in Pre-launch and Launch Modes for general check
supervision. Only DMS functions are activated. It is possible to
command thrusters through AIU for RCS Priming.
 
Sun Acquisition Mode
---------------------
This mode is used during Separation Sequence to perform rate
reduction (if necessary), Sun acquisition and Sun pointing. SAM is
also used as second level back-up mode to recover Sun pointing
attitude in case of an unsuccessful back-up to Sun Keeping Mode.
 
Safe/Hold Mode
---------------
The SHM follows the Sun Acquisition Mode / Sun Keeping Mode to
achieve a 3-axis attitude based on star trackers, gyros and reaction
wheels, with solar arrays pointing towards the Sun and Medium and
High Gain Antennae (i.e. S/C Xaxis) pointing towards the Earth and
the Y-axis normally pointing to the noth of the ecliptic plane.
 
In some mission phases (i.e. defined by the minimum earth distance),
S/C X-axis pointing towards the Earth is forbidden because of thermal
constraints. Then, +X axis is pointed towards the Sun, and the High
Gain Antenna is pointed towards the Earth.
 
Normal Mode
------------
The NM is used in Active Cruise and Near Comet phases for nominal
longterm operations, for comet observation and SSP delivery. Reaction
wheel off-loading is a function of the Normal Mode.
 
Thruster Transition Mode
-------------------------
The TTM is used for transition from Normal Mode to operational
thruster Modes, and vice-versa, for control tranquillisation.
 
Orbit Control Mode
------------------
The OCM is used in Active Cruise Mode for trajectory and orbit
corrections.
 
Asteroid Fly-By Mode
--------------------
The AFB mode is dedicated to asteroid observation.
 
Near Sun Hibernation Mode
-------------------------
The NSHM is a 3-axis controlled mode (with the attitude estimation
based on the use of STR only, and no gyro), with a dedicated thruster
control (i.e. single sided) to minimise the fuel consumption.
 
Spin-up Mode
------------
The SpM is necessary to spin up the spacecraft at hibernation entry
(spin down at hibernation exit is achieved by Sun Keeping Mode). The
attitude control concept is a completely passive inertial spin during
the deep space hibernation phase.
 
There is no AOCMS Deep Space Hibernation Mode.
 
Sun Keeping Mode
----------------
The Sun Keeping Mode is used nominally at wake-up after Deep Space
hibernation, and as first level back-up mode to recover Sun pointing
attitude in case of a failure involving the Avionics and for which a
local reconfiguration on redundant units is not efficient. In case
the autonomous entry to Safe / Hold Mode is disabled or not
successful Earth Strobing Mode is established leading to a slow spin
motion around the Sun direction. Then the + X-axis is pointed towards
the expected earth direction (i.e. using the actual Sun/spacecraft/
Earth angle). The rotation along the Sun line is maintained therefore
the Earth crosses once per revolution the + X-axis which will allow
communication with the MGA.
 
System Level Modes
=====================================================================
 
A basic conficuration of the system level modes is given below:
 
Pre-launch      only DMS on, AOCMS PM on, external power supply
Mode
 
Launch Mode     Initially: DMS on, SSMM in standby with 1 MM,
                AOCMS PM on, separation sequence program running,
                power supply from batteries Finally: DMS on, AOCMS
                in Sun Acquisition Mode, TTC S-band downlink on,
                power supply from solar arrays, X-axis and solar
                arrays Sun pointing.
 
Activation      DMS on, AOCMS in Normal Mode, TTC S- or X-band
Mode            downlink via HGA (initially in S-band via LGA),
                3-axis stabilised, SA Sun pointing attitude
 
Active Cruise   DMS on, AOCMS in Normal Mode or Orbit Control
Mode            Mode, TTC S- or X-band downlink via HGA, 3-axis
                stabilised, SA Sun pointing attitude
 
Deep Space      CDMU on, AOCMS in SBM mode, inertial spin
Hibernation     stabilisation mode, wake-up timers on, thermostat
Mode            control of heaters
 
 
Near Sun        DMS on, AOCMS in NSHM, 3-axis active control mode
Hibernation     with 2 PMs, star tracker, thrusters, X-axis Sun or
Mode            Earth pointing
 
Asteroid        DMS on, TTC X-band downlink via HGA, SA Sun
Fly-by Mode     pointing, payload on, AOCMS in AFM mode: closed loop
                asteroid tracking with navigation camera, during Near
                Fly-by: HGA tracking stopped
 
Near Comet      DMS on, TTC X-band downlink via HGA, navigation
Mode            camera and payload on, AOCMS in Normal Mode: 3-axis
                stabilised, SA Sun pointing, instruments comet
                pointing;
 
Safe Mode       DMS on, AOCMS in Safe/Hold Mode; SA Sun pointing, X-
                axis Sun or Earth pointing, 3-axis stabilised using
                gyros, star tracker, RWs(if enabled by ground); TTC
                S-Band downlink via HGA; RXs on HGA/LGA; payload off
 
Survival Mode   DMS on, AOCMS in SKM submode 'MGA Strobing' (or in
                SKM if this submode is disabled), SA Sun pointing
                with offset from +X-axis = SSCE angle, fixed small
                residual rate around Sun vector; control by
                thrusters, Sun sensors, gyros; S-Band carrier
                downlink via MGA, RXs on MGA/LGA, load off
 
 
Ground Segment
=====================================================================
 
Ground Station and Communications Network performing telemetry,
telecommand and tracking operations within the S/X-band frequencies.
Telecommand will always be in the S-band, whilst telemetry will be
switchable between S- and X-band, with the possibility to transmit
simultaneously in both frequency bands, only one of which will be
modulated (S-band down-link is primarily used during the near Earth
mission phases). The ground station used throughout all mission
phases will be the ESA Perth 32m deep-space terminal (complemented by
the ESA Kourou 15m station during near-Earth mission phases). In
addition, the NASA Deep Space Network (DSN) 34m and/or 70m network is
envisaged for back-up and emergency cases.
 
New Norcia      Dur.   Start-Date        End-Date
--------------------------------------------------
NNO Daily       129d    26/02/04         03/07/04
NNO Weekly      64d     04/07/04         05/09/04
NNO Daily       56d     06/09/04         31/10/04
NNO Weekly      61d     01/11/04         31/12/04
NNO Weekly      30d     01/01/05         30/01/05
NNO Daily       116d    31/01/05         26/05/05
NNO Daily       52d     27/05/05         17/07/05
NNO Weekly      63d     18/07/05         18/09/05
NNO Daily       7d      19/09/05         25/09/05
NNO Weekly      21d     26/09/05         16/10/05
NNO Daily       7d      17/10/05         23/10/05
NNO Weekly      28d     24/10/05         20/11/05
NNO Monthly     41d     21/11/05         31/12/05
NNO Monthly     50d     01/01/06         19/02/06
NNO Daily       16d     20/02/06         07/03/06
NNO Weekly      13d     08/03/06         20/03/06
NNO Daily       48d     21/03/06         07/05/06
NNO Weekly      14d     08/05/06         21/05/06
NNO Daily       3d      22/05/06         24/05/06
NNO Weekly      28d     25/05/06         21/06/06
NNO Monthly     32d     22/06/06         23/07/06
NNO Weekly      35d     24/07/06         27/08/06
NNO Daily       63d     28/08/06         29/10/06
NNO Weekly      28d     30/10/06         26/11/06
NNO Daily       28d     27/11/06         24/12/06
NNO Weekly      7d      25/12/06         31/12/06
NNO Weekly      31d     01/01/07         31/01/07
NNO Daily       122d    01/02/07         02/06/07
NNO Weekly      28d     03/06/07         30/06/07
NNO Monthly     71d     01/07/07         09/09/07
NNO Weekly      21d     10/09/07         30/09/07
NNO Daily       74d     01/10/07         13/12/07
NNO Weekly      18d     14/12/07         31/12/07
NNO Weekly      10d     01/01/08         10/01/08
NNO Daily       7d      11/01/08         17/01/08
NNO Weekly      28d     18/01/08         14/02/08
NNO Monthly     136d    15/02/08         29/06/08
NNO Daily       129d    30/06/08         05/11/08
NNO Weekly      56d     06/11/08         31/12/08
NNO Weekly      21d     01/01/09         21/01/09
NNO Weekly      28d     22/01/09         18/02/09
NNO Daily       65d     19/02/09         24/04/09
NNO Weekly      28d     25/04/09         22/05/09
NNO Monthly     105d    23/05/09         04/09/09
NNO Weekly      28d     05/09/09         02/10/09
NNO Daily       79d     01/10/09         18/12/09
NNO Weekly      13d     19/12/09         31/12/09
NNO Daily       63d     01/01/10         04/03/10
NNO Monthly     62d     05/03/10         05/05/10
NNO Daily       144d    06/05/10         26/09/10
NNO Weekly      42d     27/09/10         07/11/10
NNO Daily       54d     08/11/10         31/12/10
NNO Daily       102d    01/01/11         12/04/11
NNO Weekly      37d     13/04/11         19/05/11
NNO Daily       55d     20/05/11         13/07/11
NNO Daily       343d    23/01/14         31/12/14
NNO Daily       365d    01/01/15         31/12/15
 
 
Cebreros
---------------------
Support of the ESA Cebreros ground station is scheduled for 90 days
between the 18-Aug-2014 and the 15-Nov-2014 to support comet
characterization and Lander delivery.
 
 
Kourou          Dur.    Start-Date       End-Date
---------------------------------------------------
Kourou 1        14d     26/02/2004      11/03/2004
Kourou 2        30d     04/02/2005      05/03/2005
Kourou 3        30d     22/10/2007      20/11/2007
Kourou 4        30d     22/10/2009      20/11/2009
 
The support around the Earth swing-by is limited to a few passes
close to the swing-by and a few weekly passes prior to the swing-by
to verify the compatibility between the ground station and the
spacecraft.
 
 
NASA DSN        Dur.   Start-Date        End-Date
--------------------------------------------------
DSN1            14d     26/02/04         10/03/04
DSN2            93d     26/02/04         29/05/04
DSN3            7d      03/06/04         09/06/04
DSN4            42d     06/09/04         17/10/04
DSN5            30d     17/02/05         18/03/05
DDOR Check      14d     07/08/06         20/08/06
DSN6            38d     01/09/06         08/10/06
DDOR1           14d     09/10/06         22/10/06
DSN7            155d    23/10/06         26/03/07
DSN8            30d     31/10/07         29/11/07
DSN9            40d     08/08/08         16/09/08
DSN10           30d     28/10/09         26/11/09
DSN11           40d     12/06/10         21/07/10
DSN12           115d    10/11/10         04/03/11
DSN13           30d     05/03/11         03/04/11
DSN14           153d    23/01/14         24/06/14
DSN15           34d     23/07/14         25/08/14
DSN16           28d     25/10/14         21/11/14
 
 
 
Acronyms
------------------------------
For more acronyms refer to Rosetta Project Glossary [RO-EST-LI-5012]
 
AFB     Asteroid Fly-By
AFM     Asteroid Fly-by Mode
AIU     AOCMS Interface Unit
AOCMS   Attitude and Orbit Control Measurement System
AOCS    Attitude and Orbit Control System
AP      Application Programs
APM     Antenna Pointing Mechanism
APME    APM Electronics
APM-M   APM Motor
APM-SS  APM Support Structure
ARA     Attitude Reference Assembly
AU      Astronomical Unit
BCR     Battery Charge Regulator
BDR     Battery Discharge Regulator
BSM     Bus Support Module
CAM     Navigation Camera
CAP     Comet Acquisition Point
CAT     Close Approach Trajectory
CDMU    Control and Data Management Unit
CFRP    Carbon Fibre Reinforced Plastic
CNES    Centre National d'Etudes Spatiales
COP     Close Observation Phase
DDOR    Delta Differential One-way Range
DLR     German Aerospace Center
DMS     Data Management Subsystem
DSHM    Deep Space Hibernation Mode
DSM     Deep Space Manouver
DSN     Deep Space Network
EEPROM  Electronically Erasable Programmable Read-Only Memory
EMC     Electromagnetic Compatibility
ESA     European Space Agency
ESD     Electro Static Discharge
ESOC    European Space Operations Center
ESTEC   European Space Research and Technology Center
EUV     Extreme UltraViolet
FAT     Far approach trajectory
FCL     Fold-back Current Limiters
FDIR    Failure Detection Isolation and Recovery
F/D     Focal Diameter
FOV     Field Of View
FUV     Far UltraViolet
GCMS    Gas Chromatography / Mass Spectrometry
GMP     Global Mapping Phase
HDRM    Hold-Down and Release Mechanism
HGA     High Gain Antenna
HGAPE   High Gain Antenna Pointing Electronics
HGAPM   High Gain Antenna Pointing Mechanism
HgCdTe  Mercury Cadmium Telluride
HIGH    High Activity Phase (Escort Phase)
HPA     High Power Amplifier
HPCM    High Power Command Module
HK      HouseKeeping
I/C     Individually Controlled
I/F     InterFace
IMP     Inertial Measurement Packages
IMU     INERTIAL MEASUREMENT UNITS
IRAS    InfraRed Astronomical Satellite
IRFPA   InfraRed Focal Plane Array
IS      Infrared Spectrometer
HRM     HGA Holddown & Release Mechanism
H/W     Hard/Ware
KAL     Keep Alive Lines
LCC      Lander Control Center
LCL     Latching Current Limiters
LEOP    Launch and Early Orbit Phase
LGA     Low Gain Antenna
LILT    Low Intensity Low Temperature
LIP     Lander Interface Panel
LOW     Low Activity Phase (Escort Phase)
MACS    Modular Attitude Control System
MEA     Main Electronics Assembly
MC      Memory Controlller
MGA     Medium Gain Antenna
MGAS    MGA S-band
MGAX    MGA X-band
MINC    Moderate Increase Phase (Escort Phase)
MLI     Multi Layer Insulation
MM      Memory Module
MMH     MonoMethylHydrazine
MPPT    Maximum Power Point Trackers
MS      Microscope
NM      Normal Mode
NNO     New Norcia ground station
NSHM    Near Sun Hibernation Mode
NTO     Nitrogen TetrOxide
OBCP    On-Board Control Procedures
OBDH    On-Board Data Handling
OCM     Orbit Control Mode
OIP     Orbit Insertion Point
PCU     Power Conditioning Unit
PDU     Power Distribution Unit
PI      Principal Investigator
P/L     PayLoad
PL-PDU  Payload Power Distribution Unit
PM      Processor Module
PSM     Payload Support Module
PSS     Power SubSystem
RAM     Random Access Memory
RCS     Reaction Control System
RF      Radio Frequency
RFDU    RF Distribution Unit
RJ      Rotary Joints
RMOC    Rosetta Mission Operations Center
RL      Rosetta Lander
RLGS    Rosetta Lander Ground Segment
RO      Rosetta Orbiter
RSI     Radio Science Investigations
RSOC    Rosetta Science Operations CenterRTU
RVM     Rendez-vous Manouver
RW      Reaction Wheel
RWA     Reaction Wheel Assembly
SA      Solar Array
SADE    Solar Array Drive Electronics
SADM    Solar Array Drive Mechanism
SAM     Sun Acquisition Mode
SAS     Sun Acquisition Sensors
SBM     Stand-By Mode
SHM     Safe/Hold Mode
SAS     Sun Acquisition Sensor
S/C     SpaceCraft
SI      Silicon
SINC    Sharp Increase Phase (Escort Phase)
STP     System Interface Temperature Points
SKM     Sun Keeping Mode
SONC    Science Operations and Navigation Center
SpM     Spin-up Mode
S/S     SubSystem
SSMM    Solid State Mass Memory
SSP     Surface Science Package
SS-PDU  Subsystems Power Distribution Unit
STR     Star TRacker
S/W     SoftWare
SWT     Sience Working Team
TC      Telecommand
TC      Telecommunications
TCS     Thermal Control Subsystem
TFG     Transfer Frame Generator
TGM     Transition to global mapping
TK      Thermal Knives
TM      Telemetry
TRP     Temperature Reference Point
TTC    Tracking, Telemetry and Command
TTM     Thruster Transition Mode
TWTL    Two Way Travelling Lighttime
TWTA    Travelling Wave Tube Amplifiers
USO     Ultra Stable Oscillator
VC      Virtual Channel
WG      WaveGuide
WIU     Waveguide Interface Unit
 

        