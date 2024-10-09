
 
  Abstract:
  =========
   Mini-RF is a side-looking synthetic aperture radar (SAR) instrument that
   is flying on the Chandrayaan-1 spacecraft.  Chandrayaan-1 is an
   Indian Space Research Organisation (ISRO) lunar orbiter.
 
   Mini-RF operates in two modes, SAR mode and a nadir-looking
   scatterometry mode.
 
  Scientific Objectives:
  ======================
   The primary scientific objectives of the Mini-RF Forerunner mission
   is to search for water-ice deposits in the north and south polar
   regions of the Moon.  It will search for anomalous radar reflectivity
   signatures (high albedo and high circular polarization ratio) that can
   differentiate volumetric water-ice deposits from the more typical
   anhydrous lunar surface material.
 
   As an additional scientific objective, the Mini-RF mission will
   characterize the lunar surface roughness at radar wavelength scales.
 
 
  Calibration:
  ============
   Amplitude calibration
   ---------------------
   The Mini-RF radar data product is comprised of the amplitude
   (or magnitude squared) of the H and the V channels of the
   dual-polarized receiver, and also the cross-product of the complex
   H and V amplitudes. These data are necessary and sufficient to form
   the 2x2 coherency matrix of the backscattered field, which is
   alternatively represented by the Stokes parameters, four real numbers.
   The first Stokes parameter represents the total backscattered power. This
   can be scaled to the normalized reflectivity sigma-zero only if the
   end-to-end transformation of the radar is calibrated absolutely. The
   starting point for this scaling is the set of pre-flight system data,
   coupled with in-flight specifics such as incidence and altitude. During
   the mission, absolute calibration will be up-dated by imaging a lunar
   area whose reflectivity is well known from Earth-based radar
   observatories. However, most lunar science measurements depend on ratios
   of the Stokes parameters, for which absolute amplitude calibration is not
   required. Rather, gain balance between the H and the V channels is the
   key objective. Relative calibration consists of evaluating the corrective
   scaling constant of the H amplitude relative to the V amplitude.
   Calibration references (noise, tone, and chirp) are included at the
   beginning and end of each data take to assist relative amplitude
   calibration. During the mission, relative calibration will be up-dated by
   radar coverage of the lunar surface at nadir, from which the observed
   backscatter should have identical amplitudes seen through both the H and
   the V channels. Any difference can be inverted to evaluate the relative
   amplitude calibration constant. In addition, the mission plan calls for
   relative amplitude calibration through a cooperative transmission and
   reception between the spacecraft and an Earth-based radar observatory.
   These data will be posted on the PDS when available. (If more specific
   information is needed, please consult the Mini-RF Calibration Plan
   [MCKERRACHERETAL2010].)
 
   Phase calibration
   -----------------
   The Mini-RF radar data product is comprised of the amplitude
   (or magnitude squared) of the H and the V channels of the dual-polarized
   receiver, and also the cross-product of the complex H and V amplitudes.
   The cross-product is one representation of the phase to be calibrated.
   These data are necessary and sufficient to form the 2x2 coherency matrix
   of the backscattered field, which is alternatively represented by the
   Stokes parameters, four real numbers. The first Stokes parameter is the
   total backscattered power (see Amplitude Calibration). Under the
   operational assumption that the radar transmits circular polarization,
   the relative phase (in the cross-product) is central to the third and the
   fourth Stokes parameter. Relative phase calibration consists of
   evaluating the corrective phase rotation constant of the H complex
   amplitude relative to the V complex amplitude such that the average phase
   difference between them is +/-90 degrees (whose sign depends on whether
   right- or left-circular polarization was transmitted) under the condition
   that the average reflecting surface is specular. The starting position
   for relative phase calibration is the set of pre-flight system data,
   coupled with in-flight measurements based on the radar's calibration
   references (see Amplitude Calibration).  During the mission, relative
   phase calibration will be up-dated by radar coverage of the lunar
   surface at nadir, from which the observed averaged backscatter should
   have known relative phase between the H and the V channels. Any
   difference can be inverted to evaluate the relative phase rotation
   calibration constant. In addition, the mission plan calls for relative
   phase calibration through a cooperative transmission and reception
   between the spacecraft and an Earth-based radar observatory. These data
   will be posted on the PDS when available. (If more specific information
   is needed, please consult the Mini-RF Calibration Plan.)
 
 
  Operational Modes:
  ===========================
 
    The Mini-RF instrument has two modes: SAR and Scatterometry.
 
  Sensors:
  ==========
  The radar is to prove the feasibility of a 10-kg class instrument in lunar
  orbit to support high-quality imaging data collection.
 
  Electronics:
  ============
   The Mini-RF assembly consists of two sections, the antenna (a passive
   array of H and V elements, of about 1 square meter area), and electronics
   (packaged in three individual sub-assemblies).

        