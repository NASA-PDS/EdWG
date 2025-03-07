
      Instrument Overview
      ===================
      The Giotto spacecraft telecommunications subsystem served as
      one element of a radio science experiment for investigations
      of comet Halley.  The second element was a set of ground
      antennas and associated electronics, most of which were in
      Australia.  The spacecraft element of the experiment is
      specified below.
 
          Instrument Id               : RSS
          Instrument Host Id          : GIO
          Instrument Name             : GIOTTO RADIOSCIENCE EXPERIMENT
          Instrument Type             : RADIO SCIENCE
 
      The Giotto Radio Science Experiment (GRE) utilized
      instrumentation with elements on the spacecraft and on
      Earth.  Much of this was shared equipment, being used for
      routine telecommunications as well as for Radio Science.
      The experiment is described in more detail by
      [EDENHOFERETAL1986A] and [EDENHOFERETAL1987A].
 
      The spacecraft radio system was constructed around a
      redundant pair of transponders which received at S-band
      (2.3 GHz, 13 cm wavelength) and transmitted at both S-band
      and X-band (8.4 GHz, 3.6 cm wavelength) frequencies.  The
      transmitted frequency during the Halley encounter was
      controlled by an on-board oscillator; at other times it was
      controlled by a signal transmitted from the ground.
 
      Each transponder included a receiver, command detector,
      exciter, and low-power amplifier.  The transponders
      provided the usual uplink command and downlink data
      transmission capabilities.
 
      Traveling wave tube amplifiers, driven at saturation,
      amplified the transponder output before the signals were
      radiated via a high-gain antenna (HGA).  The HGA offset
      reflector had a diameter of 1.46 m and was despun with
      respect to the spacecraft body.  HGA polarization was
      right circularly polarized for S-band up/downlink and for
      X-band downlink.  S-band beamwidth was about 5 degrees;
      X-band beamwidth was about 2 degrees.
 
      Ground stations included antennas, associated electronics,
      and operational systems at two complexes in Australia.  The
      prime system for GRE was the NASA Deep Space Network (DSN)
      station near Canberra; its 64-m antenna is known as DSS 43.
      Geodetic coordinates for the 64-m antenna are 148 deg, 58
      min, 48 sec E longitude and 35 deg, 24 min, 14 sec S
      latitude.  Raw data from the DSN tracking system included
      Doppler measurements along the line of sight to the
      spacecraft.  Raw data from the open loop receiver system
      included digital samples of baseband output.  The second
      system was the 64-m antenna operated by the Australian
      CSIRO near Parkes; it served as the primary Giotto ground
      receiving facility for the European Space Agency in
      addition to its role as a receiving site for the GRE
      [HALL1986].
 
      Once the radio signal from the spacecraft had been captured
      by a ground antenna, it was amplified by cryogenic maser
      amplifiers.  Two measurement options were then available:
 
        (1) Open-loop Data Acquisition
        (2) Closed-loop Data Acquisition
 
 
      Open-Loop Data Acquisition
      --------------------------
 
        Open-loop data acquisition is performed by filtering and
        then downconverting the received carrier signal to
        baseband, where it is sampled for subsequent manipulation
        in digital form.  The open-loop receiver is tuned on the
        basis of frequency predictions that take into account the
        best estimate of the carrier frequency transmitted by the
        spacecraft and Doppler corrections based on relative
        spacecraft-to-ground motion.  The quantized samples can
        then be recorded on magnetic tape.
 
 
      Closed-Loop Data Acquisition
      ----------------------------
 
        Closed-loop data acquisition is performed with a phase-
        locked loop receiver; it is usually employed when the
        spacecraft is operating in its 'coherent' mode.  'Two-way'
        Doppler shifts are determined by comparing an estimate of
        the downlink carrier frequency from the phase-locked loop
        with a reference from the ground station's frequency and
        timing subsystem.  Since the station frequency reference
        is also used to generate the uplink carrier, the
        determination can be as accurate as the fundamental
        station clock -- typically a hydrogen maser frequency
        standard and, therefore, more stable than the crystal
        oscillator on board the spacecraft.
 
        The Doppler integration time needed to achieve a
        particular signal-to-noise ratio controls the time
        interval between successive measurements.  Amplitude of
        the received signal is estimated by sampling the
        calibrated automatic gain control (AGC) voltage of the
        phase-locked loop receiver's coherent AGC loop.
 
        'One-way' closed-loop Doppler shifts are determined in
        much the same way except that the downlink measurement
        from the phase locked loop must be compared with an
        estimate of the spacecraft carrier frequency; in this
        case the accuracy is limited by the relative performance
        of the reference oscillators on the ground and the
        spacecraft.  Both frequency and amplitude measurements
        obtained at the DSN station can then be recorded on
        magnetic tape and/or transmitted electronically to JPL.
        Files of data specifically intended for navigation and
        radio science are derived from the raw measurements by
        the DSN Radio Metric Data Conditioning Team.
 
        Operation of the DSN radio science equipment is described
        in more detail by [ASMAR&HERRERA1993].
 
      The strength of a spacecraft carrier signal, and thus the
      quality of the radio science data, depends on its modulation
      state.  During the Halley encounter, only the X-band downlink
      was activated; it was modulated with science data.  The link
      budget for the GRE prime receiver at Canberra, Australia is
      shown below [EDENHOFERETAL1986B]:
 
 
                                           S-band   S-band    X-band
                                           uplink  downlink  downlink
                                           ------  --------  --------
          Signal frequency (GHz)            2.117    2.299     8.429
          TX power (dBm)                    73       36.7      43.2
          Ground antenna gain (dB)          60.6     61.7      71.9
          Propagation loss (dB)           -262.5   -263.2    -274.5
          S/C antenna gain (dB)             25.3     26.3      39
          RF losses (dB)                    -2.3     -1.9      -1.6
          Signal level RX input (dBm)     -105.9   -140.4    -122
          System noise temperature (dBK)    27.2     13.7      13.8
          Boltzmann constant (dBm/HzK)    -198.6   -198.6    -198.6
          Received S/No (dBHz)              65.5     44.5      62.8
          Modulation loss (dB)               0       -3.6      -8.2
          PLL bandwidth (dBHz)              15.4     16.8      16.8
          Required C/N (dB)                 10       15        15
          Margin (dB)                       40.1      9.1      22.8
 
 
 
 
      Science Objectives
      ==================
      The primary objective of the Giotto Radio Science
      Experiment was determination of the Halley mass fluence
      resulting from atmospheric drag.  A second objective was
      determining the electron content of the ionosphere of the
      comet; this part of the experiment was badly degraded when
      Giotto project management chose to operate only an X-band
      downlink during the encounter.
 
      Mass fluence was determined by measuring the change
      in spacecraft radial velocity (with respect to receiving
      stations on the Earth) during the encounter.  Velocity
      changes were inferred from Doppler shifts in the received
      signal.  Doppler shifts not in accord with the expected
      trajectory could be interpreted as resulting from drag on
      the spacecraft by dust and gas.
 
      Passage of the radio wave through a plasma can also cause
      Doppler shifts on the received signal.  The plasma effects
      can be readily separated from other effects if measurements
      are made at two well-separated radio frequencies.  The
      inability to make measurements at S-band meant that only
      indirect measurements and modeling could be used to infer
      the density of charged particles in the Halley environment.
 
      Calibration Descriptions
      ========================
      Several calibration measurements were carried out; most
      were directed toward estimating the propagation effects of
      charged particles along the ray path.
 
      Earth Ionosphere Plasma Content
      -------------------------------
 
        VHF Faraday rotation measurements were made at Canberra
        using the ETS-2 geostationary satellite.  These
        measurements would provide a measure of the plasma
        content in the Earth's ionosphere over Canberra.
 
      Other Earth Atmospheric Effects
      -------------------------------
 
        Acquisition of data at two Earth sites (Canberra and
        Parkes) ensured that local anomalies in propagation
        conditions over a single antenna (such as changes in
        the ionosphere) could be calibrated and removed.  The
        results from Canberra and Parkes were very similar
        [EDENHOFERETAL1987B].
 
 
      Ray Path Reference
      ------------------
 
        The Sakigake spacecraft was tracked at S-band by the
        DSS 42 antenna -- a 34-m antenna that is also part of
        the Canberra DSN complex.  Since Sakigake was in the
        same part of the sky as Giotto, differences in the
        properties of the received signals would depend
        primarily on the propagation conditions in the
        immediate environment of Halley during the Giotto
        encounter.
 
 
      Vega Spacecraft Measurements
      ----------------------------
 
        Vega-1 and Vega-2 used dual-frequency radio methods to
        obtain estimates of peak electron densities during
        their encounters with Halley (2500 electrons per cubic
        centimeter at 8890 km closest approach distance and
        1500 el/cc at 8030 km, respectively).  Extrapolation
        of these values to the Giotto flyby conditions gave
        numbers consistent with simulation [EDENHOFERETAL1986C].
 
 
      Asymptotic Spacecraft Trajectory Calibration
      --------------------------------------------
 
        Two-way Doppler and ranging data were acquired both
        before and after the Halley encounter.  These showed
        that the net change in radial velocity was 23.05 +/- 0.05
        cm/sec during the encounter [EDENHOFERETAL1987B].
 
 
      On-Board Oscillator Drift
      -------------------------
 
        Measured linear drift of the on-board Giotto oscillator
        was about +1 Hz per minute [EDENHOFERETAL1987B].
 
 
      Operational Considerations
      ==========================
      Giotto Project management chose to operate only the X-band
      spacecraft transmitter during the Halley encounter.  This
      made extraction of the electron content in the comet
      environment extremely difficult, if not impossible
      [EDENHOFERETAL1987B].
 
      Instrument Section / Operating Mode Descriptions
       ================================================
      The instrument sections and modes for operation during the
      Halley encounter period are shown below:
 
 
          Section             Options         Mode
          ----------------------------------------
 
          Ground Equipment:
            Antenna           64-m            N/A
            Receiver          X-band          Open-Loop
                                                Closed-Loop
          Spacecraft Equipment:
            Antenna           High-Gain       N/A
            Transponder                       Non-Coherent
            Transmitter       X-band          N/A
 
      The closed-loop and open-loop receivers were operated at
      their maximum sampling rates (10 Hz and 50 kHz,
      respectively).
 
      During the pre- and post-encounter periods the system was
      operated in the two-way coherent mode to obtain both
      Doppler and ranging data.  Details on those operations
      are not available.

        