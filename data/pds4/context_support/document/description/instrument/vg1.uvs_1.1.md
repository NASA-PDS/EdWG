
 
    INSTRUMENT: ULTRAVIOLET SPECTROMETER
    SPACECRAFT: VOYAGER 1 & 2
 
 
    Instrument Information
    ======================
      Instrument Id                  : UVS
      Instrument Host Id             : { VG1, VG2 }
      Pi PDS User Id                 : ALBROADFOOT
      Instrument Name                : ULTRAVIOLET SPECTROMETER
      Instrument Type                : ULTRAVIOLET SPECTROMETER
      Build Date                     : N/A
      Instrument Mass                : 4.52
      Instrument Length              : 43.18
      Instrument Width               : 14.78
      Instrument Height              : 17.15
      Instrument Serial Number       : 3
      Instrument Manufacturer Name   : N/A
 
 
    Instrument Description
    ======================
      The Voyager 1 and 2 Ultraviolet Spectrometers are nearly
      identical instruments.  This discussion applies to both, except
      in a few instances in which important differences between the
      two are noted explicitly.  The Voyager 1 Ultraviolet
      Spectrometer (UVS) is a compact Wadsworth mounted objective
      grating spectrometer that covers the wavelength range of 0.0535
      to 0.1702 micron (0.0513 to 0.1680 micron for the Voyager 2
      UVS).  It records the entire spectrum within this range in a
      single exposure.  It has no moving parts.  A mechanical
      'collimator' consisting of a series of 13 aperture plates
      defines the main 'airglow' field of view (FOV) of 0.10 degrees
      degrees full-width-half-maximum (FWHM) x 0.87 degrees in length.
      Light passing through the collimator strikes the concave
      diffraction grating at near normal incidence.  The grating
      disperses and focuses light onto a 1-d array detector that
      records individual photoevents.  An auxiliary field of view for
      solar occultation experiments is offset 20 degrees from the
      airglow field by a small mirror near the front of the
      collimator. Using this 'occultation port', the UVS can view the
      Sun without pointing the main field, and those of other
      coaligned instruments, directly at the Sun.  The occultation
      field is 0.25 FWHM x 0.87 degrees.  A sunshade prevents
      illumination of the main entrance aperture by the sun during
      occultation observations.
 
      The UVS has two spectral resolutions depending on the nature of
      the source.  An extended monochromatic source that fills the
      FOV ideally produces a triangular intensity distribution of 0.1
      degree FWHM.  (The actual response function is slightly rounded
      at the top and base, but a triangle is a satisfactory
      approximation for most applications.) The 0.1 degree
      corresponds to width of 3.5 anodes, or 0.0033 microns.  This
      inherent spectral resolution may often be improved by spectral
      analysis.  A monochromatic point source is imaged onto a width
      of about 1 anode for a practical resolution of about 0.0015
      microns.  Precise measurements of the relative response as a
      function of position within the FOV have been made by rastering
      the FOV across a star.  At wavelengths longward of 0.1350
      microns there is a slight (~10%) asymmetry in the response on
      either side of the center of the FOV.
 
      The effective sizes of the entrance apertures are (airglow
      port) 21.2 and (occultation port) 0.75 cm**2.
 
      The anode array is scanned at a rate of 3125 scans per second
      and the results are added into an internal memory.  The UVS
      transmits the contents of this memory to the flight data system
      (FDS) on command of the FDS.  The FDS retrieves values for a
      pair of channels each 5 msec, and so reads a complete spectrum
      from the UVS in 0.32 sec.  For the fastest transmitted data
      rate (OC-1, see below) used for occultation observations, this
      readout proceeds continuously, producing a series of spectra
      separated by 0.32 sec.  For lower data rates, the memory is
      read in bursts of 0.32 sec separated by the appropriate
      intervals.  During these intervals, the UVS integrates the
      spectrum in its internal memory.  As the data is transferred to
      the FDS it is logarithmically compressed from 16 to 10 bits.
 
      The FDS determines the rate at which spectra are read from the
      UVS after being integrated internally in the instrument memory.
      Most planetary observations are made at one of two data rates,
      OC-1 (0.32 sec spectra, for occultation measurements) and GS-3
      (3.84 sec spectra, for emission spectroscopy).  Slower rates
      are used from time to time.  Rates and their designations are:
 
          Name            Mode #           Integration time (sec)
            OC-1            1                0.32
            GS-3            2                3.84
            CR-1            3                12
            CR-2            4                48
            CR-4            6                192
            CR-6            8                720
            CR-5T           9                240
            UV-5A           10               3.84
 
      A description of the UVS investigation is given by
      [BROADFOOTETAL1977].  Performance and analysis techniques are
      described by [BROADFOOTETAL1981].
 
 
    Scientific Objectives
    =====================
      The primary goal of the UVS is to study the composition and
      structure of the atmospheres of the outer planets and their
      satellites.  Secondary goals include the study of
      magnetospheric particle populations, magnetosphere-atmosphere
      interactions, the composition and distribution of the
      interplanetary wind, determinations of the solar flux, and
      stellar astronomy.
 
 
    Operational Considerations
    ==========================
      The Voyager UVS instruments have operated nearly continuously
      since launch in 1977.  With the singular exception of a
      decrease in the Voyager 1 microchannel plates (MCP) gain, due
      to a high radiation-induced count rate during passage through
      the inner Jovian magnetosphere, both instruments have remained
      photometrically stable at a better than 3% level since 1977.
      In-flight performance of the UVS from launch through the 1979
      Jupiter encounters is reviewed in [BROADFOOTETAL1981] and an up
      to date description of astronomical observations is contained
      in [HOLBERG1990] and [LINICK&HOLBERG1991].
 
 
    Calibration Description
    =======================
      Laboratory calibration of the UVS included measurements of:
 
          1) sensitivity at a number of wavelengths throughout the
             spectral range,
          2) response to scattered light,
          3) off-axis response, including collimator transmission
             function, and
          4) intrinsic dark count rate.
 
      In-flight calibration has included assessments of absolute
      sensitivity by comparisons with stars, and measurements of the
      FOV response profile using stars.
 
      Before the absolute calibration can be applied to a measured
      spectrum, three or four spectral analysis steps are required.
      These are flat field correction, dark count subtraction, and
      descattering, and (sometimes) sky background removal.
 
      Channel-to-channel variations in sensitivity result from
      variations in effective count threshold among channels.
      Applying a 'fixed pattern noise' (FPN) correction adjusts the
      signal levels to their equivalents for a common threshold in
      all channels.  The FPN correction involves a channel-by-channel
      multiplication by a correction spectrum.  The correction
      spectra are different for Voyager 1 and Voyager 2.  In fact,
      two spectra are in use for Voyager 1.  The first is used for
      data acquired before Jupiter encounter and the second for data
      after encounter.  The two differ to account for changes in the
      response of the Voyager 1 UVS induced by its operation in the
      intense Jovian radiation environment.
 
      Channels 3 and 4 have large FPN corrections, i.e.  they are
      less sensitive than the others.  Therefore the statistical
      accuracy of the signal in these channels is lower than in the
      other channels.
 
 
      Dark Counts
      -----------
        In interplanetary space, detector dark counts arise mainly
        from effects of gamma radiation from the radioisotope
        thermoelectric generators that power the spacecraft.  The
        count rate is about 0.02 counts per channel per second.  The
        shape is approximately flat in wavelength, with a step near
        the edge of the filter in the detector.  The shape is
        accurately known from long observations of the calibration
        plate mounted on the spacecraft.  Almost no photon signal
        (except for a weak reflection of sky-background H Lyman
        alpha) is recorded during these observations.  The absolute
        level varies slightly with scan platform position, because
        rotating the scan platform changes the shielding mass between
        the UVS detector and the generators.  For data acquired
        outside a planetary magnetosphere, subtracting a scaled dark
        spectrum from a calibration plate observation is usually a
        satisfactory correction for dark counting.
 
        Within a planetary magnetosphere, the dark count rate can
        include contributions from high-energy particles.  For lower
        levels, scaling a calibration plate spectrum is again
        satisfactory, but for higher levels the shape of the dark
        spectrum changes and another method must be used to
        estimate dark levels.  The best alternative is to use a
        spectrum taken at nearly the same time with no significant
        source in the FOV.  Satellite observations often fill this
        need.
 
 
      Descattering
      ------------
        Light scattered within the instrument illuminates channels
        outside the ideal transmission function of the collimator.
        The effects of scattering are removed by a process called
        descattering.  Descattering is accomplished through the use
        of a matrix operator, a 126x126 element matrix which
        describes the response of detector channel 'j' to the
        measured signal at channel 'i'.  This scattering matrix is
        completely empirical, having been determined from laboratory
        measurements of 50 individual emission lines covering the
        entire passband.  Descattering is a linear operation.  Dark
        counts must be subtracted prior to descattering as the
        descattering algorithm is based on the assumption that only
        photon events are present.  Descattering will also correct
        for second order response.  Therefore, if the spectrum to be
        descattered contains artifacts, such as anomalously high or
        low counts in channels 3 or 4, a corresponding error will be
        introduced in the vicinity of both the first and second order
        positions.
 
 
      Sky Background Subtraction
      --------------------------
        When the UVS slit is not completely filled by the disk of a
        planet, the portion off the planet sees the sky background.
        Fortunately, in the far UV the sky is generally quite dark
        and diffuse starlight is seldom significant.  However, bright
        emissions at H Lyman alpha, Lyman beta, and He 0.0584 microns
        from the interplanetary medium (IPM) often must be taken into
        account.  These lines arise from strong solar chromospheric
        emission lines that are scattered from neutral H and He of
        the local interstellar medium.  The physics of this
        'interstellar wind' is complex and leads to emission which is
        inhomogeneous in space and variable in time.  The IPM
        responds to active regions of the solar chromosphere as the
        sun rotates.  This means that the sky brightness as seen by
        the UVS can change noticeably on time scale of days.  As with
        instrumental dark counts, there are two standard means of
        removing sky background: direct subtraction of an adjacent
        sky background suitably scaled, if available, and
        construction of a synthetic sky background spectrum.
 
 
      Calibration
      -----------
        Calibrating the spectra converts them from count units to
        absolute brightness units. This step has not been included in
        the data processing because the correct procedure depends on
        the type of source viewed. The data spectra represent count
        rates after correction for fixed pattern noise, a background
        subtraction, and descattering. Multiplying these spectra by
        one of the calibration spectra converts it to brightness
        units. There is a calibration spectrum corresponding to each
        of the two source types, namely point sources and extended
        sources.
 
        Point Source: Multiplying a data spectrum by the calibration
        spectrum VxPTCAL.TAB (x=1 for Voyager 1 and x=2 for Voyager 2)
        converts the spectrum from counts/(channel) to
        photons/(cm**2-Angstrom-time), where time is the integration
        time of the spectrum.
 
        Extended Source, continuum emission: Multiplying a data
        spectrum that has been normalized to an integration time of 1
        second by the calibration spectrum VxFLCAL.TAB (x=1 for
        Voyager 1 and 2 for Voyager 2) converts the spectrum from
        counts/(channel-second) to spectral brightness in units of
        Rayleighs/Angstrom for a source that fills the field of view.
 
        Extended Source, monochromatic emission: The finite spectral
        resolution (about 35 A) of the spectrograph must be considered
        in this case. For isolated lines (those that are not strongly
        blended with emissions at nearby wavelengths) it is sufficient
        to sum the channels that include light from the emission of
        interest (about 7 channels) and multiply by the appropriate
        calibration factor. This factor is the product of the
        dispersion (9.26 Angstroms/channel) and the value in
        VxFLCAL.TAB corresponding to the center channel of the
        wavelength of interest. The resulting quantity is the
        brightness of a monochromatic emission that fills the field of
        view. For more complex spectra that include blended emissions,
        the most accurate approach is spectral analysis by generating
        synthetic spectra. This technique uses an iterative approach
        to adjust an estimated brightness spectrum until the model
        spectrum computed from it matches the observed spectrum. The
        model can be fairly simple, but must include the triangular
        transmission profile of the collimator and the instrument
        sensitivity (calibration). The calibration factor described
        earlier in this paragraph is the correct one to use for this
        kind of synthesis.
 
 
        Calibration and spectral analysis issues are discussed by
        [HOLBERGETAL1982] and [HOLBERG1986].
 
 
    Platform Mounting Descriptions
    ==============================
      The UVS is mounted on the scan platform.  The instrument is
      approximately bore-sighted with the wide and narrow angle
      television cameras, and with the PPS and IRIS instruments.  The
      alignment of the fields is not perfect; the following table
      gives offsets of the centers of the UVS fields relative to the
      centers of the ISS Narrow Angle Camera fields of view.
      Elevation is positive to the right within the imaging field of
      view, and cross-elevation is positive downward.  The narrow axis
      of the UVS slit is aligned with the elevation direction.
 
          Instrument        Elevation        Cross-Elevation
          --------------------------------------------------
           Voyager 1         +0.010 deg         -0.030 deg
                            +18.9 pixels       -56.6 pixels
           Voyager 2          0.0 deg           +0.08 deg
                              0.0 pixels      +150.9 pixels
 
      Cone Offset Angle              : UNK
      Cross Cone Offset Angle        : UNK
      Twist Offset Angle             : UNK
 
 
    Principal Investigator
    ======================
      The Principal Investigator for the ultraviolet spectrometer
      instrument is A. L. Broadfoot.
 
 
    Section 'UVS'
    =============
      Total Fovs                     : 2
      Data Rate                      : VARIABLE
      Sample Bits                    : 16
 
 
      'UVS' Detectors
      ---------------
        SPECTROMETER
 
 
      'UVS' Electronics
      -----------------
        UVS
 
 
      'UVS' Section Optic IDs
      -----------------------
        UVS
 
 
      In modes
      --------
        PULSE COUNTING
        PULSE INTEGRATION
        HIGH VOLTAGE 0
        HIGH VOLTAGE 1
        HIGH VOLTAGE 2
        HIGH VOLTAGE 3
        HIGH VOLTAGE 4
        HIGH VOLTAGE 5
        HIGH VOLTAGE 6
        HIGH VOLTAGE 7
 
 
      'UVS' Section FOV Shape 'RECTANGULAR'
      -------------------------------------
        The occultation field is offset from the airglow field by a
        small mirror.  The offset is toward lower elevation.  The
        elevation offsets are:
 
                  Voyager 1       -19.53  deg
                  Voyager 2       -19.296 deg
 
        Section Id                     : UVS
        Fovs                           : 1
        Horizontal Pixel Fov           : N/A
        Vertical Pixel Fov             : N/A
        Horizontal Fov                 : 0.86
        Vertical Fov                   : 0.25
 
 
      'UVS' Section Parameter 'SURFACE BRIGHTNESS'
      --------------------------------------------
        Sampling Parameter Name        : TIME
        Section Id                     : UVS
        Instrument Parameter Unit      : RAYLEIGHS
        Minimum Instrument Parameter   : 0.000000
        Maximum Instrument Parameter   : 0.000000
        Minimum Sampling Parameter     : 0.32
        Maximum Sampling Parameter     : 720
        Sampling Parameter Unit        : SECOND
 
 
      'UVS' Section Parameter 'FLUX'
      ------------------------------
        Sampling Parameter Name        : TIME
        Section Id                     : UVS
        Instrument Parameter Unit      : PHOTONS CM**-2 SEC**-1
        Minimum Instrument Parameter   : N/A
        Maximum Instrument Parameter   : N/A
        Minimum Sampling Parameter     : 0.32
        Maximum Sampling Parameter     : 720
        Sampling Parameter Unit        : SECOND
 
 
    Instrument Detector 'SPECTROMETER'
    ==================================
      The windowless, photoevent-counting detector consists of an
      electron multiplier, a pair of microchannel plates (MCP) in
      series, and a 128-element linear self-scanned readout array.
      Photoelectrons ejected at the front of the MCP stack are
      amplified by a factor of about 1E6, and the resulting charge
      pulse is collected by the anode array.  The 128 narrow aluminum
      anodes, each 3 mm long, are deposited on 0.1-mm centers for a
      collecting length (in the dispersion direction) of 13 mm.
 
      The anodes are accessed sequentially by a shift register and
      FET switches contained on the single integrated circuit.  The
      scanning circuitry discharges each anode into a charge
      sensitive preamplifier.  The charge pulse is digitized and the
      information added into a shift register memory consisting of
      128 16-bit words.  The 128-anode array consists of two separate
      interdigitated 64-anode arrays scanned by two shift registers.
      The shift registers and memory are driven by a 200 kHz clock,
      so that an individual anode is accessed every 320 microsecond.
      The detector scan rate is therefore about 3125 Hz.
 
      Wavelengths shorter than about 0.1250 micron strike the MCP
      directly.  Longer wavelengths first pass through a MgF2 filter
      with a semi-transparent photocathode of CuI.  This serves to
      boost the quantum efficiency at long wavelengths and to reduce
      the response to second-order light.
 
      The detector is heavily shielded to reduce its response to
      trapped particle radiation.  A description of the detector may
      be found in [BROADFOOT&SANDEL1977].
 
      Detector Type                  : MICROCHANNEL PLATES WITH ANODE
                                         ARRAY
      Detector Aspect Ratio          : N/A
      Minimum Wavelength             : 0.0535
      Maximum Wavelength             : 0.1702
      Nominal Operating Temperature  : 250
 
 
    Instrument Electronics 'UVS'
    ============================
      The UVS electronics is housed in an enclosure integral with the
      optical section of instrument.  Most of the electronics is in
      the base of the instrument, but clock drive generators for the
      anode array and the first stage of charge sensitive
      preamplification of the analog signal processing electronics
      are mounted in the detector housing so that they are near the
      anode array.  Elements of the electronics complement include:
 
           (1)  Low voltage power supply
           (2)  High voltage power supply
           (3)  Clock drive generator for the anode array
           (4)  Analog signal processing electronics including A/D
                conversion
           (5)  128x16 bit accumulation memory for spectrum
           (6)  FDS interface
 
      The FDS interface sends data to the FDS on demand and accepts
      mode commands from the FDS.  The mode commands set the level of
      the high voltage applied to the MCPs of the detector and set
      the mode of analog signal processing (pulse counting or
      integration).
 
      Radiation-hard electronics components were used where possible,
      and spot radiation shielding was used to reduce the fluence at
      certain critical elements.
 
 
    Instrument Optics 'UVS'
    =======================
      The optical system consists mainly of the mechanical collimator
      and concave diffraction grating.  The 13 aperture plates of the
      collimator establish a field of 0.1x0.87 degree for the airglow
      field and 0.25x0.87 degree for the occultation field.  The 0.1
      and 0.25 degree dimensions are in the dispersion direction, and
      the 0.87 degree dimension is in the cross-dispersion direction.
      The collimator provides separate light paths for the airglow
      and occultation ports, and a small mirror diverts the
      occultation field by 20 degrees from the airglow field.
 
      The concave diffraction grating is a platinum coated replica,
      ruled at 540 lines/mm, blazed at 0.0800 microns and having a
      spherical radius of curvature of 400.1 mm.  Dispersion in the
      image plane is 0.00926 microns/mm, or 0.000926 microns/channel.
      The grating substrate is a 4x6-cm rectangle, and the useful
      ruled area is 21 square cm.
 
      Telescope Diameter             : 0.06
      Telescope F Number             : 4
      Telescope Focal Length         : 0.20
      Telescope Resolution           : UNK
      Telescope Serial Number        : UNK
      Telescope T Number             : UNK
      Telescope T Number Error       : UNK
      Telescope Transmittance        : UNK
 
 
    Instrument Mode 'PULSE COUNTING'
    ================================
      Two modes of electrical operation allow the detector to operate
      in a photon-counting mode for low source intensities, or in an
      integration mode for high source intensities.  In the pulse
      counting mode, the number in the corresponding memory location
      is incremented by one if a charge above a fixed threshold is
      detected on an anode.  The access time of 320 microsec implies
      that single random photoevents can be recorded on any one of
      the anodes at a rate of about 300 Hz with a coincidence of 10%.
      The pulse-counting mode is used for all measurements except
      solar occultations.
 
      Data Path Type                 : N/A
      Gain Mode Id                   : N/A
      Instrument Power Consumption   : 3.2
 
 
      In sections
      -----------
        UVS
 
 
    Instrument Mode 'PULSE INTEGRATION'
    ===================================
      In the pulse integration mode a 3-bit A-to-D converter is
      introduced ahead of the adder.  In this case the charge on each
      anode is coarsely digitized and added to the previously
      accumulated signal in memory.  The statistics of sampling these
      events is complicated by the logarithmic pulse height
      distribution of the events.  There is also a logarithmic
      current limit function of the MCPs at the high event rates that
      normally obtain when this mode is used.  Because both these
      characteristics lead to non-linear response, modeling of the
      detector response is needed to restore linearity.  The
      integration mode is used for observing solar occultations.
 
      Data Path Type                 : N/A
      Gain Mode Id                   : N/A
      Instrument Power Consumption   : 3.2
 
 
      In sections
      -----------
        UVS
 
 
    Instrument Mode 'HIGH VOLTAGE 0'
    ================================
      The gain of the electron multiplier can be adjusted by setting
      the potential drop across the microchannel plates.  The high
      voltage level is commanded by the FDS.  Level 0 corresponds to
      high voltage off.
 
      Data Path Type                 : N/A
      Gain Mode Id                   : N/A
      Instrument Power Consumption   : 2.8
 
 
      In sections
      -----------
        UVS
 
 
    Instrument Mode 'HIGH VOLTAGE 1'
    ================================
      The gain of the electron multiplier can be adjusted by setting
      the potential drop across the microchannel plates.  The high
      voltage level is commanded by the FDS.  Level 1 is used for
      occultation and solar observations.
 
      Data Path Type                 : N/A
      Gain Mode Id                   : N/A
      Instrument Power Consumption   : 3.2
 
 
      In sections
      -----------
        UVS
 
 
    Instrument Mode 'HIGH VOLTAGE 2'
    ================================
      The gain of the electron multiplier can be adjusted by setting
      the potential drop across the microchannel plates.  The high
      voltage level is commanded by the FDS.  Level 2 is used for
      occultation and solar observations.
 
      Data Path Type                 : N/A
      Gain Mode Id                   : N/A
      Instrument Power Consumption   : 3.2
 
 
      In sections
      -----------
        UVS
 
 
    Instrument Mode 'HIGH VOLTAGE 3'
    ================================
      The gain of the electron multiplier can be adjusted by setting
      the potential drop across the microchannel plates.  The high
      voltage level is commanded by the FDS.  Level 3 is used for
      airglow observations and some occultation observations.
 
      Data Path Type                 : N/A
      Gain Mode Id                   : N/A
      Instrument Power Consumption   : 3.2
 
 
      In sections
      -----------
        UVS
 
 
    Instrument Mode 'HIGH VOLTAGE 4'
    ================================
      The gain of the electron multiplier can be adjusted by setting
      the potential drop across the microchannel plates.  The high
      voltage level is commanded by the FDS.  Level 4 is intended to
      recoup losses in supply output that could have occurred due to
      radiation damage.  It is not normally used for observations.
 
      Data Path Type                 : N/A
      Gain Mode Id                   : N/A
      Instrument Power Consumption   : 3.2
 
 
      In sections
      -----------
        UVS
 
 
    Instrument Mode 'HIGH VOLTAGE 5'
    ================================
      The gain of the electron multiplier can be adjusted by setting
      the potential drop across the microchannel plates.  The high
      voltage level is commanded by the FDS.  Level 5 is intended to
      recoup losses in supply output that could have occurred due to
      radiation damage.  It is not normally used for observations.
 
      Data Path Type                 : N/A
      Gain Mode Id                   : N/A
      Instrument Power Consumption   : 3.2
 
 
      In sections
      -----------
        UVS
 
 
    Instrument Mode 'HIGH VOLTAGE 6'
    ================================
      The gain of the electron multiplier can be adjusted by setting
      the potential drop across the microchannel plates.  The high
      voltage level is commanded by the FDS.  Level 6 is intended to
      recoup losses in supply output that could have occurred due to
      radiation damage.  It is not normally used for observations.
 
      Data Path Type                 : N/A
      Gain Mode Id                   : N/A
      Instrument Power Consumption   : 3.2
 
 
      In sections
      -----------
        UVS
 
 
    Instrument Mode 'HIGH VOLTAGE 7'
    ================================
      The gain of the electron multiplier can be adjusted by setting
      the potential drop across the microchannel plates.  The high
      voltage level is commanded by the FDS.  Level 7 is intended to
      recoup losses in supply output that could have occurred due to
      radiation damage.  It is not normally used for observations.
 
      Data Path Type                 : N/A
      Gain Mode Id                   : N/A
      Instrument Power Consumption   : 3.2
 
 
      In sections
      -----------
        UVS

        