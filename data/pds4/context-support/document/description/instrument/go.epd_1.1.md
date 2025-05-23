
 
     The Galileo Energetic Particles Detector is fully described by
Williams et al [WILLIAMSETAL1992].
 
INTRODUCTION
 
     Jupiter possesses the largest planetary magnetosphere in the
solar system.  It is the largest in spatial dimension, has the highest
trapped particle energies and intensities, has the greatest
compositional variety in its major particle populations, displays the
largest co-rotational effects and has the largest number of moons
within the magnetosphere that provide both strong sources for and
losses of the observed particle populations.  These characteristics,
uncovered by the Pioneer and Voyager flybys demand an instrument
design capable of accommodating the great range in parametric values
established by these extremes.
 
     Within the Jovian magnetosphere, the energetic (>=20 keV)
particle populations play an important dual role.  First, they
represent a major factor in determining the size, shape, and dynamics
of the system.  For example, observations of energetic particle
intensities and corresponding energy densities show that these
populations are important in (1) standing off the solar wind and
thereby determining magnetopause position; (2) determining the general
magnetic field configuration in the evening magnetosphere and (3)
establishing the bulk of the ring current responsible for the
magnetodisk configuration of the middle-Jovian magnetosphere.
 
     Secondly the energetic particles play an important diagnostic
role in the determination of energization, transport, and loss
processes active in the Jovian magnetosphere.  In this role they also
provide a remote sensing capability for identifying magnetospheric
structures through finite gyroradius effects and for diagnosing remote
processes through field-aligned flow, E x B drift, and magnetic drift
effects.
 
     The Galileo EPD will provide major extensions to the Jovian
energetic particle data base obtained from the Pioneer and Voyager
flybys.  For example:
(1)  Galileo will be placed into a highly elliptical orbit around
Jupiter.  The nominal two-year mission lifetime will allow both a
direct measure of time variations in the Jovian magnetosphere and a
significantly larger spatial sample of the system than has been
possible with the previous flybys.
(2) The nominal mission includes several close ( < 1000 km) flybys of
the Galilean satellites thereby providing the best opportunity to date
to observe details of the satellite/magnetospheric interactions.
(3)  The EPD provides the first 4-pi steradian angular coverage for
Jovian energetic particles, thereby assuring that the necessary
energetic particle measurements will be obtained independent of
satellite orientation and magnetic field direction.
(4)  The low-energy thresholds of the EPD effectively close the energy
gap between plasma and energetic particle measurements that has
existed in previous observations and assures that processes thought to
operate in that gap will be tested by direct observation.  For
example, it has been suggested that the particles powering Jovian
aurora are ions of energies <=100 keV/nucl, a composition energy range
to be measured by Galileo instrumentation at Jupiter.
 
EPD OVERVIEW
 
     The EPD instrument is the result of a joint effort between The
Johns Hopkins University Applied Physics Laboratory (JHU/APL), The
Max-Planck-Institute fur Aeronomie (MPAe) and The National Oceanic and
Atmospheric Administration Space Environment Laboratory (NOAA/SEL).
Proposed in 1976 with initial funds received in late 1977, the EPD was
launched onboard the Galileo spacecraft on October 12, 1989.  The MPAe
was responsible for the detector heads and three analog circuit boards
associated with those heads.  The NOAA/SEL was responsible for the
original time-of-flight (TOF) circuitry.  The TOF circuitry employed
in the upgraded TOF detector actually flown (and described in the
composition measurement system, CMS, section) was the joint
responsibility of MPAe and JHU/APL.  The JHU/APL was responsible for
all remaining electronics, the scanning motor, the data system,
instrument power, structure test, instrument integration, and
spacecraft integration.  Calibrations were performed by JHU/APL and
MPAe.
     The general characteristics of the EPD are listed in the
following table:
 
------------------------------------------------------------------------
      Galileo Energetic Particle Detector (EPD) characteristics
------------------------------------------------------------------------
Mass: 10.5kg   Power: 6W electronics; 4W heaters    Bit rate: 912bps
Size: 19.5cm x 27cm x 36.1cm
 
Two bi-directional telescopes mounted on stepper platform
 
4pi steradian coverage with 52 to 420 samples every 7 S/C spins (~140s)
 
Geometric factors: 6E-03 - 5E-01 cm^2/sr, dependent on detector head
 
Time resolution: 0.33-2.67 s dependent on rate channel
 
Magnetic deflection, deltaE x E, and time-of-flight systems
 
Energy coverage: (Mev/nucl)
0.02-55        Z>=1
0.025-15.5     Helium
0.012-10.7     Oxygen
0.01-13        Sulfur
0.01-15        Iron
0.015-11  Electrons
 
64 rate channels plus pulse height analysis
------------------------------------------------------------------------
 
     The two bi-directional solid-state detector telescopes are the
Low Energy Magnetospheric Measurement System (LEMMS) and the
Composition Measurement System (CMS).  These detector heads are
mounted on a platform and rotated by a stepper motor contained in the
main electronics box.  The combination of the satellite spin and the
stepper motor rotation (nominally stepping to the next position after
each spacecraft spin) provides 4 pi steradian coverage of the unit
sphere.  The 0 degree ends of the two telescopes have a clear field of
view over the unit sphere and also can be positioned behind a
foreground shield/source holder for background measurements and
in-flight calibrations.  The 180 degree ends experience obscuration
effects in motor positions 4, 5, and 6 caused by the magnetometer boom
and foreground shield.
     The zero degree end of the LEMMS unit uses magnetic deflection
to separate electrons from ions and provides, from detectors A and B,
total-ion energy above ~20keV and from detectors E1, E2 and F1, F2
electron spectra above ~15keV.  The 180 degree end of LEMMS uses
absorbers in combination with detectors C and D to provide
measurements of ions >~16Mev and electrons >~2Mev.
     The zero degree end of the CMS telescope employs a
time-of-flight (TOF) versus total energy technique to measure
elemental energy spectra above ~10keV/nucl for helium through iron.  A
sweeping magnet in the entrance collimator prevents electrons with
energies <~256keV from entering the system.  TOF start and stop pulses
are generated as the incoming ions pass, respectively, through a thin
entrance foil and impinge on the detector KT.  Electrons released from
the foil and the detector are accelerated and deflected through a
series of grids and are detected by the microchannel places, MCP1 and
MCP2.  The time difference between the start pulse, MCP1, and the stop
pulse, MCP2, is then obtained, along with the ion total energy from
KT.  Knowing the ion total energy and its travel time through the
system (which gives its velocity), the ion mass is determined.
     The 180 degree end of the CMS telescope measures the ion
energy loss, deltaE, as the ions pass through detectors Ja and Jb and
the ion residual energy E=E(total) - deltaE, as they impact detectors
Ka and Kb.  The resulting deltaE and E measurement provides a measure
of ion composition for energies >~200keV/nucl.
     The planned normal mode of EPD operation is to have both the
telescopes powered and to step the stepper platform once each
satellite spin.  This will yield a 4-pi scan of the unit sphere
approximately every 140s.  Many other scanning modes are available and
will be used for special circumstances.  For example, during satellite
encounters, the EPD will be configured to scan particular directions
such as the expected direction of the magnetic flux tube, the
direction of the Galilean satellite wakes as they travel through the
Jovian magnetosphere, and the direction of the E x B drift paths.
 
     The following table contains the channel energy ranges and
geometric factors for the detectors on the LEMMS telescope.
 
Channel         Species         Energy Range    Geometric Factor
Name                            (MeV)           (cm**2 sr)
------------------------------------------------------------------------
A0              Z >= 1          0.022-  0.042   0.006
A1              Z >= 1          0.042-  0.065   0.006
A2              Z >= 1          0.065-  0.120   0.006
A3              Z >= 1          0.120-  0.280   0.006
A4              Z >= 1          0.280-  0.515   0.006
A5              Z >= 1          0.515-  0.825   0.006
A6              Z >= 1          0.825-  1.68    0.006
A7              Z >= 1          1.68 -  3.20    0.006
A8              Z >= 2          3.50 -  12.4    0.006
B0              Z  = 1          3.20 -  10.1    0.006
B1              electrons       ~1.5 -  10.5    0.006
B2              Z  = 2          16.0 -  100.    0.006
DC0             Z >= 1          14.5 -  33.5    0.5
DC1             Z >= 1           51. -  59.     0.5
DC2             electrons       >~ 2.           0.5
DC3             electrons       >~11.           0.5
E0              electrons       0.015-  0.029   0.007*
E1              electrons       0.029-  0.042   0.026*
E2              electrons       0.042-  0.055   0.035*
E3              electrons       0.055-  0.093   0.034*
F0              electrons       0.093-  0.188   0.025*
F1              electrons       0.174-  0.304   0.017*
F2              electrons       0.304-  0.527   0.016*
F3              electrons       0.527-  0.884   0.012*
AS              singles        all counts     0.006
                               in detector
BS              singles        all counts     0.006
                               in detector
CS              singles        all counts     0.5
                               in detector
DS              singles        all counts     0.5
                               in detector
EB1             background     sidewise penetrators
EB2             background     E1E2 coincidences
FB1             background     Sidewise penetrators
FB2             background     F1F2 coincidences
 
 
*  Geometric factor determined from table in paper by Y. Wu, T.P.
   Armstrong [WU&ARMSTRONG1988].  Updated by EPD Team 05/19/98.
 
 
 
 
     The following table contains the channel energy ranges and
geometric factors for the detectors on the CMS telescope.
 
 
Channel         Species         Energy Range    Geometric Factor
Name                            (MeV nucl^-1)     (cm**2 sr)
------------------------------------------------------------------------
TOF x E
------------------------------------------------------------------------
TP1       protons             0.08-0.22             0.007
TP2       protons             0.22-0.54             0.007
TP3       protons             0.54-1.25             0.007
TA1       alphas              0.027-0.155           0.007
TA2       alphas              0.155-1.00            0.007
TO1       medium nuclei       0.012-0.026           0.007
TO2       medium nuclei       0.026-0.051           0.007
TO3       medium nuclei       0.051-0.112           0.007
TO4       medium nuclei       0.112-0.562           0.007
TS1       intermediate        0.016-0.030           0.007
TS2       intermediate        0.030-0.062           0.007
TS3       intermediate        0.062-0.31            0.007
TH1       heavy nuclei        0.02 -0.20            0.007
TACS      singles
STARTS         rates
KtS
 
 
------------------------------------------------------------------------
Delta E x E
------------------------------------------------------------------------
CA1       alphas              0.17- 0.49
CA3       alphas              0.49- 0.68
CA4       alphas              0.68- 1.4
CM1       medium nuclei       0.16- 0.55
CM3       medium nuclei       0.55- 1.1
CM4       medium nuclei       1.1 - 2.9
CM5       medium nuclei       2.9 -10.7
CN0       intermediate        1.0 - 2.2
CN1       intermediate        2.2 -11.7
CH1       heavy nuclei        0.22- 0.33
CH3       heavy nuclei        0.33- 0.67
CH4       heavy nuclei        0.67- 1.3
CH5       heavy nuclei        1.3 -15.0
JaS       singles rates
JbS       singles rates
KS        singles rates
 
 
Phase 2 Implications of LGA Mission for EPD:
-----------------------------------------------------------------------
     In its normal mode EPD uses 912 bps to transmit 64 rate channels,
with time resolution of 1/3, 2/3, or 4/3 seconds. The S/C spin period
is ~20 seconds and the EPD motor moves to a new polar angle every spin.
Ground processing converts this time based data stream into displays
with 7 polar angles and 64, 32, or 16 azimuthal sectors.  The LRS
record mode will still provide this resolution of coverage.
 
In the LGA mission EPD was allocated bit rates of 5, 10, 15, 20, 30, or
40 bps, depending on S/C TM format. The lowest bit rates will be the
most common.
 
At these low rates the EPD measurements must be sectored on board the
S/C, and accumulated for extended periods. The challenge was to design
a realizable combination of channels, time and angular resolution that
fits the available bit rate and maximizes science return.
 
 
EPD LGA Science Mission Design:
-----------------------------------------------------------------------
1. Introduction
 
The EPD collects particle flux measurements from almost the entire 4-pi
sphere by making and reporting fairly rapid particle measurements as the
spacecraft and the EPD motor platform sweep the EPD sensors through the
sky. The instrument simultaneously samples the particle flux in a number
of energy ranges, and sorts the particles out by mass, energy, and
direction.
 
It is important to preserve the directional information on the particle
measurements, as well as the mass and energy information. While the
temporal variations are also important to the science team, they are of
lower priority. In considering any new telemetry scheme, therefore, it
is necessary to preserve the mass, energy, and direction information.
 
Ideally, the EPD instrument could adapt to the reduced telemetry
allocations by doing on-board data averaging, editing, compression, etc.
Unfortunately, the version 1&2 software telemetry formats are
time-based, and do not easily support theses types of operations without
eliminating the directional information. It will therefore be necessary
to redesign the telemetry format such that it is spin-based; such an
approach allows data from adjacent spins to be averaged together, thus
reducing the bit rate required to send down the results.
 
It was determined that the EPD already contains sufficient hardware and
software resources necessary to handle the new tasks required of it,
however the rate channel RAM buffer storage requirements far exceed what
could be made available in the instrument. This single result drives
most of the interface requirements that will be presented below.
 
A number of cooperative EPD+CDS processing approaches have been looked
at with an eye to keeping as many tasks and storage buffers in the EPD
as possible. To generate a useful EPD data set, it will be necessary to
transfer raw rate channel data to the CDS, where it will be summed into
appropriate sector-based 4-byte counters. These counters will be
log-compressed, formatted, and passed on to the CDS telemetry processor
at the end of each instrument cycle.
 
 
2. Software Versions
 
The EPD instrument software has undergone a number of changes of the
course of the mission development cycle. The original instrument
software was finalized in about 1980, and was committed to ROM
fabricated by Sandia National Labs. This  software version, which I'll
refer to as the 'Version1' software, is still in the flight
instrument.
 
Prior to the original launch date of 1986, a few minor bugs were
discovered in the  software, and several small RAM patches were designed
to correct the problems. These  patches were tested in SAF during the
original integration checkout, but were never flown.
 
After the Challenger disaster, the EPD hardware underwent a number of
major modifications to support the addition of a new CMS TOF sensor.
Included in these modifications was the addition of a high voltage power
supply. New software was needed to operate the high voltage power
supply, reformat the telemetry output, and control enables, etc. The
software also included corrections to the minor bugs in the original
code. This software version, which I'll refer to as the 'Version2'
software, was to be the standard operating code for the 1989 mission. It
is important to note that if the REV2 software patch is not loaded, the
instrument reverts to the Rev1 (ROM- based) software. In this mode, the
instrument performs 99% of its intended functions, with the exception
that the high voltage supply (and thus the CMS TOF) can not be used.
This mode was used at Venus, Gaspra, and Ida.
 
The S-band mission will require us to greatly modify the way the EPD
collects and formats telemetry. New EPD software must be written to
enable the EPD to perform a number of new tasks. This software will work
closely with new software in the CDS which will collect and average the
EPD rate readouts. I will refer to the combined new real-time mode EPD
and CDS software as the 'Version3' version software.
 
There will be periods during the Galileo mission (such as satellite
encounters) when the CDS will collect data at the old, HGA-based rates.
After the data will be put on the tape recorded for later playback, the
system will revert back to the standard S-band collection scheme. A
requirement for the new Version3 software, therefore, is that it be
easily backward-compatible. By this I mean that it should be relatively
painless to quickly switch from the old HGA-based software to the new
Rev3 software.
 
When the instrument is put back into the record mode, we will want the
capability to operate the full instrument, i.e. the CMS TOF and high
voltage supply. It would therefore be desirable to have the ability to
switch from the Version3 software to the previous Version2 software. It
is not clear that we would want or be able to use all of the features
that were included in the Version2 software, however. We will therefore
modify the previous Version2 software for use with the LGA mission. This
version, which I'll refer to as the 'Version4' software, will handle
many of the same tasks as the Version2 software, but may not have all
the 'bells and whistles' in order to make the code more compact.
 
To summarize the material above:
 
EPD Software  Description
Version1      Original ROM-based code
Version2      Code generated for 1989 HGA mission
Version3      New real-time mode telemetry rate code for LGA-based
              mission
Version4      New record mode telemetry rate code for LGA-based mission
 
 
3. Science Background
 
The EPD instrument combines the output of two fairly independent sensor
subsystems, the LEMMS sensor and the CMS sensor. Two types of data are
produced by each of these sensors: rate channel data (channel counters)
and PHA (single event pulse height analysis) data. The science telemetry
is made up of rate channel and PHA data from both sensors.
 
The EPD science team has evaluated the scientific priorities from the
instrument in the context of a telemetry-starved SBAND environment. The
minimum spatial and temporal resolution requirements were determined for
each measurement; measurements with similar requirements were then
grouped together. A strawman telemetry format was then created by
trading off the projected telemetry and memory allocations for the EPD
vs. The science return from the measurements.
 
For the Version3 telemetry format, we decided to report all the CMS TOF
sensor rate channel measurements and selected PHA events. The LEMMS rate
channels measurements were also preserved. None of the CMS Delta-E x E
sensor measurements or LEMMS PHA spectral measurements were kept,
 however, except for LRS periods.
 
3.1 Spatial Resolution
 
The EPD motor was intended to quickly move the EPD sensor view angle
between 8 defined positions. These positions, called motor positions
(sometimes motor sectors) are numbered from 0 to 7, and are nominally 30
degrees apart. The calibrate position, 0 , is the exception, and is 45
 degrees away from position 1.
 
Unit sphere coverage for the EPD's sensors is provided by combining the
EPD motor stepping and the motion of the spacecraft spin. In the
original telemetry design, most rate channels were read and reported via
telemetry at least 15 times in each motor position (20 seconds). These
measurements were repeated in each of the 8 motor positions, yielding
120 spatial measurements per channel across the unit sphere.
 
Unfortunately, this type of spatial resolution will not be possible in
the Version3 software. To create the broader spatial sectors needed to
maintain some directional information on the particle fluxes while
conserving bit-rate, we divided the spacecraft spin into four 90-degree
sectors, and used the motor stepping pattern between positions 0 and 6
(7 will not be used). This reduces the original 120 sectors to only 28
sectors (4 spin sectors x 7 motor positions).
 
To reduce the bit-rate further, these 28 sectors will be summed together
using one of three algorithms. These algorithms will be used to produce
sector patterns which we'll call the 'high,' 'low,' and 'omni'
spatial resolution channel types. The unit sphere will now be divided
into either 17, 7, or 2 'super' sectors; each of these was the result
of summing one or more sectors together.
 
Each of the rate channels will be assigned to use one of these three
channel type formats; the more important the channel's data, the higher
the resolution it is given.
 
3.2 Motor Stepping
 
The EPD motor movement is directed primarily by the motor controller
board, and its associated processor hardware and software. The motor
controller is a slave to the data system board; its commands are
generated by and/or received from the data system, and its status is
sent to the data system.
 
As its name implies, the motor controller board handles all low level
motor control functions. It determines direction, stepping pattern,
position measurement, etc., and generates the actual motor phase pulses
that move the motor. Each time an electrical pulse is sent to the motor,
it will take a 'step' of 1.8 degrees. A series of pulses, sent over
about 1/2 second, is normally used to move the motor from one motor
position to the next.
 
The overall, high-level timing of the motor, however, is dictated by
the data system; it generates motor 'trigger' signals that tell the
motor controller when to initiate a motor movement. In the original
 design, the motor triggers are sent once every 20 seconds, but this
 timing can be altered via the 'motor dwell' command.
 
The motor trigger should be viewed as a timing synchronization signal,
not a command to move. When the motor controller receives the motor
trigger, its processor examines what stepping mode it is presently
executing. If the motor had been commanded to cease scan or stop at a
particular sector, the motor will do nothing in response to the motor
trigger; it will initiate a motor movement only if the commanded
stepping mode requires one.
 
In the new Version3 software, the data system will synchronize the motor
movement to the spacecraft spin by generating a motor trigger at the
 beginning of each spin of the spacecraft. The data system will use the
 CDS-supplied AACS spin vector information to determine when a new spin
has started. The motor controller interface will remain the same in that
it will simply respond to motor triggers using its original software.
 
The motor system operates in a 'windshield wiper' mode; it rotates 235
degrees in one direction, then reverses itself and goes back 235 degrees
in the opposite direction. Within this 235 degree rotational space,
there are 8 predefined, discrete motor positions, numbered 0 through 7.
In the Record Mode, the motor will visit all 8 positions, moving once
every 20 seconds from one position to the next (the actual motor
movement requires approximately 1/2 second).
 
In the Real-time Mode, the motor will only visit 7 of the 8 positions;
position number 7 is not used. The motor stepping will be synchronized
to the spacecraft spin rate, moving once per spin when the spacecraft
spin vector passes through 0. The motor movement synchronization is good
to 1/3 second resolution, resulting in approximately 6 degree
uncertainty. More information on the Real-time motor movements is
included in later sections of this document.
 
3.3 Temporal Resolution
 
As stated before, most EPD channels were previously read out once every
4/3 seconds. In the Version3 telemetry format, the channel read outs
will vary depending on what the EPD telemetry allocation is. The higher
the bit-rate, the higher the time resolution that will be used.
 
A new EPD data construct, called the EPD science record, will be used to
group the science measurements together. A science record will extend
over a number of spacecraft rotations; the sectorized rate channel data
in the record will be averaged across the multiple spins.
 
An EPD science record period will always be an integer multiple of EPD
cycles, where a motor cycle is defined as 6 EPD motor position steps.
Since the EPD motor will be synchronized to move once per spacecraft
spin, a motor cycle is 6 equal to spacecraft spin periods. Assuming a
nominal spin rate of 3.15 rpm, the nominal spin period is 19.048
seconds. Our minimum science record is one motor cycle (114.29 seconds)
and our maximum is 6 motor cycles (685.71 seconds or 11.4 minutes).
 
Worst-case time resolution chosen to be ~12 minutes (at 5 bps). This
should be reasonable--much of the Voyager analysis was done with 15
minute averages. Higher resolution will be available at the higher bit
rates. Angular resolution chosen to cover 4 Pie steradians with 1, 6, or
 16 measurements (and cal).
 
As described above, each rate channel is assigned to use one of the
three channel type formats. If these assignments were frozen, however,
it would not be possible to make good use of the variable bit-rate
allocated to the EPD. For this reason, two different mappings of rate
channel to channel type assignment will be used. These mappings will be
referred to as Channel Map 1 and Channel Map 2. The proposed channel
mappings are shown in Tables below. 3.4 Channel Bins
 
The combination of a rate channel and its channel map will create rate
channel 'bins.' The number of bins assigned to a rate channel can be
determined by looking at the number of readouts made in the unit sphere
for the channel; this is defined by which rate channel type the rate
channel is mapped to. To clarify, I'll give an example:
 
The LEMMS rate channel 'A4' is assigned to the a 'low' channel type
under Channel Map 1, and a 'high' channel type under Channel Map 2.
 Since a 'low' channel type incorporates 7 readouts across the unit
 sphere, there will be 7 bins assigned to A4 when the EPD bit rate
allocation dictates the use of Channel Map 1. Similarly, there will be
17 bins assigned to A4 when the EPD bit rate allocation dictates the use
of Channel Map 2.
 
By totaling up the number of bins assigned to each rate channel in the
two channel maps, we determine that under Channel Map 1, there will be
167 CMS bins and 189 LEMMS bins, for a total of 356 bins. Under Channel
Map 2, there will be a 202 CMS bins and 249 LEMMS bins, for a total of
451 bins.
 
It is important to remember that the counts that go into these bins are
generated by the instrument across many spacecraft spins, and the bins
are written to in a quasi random fashion, based on where the spacecraft
spin vector is pointing and what motor position the EPD is in. This
means that the data contained in these bins must be stored somewhere
throughout the science record, not just when a channel is being read.
 
The EPD rate channel accumulators each contain 24 bits counters, thus a
maximum count of 2^24=16,777,216 can be held in each accumulator before
it will role-over. If the bin is to be read once every science record,
(maximum time of 685.71 seconds long), a 24 bit bin can only handle an
average count rate of only about 24K counts/sec. Some of the LEMMS and
CMS rate channels should produce counts are rates above 200K per second.
For this reason, at least some of the bins must be 4 bytes long to
handle the expected range.
 
For this and more technical information, see EPD SBAND MISSION Software
requirements Revision D (S1i-2-949-D) By Stephen Jaskulek at APL.
 
Rate Channel Assignments for EPD LEMMS Sensor:
Channel Map 1
 
 
Energy Range        Channel   16 sec.   6 sec.           Omni      Total
                               +Cal      +Cal            +Cal
                               Channels
 
LEMMS (MeV)
 
 
0.022 - 0.042 KEV     A0                  1                          7
0.042 - 0.065         A1        1                                   17
0.065 - 0.120         A2        1                                   17
0.120 - 0.280         A3                  1                          7
0.280 - 0.515         A4                  1                          7
0.515 - 0.825         A5                  1                          7
0.825 - 1.68          A6                  1                          7
1.68 - 3.20           A7                  1                          7
3.50 - 12.4 (z>= 2)   A8                  1                          7
 
 
0.015 - 0.029         E0                  1                          7
0.029 - 0.042         E1        1                                   17
0.042 - 0.055         E2                  1                          7
0.055 - 0.093         E3                  1                          7
 
 
0.093 - 0.188         F0                  1                          7
0.174 - 0.304         F1                  1                          7
0.304 - 0.527         F2        1                                   17
0.527 - 0.884         F3                  1                          7
 
 
3.20 - 10.1 (z=1)     B0                                   1         2
1.5 - 10.5 (e-)       B1                                   1         2
16.0 - 100. (z=2)     B2                                   1         2
 
 
14.5 - 33.5 (z>=1)    DC0                                  1         2
51 - 59 (z>=1)        DC1                                  1         2
>= 2.0 (e-)           DC2                                  1         2
>=11 (e-)             DC3                                  1         2
 
 
A Singles             AS                                   1         2
B Singles             BS                                   1         2
C Singles             CS                                   1         2
D Singles             DS                                   1         2
Background            EB1                                  1         2
Background            EB2                                  1         2
Background            FB1                                  1         2
Background            FB2                                  1         2
 
 
LEMMS Total                     4         13               15        189
 
 
Rate Channel Assignments for EPD CMS Sensor
Channel Map 1
 
 
Energy Range        Channel   16 sec.   6 sec.         Omni      Total
                              +Cal      +Cal           +Cal
                              Channels
 
TOF x E (MeV)
0.08 - 0.22 (H)       TP1       1                                  17
0.22 - 0.54 (H)       TP2       1                                  17
0.54 - 1.25 (H)       TP3                 1                         7
0.027 - 0.155 (He)    TA1                 1                         7
0.155 - 1.0 (He)      TA2                 1                         7
0.012 - 0.026 (CNO)   TO1       1                                  17
0.026 - 0.051 (CNO)   TO2       1                                  17
0.051 - 0.112 (CNO)   TO3                 1                         7
0.112 - 0.562 (CNO)   TO4                 1                         7
0.016 - 0.030 (S)     TS1       1                                  17
0.030 - 0.062 (S)     TS2                 1                         7
0.062 - 0.31 (S)      TS3                                 1         2
0.02 - 0.20 (Fe)      TH1                 1                         7
TAC Singles           TACS                1                         7
KT Singles            KTS                 1                         7
Start Singles         STARTS    1                                  17
 
 
CMS Total                       6         9               1       167
 
 
Total Channels                 10        22              16       356
 
 
 
 
 
 
Rate Channel Assignments for EPD LEMMS Sensor
Channel Map 2
 
 
Energy Range        Channel   16 sec.   6 sec.         Omni      Total
                              +Cal      +Cal           +Cal
                              Channels
 
LEMMS (MeV)
 
 
0.022 - 0.042 KEV     A0                  1                         7
0.042 - 0.065         A1        1                                  17
0.065 - 0.120         A2        1                                  17
0.120 - 0.280         A3        1                                  17
0.280 - 0.515         A4        1                                  17
0.515 - 0.825         A5        1                                  17
0.825 - 1.68          A6                  1                         7
1.68 - 3.20           A7                  1                         7
3.50 - 12.4 (z>= 2)   A8                  1                         7
 
 
0.015 - 0.029         E0                  1                         7
0.029 - 0.042         E1        1                                  17
0.042 - 0.055         E2                  1                         7
0.055 - 0.093         E3                  1                         7
 
 
0.093 - 0.188         F0                  1                         7
0.174 - 0.304         F1                  1                         7
0.304 - 0.527         F2        1                                  17
0.527 - 0.884         F3                  1                         7
 
 
3.20 - 10.1 (z=1)     B0                  1                         7
1.5 - 10.5 (e-)       B1                  1                         7
16.0 - 100. (z=2)     B2                  1                         7
 
 
14.5 - 33.5 (z>=1)    DC0                                 1         2
51 - 59 (z>=1)        DC1                                 1         2
>= 2.0 (e-)           DC2                                 1         2
>=11 (e-)             DC3                                 1         2
 
 
A Singles             AS                                  1         2
B Singles             BS                  1                         7
C Singles             CS                                  1         2
D Singles             DS                                  1         2
Background            EB1                 1                         7
Background            EB2                                 1         2
Background            FB1                 1                         7
Background            FB2                                 1         2
 
 
LEMMS Total                      7       16               9       249
 
 
Rate Channel Assignments for EPD CMS Sensor
Channel Map 2
 
 
Energy Range        Channel   16 sec.   6 sec.         Omni      Total
                              +Cal      +Cal           +Cal
                              Channels
 
TOF x E (MeV)
0.08 - 0.22 (H)       TP1       1                                 17
0.22 - 0.54 (H)       TP2       1                                 17
0.54 - 1.25 (H)       TP3                 1                        7
0.027 - 0.155 (He)    TA1       1                                 17
0.155 - 1.0 (He)      TA2                 1                        7
0.012 - 0.026 (CNO)   TO1       1                                 17
0.026 - 0.051 (CNO)   TO2       1                                 17
0.051 - 0.112 (CNO)   TO3       1                                 17
0.112 - 0.562 (CNO)   TO4                 1                        7
0.016 - 0.030 (S)     TS1       1                                 17
0.030 - 0.062 (S)     TS2       1                                 17
0.062 - 0.31 (S)      TS3                 1                        7
0.02 - 0.20 (Fe)      TH1                 1                        7
TAC Singles           TACS                1                        7
KT Singles            KTS                 1                        7
Start Singles         STARTS    1                                 17
 
 
CMS Total                       9         7                      202
 
 
Total Channels                 16        23              9       451

        