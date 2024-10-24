
 
 
  Instrument Overview
  ===================
    The Impactor Targeting Sensor (ITS) consisted of an f/17.5 Cassegrain
    telescope feeding directly onto a CCD for direct, optical imaging.
    It was an exact clone of the Medium Resolution Instrument (MRI) and
    its visual CCD camera except that the filter wheel had been deleted.
    In all other respects it was identical.
 
    The ITS telescope was a classical Cassegrain design with the following
    parameters:
 
      Primary aperture        : 12.0 cm diameter, round
      Primary focal ratio     :  3.75
      Secondary Obscuration   :  6.6 cm diameter, round
      Secondary magnification :  4.75x (net Cassegrain focal length 210 cm)
      Back focal distance     : 30.0 cm
 
    The detector was a 1024 x 1024 split-frame, frame-transfer CCD with
    21-micron-square pixels.  The electronics allowed readout of centered
    sub-frames in multiples of 2:  64x64, 128x128, and so on, with or
    without rows of overscan.  Transfer time, to move the two halves of
    the image from the exposing area to the two shielded areas was about
    5.2 milliseconds.  There were readout amplifiers in each of the four
    quadrants.  Readout time for a full frame was 1.8 seconds.  Net pixel
    scale was 10 microradians/pixel (2 arcseconds/pixel).  The surface
    scale was 0.2 meters/pixel at 20 kilometers.  Images were transmitted
    to the flyby spacecraft for re-transmission to Earth.
 
    The ITS instrument was mounted behind the main deck of the impactor
    spacecraft and looked through a rectangular cutout on one edge of the
    copper cratering mass at the front of the impactor.
 
    For a detailed discussion of the instrument, see Hampton, et al.
    (2005) [HAMPTONETAL2005].  This instrument overview was provided by
    Dr. Michael A'Hearn, the principal investigator for the Deep Impact
    mission.
 
 
  Instrument Calibration
  ======================
    The ITS instrument was calibrated by using in-flight data as well as
    pre-launch data taken during a thermal-vacuum test (TV3) performed
    in January and February 2003.  The calibration of the ITS instrument
    was discussed in the 'Deep Impact Instrument Calibration' paper by
    Klaasen, et al. (2006) [KLAASENETAL2006].
 
    The two central rows of the CCD are physically 1/6-pixel narrower
    and collect only 5/6 of the charge of a normal row (Klaasen, et al.,
    2008 [KLAASENETAL2006]; Klaasen, et al., 2012 [KLAASENETAL2011]).
    However, the data pipeline reconstructs images with uniform row
    spacing, which introduces a 1/3-pixel extension at the center of the
    raw and calibrated image arrays.  Thus for two features on either
    side of the midpoint line outside of the two central rows, the
    vertical component of the true angular separation between those
    features is one-third of a pixel less than their measured separation
    in the reconstructed image.  As for all geometric distortions,
    correction of this 1/3-pixel extension will require resampling of
    the image and an attendant loss in spatial resolution.  The data
    pipeline process does not perform this correction in order to
    preserve the best spatial resolution.  However, it does correct for
    the 1/6 decrease of signal in the two central rows by the flat-field
    division so that the pixels in those two rows have the correct scene
    radiance in the calibrated images.  Thus, the surface brightness
    measurement is preserved anywhere in the geometrically distorted but
    calibrated images.  Point source or disk-integrated photometric
    measurements using aperture photometry that includes these central
    rows will be slightly distorted unless special adjustments are made,
    such as subtracting 1/6-pixel worth of signal to the two central
    rows and adjusting for the geometric distortion in the calibrated
    images, as described in Appendix A of Belton, et al. (2011)
    [BELTONETAL2011].
 
 
  Flight Performance
  ==================
    The ITS instrument generally performed as expected during flight.
 
 
  This instrument description was originally provided by Dr. Michael A'Hearn
  for the Deep Impact mission, then updated during the EPOXI mission.

        