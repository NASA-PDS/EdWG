# Lunar Reconnaissance Orbiter Mission Description

## Mission Overview

The majority of the text in this file was extracted and/or modified from:

1. Lunar Reconnaissance Orbiter Project Mission Concept of Operations, R. Saylor, 431-OPS-000042, 2006. 
2. Lunar Reconnaissance Orbiter Project Mission Design Handbook, R. Saylor, 431-HDBK-000486, 2006. 
3. Exploration and Science, presentation from LOLA Delta-PDR held on October 6, 2005
4. Theory of LEND Science and Observations, presentation from LEND PDR held  on September 21-23, 2005
5. Investigation Overview, presentation from LROC PDR held on September 8, 2005.
6. The Lunar Reconnaissance Orbiter: Plans for the Extended Science Phase, R. Vondrak et al, poster session, 43rd Lunar and Planetary Conference, March 22, 2012.
7. Bistatic Radar Observations of the Moon Using The Arecibo Observatory & Mini-RF Instrument on LRO, D.B.J. Bussey et al, presentation, 43rd Lunar and Planetary Conference, March 20, 2012.

LRO was launched on June 18, 2009 on an Evolved Expendable Launch Vehicle (EELV). The EELV inserted the orbiter into a direct trajectory to the Moon. The orbiter used the on-board propulsion system to enter into lunar orbit. After orbiter commissioning, the orbiter entered the nominal mission orbit of 50 km. LRO will perform routine measurement operations for one year. After one year, LRO may continue operations as part of an extended mission operations phase. The duration of extended mission is dependent on the orbit. After LRO uses all of the onboard fuel, LRO’s orbit will degrade and eventually impact the surface of the Moon.   

The orbiter carried a secondary payload, the Lunar Crater Observation and Sensing Satellite (LCROSS), which operated as a separate mission to observe the impact of a spent Centaur rocket released over the Moon’s south pole. (Data from the LCROSS mission are archived separately in PDS.)

Once LRO was in the final mission orbit, the six instruments began to collect measurement data for the mission.  A technology demonstration instrument, the Miniature-Radio Frequency (Mini-RF) instrument, also collected data during the nominal mission. At the start of the science mission, the status of Mini-RF was changed from technology demonstration instrument to science instrument. Mini-RF ceased acquiring monostatic radar data in December 2010 due to transmitter failure and in 2011 began acquiring bistatic radar measurements.

Radio Science on LRO, while not a formal investigation, includes the S-band communication and tracking system, the spacecraft timing system, as well as Laser Ranging, a technology demonstration component.  Data are collected using various elements of the Mission Operations Center and the LOLA SOC.  While the primary function of the radio subsystem is to support commanding, telemetry and tracking, the data are also scientifically useful.  Range and Doppler data from S-band tracking at a worldwide station network aids in refining lunar gravity models as well as positioning the spacecraft.  Laser ranging data, which improve the precision of orbit determination, in turn improve the accuracy of topographic measurement.
 
A description of the LRO instruments follows:
 
1\. Cosmic Ray Telescope for Effects of Radiation (CRaTER): Harlan Spence leads the CRaTER measurement investigation from Boston University (BU). The CRaTER instrument measures cosmic ray sources from two different directions (looking nadir and zenith). The instrument telescope contains a series of five detectors spaced apart that measure the different cosmic rays. CRaTER measurement goals are to:
    
    a. Measure and characterize the deep space radiation environment and spectra of galactic and solar cosmic rays.
    b. Characterize the biological impacts from the radiation environment.
 
CRaTER measures the Linear Energy Transfer (LET) spectra behind tissue equivalent material. LET spectra are the missing link connecting both Galactic Cosmic Rays (GCRs) and Solar Energetic Particles (SEP) to potential damage to tissue. CRaTER measures low LET from 200 keV to 100 MeV and high LET from 2 MeV to 1 GeV.
 
The CRaTER instrument has both a nadir and zenith field of view. The zenith field of view measures the primary sources of GCRs and SEPs. The nadir field of view measures sources of radiation from the lunar surface.
 
The instrument operates continuously during the entire orbit and operates autonomously. CRaTER nominally generates ~0.5 kbps of data but when solar flares are detected, the data rate can increase to ~90 kbps.
 
2\. Diviner Lunar Radiometer Experiment (DLRE): David Paige leads the Diviner measurement investigation from the University of California, Los Angeles (UCLA). Diviner includes a 9-channel radiometer with a wavelength range from 0.3 to 200 microns. DLRE makes precise radiometric temperature measurements of the lunar surface with the following measurement goals:
 
    a. Map global day/night surface temperatures.
    b. Characterize thermal environments for habitability.
    c. Determine rock abundances at landing sites.
    d. Identify potential polar ice reservoirs.
    e. Search for near-surface and exposed ice deposits.
 
DLRE is a 9-channel radiometer that measures wavelengths from 0.3 to 200 micron. Measurements have a spatial resolution of less than 500 m at the 50 km altitude.
 
DLRE operates continuously during the entire orbit. During most of the orbit, the instrument looks at nadir, but the instrument has two gimbals which allows it to rotate about both axes. Periodically throughout the orbit, the instrument rotates to perform two types of calibration activities. The first is a deep space/internal black body calibration. The instrument rotates to either deep space or the internal black body target for approximately 32 seconds. The deep space/black body calibration is performed approximately 12 times per orbit. The second calibration activity is the solar calibration activity. The instrument has a solar calibration target located just below the main instrument drum. During each orbit, the instrument rotates so that the solar target is illuminated by the Sun. The solar and the deep space/internal black body calibrations are both triggered by onboard event tables. The event tables are uplinked periodically throughout each month.
 
DLRE collects approximately 3.5 Gbits of data each day. Besides the periodic uplink of new event tables, the instrument operates autonomously throughout the orbit. There may be a possibility of interference with LROC imaging if a DLRE calibration sequence occurs during LROC NAC imaging. DLRE can execute a freeze command that will prevent a calibration sequence from occurring. The freeze command is inserted just prior to the LROC image commands as part of the spacecraft daily command load.
 
3\. Lyman-Alpha Mapping Project (LAMP): Alan Stern leads the LAMP measurement investigation from Southwest Research Institute (SwRI). The LAMP instrument includes high and low power supplies and a double delay line detector. The LAMP instrument measurement goals are to:
 
    a. Provide landform mapping from Lyman-alpha albedos at sub-km resolution in and around the permanently shadowed regions of the lunar surface.
    b. Identify and localize exposed water frost.
    c. Demonstrate the feasibility of using starlight and sky-glow for future surface mission applications.
 
LAMP measurements provide additional characteristics on landing sites as well as aid in the search for localized exposed water ice. The LAMP instrument’s sensitivity to ultraviolet (UV) absorption near 1600 angstrom allows detection of water frost. LAMP also provides images of permanently shadowed regions at ~500 m resolution.
 
The LAMP instrument is powered during the entire lunar orbit, but only collects measurement data over the night portion of the orbit. The LAMP instrument incorporates a Lunar Terminator Sensor (LTS) that detect the terminator line. The LTS contains two sensor channels with each channel offset from the LAMP boresight by +/- 1.5 degrees in a plane that contains the spacecraft ‘in-track’ motion (i.e. parallel to the LAMP entrance slit  width). When the instrument is approaching the terminator line, the instrument high voltages are reduced when passing from dark to light to prevent the detector from saturating during the dayside portion of the  orbit. The LTS also signals the instrument when the terminator (light to dark) is passed and the high voltages are then increased for measurement data collection. In case of an LTS failure, the ground generates a terminator prediction product that will be used to trigger the high  voltage operations from the daily command load.
 
The LAMP main door has a small hole which allows it to operate over the sunlit portion of the orbit. In this mode, the LTS provides the software with the signal to open and close the door. When LAMP operates over the entire orbit, the data volume per day is doubled to approximately 2.14 Gbits.
 
LAMP routinely collects approximately 1 Gbit of data per day and operates autonomously throughout the orbit without any daily operations input.
 
4\. Lunar Exploration Neutron Detector (LEND): The LEND measurement investigation is led by Igor Mitrofanov from the Russian Institute for Space Research. The LEND instrument includes a collimated sensor and sensors to detect thermal, epithermal, and high-energy neutrons.

LEND objectives include:
 
    a. Creation of high-resolution hydrogen distribution maps with sensitivity of about 100 ppm of hydrogen weight and horizontal spatial resolution of 5 km.
    b. Characterization of surface distribution and column density of possible near-surface water ice deposits at the Moon’s polar cold traps.
    c. Creation of a global model of neutron component of space radiation at an altitude of 30-50 km above the surface with spatial resolution of 20-50 km at the spectral range from thermal energies up to 15 MeV.

LEND sensors STN1, STN2, STN3, and SETN detect thermal neutrons and epithermal neutrons to characterize the lunar radiation environment. Sensors STN1 and STN3 operate as a Doppler filter for thermal neutrons from the front side and back side of the instrument. Sensors SETN and STN2 have open fields of view. Sensor SHEN detects high energy neutrons at 16 energy channels from 300 keV to more than 15 MeV to characterize the lunar radiation environment. The SHEN sensor has a narrow field of view of about 20-30 degrees. LEND collimated sensors CSETN1-4 detect epithermal neutrons with high angular resolution to characterize spatial variations of lunar neutron albedo, which depend on content of hydrogen in 1-2 m of the regolith. LEND collimated sensors CSETN1-4 and SHEN detect epithermal neutrons and high energy neutrons with high angular resolution to test water ice deposits on the lunar surface.
 
LEND measurements include:
 
    a. Measurement of thermal neutrons with flux variation greater than 1% and altitude-dependent spatial resolution about 50km.
    b. Measurement of epithermal neutrons greater than 0.4 electron Volts (eV) with flux variation about 2% (pole) and 10% (equator).
    c. Measurement of high-energy neutrons 0.3 - 15.0 Mega-electron Volts (MeV) with flux variations 4% (pole) and 10% (equator).
 
LEND operates autonomously, collecting data throughout the lunar orbit. LEND generates approximately 0.26 Gbits of measurement data per day. In order to perform early calibration measurements, LEND became active shortly after the first mid course correction (MCC) burn. Operationally, LEND is simple and has only three instrument modes: MEASUREMENTS, STAND-BY, and OFF. While in MEASUREMENTS mode, instrument electronics and detector high voltage are both ‘on’ and the instrument generates measurement and housekeeping data. In STAND-BY mode, instrument electronics are ‘on’, detector high voltage is ‘off’, and only housekeeping data are generated. While in OFF mode, the instrument is ‘off’, the instrument external heater is ‘on’, and only external temperature data are generated.
 
LEND instrument performance has decreased in recent years owing to the increasing orbital altitude of the spacecraft. While the LEND science team has had successes in providing insights into the distribution of neutrons (and therefore hydrogen) across the lunar surface, the opportunity for new science going forward is not realistic for LEND. The instrument has been transitioned into a data-collection only mode for ESM4 and beyond. Data will be collected by the instrument and pipeline processed for delivery to the PDS.

5\. Lunar Orbiter Laser Altimeter (LOLA): David Smith leads the LOLA measurement investigation from GSFC. LOLA uses a 1064 nanometer (nm) laser that expands to provide a five spot pattern on the Moon’s surface. A telescope receives the reflected light where the Electronics processes the return.

The primary LOLA objectives are:
 
    a. Produce a high-resolution global topographic model and global geodetic framework that enables precise targeting, safe landing, and safe mobility on the Moon’s surface. LOLA determines the topography of the Moon to geodetic quality from global to landing-site relevant scales.
    b. Characterize the polar illumination environment at relevant temporal scales, and image permanently shadowed regions of the Moon on landform scales to identify possible locations of surface ice crystals in shadowed polar craters.
    c. Identify the locations of appreciable surface water ice in the permanently shadowed regions of the Moon’s polar cold traps.
    d. Assess meter and smaller-scale features to facilitate safety analysis of potential future lunar landing sites.
 
LOLA has two secondary objectives:
 
    a. Establish a global geodetic reference system for the Moon.
    b. Improve the model of the lunar gravity field to facilitate precision navigation and landing

LOLA has the following capabilities. It measures the distance between the spacecraft and the surface which, along with the spacecraft position, will allow precise measurements of the lunar shape. The instrument lays down a laser spot pattern that provides altimetry measurements along- and across-track to enable the surface slope to be derived for safe landing. It measures the distribution of elevation within the laser footprint for estimation of surface roughness (rock size). LOLA also identifies regions of enhanced surface reflectance that might indicate the presence of water ice on the surface.

LOLA achieves its measurement objectives as follows:
 
    a. LOLA provides 5 profiles in a 70-meter swath.
    b. The instrument provides full spatial sampling after one year:
       i. ~ 1.2 km average spacing at equator
       ii. ~ 25 m average spacing above 86 degrees north and south
    c. The LOLA ground software performs cross-over analysis of LOLA data- topography, slopes, and roughness are the same on both tracks.
    d. LOLA data provide precision information about the orbiter’s location- S-band tracking data are augmented by Earth-based laser ranges.
    e. LOLA data improve the lunar gravity field model via cross-over analysis.
 
LOLA Mapping Data Products include the following:
 
    a. Topography with average horizontal resolutions (after one year) of 1.2 km at equator and of 25 m at latitudes greater than 86 degrees, with accuracies of +/-50 m in horizontal and less than 1 m in vertical.
    b. Surface slopes with average horizontal resolutions (after one year) of 50 m with accuracy of less than +/- 0.5 degrees.
    c. Surface roughness with average horizontal resolutions (after one year) of 5 m with accuracy of ~30 cm.
    d. Elevations of permanently shadowed regions with average horizontal resolutions (after one year) of 25 m with accuracy of ~10 cm.
    e. Reflectance of permanently shadowed regions with average horizontal resolutions (after one year) of 50 m with accuracy of +/- 5%.
    f. Polar illumination with average horizontal resolutions (after one year) of 50 m with accuracy of less than 1 m.
    g. Landing site surveys (approximately 50).
    h. Global lunar coordinate system with point-to-point distances with accuracy of +/- 70 m.
    i. Precision LRO orbits with accuracy of +/- 50 m in horizontal and +/- 1 m in vertical.
    j. Improved gravity model with a goal of producing a global gravity model that is as good as today’s nearside gravity model.
 
6\. Lunar Reconnaissance Orbiter Camera (LROC): Mark Robinson leads LROC measurement investigation from Arizona State University (ASU). LROC consists of two narrow angle cameras (NAC), a wide-angle camera (WAC), and a Sequence and Compression System (SCS).

LROC measurement objectives include:
 
    a. Landing site identification and certification, with unambiguous identification of meter-scale hazards.
    b. Unambiguous mapping of permanent shadows and sunlit regions.
    c. Meter-scale mapping of polar regions with continuous illumination.
    d. Overlapping observations to enable derivation of meter-scale topography.
    e. Global multispectral imaging to map ilmenite and other minerals.
    f. Global morphology base map.
    g. Characterize regolith properties.
    h. Determine current impact hazards by re-imaging 1-2m/pixel Apollo images.

The NAC operational concept is as follows:
 
    a. 25 km downtrack (no summing)
    b. 50 cm / pixel - 5 km cross track at 50 km
    c. 10 degree (300 km) ‘read-out gap’ (less with smaller images)
    d. Image targets at nadir with favorable lighting conditions
    e. Build up complete 1 m/pixel maps from 85.5 degrees to pole (N and S)
    f. Photometric and geometric stereo through repeat coverage.
 
The WAC operational concept is as follows:
 
    a. Continuous pole-to-pole 50 km swath mapping in all 7 bands possible
    b. Repeat BW coverage at poles every orbit 100 km swath width
    c. Global 100 m/pixel (vis) / 400m/pixel (UV) at 50km and 50-75 degree incidence angle.
 
LROC provides the following capabilities:
 
    a. Landing site identification and certification
         i. Unambiguous identification of 1 m hazards with 0.5 m/pixel and MTF greater than 0.2 at Nyquist, for blocks and small craters
        ii. 5 km swath with two NACs
       iii. Topography.
    b. Polar illumination
         i. WAC repeat synoptic coverage at high time resolution (every orbit) over full year: 80 degrees to 90 degrees to 88 degrees; full overlap 88 degrees to 90 degrees every orbit; excellent repeat coverage 85 degrees to 90 degrees
        ii. NAC meter scale mapping of poles: summer mosaics of each pole for morphology and permanent shadow from 85.5 degrees to the pole; winter repeat coverage observations of highly illuminated peaks/ridges, capable of finding smallest usable unit of ‘perma-light’
    c. High resolution topography
         i. Stereo coverage: point cross track, limited by project constraints and orbit progression, is easy at poles and more difficult at equator; two NACs offset ~50 lines downtrack for correlation and remove spacecraft pointing variation; 5 meter (or better) correlation patch
        ii. Photometric stereo: three images at different lighting; 1 to 2 m/pixel (bin for SNR); directly supports landing site certification and science analysis
    d. Multispectral mapping
         i. WAC uv/visible: 315, 360, 415, 560, 600, 640, 680 nm; global visible map at 100 m/pixel; global UV map at 400 m/pixel; map TiO2 soils (hold H, He); pyroclastic glasses (volatiles); olivine (magmatic processes)
        ii. Meshes with Clementine 100-200 m/pixel (415, 750, 900, 950, 1000)
    e. Global morphology: 100 m/pixel global map with 55-75 degree incidence angle - critical for mapping, basemap, crater counts (current best LO 50-600 m/pixel, poorest on farside); key for establishing relative age dates (ultimately absolute); resource assessment; context imaging
    f. Current impact rates
         i. Re-image Apollo pan coverage at same lighting (high and low Sun) at 1 m/pixel
        ii. Rates of impacts from 0.1 m to 10 m bolides poorly known (x100 difference in current models)
       iii. Should have been 950 craters &gt;10 m/diameter formed since 1972 (crater ~10x impactor)
        iv. Re-image 1 percent of Moon at 1 m/pixel should find at least 9 craters
         v. Critical measurement for understanding most dangerous impact hazards on Moon.
 
7\. Miniature-Radio Frequency (Mini-RF): Ben Bussey of the Johns Hopkins University Applied Physics Laboratory (JHU/APL) leads the Mini-RF measurement investigation. JHU/APL is responsible for instrument operations. Mini-RF is a Synthetic Aperture Radar (SAR) that consists of a fixed planar antenna mounted on an external spacecraft surface, and a cable harness between the electronics and the antenna. It operated on a non-interference basis during the nominal mission. After Mini-RF ceased acquiring monostatic radar data in December 2010, it began acquiring bistatic radar measurements in 2011.
 
Mini-RF measurements include:
 
    a. Imaging from 50km altitude surface areas that have been imaged by Forerunner with the same dual polarization, resolution, and S-band frequency as was used by Forerunner. The Forerunner instrument is on the ISRO Chandrayaan-1 mission to the Moon.
    b. Imaging polar areas with both S- and X-band, and at both baseline and zoom resolutions
    c. Acquiring data in a continuous transmit mode that is applicable for topography generation using post processing techniques
    d. Conducting a set of experiments to test the usability of Mini-RF hardware as a communications asset.
    e. Acquiring bistatic radar measurements from a high-power signal transmitted from the Arecibo Observatory Planetary Radar and reflected off the lunar surface.
 
Mini-RF Conops has six primary components:

    a. The communications experiment consists of two 10-minute data takes, approximately 24 hours apart, that occurred during the instrument commissioning phase, before the nominal mission.
    b. SAR Data Acquisition during nominal mission: Mini-RF acquired one 4-minute SAR data strip every month. Within this strip it is possible to alternate between different SAR modes, e.g. S or X band, baseline or zoom resolution. In addition, twice a year, Mini-RF acquired four 2-minute strips from four consecutive orbits.
    c. Continuous Mode Data Acquisition during nominal mission:  Mini-RF acquired one 4-minute SAR data strip every month. Additionally, twice a year, Mini-RF acquired four 2-minute strips on four consecutive orbits.
    d. Mini-RF Exploration Utilization Plan (MEUP): additional polar campaign data acquisitions were allowed during late nominal mission and early science mission during periods where the Beta angle is greater than 60 degrees (to mitigate impact on spacecraft solar array).
    e. During the science mission, a primary goal was to acquire significant global-scale s-band zoom data.
    f. Starting in 2011, Mini-RF was used to collect the first ever planetary bistatic radar images at non Beta=0 angles, to determine if the Moon’s polar craters contain ice. These measurements can be used for studies of the composition and structure of pyroclastic deposits, impact ejecta and melts, and the lunar regolith.
 
8\.  Radio Science (RS):  Gregory Neumann of the Goddard Space Flight Center (GSFC) leads the Radio Science data collection effort.  Data and Documentation are generated by the Universal Space Network, White Sands Complex, Deep Space Network, the LRO Project, and the LOLA Science Team. The Goddard Geophysical Astronomical Observatory provides satellite laser ranging data and coordinates data from International Laser Ranging Service partners in other countries.
 
Radio Science Data consist of primary and ancillary data; where the latter are needed for the processing or interpretation of the former.  The specific files that are being archived by the RS team are:
 
    a. Tracking Data
      The Station Raw Tracking Data support tracking of the orbiter and generation of orbit and mission products.  Each ground station (WS1 and the USN stations) creates data in a format identified as the Universal Tracking Data Format (UTDF) as described in publication 453-HDBK-GN (May 2007).
    b. Weather Data
      These ascii files are generated by various ground stations and record information such as time, temperature, pressure, relative humidity and wind speed.
    c. Small Forces Files
      These files include the updated parameters for thruster calibration based on all information from past maneuvers.  An assessment is made of the maneuver execution based on pre- and post-maneuver orbit solutions and telemetry, which is then used to determine a thrust scale factor for future maneuvers using the same thruster set.
    d. Laser Ranging Data (normal point and full rate)
      These data consist of one way range measurements via laser pulse time-of-flight from Earth to LRO, using one of LOLA’s laser detectors. This is essential to meeting the spacecraft’s precision orbit determination requirement, but also has secondary scientific value.

## Mission Phases

*Launch*

2009-06-18  (2009-169)
 
The launch phase began with launch vehicle lift-off and lasted about 90 minutes until payload separation. The payload had achieved the trans-lunar trajectory.
 
*Cruise*

2009-06-18 to 2009-06-23 (2009-169 to 2009-174)
 
The early cruise phase began with payload separation and lasted about 90 minutes until observing mode began. The orbiter performed Sun acquisition, ground acquisition, and deployments. Initial planning for a mid-course correction (MCC) occurred during this phase.
 
The mid-cruise phase began with observing mode and lasted about a day until completion of the mid-course correction (MCC). During this phase propulsion checks were performed, final MCC planning was done, and the MCC was executed.
 
The late cruise phase began with completion of the mid-course correction (MCC) and lasted until the lunar orbit insertion (LOI) sequence began. During this phase the CRaTER and LEND instruments performed early activation tasks, the orbiter underwent functional checks, and LOI planning was done.

*Lunar Orbit Acquisition* 

2009-06-23 (2009-174)
 
The lunar orbit acquisition phase began with the start of the lunar orbit insertion (LOI) sequence and lasted until the commissioning orbit was attained.
 
*Commissioning*

2009-06-23 to 2009-09-14  (2009-174 to 2009-257)
 
The commissioning phase began with attainment of the 30x216 km commissioning orbit and lasted until the mission orbit was achieved. During this phase orbiter and instrument checks and calibrations were performed and the orbit was adjusted to the mission orbit.
 
*Nominal Mission*

2009-09-15 to 2010-09-15  (2009-258 to 2010-258)
 
The nominal mission phase began with the attainment of the mission orbit and continued for 1 year. During this phase routine operations, non-routine operations, and measurement data processing were performed.

*Science Mission*

2010-09-16 to 2012-09-15 (2010-259 to 2012-259)
 
The science mission began at the completion of one year of nominal operations (officially at 15:40 UTC on September 16, 2010). It lasted 2 years. During this phase, objectives that had not been determined were to be realized, and impact planning and prediction would be performed.

The beginning of this phase marked the transition of LRO programmatic control from the NASA Exploration Systems Mission Directorate (ESMD) to the NASA Science Mission Directorate (SMD).

*Extended Science Mission*

2012-09-15 to 2014-09-15 (2012-259 to 2014-258)
 
The extended science mission began at the completion of the two-year Science mission (officially at 01:50 UTC on September 15, 2012). It lasted 2 years. During this phase, objectives included: understanding the bombardment history of the Moon; interpreting lunar geologic processes; mapping the global lunar regolith; identifying volatiles on the Moon; and measuring the lunar atmosphere and radiation environment.
 
*Second Extended Science Mission*

2014-09-15 to 2016-09-15 (2014-258 to 2016-259)
 
The second extended science mission (ESM2) began at the completion of the two-year Extended Science Mission (ESM1).  The Second Extended Science Mission began officially at 01:14:43 UTC on September 15, 2014. It lasted 2 years.

*Third Extended Science Mission*

2016-09-15 to 2019-09-15 (2016-259 to 2019-258)

The third extended science mission (ESM3) began at the completion of the two-year Second Extended Science Mission (ESM2).  The Third Extended Science Mission began officially at 00:39:44 UTC on September 15, 2016. It was to last for 2 years but was extended by the NASA Science Mission Directorate for an additional year.

Note: the Third Extended Science Mission, a.k.a., the Cornerstone mission is a result of the Cornerstone Mission proposal. For consistency with data products, use of ESM3 or Third Extended Science Mission is the agreed upon nomenclature.

*Fourth Extended Science Mission*

2019-09-15 to 2022-10-01 (2019-258 to 2022-274)

The fourth extended science mission (ESM4) began at the completion of the three-year Third Extended Science Mission (ESM3).  The Fourth Extended Science Mission began officially at 01:31:01 UTC on September 15, 2019. It lasted 3 years.

*Fifth Extended Science Mission*

2022-10-01 to 2025-10-01 (2022-274 to 2025-274)

The fifth extended science mission (ESM5) began at the completion of the three-year Fourth Extended Science Mission (ESM4). The Fifth Extended Science Mission began officially at 00:46:06+00 UTC on October 1, 2022. It will last 3 years or until the orbiter impacts the lunar surface.

## Mission Objectives Summary

The primary objective of the Lunar Reconnaissance Orbiter (LRO) mission is to conduct investigations that support future human exploration of the Moon.  Specific LRO mission objectives are: 
    
    1. Characterize the lunar radiation environment, biological impacts, and potential mitigation. Key aspects of this objective include determining the global radiation environment, investigating the capabilities of potential shielding materials, and validating deep space radiation prototype hardware and software.
    2. Develop a high-resolution global, three-dimensional geodetic grid of the Moon and provide the topography necessary for selecting future landing sites.
    3. Assess in detail the resources and environments of the Moon's Polar Regions.
    4. Provide high spatial resolution assessment of the Moon's surface addressing elemental composition, mineralogy, and regolith characteristics.

## References

1. Saylor, R. Lunar Reconnaissance Orbiter Project Mission Concept of Operations, 431-OPS-000042, 2006. 
 
2. Saylor, R. Lunar Reconnaissance Orbiter Project Mission Design Handbook, 431-HDBK-000486, 2006. 
 
3. Exploration and Science, presentation from LOLA Delta-PDR held on October 6, 2005.
 
4. Theory of LEND Science and Observations, presentation from LEND PDR held on September 21-23, 2005.
 
5. Investigation Overview, presentation from LROC PDR held on September 8, 2005.
 
6. Vondrak, R., et al. The Lunar Reconnaissance Orbiter: Plans for the Extended Science Phase, poster session, 43rd Lunar and Planetary Conference, March 22, 2012.
 
7. Bussey, D.B.J., et al. Bistatic Radar Observations of the Moon Using The Arecibo Observatory & Mini-RF Instrument on LRO, presentation, 43rd Lunar and Planetary Conference, March 20, 2012.



