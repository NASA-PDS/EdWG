
 
########################################################################
########################################################################
REQUIRED READING:
- McComas et al.  (2007) [MCCOMASETAL2007]
- Weaver et al.  (2007) [WEAVERETAL2007]
########################################################################
########################################################################
 
 
      The SWAP description was was adapted from the New Horizons website,
      Weaver et al.  (2007) [WEAVERETAL2007], and McComas et al. (2007)
      [MCCOMASETAL2007].
 
 
Instrument Overview
========
 
 
Specifications
--------
 
NAME:                    SWAP (Solar Wind Around Pluto)
DESCRIPTION:             Low energy plasma instrument
PRINCIPAL INVESTIGATOR:  Dave McComas, SwRI
ENERGY RANGE:            30 eV - 7.7 keV
FIELD OF VIEW:           270 deg x 10 deg (Note 1)
ANGULAR RESOLUTION:      N/A
ENERGY RESOLUTION:       1eV (<2keV); 9% (>2 keV)
 
Note 1:  deflection angles up to +15 deg additional
 
Description
--------
Solar Wind Around Pluto (SWAP) instrument is designed to measure the
properties of solar wind ions for the New Horizons mission to Pluto. The SWAP
instrument is an electrostatic instrument. The SWAP electro-optics control
the energy band pass of ions entering the instrument. The electro-optics have
three parts:  the Retarding Potential Analyzer (RPA), the Electrostatic
Analyzer (ESA), and the deflector (DFL). The RPA consists of four grids with
the inner two having a positive voltage, which repels ions with energies less
than the corresponding potential energy (qV). The Electrostatic Analyzer has
two parts, which are concentrically spaced, an inner dome and an outer
spherical shell (at ground). For any given settings of the RPA and ESA
voltages, only ions with a limited range (bandpass) of energies pass through
the ESA to reach the detector. The deflector is used to adjust the field of
view.
 
SWAPs ESA and RPA voltages are used together to select the E/q (energy)
passband. When the RPA is off, the passband is determined solely by the ESA
voltage, which provides an 8.5% FWHM resolution.  At increasing RPA voltages
for a given ESA voltage, the passband is cutoff in a variable shark-fin
shape, allowing roughly two decades decreased sensitivity. Finally,
differentiating adjacent RPA/ESA voltage combinations, or deconvolving
multiple combinations, provides high-resolution differential measurements of
the incident beam's flux as a function of energy.  Differences in the ion
energy as small as 1-2 eV are distinguishable at typical solar wind energies
of ~1000 eV which is a resolution on the order of 0.1%.
 
See the Required Reading documents listed above, and provided with this data
set, for further details of this instrument and its capabilities.
 
 
Scientific Objective
========
 
The Solar Wind Analyzer around Pluto (SWAP) instrument will measure charged
particles from the solar wind near Pluto to determine whether Pluto has a
magnetosphere and how fast its atmosphere is escaping.
 
 
Calibration
========
 
See
 
  /DOCUMENT/SWAP/SWAP_CAL.*
 
and Section 4 of  McComas et al. (2007) [MCCOMASETAL2007], also available as
a preprint at this URL:
 
  http://www.boulder.swri.edu/pkb/ssr/ssr-swap.pdf
 
as of 20.April, 2007.
 
 
Operational Considerations
========
 
SWAP data are affected by spacecraft attitude and thruster firings.  Values
for those parameters concurrent with each observation, along with
housekeeping information, are included in the observation's data file.
 
The SWAP experiment detects atmospheric escape from Pluto as a change in the
solar wind caused by the interaction of the Pluto atmosphere with the solar
wind.  In certain scenarios, a factor of 10 variation in the solar wind may
occur over a period of days.  It is therefore critical to measure the solar
wind for several solar rotations in order to characterize the most likely
external solar wind properties during the actual encounter period.
 
 
Detectors & Electronics
========
 
See the instrument description and specifications above.
 
 
Operational Modes
========
 
The SWAP instrument uses seven modes:  OFF; BOOT; LVENG; LVSCI; HVENG; HVSCI.
 For a description of these modes see Tables IV & V in the Space Science
Reviews paper McComas et al. (2007) [MCCOMASETAL2007], also available as a
preprint at this URL:
 
  http://www.boulder.swri.edu/pkb/ssr/ssr-swap.pdf
 
 
Science Data Collection
-----------------------
Science data are collected in the HVENG and HVSCI modes.  HVENG was used
extensively during commissioning for initial HV ramp-up.  HVSCI is the
primary SWAP science mode.  In HVSCI, the optical power supply voltages are
stepped every 0.5 seconds.  During each 0.5-second period at a single pair of
RPA/EPA voltage settings, approximately 100 milliseconds are allowed for the
optical power supply settling time and 390 milliseconds are allocated to
counting events.  An overall cadence comprising 128 0.5-second steps defines
the 64-second science-acquisition frames and hence all science activities.
 
Two methods of sweeping during each 64 second period, called the coarse-fine
and coarse-coarse sweeps, are user selectable.  A typical coarse-fine sweep
comprises a 32-second coarse sweep which covers the entire energy range with
64 logarithmically-spaced optical power supply voltages, followed by a
32-second (also 64 0.5-second steps) fine sweep.  A coarse-coarse sweep
comprises two 32-second coarse sweeps performed in one 64-second period.
 
For both sweep types, the optical power supply voltages are set from one of
several user-selectable tables.  For the coarse-fine sweep, the peak value of
the event counter during the coarse sweep is located to set the center
voltages of the fine sweep so that a finer resolution sweep around that peak
response can be performed.
 
The following graphics describe very roughly of what happens during a typical
coarse-fine sweep; more detailed plots are avaiable in the documents referred
to earlier.  In all three graphics, the abscissa is time covering one
64-second coarse-fine sweep.  The legend inside each plot gives a
descripting, the range, and the untis of the ordinate.
 
In the first 32 seconds on the left of the plots, the ESA and RPA voltages go
rapidly through a large range in a coarse sweep that covers the entire energy
range of the instrument.  At around ten to fifteen seconds into that coarse
sweep, there is a rise in count rate indicated by the peak.  Based on the
timing and voltages corresponding to that peak, the SWAP instrument sets the
ESA and RPA voltages and changes them more slowly through the fine sweep
during the second 32 seconds on the right of the plots, and there is a peak
observed at much higher resultion during that time.
 
_____________________________________________________________________________
                                                                             |
                                                            *                |
          Output Count rate (0-600Hz)                      * *               |
                                                          *  *               |
                                                         *    *              |
                                                         *     *             |
                                                        *      *             |
                                                        *       *            |
             *                                         *        *            |
            * *                                        *         *           |
           *   *                                     **           *          |
_**********_____*************************************______________********__|
0s                                32s                                      64s
 
_____________________________________________________________________________
                                                                             |
*                                                                            |
*          Input ESA Voltage (0-4000V)                                       |
 *                                                                           |
  *                                                                          |
   **                                                                        |
     **                                                                      |
       ***                                                                   |
          ****                       ______________                          |
              *****                 *              --------------____________|
                   ******          *                                         |
_________________________**********__________________________________________|
0s                                32s                                      64s
 
_____________________________________________________________________________
                                                                             |
******                                                                       |
     *     Input RPA Voltage (0-2000V)                                       |
     *                                                                       |
      *                                                                      |
       *                                                                     |
        *                            ______                                  |
         **                         *      ------_______                     |
            **                      *                   ------______         |
              ***                  *                                ------___|
                 *******           *                                         |
________________________***********__________________________________________|
0s                                32s                                      64s
 
 
One result of this is that there will be gaps in the apparent energy
resolution when the data from coarse and fine sweeps are compared against
each other.
 
 
Measured Parameters
========
 
SWAP counts events which represent the interactions between the SWAP
electro-optics and solar wind particles.  The energy of any detected event is
determined by the energy bandpass in effect at the time of that event, which
in turn is determined by the ESA and RPA settings (voltages).   SWAP sweeps
its energy bandpass over the instrument's energy range, sorts events into
energy and time bins, and returns either real-time science or summary data
based on those events.
 
Indirectly through calibration, the SWAP instrument measures the bulk
properties of the solar wind (speed, density or flux, temperature), and
analysis of changes in these parameters during Pluto encounter will provide
an indication of the nature of any atmospheric particles that are escaping
Pluto.
 
See the SWAP SSR paper for more detail.

        