
 
 
  Instrument Overview
  ===================
      A full discussion of the Large Angle Spectrometric Coronagraph is
    provided
 
      in the LASCO Handbook for Scientific Investigators, Version 1.0 (Cook
 
      1994, [COOK1994]), which can be found in the documents directory of this
 
      archive. Excerpts for the instrument are provided here.
 
 
 
    LASCO Overview
 
    ==============
 
 
 
    The Large Angle Spectrometric Coronagraph (LASCO) is a wide-field white
 
    light and spectrometric coronagraph consisting of three optical systems
 
    having nested fields of view that together observe the solar corona from
 
    just above the limb at 1.1 Rsun out to very great elongations.
 
 
 
    The three telescopes comprising LASCO are designated the C1, with coverage
 
    from 1.1 to 3.0 Rsun, the C2, with coverage deliberately overlapping parts
 
    of both C1 and C3, and extending from 2.0 to 6.0 Rsun, and the C3, which
 
    spans the outer corona from about 3.7 to 32 Rsun. C1 is an internally
 
    occulted coronagraph, while C2 and C3 are externally occulted instruments.
 
    C1 has a narrow passband Fabry-Perot interferometer tuned to hot coronal
 
    emission lines. C1 has not been used regularly since June 24, 1998, thus
 
    telemetry since then has been re-allocated to the C2 and C3 coronagraphs.
 
 
 
    Each of the three telescopes has a filter wheel, a polarizer wheel, and a
 
    shutter, and each uses a front-side illuminated, 1024x1024 pixel CCD. The
 
    pixel scale of the telescopes are 5.6 ''/pixel in C1, 11.8 ''/pixel in C2
 
    and 56 ''/pixel in C3. The quantum efficiency of the CCD is about 0.3-0.5
 
    in the 500 to 700 nm spectral region. The full discussion of the CCD
    camera
 
    is outlined in Ch 8 of Cook
 
    (1994) [COOK1994].
 
 
 
 
 
    Telemetry, Encoding and Compression
 
    ===================================
 
 
 
    LASCO is basically telemetry limited in its operations. After taking and
 
    processing an image, the data is passed to a 2 Mbyte telemetry buffer. Its
 
    storage capacity is approximately 10 compressed images, and with the low
 
    spacecraft telemetry rate (4.2 Kbps) results in a transmission time of
    about
 
    60 minutes for a full 1024x1024, 2 bytes per pixel image. (Note that the
 
    individual pixel intensities from the camera analog-to-digital converters
 
    are actually represented by only 14 bits, leaving a factor of 4 headroom
    in
 
    the 16 bits which are reserved in the data format.) Thus, image
    compression
 
    is desirable. The average compression factor is about 10. Thus on average,
 
    the readout time is about 6 minutes, which allows around 200 images each
    day
 
    to be transmitted.
 
 
 
    A number of image processing techniques are included in the flight
    software,
 
    from simple square root through transform encoding. The types of
    processing
 
    and compression utilized are determined by ground command and executed
 
    through stored sequences, with parameters stored in tables. After a camera
 
    image is stored in a 2 Mbyte image buffer, the appropriate algorithms are
 
    applied.  Additional compression is obtained by transmitting only the
    pixels
 
    that are not obscured by the occulting disk or the aperture stop. Time
 
    resolution can be traded against field coverage to further reduce the data
 
    download requirement.

        