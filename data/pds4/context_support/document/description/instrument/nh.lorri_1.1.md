
 
########################################################################
########################################################################
REQUIRED READING:
- Cheng et al. (2007) [CHENGETAL2007]
- Conard et al. (2005) [CONARDETAL2005]
########################################################################
########################################################################
 
      The LORRI description was was adapted from Conard et al. (2005),
      Cheng et al. (2007),  and the New Horizons website.
 
 
  INSTRUMENT OVERVIEW
  ===================
    The LOng-Range Reconnaissance Imager (LORRI) is an instrument that was
    designed, fabricated, and qualified for the New Horizons mission to
    the outermost planet Pluto, its giant satellite Charon, and the Kuiper
    Belt, which is the vast belt of icy bodies extending roughly from
    Neptune's orbit out to 50 astronomical units (AU). New Horizons is
    being prepared for launch in January 2006 as the inaugural mission in
    NASA's New Frontiers program.
 
 
    SPECIFICATIONS
    --------------
      NAME:                    LORRI (Long-Range Reconnaissance Imager)
      DESCRIPTION:             High-resolution telescope
      PRINCIPAL INVESTIGATOR:  Andy Cheng, APL
      WAVELENGTH RANGE:        350 - 850nm
      FIELD OF VIEW:           5.06 x 5.06 degrees
      ANGULAR RESOLUTION:      0.00494 milliradians
      WAVELENGTH RESOLUTION:   N/A
 
 
    DESCRIPTION
    -----------
      LORRI is a narrow angle (field of view=0.29 deg), high resolution
      (instantaneous field of view = 4.94 urad), Ritchey-Chretien
      telescope with a 20.8 cm diameter primary mirror, a focal length of
      263 cm, and a three lens field-flattening assembly. A 1024 x 1024
      pixel (optically active region), back-thinned, backside-illuminated
      charge-coupled device (CCD) detector (model CCD 47-20 from E2V
      Technologies) is located at the telescope focal plane and is
      operated in standard frame-transfer mode. LORRI does not have any
      color filters; it provides panchromatic imaging over a wide bandpass
      that extends approximately from 350 nm to 850 nm. A unique aspect of
      LORRI is the extreme thermal environment, as the instrument is
      situated inside a near room temperature spacecraft, while pointing
      primarily at cold space. This environment forced the use of a
      silicon carbide optical system, which is designed to maintain focus
      over the operating temperature range without a focus adjustment
      mechanism. Another challenging aspect of the design is that the
      spacecraft will be thruster stabilized (no reaction wheels), which
      places stringent limits on the available exposure time and the
      optical throughput needed to accomplish the high-resolution
      observations required.  LORRI was designed and fabricated by a
      combined effort of The Johns Hopkins University Applied Physics
      Laboratory (APL) and SSG Precision Optronics Incorporated (SSG).
 
      LORRI has four subassemblies in close proximity connected by
      electrical harnesses. These are the optical telescope assembly
      (OTA), the aperture cover door, the associated support electronics
      (ASE), and the focal plane unit (FPU). Except for the door, all are
      mounted inside the spacecraft on its central deck; the door is
      mounted to an external spacecraft panel. LORRI is electronically
      shuttered, with no moving parts aside from the cover door. The ASE
      implements all electrical interfaces between LORRI and the
      spacecraft except for the door control, several spacecraft
      thermistors, and two decontamination heaters. Figure 3 is a block
      diagram of the instrument.  Conard et al. (2005) give a detailed
      description of LORRI design, manufacture and test.
 
 
  Scientific Objectives
  =====================
    Hemispheric panchromatic maps of Pluto and Charon at best resolution
    exceeding 0.5 km/pixel.
 
    Search for atmospheric haze at a vertical resolution <5 km
 
    Long time base of observations, extending over 10 to 12 Pluto rotations
 
    Panchromatic maps of the far-side hemisphere
 
    High resolution panchromatic maps of the terminator region
 
    Panchromatic, wide phase angle coverage of Pluto, Charon, Nix, and
    Hydra
 
    Panchromatic stereo images of Pluto, Charon, Nix, and Hydra
 
    Orbital parameters, bulk parameters of Pluto, Charon, Nix, and Hydra
 
    Search for satellites and rings
 
 
  Calibration
  ===========
    See Cheng et al. (2007).
 
 
  Detectors
  =========
    Frame transfer CCD.  See Cheng et al. (2007) for details.
 
 
  Electronics
  ===========
    LORRI electronics consist of the ASE and FPU. The ASE contains three
    printed circuit cards. These are the low voltage power supply (LVPS),
    the event processor unit (EPU), and the imager input/output (IM I/O).
    The ASE is the primary interface between the spacecraft and the FPU,
    which mounts and controls the CCD. Additional information can be found
    in Conard et al.  (2005).
 
 
  Filters
  =======
    None.
 
 
  Optics
  ======
    The LORRI OTA is a Ritchey-Chretien design, with high system
    throughput required because of the short allowed exposure time and low
    light level at Pluto. The complete LORRI OTA design was evaluated with
    a computer-aided design model including stray light analysis. Specular
    reflections and bidirectional reflectance distribution functions of
    the Aeroglaze Z-306 black paint, primary and secondary mirrors, field
    group optics and focal plane were included in the model. The primary
    and secondary baffle tubes were sized to minimize obscuration and
    suppress direct paths to the FPA's active area. The telescope
    magnification and obscuration were balanced, affecting the optical
    sensitivity and MTF, respectively. Out-of-field stray light was
    evaluated by generating point source transmittance curves with angular
    scans across the boresight in two orthogonal directions (-70 degrees
    to ++70 degrees for each scan) to search for any obscured paths with
    unacceptable amplitude.
 
    See Cheng et al. (2007) for more details.
 
 
  Operational Modes
  =================
    LORRI high-rate image data telemetry APID definitions
 
             C&DH  binning
      APID   side  mode    compression type
 
      0x630    1    1x1    lossless
      0x631    1    1x1    packetized
      0x632    1    1x1    lossy
      0x633    1    4x4    lossless
      0x634    1    4x4    packetized
      0x635    1    4x4    lossy
      0x636    2    1x1    lossless
      0x637    2    1x1    packetized
      0x638    2    1x1    lossy
      0x639    2    4x4    lossless
      0x63A    2    4x4    packetized
      0x63B    2    4x4    lossy
 
 
  Measured Parameters
  ===================
    Radiance.
 
 

        