
 
  Instrument Overview
  ===================
   The Lunar Prospector Engineering 'instrument' consists of the
   spacecraft attitude control system (ACS), the command and data
   handling (CDH) subsystem, and the communications subsystem (COM).
   Various data products from each of the systems have been included in
   the archive of the NASA level 0 data [BINDERETAL1998].
 
 
  Science Objectives
  ==================
    The engineering systems support science rather than acquire science
    data. The individual systems were designed to meet the accuracy
    requirements of the science payload.
 
 
  Platform Mounting Descriptions
  ==============================
    The communications antenna is mounted along the spacecraft spin axis
    (+Z). The sun pulse and limb crossing sensor mounting locations were
    not provided to the archive.
 
 
  Operational Considerations
  ==========================
    The instantaneous spin rate varies as the spacecraft passes into and
    out of the Moon's shadow and after each spacecraft maneuver. When the
    spacecraft is in eclipse, the sun pulse is estimated using the
    pre-eclipse measured spin rate, the calibrated spin rate change
    during eclipse, and limb sensor telemetry.
 
  Operation and Sampling Modes
  ============================
    The communication system consists of an S-band transponder, an omni
    antenna with 3-pi steradian antenna pattern for uplink and downlink,
    and a medium gain antenna for downlink.  The engineering-only
    downlink data rate is 300 bps and the science/engineering downlink
    data rate is 3600 bps.
 
    Command and control of the spacecraft is achieved by a simple Command
    and Data Handling (C&DH) unit.  As an individual command is uplinked
    to the spacecraft, the C&DH directs the command to the appropriate
    subsystem.  All science and engineering data are collected by the
    C&DH and then are buffered and formatted for downlink by the C&DH.
    The data are downlinked at 1800 bps immediately and simultaneously
    dumped into a solid state recorder.  The data stored on the solid
    state recorder is downlinked 53 minutes later.  These delayed data
    frames are interleaved into the real-time data stream, yielding a
    total downlink rate of 3600 bps.  The purpose of the delayed stream
    is to receive data acquired during communications blackout periods
    and to eliminate the need for a commandable data recorder.
 
    The ACS system consists of sun and limb crossing sensors. The data
    from these sensors is used to determine the spacecraft attitude and
    spin rate.
 
 
  Principal Investigator
  ======================
    The LP science team consists of the PI, Alan Binder and six Co-I's,
    and is divided into three groups.  The Spectrometer Group consists of
    William Feldman, Binder, and G. Scott Hubbard.  The Magnetics Group
    consists of Robert Lin, Mario Acuna, and Lon Hood.  The Gravity Group
    consists of Alexander Konopliv.

        