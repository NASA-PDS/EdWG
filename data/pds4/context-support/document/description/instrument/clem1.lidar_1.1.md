
 
 
 
    Instrument Overview
    ===================
      Laser Rangefinder (LIDAR): The LIDAR unit shares the
      telescope of the HiRes camera, splitting the 1064 nm
      return signal from the NdYag source off to an avalanche
      photodiode (APD) detector with dichroic filter. The
      optics are non-imaging, providing an exit pupil through
      simple relay optics at the APD. The APD electronics
      include a temperature compensation feature for the APD
      bias voltage and programmable thresholding of the output
      signal. The APD current is amplified and inverted to a
      voltage by a transimpedance amplifier with a gain of 230X,
      a low frequency cutoff of 3 MHz, and a high frequency
      cutoff of 23 MHz.  The voltage derived from the APD
      current is amplified, then discriminated for changes
      (increase) through a 14 MHz discriminator.  Voltage
      changes exceeding the programmed threshold are flagged
      as returns [NOZETTEETAL1994].
 
      The LIDAR instrument measured the slant range from the
      spacecraft to the lunar surface at spacecraft altitudes of
      640 km or less.  These measurements were used to determine
      the global lunar topography field.
 
 
    Scientific Observations
    =======================
      Throughout the Lunar Mapping phase of the mission, the
      LIDAR system acquired high resolution profiles of lunar
      topography.  Over those parts of each revolution where
      radio tracking of the spacecraft was possible, variations
      in the gravity field of the Moon could be measured.  The
      combination of topography profiles and gravity maps places
      important constraints on the interior structure of the
      Moon.  The orbital topography data were gridded and used
      to produce a spherical harmonic topography model (GLTM-
      2B).  This topographic model represents the first reliable
      global characterization of surface heights for the Moon
      [ZUBERETAL1994].
 
 
    Calibration
    ===========
      N/A
 
 
    Operational Considerations
    ==========================
      Below 640 km, the instrument had adequate sensitivity to
      obtain range measurements from both mare and highland
      surfaces.  While the ranging success rate for all
      measurements was ~20%, many more successful returns were
      obtained from the smooth mare surfaces than the rougher
      highlands.  However, the distribution of points allowed a
      qualitative physical description of the shape of the
      Moon.
 
 
    Detectors
    =========
      The LIDAR uses a avalanche photodiode (APD) detector with
      a dichroic filter.
 
 
    Electronics
    ===========
      The APD electronics includes a temperature compensation
      feature for the APD bias voltage and programmable
      thresholding of the output signal.
 
 
    Filters
    =======
      There were no instrument filters.
 
 
    Optics
    ======
      The optics are non-imaging, providing an exit pupil
      through simple relay optics at the APD.
 
 
    Operational Modes
    =================
      The Clementine LIDAR operated in two distinct modes, 'ON'
      and 'OFF'.  There was also the ability to range at 8Hz,
      and this was done several times the week before the
      spacecraft left the Moon.
 
 
    Subsystems
    ==========
      N/A
 
 
    Measured Parameters
    ===================
      The LIDAR instrument measured the slant range from the
      spacecraft to the lunar surface at spacecraft altitudes of
      640 km or less.  Clock cycles were returned which were
      then converted to range by a multiplicative factor.
      Basically, the range value was determined by the number of
      clock cycles between the laser start pulse and the
      received signal.  These cycles were time-tagged, and from
      the time tag it was possible to reconstruct the latitude
      and longitude position on the surface by knowing the
      spacecraft orbit and orientation.  The instrument
      collected data for approximately one-half hour per 5-hour
      orbit during the 2-month lunar mapping mission
      [ZUBERETAL1994].
 
      The clock counter has only 14 bits owing to hardware
      availability limitations.  In order to allow returns up to
      the 640 km maximum range required in the lunar mission,
      returns are binned four to a clock count, turning the 15
      MHz response into a 39.972 meter height bin.  Internal
      memory in the LIDAR unit saves up to six 'returns' per
      laser firing, with up to four saved in the programmable
      search range.  The programmable search range simply refers
      to the range of possible detection thresholds, defined as
      a fixed number of set 10 mV voltage levels which had to be
      exceeded [NOZETTEETAL1994].
 
      The detection threshold was never formally 'confirmed'.
      It was selected on the basis of: 1) a link analysis, which
      is a statistical analysis which looks at how to maximize
      the probability of getting a valid hit while minimizing
      the probability of triggering the detector due to solar
      background or electronic noise; and 2) experience on how
      the instrument was operating in orbit.  Clementine mission
      scientists or the LLNL engineers manually uploaded the
      threshold values every day, and the values were dependent
      on: spacecraft orbital height, surface albedo (maria or
      highlands), sun angle (sunlit or dark), and instrument
      gain.
 
      During the course of the mission the LIDAR typically
      ranged at a rate of 1 shot per 1.6 seconds and triggered
      on about 123,000 shots, corresponding to 19% of the
      transmitted laser pulses.  Typical along-track shot
      spacings were on the order of 20 km, but this varied
      considerably [ZUBERETAL1994].
 

        