
 
  Instrument Host Overview
  ========================
    For most Galileo Orbiter experiments, data were collected by
    instruments on the spacecraft; those data were then relayed
    via the telemetry system to stations of the NASA Deep Space
    Network (DSN) on the ground.  Radio Science also required
    that DSN hardware participate in data acquisition on the
    ground.  The following sections provide an overview, first
    of the Orbiter and then of the DSN ground system as both
    supported Galileo Orbiter science activities.
 
  Instrument Host Overview - Spacecraft
  =====================================
    Launched 1989-10-18 by the Space Shuttle Atlantis, Galileo
    was the first spacecraft to use a dual-spin attitude
    stabilization system.  The rotor (or spun section) turned at
    approximately three revolutions per minute while the stator
    (or despun section) maintained a fixed orientation in space.
    This design accommodated the different requirements of remote
    sensing instruments (mounted on the stator) and fields and
    particles instruments (mounted on the rotor); spacecraft
    engineering subsystems were also mounted on the rotor.  The
    rotor and stator were connected by a spin bearing assembly,
    which conducted power via slip rings and data signals via
    rotary transformers.
 
    There were eleven subsystems and nine scientific instruments
    on the orbiter.  The spacecraft power source was a pair of
    radioisotope thermoelectric generators.  Propulsion was
    provided by a bipropellant system of twelve 10-newton
    thrusters and one 400 newton engine.  The command and data
    subsubsystem consisted of multiple microprocessors and a
    high-speed data bus.  The telecommunications subsystem was
    designed to transmit data to Earth at rates ranging from
    10 bps to a maximum of 134 kilobits per second at S-band
    and X-band frequencies.  The rotor had one 4.8 meter high-gain
    antenna and two low-gain antennas, but the high-gain antenna
    never deployed properly so data were returned from Jupiter at
    rates far below the design maxima using the low-gain antennas.
    The stator contained a radio relay antenna operating at L band
    for receiving data from the atmospheric probe, which is
    described elsewhere.
 
    Science instruments fell into two general categories.  Remote
    sensing instruments included:
         PPR       Photopolarimeter Radiometer
         NIMS      Near-Infrared Mapping Spectrometer
         SSI       Solid State Imaging Camera
         UVS/EUV   Ultraviolet Spectrometer/Extreme Ultraviolet
                     Spectrometer
 
    Instruments primarily designed for 'in situ' measurements
    included:
         EPD       Energetic Particles Detector
         DDS       Dust Detector Subsystem
         PLS       Plasma detector
         PWS       Plasma Wave Subsystem
         MAG       Magnetometer
 
    The Heavy Ion Counter (HIC) is an engineering subsystem which
    was added to the spacecraft to monitor high energy ions, but
    it is also being used to collect science data.
 
    The two Radio Science (RSS) experiments, Celestial Mechanics
    and Propagation, were conducted using equipment on both the
    Orbiter and on the ground.
 
    The mass of the Orbiter at launch was 2223 kg, of which 925 kg
    was usable propellant.  The Orbiter payload mass was 118 kg.
    Orbiter height was 6.15 m.
 
    Overall project management for Galileo was provided by the
    California Institute of Technology's Jet Propulsion Laboratory
    in Pasadena, California, which also built the orbiter.  Ames
    Research Center in Mountain View, California, was responsible
    for the development of the probe, which was supplied by Hughes
    Aircraft Company and the General Electric Company.  The Federal
    Republic of Germany provided the orbiter's main propulsion
    system, one complete scientific instrument one the orbiter
    (DDS), another on the probe (HAD), and major elements of others.
 
    For more information see [YEATESETAL1985; DAMARIOETAL1992]
 
    Platform Descriptions
    ---------------------
      The Rotor was the spinning section of the Galileo Orbiter
      and represented most of the spacecraft mass; it carried the
      high-gain communications antenna, the propulsion module,
      flight computers, and most support systems.  Two booms were
      attached to the Rotor; each was unfurled and extended
      automatically after launch.  The science boom extended to a
      distance of three meters from the spacecraft centerline;
      to it were mounted the EPD, DDS, HIC, and PLS instruments.
      The magnetometer boom extended outward eleven meters from
      the centerline and was attached to the science boom.  It
      carried the PWS antenna and two MAG sensors, one at the
      midpoint of the boom and the other at its outboard end.
      The EUV spectrometer was mounted on the Rotor bus.  For
      more information see [YEATESETAL1985; DAMARIOETAL1992]
 
      The Stator was the despun section of the Orbiter.  It was
      turned via an electric motor opposite to the rotation of the
      Rotor, so that it maintained a stable orientation in space.
      Attached to the Stator was a moveable scan platform which
      contained the remote sensing instruments: PPR, NIMS, SSI,
      and UVS.  The Probe and the Probe relay antenna were also
      attached to the Stator.  For more information see
      [YEATESETAL1985; DAMARIOETAL1992].
 
      The Rotor and Stator were connected by a spin bearing
      assembly (SBA), which conducted power via slip rings and
      data signals via rotary transformers.
 
    Telecommunications Subsystem
    ----------------------------
      The Telecommunications Subsystem was located in the Rotor
      section of the Orbiter.  It included elements for receiving
      uplink command signals and for transmitting downlink
      telemetry.  The uplink portion of the system received radio
      signals with command data at 2115 MHz and demodulated,
      detected, and routed those to the Command and Data System
      (CDS).  The downlink portion received telemetry data from
      the CDS and was designed to modulate S-band and X-band
      carriers at 2295 and 8415 MHz, respectively, at data rates
      as high as 134.4 kilobits per second (kbps).
 
      A 4.8 meter umbrella-like high-gain antenna (HGA) and two
      low-gain antennas (LGAs) were mounted on the Rotor.  The
      LGAs operated only at S-band.  One was mounted on a boom
      and was included primarily to improve Galileo's
      telecommunications during the flight to Venus (while
      the heat-sensitive HGA remained furled).  The other LGA was
      mounted at the top of the HGA.  The Stator contained a radio
      relay antenna operating at L-band for receiving Probe data
      during its atmospheric entry.
 
      On 1991-04-11 the HGA was commanded to unfurl; but telemetry
      showed that the motors had stalled with the ribs only partly
      deployed.  Months of tests and simulations followed, but
      without further progress in opening the antenna.  Engineers
      deduced that the problem most likely resulted from sticking
      of a few antenna ribs, caused by friction between their
      standoff pins and sockets.  The excess friction resulted from
      etching of surfaces after dry lubricant, bonded to the standoff
      pins during manufacture, was shaken loose during pre-launch
      transport.
 
      The mission was conducted using the LGA mounted on top of the
      HGA (the boom-mounted LGA was stowed after its service en
      route to Venus had been completed).  Without adaptations, the
      LGA data transmission rate at Jupiter would have been limited
      to only 8-16 bits per second (bps), compared to the HGA's
      134.4 kbps.  Onboard software changes, coupled with hardware
      and software changes at Earth-based receiving stations,
      increased the data rate from Jupiter by as much as 10 times,
      to 160 bps.
 
      'Lossless' data compression allows data to be recovered
      exactly, once they have been received on the ground.  'Lossy'
      data compression allows controlled corruption of the data
      through mathematical approximations but with significant
      increases in transmission rate.  Lossy compression was used
      with Galileo Orbiter imaging and plasma wave data to reduce
      volumes to as little as 1/80th of their original volumes.
 
      On the ground S-band communications capabilities were upgraded
      at the Canberra DSN tracking station (because Jupiter was at
      southern declinations during most of the Galileo tour,
      Canberra received more data from the Orbiter than the other
      DSN stations).  'Block V' receivers were installed at all
      stations; these could operate without need for a residual
      carrier, meaning all of the spacecraft radiated power could be
      assigned to carry its modulation.  Early in the tour, arraying
      of 34-m antennas with the 70-m antenna at each site was
      implemented; arraying of pairs of 70-m antennas and arraying
      with the 64-m CSIRO antenna at Parkes (Australia) were also
      used to increase data rates.
 
      The TCS as designed would have provided a dual channel
      downlink.  The high-rate channel would have provided a
      convolutionally coded, pulse-code modulated microwave channel,
      while a low-rate channel data was uncoded.  Downlink
      transmission of telemetry data would have been possible at
      S-band and/or X-band over a wide range of selectable data
      rates, including 134 and 115.2 kbps at Jupiter.
 
      Approximately 160 W (33 percent of total available) was
      provided for the combined S-band and X-band communications
      function.  Dual power level, traveling wave tube amplifier
      transmitters were to provide maximum S-band cruise data return
      and high-rate X-band data return from Jupiter while
      simultaneously satisfying dual-frequency tracking and
      radio science requirements.
 
      Several other features were incorporated in the
      telecommunications area, mainly to enhance radio science and
      navigation.  A noncoherent tracking mode was available which
      permitted the Orbiter to be commanded while the downlink
      frequency source was controlled by an auxiliary oscillator or
      an ultrastable oscillator -- providing short-term frequency
      stability of better than 5 parts in 10^12.  A differential
      downlink-only ranging mode was also available using one
      S-band and three X-band sine wave tones modulated onto the
      downlinks to enhance navigational accuracy.  A single X-band
      to S-band down-converter receiver was available for receiving
      X-band uplink signals to enhance radio science and the search
      for gravity waves.  These X-band capabilities were never used,
      however, because X-band was only available through the high
      gain antenna.  The capability existed to completely remove all
      telemetry modulation from the downlink carriers, thus
      maximizing atmospheric penetration depth during Earth
      occultations.
 
    Propulsion Subsystem
    --------------------
      The Galileo Retropropulsion Module (RPM system), located on
      the Rotor platform of the Orbiter, was supplied by the Federal
      Republic of Germany.  It was based on earlier bipropellant
      Symphonie designs.
 
      The Propulsion Subsystem provided all directed impulse for
      attitude control, trajectory correction, and Jupiter orbit
      insertion.  The propulsion functions consisted of spin rate
      control, fine turning to point the HGA to Earth, and
      orientation of the spacecraft for propulsive or science
      maneuvers.
 
      The RPM included four propellant tanks (two fuel tanks
      containing  monomethylhydrazine and two oxidizer tanks
      containing nitrogen tetroxide), two helium pressurant tanks,
      twelve 10-N thrusters (six each mounted on separate
      cantilevered booms), one 400-N engine, and necessary isolation
      and control elements.  At launch, the system was fully loaded
      with 932 kg of usable propellant and weighed about 1145 kg.
      Four of the 10-N thrusters were mounted in a direction to
      provide a functional backup for the 400-N engine.  The
      thrusters were mechanized on two separate branches providing
      redundancy for spin control, HGA pointing, and trajectory
      correction.  The 400-N engine was used three times -- all
      subsequent to Probe separation.
 
      Control of propellant to the 10-N thrusters and the 400-N
      engine was accomplished by opening and closing fuel and
      oxidizer solenoid latch valves via electrical signals from
      the attitude control system propulsion drive electronics.
      The propulsion drive electronics also provided the control
      signals for opening and closing the thruster and
      400-N engine valves.
 
    Command, Telemetry, and Data Handling Subsystem
    -----------------------------------------------
      Primary command, control, and data handling was performed
      by the actively redundant Command and Data Subsystem (CDS).
      Its major functions included receiving and processing
      real-time commands from Earth and forwarding them to
      appropriate spacecraft subsystems, executing sequences of
      stored commands (either as part of a normal preplanned
      flight activity or in response to the actuation of various
      fault recovery routines), controlling and selecting data
      modes, and collecting and formatting science and engineering
      data for downlink transmission.  The CDS architecture used
      multiple microprocessors and a high-speed data bus for both
      internal and user communication.
 
      A majority of the CDS electronics were located on the Orbiter
      Rotor platform in proximity to the data storage, science, and
      telecommunications equipment.  CDS Stator elements were
      limited to those necessary to support the Probe and relay
      radio hardware equipment, the remote sensing instruments
      mounted on the scan platform, the launch vehicle, and sequence
      operations.  Six 1802 microprocessors, memory units, and the
      data bus comprised the 'heart' of the CDS.  Four of the
      microprocessors (two high-level modules and two low-level
      modules) and four memory units contained a total of 144000
      words of random access memory (RAM) and were located on the
      Rotor platform along with supporting electronics.  The
      low-level modules of the remaining two microprocessors, each
      with 16K RAM, were located on the Stator platform.  The data
      bus comprised three dedicated busses.   The bus interface was
      used by all data systems -- that is, Orbiter science, the
      attitude and articulation control subsystem, and relay radio
      hardware receivers.
 
      Interfacing between Rotor and Stator portions of the CDS was
      accomplished via slip rings and rotary transformers mounted
      on the spin bearing assembly.  Efficient and effective
      communication among data systems was accomplished using a
      specifically defined protocol structure and real-time
      interrupt time slicing.  The protocol addressing schemes
      provided for either a relatively simple bus adapter that
      relied on direct memory access by the user's processor or a
      more complex bus adapter with direct memory access capability
      independent of the processor.
 
    Attitude and Articulation Control Subsystem
    -------------------------------------------
      The Attitude and Articulation Control Subsystem (AACS) was
      responsible for maintaining spin rate of the spacecraft;
      orienting the spin vector; controlling propulsion isolation
      valves, heaters, 10-N thruster firing, and 400-N engine
      firing; and controlling the science platform containing the
      remote sensing instruments on the Stator platform.
 
      Design of the AACS was profoundly influenced by science
      requirements and the various spacecraft operational
      configurations that had to be accommodated.  Configurations
      included the basic cruise dual spin configuration (Orbiter
      with Probe), dual spin without the Probe (for orbital
      operations) and 'all spin' configurations with and without the
      Probe for trajectory corrections at spin rates from 3 to 10
      rpm.
 
      The AACS incorporated many functional elements to meet the
      demanding  performance, lifetime, and reliability requirements
      of the mission.  The majority of the AACS functional elements
      were block redundant and located on the Rotor platform.
      Stator elements included those necessary for controlling the
      pointing and slewing of the scan platform, pointing the relay
      antenna, and interfacing with the Rotor section electronics.
 
      The central element of the AACS was the attitude control
      electronics (ACE) package that controlled the AACS
      configuration; monitored its health; performed executive,
      telemetry, command, and processing functions; provided spin
      position data to other subsystems; and provided AACS fault
      recovery.  The 'heart' of the ACE was a high-speed 2900
      ATAC-16 processor and memory containing 31K words of 16-bit
      RAM and 1K words of 16-bit read-only memory (ROM).
 
      ROM storage was used only for those functions required
      to safeguard the science instruments, switch to the
      low-gain antenna, and Sun point the Orbiter to permit
      ground commanding.  Activation of the ROM sequences
      occurred only when a loss of RAM was detected.
 
      The ACE also contained electronics necessary to interface with
      AACS peripheral elements in the Rotor section, the Stator
      electronics, and the CDS.  Interfacing between Rotor and
      Stator AACS elements was accomplished via rotary transformers
      located on the Spin Bearing Assembly (SBA).
 
      Other major AACS functional elements included:
 
      - a radiation hardened star scanner employing photomultiplier
        tubes for star field identification during in-flight attitude
        determination
 
      - linear actuators for raising or lowering the RTG booms to
        reduce wobble and maintain stability
 
      - acquisition sensors for attitude determination, spin rate
        sensing during launch, and Sun acquisition
 
      - propulsion drive electronics to control the RPM latch valve,
        thrusters, and 400-N engine valves
 
      - a spin bearing assembly to provide the mechanical and
        electrical interface between Rotor and Stator sections of
        the Orbiter as well as to provide despun orientation
 
      - gyros mounted on the Stator scan platform to control platform
        articulation and stabilization.
 
      - accelerometers mounted on the Stator platform diametrically
        opposite to each other and aligned parallel to the Orbiter
        spin axis to measure velocity changes during propulsive burns
 
      - a scan actuator subassembly to provide scan platform cone
        actuation and positioning information.
 
      After launch vehicle separation and RPM pressurization, the
      spacecraft assumed the 'all-spin' configuration.  This was
      used frequently during the mission and for all propulsive
      maneuvers to provide stabilization.  In all-spin configuration
      for 10-N thruster burns, the entire Orbiter would spin at
      roughly 3 rpm; for 400-N engine burns, the Orbiter would
      spin at 10 rpm.  This configuration was also used during
      science calibration target observations by the remote sensing
      science instruments.
 
      For most of the mission, the AACS operated in the cruise mode,
      in which the Orbiter operated in the dual-spin configuration
      with the Rotor platform inertially fixed.  Major AACS
      functions performed in this mode were wobble control, high-gain
      antenna pointing, attitude determination, and spin rate control.
 
      The final AACS mode was the inertial mode.  Transition to this
      mode was from the cruise mode with gyros active.  While in this
      mode the AACS performed functions such as closed-loop commanded
      turns using the RPM thrusters, accurate pointing and slewing of
      the scan platform, and closed-loop control for wobble angle
      compensation.
 
    Electric Power Subsystem
    ------------------------
      Electrical power was provided to Galileo's equipment by two
      radioisotope thermoelectric generators.  Heat produced by
      natural radioactive decay of plutonium 238 dioxide was
      converted to electricity (570 watts at launch, 485 watts at
      the end of the mission) to operate the Orbiter equipment for
      its eight-year baseline mission.  This was the same type of
      power source used by the two Voyager spacecraft missions to
      the outer planets, the Pioneer Jupiter spacecraft, and the
      twin Viking Mars landers.
 
    Spacecraft Coordinate Systems
    -----------------------------
      The Rotor coordinate system consisted of three mutually
      perpendicular axes: Xr, Yr, and Zr.  The Zr axis was
      nominally parallel to the spin bearing assembly (SBA) axis
      and passed through the center of the Rotor with +Zr directed
      opposite to the HGA boresight direction.  +Yr was normal to
      Zr and was directed toward the science boom.  +Xr was normal
      to both Yr and Zr and formed a right-handed system.  The
      angular momentum vector for the spinning spacecraft was in
      the +Zr direction.
 
             \            / HGA
              \          /
               \   /\   /
              ------------
             |   ROTOR    |-------------------\    Science and MAG
             |            |-------------------/         Boom
              ------------
                SBA |
                    |              ---> +Yr
 
                   +Zr
 
      The Stator coordinate system consisted of three mutually
      perpendicular axes: Xs, Ys, and Zs.  The Zs axis was
      nominally parallel to the SBA axis and passed through the
      center of the Stator with +Zs directed opposite to the HGA
      boresight direction (+Zs was parallel to +Zr).  +Ys was normal
      to Zs and was directed opposite to the scan platform direction.
      +Xs was normal to both Ys and Zs and formed a right-handed
      system.
 
                   SBA |
                 ------------
                |   STATOR   |-------------------\      Scan
                |            |-------------------/    Platform
                 ------------
                       |
          +Ys <---     |
 
                      +Zs
 
                         -Zr,-Zs
 
                            |
                            |                              /
                            |                          __(o)-._
                            |                     _.--_/\/'     -
                                            ....-   _/\/'
                         __---__                  _/\/'
                        '-_/|\_-`               _/\/'
                         __|]]_               _(o)'
                   __---- /|||\----__       _/\/'    +Yr,-Ys
                _--\ __----------__ /--_  _/\/'     /
               /  _--\    __|___  /--_  \/\/'     /
               \-/   __-\-  |   /--   \/\/'     /
                `\--/--___\-|-/___-\-///'     /
                ,_`-`---| |___| |__/\/'     /
              ,--/---===_/||\ -`---(o)    /
           ,/--/ ,-, ,--('||))|---|)\|\
        ,/--/    |]]=\== \_|/ |___]-)\|\,--
      /--/:      '-'  `__-------_=]=  \|[[[
   [=[=/! :            [_-------_\==   \[[[
        '              //_-- --_[=--     [-_ ---------- +Xr, -Xs
    -Xr,+Xs ------- ---`\      /[_]'     \/_\_
                  /'|`\[|`\_ //'          [  ]=
                  `-[-'[]_] -             [___]=]
                        ---
                    /       |
                  /         |
                /           |
              /             |
          -Yr,+Ys           |
 
                         +Zr,+Zs
 
      Figure - Perspective view of Galileo Orbiter spacecraft (Should
      be viewed in a mono-spaced font such as Courier)
 
      The scan platform coordinate system consisted of three mutually
      perpendicular axes: L, M, and N.  The platform had a primary
      mounting plane which was established by three mounting points
      on the platform.  Two reference pins (Pin 1 and Pin 2) were
      installed on the primary mounting plane to establish platform
      alignment.  The origin of the coordinate system was at the
      intersection of the center line of Pins 1 and 2 and the primary
      mounting plane.  The coordinate axis L, defining look direction,
      was parallel to the SSI instrument and passed through the center
      line of Pins 1 and 2.  Coordinate axis M was in the primary
      mounting plane, perpendicular to L, and passing through the
      origin.  Axis N was mutually perpendicular to both L and M such
      that L = M x N.  Individual instruments were assigned
      subscripted Li, Mi, Ni coordinate systems such that an
      instrument pointing vector was specified by direction cosines
      of its coordinate axes Li, Mi, Ni with respect to the platform
      coordinates L, M, N.
 
    Spacecraft Safing Summary
    -------------------------
      Throughout the mission there have been a number of occasions
      when the spacecraft detected a fault condition onboard and
      configured itself to a safe state.  At that time, all onboard
      sequences are cancelled, and a number of science instruments
      are powered off.  The following table lists the time of these
      'safing' events, which stored sequence was aborted, and the
      reason that the spacecraft entered its fault protection
      routines.  The times of the events have been extracted from
      different sources.  Some times are known exactly and others
      have uncertainties of up to 5 minutes.  The most uncertain
      times are indicated with an *.
 
      Date       SCET (UTC)        SEQ    Cause of safing
      1990-01-15 90-015/22:52*     EV-5   star scanner calibration
      1991-03-26 91-085/13:31:18   VE-14  B-string CDS bus reset
      1991-05-03 91-123/05:26      n/a    A-string CDS bus reset
      1991-07-20 91-201/02:09:00   n/a    A_string CDS bus reset
      1993-06-10 93-161/16:53:05   EJ-1   A-string CDS bus reset
      1993-06-17 93-168/18:22:04   n/a    A-string CDS bus reset
      1993-07-10 93-191/20:16:58   EJ-2   A-string CDS bus reset
      1993-07-12 93-193/01:37*     n/a    A-string CDS bus reset
      1993-08-11 93-223/22:04:40   EJ-2'  A-string CDS bus reset
      1993-09-24 93-267/14:14:54   EJ-3   A-string CDS bus reset
      1994-09-14 94-257/03:10:51   EJ-7B  DMSMRO memory failure
      1994-09-16 94-259/16:38*     n/a    CAP privileged error
      1995-02-04 95-035/17:44:39   n/a    Phase 1 In-Flight Load-planned
      1996-01-05 96-005/21:51:12   J0C-A  SITURN cmd constr. violation
      1996-05-18 96-139/01:26*     n/a    Phase 2 In-Flight Load-planned
      1996-08-24 96-237/15:30:32   G01-C  timing overrun from DACs
      1997-12-22 97-356/16:52*     E12BHG AACS Anomaly
      1998-05-28 98-148/20:21:26   E14BGD Safing during OTM-47
      1998-07-20 98-201/17:35:46   E16AKE Despun BUS POR
      1998-11-22 98-326/05:24:13   E18AFE Simultaneous 2 string CDS bus reset
                                          two resets: 98-326/05:24:13.102 and
                                          98-327/01:29*
      1998-12-09 98-343/17:05:10   E18BFE Sequence stopped by B18T24 RBS
      1999-02-01 99-032/05:41:33   E19AHC SUNACQ Failure
      1999-10-10 99-283/09:17:06   I24AGE B-String CDS bus reset
      1999-11-26 99-330/22:00:02   I25ADF B-String code error in box 5
                                          start ADD
      2000-02-24 00-055/12:00:13   I27ADC A&B string CDS bus reset
      2002-01-17 02-017/13:41:09   I33AFE A-string CDS bus reset (parity err)
      2002-02-16 02-047/20:51:00   I33BED A-string CDS bus reset
      2002-10-02 02-275/03:41:22   I33EDE Commanding Error
      2002-11-05 02-309/06:35:36   A34AHG Radiation Failure
 
      The most common cause of spacecraft safing was from a CDS despun
      bus reset of either the A-string or B-string.  It has been
      determined by analysis that there has been current leakage
      somewhere in the spacecraft power bus, and that the resulting
      bus imbalances are most likely caused by brush debris forming
      high-resistance leakage paths across the brush armatures in the
      spin bearing assembly.  These paths are formed and then
      'blown open' before the resistance becomes low enough to permit
      significant current flow.  In some cases the brush was 'lifted'
      briefing while debris paths were causing power to 'touch' the
      brush and this tripped a reset signal in the CDS.  Onboard fault
      protection 'safes' the spacecraft when the reset trips
      [ONEIL1991].  No damage has occurred on the spacecraft as a
      result of these trips, but the spacecraft operations are
      disrupted until the onboard sequences and spacecraft state can
      be restored from the ground.  In April of 1999 a change was made
      to the CDS flight software that allows it to detect and
      autonomously recover from despun bus resets.  With this new
      software enabled, the CDS strings do not 'go down', 'safing'
      does not execute and the onboard sequences continue.
 
      On September 13, 1994 a memory cell in the CDS failed during the
      playback of Shoemaker-Levy 9 recorded data and resulted in
      spacecraft safing to be entered twice.  After 12 days the
      spacecraft was reconfigured back to normal operations.  The
      failed memory cell was located in a bulk storage (DBUM-1A)
      module of the CDS, and was only used during tape recorder/memory
      readout playbacks and other short term storage of data
      [ONEIL1995].
 
      Following the successful insertion into Jupiter orbit in
      December 1995, a spacecraft turn was attempted on January 5,
      1996.  The spacecraft was in a non-standard configuration
      following the JOI maneuver which resulted in an incompatibility
      between the turn design and the spacecraft state.  The
      spacecraft entered safing, but was recovered shortly afterwards.
 
      On August 24, 1996 the spacecraft went into safing due to a
      timing overrun condition in the CDS, ending any further data
      return from the G1 encounter.  The timing overrun was traced
      to the transmission of 4 Delayed Action Commands which stressed
      the limits of the CDS running the new Phase 2 flight software.
      By September 1, the spacecraft had been returned to normal
      operations and the G2 encounter sequence began on schedule
      [ONEIL1996].
 
      Twice during the Prime Mission, during the loading of new
      flight software for Phase 1 and Phase 2, the spacecraft was
      purposely commanded to trigger the safing response in order to
      put all subsystems in a known state prior to the load.
 
      On May 28, 1998 the spacecraft entered safing for the first
      time in the Galileo Europa Mission.  Safing occurred during
      the maneuver, OTM-47, inbound to the Europa 15 encounter.  The
      spacecraft executed the majority of the maneuver before a
      sequence timing error created an AACS command constraint
      violation which caused the spacecraft to abort the on-board
      sequence and safe itself. The Science Virtual Machine was
      recovered on 98-149, and a mini-sequence was uplinked to
      turn on the science instruments and match the spacecraft
      states to the E15A sequence.
 
      On February 1, 1999, four hours after completing the close
      approach science recordings, the spacecraft entered safing
      during a sun acquisition turn designed to move the spacecraft
      from the science data taking attitude back to the nominal
      earth pointed attitude.  It appears that the cause of the sun
      acquisition halt was the result of a failure of the two
      acquisition sensors to provide the complete overlap they
      were design for.
 
      On October 10, 1999 the spacecraft entered safing when high
      radiation on approach to the Io 24 encounter caused an error
      in the CDS B-string memory.  The hardware error causing the
      safing was a memory read error in the CDS B string High
      Level Module - the 'executive controller' for the CDS B
      string.  Because the error was detected by the CDS bus
      controller (and not the microprocessor), this is likely to
      be an error in memory used for data buffers. Within 18 hours
      of safing the I24 sequence was regenerated, loaded onboard,
      and the 75% of the I24 encounter data was acquired.
 
     During the extended mission five of the anomalies were caused by
     CDS bus resets that were nominally handled with software changes
     implemented previously.I33EDE where the spacecraft entered safing
     on October 2, 2002 was due to commanding error on the ground
     during fault protection changes (ISA 11007).
 
     In A34A an anomaly occurred on November 5, 2002 at 06:19 UTC, when
     the spacecraft flew within 160 km of the surface of Amalthea. The
     speed of the spacecraft relative to Amalthea was approximately
     18.4 kilometers per second (41,000 miles per hour), taking less
     than 15 seconds to pass by.  Approximately 17 minutes after
     closest approach, the intensity of the radiation caused a failure
     in computer circuitry that handles timing of the events on the
     spacecraft. This caused the computer to switch to the CDS B-string
     and go into safe mode. There were also several additional faults
     which triggered repeated requests to place the spacecraft in safe
     mode.
 
  Instrument Host Overview - DSN
  ==============================
    Galileo Radio Science investigations utilized instrumentation
    with elements both on the spacecraft and at the NASA Deep Space
    Network (DSN).  Much of this was shared equipment, being used
    for routine telecommunications as well as for Radio Science.
 
    The Deep Space Network was a telecommunications facility
    managed by the Jet Propulsion Laboratory of the California
    Institute of Technology for the U.S. National Aeronautics and
    Space Administration.
 
    The primary function of the DSN was to provide two-way
    communications between the Earth and spacecraft exploring the
    solar system.  To carry out this function the DSN was equipped
    with high-power transmitters, low-noise amplifiers and
    receivers, and appropriate monitoring and control systems.
 
    The DSN consisted of three complexes situated at approximately
    equally spaced longitudinal intervals around the globe at
    Goldstone (near Barstow, California), Robledo (near Madrid,
    Spain), and Tidbinbilla (near Canberra, Australia).  Two of
    the complexes were located in the northern hemisphere while
    the third was in the southern hemisphere.
 
    The network comprised four subnets, each of which included
    one antenna at each complex.  The four subnets were defined
    according to the properties of their respective antennas: 70-m
    diameter, standard 34-m diameter, high-efficiency 34-m diameter,
    and 26-m diameter.
 
    These DSN complexes, in conjunction with telecommunications
    subsystems onboard planetary spacecraft, constituted the major
    elements of instrumentation for radio science investigations.
 
    For more information see [ASMAR&RENZETTI1993].

        