
 
  Instrument Host Overview
  ========================
    The Deep Impact Impactor vehicle was a complete spacecraft with a
    CCD-based camera and telescope called the Impactor Targeting Sensor
    (ITS) for both scientific imaging and auto-navigation; a complete
    attitude control subsystem using hemispherical resonator gyros; a star
    tracker; and a complete, hydrazine-based propulsion system.
    Electrical power was supplied by an internal battery since the
    expected operating lifetime was very short (24 hours).
 
    The impactor was mechanically and electrically attached to the flyby
    spacecraft and both launched together.  They flew together until one
    day before the impact event.  On July 3, 2005, the impactor was
    released and gently pushed away from the flyby craft at a distance of
    about 864,000 km from comet Tempel 1.  The auto-navigation system took
    control and maneuvered the impactor to ensure an impact on an
    illuminated portion of the cometary nucleus.  On July 4, 2005, the
    impactor hit the nucleus at a relative speed of 10.3 km/s.  The 360-kg
    Impactor released 19 gigajoules of kinetic energy to excavate a crater
    on the surface of the nucleus.  The best estimate of the time of
    the impact was 05:44:34.200 UT (at the impactor spacecraft,
    Earth-received time 05:52:00 UT).
 
    About half of the mass of the impactor was copper, a noble metal,
    which minimized chemical reactions that could lead to species that
    might contaminate the spectrum with bright lines.  About half this
    copper was in a spherical cap at the 'front' of the impactor.  This cap
    was made of chambered discs that were internally hollowed, much like a
    lightweight telescope mirror, to reduce the density by a factor two or
    so from the bulk density of copper.
 
    Data taken by the ITS were white-light images and were used by the
    on-board software for auto-navigation and transmitted to the flyby
    craft over an S-band link at 64 kilobits per seconds (kbps).  Attitude
    control and minor trajectory corrections were performed using a small
    hydrazine propulsion subsystem.
 
    Some of the last ITS frames taken before impact were blurred due to
    dust hits.  Analysis of ITS data show a slight degradation of the
    amount of light received by the CCD, apparently caused by the
    sandblasting of the optics by small particles.  The last ITS image
    was taken a few seconds before impact.
 
    The system requirement specifications for the impactor were:
 
      Image Data Volume       : Approximately 17 megabytes
      Pointing Accuracy       : 2 milliradian 3-sigma
      Pointing Knowledge      : 150 microradian, 3 axes, 3-sigma
      Targeting Accuracy      : 300 m 3-sigma with respect to the
                                center of brightness of the nucleus
      Telecom Band            : S-Band
      Data Rate to Flyby      : 64 kbps
      Command Rate            : 16 kbps
      Energy Storage          : 2.8 kilowatt-hr for 24 hr mission
      Propulsion              : 25 m/s delta-velocity
 
 
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
 
 
  Recommended Reading
  ===================
    For a detailed descriptions of the impactor spacecraft and
    auto-navigation, see A'Hearn, et al. (2005) [AHEARNETAL2005B],
    Blume (2005) [BLUME2005], Hampton, et al. (2005) [HAMPTONETAL2005],
    and Mastrodemos, et al. (2005) [MASTRODEMOSETAL2005].
 
    For information about the anticipated flight data and the cratering
    experiment, see Klaasen, et al. (2005) [KLAASENETAL2005],
    Richardson, et al. (2005) [RICHARDSONETAL2005], and Schultz and Ernst
    (2005) [SCHULTZ&ERNST2005].  Initial results from the mission were
    presented by A'Hearn, et al. (2005) [AHEARNETAL2005A].
 
  This instrument host description was provided by Dr. Michael A'Hearn,
  the principal investigator for the Deep Impact mission.

        