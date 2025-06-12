
 
The instrument overview provided here is the summary description from
the EDR SIS (in the document directory).  [MALINETAL2001] describes
the Mars Climate Orbiter MARCI; currently there is no published MRO-
MARCI paper, but a paper describing the investigation is being written
and may be included on future archive volumes.
 
  Instrument Overview
  ===================
    MARCI is a framing camera with a 1024x1024 pixel interline
    transfer CCD (Kodak KAI-1001) with 9x9 micron pixels.  MARCI has
    two  all-refractive 180-degree 'fisheye' lenses, one optimized for
    the visible and near-IR and one for the UV bands.  The beams from
    these two lenses are brought to the CCD  through  a prism.  A
    color filter array with seven dif- ferent bandpasses (five
    visible/near-IR and two UV) is directly  bonded to the CCD.  A
    typical image consists of seven 'framelets', each 1024 pixels wide
    and 16 pixels high, in each of these bandpasses.  The visible
    bands can be optionally summed; the UV bands are always summed
    8x8.  The visible resolution from 300 km is about 1 km/pixel at
    nadir.
 
    The core of the MARCI electronics is a Motorola 56166 DSP, which
    interfaces to the spacecraft, generates the CCD clocks, and
    received digitized pixels from an Analog Devices AD1672 analog-to-
    digital converter.  Both lossless and lossy image data compression
    can be applied by software running in the spacecraft computer.
 
    MARCI was originally designed for the Mars Climate Orbiter
    mission.  For MRO, a separate subsystem, the MARCI Interface
    Adapter or MIA, was designed and built to translate the MRO
    command/data protocol into a form that could be interpreted by the
    heritage MARCI hardware.

        