
########################################################################
########################################################################
REQUIRED UNDERSTANDING:  THE REX AND THE NEW HORIZONS (NH) REGENERATIVE
RANGING TRACKER [DEBOLTETAL2005] ARE

   *****SEPARATE***** AND *****INDEPENDENT*****

SUBSYSTEMS THAT BOTH USE THE RADIO FREQUENCY (RF) AND TELECOMMUNICATIONS
SUBSYSTEMS.  TRACKING DATA WILL NOT BE ARCHIVED IN REX DATA SETS.
########################################################################
########################################################################

########################################################################
########################################################################
REQUIRED READING:
- Tyler et al. (2008) [TYLERETAL2008]
########################################################################
########################################################################

      The REX & DSN descriptions were adapted from [DEBOLTETAL2005],
      from [DEBOYETAL2004], from [TYLERETAL2008], from PDS dataset
      CO-SS-RSS-1-SCC2-V1.0 at the PDS Atmospheres sub-node, and from
      the New Horizons website.


INSTRUMENT OVERVIEW
===================

REX requires the coordinated use of Earth-based transmitters and the New
Horizons receiver.  The Earth-based 'Ground Element' is made up of the Deep
Space Network (DSN) hardware and operations facilities that support the New
Horizons (NH) mission.  The 'Flight Element' includes the 2.1 m spacecraft
high-gain antenna (HGA) and the NH radio receiver that has a REX-specific
signal processing board, which sends its output to spacecraft data storage.


Scientific Objectives - REX
========

The primary purpose of the REX system was to investigate open questions
regarding atmospheric and ionospheric structure, surface conditions, and
planetary radii of both Pluto and Charon.

The REX encounter with the Pluto system was focused on occultations, by Pluto
and Charon, of an Earth-based, uplink radio signal.  The New Horizons HGA
remained pointed toward Earth for the duration of the occultation events,
beginning and ending with the line-of-sight to Earth well above any
anticipated sensible atmosphere or ionosphere.  This arrangement
set up three investigations at each occultation, plus a fourth gravity
investigation:

Investigation 1:  Atmosphere characterization or detection
--------

As the Earth-spacecraft line-of-sight passed through the atmosphere of Pluto,
there was a detectable shift in phase of the 7.2 GHz uplink signal as
measured via the heterodyne-, downconversion- and sampling-circuitry that
composes REX.  These occultation phase shifts provide opportunities for
characterization of Pluto's atmosphere and of a possibly sensible ionosphere;
a similar encounter allows a search for a sensible atmosphere and ionosphere
of Charon.


Investigation 2:  Diameter measurement
--------

As the path of the signal approached the limb, there were predicable,
detectable changes in signal strength due to diffraction, allowing precise
measurement of entry and exit events.  The time difference between the entry
and exit events, plus knowledge of Pluto-Charon, Earth, and spacecraft
ephemerides, provide the length of the occultation chords.


Investigation 3:  Front and dark side thermal emission
--------

Just before closest approach, the HGA boresight was swept across Pluto's
surface.  In one observation (DISKTHERM), the measurement was of sunlit
surface thermal emission.  In the others (THERMSCAN), 34m DSN antennas
radiated Right- and Left-Circular Polar 7.2GHz signals timed to arrive
at Pluto during the observation.  The HGA measured the reflected signal,
making this a Bi-Static Radar (BSR) measurement; one scan was directed
at the specular reflection point; the other BSR measurement was aimed off
of the Earth-Pluto-Spacecraft radio metric equator.

During each occultation (when the uplink signal from Earth was blocked),
REX made measurements of radiothermal emissions at 4.2 cm (7.2 GHz).
The motion of the spacecraft caused the antenna beam to sweep across the
night side of Pluto and Charon while the pointing of the HGA remained fixed
in the Earth direction.


Investigation 4:  Individual body masses
--------

Away from the limbs and above any atmosphere, perturbations in the measured
uplink signal, caused by the gravitational attractions of Pluto and Charon
on the spacecraft, may be used to infer their individual masses.  However,
the reader should note that the proposed gravity investigation is beyond the
chosen scope of this data set, and no ranging data will be included here.

Those four investigation descriptions are greatly simplified; see
[TYLERETAL2008] for more detail.


INSTRUMENT OVERVIEW - FLIGHT ELEMENT
====================================

On-board the NH spacecraft, hardware specific to REX are an analog-to-digital
converter and the REX Actel Field-Programmable Gate Array (FPGA).  These are
on the Radiometrics card within the Integrated Electronics Module (IEM) that
is the NH transceiver [DEBOYETAL2004].  N.B. there are two redundanct IEMs.
Note also that the word 'transceiver' is often used when describing REX
operations, here and elsewhere, because the REX hardware receives its input
signal via the transceiver hardware; such usage does not imply REX has any
transmission capability; REX is uplink-only.

Other spacecraft hardware external to the REX hardware, but used by REX,
include a digital receiver on the uplink card of the NH transceiver IEM, the
2.1 meter high gain antenna (HGA) and an ultrasable oscillator providing the
precision frequency reference necessary for the uplink radio science
experiment.  N.B. there are two redundant USOs.  Refer to [TYLERETAL2008],
[FOUNTAINETAL2008] and [DEBOYETAL2004] for further details.

Signals captured by the HGA are downconverted and passed through a 4.5 MHz
filter before entering the REX signal conditioning unit.  Outputs from this
unit are: (1) in-phase (I) and quadrature (Q) 16-bit integer samples at
1250 sample pairs (complex) per 1.024 seconds -- i.e., approximately 1220.7
I samples per second and 1220.7 Q samples per second; and (2) the
radiometer output, consisting of 40-bit accumulating samples at a rate of
10 samples every 1.024 seconds.

REX is part of the redundant spacecraft telecommunication subsystems and
signal paths that use the single HGA in common. The two REX cards are
designated as Sides A and B (also Channels A and B).  REX Side A always
received RCP (Right Circular Polarization) uplink signal from the DSN;
Side B always received LCP (Left Circular Polarization) uplink signal
from the DSN.  This is unaffected by the switching described in the next
paragraph.  See [REX Use of the DSN] topic below for a description of
uplink signal polarity sent during REX observations.

Sides A and B can be operated simultaneously, to increase SNR, using
uplink signals with RCP and LCP, respectively.  Normally Side A
communicates with spacecraft CDH1 (Command and Data Handling), and B with
CDH2, but that can be switched if required by spacecraft events; as of the
end of 2015, this switch has never occurred.  There are two USOs, and each
REX side is referenced to a separate USO, and that must be considered when
using the data. The USOs are also cross-strapped so either can provide
timing to both sides in the event of a single USO failure. Execution of
the command to do so would be a one-time, irreversible event, and as of
the end of 2015 that has not occurred.


SPECIFICATIONS
--------------

NAME:                    REX (Radio Science Experiment)
DESCRIPTION:             Local oscillator vs. uplink signal phase comparator
PRINCIPAL INVESTIGATOR:  Ivan Linscott, Stanford University
WAVELENGTH RANGE:        4.2 cm
FIELD OF VIEW:           20 mRad
ANGULAR RESOLUTION:      20 mRad
FREQUENCY RESOLUTION:    3E-13 (delta-f/f)
POWER CONSUMPTION:       1.6 W      (per-side; see Note 1)
MASS:                    160 g      (per-side; see Note 1)
VOLUME:                  520 cm**3  (per-side; see Note 1)

Note 1:  Resource usage values include those for the following components:
         Analog-to-Digital Converter (ADC), Field-Programmable Gate Array
         (FPGA), and Integrated Ciruit (IC) buffers.


Instrument Calibration - REX
========

HGA Beam Pattern Calibration
--------

The REX commissioning test on July 20, 2006 was dedicated to mapping the beam
pattern of the NH spacecraft high gain antenna. The REX science team obtained
the beam pattern by tuning the frequency of an unmodulated uplink signal of
constant power from the DSN to arrive at the NH spacecraft with a constant
frequency; the signal served as a calibration source. At the same time, the
team varied the spacecraft attitude with respect to the direction to Earth,
thus implementing a scan of the HGA beam over a small range of angles about
the Earth direction, centered approximately on the beam maximum. The initial
offset of the scan was set at the upper left corner of a 2deg x 2deg angular
box.  The beam direction then was made to 'nod and step' parallel to the box
edges so as to perform a raster scan about the Earth direction. During the
scan, REX processed the uplink signal from the tranceiver, with the REX
output recorded and time-tagged on-board. At the same time the spacecraft body
vectors were logged and time-tagged. The combination of these two time
sequences allowed the team to map estimates of the uplink signal power to the
spacecraft pointing direction.


Sample Calibration
--------

Raw 16-bit I and Q samples are scaled to Volts based on the assumed-stable
reference voltage of the 12-bit ADC, plus the design of the digital filter
implemented within the FPGA.  The net result is a gain-independent, direct
scaling factor, which value is in the Science Operation Center/Instrument
Inteface Control Document - SOC_INST_ICD - provided with this data set.

N.B. the IQ data calibration is present only to satisfy a PDS requirement;
     it is more or less meaningless as it provides no additional information
     not already in the raw data, because the purpose of the IQ data is
     the signal phase relationship encoded in the Q:I ratio of each IQ pair.
     The calibrated IQ data provide no additional insight into that ratio
     not already present in the raw data.  The noise inherent in any single
     measurement swamps any error in the calibration (e.g. fluctuation in
     the ADC reference voltage).  Statistically, the radiometry values, by
     both intent and design, will be more useful in evaluating signal
     strength in scientific units.

The 40-bit radiometer samples are scaled to temperature values in Kelvin,
using a reference temperature calibrated from the noise figure of the New
Horizons radio receiver and a gain setting (AGC or AGCGAIN).

Note that the acronym AGC comes from the nomenclature of the RF Uplink
hardware, which is separate from REX, and which uses Automatic Gain Control as
part of its carrier tracking loop.  For REX there is no automatic gain control
and REX gain is manually set by commands from the ground based on the expected
uplink power, or radiometry, in the REX band.


Radiometer Calibration
--------

Summary:  the System Noise Temperature of the REX instrument is 146K.

System Noise Temperature (SNT) is typically measured by injecting known
amounts of noise power into the signal path and comparing the total power
with the noise injection 'on' against the total power with the noise
injection 'off.'  That operation is based on the fact that receiver noise
power is directly proportional to temperature.  Normally, measuring the
relative increase in noise power due to the presence of an absolutely
calibrated thermal noise source allows direct calculation of SNT.

However, for the NH radio subsystem, without an absolutely calibrated
thermal noise source, it is possible to calculate the SNT using multiple
standard radio sources and Cold Sky:  'on' is when the HGA is pointing at a
standard radio source; 'off' is when the HGA is pointing at Cold Sky.

There are three Cold Sky locations chosen for NH REX,
where the the sky temperature is within a few tenth's of a Kelvin of the
Cosmic Microwave Background - CMB - over a section of the sky larger than
several times the half-power beam width of the HGA.

Using the ratios of radiometry measurements of multiple standard radio
sources to radiometry measurements of Cold Sky allows indirect calculation
of the SNT, as long as the relative power ratios between the standard radio
sources are known and are not unity, and with the following assumptions:

1) we assume that the REX radiometry system response is linear with power.

2) we assume that the maximum signal when the HGA scans across a standard
   radio source is proportional to the X-band radio flux from that source.
   The peak in the HGA beam pattern is a significant fraction of a degree,
   which is much broader than the pointing deadband of 0.1deg used for
   these observations, so this assumption is reasonable.

3) we assume that the Standard radio sources chosen for this calibration
   are 'thermal', i.e. they possess blackbody radiation spectra that are
   constant, or at least interpolable, across the REX band.

Refer to DOCUMENT/NH_REX_RADIOMETER_CALIB_V4P7.LBL for more detail.

On 29 June, 2006, the team obtained a series of five
crossed scans of radio astronomy sources together with dwells on cold sky.
The spacecraft HGA was initially commanded to point at an offset from the
source direction of -1 degree along the NH body X coordinate, and then scanned
across the source at 1E-4 rad/s to X = +1 degree, a maneuver that required
approximately 350s.  Similar scans were performed for the vertical, or Z
coordinate, but with a dwell of 300 s at the origin X = Z = 0.

Two of the targets were positioned on the sky where the galactic synchrotron
background was very low, and within a few tenths of a kelvin of the Cosmic
Microwave Background (CMB).  These two targets were called the Cold Sky Cals.
The other targets were standard radio sources with known radio fluxes.  The
calibration procedure then mapped the SNR's of the targets (the signal was
characterized by the radio sources; the noise was characterized by the Cold
Sky Cals) against the expected radio fluxes, and produced a log-log linear
relationship with a 1% standard deviation.

One-second samples of power in a 4.5 MHz bandwidth were smoothed using a 10s
sliding window; the standard deviation of the 10s averages indicates that the
NH transceiver is radiometrically stable at a level of approximately 5 parts
in 10,000, and thus adequate for measuring radiometric temperature to a
one-sigma uncertainty of about 0.1K (1 part in 1000).

Again, refer to DOCUMENT/NH_REX_RADIOMETER_CALIB_V4P7.LBL for the latest
information regarding how the REX calibration was performed.

Gain Linearity tests
--------

The gain setting (AGC or AGCGAIN) is designed to produce linear results
in the radiometry calibration formula in units of dBm (the formula is
available in the Science Operations Center/Instrument Interface Control
Document - SOC_INST_ICD).  These tests varied the gain setting (steps
of two in the gain setting, equivalent to ~1dB) while measuring a single
target source i.e. an unmodulated, constant-strength signal sent from the
DSN.  The results indicated that the instrument performs as designed.

Note that the acronym AGC comes from the nomenclature of the RF Uplink
hardware, which is separate from REX, and which uses Automatic Gain Control as
part of its carrier tracking loop.  For REX there is no automatic gain control
and REX gain is manually set by commands from the ground based on the expected
uplink power, or radiometry, in the REX band.

As of 2017, a link analysis is in process to verify the amplitude stability
of the gain over the length of the mission. Please contact the instrument
representative or the SOC for more details if needed.

Instrument characterizations
--------

In addition to instrument calibration, the following activities were performed
as part of commissioning during the Launch mission phase.

Some of these tests were also performed during the Pluto Cruise mission phase
as part of spacecraft Annual CheckOut (ACO) activies to monitor instrument
functionality and stability.


Spur tests/Spurious signal tests/Find weak tones, no uplink
--------

The test for spurs in the REX band is part of the Annual Checkout activities
for New Horizons.  The test involves setting the open-loop AGC to near the
upper end of it's range and acquiring REX data with no uplink.  A spur is a
narrowband frequency, revealed as a narrow spectral line in the
time-integrated spectrum of the REX band.


Interference tests
--------

During encounter, multiple instruments on-board New Horizons operated
simultaneously.  Tests were performed during Commissioning to verify that
simultaneous operation of these instrument suites did not cause mutual
interference.  For REX, both REX and ALICE operated simultaneously to
observe the occultations of the Earth and Sun by Pluto and Charon.  At Pluto
Encounter, the Earth and Sun are separated by 1.5 degrees, and Earth
occultations for REX and the Solar occultation for ALICE by Pluto and Charon
occurred very close together in time.  The mutual interference test for REX
and ALICE had both instruments on, i.e. both REX and ALICE were acquiring
data, REX without an uplink and ALICE without the Sun in it's aperture.
Neither instrument found any artifacts during these tests.


Uplink simulates multi-tones to assess intermodulation distortion
--------

Two uplinks, close in frequency in the REX band, were transmitted to New
Horizons in each of Right-hand and Left-hand Circular Polarization (RCP and
LCP), to assess the incidence of intermodulation distortion.  None was found
at a level of less than -60 dBc.


Miscellaneous characterizations and tests; see [TYLERETAL2008] section 6
--------

- Functional Verification
- Uplink Signal Acquisition (minimum SNR)
- USO Stability
- REX Passband Response


Summary
-------

All calibration and characterization activities indicate the REX instrument
operates as expected.

See section 6 of [TYLERETAL2008] for more details of the REX instrument
performance, as well as DOCUMENT/NH_REX_RADIOMETER_CALIB_V4P7.LBL.


Operational Considerations - REX
========

Controls
--------

The primary controls for REX are its power, the allocation of memory to store
REX data on the Solid State Recorder (SSR) via Command and Data Handling
(C&DH), and the gain setting (AGC).  REX generates In-phase, Quadrature-phase
and Radiometry values whenever it is on, although the memory allocation
determines when and whether those values are stored in the SSR.
Configuration of the spacecraft telecommuncations subsystem for use by REX
([HASKINS&MILLARD2004]; [TYLERETAL2008]; [DEBOYETAL2004]), allocation of
memory on the Solid State Recorder to store REX data, and telemetering stored
data to Earth are all necessary but outside the scope of this document.

The intersection of the periods when REX was on (time) and data allocations
(data volume) can be inferred from the existence of time-contiguous files of
REX data in the archived data set.

The AGC settings are provided as state tables, REX_ACGGAINA.* and
REX_AGCGAINB.* in the DOCUMENT/ section of the REX data sets.

Note that the acronym AGC comes from the nomenclature of the RF Uplink
hardware, which is separate from REX, and which uses Automatic Gain Control as
part of its carrier tracking loop.  For REX there is no automatic gain control
and REX gain is manually set by commands from the ground based on the expected
uplink power, or radiometry, in the REX band.


REX data compression and Time Tag anomalies
-------------------------------------------

REX writes data to the SSR as a series of frames at 1 frame per 1.024s, from
the first 1PPS (One Pulse Per Second spacecraft timekeeping signal)
encountered after both the instrument is powered on and an SSR allocation goes
active, until either the instrument is powered off or the SSR allocation is
filled.  For this reason, it is possible for the first frame written to the
SSR (due to the wait until the first 1PPS) and last frame written to the SSR
(due to a power off asynchronous with frame boundaries) to be incomplete.

When REX data are stored to the SSR using compression, C&DH processing logic
assumes complete frames.  Thus, when C&DH tries to compress REX data with
incomplete frames, it logs an error.  Once this behavior was recognized (after
05 March 2007) REX data were always downlinked in packetized formats
(Application Process Identifiers. ApIDs - 0x7b1 or 0x7b3) rather than
compressed formats (ApIDs 0x7b0 or 0x7b2).  N.B. ApIDs are case insensitive.

REX Time Tags are used to keep track of REX Output Frames (ROFs) by
incrementing ten times within each frame and continuing to
increment once between consecutive frames.  Inconsistencies in
the Time Tags can be used to locate errors due to the REX data compression
issue and any other corrupt frames.  Any such frames are listed in file
ERRATA.TXT in this data set.  Such frames are rare, so ignoring those frames
will not significantly affect REX data analysis.


Detector & Electronics - Flight Element
=======================================

The amplifier chain is a conventional heterodyne design (see the figure
below). The noise performance of the receiver has been improved over previous
implementations by locating the leading low-noise amplifier (LNA) close to the
antenna to reduce the effective temperature of the wave guide connecting the
LNA to the high-gain antenna (HGA). The various mixing frequencies, fLO, for
the intermediate frequency (IF) amplifier stages are derived from the USO, as
are the clock reference frequencies used to drive the analog-to-digital
converter. The REX portion of the system, which follows the 4.5 MHz buffer and
anti-aliasing filter, is made up of an analog-to-digital converter (ADC) which
feeds a triply redundant programmed gate array (FPGA). This gate array
implements the two data processing functions required by the REX experiment.
These are i) calculation of the total power in the 4.5 MHz bandwidth
containing the uplink signal that enters the antenna, and ii) processing of
the 4.5 MHz data stream to isolate the 1 kHz portion of the frequency spectrum
containing the occultation signals in order that these can be returned to the
ground efficiently. The output of both processes is passed to the NH on-board
data memory for later transmission to Earth.


 ____________________________NH Receiver___________________________
/                                                                  \

 HGA
\             _    +---------+    _   +-------------------> To NH Command
 \   +---+   / \   |  IF     |   / \  |                     & Tracking
+-)--|LNA|-->|X|-->|Amplifier|-->|X|--+
 /   +---+   \_/   | Chain   |   \_/  |   +-------------+
/             ^    +---------+    ^   +-->|4.5MHz Filter|--> To REX
 7.2Ghz       |f                  |f      +-------------+
 from DSN     | LO                | LO
              |   1               |   final
              |     +---+         |
              +-----|   |---------+
                    +---+
                      ^
 ____________________ | _____REX Signal Conditioning____________________
/                     |                                                 \
                     ~~~

           ==========REX Hardware==========================
           [                                              ]
           [              = = =FPGA = = = = = = = = = = = ]
           [                                              ]
           [              [                             ] ]
           [                      +----------+            ]
           [              [       |4MHz Power|          ] ] 10 samples/1024ms
f  =2.5MHz [  +-------+       +-->|Integrator|--(/40)-+   ] @ 5 bytes/sample
 IF        [  |  ADC  |   [   |   +----------+        | ] ]
from  ------->|(T ,f )|-(/12)-+                       +--------> To NH SSR
4.5MHz     [  |  s  s |   [   |   +----------+        | ] ]
Filter     [  +-------+       +-->|~1kHz I&Q |--(/16)-+   ] 1250 complex
           [              [       |Digital   |        | ] ] samples/1024ms
           [                      |Filter    |--(/16)-+   ] @ 2*2 bytes/sample
           [              [       +----------+          ] ]
           [                                              ]
           [              = = = = = = = = = = = = = = = = ]
           [                                              ]
           ================================================
                ^
                |    ~~~
                |     |
 ______________ | ___ | _____USO Frequency Distribution_______
/               |     |                                       \
  =====         |     |
 ( USO )--------+-----+----> to Transceiver
  =====


See also the description above and [TYLERETAL2008], which contains a better
figure than can be achieved by the ASCII graphics used above.


Operational Modes - REX
========

There are three controls on the REX hardware:  the power; the input signal
source; a gain control.  REX generates 1250 IQ sample pairs and 10
cumulative radiometry values per ROF any time it is powered on.  In addition
to the HGA signal, REX can also be commanded to process any of a set of
internal test patterns stored in the REX signal processor:  impulse
response; three square waves of different frequencies; two pseudo-random
number sequences of different amplitudes; all zeros.  The gain control is
an integer value that is kept track of via monitoring of uplink commanding;
there is no feedback of the gain setting in the data downlink.  The gain
control affects the radiometer calibration only; it does not affect the IQ
calibration.

The phrases 'REX mode' and 'Radiometry mode' are used in several documents;
they do not refer to specific instrument modes or configurations, but rather
to specific types of observation and whether the IQ pair or the radiometery
values are the focus of the observation.  Although they are not strictly
operational modes, they are defined here for convenience.

1) REX mode for occultation studies.

Returns 16-bit In-phase and Quadrature (I&Q) ADC value pairs from the input
signal.  The input signal is normally from the HGA by way of the receiver
electronics, but the input select command can make REX use any of seven
internally generated signals, for which the results can be compared with
deterministic results to ensure consistent operation of REX.

2) Radiometry mode for surface temperature measurement.

At those times when the New Horizons spacecraft high gain antenna (HGA) points
toward Pluto or Charon, the REX instrument, operating in a 'radiometry mode,'
will receive 7.2 GHz thermal radio emission from the two bodies.
Opportunities to observe radio thermal emission occur during the several
minutes of radio occultation measurements when the disks of Pluto and Charon
obscure the Earth.  The REX instrument will detect radiation from the
obscuring body as an increase in the radio system noise level in the
radiometry channel and also an increase in the noise floor of the occultation
channel.  These observations will be used to derive the nightside emission
temperatures of Pluto and Charon.  Similar observations will be taken of the
day side emission temperatures on approach for comparison.

See [TYLERETAL2008] for further details.


Measured Parameters - REX
========

1) Instantaneous strength of
   - uplink baseband signal, heterodyned by the Intermediate Frequency (IF)
     amplifier, a conventional design, to an intermediate frequency of
     2.5MHz, and passed through a 4.5Mhz filter,
   - sampled at 10 Msample/s,
   - downconverted and output as I&Q value pairs
     - at a rate of 1250 I&Q value pairs per 1.024s.

The process of down conversion from 10 Msample/s is accomplished by digitally
shifting to zero frequency the uplink carrier signal centered initially at
the 2.5MHz IF center frequency, followed by use of time-invarient baseband
filters to reduce the bandwidth.  The details are too extensive to include
here, but are explained in detail in [TYLERETAL2008].

2) Integrated power
   - cumulative over 1.024 seconds,
   - reset every 1.024 seconds,
   - at 10 samples per 1.024 second.

The REX power integrator (see the figure above) follows the conversion of the
uplink NH transceiver signal to 10 bit digital samples.  These data are passed
to the REX processor at a rate of 10 Msample/s, where they are processed to
extract the total power in the input stream.  This is accomplished by squaring
and averaging input samples over 102.4ms for each output sample, as

                 kN
               _____
               \
                \       2
  P  (k) =      /   s(i)
   UP          /____
                i=1

where

  s(i)    = one input sample (12 bit register, 10Ms/s)

  P  (k)  = one output power sample @ 40 bits
   UP

  k       = the index of one output sample, 1 to 10
  i       = the index of the input samples
  N       = the number of input samples included in 102.4ms


See [TYLERETAL2008] for further details.


Absolute time of Time Tags and Radiometry (10 samples per ROF)
==============================================================

  The Time Tags are absolute counters, starting at 0 for the START_TIME
  from PDS label of the first ROF in a run of ROFs, and increment every
  102.4ms.

  The raw radiometer values accumulate squared ADC measurements over
  each ROF, with the first raw radiometer value, in any ROF after the
  first ROF, representing the accumulation for the preceding ROF.  So
  the midpoint of the time period represented by each raw radiometer
  value is halfway between the time of the corresponding time tag and
  the previous START_TIME.  This means the midpoint for the first
  accumulated value, in any raw or calibrated (cal) ROF after the first
  ROF, is 512ms before START_TIME i.e. in the middle of the previous
  ROF.  The midpoint of the time period of the calibrated radiometer
  values, except the first in each ROF, is 51.2ms before the time of the
  corresponding time tag value.

  The items above are spelled out in the following table indicating the
  absolute timestamp for each of the column values in the ten rows of
  the EXTENSION_RAD_TIME_TAGS_TABLE OBJECT of the data files, where

    S0 = START_TIME (in the PDS label)

  +-------+---------------+---------------------+----------------------+
  | Index | Time Tag time | Raw radiometer time | Cal radiometer value |
  +-------+---------------+---------------------+----------------------+
  |   0   |  S0 +   0.0ms |   S0 - 512.0ms      |  S0 - 512.0ms        |
  |   1   |  S0 + 102.4ms |   S0 +  51.2ms      |  S0 +  51.2ms        |
  |   2   |  S0 + 204.8ms |   S0 + 102.4ms      |  S0 + 153.6ms        |
  |   3   |  S0 + 307.2ms |   S0 + 153.6ms      |  S0 + 256.0ms        |
  |   4   |  S0 + 409.6ms |   S0 + 204.8ms      |  S0 + 358.4ms        |
  |   5   |  S0 + 512.0ms |   S0 + 256.0ms      |  S0 + 460.8ms        |
  |   6   |  S0 + 614.4ms |   S0 + 307.2ms      |  S0 + 563.2ms        |
  |   7   |  S0 + 716.8ms |   S0 + 358.4ms      |  S0 + 665.6ms        |
  |   8   |  S0 + 819.2ms |   S0 + 409.6ms      |  S0 + 768.0ms        |
  |   9   |  S0 + 921.6ms |   S0 + 460.8ms      |  S0 + 870.4ms        |
  +-------+---------------+---------------------+----------------------+


Absolute time of IQ pairs (1250 sample pairs per ROF)
=====================================================

  The timestamp apropo the first IQ pair in a ROF is (1024/1250)ms
  before the START_TIME of that ROF; the timestamp of any other IQ pair
  is (1024/1250)ms after the previous IQ pair.


Instrument Overview - DSN
=========================

  Three Deep Space Communications Complexes (DSCCs) (Barstow, CA; Canberra,
  Australia; and Madrid, Spain) compose the Deep Space Network (DSN).  Each
  complex is equipped with several antennas, associated electronics, and
  operational systems. Transmission and reception are possible in several
  radio frequency bands; REX uses X-band (7100-8500 MHz, or 4.2-3.5 cm).

  The DSN is managed by the Jet Propulsion Laboratory (JPL), California
  Institute of Technology, for the U.S. National Aeronautics and Space
  Administration (NASA).

  For more information on the DSN and its use in Radio Science see
  [ASMAR&RENZETTI1993].  For design specifications on DSN subsystems see
  [DSN810-5].


REX Use of the DSN
==================

  When REX measures signals transmitted by the DSN, the transmitted frequency
  is corrected for station motion (e.g., Earth orbit and rotation) and
  spacecraft motion so that the signal received at the spacecraft is within a
  narrow fraction (a few hundred Hertz) of the 2.5 MHz IF.

  For REX occultations, the DSN provides a frequency ephemeris (a description
  of the transmitted frequency as a series of linear ramps) in Tracking and
  Navigation Files (TNFs).  REX radiometry observations do not require DSN
  signals. Hence, Tracking and Navigation Files (TNF) are not required prior
  to arrival at Pluto, other than for Lunar occultations in 2011 and 2014.

  In general, any time REX was using DSN uplink signals, the DSN transmitted
  the polarization of uplink signal(s) apropo to the REX Sides (A and/or B)
  that were in operation at that time.  That is, when only Side A was on,
  the DSN transmitted RCP uplink signal; when only Side B was on, the DSN
  transmitted LCP uplink signal; when both Sides A and B were on, the DSN
  transmitted both RCP and LCP uplink signals.


Subsystems - DSN
================

  The DSCCs are an integral part of Radio Science instrumentation.  The
  following paragraphs describe the functions performed by individual
  subsystems of a DSCC. For additional information, consult [DSN810-5].

  Each DSCC includes a set of antennas, a Signal Processing Center (SPC),
  and communication links to JPL.  The following table lists some of the DSN
  antennas available to REX.  The Deep Space Station (DSS) nomenclature
  has been carried over from earlier times when antennas were individually
  instrumented.

                      GOLDSTONE     CANBERRA      MADRID
        Antenna        SPC 10        SPC 40       SPC 60
        --------      ---------     --------     --------
        34-m HEF        DSS 15       DSS 45       DSS 65
        34-m BWG        DSS 24       DSS 34       DSS 54
                        DSS 25       DSS 35       DSS 55
                        DSS 26       DSS 36
        34-m HSB        DSS 27
                        DSS 28
        70-m            DSS 14       DSS 43       DSS 63
        Developmental   DSS 13

  Antennas are grouped above by diameter and design. HEF is high efficiency,
  BWG is beam waveguide, and HSB is high-speed BWG.

  DSCC Receiver-Exciter Subsystem
  -------------------------------
    The receiver-exciter subsystem is split into the exciter component (UPL
    for Uplink Subsystem) and a separate receiver component, not used by REX.
    The UPL comprises the Exciter, the Command Modulation, the Uplink
    Controller, and the Uplink Ranging assemblies. The exciter generates
    a sky-level signal, which is provided to the Transmitter Subsystem (TXR)
    for transmission to the spacecraft. It is tunable under command of a
    Digitally Controlled Oscillator (DCO).

  DSCC Transmitter Subsystem
  --------------------------
    The Transmitter (TXR) Subsystem accepts a sky-level frequency signal from
    the Uplink Subsystem exciter. This signal is routed via the diplexer
    through the feed horn to the antenna, where it is then focused and
    beamed to the spacecraft.

    The Transmitter Subsystem power capabilities range from 18 kW
    to 400 kW, for S- and X-band uplink.  Power levels above 20 kW
    for NH REX operations were supplied only from 70-m stations.

  DSCC Monitor and Control Subsystem
  ----------------------------------

    The DSCC Monitor and Control Subsystem (DMC) is part of the Monitor and
    Control System (MON) which also includes the ground communications
    Central Communications Terminal (CCT) and the Network Operations Control
    Center (NOCC) Monitor and Control Subsystem.  The DMC is the center of
    activity at a DSCC.  The DMC receives and archives most of the
    information from the NOCC needed by the various DSCC subsystems during
    their operation.  Control of most of the DSCC subsystems, as well as the
    handling and displaying of any responses to control directives and
    configuration and status information received from each of the
    subsystems, are done through the DMC.  The effect of this is to
    centralize the control, display, and short-term archiving functions
    necessary to operate a DSCC.  Communication among the various subsystems
    is done using a Local Area Network (LAN) hooked up to each subsystem via
    a network interface unit (NIU).


    The DSCC Monitor and Control (DMC) subsystem operations are divided into
    two separate areas: the Complex Monitor and Control (CMC) and the Network
    Monitor and Control (NMC).  The primary purpose of the CMC processor for
    Radio Science support is to receive and store all predict sets transmitted
    from the Network Operations Control Center (NOCC) -- such as antenna
    pointing, tracking, receiver, and uplink predict sets -- and then, at a
    later time, to distribute them to the appropriate subsystems via the LAN.
    The NMC processor provides the operator interface for monitor and control
    of a link -- a group of equipment required to support a spacecraft pass.

  DSCC Tracking Subsystem
  ----------------------------------
    All Tracking Subsystem (DTK) functions are incorporated within the UPL
    and the Downlink Tracking and Telemetry Subsystem (DTT). The primary
    functions of the DTK are to acquire and maintain communications with
    the spacecraft and to generate and format radio metric data containing
    Doppler, range, and uplink frequency ramps.  Only the ramps are used
    for REX.

    In addition, the Tracking Subsystem receives from the CMC uplink tuning
    predicts (used to program the DCO).  From the (NMC, it receives
    configuration and control directives, as well as configuration and status
    information on the transmitter, microwave, and frequency and timing
    subsystems.

  DSCC Frequency and Timing Subsystem
  -----------------------------------
    The Frequency and Timing Subsystem (FTS) provides all of the
    frequency and timing references required by the other DSCC
    subsystems.  It contains four frequency standards, of which
    one is prime and the other three are backups.  Selection of
    the prime standard is done via the CMC.  Of these four
    standards, two are hydrogen masers followed by clean-up loops
    (CUL) and two are cesium standards.

    Allan Deviations of the signals sent to REX (derived from FTS) are:

           Integration Time (seconds)            Allan Deviation
           --------------------------          --------------------
                        1                              2E-13
                       10                              8E-14
                      100                              2E-14
                     1000                              4E-15


Optics - DSN
============

  X-Band performance of the DSN ground stations depends primarily on the size
  of the antenna and capabilities of the electronics.

  Antenna Performance
  -------------------
    Performance of antennas is summarized in the following table.  Beamwidth
    is half-power full angular width. Polarization is circular; X-Band can
    transmit either left or right circular polarization (LCP or RCP,
    respectively).

                       DSS X-Band Characteristics

                                          70-m      34-m     34-m
       Transmit                                      BWG      HEF
       --------                          -----     -----    -----
       Frequency (MHz)                   7145-     7145-    7145-
                                          7190      7190     7190
       Wavelength (m)                    0.042     0.042    0.042
       Ant Gain (dBi)                       73        67       67
       Beamwidth (deg)                   0.038     0.077    0.077
       Polarization                     L or R    L or R   L or R
       Tx Power (kW)                      >=20        20       20

    Although some 34-m antennas were either upgraded or in the process of
    being upgraded during Pluto Encounter, only 70-m antennas were used
    to transmit at powers above 20kW for NH REX operations.


  Antenna Pointing
  ----------------
    Pointing of DSCC antennas may be carried out in several ways. In  conscan
    mode antenna pointing is offset slightly, following a conical path around
    the nominal direction during routine uplink commanding and telemetry
    reception. The slight signal degradation during one time interval is used
    to correct the pointing for the next. In planetary mode, the system
    interpolates from three (slowly changing) RA-DEC target coordinates;
    this is 'planetary' pointing since there is no feedback from a detected
    signal. In sidereal mode, the antenna tracks a fixed point on the
    celestial sphere. In precision mode the antenna pointing is adjusted
    using an optical feedback system. REX uses only planetary pointing.


Calibration - DSN
=================

  Calibrations of hardware systems are carried out periodically by DSN
  personnel; these ensure that systems operate at required performance levels
  - for example, that antenna patterns, receiver gain, and propagation delays
  meet specifications.  Additional information may be available in [DSN810-5].


Location - DSN
==============

  Accurate analysis of REX occultation data requires knowledge of the
  locations of the DSN tracking stations.  The coordinate system in which the
  locations of the tracking stations are expressed should be consistent with
  the reference frame definitions used to provide Earth orientation
  calibrations.

  The International Earth Rotation Service (IERS) has established
  a terrestrial reference frame for use with Earth orientation
  measurements. The IERS issues a new realization of the terrestrial
  reference frame each year.  The definition of the coordinate
  system has been changing slowly as the data have improved
  and as ideas about how to best define the coordinate system have
  developed.  The overall changes from year to year have been at the
  few-cm level.  Refer to [DSN810-5] section 301 or the Navigation and
  Ancillary Information Facility at JPL SPICE kernels for the latest
  locations; the values provided here are only provided as examples.

  The DSN station locations have been determined by use of VLBI
  measurements and by conventional and GPS surveying.

  The DSN Station Locations in ITRF1993 Cartesian reference frame
  at the epoch noted (assuming subreflector-fixed configuration)
  are as follows:

  Antenna     x(m)          y(m)          z(m)      Epoch
  --------------------------------------------------------
  DSS 13  -2351112.491  -4655530.714  +3660912.787  1993.0
  DSS 14  -2353621.251  -4641341.542  +3677052.370  1993.0
  DSS 15  -2353538.790  -4641649.507  +3676670.043  1993.0
  DSS 34  -4461146.720  +2682439.296  -3674393.517  1993.0
  DSS 35  -4461273.0838 +2682568.9220 -3674152.0885 2003.0
  DSS 36  -4461170.2358 +2682816.0240 -3674085.9737 2003.0
  DSS 43  -4460894.585  +2682361.554  -3674748.580  1993.0
  DSS 45  -4460935.250  +2682765.710  -3674381.402  1993.0
  DSS 63  +4849092.647  -0360180.569  +4115109.113  1993.0
  DSS 65  +4849336.730  -0360488.859  +4114748.775  1993.0


ACRONYMS AND ABBREVIATIONS - DSN
================================

  ACS      Antenna Control System
  ADC      Analog-to-Digital Converter
  AGC      Automatic Gain Control N.B. REX gain is not automatic
  ATDF     Archival Tracking Data File
  AUX      Auxiliary
  BPF      Band Pass Filter
  bps      bits per second
  BVE      Block V Exciter
  BVR      Block V Exciter
  BWG      Beam WaveGuide (antenna)
  CCT      Central Communications Terminal
  CDU      Command Detector Unit
  CMC      Complex Monitor and Control
  CRG      Coherent Reference Generator
  CSO      Compensated Sapphire Oscillator
  CUL      Clean-up Loop
  DANA     a type of frequency synthesizer
  dB       deciBel
  dBi      dB relative to isotropic
  dBm      dB relative to one milliwatt
  DCO      Digitally Controlled Oscillator
  DEC      Declination
  deg      degree
  DMC      DSCC Monitor and Control Subsystem
  DOD      Differential One-Way Doppler
  DOR      Differential One-way Ranging
  DSCC     Deep Space Communications Complex
  DSN      Deep Space Network
  DSS      Deep Space Station
  DTK      DSCC Tracking Subsystem
  DTT      DSCC Downlink Tracking and Telemetry Subsystem
  E        east
  EL       Elevation
  FTS      Frequency and Timing Subsystem
  GHz      Gigahertz
  GPS      Global Positioning System
  HEF      High-Efficiency (as in 34-m HEF antennas)
  HGA      High-Gain Antenna
  HSB      High-Speed BWG
  I        In-phase
  IERS     International Earth Rotation Service
  IF       Intermediate Frequency
  IVC      IF Selection Switch
  JPL      Jet Propulsion Laboratory
  K        Kelvin
  kbps     kilobits per second
  LCP      Left-Circularly Polarized
  LGA      Low-Gain Antenna
  LMC      Link Monitor and Control
  LNA      Low-Noise Amplifier
  LO       Local Oscillator
  Ms/s     Million samples per second
  m        meters
  MCA      Master Clock Assembly
  MDA      Metric Data Assembly
  MHz      Megahertz
  MON      Monitor and Control System
  MSA      Mission Support Area
  N        north
  NH       New Horizons
  NMC      Network Monitor and Control
  NOCC     Network Operations and Control System
  NRV      NOCC Radio Science/VLBI Display Subsystem
  NSS      NOCC Support Subsystem
  OCI      Operator Control Input
  PDS      Planetary Data System
  Q        Quadrature
  RA       Right Ascension
  REC      Receiver-Exciter Controller
  REX      Radio Science Experiment (a New Horizons instrument)
  RCP      Right-Circularly Polarized
  RF       Radio Frequency
  RFE      (Probe) Receiver Front End
  RFIS     Radio Frequency Instrument Subsystem
  RFS      Radio Frequency Subsystem
  RMS      Root Mean Square
  SPC      Signal Processing Center
  sps      samples per second
  SRA      Sequential Ranging Assembly
  SSR      Solid State Recorder or Space Science Reviews, (publication
            journal)
  TBD      to be determined
  TDDS     Tracking Data Delivery Subsystem
  TID      Time Insertion and Distribution Assembly
  TLM      Telemetry
  TLP      Telemetry Processor
  TNF      Tracking and Navigation File
  TWM      Traveling Wave Maser
  TXR      Transmitter (subsystem)
  UNK      unknown
  UPL      DSCC Uplink Subsystem
  USO      UltraStable Oscillator
  UTC      Universal Coordinated Time
  VLBI     Very Long Baseline Interferometry
  X-band   approximately 7800-8500 MHz
        