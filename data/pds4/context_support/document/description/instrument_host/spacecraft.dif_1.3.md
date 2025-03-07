
 
 
  Instrument Host Overview
  ========================
    The Deep Impact flyby spacecraft was used for the NASA Deep Impact
    mission in 2005 and for the extended mission EPOXI from October 2007
    through end of mission on 20 September 2013.
 
    The flyby vehicle carries three scientific instruments:  a
    high-resolution infrared imaging spectrometer (HRII), a high-resolution
    multi-spectral visible CCD (HRIV), and a medium-resolution
    multi-spectral visible CCD (MRI).  It was launched on 12 January 2005
    with an attached impactor spacecraft.  On 3 July 2005, the flyby craft
    released the impactor, successfully delivering it into the path of
    comet 9P/Tempel 1.  About 24 hours later, the flyby spacecraft recorded
    the resulting 19-gigajoule impact beginning about 05:44:34.265 UT on
    July 4, 2005 (at the flyby spacecraft, Earth-received time 05:52:00
    UT).  The encounter occurred at distances of 1.5 AU from the Sun and
    0.9 AU from the Earth.  About 14 minutes after impact, the flyby
    vehicle was at closest approach of 500 km from the nucleus.
 
    Because the flyby spacecraft and its instruments survived the
    encounter with Tempel 1, NASA executed a trajectory correction
    maneuver on 20 July 2005 which put the spacecraft on a new orbit to
    fly past Earth in late December 2007 and solicited proposals for an
    extended mission.  The spacecraft was put into sleep mode on 9 August
    2005.  It was woken up on 25 September 2007 in preparation for the
    selected EPOXI mission.
 
    From mid-January through August 2008, the HRIV instrument successfully
    observed transits of eight known extrasolar planets for the EPOXI
    mission.  Also during this period, the HRII and HRIV instruments
    continuously observed the Earth at equatorial latitudes for 24 hours at
    three different times.  In 2009 the same instruments observed Earth
    again but at northern and southern latitudes.  Also Mars was observed
    for 24 hours and the exoplanet microlensing event, MOA-2009-BLG-266 was
    imaged over several days.
 
    From mid-October to mid-November 2008, the first deep space
    communications network, also known as the Interplanetary Internet, was
    successfully tested using the Deep Impact flyby spacecraft.  Using
    software called Delay-Tolerant Networking (DTN) dozens of images were
    transmitted to and from the flyby spacecraft located more than 32
    million kilometers from Earth.
 
    In late 2010 the flyby spacecraft wrapped up its EPOXI mission with an
    encounter of comet 103P/Hartley 2.  After observing the comet for 60
    days with the same suite of instruments used at 9P/Tempel 1, the flyby
    spacecraft had its closest approach of 103P/Hartley 2 at 13:59:47.31 UTC
    on 4 November 2010 at a distance of 694 km and a flyby speed of 12.3
    km/s. The spacecraft flew under the comet on a slightly northward
    trajectory in an ecliptic reference frame, then rotated to keep the
    body-mounted instruments pointed at the comet for departure imaging that
    continued for 21 days.
 
    On 14 August 2013, the flyby spacecraft failed to phone home.  The
    operations team eventually traced the issue to a problem with a time
    computation that put the spacecraft computer into an infinite reboot
    loop, thereby losing both attitude control and communications.  After
    trying unsuccessfully for more than a month to regain contact, NASA
    announced the end of operations for the Deep Impact flyby spacecraft
    on 20 September 2013.
 
 
  Instrument Host Details
  =======================
    The flyby vehicle is a 3-axis stabilized spacecraft that carries three
    scientific instruments as noted above:  HRII, HRIV, and MRI. The
    instruments, an integrated set of four hemispherical resonator gyros,
    and two star-trackers are mounted on a rigid platform attached to the
    spacecraft in the X-Z plane, parallel to the solar panel.  The
    instrument pointing direction is in the X-Z plane, at approximately 45
    degrees to the -X and +Z axes, where +Y is perpendicular to the solar
    panels on the sunward side.  Because the instruments are body-mounted,
    pointing is accomplished by slewing the spacecraft with reaction wheels
    and hydrazine thrusters.
 
    The spacecraft is equipped with a once-deployed solar panel and one
    NiH2 battery for its power subsystem.  The 7.2-meter^2 solar panel has
    a maximum off-sun pointing constraint of 30 degrees to avoid problems
    caused by overheating of the subsystems.  The flyby spacecraft has
    redundant RAD750 computers with 309 megabytes (MB) of memory for
    scientific data.  All critical data are stored redundantly on both
    computers and a subset can be transmitted in near-real time to Earth.
 
    Communications are achieved via either a gimballed high-gain antenna
    (HGA) or a fixed low-gain antenna (LGA).  During the missions, Deep
    Space Network (DSN) support is provided primarily with 34-m antennas
    with 70-m support used during the comet encounter phases.  The HGA
    antenna has the capability to transmit 20 to 200 kilobits per second
    (kbps).  At the maximum downlink rate, it takes 4.5 hours to empty the
    309-MB memory.  Pointing range of the HGA is limited to the +x
    hemisphere of the flyby vehicle.  The flyby craft uses X-band to
    communicate with Earth.  For Deep Impact, it used the S-band for
    bi-directional communication with the impactor spacecraft after
    separation.
 
    Attitude control and propulsive maneuvers are performed using a
    blowdown hydrazine propulsion subsystem designed to provide 190 m/s of
    delta-velocity.
 
    The normal spacecraft attitude during the missions points the +y- axis
    of the spacecraft to within 30 degrees of the sun.  Pointing outside
    this range is limited to 15 minutes every 4 hours to avoid overheating
    of subsystems.  This constraint limits calibrations during cruise and
    observations of the comets during closest approach and prior to 10 days
    before encounter.
 
    Debris shields are placed on the spacecraft to protect it from high
    velocity dust impacts during the encounter with Tempel 1.  The
    shielding is designed for a velocity vector of the spacecraft in the +X
    direction (dust relative motion toward -X).
 
    Science objectives for the Deep Impact mission were met using three
    instrument subsystems:  HRII, HRIV, and MRI.  The EPOXI mission uses
    these same three instruments to achieve its scientific objectives.
    Additionally for the Deep Impact mission, data from the DSN radio
    subsystem were analyzed for deflections of the spacecraft caused by the
    mass of the comet and for slowdowns as a result of gas and dust drag
    (as expected, no effects were noted in the tracking data).  For more
    information about the DSN and its use in radio science see the report
    by Asmar and Renzetti (1993) [ASMAR&RENZETTI1993].
 
    The system requirement specifications for the flyby spacecraft were:
 
      Payload Power             : 92 watts, average during engagement
      Payload Mass              : 370-kg impactor, 90-kg instruments
      Payload Total Data Volume : 309 MB
      Payload Data Downlinked   : 309 MB
      Pointing Accuracy         : 200 microradian
      Pointing Knowledge        : 65 microradian, 3 axes 3-sigma
      Telecom Band to Earth     : X-band
      Uplink/Downlink Rates     : 125 bps/200 kbps
      Telecom Band to Impactor  : S-band
      Data Rate to Impactor     : 64 kbps
      Propulsion                : 190 m/s delta-velocity
 
 
  Flight Performance
  ==================
 
    Clock Correlation
    -----------------
      During the Deep Impact mission, clock correlation packets indicated
      large drifts in the clocks on-board the flyby and impactor spacecraft
      due to thermal changes induced by trajectory correction maneuvers
      near encounter.  The drifts resulted in a difference of several
      seconds between impact times based on data from the flyby and
      impactor spacecraft and ground-based data.
 
      During January 2006 the project used available spacecraft data and
      advice from engineering personnel to correlate the flyby clock and
      Dynamical Barycentric Time (TDB) to within one or two seconds and
      the flyby and impactor clocks to one-half of a second.  The project
      moved the estimated impact time forward by two seconds, from
      05:44:36 UTC on 4 July 2005 as reported by A'Hearn, et al. (2005)
      [AHEARNETAL2005A] to 05:44:34.265 UTC at the flyby spacecraft and
      05:44:34.200 UTC at the impactor spacecraft.  The project also
      generated self-consistent SPICE CK kernels based on this analysis.
 
      The improved kernels were included in the Deep Impact SPICE data set
      archived in the PDS.  The timing discrepancy is discussed in the Deep
      Impact Spacecraft Clock Correlation report included in the Deep
      Impact and EPOXI documentation data set,
      DI-C-HRII/HRIV/MRI/ITS-6-DOC-SET-V4.0.
 
      As of early 2009, the best spacecraft clock correlation data still had
      known inaccuracies of up to 0.5 seconds.  The mission operations team
      has since figured out how to correct raw clock correlation data for
      the flyby spacecraft to allow timing fits that are accurate to at
      least the sub-second level.  The project plans to generate, most
      likely in 2013, a complete corrected set of correlations since launch.
      This will ultimately result in a future version of a spacecraft clock
      SPICE kernel that will retroactively change correlation for **all**
      Deep Impact and EPOXI data.  When this kernel is available, it will be
      added to the SPICE data sets for the two missions and posted on the
      NAIF/SPICE web site at http://naif.jpl.nasa.gov/naif/.
 
 
    Safe Mode and Telecom Anomaly
    -----------------------------
      During the EPOCh phase of the EPOXI mission, the flyby spacecraft
      experienced a safe mode and a telecom anomaly that disrupted and
      delayed data acquisition for several weeks, which was very unusual.
 
      On 17 February 2008, the flyby spacecraft autonomously entered safe
      mode as it was turning to an optimal attitude to transmit EPOCh data
      to Earth.  Mission controllers believed the safe mode was triggered
      when one of the reaction wheels, which helps maintain spacecraft
      attitude, experienced slightly higher temperatures than the on-board
      fault protection software would allow.  After slowly downlinking
      some engineering data to Earth, controllers determined the
      spacecraft could be brought out of safe mode without triggering new
      problems.  On 29 February the spacecraft successfully exited safe
      mode and began downlinking the EPOCh images taken before safe mode
      was entered.  On 6 March 2008, the flyby spacecraft resumed
      observations of exoplanet transits.
 
      After the March 28th downlink of 5000 photometric HRIV frames of
      transiting planet system XO-2, a telecommunication anomaly occurred.
      This was the largest volume of data in a single downlink for EPOXI
      to date.  Following this downlink, EPOCh observations were paused to
      investigate the cause of an 8-dB (33%) loss of downlink signal and
      some slightly elevated temperatures on the spacecraft as it passed
      through perihelion.  As the spacecraft cooled over three weeks (a
      combination of moving further from the sun and all instruments being
      turned off), telemetry strength returned, and the project restarted
      EPOCh by first downlinking the images of XO-2 that had been stored
      on board the spacecraft since the end of March.  Telecommunications
      functioned as expected and observations of exoplanet transit resumed.
 
 
    Pointing Stability
    ------------------
      Rieber and Sharrow (2009) [RIEBER&SHARROW2009] discuss how the
      flight system was re-adapted to improve pointing stability of the
      flyby spacecraft to prevent EPOCh exoplanet targets from wandering
      outside the HRIV frame.
 
 
  Recommended Reading
  ===================
    For a detailed descriptions of the flyby spacecraft and
    auto-navigation, see A'Hearn, et al. (2005) [AHEARNETAL2005B], Blume
    (2005) [BLUME2005], Hampton, et al. (2005) [HAMPTONETAL2005], and
    Mastrodemos, et al. (2005) [MASTRODEMOSETAL2005].  For information
    about the anticipated flight data and the cratering experiment for the
    Deep Impact mission, see Klaasen, et al. (2005) [KLAASENETAL2005],
    Richardson, et al. (2005) [RICHARDSONETAL2005], and Schultz and Ernst
    (2005) [SCHULTZ&ERNST2005].  The submitted versions of these
    publications are included in the Deep Impact and EPOXI documentation
    data set, DI-C-HRII/HRIV/MRI/ITS-6-DOC-SET-V4.0.  Initial results from
    Deep Impact are presented by A'Hearn, et al. (2005) [AHEARNETAL2005A].
 
    Rieber and Sharrow, (2009) [RIEBER&SHARROW2009] describe how the
    flight system and mission operations were re-adapted such that
    exoplanet transit imaging for EPOCh posed minimal risk to the Hartley
    2 encounter for DIXI.  The pointing stability of the flyby spacecraft
    is also discussed in this paper.
 
 
  This instrument host description was originally provided by Dr. Michael
  A'Hearn for the Deep Impact mission and will be updated as the EPOXI
  mission progresses.

        