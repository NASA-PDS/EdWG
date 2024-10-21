
 
Instrument Overview
===================
The Microwave Radiometer (MWR) is one of a suite of instruments on Juno.
The Juno mission has the overall goal of answering the outstanding questions
outstanding about Jupiter's structure and origin. Specifically, the MWR was 
designed to characterize Jupiter's atmosphere as following:

-  Determine the global O/H ratio (water abundance) in Jupiter's
atmosphere
-  Measure latitudinal variations in Jupiter's deep atmosphere
(composition, temperature, cloud opacity, and dynamics) 
-  Measure the microwave brightness temperatures of Jupiter over all
latitudes at wavelengths that fully sample the atmospheric thermal
emission at all altitude levels from the ammonia cloud-forming
region to below the water cloud-forming region

To achieve this the MWR experiment uses a microwave sounding approach 
described in Janssen et al., 2005. The MWR instrument measures the 
atmospheric thermal emission at six frequencies. Thermal emission from an 
atmosphere arises because of the presence of absorbing constituents in the 
atmosphere, and the measured emission contains information on both the 
concentration and temperature of these constituents. The information content 
changes with frequency, and the determination of the spectrum of atmospheric 
thermal emission can be used to infer key parameters of both the temperature 
and compositional structure of the atmosphere. Water and ammonia are the only 
significant sources of microwave opacity in Jupiter's atmosphere, so their 
concentrations are the unique target of any microwave sounding approach.  

The MWR instrument comprises what are essentially six independent 
radiometers, each of which measures the microwave emission viewed through its 
own independent antenna. The six antennas are distributed around the 
spacecraft body and view in a direction perpendicular to the spin axis of the 
spacecraft.  Since the spin axis of the spacecraft is oriented approximately 
perpendicular to the orbit plane, the beam of each antenna sweeps through a 
great circle on the sky that passes along the sub-spacecraft track on Jupiter 
and through the nadir direction.  Each point along this track is thus 
observed numerous times, at different emission angles, as the spacecraft 
spins and moves along its orbit.  The accumulated data at each such point and 
its dependence on emission angle an frequency is then analyzed to obtain 
vertical atmospheric composition and structure using a radiative transfer 
model.

Each receiver makes contiguous radiometric measurements, or integrations, of 
fixed 100-ms duration. In a typical sequence of such integrations an internal 
switch is cycled from the antenna input to periodically view an internal 
load, and three independent internal reference noise sources are periodically 
switched on and off for calibration. The cycle for such switching is 
synchronous for all receivers and is set by selecting from a table contained 
in the flight software. The table may be changed by an uplink command. The 
choice of specific sequences depends on instrument performance and 
optimization of the calibration algorithm.

For the key observations to be made in the nine-hour window around Jupiter
perijove, the MWR is desiged to downlink all contiguous 100-ms observations. 
Outside this window, however, not all of this data is essential and in most 
cases the resulting data would quickly fill the MWR's partition on the 
spacecraft. To avoid this, a command is sent to downlink only a fraction of 
the data obtained. The instrument organizes its data stream into time-
contiguous units of ten 100-ms observations, each thus corresponding to one 
second's worth of observation. Successive units may be contiguous in time 
(full data rate) or separated by n seconds each (reduced data rate). A 
different on-board switching sequence is typically commanded in order to 
optimize the calibration for reduced sampling rates.

Documents that describe the major components of the MWR instrument and its 
operation will be found in the DOCUMENTS folder and include:
1. The MWR volume SIS
2. The MWR instrument paper (Janssen et al., 2017)
3. The MWR Operations Guide (not yet available)
4. The MWR Instrument Users Guide
5. The MWR Flight Software Users Guide
6. The MWR Algorithm and Theoretical Basis Document and Error Analysis

The canonical paper that describes the design, operation, calibration, and 
analysis of the MWR data to achieve the scientific objectives of the MWR 
experiment is Janssen et al., 2017.

        