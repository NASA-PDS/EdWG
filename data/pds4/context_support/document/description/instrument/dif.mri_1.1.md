
 
 
  Instrument Overview
  ===================
    The Medium Resolution Imager consists of an f/17.5 Cassegrain telescope
    followed by a filter wheel feeding directly onto a CCD for direct,
    optical imaging.
 
    The MRI telescope is a classical Cassegrain design with the following
    parameters:
 
      Primary aperture        : 12.0 cm diameter, round
      Primary focal ratio     :  3.75
      Secondary Obscuration   :  6.6 cm diameter, round
      Secondary magnification :  4.75x (net Cassegrain focal length 210 cm)
      Back focal distance     : 30.0 cm
 
    The filter wheel contains two clear apertures and eight filters.  The
    filters include duplicates of some of the medium-band filters in the
    High Resolution Instrument and narrow-band filters that isolate OH, CN,
    and C2 as well as the green and violet continuum.  These narrow-band
    filters were designed to match the Hale-Bopp filter sets used for
    ground-based programs since 1996; see Farnham, et al. (2000)
    [FARNHAMETAL2000].  The longest wavelength filter is actually a
    long-pass filter that used the CCD response to define the
    long-wavelength cutoff at about 960 nanometers.  Filter transmission
    profiles are illustrated by Hampton, et al. (2005) [HAMPTONETAL2005]
    and provided in the calibrated science data sets for the Deep Impact and
    EPOXI missions.
 
    The detector is a 1024 x 1024 split-frame, frame-transfer CCD with
    21-micron-square pixels.  The electronics allow readout of centered
    sub-frames in multiples of 2:  64x64, 128x128, and so on, with or
    without rows of overscan.  Transfer time, to move the two halves of
    the image from the exposing area to the two shielded areas, is about
    5.2 milliseconds.  There are readout amplifiers in each of the four
    quadrants.  Readout time for a full frame is 1.8 seconds.  Net pixel
    scale is 10 microradians/pixel (2 arcseconds/pixel).
 
    The MRI instrument in full-frame 1024 x 1024 mode has the following
    field-of-view characteristics:
 
      Pixel Size     :   21 micrometers
      Pixel FOV      : 10.0 microradians or 2.06265 arcseconds
      Instrument FOV : 10.0 milliradians or 0.587 degrees
      Surface Scale  :    7 meters/pixel at 700 kilometers
 
    The MRI instrument includes an internal stimulator lamp for calibrating
    between the four quadrants of the CCD; it is not a standard calibrator.
 
    The three instruments on the flyby spacecraft, MRI, HRII (High
    Resolution IR Imaging Spectrometer) and HRIV (High Resolution Visible
    CCD), are mounted on a separate instrument platform together with
    the star trackers.  The three instruments are nominally co-aligned
    as described by Klaasen, et al. (2008) [KLAASENETAL2006].
 
    For a detailed discussion of the instrument and how it was used during
    the Deep Impact mission, see Hampton, et al. (2005) [HAMPTONETAL2005]
    and Klaasen, et al. (2005) [KLAASENETAL2005].  For the EPOXI mission,
    the MRI instrument is used primarily during the encounter with comet
    103P/Hartley 2.
 
 
  Instrument Calibration
  ======================
    The MRI instrument was originally calibrated by using in-flight data
    acquired during Deep Impact as well as pre-launch data taken during a
    thermal-vacuum test (TV4) performed in 2003.  In-flight calibrations
    continued through the EPOXI mission to monitor performance and to provide
    additional data for refining the calibration pipeline.  Instrument
    calibration for Deep Impact is discussed by Klaasen, et al. (2008)
    [KLAASENETAL2006]; instrument calibration for EPOXI is discussed by
    Klaasen, et al. (2013) [KLAASENETAL2011].
 
    The two central rows of the CCD are physically 1/6-pixel narrower
    and collect only 5/6 of the charge of a normal row (Klaasen, et al.,
    2008 [KLAASENETAL2006]; Klaasen, et al., 2013 [KLAASENETAL2011]).
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
    [BELTONETAL2011].  An alternative method that corrects for the
    1/3-pixel extension was developed for Hartley 2 photometry and is
    described in the dataset DIF-C-MRI-5-EPOXI-HARTLEY2-PHOTOM-V1.0.
 
 
  Flight Performance
  ==================
    The MRI instrument generally performed as expected during flight.
    Calibration data acquired throughout EPOXI showed changes to the flat
    fields, the electronic crosstalk between the CCD quadrants, the response
    of the filters, and the calibration constants since Deep Impact in 2005.
    Therefore new calibration files and constants were incorporated into the
    calibration pipeline for EPOXI processing; additional improvements such
    as stripe removal are discussed by Klaasen, et al. (2013)
    [KLAASENETAL2011].
 
 
  This instrument description was originally provided by Dr. Michael A'Hearn
  for the Deep Impact mission, then updated as the EPOXI mission progressed.

        