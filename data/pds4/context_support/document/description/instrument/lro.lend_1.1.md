
 
 
  Instrument Overview
  ===================
    The Lunar Exploration Neutron Detector, LEND, was designed and
    built by P.I. Igor Mitrofanov at the Russian Space Institute for
    incorporation into NASA's Lunar Reconnaissance Orbiter (LRO) as
    a large orbital neutron telescope for mapping the Moon's neutron
    albedo. LEND is the follow-on instrument from the High Energy
    Neutron Detector (HEND) onboard Mars Odyssey, although LEND
    incorporates a set of collimated detectors to improve spatial
    resolution. The methods and procedures of LEND data processing
    and analysis are based on existing procedures that have been
    developed for analysis of HEND data.
 
    The LEND instrument is based on the registration of secondary
    neutrons from the Moon, which are created in the upper 1-2 meters
    of lunar regolith which is irradiated by cosmic rays. Neutrons
    of high energy are born in the regolith and then slowed down and
    absorbed by nuclei of the major elements in the regolith through
    inelastic scattering and capture. The neutron
    flux coming out of the regolith depends upon the composition of
    the regolith, and is strongly affected by the presence of hydrogen
    or its compounds. When colliding with a hydrogen nucleus, a
    neutron losses half of its energy which leads to fast
    thermalization, thus to a significant increase of the flux of
    thermal neutrons and reduction in the flux of the epithermal
    neutrons. The orbital flux of epithermal neutrons depeds upon
    the hydrogen content of the regolith.
 
    Usage of different methods of neutron spectrometry allows us to
    obtain the average hydrogen or water ice content along with
    estimates of thickness of the ice cover due to comparison of
    counting rates of neutrons having different energies. The flux of
    epithermal neutrons and the flux of fast neutrons depend upon the
    thickness of water ice on the Lunar surface.
 
    LEND has eight 3He sensors for detecting thermal and epithermal
    neutrons. Four of the 3He sensors un-collimated and four are
    collimated. The external sensors STN1-3 (Sensor Thermal Neutrons)
    and SETN (Sensor EpiThermal Neutrons) are the un-collimated
    sensors that detect thermal and epithermal neutrons. STN-3 and
    SETN both have open fields of view. The combination of these two
    sensors will allow the measurement of local density of thermal and
    epithermal neutrons around the spacecraft. STN 1 and 2 are located
    near the midpoint of the instrument and have the thick mass of the
    collimation module just between them. For sensors on the +X and -X
    sides, the collimation material absorbs all external particles
    coming from directions -X and +X, respectively. The velocity
    vector of LRO will correspond to one of these directions:
    therefore, sensors STN 1 and 2 will detect neutrons with
    velocities (Vn + Vorb) and (Vn - Vorb), respectively, and will
    operate as a Doppler filter to separate the flux of external
    neutrons from the Moon from the local spacecraft background. The
    full set of four sensors, SETN and STN 1-3, will provide the data
    to characterize the neutron component of lunar radiation
    background at the altitude of LRO separately from the neutron
    component of local background produced by LRO itself.
 
    The collimated sensors of epithermal neutrons, CSETN1-4, are also
    3He counters, that are installed inside the collimating module,
    which effectively absorbs external neutrons outside of instrument
    Field of View. Absorbing neutrons is very difficult; one of the
    best absorbing materials is 10B, and its absorption efficiency
    becomes much higher when neutrons are slower. The LEND
    collimators have external layers of polyethylene for moderation
    of impacting neutrons and internal layers of 10B for their
    efficiency. These sensors are also enclosed by Cd shields that
    absorb all neutrons with energies below ~0.4 eV, which mainly
    correspond to thermal neutrons. The neutron collimator provides
    the instrument Field of View (FOV): epithermal neutrons of direct
    flux inside the FOV are recorded by the detector, while the
    majority of neutrons outside the FOV are absorbed by the
    collimator. This collimation technique provides mapping of
    epithermal neutrons from the Moon's surface with the horizontal
    resolution of 5 km for LRO at an altitude of 50 km.
 
    The final LEND sensor is the Sensor for High Energy Neutrons
    (SHEN), which is a stilbene scintillator that produces a
    flash of light each time a high energy neutron in the energy
    range 0.3 to 15.0 MeV collides with a hydrogen nucleus and
    creates a recoil proton. Special shape-sensitive electronics
    distinguish proton counts from electron counts, and an active
    anti-coincidence shield eliminates external charged particles.
    This sensor is installed inside the central hole of the
    collimation unit, and its Field of View corresponds to
    40-degree (HWHM). The SHEN sensor outputs data in 16 energy
    channels from 300 keV to more than 15 MeV, and is the source
    of the SC1-3 spectra.
 
    For further information about the LEND instrument and the
    LEND experiment please see MITROFANOVETAL2008].
 
 
  Scientific Objectives
  =====================
    The science objectives of neutron mapping of the Moon are
    outlined by three investigation tasks developed by the
    LRO team.
 
    Task (1) is to explain the origin of the neutron flux depressions
    in the lunar polar regions, which could be produced by enhancement
    of implanted hydrogen from the solar wind, or by accumulated
    deposits of water ice from comet impacts in shadowed craters.
 
    Task (2) focuses on the variation of hydrogen content at moderate
    latitudes of the Moon in comparison to surface variations of
    minerals, thermal conductivity and soil maturity.
 
    Task (3) corresponds to the measurement of neutrons over a broad
    energy range from thermal energies up to tens of MeV to determine
    the neutron contribution to the total radiation dose at an altitude
    of 50 km above the Moon.
 
    The Lunar Exploration Neutron Detector (LEND) will sddress these
    tasks by:
 
    Creating high resolution Hydrogen distribution maps with
    sensitivity of about 100 ppm of Hydrogen weight and horizontal
    spatial resolution of 5 km.
 
    Characterizing surface distribution and column density of
    possible near-surface water ice deposits in the Moon's polar
    cold traps.
 
    Creating a global model of neutron component of space
    radiation at altitude of 30-50 km above Moon's surface with
    spatial resolution of 20-50 km at the spectral range from
    thermal energies up to 15 MeV.
 
 
  Calibration
  ===========
    Calibration information for the LEND instrument is provided
    in the LEND Calibration Report
    (calib/LEND_calibration_report.pdf).
 
 
  Operational Modes
  =================
    LEND operates autonomously, collecting data throughout the
    lunar orbit. LEND generates approximately 0.26 Gbits of
    measurement data per day. In order to perform early calibration
    measurements, LEND became active shortly after the first mid
    course correction (MCC) burn. Operationally, LEND is simple and
    has only three instrument modes: MEASUREMENTS, STAND-BY, and
    OFF. While in MEASUREMENTS mode, instrument electronics and
    detector high voltage are both 'on' and the instrument
    generates measurement and housekeeping data. In STAND-BY mode,
    instrument electronics are 'on', detector high voltage is 'off',
    and only housekeeping data are generated. While in OFF mode,
    the instrument is 'off', the instrument external heater is
    'on', and only external temperature data are generated.

        