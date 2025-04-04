
 
########################################################################
########################################################################
REQUIRED READING:
- Stern et al.  (2007) [STERNETAL2007]
- SOC Instrument Interface Control Document (ICD)
########################################################################
########################################################################
 
      The ALICE description is adapted from Slater et al. (2007)
      [SLATERETAL2007] and Stern et al. (2005) [STERNETAL2005].
 
 
INSTRUMENT OVERVIEW
========
 
The New Horizons ALICE instrument is a lightweight (4.4 kg), low-power (4.4
Watt) imaging spectrograph aboard the New Horizons mission to Pluto/Charon
and the Kuiper Belt. Its primary job is to determine the relative abundances
of various species in Pluto's atmosphere. ALICE will also be used to search
for an atmosphere around Pluto's moon, Charon, as well as the Kuiper Belt
Objects (KBOs) that New Horizons hopes to fly by after Pluto-Charon, and it
will make UV surface reflectivity measurements of all of these bodies as
well. The instrument incorporates an off-axis telescope feeding a
Rowland-circle spectrograph with a 520-1870A spectral passband, a spectral
point spread function of 3-6A FWHM, and an instantaneous spatial
field-of-view that is 6 degrees long. Different input apertures that feed the
telescope allow for both airglow and solar occultation observations during
the mission. The focal plane detector is an imaging microchannel plate (MCP)
double delay-line detector with dual solar-blind opaque photocathodes (KBr
and CsI) and a focal surface that matches the instrument's 15-cm diameter
Rowland-circle.
 
SPECIFICATIONS
--------
 
NAME:                    ALICE
DESCRIPTION:             Ultraviolet Mapping Spectrograph
PRINCIPAL INVESTIGATOR:  Alan Stern, SwRI
WAVELENGTH RANGE:        520 - 1870 Angstrom
FIELD OF VIEW:           1.7 x 70 mRad (Note 1); 35 x 35 mRad (Note 2)
ANGULAR RESOLUTION:      1.7 x 5.2 mRad
WAVELENGTH OFFSET:       229.5+/-1.5 Angstrom at first pixel
WAVELENGTH RESOLUTION:   1.815+/-0.004 Angstrom/pixel
ACTIVE PIXELS:           ~780 pixels (Note 3)
 
Note 1:  Slit
Note 2:  Solar occultation aperture
Note 3:  Starting at an offset of 130 pixels from the first pixel
 
 
DESCRIPTION
--------
 
This ALICE is a lightweight (4.4 kg), low-power (4.4 W), ultraviolet
spectrograph based on the ALICE instrument now in flight aboard the European
Space Agency's Rosetta spacecraft. Its primary job will be to detect a
variety of important atomic and molecular species in Pluto's atmosphere, and
to determine their relative abundances so that a complete picture of Pluto's
atmospheric composition can be determined for the first time. ALICE will also
be used to search for an atmosphere around Pluto's moon, Charon, as well as
the Kuiper Belt Objects (KBOs) New Horizons hopes to fly by after
Pluto-Charon.
 
Light can enter the telescope section through either a 40mm x 40mm entrance
aperture (i.e. the airglow channel) or a stopped-down 1-mm diameter entrance
aperture and flat relay mirror (i.e. the SOC) and is collected and focused by
an off-axis paraboloidal (OAP) primary mirror onto the spectrograph entrance
slit. The OAP has a 120 mm focal length.
 
 
Scientific Objectives
========
 
Upper atmospheric temperature and pressure profiles of Pluto
 
Temperature and vertical temperature gradient should be measured to ~10% at a
vertical resolution of ~100 km for atmospheric densities greater than ~109
cm-3.
 
Search for atmospheric haze at a vertical resolution <5 km
 
Mole fractions of N2, CO, CH4 and Ar in Pluto's upper atmosphere.
 
Atmospheric escape rate from Pluto
 
Minor atmospheric species at Pluto
 
Search for an atmosphere of Charon
 
Constrain escape rate from upper atmospheric structure
 
 
Calibration
========
 
ALICE instrument calibration issues include the following:
 
- Dark count rate
 
- Spectral offsets i.e.  which wavelength is sampled by each pixel
 
- Spectral and spatial resolution and point-spread function
 
- Scattered light characteristics, including H Lyman-alpha
 
- Absolute effective area
 
See Stern et al. (2007) for details.
 
 
Operational Considerations
========
 
The New Horizons ALICE UV spectrometer was successfully launched on 19
January 2006 and is operating normally in space. All in flight performance
tests to date have shown performance within specification; the pointing and
AGC sensitivity tests completed in September 2006 are in analysis, and the
initial results of these tests indicate nominal performance. The primary
remaining tests to be performed will be testing of the solar occultation
aperture after it is opened near the end of 2006, and instrument mutual noise
susceptibility testing in the spring of 2007.
 
 
Detectors
========
 
The detector is a 2-D array of 1024 spectral pixels by 32 spatial pixels.
 
Although there are 1024 spectral pixel columns across the detector array,
only about 780 are active, starting at an offset of 130 columns from the
first spectral column.
 
See Stern et al. (2007) for details.
 
 
Electronics
========
 
Major electronic subsystems are
 
- Low-Voltage Power Supply Electronics.
 
- Command-and-Data-Handling Electronics.
 
- Decontamination Heaters.
 
- High Voltage Power Supplies.
 
See Stern et al. (2007) for details.
 
 
Optics
========
 
Summary information is above; see Stern et al. (2007) for details.
 
 
Operational Modes
========
 
Optics Aperture Modes
---------------------
Alice has two separate entrance apertures that feed light to the telescope
section of the instrument:  an 'airglow' aperture, which allows measurement
of emissions from atmospheric constituents, and an 'occultation' aperture,
when either the Sun or a bright star is viewed through the atmosphere
producing absorption by the atmospheric constituents. The Alice occultation
mode will be used just after New Horizons passes behind Pluto and looks back
at the Sun through Pluto's atmosphere.
 
Data Acquisition Modes
----------------------
P-ALICE has two detector data collection modes: (i) Pixel List Mode; (ii)
Histogram Imaging Mode.  The P-ALICE flight software controls both modes.
Data are collected in a dual-port acquisition memory that comprises two
separate 32kx16-bit memory channels.  In both modes, the instrument is turned
on and photons hitting a pixel on the detector, that result in analog pulses
above a set threshhold level, generate photon events that are then
transferred to the flight software.  Each photon event contains the pixel
location of the event.  The difference between the modes is in how the flight
software stores the photon events in the memory channels.
 
Pixel List Mode:  continuous 1-D stream of photon events and time hacks
-----------------------------------------------------------------------
In Pixel List Mode (PLM), the 2-D pixel array location of each single photon
event from the detector is transferred from ALICE to the spacecraft memory as
a stream of data; the data stream is also interspersed with timing
information (time hacks) that can be used to constrain the time of each
photon event.
 
In PLM, each ALICE memory channel acts as a linear data stream buffer:
while one memory channel is being written to with detector data, the
other is written to spacecraft memory.  Once the instrument fills the
first memory channel, the roles switch and the detector data go to the
second channel while the first channel is written to spacecraft memory.
This double-buffering - called 'ping-pong' acquisition - allows continuous
readout and storage of detector event data.
 
In this mode, a single event is represented by one 16-bit word in instrument
memory and can be either a detector photon event or a time hack event.
Photon events occur stochastically in time and are generated by photons
hitting the detector.  Time hack events, referred to simply as 'time hacks,'
occur at regular intervals in time and are generated by the ALICE flight
software.  The time hack interval is programmable and can be as short as 4ms.
 The PLM data stream comprises photon event locations interspersed with time
hack values.  Time hacks can be converted to timestamps in the series of
events and may be used to provide temporal information about the PLM data
stream and to constrain the time that any photon event occurs.
 
Histogram Imaging Mode:  summing of photon events into a 2-D spectrogram
------------------------------------------------------------------------
In Histogram Imaging Mode (HIM), the ALICE flight software sums detector
photon event counts for each pixel over a specified period (exposure) and
then writes the result out as a 2-D array i.e. a spectral-spatial image or
spectrogram.  In this mode, the 1-D 32k memory channel is treated as a 2-D
1024x32 array; each memory channel location thus accumulates the photon event
count acquired at its corresponding pixel location in the detector array.
While some have found it confusing to call this a histogram, it is only an
extension of the normally 1-D arrangement of histogram bins into pixels
representing bins in two dimensions.
 
Note that the timing information present in the time hacks of the PLM data
stream is neither generated nor saved in HIM.  Therefore, while the PLM data
stream can be analyzed to generate the equivalentof the HIM spectrogram, the
HIM data cannot be used to generate the PLM data.
 
Besides the collection and binning of detector events, HIM collects
pulse-height distribution (PHD) data from the detector electronics.  These
PHD data are collected and binned into a 64-bin histogram that is stored
within the first two rows of the detector histogram, in a location where no
physical pixel within the detector active area exists (therefore, the PHD
data does not interfere with the collected detector data).  During ground
processing, the Science Operations Center pipeline software reads these PHD
data and then zeroes the relevant area of the input array before creating the
data products.
 
The same ALICE instrument software that controls the PLM ping-pong
acquisitions also controls the HIM.
 
See Stern et al. (2007) for further details.
 
Measured Parameters
===================
 
Pixel List Mode
---------------
Each 16-bit word in the PLM data stream represents either the detector
location of a photon event or the time of a time hack.
 
One bit in each word identifies that word as a photon event or as a time
hack.  The meaning of the remaining fifteen bits depends on which type of
event the word represents.  Photon events use ten bits for the spectral
detector position (0 to 1023) and five bits for the spatial detector (0 to
31).  Time hack events use all fifteen bits to represent the number of 4ms
time intervals since either the instrument was turned on or the most recent
rollover of the time hack counter.
 
Histogram Imaging Mode
----------------------
Accumulated count of photon events, which each generated an analog pulse
above the set threshhold, at each pixel location for the duration of each
exposure.
 
MCP pulse-height distribution histogram.
 
 
 
 

        