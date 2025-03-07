
      Instrument Overview
      ===================
      The instrument is a photometer-polarimeter which views along the spin-
      axis of the spacecraft.  Unlike most other instruments on Giotto which
      view in the ram direction, OPE views in the anti-ram direction, i.e. in
      the direction from which the spacecraft has come.  It thus measures the
      integral brightness along the track as a function of position along the
      track.  The derivative of this signal is, therefore, the polarized
      emissivity at each point of the track.
 
      The instrument has no moving parts.  An f/1.7 objective of 18-mm
      diameter images the 'sky' onto a field stop with an effective field of
      view of 3 degrees.  The seven interference filters to isolate various
      spectral regions are deposited in a mosaic directly on the front
      element of the objective and the linearly polarized foil is sandwiched
      between the elements of the objective.  Immediately behind the field
      stop, a field lens reimages the objective and its mosaic of filters
      onto a micro-channel plate.  The micro-channel plate provides anodes
      for each of the seven filters.  The mosaic of filters is laid out in
      such a way as to provide approximately equal output signals in each
      bandpass and to partially correct for aberrations of the optical
      system.  Polarization is measured by the rotation of the spacecraft
      (which rotates the linearly polarized foil together with the whole
      instrument) at 15 RPM.  This allows determination of the first three
      Stokes parameters once every 2 seconds (once every half rotation).
      The data are sampled every 0.5 seconds, i.e., every 45 degrees of
      spacecraft (polaroid) rotation.
 
      The instrument is mounted on the top platform of the Giotto spacecraft,
      near the periphery of the spacecraft where it is in the shadow of the
      solar panels and can see past the de-spun high-gain antenna.  The
      instrument is baffled against stray light from the coma outside the
      field of view and against light reflected from the high-gain antenna
      or the tripod.  The baffle is 270 mm long with 7 vanes.  A
      self-luminescent white source is mounted on the back of the baffle
      cover for testing and calibration during the cruise phase.  This
      baffle cover was ejected by a pyrotechnic device in October 1985.
 
      Instrument Manufacturer : Service d'Aeronomie du CNRS, Verrieres le
                                Buisson, France
      Instrument Mass	        : 1.32  <kg>
 
      Science Objectives
      ==================
      - Determine the changes in both number density (including inhomogen-
        eities) and the grain-size distribution as a function of Giotto's
        position inside the coma.
      - Determine the spatial distribution along the trajectory of emissions
        due to OH, CN, C2, and CO+, in order to derive the production rates
        of the parent species, as well as their nature, and to obtain
        information on the physical processes leading to the formation of
        the observed radicals by means of the study of the polarization of
        their emission as a function of distance from the nucleus.
      - Investigate the dynamical coupling of gas and dust by determining
        the gas-to-dust mass production ratio as a function of distance from
        the nucleus and the possible correlation with grain size.
      - Compare the optical properties of cometary dust with those of
        interplanetary and interstellar grains in an effort to understand the
        histories and mutual interactions of all three dust complexes.
 
      Calibration Description
      =======================
      The pre-flight calibration was carried out primarily at the Max-Planck-
      Insitut-fuer-Astronomie in Heidelberg.  The linearity of each of the
      seven channels was calibrated by a boot-strap method, starting with two
      incident light signals, C1 and C2, of comparable intensity and
      comparing the output of the sum of the two signals, C3, with the sum of
      the outputs for the two separate signals. The Intensity-Linearity-Ratio
      (ILR) for the counting level (C1+C2)/2 is then given by C3/(C1+C2).
      The results of a series of measurements on each channel were fitted by
      least squares and the resultant curves were used to calibrate the data.
 
      Cross-talk between the channels, which could arise either from optical
      scattering within the filters or misalignment of the optics with the
      detector or electronic cross-talk, was measured with a beam from a
      monochromator having a spectral width of approximately 0.1nm.  The
      response of each channel of the instrument was recorded at a variety
      of wavelengths.  The results were integrated across each bandpass and
      compared with the integrated signal received in the out-of-bandpass
      channels.  The out-of-band and in-band counts were corrected by
      applying a preliminary ILR derived as a composite of all channels.  The
      signals determined in this way were used to determine the preliminary
      crosstalk.  This procedure was iterated until it converged.  The final
      cross-talk was found to be less than 3%.
 
      A final calibration was obtained on the background sky, zodiacal light
      plus diffuse starlight, immediately prior to the encounter.
 
      General steps in going from raw counts to flux include the following:
 
       0. Correct for non-linearity (this correction is completely
          negligible for Halley far from the encounter).   It is small for
          Halley at closest approach (where signals are strongest) compared
          to other uncertainties.
       1. Take dark current from same clock-sector reading and multiply by
          ratios of areas (obs channel/dark channel) on the MCP and subtract
       2. Estimate scattered light, as a function of clock-sector, from the
          observations before and after encounter.
       3. Correct for cross-talk between channels using matrix in Giovane et
          al., 1991.
       4. For CO+ channel, multiply by absolute inverse responsivity.
       5. For other channels, either add clock sectors separated by 90
          degrees or  multiply by two (very approximate), to go from the
          polarized intensity to total intensity.
 
      Operational Considerations
      ==========================
      During the flythrough of Halley's coma, the instrument was pointed in
      the direction opposite the direction of motion.  Direct differentiation
      of the signal, with a full measurement every two seconds, should
      lead to the mean polarized emissivity in a cylinder of length about
      137 km (2 seconds of travel) and diameter 6 km (2.62 deg field of
      view at a distance of 137 km).  During the entire encounter with
      Halley, the scattering angle was 107.2 degrees.
 
      Although the instrument was not damaged during the encounter, the
      viewing direction after a dust particle impacted Giotto was not anymore
      parallel to the direction of motion, and not well determined, and thus
      the data could not be analyzed.
 
      Measurements were performed every 45 degrees in rotational phase.
      Only five phases gave a usable signal; these phases can readily be
      identified in the data tables by the chronology of the cometocentric
      distance: each geometrical configuration repeats itself every 4 sec
      or every 274 km along the spacecraft track.
 
      Due to the strength of the underlying continuum signal in the CO+
      filter, the weak CO+ emission was not truly detected and that channel
      can be considred as another continuum channel.
 
      Detectors
      =========
      Detector ID                    : OPE
      Detector type                  : Micro-Channel Plate
 
      Filters (see Giovane etal, 1991)
      ===============================================
      Continuum 1 Filter
      ------------------
      Center Filter Wavelength	: 0.4423 micron
        Interference filter with bandwidth at 50% of peak = 0.0047 microns
        and bandwidth at 1% of peak = 0.0090 microns. Peak transmission of
        0.46.
 
      Continuum 2 Filter
      ------------------
      Center Filter Wavelength	: 0.5771 micron
        Interference filter with bandwidth at 50% of peak = 0.0098 microns
        and bandwidth at 1% of peak = 0.0090 microns. Peak transmission of
        0.73.
 
      Continuum 3 Filter
      ------------------
      Center Filter Wavelength	: 0.7175 micron
        Interference filter with bandwidth at 50% of peak = 0.0034 microns
        and bandwidth at 1% of peak = 0.0075 microns. Peak transmission of
        0.39.
 
      OH Filter
      ---------
      Center Filter Wavelength	: 0.3113 micron
        Interference filter with bandwidth at 50% of peak = 0.0054 microns
        and bandwidth at 1% of peak = 0.0100 microns.Peak transmission of
        0.23.
 
      CN Filter
      ---------
      Center Filter Wavelength	: 0.3875 micron
        Interference filter with bandwidth at 50% of peak = 0.0037 microns
        and bandwidth at 1% of peak = 0.0100 microns. Peak transmission of
        0.37.
 
      CO+ Filter
      ----------
      Center Filter Wavelength	: 0.4249 micron
        Interference filter with bandwidth at 50% of peak = 0.0036 microns
        and bandwidth at 1% of peak = 0.0080 microns. Peak transmission of
        0.51.
 
      C2 Filter
      ---------
      Center Filter Wavelength	: 0.5145 micron
        Interference filter with bandwidth at 50% of peak = 0.0036 microns
        and bandwidth at 1% of peak = 0.0060 microns.Peak transmission of
        0.70.
 
 
      Optics
      ======
      Telescope Focal Length	       : 0.0306 m
      Telescope Diameter             : 0.018 m
      Telescope F Number             :  1.7
 
 
      Platform Mounting Description
      =============================
      The instrument is mounted on the top platform of the Giotto spacecraft,
      near the periphery of the spacecraft where it is in the shadow of the
      solar panels and can see past the de-spun high-gain antenna.  It views
      parallel to the spin axis.  At the encounter with P/Halley, this is the
      direction opposite the ram direction.
 
 
      Instrument Section Description
      ==============================
      Section ID   : OPE
      Data Rate    : 723 bits/sec
      FOV Shape    : CIRCULAR

        