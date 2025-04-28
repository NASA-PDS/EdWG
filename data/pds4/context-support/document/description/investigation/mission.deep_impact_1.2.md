
 
 
  Mission Overview
  ================
    The goal of the Deep Impact mission was to understand the physical
    and chemical properties of a comet as a function of depth below the
    surface.  To reach this goal, Deep Impact reproduced the impact of
    a boulder onto a cometary nucleus at a hypervelocity speed,
    characteristic of collisions in the asteroid belt.  The mission
    delivered an impactor spacecraft of approximately 360 kg onto the
    nucleus of 9P/Tempel 1 at a relative speed of 10.3 km/s.  The kinetic
    energy of the impactor, about 19 gigajoules, produced a crater with
    a diameter between 100 and 250 meters in about 200 seconds (A'Hearn,
    et al. (2005) [AHEARNETAL2005A], Schultz and Ernst (2005)
    [SCHULTZ&ERNST2005], Richardson, et al. (2005) [RICHARDSONETAL2005]),
    and Busko, et al. (2007) [BUSKOETAL2007]).  The impact was imaged by
    the three instruments on board the flyby spacecraft.  The best
    estimate of the impact time was 4 July 2005 at 05:44:34 UTC at the
    flyby spacecraft (Earth-observed time 05:52:00 UTC).  The phase angle
    on approach for both spacecraft was about 62.9 degrees.
 
    Deep Impact consisted of two spacecraft launched together on
    12 January 2005 at 18:47:08.57 UTC and which flew together until
    one day before impact on 4 July 2005.  On July 3 at 05:59:58 UTC,
    the two spacecraft separated while on a course to impact comet
    Tempel 1.  They immediately went into auto-navigation mode using
    an algorithm that ensured the impactor would hit an illuminated
    area of the nucleus and the flyby spacecraft would point to the
    same area for imaging the impact.  The impactor observed the comet
    with a visible CCD (ITS) until several seconds before the impact.
    Shortly after separation, the flyby spacecraft performed a trajectory
    correction maneuver and passed approximately 500 km below the
    nucleus, as seen from the sun.  The flyby spacecraft recorded the
    encounter and the impact with the High Resolution telescope's visible
    CCD (HRIV) and infrared imaging spectrometer (HRII) as well as with
    the Medium Resolution telescope's visible CCD (MRI).  Initial results
    from the encounter were discussed by A'Hearn, et al. (2005)
    [AHEARNETAL2005A].  Detailed results were presented later in
    volume 187 of Icarus (March 2007), dedicated specifically to
    Deep Impact.
 
    The mission, science objectives, instrumentation, and expected
    results were described in a special edition of Space Science Reviews
    (SSR) dedicated to Deep Impact.  See A'Hearn, et al. (2005)
    [AHEARNETAL2005B], Blume (2005) [BLUME2005], Mastrodemos, et al.
    (2005) [MASTRODEMOSETAL2005], Hampton, et al. (2005)
    [HAMPTONETAL2005], Klaasen, et al. (2005) [KLAASENETAL2005], Belton,
    et al. (2005) [BELTONETAL2005], Lisse, et al. (2005)
    [LISSEETAL2005], Sunshine, et al. (2005) [SUNSHINEETAL2005],
    Richardson, et al. (2005) [RICHARDSONETAL2005], Schultz and Ernst
    (2005) [SCHULTZ&ERNST2005], Thomas, et al. (2005) [THOMASETAL2005],
    and Yeomans, et al. (2005) [YEOMANSETAL2005], and McFadden, et al.
    (2005) [MCFADDENETAL2005].  These SSR papers are included in the
    Deep Impact and EPOXI documentation set, archived as PDS dataset
    DI-C-HRII/HRIV/MRI/ITS-6-DOC-SET-V4.0.
 
    The world-wide Earth-based observing campaign for the mission was
    described by Meech, et al. (2005) [MEECHETAL2005] in the SSR
    edition.  McFadden, et al. (2005) [MCFADDENETAL2005] discussed the
    Education and Public Outreach component of the mission.
 
    Calibration of Deep Impact instruments and the calibration
    pipeline were discussed in Klaasen, et al. (2008) [KLAASENETAL2006].
    A draft of this calibration paper is included in the Deep Impact
    and EPOXI documentation set, archived as PDS dataset
    DI-C-HRII/HRIV/MRI/ITS-6-DOC-SET-V4.0.
 
 
    Known Clock Discrepancy
    -----------------------
      There is a known one- or two-second uncertainty in the time
      of the impact.  Clock correlation packets indicated large drifts
      in the clocks on-board the flyby and impactor spacecraft due to
      thermal changes induced by trajectory correction maneuvers near
      encounter.  The drifts resulted in a difference of several
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
 
      The improved kernels were included in the Deep Impact SPICE data
      set archived in the PDS.  The timing discrepancy is discussed in
      the 'Deep Impact Spacecraft Clock Correlation' report included
      in the Deep Impact and EPOXI documentation set, archived as PDS
      dataset DI-C-HRII/HRIV/MRI/ITS-6-DOC-SET-V4.0.
 
 
  Mission Phases
  ==============
    Three primary phases are defined for the archive of flight-related
    data:  thermal-vacuum ground calibrations (TV), cruise, and 9P
    encounter.  A post-encounter phase is included below because
    the Deep Impact SPICE archive includes a SP-kernel providing
    the trajectory of the flyby spacecraft through 2009 and another
    providing the ephemeris of 9P/Tempel 1 through 2050.
 
 
    THERMAL-VACUUM GROUND CALIBRATIONS (TV1-TV5)
    --------------------------------------------
      Data acquired during ground-based thermal-vacuum tests TV1 through
      TV4 were archived in the PDS.  The science team used these data for
      pre-flight calibration analysis.  TV5 data were not used for science
      calibrations but may be be archived at a future data.
 
 
        TV#   Instruments Tested    Test Period
        ---   --------------------  --------------------
        TV1   HRII                  2002 June-July
        TV2   HRII, HRIV            2002 August-September
        TV3   ITS                   2003 January
        TV4   HRII, HRIV, MRI       2003 February-March
        TV5   HRII, HRIV, MRI, ITS  2004 June-July
 
 
    CRUISE
    ------
      Mission Phase Start Time  : 2005-01-12 (DOY 012)
      Mission Phase Stop Time   : 2005-04-30 (DOY 120, Impact-65 days)
 
      The cruise phase began at the lift-off of the launch vehicle. This
      phase included checkout of the HRII, HRIV, and MRI instruments in
      the second and third days after launch.  Science calibrations began
      shortly after checkout, then were performed approximately once every
      month.  The best sets of data for science calibrations were acquired
      in April, May, and June 2005 and during the post-impact calibration
      in July.  Calibration targets included the Moon, Earth, stars,
      nebulae, and galactic clusters.  Comet 9P/Tempel 1 was not imaged
      for scientific purposes during this phase.  Details of the cruise
      calibrations were discussed in the 'Deep Impact Instrument
      Calibration' paper by Klaasen, et al. (2008) [KLAASENETAL2006].
 
 
    9P ENCOUNTER
    ------------
      Mission Phase Start Time  : 2005-05-01 (DOY 121, Impact-64 days)
      Mission Phase Stop Time   : 2005-07-13 (DOY 194, Impact+9 days)
 
      Scientific data acquisition of comet 9P/Tempel 1 began and ended
      during this phase.  On the approach to the comet, the objectives
      were to determine the size of the nucleus, map the albedo, and
      spectral variations of the surface, determine the rotational state
      of the nucleus, and monitor the activity of the nucleus.  Other
      objectives included identifying large-scale structure in the coma,
      mapping the evolution of the inner coma over a full rotation period,
      and searching for satellites to constrain the mass of the nucleus
      (none were found).  Also, science calibrations were performed in
      early May and June.  During approach, the HRII, HRIV, and MRI
      instruments began acquiring data once every day, then every four
      hours from 7 May through 30 June.  On 1 July, the sampling rate
      changed to every two hours.  About 24 hours before impact, data
      were acquired every hour until about 3 July 20:00 UT, nine hours
      before impact.  Then, data were acquired every 30 minutes until
      ten minutes before impact when the instruments began continuously
      imaging the comet.
 
      During approach, the phase angle of the nucleus
      (sun-comet-spacecraft) increased by about 0.5 degree/day, beginning
      at 28 degrees and reaching 60 degrees at impact minus seven days.
      About three days from impact the HRIV instrument spatially resolved
      the nucleus.  The HRII and MRI instruments did not resolve the
      nucleus until the day before impact.  Due to pointing errors, the
      HRII instrument was not imaging the comet until 20 June.
 
      Twenty-four hours before the scheduled impact, the flyby craft
      released the impactor at a distance of about 864,000 km from the
      comet.  The ITS instrument began acquiring data, and the impactor
      spacecraft transmitted the data over a S-band link to the flyby
      spacecraft.  About 18 hours before impact, a small set of
      calibration data (darks and internal stimulator frames) were
      acquired for each instrument.  The pixel scales of the four
      instruments as a function of time before impact were:
 
                     Pixel Scale (meters/pixel)
             Time     ITS    HRIV   MRI    HRII
            -------  -----  -----  -----  -----
            I-20 hr   7415   1480   7430   7350
            I-1 hr     370     90    460    450
            I-2 s      0.1     17     87     87
 
      The last ITS image was taken at 05:44:29 UT (at the impactor),
      about 5 seconds before impact, with an estimated pixel scale of
      0.5 meters/pixel.
 
      During the impact event, the instruments on the flyby craft
      continuously recorded the development of the crater and start of
      the ejecta flow.  At impact+804 seconds (05:57:58 UT), the flyby
      space craft entered shield mode (SM) where the shields were pointed
      in the direction of the spacecraft's velocity vector to protect the
      instruments from dust impacts during closest approach to the comet.
      During the impact event, pixel scales of the instruments were:
 
                    Pixel Scale (meters/pixel)
             Time     HRIV     MRI     HRII
            --------  ------  ------  ------
            I+1 s       17     86      86
            I+24 s      17     84      84
            I+470 s    7.8     38      39
            I+802 s    1.4      7       7
            SM Entry   n/a    n/a     6.7
 
      The HRIV and MRI instruments stopped imaging immediately before
      shield mode.  HRII continued (smeared) spectral imaging for about
      50 seconds into shield mode.  The flyby spacecraft remained in
      shield mode for about 24 minutes, through closest approach and
      until the dust-impact hazard zone had been passed.  To exit
      shield mode, the spacecraft performed an attitude maneuver over
      several minutes, flipping over and pointing its instruments back
      toward the nucleus.  Once in lookback attitude, the HRIV instrument
      continued to image the impact site for another 12 hours.  The MRI
      and HRII instruments continued to monitor the comet for 60 hours,
      until 6 July 18:17 UT.  During lookback imaging, the pixel scales
      of the instruments were:
 
                     Pixel Scale (meters/pixel)
             Time      HRIV     MRI    HRII    Comments
            --------- ------  ------  ------   -----------------------------
            I+44 m       37     n/a     183    4 Jul 06:28:53 UT, first HRIV
                                               and HRII after SM exit
            I+48 m       42     210     199    4 Jul 06:32:41 UT, first MRI
                                               after SM exit
            I+134 m     146     737     756    4 Jul 07:58 (SM Entry+ 2 h)
            I+734 m     880    4406    4422    5 Jul 17:58 (SM Entry+12 h)
            I+24.24 h   n/a    8810    8826    5 Jul 05:58 (SM Entry+24 h)
            I+36.24 h   n/a   13214   13230    5 Jul 17:58 (SM Entry+36 h)
            I+48.24 h   n/a   17618   17635    6 Jul 05:58 (SM Entry+48 h)
            I+60.24 h   n/a   21950   21968    6 Jul 17:58 (SM Entry+60 h)
 
      At impact, data determined to be less critical were stored in
      the buffer memory of the two processors (A and B) on the flyby
      spacecraft.  During lookback, the flyby craft transmitted these
      stored data back to Earth.  Due to a planning oversight, the memory
      of processor B was not cleared of data before lookback began.  This
      caused some lookback images to never be recorded.  The last science
      calibration started about two days after impact and continued to
      13 July, which concluded the scientific activities of the mission.
 
      Steve Wissler from mission operations at JPL provided the actual
      UTC times for several key events at the flyby and impactor
      spacecraft (s/c):
 
               Flyby Spacecraft Event            Actual UTC at s/c
        -------------------------------------  ---------------------
        Last TCM before impactor release       2005-07-02 23:59:58.3
        Impactor battery activated             2005-07-03 04:57:59.4
        Impactor release                       2005-07-03 05:59:58.3
        Flyby s/c divert maneuver              2005-07-03 06:11:58.3
        Flyby enters shield mode               2005-07-04 05:57:58.3
        Closest approach                       2005-07-04 05:58:58 (planned)
        Flyby s/c turns for look back imaging  2005-07-04 06:24:37.2
 
      The mission operations also provided the actual UTC times for
      several events at the impactor spacecraft:
 
             Impactor Spacecraft Event           Actual UTC at s/c
        -------------------------------------  ---------------------
        Auto-navigation system begins imaging  2005-07-04 03:44:37.7
        1st TCM (burn center)                  2005-07-04 04:13:57.7
        2nd TCM (burn center)                  2005-07-04 05:09:05.8
        3rd TCM (burn center)                  2005-07-04 05:32:06.8
 
 
    9P POST-ENCOUNTER CRUISE
    ------------------------
      Mission Phase Start Time  : 2005-07-13 (DOY 194, Impact+9 days)
      Mission Phase Stop Time   : 2009
 
      In the Deep Impact SPICE archive, the SP-kernel providing the
      trajectory of the flyby spacecraft extends through 2009, and the
      SP-kernel providing the ephemeris of Tempel 1 extends through 2050.
      There are no data from the science instruments for this phase.
 
      Since the flyby spacecraft and its instruments survived the
      encounter with Tempel 1, a trajectory correction maneuver was
      performed on 20 July 2005 to put the spacecraft into an orbit
      for Earth return in late 2007, favoring an extended mission.
      On 9 August 2005, the flyby craft was put into sleep mode.
      On 10 February 2006, an aliveness test was performed on the
      spacecraft.  The results of the wake-up and pointing activities
      indicated it was healthy for an extended mission.
 
 
  Mission Data
  ============
    The following mission-related data are archived at the PDS:
 
    - Pre-launch, thermal-vac calibration (HRII, HRIV, MRI, ITS)
    - Raw science and calibration imaging from flight (HRII, HRIV, MRI,
      and ITS)
    - Reduced science imaging from flight in physical units of radiance
      (uncleaned and cleaned) for HRII, HRIV, MRI, and ITS and cleaned
      I-over-F data for HRIV, MRI, and ITS.
    - Raw and reduced navigation images from flight (HRIV, MRI, ITS)
    - Radio science data from flight
    - SPICE data, including 5-Hz telemetry from the Attitude Determination
      and Control System (ADCS) as a CK kernel
    - Higher-level products, including a shape model and surface
      temperature maps for Tempel 1.
    - Select data from the Earth-based observing campaign
 
  This mission overview was originally paraphrased from A'Hearn, et al.
  (2005) [AHEARNETAL2005B] with permission from the Deep Impact project,
  then revised throughout the mission by the archive team.

PDS4 note: awaiting LID references to facilities and telescopes
- W.M. KECK OBSERVATORY 10-M KECK I RITCHEY-CHRETIEN ALTAZIMUTH REFLECTOR
        