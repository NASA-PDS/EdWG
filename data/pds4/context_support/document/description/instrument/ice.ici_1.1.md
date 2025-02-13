
 
Instrument Overview
===================
 The Ion Composition Instrument is a novel spectrometer for measuring
 the ionic composition of the solar wind from the ICE (ISEE-C, ISEE3)
 spacecraft.  The resolution and dynamic range of the instrument are
 sufficient to be able to resolve up to twelve individual ions or groups
 of ions.  This will permit the solution of a number of fundamental
 problems related to solar abundances and the formation of the solar
 wind.  The spectrometer is composed of a stigmatic Wien filter and
 hemispherical electrostatic energy analyzer.  The use of curved
 electric field plates in the filter results in a substantial saving of
 weight with respect to a conventional filter of the same resolution and
 angular acceptance.
 
 The spectrometer is controlled by a microprocessor based on a special
 purpose computer which has three modes of operations: full and partial
 survey modes and a search mode.  In the search mode, the instrument
 locks on to the solar wind.  This allows four times the time resolution
 of the full survey mode and yields a full mass spectrum every 12.6 min.
 
SCIENTIFIC OVERVIEW
===================
 
 ION COMPOSITION studies in the solar wind are essential for
 understanding the dynamics and energetics of the solar wind
 acceleration region, and are an important source of solar abundance
 information.  The ion composition of the solar wind is, however, poorly
 known because of the technical difficulties associated with the
 separation of the different ions over the wide dynamic range involved.
 
 With electrostatic energy analyzers, the He+2 /H+ abundance ratio has
 been studied extensively in the solar wind, and large variations found.
 During quiet low-temperature conditions, ions other than H+ and 4He+2
 have been separated with this technique and the presence of heavy ions
 has been demonstrated.  In addition, some information about abundances
 and charge state distributions has been obtained.
 
 The foil collection technique has been used to determine the abundances
 of the isotopes of He, Ne, and Ar in the solar wind. Although this
 method has yielded precise abundance data, its time resolution is
 limited.
 
 The ICE spacecraft will be continuously in the solar wind and thus
 affords an opportunity for a comprehensive uninterrupted composition
 study.  With a continuous record of such a large number of ions,
 fundamental problems concerning the origin of the solar wind and solar
 composition can be investigated. Some of these are discussed below.
 
 1) A number of momentum transfer mechanisms for the acceleration of
 heavy ions into the solar wind have been proposed.  Under the inferred
 conditions in the solar wind source region, coulomb collisions would be
 sufficient to transfer momentum from protons to heavy ions with high
 Z**2/M ratios.  Momentum transfer by waves has also been proposed as an
 efficient mechanism.
 
 To assess the relative importance of the various mechanisms,
 measurements of solar wind ions over a large range of M and Z under
 varying conditions in the corona and solar wind are necessary.
 
 2) Bame et al. (1978) have recently proposed that the He/H ratio of
 0.04-0.05 typically found in fast solar wind streamers be equated with
 the He/H ratio in the outer convective zone of the sun.  This is a
 factor of two lower than the generally accepted value and, if
 correct, would reduce the calculated boron neutrino flux.  A
 comprehensive investigation of the ion abundance variations should lead
 to a better understanding of ion fractionation processes in the solar
 corona, and in turn should yield accurate estimates of the He/H ratio.
 
 3) A correlation between the He/H ratio and solar wind speed has been
 observed but the mechanism is unknown. By extending correlation studies
 to other ions it may be possible to uncover the mechanism.
 
 4) Local temperatures and temperature gradients in the corona can be
 estimated from measurement of the charge distribution of Fe ions and
 the charge states of 0 and Si. To test the validity of the various
 solar wind expansion models, the experimentally derived temperatures
 and gradients can be compared to those derived from the models.
 
 5) An average 4He/3He ratio of 2350 +- 120 has been derived from the
 five Apollo solar wind foil experiments , however, the ratio appears to
 be highly variable.  In one instance, a ratio of 500 was observed over
 a two-day period With the mass spectrometer on ICE (ISEE-C), 3He will
 be continuously monitored, permitting an accurate determination of the
 solar surface abundance of this cosmologically important nucleus. The
 relation between anomalous 3He abundances in the solar wind and the
 small 4 He/3He ratios in some solar flares can also be studied.
 
 
Calibration
===========
 The sensor was calibrated at the test facility of the Physikalisches
 Institut of the University of Bern.  This facility consists of a
 vacuum chamber in which a homogeneous monoenergetic mass separated
 beam of ions can be produced and directed at the sensor mounted on a
 test platform which can be rotated about two axes perpendicular to the
 direction of the ion beam.  Sweep circuits were used to synchronously
 change the voltages on the plates of the filter and analyzer while the
 outputs of each of the three CEM's strobed a multi-channel analyzer
 operating in the pulse-height-analysis mode. Calibrations were
 performed with H2+ and He+ at nominal velocities of 300, 400, 500, and
 600 km/s.  The orientation of the sensor with respect to the incident
 ion beam was changed in small increments over a range of +- 8 degree in
 the horizontal plane and +- 14 degree in the vertical plane.  Angular
 acceptances derived from these functions are in good agreement with
 theory, whereas the experimental resolution always exceeds that
 predicted. The absolute values of the transmission determined at normal
 incidence for H2+ and 4He+ at the four different values of ion velocity
 are in excellent agreement with theory.  The ability of the instrument
 to reject stray ions which create ghost peaks by scattering from the
 outside plates of the analyzer and contribute to the background was
 measured.  In all cases, the ratio of ghost peak counts to counts in
 the main peak was less than 10**-4  with the ghost peaks always
 appearing at energy values 7 percent less than those of the
 corresponding main peaks. Because of the large difference in M/Z
 between 4He and 3He, interference of 4He+2 at the position of the 3He+2
 peak is less than 10**-5 of the 4He signal.
 
 
Operational Considerations
==========================
 The input voltages to the power supplies which provide the potential to
 the electric field plates of the Wien filter and energy analyzer are
 obtained from 12-bit digital-to-analog converters.  The digital
 inputs to the converters come from the microcomputer-based processor.
 The full parameter range covered by the experiment is 300-600 km/s in
 velocity, 840- 11720 eV/Z in energy per charge, and 1.5-5.6 in mass per
 charge.  The velocity range is divided into n steps and the energy
 per charge range into m steps, with both being logarithmically
 related.
 
     V(1s), (n, m) = R1**(m-1)*R2**(n-1)*V1(1,1),    energy analyzer
 
        V(2s),(n) = R2** (n -1)*V2 (1),  Wien filter
 
 1 < n < 24, 1 <m <-40 (15)
 
 where V1s, and V2s, are the digital values of the voltages applied to
 the inputs of the power supplies, V1(1, 1) and V2(1) are the voltages
 for the velocity step n = 1 and the mass step m = 1, and R1 and R2 are
 constants.
 
 There are three modes of operation which are selectable by ground
 command.  In mode 1, m is varied from 1 to 40.  For each value of m, n
 is varied over its complete range.  This mode is useful for surveying
 the solar wind.  In mode 2, minimum and maximum values of m and n are
 chosen, so that only a part of the fuli parameter range is scanned;
 this mode will be for particular MIZ ratio determinations.  Mode 3 is a
 search mode.  The value of n corresponding to the velocity of the solar
 wind is determined by varying n from I to 24 while holding m constant
 at the value corresponding to that for 4 He until the value of n
 corresponding to the maximum counting rate is found.  A scan is then
 made from n = n (solar wind) - 3 to n = n (solar wind) + 3 varying m
 between specified minimum and maximum values.  This mode is intended
 for normal operations, as it yields the most data per unit time.  In
 general, after each spin of the spacecraft a step is taken, but
 provisions have been made for holding a step for s = 2, 4, or 8
 rotations of the spacecraft.
 
 The telemetry contains details of the mode, specified by the values of
 VI(l, 1), V2(l), mmin, mmax, nmin, nmax, s, R1, R2, and the counts from
 each of the detectors (separately logarithmically compressed above
 127) for the corresponding values of m and n. At the minimum time
 resolution, a spectrum is obtained every 24 X 40 X 3 s (spin period = 3
 s), or 48 min. Use of the search mode reduces this to approximately 12
 X 3 + 6 X 40 X 3 s = 12 min, 36 s.
 
 
Detectors
=========
 The basic requirements of the instrument were that it be capable of
 measuring ionic abundances over the M/Z range of 1.5-5.6 (3He+2 -
 56Fe+10) at velocities from 300 to 600 km/s. To keep the dynamic range
 near 1x10**4 , H+ is not measured. The geometric factor g of the
 instrument is related to the ion flux F and count rate N by
              g = N/F                                       (1)
 In order that N be at least one count per second for the least abundant
 ion species under consideration, g must be of order 10**-3 cm2. The
 dimensions of the apertures and angular acceptances in the plane of
 the spacecraft rotation and perpendicular to it determine g. The
 combination of a Wien filter and an electrostatic energy analyzer is a
 well-known means for determining the velocity and the energy per charge
 and, hence, the mass per charge of ions.  Low resolution mass
 spectrometers of this type have been flown in the solar wind  and in
 the inner magnetosphere.
 
 The spherical electrostatic energy analyzer is of conventional design.
 Care was taken to insure that the height and spacing of the plates were
 sufficient to accommodate the maximum angular divergence of entering
 ions; the analyzer constant is 5.86 eV/V, and its energy resolution is
 50.  With this design, the energy analyzer will transmit virtually all
 ions at the tuned energy independent of the angle with which they leave
 the Wien filter and enter the analyzer.  It was thus assumed that the
 transmission function for the tuned analyzer is unity.
 
 
Filters
=======
 It has been shown that the Wien filter can be made to focus along the
 direction of the magnetic field as well; as perpendicular to it by
 using cylindrical electrical plates. When this is done, the focusing
 length will be longer than for the parallel plate filter by a factor of
 2**-1/2 however, the height of the filter can be reduced by up to a
 factor of 2. The result is a filter with volume and approximate
 weight 2**-1/2 that of a conventional filter of comparable resolution
 and geometric factor.  Three important parameters are 1) Ion Optics; 2)
 Transmission Properties; 3) Velocity Resolution; and 4) Angular
 Acceptance.
 
 
Measured Parameters
===================
 
 The table below details a description of the Wien filter and energy
 analyzer parameters.  An approximation to the geometric factor is
 
    g = s * h * T * (delta alpha) (1/2)/180        (14)
 
 where s and h are the width and height of the Wien filter entrance
 aperture, (delta alpha) (1/2) is the acceptance angle in the x-z plane,
 and T is the transmission.  Using the data from Coplan et al. (1978)
 Table II at a speed of 450 km/s, g is typically 1.7 x 10**-3 CM**2 for
 3He and 4x 10**-4 CM**2  for the Fe ions, results which are close to
 the design goal.  To achieve the theoretical resolution, the magnetic
 field in the working gap of the Wien filter was made homogeneous to
 better than +-l percent by the use of shaped pole pieces.  The magnets
 used are sintered samarium cobalt, and a contoured yoke of vanadium
 pennendur provides a flux path for the internal magnetic field and
 serves as the principal structural element of the filter.  To reduce
 the joint area (which contributes to flux leakage), the yoke was fabri-
 cated with only one open end.  A shield of high permeability material
 further attenuates the external magnetic field to acceptable levels.
 The electric field in the Wien filter is produced by plates of gold
 plated aluminum with shims on top and bottom of each to correct for
 fringing fields.  The plates of the electrostatic analyzer were
 roughened and plated with copper sulfide black in order to reduce ion
 scattering and UV reflectivity.  A grounded high-transmission grid
 covers the exit aperture to reduce field distortion inside the
 analyzer.
 
 Ions leaving the exit aperture of the analyzer are detected by
 three identical channeltron electron multipliers (CEM's)
 mounted on ceramic circuit boards which also contain pre-
 amplifiers and discriminators.  The multipliers are operated in
 the saturated pulse mode and the discriminators are set at a
 level corresponding to approximately 10**-13 C of charge per
 pulse.
 
 A grid, maintained at the potential of the CEM input, is placed
 directly in front of the detectors to increase counting efficiency by
 ensuring that all secondary electrons are collected.  The relative
 count rates in each of the detectors depend on the angular
 distribution of the ions entering the filter and can be used to obtain
 the direction of the bulk motion of each species and some temperature
 information.  Counts are only registered during 12 percent of the spin
 period of 3 s, giving a total background count rate of 0.02 per spin
 period. By comparison, the count rate for each of the Fe charge states
 (flux, 3 X 10**3 CM**-2 S**-1  ; geometric factor, 4 X 10**-4 CM**2) i
 s estimated to be 4 counts per spin period.
 
                               TABLE
                        INSTRUMENT PARAMETERS
 
    Wier, Filter (Stigmatic)
    Working Gap Length                                    180 mm
    Working Gap Cross-Section                             11 mm 33 mm
    Average Magnetic Field                                0.1454 W/m**2
    Zero equipotential Radius of Curvature in (x,y)-plane 30.8 mm
    Entrance nd Exit Aperture Dimensions                  2 mm X 15 mm
    Transmission                                          26-50%
    Resolution (V(0)/delta V)                             20-30
    Angular acceptance in ecliptic plane                  0.5 - 3.6 deg
    Angular acceptance vertical to ecliptic plane         3 - 12 deg
    Weight                                                2.7 kg
 
    Electrostatic Energy Analyzer (spherical)
    Radius of zero equipotential                          50.0 mm
    Radius of outer plate                                 54.7 mm
    Radius of inner plate                                 46.1 mm
    Sector Angle                                          167 deg
    Entrance and exit aperture dl-nsi.ns                  2 mm x 15 mm
    Resolution (EIAE)                                     50
    Weight                                                0.178 kg
 
    Massspctrometer (Filter and Analyzer)
    Range                                                 3He - Fe
    Dynamic range                                         10**4 - 10**5
    Overall gemtric factor                    4x10**-4 - 1.7x10**-3 CM**2
 
    Weight of sensor (without electronics)                4.ZB kg
    Total weight of instrument                            5.6 kg
 

        