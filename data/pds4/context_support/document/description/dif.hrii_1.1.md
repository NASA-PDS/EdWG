
 
 
  Instrument Overview
  ===================
    The High Resolution Imager (HRI) consists of a long-focal-length
    telescope with a dichroic beam splitter, located in front of the focal
    plane, that reflects visible (0.3 to 1.0 microns) light through a
    filter wheel to a CCD for direct, optical imaging.  The beam splitter
    transmits the near-infrared light (1 to 5 microns) to a 2-prism
    spectrometer.  For convenience, we consider these as two separate
    instruments, HRIV (High Resolution Visible CCD) and HRII (High
    Resolution IR spectrometer), sharing the telescope since the two
    focal planes operate in parallel asynchronously.
 
    The HRI telescope is a classical Cassegrain design with the following
    parameters:
 
      Primary aperture        : 30.0 cm diameter, round
      Primary focal ratio     :  4.5
      Secondary Obscuration   :  9.7 cm diameter, round
      Secondary magnification :  7.8x (net Cassegrain focal length 1050 cm)
      Back focal distance     : 30.0 cm
 
    The dichroic beam-splitter has equal transmission and reflection
    occurring at about 1.05 microns and is placed in front of the
    telescope focal plane.  The spectrometer is a 2-prism design, one
    of calcium fluoride (CaF_2) and one of zinc selenide (ZnSe) to
    maximize etendue and minimize problems with order separation.  The
    camera and collimator lead to a net demagnification of 3x, for an
    effective focal ratio of f/12 and effective focal length of 360 cm in
    the final beam.  The entrance slit subtends on the sky 2.53
    milliradians by 10 microradians (0.145 degrees by 2 arcseconds),
    filling the 512-pixel height of the IR array.  The slit width of
    10 microradians matches the binned pixel (2x2) mode used for most
    observations.
 
    The near-infrared detector is a 1024 (wavelength) x 512 (spatial)
    pixel mercury cadmium telluride (HgCdTe) device manufactured by
    Rockwell using the multiplexer originally developed under contract
    from the University of Hawaii for use in the WFC3 on HST.  Physically,
    it is a 1024 x 1024 device, but only half of the device is active.
    Pixels are 18 microns square and normal operations include 2x2
    binning (post-readout; pixels are averaged together).  Spectral
    resolving power, because of the 2-prism design, varies from greater
    than 740 at 1.04 microns down to 210 at 2.6 microns, and back up
    to 385 at 4.8 microns.  Due to saturation problems in warm areas
    of a cometary nucleus, the central quarter of the detector is
    covered with a neutral density filter, which is also called the
    anti-saturation filter.
 
    When operated in the 512 x 256 pixel, 2x2 binning mode, the HRII
    instrument has the following field-of-view characteristics:
 
      Spatial
      -------
        Physical Pixel Size :   36 micrometers
        Effective Pixel FOV : 10.0 microradians or 2.06265 arcseconds
        Effective FOV       :  2.5 milliradians or 0.15 degrees
 
      Spectral
      --------
        Effective Pixel FOV : 10.0 microradians
        Effective FOV       : 10.0 microradians (slit width)
 
      Note:  For unbinned modes, pixels are 5 microradians wide
             in the spatial dimension and the slit width remains
             fixed at 10.0 microradians.  Therefore an unbinned
             pixel subtends 10 microradians x 5 microradians or
             5x10^-11 steradians on the sky while a binned pixel
             subtends 10 microradians x 10 microradians or
             1x10^-10 steradians.
 
    The spectrometer includes an internal stimulator lamp for calibrating
    between the two quadrants of the spectrometer (i.e., not as a standard
    calibrator).  However the lamp was broken during one of the ground
    thermal-vacuum tests and was not replaced.  Therefore this lamp was
    never used during the Deep Impact and EPOXI missions.
 
    The three instruments on the flyby spacecraft, HRII, HRIV (High-
    Resolution Visible CCD) and MRI (Medium-Resolution Visible CCD), are
    mounted on a separate instrument platform together with the star
    trackers.  The three instruments are nominally co-aligned as
    described by by Klaasen, et al. (2008) [KLAASENETAL2006].
 
    For a detailed discussion of the instrument and how it was used during
    the Deep Impact mission, see Hampton, et al. (2005) [HAMPTONETAL2005]
    and Klaasen, et al. (2005) [KLAASENETAL2005].  For the EPOXI mission,
    the HRII instrument imaged Earth and Mars as remotely-sensed planets
    and comet 103P/Hartley 2.
 
 
  Instrument Calibration
  ======================
    The HRII instrument was originally calibrated by using in-flight data
    acquired during Deep Impact as well as pre-launch data taken during
    thermal-vacuum tests (TV1, TV2, and TV4) performed in 2002 and 2003.
    In-flight calibrations continued through the EPOXI mission to monitor
    performance and to provide additional data for refining the calibration
    pipeline.  Instrument calibration for Deep Impact is discussed by
    Klaasen, et al. (2008) [KLAASENETAL2006]; instrument calibration for
    EPOXI is discussed by Klaasen, et al. (2013) [KLAASENETAL2011].
 
 
  Flight Performance
  ==================
    The HRII instrument generally performed as expected during flight.
    During Deep Impact, small changes in instrumental temperatures affected
    the dark current more than expected from ground thermal-vacuum tests.
    This effect continued for EPOXI and is discussed in the Deep Impact
    instrument calibration paper by Klaasen, et al. (2008)
    [KLAASENETAL2006].  Calibration data acquired throughout EPOXI showed
    changes to the linearity constants and increases to the numbers of bad
    pixels.  Also a new flat field that corrected for the anti-saturation
    filter was constructed.  Therefore new calibration files and constants
    were incorporated into the calibration pipeline for EPOXI processing;
    additional improvements such as the timing for certain imaging modes
    are discussed by Klaasen, et al. (2013) [KLAASENETAL2011].
 
    During the Deep Impact mission, early images of stars acquired by the
    HRIV CCD indicated the HRI telescope was out of focus.  An analysis
    showed the focus was forward of the HRIV CCD, so bakeouts were
    performed in late February and early March 2005 to improve the focus.
    The bakeouts reduced the defocus from 1.0 cm to 0.6 cm, which caused
    the width of star images to decrease from about 12 pixels to about 9
    pixels in a HRIV frame.  This focus problem had only a nominal effect
    on the HRII instrument.  For a detailed discussion about the focus
    of the HRI telescope, please see Klaasen, et al. (2008)
    [KLAASENETAL2006] and Lindler, et al. (2007) [LINDLERETAL2007].
 
  This instrument description was originally provided by Dr. Michael A'Hearn
  for the Deep Impact mission, then updated as the EPOXI mission progressed.

        