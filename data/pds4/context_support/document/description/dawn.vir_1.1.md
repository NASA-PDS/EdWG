
 
Instrument Overview
===================
VIR is an imaging spectrometer having moderate spectral resolution
that combines two data channels in one instrument. The two data
channels, Visible (spectral range 0.25-1 micron) and Infrared
(spectral range 0.95-5 micron), are committed to spectral mapping
and are housed in the same optical subsystem. The instrument is
composed by the Optics Module (OM), the  Proximity Electronic box
(PEM), housed inside the Optics Module, and the Main Electronic
box (ME). The proximity electronic box (PEM) contains all
the electronics needed to interface the Main Electronics,
to drive the FPAs, the scan mirror and the cover mechanism and to
perform the acquisition and conversion of the science and
housekeeping data. The Main Electronics manages the
operation of the two channels, gathers data and housekeeping
information, stores the data, performs data compression, controls
the cryo-cooler and interfaces the instrument with the S/C.
A complete description of the instrument and its performance
can be found in [BINIETAL2005].
 
Technical Description
=====================
The optical concept is inherited from the visible channel of the
Cassini Visible Infrared Mapping Spectrometer (VIMS-V) and from
the Rosetta Visible InfraRed Thermal Imaging Spectrometer(VIRTIS).
This concept matches a Shafer telescope to an Offner grating
spectrometer to disperse a line image across two FPAs.
The optical subsystem is housed inside the Cold Box of the Optics
Module. The spectrometer has the ability to point and scan along
the direction perpendicular to the slit.
VIR can be divided in three modules:
the Optical Head, the Proximity Electronics Module and the Main
Electronics.
 
VIR OPTICAL HEAD
----------------
The Optical Head contains the following items:
  - telescope optical components, mountings and optical bench,
    and scan unit
  - spectrometer optical components, mountings and housing
  - internal calibration system
  - slit and shutter mechanism
  - visible detector assembly
  - infrared detector assembly
  - external and internal baffles
  - cover unit
  - radiators
The VIR optical system is a Shafer telescope matched through a slit
to an Offner grating spectrometer. The Shafer consists of 5 mirrors
mounted on an aluminum optical bench. The primary mirror is
a scanning Beryllium mirror driven by a torque motor.
The bench is machined from a single aluminum alloy billet and acts
both  as a cold plate and optical support structure, mounted on the
ledge of the Cold Box.
The Offner spectrometer consists of a mirror and a spherical convex
diffraction grating housed in an aluminum structure that is flange
mounted to the telescope.
 
PROXIMITY ELECTRONICS
---------------------
The Proximity Electronics consists of the following items:
  - box structure
  - mother board and connectors
  - CCD boards
  - IR board
  - scan mirror and cover board
 
MAIN ELECTRONICS DESCRIPTION
----------------------------
The ME is physically separated from the Optics Module. It consists of
the Digital Processing Units (DPUs), the S/C interface control units,
the power supply for all the sub-units of the instrument excluding
the cryocooler, the interface units and the coolers electronics. The
DPU, S/C interfaces, instrument interfaces are also called DHSU
(Data Handling and Support Unit).
The VIR sub-systems (PEM, coolers, covers and scan mirror) are
switched on/off by means of the Power Distribution Unit (PDU) of the
ME/power supply unit, controlled by the DHSU. The main tasks
of the DHSU are:
  - acquire, pre-process, compress and format the science and
    calibration data
  - control and power switch the sub-systems, the coolers and the
    Covers
  - health check the instrument and provide the operational status
    of VIR to the S/C
  - execute uplink and downlink activities to and from VIR
  - interpretate and execute the telecommands
  - manage and synchrone the activities between VIR and the S/C
  - store the science data in the instrument Mass Memory
    (2 Gbit), before downloading to the S/C solid state recorder.
 
Scientific objectives
=====================
A Multispectral Imager - covering the range from the near UV
(0.25 micron) to the near IR (5.0 micron) and having moderate to high
spectral resolution and imaging capabilities - is an appropriate
instrument for the determination of global (size, shape, albedo,
etc.), and local (mineralogical features, topography, roughness, dust
and gas production rates, etc.) properties of Vesta and Ceres.
The primary scientific objectives of VIR during the Dawn mission are:
  - to study the mineralogy of Vesta and Ceres, and their environment
  - to determine the nature of rock-forming minerals and their
    relative abundances
  - to measure the temperature of their surfaces
  - to generate physiographic maps of the surfaces
Secondary objectives are:
  - provide synthetic maps of the surface
  - merge data from different instruments through data fusion
    Techniques
  - identify gaseous species emitted by the surface and physical
    Condition of the exosphere- if any.
 
Calibration measurements
========================
Before the integration of the VIR experiment on the DAWN spacecraft
a full calibration of the instrument has been performed to completely
characterize the instrumental performances.
The fundamental calibrations necessary to correctly retrieve the
scientific information from VIR data are:
  1- Geometric calibration: measurement of IFOV, FOV and in field
     distorsions;
  2- Spectral calibration: correlation between spectral dispersion
     axis of the focal planes with wavelength;
  3- Spatial calibration: evaluation of the flat-field matrices
     necessary to homogenize the focal planes responses;
  4- Radiometric calibration: determination of the Instrument
     Transfer Function (ITF), that allows to convert digital numbers
     (DN) in physical units of spectral radiance
     (W m-2 micron-1 sterad-1).
These quantities, continuously checked during the flight at each
switch on of the experiment, are used in the data pipeline before
the scientific analysis.
 
Principal Investigator
======================
Maria Cristina De Sanctis
Istituto Nazionale di Astrofisica, Rome
 
References
==========
 - C.T. Russell et al., 'Dawn Mission to Vesta and Ceres', Earth,
   Moon and Planets 101, 65-91, 2007
 
 - M.C. De Sanctis, et al., 'The VIR Spectrometer', Space Sci Rev,
   doi:10.1007/s11214-010-9668-5, 2010

        