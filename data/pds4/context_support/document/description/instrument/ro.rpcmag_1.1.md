
 
 
Instrument Overview
===================
 
 
The ROSETTA orbiter magnetometer (RPCMAG)is part of the ROSETTA Plasma
Consortium (RPC) set of Scientific instruments. The purpose of the
magnetometer is the measurement of the interplanetary magnetic field
close to different targets visited by the ROSETTA spacecraft.
 
 
 
Science Objectives of the Investigation
=======================================
+ Measurements of the interplanetary magnetic field during the flybys
  at planet Mars & Earth, the asteroids and in the environment of
  comet 67p/Churyumov-Gerasimenko.
+ Study of the structure and dynamics of the cometary-solar wind
  interaction region.
+ Study of the generation and evolution of the cometary magnetic
  Cavity.
+ Study of cometary tail evolution and structure.
 
 
 
The Cometary Magnetic Field - A historical perspective
======================================================
 
In 1951 the German Astronomer Ludwig Biermann used the fact that
cometary tails are always pointing away from the Sun to postulate the
solar wind.
It was Hannes Alfven who suggested in 1957 that cometary tails are due
to the draping of the interplanetary magnetic field around the
cometary nucleus.
To explain this draping effect C.S. Wu and R.C. Davidson in 1972
studied the pick-up of cometary ions and the associated mass loading
of the solar wind.
Associated strong plasma wave turbulence due to this mass loading was
first detected by B.T. Tsurutani and E.J. Smith in 1986.
 
The magnetic field draping itself was first measured by F. M. Neubauer
and co-workers using magnetic field measurements made onboard the
GIOTTO s/c.
 
 
 
The ROSETTA Orbiter Magnetic Field Instrument
=============================================
 
+ Fluxgate-Magnetometer with a resolution of at least 40 pT
+ 2 Sensors OB/IB
+ 20 Bit ADC
+ Measuring B-Field in 3 components with a max. vector rate of 20 Hz
+ The Fluxgate Magnetometer RPC-MAG performance parameters are in full
  accordance with the EID-B design goals.
+ The Outboard/ Inboard sampling rate can be inverted by command
  either for higher Inboard time resolution or in case of outboard
  failure.
+ The sensors are fully calibrated also versus a wide temperature
  range. The temperature at Outboard and Inboard sensor is monitored
  in MAG housekeeping data.
 
 
 
FGM Classification
===================
+ Saturated-Core-Magnetometer
+ Vector measurements possible
+ No absolute measurements
+ Lightweight, compact construction
+ Low power consumption
+ Qualified for space applications
 
 
RPC-MAG FGM  Characteristics
============================
 
 Mass (sensor):                             45 g
 Volume (sensor):                        23 cm^3
 Mass (electronics):                       336 g
 Mass (harness H10):                       109 g
 Mass (harness H11):                        55 g
 Power:                            840  mW @ 28V
 Operation interval:                    15 years
 Sampling:                          20 vectors/s
 Bandwidth:                            0 - 10 Hz
 Resolution:                          +-0.031 nT
 Dynamics range:                      +-16384 nT
 Conversion:                       7 * 20Bit ADC
 Temperature Range:
                    operating:   -160 ... +120deg C
                non-operating:   -180 ... +150deg C
 
 
 
Flight Unit Components
======================
 DPU:            FS
 IB-Sensor:      FM
 OB-Sensor:      FM
 
 
 
Major Operational Constraints
=============================
 
+ RPC-MAG has to be operational as long as power is available
+ RPC-MAG has a joint operational requirement with ROMAP, especially
  during the lander descent.
+ RPC-MAG has a requirement on Spacecraft Magnetic Cleanliness of 25nT
  at the OB sensor. According to the performed continuous magnetic
  mappings of all units and s/c magnetic system modelling the expected
  magnetic field at the OB sensor is about 45nT (without boom motor
  field).
+ MAG will see some stray fields from other units like: Reaction
  Wheels, Solar Panel Motor and Thruster firing. This needs to be
  monitored during flight, especially during switch on procedures, for
  purposes of inflight calibration.
 
 
History of the Instrument - Design Changes
==========================================
 
The magnetometer experiment came on board of ROSETTA in a very late
phase of the project. For this reason the mechanical (mass) and
electrical requirements (power) were extremely stringent: mass below
1kg, power below 1W! In addition the project mass budget went negative
after few months so that the project had to run general descoping
actions to reduce mass. The first mass reduction action did not safe
enough mass, so a second run had to be made. This led to severe
descopings on the magnetometer sensors and electronics whose mass was
already in the margin of the other experiments:
Actions:
 + reduce size and mass of sensor,
 + integrate small micro-D connector into sensor:
   as a result the MAG sensors are extremely small and have low mass
   of 36g ! But due to this no access to tune the inner ring-cores for
   low offset was possible anymore.
 + The electronics board was reduced by 30% in size (from 1.5 boards
   to 1 board only) and down to 1.5mm thickness of the big multilayer
   board by higher integration. Connectors had to be changed from
   cannon-D to micro-D. The higher integration and size reduction was
   reached by new very dense layout and deletion of offset temperature
   compensation circuit for all 6 sensor-axes !
 
This mass saving action later on during qualification (vibration of
RPC-0) resulted in a dramatic failure of the MAG board where both
ASICS (128 pins)lost several pins due to very high resonance peaks of
the multilayer board. The rework and redesign took several weeks and
could only be solved by increasing the stiffness of the board by
adding (gluing) additional stiffeners on top and bottom side of the
board thus adding several 100g of mass.
 
Comment: at this stage of the project the launcher has changed from
         ARIANE 4 to 5 giving more mass for ROSETTA.
 
 
 
 
FGM  Location
=============
 
Sensors : on Boom 1.5 m away from s/c to minimize s/c generated
          noise/disturbances.
          Distance  between Sensors : 15 cm
          2 sensors for redundancy and to eliminate residual noise
          from  s/c.
Electronics: inside s/c in RPC-0 Box, common box for ALL RPC
             electronics.
 
 
 
MAG Sensor - History
====================
The prototype of the ROSETTA FGM-sensors have been successfully flown
onboard the DS-1 s/c.
 
Design Changes:
Due to the extreme boom temperature it became necessary to change
the MAG sensors baseplate from isolating Glassfibre to Carbonfibre
which has a much better thermal conductivity in order to get rid of
the internal 25mW drive power for each sensor. Without this change,
each sensor would heat up much higher then expected.
 
 
 
MAG Sensor: Characteristics
===========================
 
Excitation Coil: 1 layer CuL, completely wounded on  ring core
                 Core material: Permalloy (Fe19Ni81)
 
Pickup Coil:     2*129 windings in 6 layers, 0.112 mm - High Temp. CuL
                 Bobbin: Macor
                         + glass ceramic
                         + Ease of machining
                         + maximum use temperature 800 deg C.
                         + low thermal conductivity (1.46W/mK)
                         + high temperature insulator (0.79kJ/kgK)
                         + excellent electrical insulator
                           (>10^16 Ohm/cm)
                         + zero porosity (0%)
                         + no outgassing in ultra high vacuum
                         + strong and rigid
                         + Coefficient of expansion:  7.4 x 10^-6/K
 
Housing:       Lexan
               + Polycarbonate
               + Excellent impact strength
               + Good weatherability
               + Ease of machining
               + Thermoformability
               + UV resisting
               + flame retardancy
               + light transmittance 86 %
               + high thermal insulation
 
 
 
MAG Sensor: Features
====================
Sensor body consists of MACOR which has a smaller thermal Coefficient
of expansion (7.4 x 10^-6/K) in comparison to the Copperwire
(17  x 10^-6/K) of the windings.
 
As the copperwires are wound so tight on the MACOR body, the thermal
Expansion of the copper does not play a role any more.
 
Both sensors are equipped with a temperature sensor PT1000 inside the
housing to measure the sensor temperature.
 
 
A/D Converter CS5508 and Radiation Hardness
===========================================
The ADC Crystal CS5508 was chosen by the Space Research Institute in
Graz because of its good performance characteristics:
+ 20-Bits
+ very low power 3.72 mW
+ on chip self-calibration circuitry
+ extended temperature range.
 
The radiation behavior of the ADC was unknown. IWF Graz bought a
special lot of this component and performed tests by using the
facilities at ESTEC to determine the amount of radiation the converter
could withstand and still remain within specification.
 
The CS 5508 total dose tolerance was found to be 27 krad. The
devices showed high susceptibility to the Single Event Upset (SEU) as
well as to the Single Event Latch-up (SEL). Additional Tantalum Metal
Sheet (0.5mm) was used to shield the ADCs against irradiation during
the mission period!
 
(comment: Tantalum is used because only mass saves from total dose
          radiation, Tantalum has a specific density of  16.6g/cm^3!.
          It must be mentioned that the glue of heavy Tantalum shields
          on top of each ADC chip causes additional stress on the chip
          pins during vibration, therefore the Tantalum spot shield
          is also glued to the board on each small side.)
 
For detailed information refer to the document:
RADIATIONHARDNESS TEST OF 20-bit CS5508 ADC CONVERTER, for RPC
MAG/ROSETTA, Diploma Thesis, Amira Omerbegovic, F755 9530008
TU Graz, November 1999.
 
 
RPCMAG Frequency Plan
=====================
 
RPCMAG needs 3 different frequencies which can all be derived from a
single 4.194304 MHz oscillator by appropriate division within
the FPGA:
 
FGM:  excitation signal 50 kHz & 12.5 kHz
      4.194304 MHz / 84  = 49.93219 kHz  => 12.63345 kHz
      The division is achieved by 84 = 26 +24 + 22
 
ADC:  drive frequency 32.768 kHz
      4.194304 MHz / 128  = 33.768 kHz
 
Device clock for  1355 transceiver PIU I/f: 400 kHz +- 10%
      4.194304 MHz / 10 = 419.439 kHz
 
 
 
Assumptions: Environmental
==========================
 
+ Power supply:
        Supply Voltage provided by PIU has to be stabilized within a
        1% range
 
+ Temperature:
        Temperature changes are taken into account  by the calibration
 
+ Radiation :
        The ADCs are shielded by Tantalum plates (thickness: 0.5 mm)
    Single Event Upsets (SEU)
        These effects cause bitflips in memories, it can be protected
        by failure correction algorithms (Hamming code) or redundancy.
        For MAG an SEU event is uncritical because of full redundancy
        and because a bitflip will cause the loss of one or few
        vectors which can be tolerated.
 
    Single Event Latch Up protection (SEL).
        It was decided by the RPC team to have the latch up protection
        (due to shortage and therefore overcurrent in some circuitry).
        The circuitry is built from SEL immune parts in the central
        RPC power unit, which in case of an SEL measures the
        overcurrent (LCL) and turns off RPC within msec. Restart has
        to be commanded.
 
 
Assumptions: Contingencies
==========================
Critical parts:
 
   + Every component has to be alive for a successful operation of the
     FGM
   + The ADCs are shielded by Tantalum plates
   + PCB located in RPC-0 for shielding
   + LCL protects electronics against short-circuits (located in PIU)
 
Possible MAG problems during flight are covered by the RPC-0 FMECA
(Failure Mode Effectiveness and Criticality Analysis)
 
 
 
Assumptions: Redundancies
=========================
 
  + 2 sensors
  + No redundancy for electronics
 
 
 
Design Margins
==============
 
The electronics design margins are standard workmanship questions for
space application. Applicable to each part, especially capacitors.The
design, therefore has been made according to ESA Standards as
described in their documentation.
 
Critical parts are the:
 + ADC  CS5508 wrt. Radiation (see above)
 + MAX 400 Op Amp which is not on the preferred parts list of  ESA or
   NASA, because it is not qualified yet. However, this part is used
   in commercial industry since years in great numbers and thus
   showing and demonstrating the quality level and reliability.
 
 
 
Operations
===========
 
The RPCMAG instrument has only two intrinsic modes:
 
 + ON
 + OFF
 
 
After power on reset, the MAG instrument calibrates itself
and starts to send continuously 20 Hz Magnetic field (B) and
Housekeeping (HK) Data.
Filtering is done in the PIU.
 
 
MAG Instrument Software
=======================
 
MAG software runs in a radiation hard 1280 FPGA! Detailed description
of the ACTEL FPGA software can be found in the following document:
 
 The building and operation of the MAG_FPGA in the Fluxgate
 Magnetometer Electronics.
 
RPCMAG has no individual s/w. It has only the capability to be
switched on/off and later it runs in continuous 20 Hz sampling mode.
Calibration of the ADCs once in every 24 hour. It only samples and
sends 20 Hz data (6 vectors + 1 HK). All other operation is done in
PIU-S/W.
 
 
A RPCMAG Data Acquisition Cycle :
 
Using a crystal oscillator the MAG FPGA sends a 'StartConvert' signal
(CONV)to the ADCs at a certain time. After all ADCs have been finished
the conversion (RDY Signal) the data will be read and transmitted to
the Link FPGA. As the 20 Hz of the MAG unit is slightly different from
the 20 Hz at the s/c there will be not an integral number of vectors
in an RPC AQP. Therefore, the CONV signal is passed  to the Link chip
(CONV1) to send a signal to the PIU. PIU will then generate a high res
time stamp for the first vector of the packet. The accuracy is better
then 1ms +- 100 us.
 
 
MAG  Software in PIU
====================
PIU is just an observer. It has no control of what MAG is doing. The
MAG S/W in the PIU has the task to
 + synchronize itself with the MAGs internal conversion signal
 + sample all 20 Hz Mag data without any loose and store on board time
   for the first value of the packet
 + prepare science and HK packets for transmission
 + filter the 20 Hz data to an appropriate mean value and set MAG to
   the right SID
 + switch the desired sensor to be primary
 + handle FCPs for MAG
 + provide HK values, measured by the MAG ADC, for  PIU, MAG, MIP
 
 
 
Mode description:
=================
 
MODE               SAMPLE   PACKET    PACKET      VECTOR
                   RATE     PERIOD    LENGTH      RATE
 
Minimum Mode SID1  1/32 Hz  1024 s    32 Pri Vec   0.03125 vec/s
                                       1 Sec Vec  0.000976 vec/s
Normal Mode  SID2     1 Hz    32 s    32 Pri Vec         1 vec/s
                                       1 Sec Vec   0.03125 vec/s
Burst  Mode  SID3    20 Hz    16 s   320 Pri Vec        20 vec/s
                                      16 Sec Vec         1 vec/s
Medium Mode  SID4     5 Hz    32 s   160 Pri Vec         5 vec/s
                                       1 Sec Vec   0.03125 vec/s
Low Mode     SID5  0.25 Hz   128 s    32 Pri Vec      0.25 vec/s
                                       1 Sec Vec  0.007812 vec/s
Test Mode    SID6    20 Hz    16 s   320 Pri Vec        20 vec/s
                                       1 Sec Vec    0.0625 vec/s
HK Mode                       32 s       8 words   0.03125 vec/s
 
 
Filter S/W
===========
 
Burst data (SID3) pass the s/w unfiltered.
Data of all other modes will be filtered in a multi stage process.
Each stage filters and decimates the data in time.
The data fields in the HK packet
        filtercfg
        stageAId
        stageBId
control the filter mode.
 
 
MODE          SAMPLE           FILTER IDs           SAMPLES PER PACKET
              RATE      STAGE 1  STAGE 2  STAGE 3   PRIMARY  SECONDARY
Minimum SID1  1/32 Hz    4        3        3         32         1
 
Normal  SID2     1 Hz    1        2        off       32         1
 
Burst   SID3    20 Hz    off      off      off       320        16
 
Medium  SID4     5 Hz    2        off      off       160        1
 
Low     SID5  0.25 Hz    4        3        off       32         1
 
Test    SID6    20 Hz    TC def.  off      off       320        1
 
 
 
Time Stamps of  Data Packets
============================
 
Due to this complex filtering process the time stamps of the measured
data are different for each mode. Each vector coming out of the PIU
gets a specific time stamp according to the actual mode. These time
stamps are shifted towards the real time of the physical event. The
time stamps of the data lie BEFORE the real measurement time. This
time displacement for the  PRIMARY vectors in  different modes is
listed in the following table:
 
MODE          SAMPLE RATE    TIME SHIFT (PRIMARY VECTORS)
Minimum SID1  1/32 Hz        223.7  s
Normal  SID2     1 Hz          8.2  s
Burst   SID3    20 Hz          0    s
Medium  SID4     5 Hz          1.35 s
Low     SID5  0.25 Hz         27.7  s
 
Thus, the true time of the physical event is achieved by adding the
listed time shift to the time stamp of the vector.
 
For the SECONDARY vectors a different time stamping applies. As the
SECONDARY vectors are not filtered but just picked out of the data
stream. Thus, the first SECONDARY vector of a packet is stamped with
the time of the end of the data  packet. Therefore, the following
shifts have to be taken into account:
 
 
MODE          SAMPLE RATE    TIME SHIFT (SECONDARY VECTORS)
Minimum SID1  1/1024 Hz       1023.95 s
Normal  SID2    1/32 Hz         31.95 s
Burst   SID3       1 Hz         15.95 s
Medium  SID4    1/32 Hz         31.95 s
Low     SID5   1/128 Hz        127.95 s
 
 
The archive data in the datasets labeled with V1.0 use the original
times tamps. For later datasets labeled V2.0 and above the time stamps
of the PRIMARY vectors have been corrected by the archive generation
software. The SECONDARY vector time stamps, however,  stay always as
they were originally transmitted in the telemetry.
 
 
Sensors extreme Temperature Tests
=================================
 
The MAG sensors on the boom will see extreme Temperatures from
-200 deg C to +150 deg C. This Temperature range for the sensors could
only be tested in the Cryo-Mumetal chamber of Garchy (France), where
the Magnetic field is completely shielded by Mumetal. A non Magnetic
Test Table inside can be cooled by liquid Nitrogen to -191 deg C. This
test was performed successfully with all sensors in January 2001. The
extreme temperature range was predicted for comet Wirtanen orbit, a
new prediction for the CG target does will probably be similar. In
Magnetsrode the positive temperature range was tested & calibrated up
to +75 deg C. However, it is impossible to test the sensors in non
magnetic environment and thermal Vacuum, no facility for this exists
worldwide.
 
 
EMC Test
========
 
The magnetic field is more or less distorted by the following s/c
units:
 
  Reaction wheels
  Solar Arrays (<0.5 nT)
  SADM (23 nT)
  Lander
  Thrusters (compensated)
 
 
 
 
Calibration
===========
 
The magnetometer has been calibrated on ground in the magnetic coil
facility MAGNETSRODE at Braunschweig, Germany. This facility is
operated by the Institute of Geophysics and extraterrestrial Physics.
 
The complete calibration is documented in the following documents:
 
  Report:                             RO-IGM-TR-0002
  DC-Analysis:                        RO-IGM-TR-0003
  AC-Analysis:                        RO-IWF-TR-0001
 
  Step by Step Calibration Procedure: RO-IGEP-TR-00028
 
 
Nominal (uncalibrated) Conversion of Digital values
===================================================
1)Science Data: Magnetic field values (range = +-15000nT , 20 Bit):
 
  B_max  = +15000 nT
  B_min  = -15000 nT
  counts = 2^20  = 1048576
  Nominal_Factor = (B_max - B_min) / counts
 
  The binary values of the 20 bit ADC Output are in the range
  of 00000h : FFFFFh corresponding to decimal values of 0 : (counts-1)
  As the ADC is operated in bipolar mode the nominal relation between
  counts and magnetic field is as follows:
  00000h <->  B_min
  80000h <->  0
  FFFFFh <->  B_max
 
  The conversion routine from binary TM data to ASCII Rawdata converts
  the binary values to signed integers in the following way
  00000h -> -counts/2
  80000h ->  0
  FFFFFh -> +counts/2
  These signed integers in the range from -counts/2 to +counts/2 are
  the EDITED RAW DATA.Unit is [counts].
  To convert these into uncalibrated [engineering, enT] nanotesla
  values, the following   algorithm is applied:
 
      B= [ADCvalue + counts/2] *  Nominal_Factor  + B_min   [enT]
 
Also the Housekeeping Reference Voltage is monitored via a 20bit ADC
and converted in the same manor.
 
 
 
2)Housekeeping Data: Magnetic field values (range = +-15000nT, 16 bit)
 
  B_max  = +15000 nT
  B_min  = -15000 nT
  counts = 2^16  = 65536
  Nominal_Factor = (B_max - B_min) / counts
 
  The binary values of the 16 bit ADC Output are in the range
  of 0000h : FFFFh corresponding to decimal values of 0 : (counts-1)
  As the ADC is operated in bipolar mode the nominal relation between
  counts and magnetic field is as follows:
  0000h  <->  B_min
  8000h  <->  0
  FFFFh  <->  B_max
 
  The conversion routine from binary TM data to ASCII Rawdata converts
  the binary values to signed integers in the following way
  0000h -> -counts/2
  8000h ->  0
  FFFFh -> +counts/2
  These signed integers in the range from -counts/2 to +counts/2 are
  the EDITED RAW DATA.Unit is [counts].
  To convert these into uncalibrated [engineering, enT] nanotesla
  values, the following   algorithm is applied:
 
      B= [ADCvalue + counts/2] *  Nominal_Factor  + B_min   [enT]
 
 
 
 
3)Housekeeping Data: Voltages (range = +-5V, 16 bit)
 
  V_max  = +2.5 V
  V_min  = -2.5 V
  counts = 2^16  = 65536
  Nominal_Factor = (V_max - V_min) / counts
 
  The binary values of the 16 bit ADC Output are in the range
  of 0000h : FFFFh corresponding to decimal values of 0 : (counts-1)
  As the ADC is operated in bipolar mode the nominal relation between
  counts and magnetic field is as follows:
  0000h  <->  V_min
  8000h  <->  0
  FFFFh  <->  V_min
 
  The conversion routine from binary TM data to ASCII Rawdata converts
  the binary values to signed integers in the following way
  0000h -> -counts/2
  8000h ->  0
  FFFFh -> +counts/2
  These signed integers in the range from -counts/2 to +counts/2 are
  the EDITED RAW DATA.Unit is [counts].
  To convert these into voltages, the following algorithm is applied:
 
      U= [ADCvalue + counts/2] *  Nominal_Factor  + V_min   [V]
 
 
Also the nominal temperatures are computed from HK voltages in a
similar way
Some voltage are monitored as 8bit values; the conversion, however,
is done in the same way.
 
 
 
 
Magnetic Cleanliness
====================
Details can be found in
IABG: B-TR40-0555
RO-IGM-SR-0003
 
 
Output data
===========
 
FGM output is:
 + Time series of 3 B-Field vectors from the IB-Sensor
 + Time series of the IB-Sensor Temperature
 + Time series of 3 B-Field vectors from the OB-Sensor
 + Time series of the OB-Sensor Temperature
 + Additional HK values for PIU & MIP
 
 
 
The RPC MAG-CREW
================
PI:          Glassmeier, Karl-Heinz, IGEP,TU-BS
TM:          Richter, Ingo, IGEP, TU-BS
 
Research
Assistant:   Diedrich, Andrea,IGEP, TU-BS, died in 2007
 
Instrument
Development: Kuhnke, Falko,TU-BS              (electronics & sensor)
             Musmann,Guenter,TU-BS            (sensor)
             Stoll, Bernd, IGEP,TU-BS         (electronics & sensor)
             Co. Pfeil/Trawid, Hildesheim     (sensor)
             Aydogar,Oezer,IWF,TU-GRAZ        (electronics)
Conversion
Software
Development  Hans Eichelberger, IWF,TU-Graz
 
 
Co-Is:  Auster, Hans-Ulrich, IGEP,TU-BS  (PI of the ROMAP FGM)
        Balogh, Andre, IC, London
        Coates, Andrew J., MSSL
        Cowley, S.W.H., Univ. Leicester (science planning & analysis)
        Flammer, K., UCSD               (science planning & analysis)
        Gombosi, Tamas,Univ.of Michigan (cometary science support)
        Horanyi, M.,Univ. of Colorado   (plasma-dust interact.)
        Jockers, Klaus, MPS Lindau      (ground based observations)
        Kuerth, Eckehard, DLR, Berlin   (comet. nucleus physics)
        Ip, W.-I., MPS, Lindau          (Science)
        Mehlem, Klaus, ESTEC            (magnetic cleanliness)
        Motschmann, Uwe,ITP, TU-BS      (science planning & analysis)
        Musmann, Guenter, IGEP, TU-BS   (ex RPC-TM)
        Neubauer, Fritz, Univ. Cologne) (overall science support)
        Richter, Ingo, IGEP, TU-BS      (MAG TM, calibration,analysis)
        Rustenbach, Juergen, MPE-Berlin,(Co-I of ROMAP FGM)
        Sauer, Konrad, MPE-Berlin       (theory and simulation)
        Schwingenschuh, Konrad, IWF-Graz(magn. cleanl.,science)
        Szegoe, K.,RMKI-KFKI,Budapest
        Tsurutani, Bruce, JPL, Pasadena  (science planning & analysis)
        Zang, Gary,Bart.Res.Inst,Delaware(science planning & analysis)
 
 
 
 
Acronyms
========
ADC:       Analog-Digital-Converter
AQP:       Acquisition Period
ASIC:      Application Specific Integrated Circuit
B-FIELD:   Magnetic Field
CG:        67P/Churyumov-Gerasimenko
CO-I:      Co-Investigator
CuL:       Kupferlackdraht, Enamelled copper wire
DDS:       Data Distribution System
DPU:       Digital Processing Unit
DS-1:      NASA's Deepspace 1 Mission
EAICD:     Experimenter  to  Archive Interface Control Document
EID-B:     Experiment Interface Document , Part B
EMC:       Electromagnetic Compatibility
ESA:       European Space Agency
ESTEC:     European Space Research and Technology Centre
FGM:       Fluxgate-Magnetometer
FM:        Flight Model
FMECA:     Failure Mode Effects and Criticality Analysis
FPGA:      Field programmable Gate Array
FCP:       Flight Control Procedure
FS:        Flight Spare Model
HK:        Housekeeping data (Supply voltages, Ref. voltages,
           Temperatures)
H/W:       Hardware
IABG:      Industrieanlagenbetriebsgesellschaft
IB:        Inboard Sensor
ID:        Identifier
I/F:       Interface
IGEP:      Institut fuer Geophysik und extraterrestrische Physik,
           TU-Braunschweig
IWF:       Institut fuer Weltraumforschung,Graz
LCL:       Latching Current Limiter
LEXAN:     Polycarbonate resin thermoplastic
MACOR:     Machinable glas ceramic
MAG:       Magnetometer
MIP:       RPC Mutual Impedance Probe
NASA:      National Aeronautics and Space Administration
OB:        Outboard Sensor
OPAMP:     Operational Amplifier
PCB:       Printed Circuit Board
PDS:       Planetary Data System
PERMALLOY: Nickel Iron magnetic alloy
PI:        Principal Investigator
PIU:       RPC Power Interface Unit
PSA:       Planetary Science Archive
PT1000:    Platinum Thermistor with 1000 Ohm nominal resistance
RAW:       Data in units of ADC counts in instrument coordinates
ROKSY:     ROSETTA Knowledge Management System
ROMAP:     ROSETTA Lander Magnetometer
RPC:       ROSETTA Plasma Consortium
RPCMAG:    ROSETTA Orbiter Magnetometer
RPC-MAG:   ROSETTA Orbiter Magnetometer
RPC-0:     RPC Main Electronics Box
SADM:      Solar Array Drive Mechanism
S/C:       Spacecraft
SID:       Science Mode Identifier
S/W:       Software
SEU:       Single Event Upset
SEL:       Single Event Latch-up
TC:        Telecommand
TM:        Telemetry
TM:        Technical Manager
TS:        Time Series
UV:        Ultraviolet
us:        microsecond
Wrt.:      with respect to
 
 
 
 
 
References
==========
 
 
Alfven H 1957, On the theory of comet tails, Tellus, 9, 92-96.
 
Biermann L 1951, Kometenschweife und solare Korpuskularstrahlung,
 Zeitschrift fuer Astrophysik, Vol. 29, p.274
 
Coates A J, Jonstone A D, Wilken B, and  Neubauer F M, 1993, Velocity
 Space Diffusion and Nongyrotropy of pickup Water Group Ions at Comet
 Grigg-Skjellerup,Journal of Geophysical Research 98, No. A12,
 20985-20994, 1993.
 
Eichelberger H U , Schwingenschuh K, Aydogar Oe, Baumjohann W, 2002,
 Calibration Report RO-IWF-TR0001, Sample Rate and Frequency Response
 Analysis of ROSETTA RPC-MAG, IWF, January 2002
 
Glassmeier K H, Neubauer F M, 1993, Low-Frequency Electromagnetic
 Plasma Waves, Comet P/Grigg-Skjellerup: Overview and Spectral
 Characteristics, Journal of Geophysical Research 98, No. A12,
 20921-20935, 1993
 
Glassmeier K H, Motschmann U, Mazelle C, Neubauer F M, Sauer K,
 Fuselier S A, Acuna M H, 1993 Mirror Modes and Fast Magnetoacoustic
 Waves Near the Magnetic Pileup Boundary of Comet P/Halley, Journal of
 Geophysical Research 98, No. A12, 20955-20964, 1993
 
 
Glassmeier K.-H., Richter I., Diedrich A., Musmann G., Auster U.,
 Motschmann U., Balogh A., Carr C., Cupido E., Coates A., Rother M.,
 Schwingenschuh K., Szegoe K., Tsurutani B.,
 RPC-MAG The Fluxgate Magnetometer in the ROSETTA Plasma Consortium,
 Space Science Reviews, 2007
 
Hedgecock P C 1975, A correlation technique for magnetometer zero
 level determination, Space Sci. Instr., 1, 83.
 
 
Huddleston  D E, Coates A J, Jonstone A D, Neubauer F M,1993, Mass
 Loading and Velocity Diffusion Models Heavy Pickup Ions at Comet
 Grigg-Skjellerup, Journal of Geophysical Research 98, No. A12,
 20995-21002, 1993
 
Johnstone  A D, Coates A J, Huddleston D E, Jockers K, Wilken B,
 Borg H, Gurglio C, Winningham J D, Amata E, 1993, Observations of the
 solar wind and cometary ions during the encounter between Giotto and
 comet P/Grigg-Skjellerup, Astronomy and Astrophysics, 272, L1-4, 1993
 
Motschmann U, Glassmeier K H,1993, Nongyrotropic Distribution of
 Pickup Ions at Comet P/Grigg-Skjellerup: A Possible Source of Wave
 Activity, Journal of Geophysical Research 98,No. A12,20977-20983,1993
 
 
Neubauer F M 1981, The Giotto Magnetometer Experiment, ESA SP-169.4
 
Neubauer F M, Musmann G, Acuna M H, Burlaga L F, Ness N F, Mariani F,
 Wallis M, Ungstrup E, Schmidt H 1983, The Giotto magnetic field
 investigation. In: Cometary Exploration, Proc. Int. Conf. Cometary
 Exploration, 15-19 November 1982, Budapest (Ed. Gombosi T I) 401-410.
 
Neubauer F M , Marschall H, Pohl M, Glassmeier K H, Musmann G,
 Mariani F, Acuna M H, Burlaga L F, Ness N F, Wallis M K, Schmidt H U,
 Ungstrup E,1993 First Results from the Giotto magnetometer experiment
 during the P/Grigg-Skjellerup encounter, Astronomy and Astrophysics,
 268, L5-8, 1993
 
Neubauer F M, Glassmeier K H, Coates A J, Johnstone A D, 1993,
 Low-Frequency Electromagnetic Plasma Waves at Comet Grigg-Skjellerup:
 Analysis and Interpretation, Journal of Geophysical Research 98,
 No. A12, 20937-20953, 1993
 
Neuhaus A, 2001, RO-IGM-SR-003, Study on the DC magnetic Requirements,
 System Report, Institut fuer Geophysik und Meteorologie, 2001
 
Omerbegovic A, 1999, Radiationhardness test of 20-bit CS5508 ADC
 Converter for RPC MAG/ROSETTA, Diploma Thesis, F755 9530008, TU Graz,
 November 1999
 
Othmer C, Richter I,2001, RO-IGM-TR-0003, Fluxgate Magnetometer
 Calibration for Rosetta:Analysis of the FM Calibration, Institut fuer
 Geophysik und Meteorologie, Braunschweig, Oktober 2001
 
Richter I, Rahm M.,2001, RO-IGM-TR-0002, Fluxgate Magnetometer
 Calibration for Rosetta: Report on the FM and  FS Calibration,
 Institut fuer Geophysik und Meteorologie, Braunschweig, Oktober 2001
 
Richter I, Cupido E., 2003, RO-RPC-UM, Rosetta Plasma Consortium:
 User's Manual,Institut fuer Geophysik und Meteorologie, Braunschweig,
 December 2003
 
Schmidt H U & Wegmann R 1982, Plama flow and magnetic field in comets.
 In: Comets (Ed. Wilkening L L) University of Arizona Press, 538-560.
 
Sulivan J,2001, The building and operation of the MAG_FPGA in the
 Fluxgate Magnetometer Electronics, KFKI RMKI,Budapset, 2001
 
Tsurutani B T, Smith E, 1986, Hydromagnetic waves and instabilities
 associated with cometary ion pickup: ICE observations turbulence
 associated with comet Giacobini Zinner,GRL,13,1986
 
Wallis M K 1973, Weakly shocked flows of the solar wind plasma through
 atmospheres of comets and planets, Planet. Space Sci., 21, 1647-1660.
 
Winske D, Wu C S, Li Y Y, Mou Z Z & Guo S Y 1985, Coupling of newborn
ions to the solar wind by electromagnetic instabilities and their
interaction with the bow shock, J. Geophys. Res., 90, 2713-2726.
 
Wu C S, Davidson R C, 1972,Electromagnetic Instabilities produced by
 Neutral-Particle Ionization in Interplanetary Space,
 J.Geophys.Res. 77, 5399,1972

        