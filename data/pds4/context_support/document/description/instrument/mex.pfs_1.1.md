
1.Introduction
==============
 
PFS is a double pendulum interferometer working in two wavelength
ranges (1.2- 5um and 5-45um, Table 1). Martian radiation is divided
into two beams by a dichroic mirror. The two ranges correspond to two
planes (one on top of the other) containing the two interferometers,
so that the same motor can simultaneously move the two pendulums and
the two channels are sampled simultaneously and independently. The
pendulum motion is accurately controlled via a laser diode reference
channel using the same optics as the martian radiation. The same
laser diode also generates the sampling signal for the analogue-
digital converter (ADC), measuring the 600 nm displacements of the
double pendulum mirror. The measurements are double-sided
interferograms, so that the onboard FFT can be computed without
needing the zero optical path difference location.
 
TABLE 1 - DETAILED PFS SCIENTIFICS PARAMETERS
-----------------------------------------------
 
PARAMETERS                    SW               LW            UNITS
 
SPECTRAL RANGE                1.2 - 5.0        5.5 - 45      [m]
SPECTRAL RANGE                2000 - 8200      230 - 1750    [cm-1]
SPECTRAL RESOLUTION           1.5              1.5           [cm-1]
(by triangular apodization)
FOV  FWHM                     1.6              2.7           (deg)
NEB                           5 10-9           4 10-8 (1)    [W cm- 2
                                                               sr -1]
 
MEASUREMENT CYCLE DURATION    10.0             10.0          [s]
DETECTOR TYPE                 Photoconductor   Pyroelectric   -
MATERIAL                      PbSe             LiTaO3         -
SHAPE/SIZE                    Square/0.7x0.7   Round/r=1.4   [mm]
NEP                           1*10^-12 (2)     4*10^-10(3)   [W/Hz.5]
SENSITIVITY                   90 (2)           30 (3)        [KV/W]
TEMPERATURE                   220 (4)          290           [K]
INTERFEROMETER TYPE                  Double Pendulum          -
REFLECTING ELEMENTS              Cubic corner reflectors      -
BEAMSPLITTER                  CaF2             CsI            -
REFL. ELEMENTS MOTION         +/- 1.5          +/- 1.5 (5)   [mm]
MAX OPTIC PATH DIFFER.        5                5             [mm]
TIME FOR MOTIONS              5                5             [s]
TIME FOR MEASUREMENTS         4.5              4.5           [s]
REFERENCE SOURCE              Laser diode      Laser diode    -
REF. SOURCE WAVELENGTH        1216             1216          [nm]
COLLECTOR OPTICS                     Parabolic mirror         -
DIAMETER                      49               38            [mm]
FOCAL LENGTH                  20               20            [mm]
COATING                       Gold             Gold           -
SW/LW SEPARATION                 KRS-5 with a multilayer
                              coating reflecting SW radiation -
OPTICS TRANSMISSION           0.64             0.78 (6)       -
MODULATION FACTOR             0.87             0.98 (7)       -
INTERFEROGRAM                 TWO-SIDED        TWO-SIDED      -
SAMPLINGS NUMBER              16384            4096(16384)    -
SAMPLING STEP                 608              2432          [nm]
DYNAMICAL RANGE               +/- 215          +/- 215        -
 
SPECTRA (from on-board FFT)                                   -
QUANTITY OF POINT             8192             2048           -
DYNAMICAL RANGE               6000             6000           -
 
ELECTRONICS
MODULATION FREQUENCY RANGE    423-1600         50-400        [Hz]
ONB FFT COMPUTATION TIME      3.35             0.83          [s]
BUFFER MEMORY VOLUME                     32                  [MBits]
 
Note
---------------------------------------------------------------------
(1) Values are given for wavelengths 2.5 and 15 m. Results of
    measurements for PFS 07 in SW.
(2) In peak of the spectral responsivity curve (near 4.8 m
    and for the modulation frequency 1000 Hz.
(3) By the modulation frequency 200 Hz.  NEB and sensitivity are
    given for the output of the preamplifier.
(4) Radiative cooling.
(5) Linearized deviation from the position, corresponding to zero
    path difference.
(6) From measurements of reflection and transmission of optical
    elements. Values are given
    for wavelengths 2.5 and 15  m
(7) From estimates of tolerances.  Values are given for wavelengths
    2.5 and 15 microns.
 
 
1.1.Instrument organization
===========================
 
PFS is a Fourier spectrometer produced by the combined efforts of
several groups from Italy, Russia, Poland, Germany, France and Spain.
The flight hardware was built in Italy (the Interferometer Block with
its controlling electronics, the digital electronics controlling the
experiment, and the Ground Support Equipment with the spacecraft
simulator) and Poland (power supply and pointing system). Special
flight parts and subassemblies were built in Russia and Germany.
 
1.2.Technical description
=========================
 
The flight hardware, totaling 31.2 kg, is divided into four modules,
with connecting cables (0.8 kg):
-Module-O (PFS-O): the interferometer, with its optics and proximity
 electronics, is the core of PFS. 21.5 kg;
-Module-S (PFS-S): the pointing device, which allows PFS to receive
 radiation from Mars or from the inflight calibration sources, 3.7 kg
-Module-E (PFS-E): the digital electronics, including a 32-Mbit mass
 memory and a realtime FFT. 3.0 kg;
-Module-P(PFS-P): the power supply, with the DC/DC converter,
 redundancies and the separate power supplies for the 16-bit
 ADCs. 2.2 kg.
 
Power requirements are:
- 5 Watt thermal control
-10 Watt in sleep mode
-35 Watt full operational mode
-44 Wpeak.
 
1.3.Module-O (PFS-O)
====================
 
The incident IR beam falls onto the entrance filter that separates
the radiation of the SW channel from that of the LW channel and
directs each into the appropriate interferometer channel. The PFS-S
in front of the interferometer allows the FOV to be pointed along and
across the projection of the flight path onto the martian surface.
It also directs the FOV at the internal blackbody sources diffusers
and to open space for inflight calibration. Each PFS channel is
equipped with a pair of retroreflectors attached by brackets to an
axle rotated by a torque motor. The axle and drive mechanism are used
for both channels, which are vertically separated. The optical path
difference is generated by the rotation of the retroreflectors. The
motor controller uses the outputs of two reference channels, which
are equipped with laser diodes. This interferometer design is very
robust against misalignment in a harsh environment, in comparison
with the classical Michelson-type interferometer. The detectors are
in the centre of the parabolic mirrors. The optical path is changed
by rotating the shaft of the double pendulum along its axis. In this
way, the optical path is four times that provided by a single
cube-corner displacement because two mirrors move at the same time.
The dichroic mirror acts as a fork that divides the two spectral
ranges. Indeed, it reflects all the wavelengths below 5um and remains
more or less transparent for longer wavelengths. The band stop for
wavelengths below 1.2um is provided by the silicon window, with its
cutoff at 1.24um and placed in the optical inlet of the SW channel.
This filter is tilted by 1.5 deg. so that the radiation returning to
the source is not partially reflected on the detector. The double-
pendulum axis is rotated by a brushless, frictionless motor (two for
redundancy). The shaft of the double pendulum is held only by two
preloaded ball bearings so additional mechanical friction is required
for stabilizing the pendulum speed. Double-sided interferograms are
acquired by placing the zero optical path difference in the centre of
the mirror displacement. A double-sided interferogram has several
advantages, including a relative insensitivity to phase errors.
Bilateral operation is adopted in order to reduce the time-cycle of
each measurement, but separate calibration for each direction is
recommended in order to maintain the radiometric accuracy. The
spectral reference beam is a diode laser (InGaAsPat 1.2um); its
detector is an IR photodiode with maximum response at about 1.2um.
The beam of the reference channel is processed like the input signal
so that its optical path coincides with that of the signal being
studied. Each channel has its own reference beam and the different
lengths of the double-pendulum arms are fully compensated for.
Because the LW beam splitter is not transparent at the wavelength
of the corresponding reference diode laser, a special small window
was added in order to keep the attenuation of the laser beams
negligible through the beam splitter itself. The unused output beams
of the two reference channels terminate into optical traps.
 
1.3.1.Optical scheme of PFS-O
=============================
 
The incident IR beam falls onto the entrance filter that separates
the radiation of the SW channel  from that of the LW channel and
directs each into the appropriate interferometer channel. The PFS-S
in front of the interferometer allows the FOV to be pointed along and
across the projection of the flight path onto the martian surface.
It also directs the FOV at the internal blackbody sources diffusers
and to open space for inflight calibration. Each PFS channel is
equipped with a pair of retroreflectors attached by brackets to an
axle rotated by a torque motor. The axle and drive mechanism are used
for both channels, which are vertically separated. The optical path
difference is generated by the rotation of the retroreflectors. The
motor controller uses the outputs of two reference channels, which
are equipped with laser diodes. This interferometer design is very
robust against misalignment in a harsh environment, in comparison
with the classical Michelson-type interferometer. The detectors are
in the centre of the parabolic mirrors. The optical path is changed
by rotating the shaft of the double pendulum along its axis. In this
way, the optical path is four times that provided by a single cube-
corner displacement because two mirrors move at the same time. The
dichroic mirror acts as a fork that divides the two spectral ranges.
Indeed, it reflects all the wavelengths below 5um and remains more or
less transparent for longer wavelengths. The band stop for
wavelengths below 1.2um is provided by the silicon window, with its
cutoff at 1.24um and placed in the optical inlet of the SW channel.
This filter is tilted by 1.5 deg so that the radiation returning to
the source is not partially reflected on the detector. The double-
pendulum axis is rotated by a brushless, frictionless motor (two for
redundancy). The shaft of the double pendulum is held only by two
preloaded ball bearings so additional mechanical friction is required
for stabilizing the pendulum speed. Double-sided interferograms are
acquired by placing the zero optical path difference in the centre of
the mirror displacement. A double-sided interferogram has several
advantages, including a relative insensitivity to phase errors.
Bilateral operation is adopted in order to reduce the time-cycle of
each measurement, but separate calibration for each direction is
recommended in order to maintain the radiometric accuracy. The
spectral reference beam is a diode laser (InGaAsPat 1.2um); its
detector is an IR photodiode with maximum response at about 1.2um.
The beam of the reference channel is processed like the input signal
so that its optical path coincides with that of the signal being
studied. Each channel has its own reference beam and the different
lengths of the double-pendulum arms are fully compensated for.
Because the LW beam splitter is not transparent at the wavelength of
the corresponding reference diode laser, a special small window was
added in order to keep the attenuation of the laser beams negligible
through the beam splitter itself. The unused output beams of the two
reference channels terminate into optical traps.
 
 
1.3.2.Electronics of PFS-O
==========================
 
Most of the electronics inside PFS-O are analogue but the
microprocessor-based On- Board Data Management (OBDM) board controls
all the complex procedures during acquisition of the interferogram,
including communication with PFS-E. It includes 32 kb word of EPROM
for software storage and 96 kb word for data. The most important
electronics block is the speed controller. The zero crossing of an
interferogram of a monochromatic source that is very stable in
wavelength can be used for sampling the interferogram of the source
under study. Ideally, the interferogram of the monochromatic source
should be a pure sine wave but it is not simply because its
interferogram is limited in time. The shorter the wavelength of the
reference source means better sampling accuracy. For PFS, 1.2um is
the reference source because of the limited variety of diode lasers
and it simplifies the optical design. The wavelength of a diode laser
depends on its temperature and power, so great care has to be taken
in their control. The speed of the double pendulum is such that a
frequency of 2  kHz is generated for the SW channel, so a train of 4
kHz pulses is produced from the electronics of the SW reference
channel. Thermal control is also very important for an IR
interferometer; heaters and thermometers are positioned at eight
locations. A locking system blocks the double pendulum during
launch and maneuvering for orbital insertion and correction. The
procedure of locking and unlocking takes a minimum of 3 minutes but
using a paraffin actuator means it can be repeated hundreds of times.
The launch acceleration vector will be along the axis of the double
pendulum for maximum robustness. The photoconductor SW channel
detector can work at temperatures down to 200K. It is passively
cooled through a radiator and its holder is partially insulated from
the rest of the IB. For the LW channel, the pyroelectric detector can
operate without performance degradation even at ambient temperatures.
 
1.4.Module-E (PFS-E)
====================
 
PFS-E controls all the PFS modules: the communications to and from
the spacecraft, memorizing and executing the command words, and
operating PFS and sending back the data words to the spacecraft.
Moreover, it synchronizes all the procedures according to the time
schedule and to the clock time from the spacecraft.
 
1.5.Module-P (PFS-P)
====================
 
PFS combines many kinds of electrical energy consumers: standard
digital and analogue electronics, sensitive preamplifiers and ADCs,
light sources and electromechanical devices (motors and relays).
All of them have different supply requirements and some need to be
electrically isolated (to ensure extremely high stability) and/or
individually controlled by Module E's processor. This is why PFS-P
is more complicated than a simple DC/DC converter: there are three
independent converters, six different power outputs (totaling 13
independent voltages), one common input interface to satellite and
one interface to DAM. All converters have cold redundancy. Switching
between main/reserve +5 Volt is controlled by the spacecraft, while
the other main/reserve converters are controlled by PFS itself.
 
1.6.Module-S (PFS-S)
====================
 
The previous version of the pointing system, for the Mars-96 mission,
had two degrees-of-freedom in pointing (two rotation axes), but was
rather heavy (8.5 kg for the system and 2.3 kg for the controlling
electronics). The pointing system is certainly necessary for
generating a complete set of measurements, since we need to measure
not only the martian radiation but also the calibration blackbody and
empty space. Mars Express provides nadir pointing so PFS itself needs
only one degree of rotation, simplifying the PFS-S design and
reducing mass considerably (to 3.7 kg).
 
1.7.Modes of operation, data-acquisition cycle
==============================================
 
PFS-S and PFS-O work in parallel during an observation session, while
PFS-E coordinates operations of the other modules by sending commands
and receiving messages. During measurements, PFS-S must be motionless
while PFS-O acquires data. This is the only synchronization point in
the data-acquisition cycle. Upon completion of acquisition, all the
modules work asynchronously while PFS-E coordinates their operations:
-starts rotation of PFS-S;
-receives LW and SW interferograms from PFS-O;
-if spectra are required, PFS uploads previously acquired LW and SW
 interferograms into the Fast Fourier Transform processor and
 downloads computed spectra;
-prepares the telemetry data pack i.e. splits information into frames
 and stores them in the mass memory;
-upon completion of the PFS-S rotation gives a command to PFS-O to
 start new acquisition.
 
After each data-acquisition cycle, PFS checks whether new
telecommands have been received and, if any, executes them. Telemetry
can be sent at any time on request from the spacecraft.
 
1.8.Inflight calibration
========================
 
During observation sessions, PFS periodically performs calibrations
by sending commands to PFS-S to point sequentially at the calibration
sources: deep space, internal blackbody and calibration lamp. The
housekeeping information obtained from PFS-O after each calibration
measurement contains, in particular, the temperatures of the sensors
and the blackbody. These data are used for the computation of the
absolute spectra for the LW channel.
 
 
2.Data-taking Along the Orbit
=============================
 
2.1.Data-transmission modes
===========================
 
The data-transmission mode (DTM) defines the kind of scientific data
that PFS must select and store in the mass memory to be sent to
Earth. PFS has 15 DTMs, numbered for historical reasons, 0, 2, 4, 5,
6, 7, 8, 17, 18, 27, 28, 9, 10, 15, 16. DTM0 is for PFS operating in
the autonomous test mode; the others are obtained in the science
mode, where PFS acquires both LW and SW interferograms. If spectra
are required (DTM 9, 10, 15, 16), PFS makes Fast Fourier Transforms
of the interferograms. Then, depending on the DTM, PFS selects the
required data. Interferograms can be selected completely or
partially. Of the 15 DTMs, 10 provide interferograms and four
spectra:
 
-MODE 0: autotest of the interferometer (4096 points in the LW
         channel and 16384 points in the SW channel provide the sine
         wave shape and the monitoring of the speed during the double
         pendulum motion);
-MODE 2: full LW interferograms;
-MODE 4: half-resolution interferograms, SW and LW;
-MODE 5: half-resolution LW interferograms;
-MODE 6: half-resolution SW interferograms;
-MODE 7: full LW interferogram + one-sided SW interferogram (
         including the zero optical path difference and right
         side);
-MODE 8: one-sided LW and SW interferograms (right side);
-MODE 17: full LW and SW interferograms;
-MODE 18: full SW interferograms;
-MODE 27: full LW interferogram + one-sided SW interferogram
          (including the zero optical path difference and left side);
-MODE 28: one-sided LW and SW interferograms (left side);
-MODE 9: modules of LW and SW spectra;
-MODE 10: modules of LW spectra;
-MODE 15: full modules of LW spectra and SW spectra with reduced
          range(2000 points in the SW channel between 2000 and 4000
           cm-1);
-MODE 16: modules of SW spectra (6144 points).
 
2.2.Data-taking along the orbit
===============================
 
PFS will perform measurement when the spacecraft is below 4000km. PFS
will wake up from its sleep mode about 1h before and follow the
scheme:
-apocentre: PFS is in sleep mode, telecommands can be received;
-pericentre minus 60min: wake-up, wait for warm-up, start autonomous
 test, calibration LW, calibration SW, calibration deep space. PFS-S
 in nadir direction. Give data to the spacecraft;
-pericentre minus 40min: start martian observations. Give data to the
 spacecraft;
-pericentre plus 48min: stop martian observations. Give data to the
 spacecraft;
-pericentre plus 53min: calibration LW, calibration SW, calibration
 deep space, autonomous test. Give data to the spacecraft. Go into
 sleep mode;
-up to apocentre in sleep mode.
 
In total, 600 measurements per orbit are taken, of which 60 are
calibrations. This corresponds to 1200 measurements per day (the
third orbit per day being for downlink) and 823440 spectra in a
martian year. The footprint from 4000km is of the order of 109km for
the SW channel and 188km for the LW channel; at pericentre (250km)
they become respectively 6.8km and 11.8km (perpendicular to the
ground track, but 20km along it).

        