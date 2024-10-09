
 
  Instrument Overview
  ===================
    A suite of 12 diagnostic sensors was integrated into the Ion
    Propulsion System (IPS) Diagnostic Subsystem (IDS). Two of
    the instruments were the plasma wave antenna and search coil.
    Time domain and spectrometer data were obtained from both sensors.
 
  Scientific Objectives
  =====================
    The NASA Solar Electric Propulsion (SEP) Technology Applications
    Readiness (NSTAR) ion thruster operating aboard Deep Space 1
    generates an environment that includes electrostatic, magnetic and
    electromagnetic fields, charged particles, and neutral particles.
    The thruster environmental components, in combination with the
    natural space environment and the space vehicle, produce the
    'induced environment.' The induced environment has the potential
    of impacting the performance of spacecraft subsystems or science
    sensors. The objective for the Ion Propulsion System (IPS)
    Diagnostics Subsystem (IDS) flown on DS1 was to characterize these
    environments within significant resource constraints.  Since the
    measured effects of the IPS on the spacecraft environment proved
    to be benign, the IDS was reprogrammed during flight to collect
    solar induced wave data and signals caused by dust impact events
    during the encounter.
 
  Detectors
  =========
    Search Coil Magnetometers - Two single-axis search coil
    magnetometers were mounted on the boom. One search coil is a new
    technology miniaturized sensor developed in the JPL MicroDevices
    Laboratory that uses a field rebalance technique for measurement.
    The second search coil was a build-to-print of the Orbiting
    Geophysical Observatory (OGO-6) single-axis sensor manufactured by
    Space Instruments, Inc., Irvine, California. The second search
    coil sensor was apparently damaged at the launch site by large AC
    fields and was inoperable during the DS1 mission. Flight
    measurements were performed with a measurement bandwidth over 10
    Hz to 50 kHz. The full-scale range at 200 Hz is 100 nT with a
    resolution of 1 pT. The AC magnetic fields were characterized as a
    discrete power spectrum with four measurement intervals per
    decade. The transient waveform for 'events' was also captured with
    a sampling rate of 20 kHz for 500-msec windows. The transient
    recorder was commanded at prescribed intervals.
 
    Plasma Wave Antenna - A simply deployed dipole plasma wave antenna
    (PWA) with adjustable-gain preamplifier was mounted onto the boom.
    The PWA is a pair of low-mass Ni-Ti shape-memory alloy (SMA)
    metallic strips with a tip-to-tip separation of 2 m. The PWA
    deployment occurs upon exposure of the stowed SMA coiled ribbon to
    the Sun. Within 2 hours, the PWA antenna slowly extends to its
    deployed position. The PWA is connected to a low-noise
    preamplifier that was built by TRW, Redondo Beach, California.
    Flight measurements were performed in a low-frequency domain of 10
    Hz to 100 kHz and a high-frequency domain of 100 kHz to 30 MHz.
    The low-frequency domain is characterized by a voltage-swept band
    pass filter with a minimum of four measurements per decade with an
    amplitude range of 100 micro-V/m to 1000 mV/m. The high-frequency
    domain is characterized with a minimum of four measurements per
    decade with the same amplitude range as the low-frequency domain.
    Transient waveform measurements were performed at a 20-kHz
    sampling rate with a 500-msec circular buffer.
 
  Electronics
  ===========
    IDS Architecture - IDS consists of two interconnected hardware
    units: a Diagnostics Sensors Electronics Unit (DSEU) and a Remote
    Sensors Unit. The IDS is an integrated package with one +28VDC and
    dual MIL-STD-1553 serial communications interface to the DS1
    spacecraft. The DSEU has 2 data sampling systems, a contamination
    monitor, and a fields monitor (processor). The data provided was
    processed using a Fields Measurement Processor (FMP). The FMP
    consists of 3 boards: processor, spectrometer, and magnetometer.
    The magnetometer is not discussed here. The spectrometer board
    amplifies both the search coil and plasma wave signals for time
    domain sampling and provides two identical low frequency, voltage
    controlled tuned band passed filters. These two filters yield the
    search coil and plasma wave data. For the plasma wave sensor, the
    spectrometer has a bank of selectable high frequency band pass
    filters.
 
  Operational Modes
  =================
    The IDS contains two separate processor elements: the DSEU
    microprocessor and the fields measurement processor
    (FMP)[HENRYETAL2000]. The DSEU microprocessor supports the
    communications interface with DS1, controls serial communications
    with the FMP, and digitizes and controls the sensors within the
    RSU. The IDS operates as a remote terminal on the DS1 MIL-STD-1553
    serial bus. Telemetry from the RSU sensors is collected on 2-
    second intervals and placed in selected 1553 subaddresses for
    transmission to DS1. Configuration messages are transmitted to the
    DSEU to select active sensors within the RSU and FMP and to
    establish sweep ranges and gains for these sensors. Configuration
    messages to the FMP are passed through the DSEU to the FMP
    directly. The DSEU polls the FMP for data at half-second
    intervals. In the typical FMP scan mode operation, a block of
    sensor data is transmitted at 16-second intervals. Occasionally,
    the FMP will transmit 0.5-second waveforms sampled at 20 kHz from
    the plasma wave and search sensors and 120 s 20 Hz from the flux-
    gate magnetometers. These 'burst' events can be commanded or
    initiated via internal triggering within the FMP.
 
  Location
  ========
    IDS was located adjacent to the ion engine on the DS1 spacecraft.
 
  Measured Parameters
  ===================
    The IDS Plasma Wave Spectrometer characterized the electrostatic
    wave and electromagnetic noise environments produced by the IPS
    and other DS1 subsystems. A large volume of both spectral and
    time-domain data were obtained throughout the DS1 mission,
    especially during IPS operations. There is not a direct
    correlation of noise amplitude with IPS operating power. The IPS
    noise levels are bounded as follows:
 
    o IPS E-field continuous noise: < 1 V/m, < 15 MHz.
    o IPS E-field transient: < 2 V/m for < 1 ms.
    o IPS B-field continuous noise: < 10 micro-T, < 10 kHz.
    o IPS B-field transient: < 200 micro-T for < 2 ms.
 
    Limits for the major DS1 subsystem noise sources, namely the
    hydrazine reaction control subsystem (RCS) thrusters and engine
    gimbal actuators (EGAs), are bounded by:
 
    o RCS thruster E-field transient: < 5 V/m for < 10 ms.
    o RCS thruster B-field transient: < 200 micro-T for < 40 ms.
    o EGA B-field continuous noise: < 10 micro-T, at 100 Hz.
    o EGA B-field transient: < 100 micro-T for < 1 s.
 
  References
  ==========
    Henry, M.D., D.E. Brinza, A.T. Mactutis, K.P. McCarty, J.D.
    Rademacher, T.R. vanZandt,R. Johnson, G. Musmann, and F. Kunke,
    NSTAR Diagnostics Package Architecture and Deep Space 1 Spacecraft
    Event Detection, IEEE 2000 Aerospace Conference Paper, 11.0502,
    2000.

        