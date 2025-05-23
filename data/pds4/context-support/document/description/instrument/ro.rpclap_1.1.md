
 
 
Instrument Overview
===================
 
The Langmuir probe instrument (RPC-LAP) is part of the set of
Rosetta orbiter instruments known as the Rosetta Plasma
Consortium (RPC). The purpose of the LAP is to provide
measurements of several plasma parameters in the parts
of space visited by Rosetta, primarily the cometary
environment. LAP uses two Langmuir probes to access
primarily the following plasma parameters:
 
- Plasma (electron) density (ne)
- Electron temperature (Te)
- Spacecraft potential (Vsc)
- Plasma drift speed (v)
- Plasma fluctuations and waves up to 8 kHz (dn/n, E)
 
Not all parameters can be derived in all regions, and
the methods for deriving a particular parameter can vary
from region to region.
 
This catalog file gives a brief overview. For more details,
please see the instrument description in Space Science
Reviews (full reference at end of this file).
 
 
Scientific objectives
=====================
 
1. By monitoring the development of plasma density,
electron temperature and flow speed from the onset of
cometary activity to the perihelion, LAP will significantly improve
our view of cometary outgassing and the formation and structure of the
cometary plasma environment.
 
2. By studying time and space variations of the fluid parameters
of the inner coma, LAP will pave the way for a detailed
understanding of this region, including the diamagnetic cavity
where no in-situ observations have previously been made.
 
3. By its ability to measure plasma density structures, LAP can
investigate dynamic features in the cometary
environment that can be compared to and linked to comet
surface events as observed by other Rosetta orbiter instruments.
 
4. By measuring density fluctuations and electric field variations
from zero frequency up to 8~kHz, LAP will be able to investigate
the stability and dynamics of the cometary plasma environment in
different stages of cometary activity. This is of particular
interest on and inside the contact surface (diamagnetic cavity boundary),
which defines the inner limit of penetration of magnetic fields
and plasma of solar wind origin into the cometary plasma environment.
 
5. By analysing LAP data together with data from other
RPC instruments, it will be possible to investigate a
broad range of problems no single RPC instrument could
cover on its own. Examples are interactions between low
frequency waves and plasma particles (LAP-ICA-IES),
MHD waves and contact surface properties (LAP-MAG), and
wave-wave interactions (LAP-MIP).
 
 
 
Measurement principles
======================
 
A spherical Langmuir probe is a conceptually simple device, but
is nevertheless able to provide data on a multitude of plasma
parameters. The use of two probes extends these possibilities
further, particularly when coupled to versatile electronics.
LAP implements several measurement principles:
 
- Bias voltage sweeps: yields ne and Te in dense (a few hundred
  electrons per cm3 and more) plasmas; photoemission saturation
  current in tenuous plasmas (below a few hundred cm-3); spacecraft
  potential (actually spacecraft-to-probe potential) in all plasmas.
- Probe current variations: yields plasma density fluctuations (dn/n)
  in dense plasmas; electric field variations in low density plasmas.
- Electric fields and spacecraft potential: Yields spacecraft potential,
  from which the plasma density can be derived in low density plasmas,
  and electric wave fields.
 
For a full description of the measurement modes, see the published
instrument descriptions ERIKSSON2007A and ERIKSSON2008A, provided in
the DOCUMENT directory.
 
 
 
RPC-LAP characteristics in brief
================================
 
+ Two spherical probes of radius 25 mm
+ Mounted at the tips of two booms of length 2.24 m and 1.62 m,
  respectively
+ Probe surface coating: titanium nitride
+ Each probe can individually operate in bias voltage or bias
  current mode
+ Bias voltage range +-31 V
+ Bias current range +-44 nA
+ One high-rate (18.75 kHz, 16 bit) and one low-rate (57.8 Hz, 20 bit)
  ADC for each probe
+ Current measurement range +-0.2 mA in low gain mode
+ Current measurement range +-0.01 mA in high gain mode
+ Voltage measurement range +-40 V
+ Analog anti-aliasing filters at 20 Hz, 4 kHz or 8 kHz
+ Flexible digital filters in flight software
+ Internal offset determination and calibration by possibility
  to sweep over open probe or internal resistor
+ One of the probes (Probe 2) can be used by RPC-MIP in its long Debye
  length mode
 
 
LAP Sensor Locations
====================
 
The LAP sensors, known as LAP1 and LAP2, probe 1 and probe 2,
or P1 and P2, are mounted at the tips of the two spacecraft
booms, of length 2.24 m and 1.62 m. In the spacecraft coordinate
system, the probes and the hinges at the boom roots are located
in the following positions:
 
Unit        x [m]     y [m]     z [m]
-------------------------------------
Probe 1     -1.19      2.43      3.88
Hinge 1     -1.19      0.85      2.30
Probe 2     -2.48      0.78     -0.65
Hinge 2     -1.19      0.65      0.30
 
In this system, the solar panels extend in the y directions,
while the +z direction is the nominal comet pointing direction.
The booms are mounted on the -x surface, where the Rosetta
lander (Philae) is carried during the cruise to the comet.
 
====================
 
Operations
==========
 
LAP has a wide variety of possible operational modes. An overview
of the various possible settings is provided in the instrument
descriptions ERIKSSON2007A and ERIKSSON2008A in the DOCUMENT directory.
The latter of these references give examples of how the variety of
LAP operational settings are condensed into 'macros', fully defining
the instrument operations from the time the macro is started. See
also the section on LAP operational modes in the EAICD.
 
 
 
RPC-LAP key people
==================
 
PI:          Anders Eriksson, Swedish Institute of Space Physics, Uppsala
TM:          Lennart Ahlen, Swedish Institute of Space Physics, Uppsala
Software:    Reine Gill, Swedish Institute of Space Physics, Uppsala
Archiving:   Liza Dackborn, Swedish Institute of Space Physics, Uppsala
 
References
==========
 
ERIKSSON2007A and ERIKSSON2008A in the DOCUMENT directory.

        