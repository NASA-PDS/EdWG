
 
Instrument Overview
===================
 
The communication, tracking, and timekeeping systems on LRO support
the generation of the precise geolocation needed by the LRO science and
measurement investigations.  The information provided by these systems is
similar to conventional Radio Science data, although traditional 'radio
science' was not an initial mission objective. The importance of the
tracking data for all of the other investigations merits its being archived
for completeness and future analysis.
 
Radio Doppler and range tracking to the LRO omnidirectional and
high-gain antennas (HGA) provides the main source of the radio science data.
The gimbaled HGA also carries a small, coboresighted, optical receiver
telescope. One-way time-of-flight from the ground to the optical receiver
using laser pulses provides an alternate tracking data type known as Laser
Ranging (LR), which is handled jointly by the Lunar Orbiter Laser Altimeter
(LOLA) Science Operations Center (SOC) and the Crustal Dynamics Data
Information System (CDDIS). The spacecraft Radio Frequency subsystems are
described herein and in more detail in [TOOLEYETAL2010]. The LR subsystem
is described in [ZUBERETAL2009], and in the LOLA instrument description
[SMITHETAL2009]. The ground elements consist of the commercial Universal
Space Network (USN), the Ka-band ground station at White Sands, New Mexico
(WS1), and the Next Generation Satellite Laser Ranging station in Greenbelt,
Maryland (NGSLR).
 
Additional data were provided by the NASA Deep Space Network (DSN) during
commissioning. Ongoing participation by the International Laser Ranging
Service (ILRS) network of stations provides further LR data that are
processed by the LOLA SOC.
 
Communication Subsystem
-----------------------
LRO's communications system consists of an S-band system to provide tracking,
telemetry and commanding (TT&C) and a high data rate Ka-band, downlink-only
system for telemetry and science data transfers. The S-Band system has a fixed
forward link data rate of 4 kbps, and a selectable on-orbit return link data
rate between 125 bps and 1093 kbps. It consists of one Spacecraft Tracking
and Data Network (STDN) compatible transponder, an S-band Radio Frequency
(RF) Switch, and the RF paths to and from the two Omni-Directional antennas
and the S- band feed on the High Gain Antenna (HGA).
 
The transponder downlinks at a frequency which is phase-locked to the uplink,
providing two-way Doppler tracking information to the ground with an accuracy
of better than 1 mm/s.  It also repeats uplinked range tones with a fixed
delay, allowing the ground to determine the distance to the Orbiter within
15 m. The Ka-band system includes a Ka-Band modulator, a Traveling Wave Tube
Amplifier (TWTA) consisting of a traveling wave tube (TWT), an Electronic
Power Conditioner (EPC), and a High Power Isolator. The Ka-band return link
is also selectable on orbit and varies from 25 Mbps to 100 Mbps.
Although the Ka-band system uses only the High Gain Antenna, the S-band
system can utilize either the Omni-Directional or the High Gain Antenna for
transmit and always uses both paths for receiving. The ground selects the
uplink path via polarization, as the HGA has opposite polarization from the
omni antennas for this reason.  Specifications for each of the S- and Ka-Band
subsystems are given in [TOOLEYETAL2010]. In brief, frequency, polarization,
and RF transmit power for the spacecraft are:
 
S-Band System:
2271.2 +/- 2.5 MHz (Transmit), 2091.3967 +/- 2.5 MHz (Receive);
Left Hand Circular Polarization (Omni)
Right Hand Circular Polarization (HGA)
5.8 Watt Diplexers
 
Ka-Band System:
25.65 GHz +/- 150 MHz (Transmit)
Left Hand Circular Polarization
41.9 Watt TWTA Output
 
The S-Comm card is designed to accommodate a telemetry interface to Earth
using S-Band frequencies. The S-Comm card is connected directly to the Single
Board Computer (SBC) via a 10 Mbps SpaceWire link [NGUYENETAL2008]. During
a ground station pass the data from the SBC flow directly into the S-Comm
card and are encoded for transmission per CCSDS recommendations for
telemetry encoding using concatenated encoding. The S-Comm provides one
telemetry stream at up to 1.093 Mbps to the transmitter for Bi-Phase Shift
Keying (BPSK) modulation onto the RF carrier.The S-Comm accepts uplinked
CCSDS telecommands from the S-Band transponder at 4 Kbps. Normally commands
are forwarded to the SBC for further processing via the SpaceWire
interface unless they are tagged as hardware-decoded commands. Hardware-
decoded commands are performed directly by the S-Comm card. The S-Comm card
can support up to 8 hardware-decoded commands, 4 of which are RS-422 outputs.
Hardware- decoded commands are only used in contingency situations.Both the
S-comm and Ka-comm card provide control of the respective Communication
Subsystem transmitters via asynchronous low rate serial interfaces.
 
LRO makes use of a global network of S-band ground stations for nominal
spacecraft tracking (at least 30 minutes per orbit) and one Ka-band station
for downlink of all the stored instrument and spacecraft data. Nominally, LRO
is never be out of contact with the ground for more than one hour at a time.
Station-keeping maneuvers and instrument calibrations occur once a month.
Momentum management maneuvers occur every 2 weeks. There is an S-band pass
every orbit (12 per day), and 4 (on average) Ka-band passes between LRO and
WS1 every day, each lasting 45 minutes. The actual number fluctuates between
2 and 6, as the Moon moves through its entire declination range each month
(as seen from the Earth). Most of the instruments operate autonomously over
the course of a single orbit, while two (LROC and Mini-RF) require daily
tailored command timelines. Nominally, LRO receives a new command timeline
from the ground once per day that includes tracking schedules and antenna
targets.
 
Ultra Stable Oscillators (USO)
------------------------------
The C&DH subsystem includes both a primary and a redundant USO to provide
precision timekeeping onboard the spacecraft. Each oscillator provides two
20-MHz signals. One signal goes to the C&DH HK/IO card and the second goes
directly to the LOLA instrument. Only one of the oscillators is powered
at any given time. The primary USO has a frequency stability factor of 10
parts per billion (ppb) over one millisecond (ms). It was chosen to provide
sufficient stability to meet the needs of the laser ranging system.
It receives a +31VDC switched service from the Power Subsystem Electronics
(PSE). The redundant USO has a frequency stability factor of 0.3
parts per million (ppm) over one millisecond (ms). It was chosen to provide
sufficient stability to meet the needs for LOLA reconstruction of the
orbital ephemeris. It receives a +15VDC switched service from the LVPC.
 
Data Downlink
-------------
The LRO flight computer is a RAD-750 processor executing at 133 MHz.
Two 100 Gbyte recorders store science data for playback to the earth at
100 Mbps. An S-band system provides command, engineering telemetry,
and navigation functions. On a given day, about 460 Gbits of data are
generated on-board the LRO spacecraft. Data are downlinked at 100 Mbps
through a single Ka-band ground station at White Sands, New Mexico,
USA (designated WS1). Even in the worst case (2 passes), there is sufficient
time to downlink the entire day's data volume.
 
Active One-Way Laser Ranging System
-----------------------------------
During the preliminary design phase an active one-way (uplink) laser ranging
system was added to LRO to improve the tracking, and thus geodetic accuracy
of the data products, over that possible with the S-Band tracking system
alone.  The elements of the active laser ranging system include a ground
station at GSFC, which transmits a 532 nm pulse at 28 Hz. This pulse is
captured by the laser ranging telescope mounted on the high gain antenna and
then transmitted via fiber optic cable to the LOLA detector assembly.
Time-stamped arrival and departure times allow for precise range measurements
from Earth to the LRO spacecraft, thus helping to determine precise position
relative to the Earth's surface. Those data, combined with known positioning
of the spacecraft and LOLA data gathered from the Moon, provide enough
information to improve the lunar gravity modeling which can, in turn, be used
to improve the orbit determination.
 
Passive Two-Way Laser Ranging System
------------------------------------
In addition to the active laser ranging system LRO carries a retro-reflector
assembly consisting of twelve 1-inch-diameter solid retro-reflective prisms
in a square array mounted on the -Z face (zenith radiator). This retro-
reflector allows high-power terrestrial laser ranging sites to perform
two-way laser ranging to LRO. This ranging is conducted as an
experiment of opportunity late in the mission. The HGA must be parked for
safety and to provide visibility to the retro-reflector assembly from Earth.
As well, the array must point within approximately 20 degrees of Earth, which
is only possible for a few days a month while LRO is in mapping
configuration.
 
Ground stations
---------------
The baseline tracking system for LRO is an S-band (2.2-2.3 GHZ) radio
frequency link for approximately ~20 hours per day [CHINETAL2007].  A
commercial network, the Universal Space Network (USN), provides
tracking with stations at Dongara, Australia; Kiruna, Sweden; Weilham,
Germany; and South Point, Hawaii. The Doppler accuracy of the USN is ~1 mm/s
(one sigma) averaged over 10 s, which for the tracking time allocated
permits LRO orbits to be determined to approximately ~10 m radially and 300
m along-track and across-track.
 
Several ILRS stations [PEARLMANETAL2008] participate in the
LR investigation as ground stations. The addition of ILRS stations provides
global coverage for LR and increases the laser ranging data set. A few of the
participating ILRS stations are also synchronizing their laser fires to the
LOLA Earth window in a similar manner to NGSLR, while several others are
firing asynchronously at 5 or 10 Hz. At 10 Hz only 2 to 4 pulses per second
fall in the LOLA Earth window. The remaining 6-8 pulses are treated
as noise by LOLA, but these are not enough to cause significant disruptions
to the LOLA measurements. Since this is an uplink-only ranging measurement,
there is no real-time feedback of spacecraft tracking as in normal SLR
operations.  Instead, LOLA's real-time housekeeping telemetry is used to
provide needed feedback to the stations. LOLA's onboard signal processing
indicates whether the Earth pulses are arriving at LRO, and in addition
tracks the time at which these pulses occur within the Earth window. The LOLA
Earth energy monitor also provides an integrated energy over each Earth
window. This information is posted in graphical form to a password protected
website that provides feedback to all participating stations. The delay
between spacecraft event and webpage plot should be less than 30s. NGSLR is
able to bias its fire times from this information to: (1) search for the
Earth window if no signal is seen in the LOLA housekeeping telemetry, and/or
(2) ensure that its laser pulses are arriving as early as possible in the
single-stop Earth window.
 
 
Appendix
--------
The USN station positions are given in the table below, in geographic
coordinates (WGS-84 Ellipsoid):
Name / idstation / lat (ddmmss.ss) / lon (ddmmss.ss) / altitude (m)
-------------------------------------------------------------------
KU1S    1 126  67 53 22.4100     21 03 56.3571 400.400  Kiruna
KU2S    1 127  67 52 59.4570     21 03 37.6140 442.000  Kiruna
WU1S    1 128  47 52 48.2500     11 05 07.0890 663.392  Weilheim
WU2S    1 129  47 52 52.3160     11 05 01.0280 663.374  Weilheim
USHS    1 105  19 00 50.0562    204 20 12.1155 385.194  Hawaii
USPS    1 103 -29 02 44.7798    115 20 55.2395 250.470  Dongara
 
The body-fixed coordinates of the tracking stations (X, Y, Z):
Name          Code    Coordinates (x,y,z; km)
--------------------------------------------------------
USN_Kiruna_1  KU1S    2246.85161 865.44085    5886.83851
USN_Kiruna_2  KU2S    2247.55970 865.47907    5886.60934
USN_Wilheim_1 WU1S    4206.09325 824.08227    4708.43445
USN_Wilheim_2 WU2S    4206.02603 823.94076    4708.51867
USN_Hawaii    USHS   -5496.58634 -2486.04351  2064.93016
USN_Dongara   USPS   -2389.19709 5043.29132  -3078.45895
White_Sands   WS1S   -1539.02700 -5158.58418  3411.91754
 
The data downlink stations are:
Name                  Code   Coordinates (x,y,z; km)
---------------------------------------------------------------
White_Sands_Ka_band   WS1K   -1539.02700 -5158.58418 3411.91754
SDO_backup_Ka_band    STSK   -1539.01044 -5158.52883 3412.00723
 
Some DSN or other network stations that participated during commissioning:
 
Name                  Code    Coordinates (x,y,z; km)
----------------------------------------------------------------
DSN_Goldstone_24      DS24    -2354.90671 -4646.84008 3669.24232
DSN_Canberra_34       DS34    -4461.14709 2682.43924  -3674.39313
DSN_Madrid_54         DS54     4849.43449 -360.72390  4114.61884
 
Coordinates of Laser Ranging stations that track the LRO HGA:
Name                  Code  ID     Coordinates (x,y,z; km)
-----------------------------------------------------------------------
LR_Greenbelt_NGSLR    GO1L  7125   1130.74360  -4831.37152  3994.07940
LR_Greenbelt_MOBLAS7  GODL  7105   1130.719703 -4831.350572 3994.106526
LR_Hartebeesthoek_SA  HARL  7501   5085.40368  2668.33144  -2768.69029
LR_McDonald_Texas     MDOL  7080   -1330.0210  -5328.4018   3236.4807
LR_Monument_Peak_CA   MONL  7110   -2386.27943 -4802.35655  3444.88331
LR_Zimmerwald_Swtzlnd ZIML  7810   4331.28368  567.54974    4633.14027
LR_Herstmonceaux_UK   HERL  7840   4033.46371  23.66248     4924.30517
LR_Grasse_France      GRSM  7845   4581.69218  556.19602    4389.35507
LR_Wettzel_Germany    WETL  7834   4075.57685  931.78546    4801.58356
LR_Yarragadee_AU      YARL  7090   -2389.00813 5043.33184  -3078.52644

        