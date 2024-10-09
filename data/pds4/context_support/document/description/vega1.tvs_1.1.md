
 
 
    Instrument Overview
    ===================
 
      The television system consists of two telescopes,
      one narrow-angle camera (TVY) for high-resolution
      imaging of the nucleus, and one large-angle camera
      (TDN) for detecting and tracking the comet.  The
      TVY optics have a reflecting objective with a focal
      length of 1200 mm and a detector which yields an
      average angular resolution of 3 arcsec, i.e.  a
      spatial resolution of the order of 150 m at the
      nominal flyby distance of 10 000 km.  The maximum
      angular dimension of the nucleus and its near
      environment is expected to be 5 arcmin at closest
      approach, and the pointing error is estimated to be
      +/- 5 arcmin.  The field of view of the TVY must
      therefore be not less than 15 arcmin.
 
      The TDN has a refractory objective with a focal
      length of 150 mm.  It is characterised by an
      angular resolution of 0.5 arcmin, required for
      early acquisition of the comet and its nucleus, and
      a 2deg field of view imposed by the constraints
      associated with control of the pointing platform.
      The light collected by each telescope is divided
      into two paths by a beam splitter, 0ne channel is
      fitted with a fixed filter, the other has a set of
      eight filters mounted on a rotating wheel, to yield
      a spectral analysis of the signal.  The images are
      forms on area CCDs cooled by a passive radiator
      regulated by a Peltier plate.  The commutable
      filters of the TDN have an additional function,
      namely to adjust the amount of light collected by
      the detector.  This channel is operated
      autonomously and performs an independent analysis
      of the video signal, thus providing redunant
      information to the platform pointing system for the
      sake of reliability.  The signals delivered by the
      three other TDN and TVY channels are handled by the
      same microprocessor system which analyses the
      images and generates the commands that control the
      motion of the platform.  The TVS electronics
      include a 816 kbit memory to store both data and
      programs, The main characteristics of the TVS are
      given below.
 
 
-------------------------------------------------------------------------
Table . Television System characteristics
 
Camera system           High resolution           Low resolution
-------------------------------------------------------------------------
Objective               Reflector                 Refractor
Focal distance          1200 mm                   150 mm
Aperture                 240 mm                    50 mm
Relative aperture       1:5, effective 1:6.5        1:3
Channel                 Multispectral  Integral   Multispectral Integral
-------------------------------------------------------------------------
Spectral range, micro m 0.4-1.1        0.63-0.76  (1) 0.4-1.1   0.63-0.76
                                                  (2)0.63-0.76
-------------------------------------------------------------------------
Number of filters       8              1          Range (1):1    1
                                                  Range (2):7
-------------------------------------------------------------------------
Field of view           26.4'x39.6'               211'x316'     211'x158'
Resolution               3.1inx4.1in           24.75inx33in    99inx132in
-------------------------------------------------------------------------
Shutter                 Mechanical                             Electronic
-------------------------------------------------------------------------
Exposure time range     0.01-163 s                              6-800 ms
-------------------------------------------------------------------------
Detector area           5l2x512 pixels                     512x256 pixels
-------------------------------------------------------------------------
Data compression        Floating window of 128 X 128 pixels    Full image
                        around brightest point                 of 128x128
                                                               pixels
                                                               after
                                                              integration
                                                            of 4x2 pixels
-------------------------------------------------------------------------
 
 
      The resolution of the images was a trade-off.
      Scientists wanted nucleus images with the highest
      possible resolution, but that was limited by weight
      considerations and by selecting a trajectory for
      the spacecraft which was far enough away from the
      nucleus to guarantee a high survival probability.
      The compromise solution was to use a
      Ritchey-Chretien type telescope for scientific
      imaging with a focal length of 1200 mm, an
      effective aperture of f/6.5, and a field of view of
      26.4x39.6 arcmin.  It was immediately obvious that
      the field of view of this narrow angle camera (NAC)
      was too small to find the nucleus autonomously.  It
      was also not possible to steer the telescope from
      the ground because the position of the nucleus in
      the coma was not well enough known.  Therefore, a
      wide angle scanning camera (WAC) had to be added to
      the payload.
 
      A major concern was the target definition, namely
      what should the pointing system be aimed at.  The
      sensors could identify only the centre of
      brightness, but it obviously was not identical to
      the centre of the nucleus.  This was partly due to
      partial illumination of the nucleus by the Sun
      (comparable to the phases of the Moon) and partly
      due to jet activity.  The pointing system might
      well have locked on to a bright dust jet and be
      steered away from the nucleus.  As we found no way
      to define an offset reliably, we decided simply to
      aim at the centre of brightness.  This targeting
      strategy worked well for Vega.
 
      The main navigation system for the platform was the
      imaging system itself.  However, as a backup an
      eight-segmented light sensitive sensor was mounted
      on the pointing platform.  Its working principle
      was extremely simple: if the centre of light from
      the comet would move away from the centre of the
      sensor, a change of the platform orientation would
      have been initiated to compensate for this offset.
      Fairly sophisticated computer simulations proved
      that this backup was reliable, but fortunately, it
      never had to be used.
 
      To have many backups was a major element in our
      design philosophy.  A third navigational backup,
      which used analog signals from a completely
      independent CCD sensor, was added to the TV system.
      The output signal was processed in a similar way to
      the eight segmented light sensitive sensor but with
      much higher precision.
 
 

        