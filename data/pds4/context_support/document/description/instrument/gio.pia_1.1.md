
 
    Instrument Overview
    ===================
      Dust is collected from the ram direction of the
      spacecraft (i.e., parallel to the spin axis)
      through an adjustable, elliptical aperture which
      has a collecting area variable between 5 cm^ and 1
      mm^2 in order to limit the rate to < 500 per
      second, the maximum with which the instrument can
      cope.  The particles, moving with roughly the
      encounter speed of 69 km/second, are then incident
      on an oblique target, the entrance aperture
      projecting to a circle adjustable up to 35 mm
      diameter.  Particles moving this fast can cause: -
      a crater in the target - partial or complete
      destruction of the particle, depending on the speed
      - emission of secondary particles - a flash of
      light - release of neutrals, electrons, and
      positive and negative ions.
 
      The target is a 10-micron thick roll of platinum
      foil doped with 5% silver.  The roll is 700mm by
      55mm and is unrolled and transported across the
      entrance aperture at a rate of 0.6mm/sec whenever
      the count- rate of dust particles exceeds a certain
      level and can also be unrolled with commands in the
      telemetry from Earth.  This transport ensures that
      the portion of the target in use is always clean.
 
      Four different detectors are used to sense the
      impact of a particle and initiate the collection of
      data for a mass spectrum.  Two detectors, although
      shielded, are relatively exposed to the outside
      environment, while the other two are completely
      shielded from the outside environment.  The impact
      of a particle onto the detector can cause
      measurable pulses on any of these four detectors
      but typically does not cause a detected pulse on
      all of them. 1.  A photomultiplier (PMT) senses the
      light-pulse produced on the impact of a particle
      onto the target.  The output of the PMT is fed
      through an rms noisemeter which is used to adjust
      the triggering threshold automatically.  Although
      shielded, ambient light fluctuations can reach the
      PMT by scattering.  (Signal PM) 2.  Pulses of
      positive ions are sensed as a pulse at the target
      itself, which is held at +1kV.  This sensor is also
      fed to an rms noise meter which adjusts the
      discriminator.  Since the target is exposed to
      ambient plasma from the ram direction, it is
      sensitive to external fluctuations.  (Signal TG) 3.
      Pulses of electrons are collected at the 'catcher
      channel', an anode to the side of the main path for
      ions.  This detector is well shielded from the
      external environment so that pulses here should all
      correspond to real events.  (Signal CA) 4.  Pulses
      of positive ions are also sensed at the
      accelerating grid, held at -2kV, which accelerates
      the ions into the mass spectrometer.  This sensor
      is also well isolated from the external
      environment.  (Signal AC) Because a dynamic range
      of at least 4 decades was desired (to detect
      particles from 0.1 to 10 microns), the amplifiers
      on these front-end channels can be switched between
      two gain ranges, each three decades and separated
      by a factor 100 (i.e.  gains 1-1000 and 100-100,000
      in arbitrary units).  The outputs of the amplifiers
      are each monitored by three single-channel
      discriminators set at relative levels of 1x, 10x,
      and 100x.
 
      The mass spectrometer operates on the
      time-of-flight principle, accelerating all ions to
      a constant energy, thereby sorting them to
      different velocities dependent on the mass.  Since
      each particle produces a burst of ions in a very
      narrow interval of time, the arrival time of the
      ions at the detector is related directly to the
      mass of the ions.  The positive ions, after passing
      the accelerator grid (-2 kV), are decelerated to an
      energy of 1 kV by a grid at the entrance to the
      first drift tube.  While passing along this first
      drift tube, the ions are focussed by an ion lens to
      remove the transverse dispersion in the motions.
      The charge induced on the lens by the passage of a
      pulse of ions is recorded as an additional monitor
      of the existence of a real particle event.  (Signal
      MO) The ions then enter a reflector which serves as
      a first order energy focussing device to remove the
      dispersion due to the initial energies which the
      ions have from the formation process (up to about
      70 eV).  They then pass along the second drift tube
      which contains a second ion lens.
 
      At the end of the second drift tube, the ions are
      incident on a multiplier with 20 dynodes.  At this
      point, the ions from a single initial particle
      impact have been sorted in time by their masses
      with ions having masses from 1 to 110 amu arriving
      roughly from 4 to 42.5 microseconds, mass being
      proportional to the square of the arrival time.
      The output of the multiplier is recorded by
      converting the signals from dynodes 5, 8, 11, 14,
      17, and 20 to a logarithmic scale and then summing
      these six signals.  This yields an output signal
      with 5 decades of dynamic range.  This signal is
      digitized and stored in a memory together with the
      digital output of a time^2 signal generator which
      provides an index of the mass of the ions.
 
      Instrument Manufacturer	:
              Max-Planck-Institut-fuer-Kernphysik
 
       Platform or Mounting Name :Spacecraft body
 
    Science Objectives
    ==================
      The objective is the in-situ measurement of the
      chemical and physical properties of cometary dust
      particles.  The chemical compositions and masses of
      individual particles will be measured.  Their
      impact rate, determined as a function of position
      relative to the comet's nucleus, will be used to
      establish the mass distribution and production
      characteristics of cometary dust.  In particular,
      the goals are to: - determine the elemental
      abundance of individual particles and to ascertain
      whether there are distinct particle classes that
      differ from each other chemically - investigate
      whether the elemental particle composition depends
      on the distance from the nucleus, and to look
      specifically for the effects of ice evaporation
      from particle surfaces - gain insight into the
      molecular composition of the impacting particles,
      with emphasis on possible evidence of organic
      matter - determine specific isotopic ratios, such
      as 6Li/7Li, 10B/11B, 12C/13C, and to try to
      establish the origin of the comet's particulate
      matter - study the mass distribution function of
      impacting particles, derive the total dust
      production rate in the measured mass range, and
      compare the latter with theoretical models -
      determine the extent of the dust envelope as a
      function of particle mass and analyze possible
      asymmetries in impact rate to model anisotropy
      effects in the dust's production.
 
    Calibration Description
    =======================
      The multiplier is calibrated in flight by an EPID
      (Electronic Pulse Induced Desorption) ion
      generator.  This provides ions of two masses with a
      known intensity ratio.  The mass scale is
      calibrated against the value from the t^2 generator
      after receipt of the telemetry by identifying
      specific lines, typically the two lines due to
      silver produced from the target.
 
    Electronics
    ===========
      The experiment runs entirely autonomously and was
      designed to collect data for a period of 4 hours,
      with nearly all the events occurring during the 20
      minutes centered on the time of closest approach.
      The control is implemented with an RCA 1802
      microprocessor and several PROMs.  A number of
      parameters about the previous measurements are
      maintained in order to adjust the operating modes
      of the system.  The normal state of the system is
      one in which it is waiting for a particle impact to
      occur.  If no impact occurs for a second, the
      internal parameters are updated.  These parameters
      include: i.  the impact rate for all events (rate
      IR, number of events per second) ii.  the impact
      rate for large events, i.e.  events in which the
      100x threshold is exceeded in one of the front-end
      channels (rate IRL, number of events per second)
      iii.  the impact rate for events with mass spectra,
      i.e.  events in which a minimum number of ions are
      counted in the mass spectrum (various rates are
      stored, IR4 is the rate of events of classes 4
      through 7 as defined below) iv.  the onboard time
      counter v.  the number of EDFs transmitted per
      second.  After updating the parameters, whether
      after an event or after the 1-second interval
      without an event, the system processes any commands
      received, sets the spectrum mode (0 to 3), enables
      the trigger channels, sets the number of front-end
      coincidences required to trigger an event, adjusts
      the sensitivity settings, sets the high voltage on
      the multiplier, adjusts the shutter position, and
      moves the target if motion is required.
 
      All instrument parameters are preset when the
      instrument is turned on.  Values stored in PROM are
      used when the instrument is turned on for the first
      time on spacecraft power.  When the instrument is
      turned off but spacecraft power is still in place,
      all instrumental parameters are stored in RAM and
      these values are used when the instrument is
      reactivated.
 
      Since small particles may not trigger all of the
      front-end channels, at low count rates an event is
      triggered whenever any single front-end channel is
      triggered.  At higher count rates additional
      front-end channels must be triggered.  Specifically
      whenever IR4 > 10/second and IR > 2*IR4, a
      coincidence with an additional front-end channel is
      required.  Whenever the triggering rate of a
      front-end channel exceeds the rate at which the
      instrument can process events, the noise-detection
      system on the front-end channel adjusts the
      triggering level upwards.  If this level exceeds,
      3.2 volts, that channel is disabled.  Normally, the
      front-end channel amplifiers are set to the high
      sensitivity range.  If all three front-end channels
      become disabled due to excessively high count
      rates, the amplifiers are automatically set to the
      low sensitivity range and reenabled.  All front-end
      channels (AC, PM, TG, CA, and MO) are set to the
      low sensitivity mode if there are enough events to
      fill the telemetry capacity, specifically if IRL >
      TMR + 3.
 
      The mode in which spectra are recorded also depends
      on the counting rate.  Every 26th event is always
      recorded in mode 0.  The mode for the remaining
      spectra (1 to 3) is increased by 1 whenever IR4 >=
      2*TMR or IR4 > 128.  It is reduced by 1 whenever
      IR4 < 2*TMR.  These mode changes are implemented at
      4-second intervals, if required.
 
      The shutter aperture is also controlled by the
      microprocessor through a stepping motor which takes
      71 steps to go from 500 mm^2 to 1 mm^2 with the
      default position ('zero' position) at 457 mm^2.
      The positions at 500 m^2 and 52.4 mm^2 are sensed
      by microswitches.  The control algorithm is based
      on the value of IR4 (event rate for classes 4 to
      7).
 
      IR4 <  15: open by 9 steps
      IR4 <  30: open by 6 steps
      IR4 <  60: open by 3 steps
      IR4 >  90: close by 3 steps
      IR4 > 180: close by 6 steps
      IR4 > 254: close by 9 steps
 
      Since only one motor is allowed to be moving at any
      given time, the shutter motor has priority over the
      target motor.
 
      The target motion is also controlled by the count
      rate, unless the shutter is also moving, starting
      when IR4 > 60 and stopping when IR4 < 30.  The rate
      of motion is fixed at 0.6 mm/s.
 
      Events are classified by the data processing system
      as follows: 1.  Events with only 1 front-end signal
      2.  Events with a coincidence between 2 front-end
      channels 3.  Events that have a coincidence with
      all 3 front-end channels but still do not exhibit a
      mass spectrum 4.  Events that have a minimum of 52,
      46, or 10 entries in the spectrum for modes 1, 2,
      and 3, respectively 5.  Events that have a minimum
      of 54/48/12 entries in the mass spectrum but not
      more than 228/148/140 entries and which also have a
      minimum of 26/21/6 entries in the mass range 6-58
      amu. 6.  Class 5 events that also have at least 2
      entries of at least 0.2 full scale in the range 5-8
      amu. 7.  Class 5 events that have a minimum of
      34/27/12 entries in the mass window but not more
      than 93/49/46 8.  Events from the statistical
      sample 9.  test pulses 10.  events from the AHV
      routine (calibration) 0.  Events that have already
      been transferred to the telemetry system.  When a
      new event is classified, the controller searches
      first for an empty section of memory in which to
      store it.  Failing that, it searches for an event
      of lower class to be overwritten.
 
      The high voltage applied to the multiplier controls
      the sensitivity and the dynamic range of the mass
      spectra.  The value is set by telecommand to one of
      128 discrete values between 0 and 4500 V.
 
 
    Instrument Operating Mode Descriptions
    ======================================
 
      Mode 0
      ------
        15 MHz Mode.  In this mode, the output of the
        multiplier is digitized and recorded in the event
        memory every 66.66 nanoseconds.  The output of
        the t^2 generator is not recorded in this mode.
 
      Mode 1
      ------
        Max/Min Mode.  At each maximum of the signal
        appearing at the MP output, a sample is taken of
        the multiplier output and of the t^2 generator.
        An additional sample is taken 1/2 mass unit after
        each maximum in the multiplier output.  This
        should correspond to the minimum between two
        adjacent masses.  In addition, an sample is taken
        every 1.13 microseconds if no other maximum has
        occurred in that interval.
 
      Mode 2
      ------
        Max/Time Mode.  For each maximum in the MP
        output, a sample is taken of the MP output and of
        the t^2 generator.  In addition, a sample is
        taken every 1.13 microseconds if no other maximum
        has occurred in that interval.
 
      Mode 3
      ------
        Max Mode.  This is the same as mode 2 except that
        samples are taken only after 8.6 microseconds.
 
 

        