
Lander overview
=============================================
The Philae Lander is a box-type unit with the dimensions
of 850 x 850 x 640 mm3. On the comet, it will rest on a tripod
called Landing Gear, with a diameter of 2.6 m and will be fixed to
the comet's surface by harpoons.
 
Philae is composed of three different parts, corresponding to its
structural design:
 
1)    Internal compartment:
This compartment hosts almost all subsystems and most of the
experiment units. It provides a temperature controlled environment
for all electronics and is built by the structural elements of an
Instrument platform and so called Pi-plates. It is surrounded by
Multilayer Insulation built of 2 tents to achieve the required
insulation at a low power environment on the comet at 3 AU distance
from Sun.
 
2)    Solar Hood:
The solar hood is built around the internal compartment and its MLI
tents, the shape follows the overall Lander shape. It hosts the solar
arrays of the Lander composed by 6 different panels. In addition two
absorber foils are mounted on the solar hood lid. These foils are
built by thin copper foils with an external TINOX surface, high
absorptivity and low emissivity, used to collect solar irradiation
and transform it into heat radiated into the internal compartment.
The solar hood also carries the camera system of the Lander, with one
camera head on each panel, thus providing a 360 degrees panoramic
view.
 
3)    Baseplate / Balcony:
The baseplate is the central structural plate carrying the solar hood
with the internal compartment underneath and providing at one end a
special area called balcony. This area hosts all experiments or parts
of them, especially the sensors, which require direct access to the
comet environment and the comet surface.
The baseplate is also the interface panel to the Landing Gear.
In addition the baseplate hosts the Push plate, which is the
interface to the Orbiter during the 10 years cruise from Launch to
the Comet.
 
The Lander mass is around 100 kg.
 
In addition three units of the Lander system are mounted on the
Orbiter, and will remain there after Lander separation for the comet.
These units provide the interfaces to the Orbiter: electrical and
data (ESS) and mechanical (MSS). The third system is a TxRx system
used to keep contact to the Lander during its operational phase on
the comet.
 
 
Lander Mission Requirements and Constraints
=============================================
The Lander is designed to fullfill the mission requirements given as:
- survive the 10 years cruise phase with long hibernation phases under
  autonomous thermal control powered by the Orbiter,
- land safely on the comet,
- provide a scientific phase after landing at 3 AU distance from Sun
  with online data transmission,
- provide a long term mission capability observing the comet on its
  way from 3 AU to the Sun
 
 
Lander Platform Definition
=============================================
The Lander platform is built by three major subsystems, required to
operate the Lander throughout the mission:
-    a Power subsystem (PSS) composed of a Battery system with a
        Primary Battery and a Secondary Battery, the later refilled
        by a Solar array generator, and the required electronics to
        distribute and control the power flow inside the Lander,
-    a Central Data Management System (CDMS), composed by two hot
        redundant computers, controlling all activities on the
        Lander, especially on the comet in an autonomous manner,
-    a Thermal Control System, composed by a 2-tent
        MultiLayerInsulation supported by two absorber foils and an
        electrical heater system. Additional independant heater
        systems are used during the cruise phase, especially when the
        Lander is in hibernation, and on the comet, when the Lander
        runs out of power and changes into a so called Wake-up mode,
        to provide a thermal environment in the Internal compartment
        as required to switch-on the Lander electronics.
 
 
Subsystem Definiton
=============================================
In addition to the already described platform units PSS, CDMS and TCS
and the On-Orbiter units ESS, MSS and ESS-TxRx, a set of subsystems
is installed on the Lander.
 
The Active Descent System ADS provides a 1-axis thruster system used
at touch-down to support the landing and prevent a rebounding until
the harpoons are shot.
An Anchoring system, built by two redundant harpoons, is used to fix
the Lander to the comet's surface after landing and provide the
required counter-force during drilling.
A Flywheel providing a 1-axis momentum wheel used to stabilize the
Lander's descent to the comet.
The Landing gear provides the necessary interface between the Lander
and the comet and supports Lander science operations by a rotation
and tiliting capability.
The structure subsystem provides the required structural elements to
built up the Lander.
A TxRx system is installed to provide access to the Lander and enable
data retrievel during its mission phase on the comet.
 
 
Lander Reference Frame
=============================================
The Lander reference frame is defined as follows:
+Z-axis is perdendicular to the baseplate, generally pointing away
from the comet towards space, during cruise parallel to the Orbiter
+Z-axis, +X-axis is generally parallel to the comet surface, pointing
opposite of the Lander's balcony, into the direction of Lander
separation from the Orbiter, during cruise into Orbiter -X direction,
+Y-axis completes the right-handed frame.
 
The frame origin is located on the upper surface of the balcony
(Z = 0), in the middle of the balcony (Y = 0), at the outer end
(X = 0).
 
 
 
Lander Operating Modes
=============================================
The Lander is operated in the following modes:
 
Hibernation Mode:
This mode is defined as: Lander attached to the Orbiter, Orbiter LCL
5A or 5B ON, Lander Hibernation heater ON (dissipation > 12W at 28V),
no power on the Lander Primary Bus
In this mode the Lander is non-operational but under thermal control
with a hibernation temperature inside the internal compartment above
minus 55 degC at the reference point.
 
Wake-up Mode:
This mode is applied on the comet, substituting the Hibernation Mode.
The PSS wake-up thermostats are closed, because the temperature
inside the internal compartment is below minus 53 degC. In this mode
the Lander is non-operational, the Lander operational electronics are
disconnected from the Primary Bus and the wake-up heaters are
connected to the Primary Bus. In this mode NO thermal control is
possible, since the wake-up heaters will only dissipate, if the
Primary Bus is powered, which requires Sun irradiation on the comet to
operate the solar arrays. Without dissipation the compartment
temperature will drop until the comet environmental temperature. When
the Lander is still attached to the Orbiter and powered from the
Orbiter-LCL 15A/B, an additional heater set will also dissipate.
 
Power Enough Mode:
This mode follows the Wake-up mode, the Lander Primary Bus is
powered, but the voltage is still below 18.5V, which correspond to a
non-sufficient power situation. The available power is not lost,
since special Power Enough loads are used to dissipate and heat the
internal compartment.
 
Stand-by Mode:
The Lander is operational, since the Lander basic operational
electronics (PCU, CDMS and one TCU) are connected to the Primary Bus
and powered.
In this mode thermal control will be performed from the dissipation
of the activated units. If the temperature of the internal
compartment drops below the TCU set-points, the respcetive TCU
heaters will also dissipate.
 
Operational Modes:
These modes define Lander operation of Experiments.
 
  ###########TO BE COMPLETED BY SONC ############

        