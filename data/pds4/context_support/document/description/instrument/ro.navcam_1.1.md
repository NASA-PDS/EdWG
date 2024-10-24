
 
======================================================================
Instrument Overview:
======================================================================
 
The ROSETTA Navigation Camera (NavCam) is a part of the ROSETTA
Attitude and Orbital Control System (AOCS).  It comprises of two
identical cameras to provide for complete redundancy and Sinle Event
Upset (SEU).  The purpose of the NavCam system is to provide Imaging,
Autonomous Acquisition and Tracking of Star-fields and Extended
Sources, and Autonomous Navigation for the ROSETTA S/C.
 
======================================================================
Objectives of the NavCam:
======================================================================
 
- Autonomous Acquisition and Tracking of Point Targets
- Autonomous Acquisition and Tracking of Extended Sources
- Imaging of Star-fields and Extended Sources
- Determine Coarse and Fine Attitude Corrections
 
======================================================================
The ROSETTA NavCam Instrument:
======================================================================
 
Two identical units each with:
 
+ Camera Optical Head (CAM-OH)
     - Active Pixel Sensor (APS) CCD with pixel angular size of 17
       arcsec.
     - Proximity Electronics:
         + CCD drivers
         + CCD bias a phase voltage regulators
         + Analogue Signal Processor
         + two Multiplexers
         + 12-bit monolithic 1.25 Mobilisation Station and Planning
           System (MSPS) Analogue-Digital Converter (ADC).
         + Interfaces for temperature control and cover mechanism
     - Timing Sequencer and Control Logic
         + CCD sequencer and analogue channel control
         + Data interface
     - Digital Signals and Power Interface
 
+ Camera Electronics Unit (CAM-OH)
     - Digital Signal Processing (DSP) Board with NavCam processor
       and other related interfaces
         + the DSP itself
         + Memory Banks
         + DSP Peripherals
         + Interfacing between the Avionics Interface Unit (AIU),
           SSMM and the Optical head (OH)
         + Insturment control function
 
+ Camera Baffle (CAM-BAF)
     - mechanism to reduce reflected light reaching the sensor.
 
======================================================================
NavCam Classification:
======================================================================
 
+ Navigation Camera (NavCam) / Autonomous Attitude Star Tracker (STR)
+ Low power consumption (16.8 W Total)
+ Compact unit
+ Qualified for space application
 
======================================================================
NavCam Characteristics:
======================================================================
 
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 |     Parameter        |    Value    |           Comment            |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Mass (OH)            |   6.05 kg   |                              |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Mass (EU)            |   2.70 kg   |                              |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Mass (BAF)           |  1.408 kg   |                              |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Total Mass           |  10.158 kg  |                              |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Total Power          |   16.8 W    |                              |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Field of View        |    5 deg    | Circular FOV                 |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Sensor Format        |  CCD - APS  |                              |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Limit Magnitude      |   Mv = 11   | Exp. Time 7 s, SNR >= 5      |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Saturation Magnitude |  Mv = 1.6   | Whole spectral range.        |
 |                      |  Mv = 0.8   | G2 Class.                    |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Attenuation control  |     517     |                              |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Integration Time     |    10 ms    | Minimum                      |
 |                      |    30 s     | Maximum                      |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Bias Error (1 sigma) | 0.185 pxls  | Mv = 11, exp. time = 7 s,    |
 |                      |             | Defocused mode               |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | NEA (1 sigma)        | 0.045 pxls  | Mv = 11, exp. time = 7 s,    |
 |                      |             | Defocused mode               |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | MTF                  |     0.3     | Focused, atten. inserted     |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Commanded Window Sz. |   20 x 20   | Minimum pixel array.         |
 |                      | 1024 x 1024 | Maximum pixel array.         |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | CCD Operative Temp.  | -50 deg C   | Minimum                      |
 | Range                | +50 deg C   | Maximum                      |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | CCD Performance      | -25 deg C   | Minimum                      |
 | Temperature Range    |   0 deg C   | Maximum                      |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 | Optics Temperature   | -60 deg C   | Minimum                      |
 | Range                | +60 deg C   | Maximum                      |
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 
 
======================================================================
Major Operational Constraints:
======================================================================
 
+ The NavCam must be in operation during all phases (except during
  Safe Mode).
+ The NavCam must have a minimum sun-avoidance angle of 65 degrees
  about boresight at a distance of 1 AU.
+ The NavCam must have a minimum sun-avoidance angle of 45 degrees
  about boresight at distances above 2 AU.
+ The NavCam in non-operational mode must have a minimum sun-
  avoidance angle of 20 degrees about boresight at distances of
  less than or equal to 1 AU.
+ The NavCam must be able to switched off by the AOCMS S/W in the
  event of entering into Safe Mode.
 
======================================================================
History of the Instrument:
======================================================================
 
The NavCam for the Rosetta mission was designed and built by Galileo
Avionica, building on a heritage of existing models, to satisfy the
requirements of the Rosetta Autonomous Navigation Component.
 
======================================================================
NavCam Locations:
======================================================================
 
Optics:       The NavCam optical heads are located on the +Z S/C axis
              with each protruding from the main body of the S/C.
 
Electronics:  The EUs for the NavCams are located on the Avionics
              power box, common for all AOCMS components.
 
======================================================================
A/D Converter:
======================================================================
 
The A/D converted housed within the CAM-OH Proximity Electronics is a
12-bit, monolithic, 1.25 Mobilisation Stationing and Planning System
(MSPS) architecture.
 
======================================================================
Operational Modes:
======================================================================
 
Each NavCam has seven different operational modes, however, only
data acquired under the IMAGING MODE will be present in the data
sets released and so only this mode shall be presented in any detail.
A point of note: IMAGING MODE can be operated under the other
available modes.
 
The MODE DESCRIPTION table below outlines the details of the
IMAGING MODE.
 
======================================================================
Mode Description:
======================================================================
 
IMAGING MODE:
 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|     SUB MODE      | FRAME RATE |   WINDOW SIZE  | INTEGRATION TIME |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| IDLE              |    1 s     |      N/A       |        N/A       |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| COVER POSITIONING |   0.8 s    |      N/A       |        N/A       |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| IMAGE ACQUISITION |    35 s    |   20 x 20 px   |       10 ms      |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| IMAGE ACQUISITION |    35 s    | 1024 x 1024 px |       30  s      |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 
The IDLE sub mode allows for the window size of the CCD to be set up
before the IMAGE ACQUISITION mode begins operation.  The sizes and
times shown here for the IMAGING MODE are the lowest and upper bounds
there are hundreds more possibilities for WINDOW SIZE, and hence read
out time, under this sub mode.
 
Generally the rule is that if a window size is one full row (1024 px)
spanned over one pixel then the readout time will be 4.1 ms, thus the
full window (1024 x 1024 px) will have a total readout time of 4.2 s
(including transfer time of 1.3 ms for the image to be received to
the Solid State Mass Memory (SSMM)).
 
======================================================================
Calibration:
======================================================================
 
This section is to be added once the calibration pipeline has been
written.

        