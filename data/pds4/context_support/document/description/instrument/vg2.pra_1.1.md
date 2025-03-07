
 
  INSTRUMENT: PLANETARY RADIO ASTRONOMY RECEIVER
  SPACECRAFT: VOYAGER 2
 
 
  Instrument Information
  ======================
    Instrument Id                     : PRA
    Instrument Host Id                : VG2
    Instrument Name                   : PLANETARY RADIO ASTRONOMY
                                        RECEIVER
    Instrument Type                   : RADIO SPECTROMETER
    PI Name                           : JAMES W. WARWICK
    Build Date                        : UNK
    Instrument Mass                   : 7.700000
    Instrument Height                 : UNK
    Instrument Length                 : UNK
    Instrument Width                  : UNK
    Instrument Manufacturer Name      : MARTIN MARIETTA
    Instrument Serial Number          : UNK
 
 
  Science Objectives
  ==================
    The Planetary Radio Astronomy (PRA) experiments' primary
    objective was to locate and explain kilometric, hectometric,
    and decametric radio emissions from the planets; to measure
    plasma resonances near the giant planets; and to detect
    lightning on the giant planets.  The instrument was also
    successful at observing solar radio emissions from the
    perspective of the outer solar system.
 
    Radio emissions can be used to determine the rate of rotation
    of the inner core of a planet, to determine the existence of a
    magnetic field, and to search for magnetic anomalies.  Radio
    emissions are often the only remote diagnostic for interactions
    occurring in the portions of magnetospheres through which a
    spacecraft does not pass.  This is particularly true for the
    inner magnetosphere, which usually goes unsampled.
 
    Further information on the instrument and the investigations
    performed can be found in [WARWICKETAL1997].
 
 
  Instrument Description
  ======================
    The Voyager Planetary Radio Astronomy (PRA) instrument
    consisted of two superheterodyne receivers, one for the range
    from 1326.0 to 1.2 kHz (center frequency) and a second for the
    range 40.55 to 1.53 MHz (center frequency).  The channels are
    numbered so that the lowest frequency channel (1.2 kHz) is
    channel number 198.  Channels in the range 1 to 128 are
    referred to as 'high band', and the remaining channels as 'low
    band'.  In low band, the channel spacing is 19.2 kHz.  In high
    band, the channel spacing is 307.2 kHz.
 
    The PRA receiver is driven by two orthogonal antennas mounted
    on the spacecraft body.  Each antenna element is made of BeCu
    hollow tubes 0.5 inches in diameter and is 10 meters in length.
    By combining the signals from the two antennas in a 90 degree
    hybrid, the PRA instrument can distinguish between the opposing
    states, left hand and right hand, of circular polarization of
    an incoming wave.
 
    The Planetary Radio Astronomy (PRA) receivers were calibrated
    under environmentally-controlled conditions and over the entire
    frequency and dynamic range of the instruments.  This
    calibration consisted in application of a known narrow-band
    signal across the inputs and recording the receiver outputs.
 
    The laboratory calibrations provided power levels for each data
    number (DN) and each frequency in terms of known inputs across
    the antenna terminals of each of the experiment's two
    monopoles.  Calibrations were carried out over a range of
    receiver temperatures, but in practice the stability of the
    receiver as a function of temperature and the stability of the
    temperature of the receiver as a function of mission phase and
    the status of the overall spacecraft were such that a single
    calibration for each DN at each frequency could be used.
 
    Receiver output levels were quantized.  The minimum value for
    the wave flux density was frequency dependent varying from
    5.E-20 W M**-2 Hz**-1 at frequencies below 1.5 MHz to 5.E-19 at
    frequencies above 1.5 MHz.  The maximum wave flux density was
    typically 50 dB above the minimum value.  The instrument noise
    level also was frequency dependent.  It was about 1.E-19 W
    M**-2 Hz**-1 below 1.5 MHz.  The noise at 10 MHz was still
    about 1E-19 W M**-2 Hz**-1, increased to about 1.E-17 W M**-2
    Hz**-1 at 25 MHz, and then decreased to an intermediate value
    at 40 MHz.
 
    The low-band and high-band operation of the receiver differ.
    In low-band the receiver operated with a sharply tuned filter
    only 1 kHz broad at the 3 dB points and in high-band, with a
    200 kHz filter.  The gain of the receivers was designed in such
    a way that the output increased discontinuously by 23 dB
    (corresponding to the 200:1 bandwidth ratio) between the lowest
    frequency of high-band and the highest frequency of low-band.
    This caused the instrument output to remain constant across the
    high-band to low-band transition point if its input was
    broadband noise.
 
    If unpolarized radiation fell orthogonally on each monopole,
    the total unpolarized flux density for signals below about 5
    MHz could be roughly estimated to be
 
    S = So (10**(m/1000)),
 
    where m was the channel reading in millibels and So is
 
    So = 1.5E-21 (W/Hz m**2).
 
    No reliable method for estimating the flux density exists for
    frequencies above 5 MHz due to the increasing effect of antenna
    resonances.
 
    Although the PRA instrument had 14 possible operating modes, in
    practice the mode called POLLO was used more than 95% of the
    time.  In POLLO, the receiver swept through all 198 channels in
    sequence from the highest frequency to the lowest.  At each
    frequency step, data were produced every 30 msec, consisting of
    25 msec of integration and 5 msec of switching and settling
    time.  Thus, a full sweep through all 200 channels took 6 sec
    (including 60 msec for two status words).  Between steps the 90
    degree hybrid was switched such that the receiver was sensitive
    to the alternate sense of circular polarization.  This toggling
    between left hand and right hand polarization itself alternated
    with each 6 sec receiver sweep.  Thus, for a given frequency, a
    pair of left hand and right hand measurements were 6 sec
    apart.

        