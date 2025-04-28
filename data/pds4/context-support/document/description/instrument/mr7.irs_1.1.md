
 
 
    INSTRUMENT: INFRARED SPECTROMETER
    SPACECRAFT: MARINER 7
 
 
    Instrument Information
    ======================
      Instrument Id                  : IRS
      Instrument Host Id             : MR7
      Pi Pds User Id                 : GPIMENTEL
      Instrument Name                : UNK
      Instrument Type                : UNK
      Build Date                     : 1969
      Instrument Mass                : 17.400000
      Instrument Length              : 0.490000
      Instrument Width               : 0.230000
      Instrument Height              : 0.250000
      Instrument Serial Number       : UNK
      Instrument Manufacturer Name   : UNIVERSITY OF CALIFORNIA,
                                       BERKELEY
 
 
    Instrument Description
    ======================
      The IRS instrument is comprised of a 10-inch Dall-Kirkham
      telescope feeding a pair of circular-variable filter (CVF)
      spectrometers.  Channel 1 covers 4.0 to 14.3 microns, detected
      by a HgGe detector at 22K, cooled by a Joule-Thomson cryostat.
      Channel 2 covers 1.9-6.0 microns; detection is by a PbSe
      detector at 175K, with radiative cooling.  Wavelength
      resolution is 0.5-1.0%.
 
      The filters were each comprised of two semicircular filters
      bonded together and accompanied by a matching set of blocking
      filters.  Thus one rotation of the wheel covered roughly n to
      2n and 2n to 4n in wavelength space.  The spectral resolution
      varied between 0.7 to 1.1%.  Two 'radiometer' slots were
      produced between the filter segments, twice per revolution, by
      rotating the blocking filter 0.01 degrees of arc relative to
      the CVF, allowing broadband light to fall on the detectors.
 
 
    Science Objectives
    ==================
      The IR Spectrometers were intended to determine the composition
      of the Mars atmosphere, including minor constituents.
 
 
    Operational Considerations
    ==========================
      It appears that the rate of rotation of the filter wheels is
      somewhat variable, producing a 'stretching' effect in the data.
 
 
    Calibration Description
    =======================
      Pre-flight calibration of the IRS instruments consisted of
      obtaining spectra of blackbody sources at varying temperatures
      in the range 77-300K, as well as absorption spectra of NH3,
      CH4, H20, CO2, and polystyrene with a high-temperature source.
      During flight, spectra were obtained periodically of a
      reference thermal target and of polystyrene superimposed on the
      Mars spectrum.  Refer to the instrument paper.  Several
      blackbody calibration spectra at various target temperatures
      are available in the data file; they are the first spectra in
      the set, flagged by having negative spectrum numbers.
 
 
    Section 'CH1'
    =============
      Total Fovs                     : 1
      Data Rate                      : UNK
      Sample Bits                    : UNK
 
 
      'CH1' Detectors
      ---------------
        CH1
 
 
      'CH1' Electronics
      -----------------
        IRS
 
 
      'CH1' Filters
      -------------
        LONGWAVE
 
 
      'CH1' Section Optic IDs
      -----------------------
        IRS
 
 
      In modes
      --------
        OPERATING
 
 
      'CH1' Section FOV Shape 'RECTANGULAR'
      -------------------------------------
        Section Id                     : CH1
        Fovs                           : 1
        Horizontal Fov                 : 0.100000
        Vertical Fov                   : 2.070000
 
 
      'CH1' Section Parameter 'SPECTRAL INTENSITY'
      --------------------------------------------
        The spectral 'Y axis' is proportional to raw instrument
        output, and therefore does not correspond to physical units
        such as radiance.  Once the instrument response is removed
        from the spectra, and an allowance made for zero-level
        response, the data can be expressed in units of radiance.
        These corrections can be made using the laboratory blackbody
        and near-Mars sky spectra included in this data set.
 
        Instrument Parameter Name      : SPECTRAL INTENSITY
        Sampling Parameter Name        : WAVELENGTH
        Minimum Instrument Parameter   : -10.000000
        Maximum Instrument Parameter   : 100.000000
        Minimum Sampling Parameter     : 3.900000
        Maximum Sampling Parameter     : 14.500000
        Noise Level                    : UNK
        Sampling Parameter Interval    : 0.016000
        Sampling Parameter Resolution  : 0.050000
        Sampling Parameter Unit        : MICROMETER
 
 
    Section 'CH2'
    =============
      Total Fovs                     : 1
      Data Rate                      : UNK
      Sample Bits                    : UNK
 
 
      'CH2' Detectors
      ---------------
        CH2
 
 
      'CH2' Electronics
      -----------------
        IRS
 
 
      'CH2' Filters
      -------------
        SHORTWAVE
 
 
      'CH2' Section Optic IDs
      -----------------------
        IRS
 
 
      In modes
      --------
        OPERATING
 
 
      'CH2' Section FOV Shape 'RECTANGULAR'
      -------------------------------------
        Section Id                     : CH1
        Fovs                           : 1
        Horizontal Fov                 : 0.100000
        Vertical Fov                   : 2.070000
 
 
      'CH2' Section Parameter 'SPECTRAL INTENSITY'
      --------------------------------------------
        The spectral 'Y axis' is proportional to raw instrument
        output, and therefore does not correspond to physical units
        such as radiance.  Once the instrument response is removed
        from the spectra, and an allowance made for zero-level
        response, the data can be expressed in units of radiance.
        These corrections can be made using the laboratory blackbody
        and near-Mars sky spectra included in this data set.
 
        Instrument Parameter Name      : SPECTRAL INTENSITY
        Sampling Parameter Name        : WAVELENGTH
        Minimum Instrument Parameter   : -10.000000
        Maximum Instrument Parameter   : 100.000000
        Minimum Sampling Parameter     : 1.880000
        Maximum Sampling Parameter     : 6.000000
        Noise Level                    : UNK
        Sampling Parameter Interval    : 0.007000
        Sampling Parameter Resolution  : 0.030000
        Sampling Parameter Unit        : MICROMETER
 
 
    Instrument Detector 'CH1'
    =========================
      Detector Type                  : HG:GE
      Detector Aspect Ratio          : 0.200000
      Minimum Wavelength             : 3.900000
      Maximum Wavelength             : 14.500000
      Nominal Operating Temperature  : 22.000000
 
 
      Description
      -----------
        The Hg:Ge detectors were made by Santa Barbara Research
        Center, had an active area of 1 by 5 mm, and were bonded to a
        copper heat sink cooled by a two-stage (nitrogen and
        hydrogen) Joule-Thomson cryostat.
 
 
      Sensitivity
      -----------
        The Mariner 7 Hg:Ge detector had a lab- measured sensitivity
        with a 500K source of 1.4 E-11 watt (noise equivalent power)
        and a D* (detectivity) of 2.73 E10.
 
 
    Instrument Detector 'CH2'
    =========================
      Detector Type                  : PBSE
      Detector Aspect Ratio          : 0.200000
      Minimum Wavelength             : 1.900000
      Maximum Wavelength             : 6.500000
      Nominal Operating Temperature  : 175.000000
 
 
      Description
      -----------
        The PbSe detectors were made by Santa Barbara Research
        Center, had an active area of 1 by 5 mm, and were bonded to
        an aluminum heat sink cooled by a 23 by 20 cm radiator plate.
 
 
      Sensitivity
      -----------
        The Mariner 7 PbSe detector had a lab- measured sensitivity
        with a 500K source of 1.36 E-10 watt (NEP) and a D*
        (detectivity) of 2.6 E10.
 
 
    Instrument Electronics 'IRS'
    ============================
 
      Description
      -----------
        The incoming radiation for each detector was chopped by
        tuning forks, at 500 hz for channel 1 and 550 hz for channel
        2.  The modulated signal from each detector was fed directly
        to its preamp, which contained the detector bias circuit.
        The preamp input stage was an FET designed to provide high
        gain and low noise.  The amplifiers were operated with both
        ac and dc feedback so that the gain and bandwidth would be
        relatively insensitive to internal component changes.
        Following the preamp were a synchronous filter, demodulator,
        log converter, output amplifier, science data multiplexer,
        and data analog to pulse width converter.  For additional
        information, please refer to the instrument description
        reference: Applied Optics, 1972, 'Mariner Mars 1969 IR
        Spectrometer, vol.  11, p.  493'
 
 
    Instrument Filter '1 - LONGWAVE'
    ================================
      Filter Name                    : LONGWAVE
      Filter Type                    : CIRCULAR-VARIABLE INTERFERENCE
      Minimum Wavelength             : 3.900000
      Maximum Wavelength             : 14.400000
 
 
      Description
      -----------
        Wavelength calibration information in flight was derived from
        observations of polystyrene film, which has many absorption
        features in the range of interest.  The polystyrene spectrum
        was superimposed on the target (Mars) spectrum each 12th
        time.  Unfortunately, these spectra are unavailable at the
        present time in digital form.  The spikes that occur in all
        the spectra are introduced by allowing broadband radiation
        onto the detector at certain rotational positions of the
        circular variable filters.  Ostensibly, these spikes
        represent wavelength fiduciaries.  Thus, for Mariner 7, the
        first spike is at 3.86 microns, the middle spike at 7.88.
        The longwave segment of CHANNEL 1 uses the middle spike as
        7.37 microns and the third spike as 14.45.  However, it will
        be found that the spikes do not relate reproducibly to the
        locations of atmospheric CO2 features; there is a small
        jitter in the relative locations.  Wavelength information can
        also be derived from the known positions of these CO2
        atmospheric features in the Mars data; this is probably the
        most accurate and dependable scheme.  The supplier has
        generated coefficients that describe a linear fit to the
        wavelength scale, based on atmospheric features and the
        spikes.  These appear in the headers for each spectrum.  Note
        that the quality of the coefficients is variable and depends
        on the noise level and the method chosen for that spectrum.
 
        Refer to the instrument paper in Applied Optics for figures
        showing the wavelength variation of filter transmission and
        spectral resolution.
 
 
    Instrument Filter '2 - SHORTWAVE'
    =================================
      Filter Name                    : SHORTWAVE
      Filter Type                    : CIRCULAR-VARIABLE INTERFERENCE
      Minimum Wavelength             : 1.880000
      Maximum Wavelength             : 6.000000
 
 
      Description
      -----------
        Wavelength calibration information in flight was derived from
        observations of polystyrene film, which has many absorption
        features in the range of interest.  The polystyrene spectrum
        was superimposed on the target (Mars) spectrum each 12th
        time.  Unfortunately, these spectra are unavailable at the
        present time in digital form.  The spikes that occur in all
        the spectra are introduced by allowing broadband radiation
        onto the detector at certain rotational positions of the
        circular variable filters.  Ostensibly, these spikes
        represent wavelength fiduciaries.  Thus, for Mariner 7, the
        spikes mark 1.88 microns and 3.69 microns for the shortwave
        part of channel 2, and 2.99 and 6.00 microns on the longwave
        side.  It will be found that the spikes do not relate
        reproducibly to the locations of atmospheric CO2 features;
        there is a small jitter in the relative locations.
        Wavelength information can also be derived from the known
        positions of these CO2 atmospheric features in the Mars data;
        this is probably the most accurate and dependable scheme.
        The supplier has generated coefficients that describe a
        linear fit to the wavelength scale, based on atmospheric
        features and the spikes.  These appear in the headers for
        each spectrum.  Note that the quality of the coefficients is
        variable and depends on the noise level and the method chosen
        for that spectrum.
 
        Refer to the instrument paper in Applied Optics for figures
        showing the wavelength variation of filter transmission and
        spectral resolution.
 
 
    Instrument Optics 'IRS'
    =======================
      Telescope Diameter             : 0.248000
      Telescope F Number             : 2.000000
      Telescope Focal Length         : 0.498000
      Telescope Resolution           : UNK
      Telescope Serial Number        : UNK
      Telescope T Number             : UNK
      Telescope T Number Error       : UNK
      Telescope Transmittance        : 0.877000
 
 
      Description
      -----------
        The IRS instrument is comprised of a 10-inch Dall-Kirkham
        telescope feeding a pair of circular-variable filter
        spectrometers.  The size of the instrument field of view (a
        slit) is 2.07 by 0.10 degrees, or 36.1 by 1.75 milliradians.
 
 
    Instrument Mode 'OPERATING'
    ===========================
      Data Path Type                 : REALTIME
      Instrument Power Consumption   : 11.000000
 
 
      In sections
      -----------
        CH1
        CH2
 
 
      Description
      -----------
        There are no separate operating modes for the IRS.  Data were
        acquired continuously during encounter, with the instrument
        taking successive spectra in this sequence: blackbody
        reference target, five Mars, polystyrene wavelength
        calibrator + Mars, five Mars, reference target, etc.
 
 
    Mounted On Platform 'SCAN PLATFORM'
    ===================================
      Cone Offset Angle              : UNK
      Cross Cone Offset Angle        : UNK
      Twist Offset Angle             : UNK
 
 
      Description
      -----------
        Position of the IRS FOV relative to the television experiment
        (from Data Format Report, 1970):
 
                                      Cone             Cross-cone
 
                TV-B             -0 deg.  1'50''      +0 deg. 0'30''
                TV-A             +0      14'50''      +0      9'31''
                IRS              -3      53'12''      +1     33'42''
 
        It is not stated for which spacecraft these values apply.
        The offset was intentional and is likely similar for both
        spacecraft.
 

        