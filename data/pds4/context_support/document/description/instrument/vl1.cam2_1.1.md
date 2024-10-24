
 
 
 
    Instrument Overview
    ===================
      The Viking Lander camera design was very different from vidicon
      framing or CCD array cameras.  The lander camera was a
      facsimile camera with a single, stationary photosensor array
      (PSA) and azimuth and elevation scanning mechanisms.  A lander
      image was generated by scanning the scene in two directions
      (azimuth and elevation) to focus light onto the photosensor
      array.  A number of published papers described the
      characteristics and performance of the lander cameras.  The
      scientific rational and early design of the cameras were
      described in Mutch et al.  [1972] and a detailed description of
      the flight cameras was given in Huck et al. [1975b].  Huck and
      Wall [1976] discussed image quality and Patterson et al.
      [1977] described camera performance during the Primary Mission.
      A summary of the information from these papers is given here as
      a high-level description of the camera and its operating modes.
 
 
    Platform Mounting Descriptions
    ==============================
      Each camera was bolted to the top of the lander body.  The
      camera had a lower stationary section containing electronics
      and an upper section that rotated in azimuth (i.e., around a
      vertical axis).  The other prominent exterior component was a
      post assembly that protected the camera window from the Mars
      environment when the camera was not in use.  At the top of the
      post was a carbon dioxide dust removal nozzle.  Major internal
      camera components were two fused silica windows, a mirror,
      elevation and azimuth rotation assemblies, a lens, the
      photosensor array, electronics, and pinlights for calibration.
      The overall camera height was 55.6 cm.  The lower assembly
      diameter was 25.6 cm and the upper assembly diameter was 14.4
      cm.  The weight of the camera was 7.26 kg.  Below is a table
      that lists the serial number of the cameras and photosensor
      arrays as they were assigned to the flight cameras [Huck et
      al., 1975a].
 
      Camera                  Serial Number  PSA Serial Number
      --------------------------------------------------------
      Viking 1, camera 1      FC-1B               M017
 
      Viking 1, camera 2      FC-2A               M020
 
      Viking 2, camera 1      FC-3A               M015
 
      Viking 2, camera 2      SPARE               M019
 
 
    Operational Considerations
    ==========================
      The camera had several features to deal with possible dust
      abrasion or obscuration.  When the camera was not in use, the
      upper assembly was rotated so that the window was behind the
      post assembly to prevent exposure to dust.  Mounted in the post
      was a nozzle for releasing carbon dioxide gas to blow dust off
      the window.  In addition, the outer window, known as the
      contamination cover, was designed to move out of the optical
      path if it became abraded or dust coated.  The contamination
      cover window was hinged and spring loaded so that it could be
      deployed by rotating the camera behind the post with enough
      force to release the spring lever.  During the Extended Mission
      the contamination cover windows of camera 1 on lander 1 and
      camera 2 on lander 2 were deployed.  One drawback of the
      contamination cover window was that its frame caused a
      vignetting effect at elevation angles above 25 deg.  [Patterson
      et al., 1977].
 
      Light entered the camera through the windows, reflected off the
      mirror toward the lens, passed through the lens, and was sensed
      by one of the photodiodes.  A voltage was generated in the
      selected photodiode that was digitized by an analog-to-digital
      (A/D) converter.  Below the lens was a black shutter that could
      be closed to sample photodiode dark current and to perform
      internal radiometric calibration.  Between the lens and
      photosensor array was a light baffle to minimize internal
      reflections.  The lens had a 0.95 cm aperture diameter and 5.37
      cm focal length.
 
      Mechanical scanning was done by rotating the mirror around a
      horizontal axis to scan each vertical line in an image.  The
      entire upper camera assembly rotated around a vertical axis to
      scan successive lines.  Image data were collected while the
      mirror rotated up through the elevation range in 512 steps
      (i.e., pixels were sampled from the bottom of the image to the
      top).  The mirror rapidly rotated down to the start position
      while the camera turned in azimuth for the next scan.  The
      mirror could rotate from 60 deg below the horizon to 40 deg
      above it for a total range of 100 deg.  The camera could see
      342.5 deg in azimuth with the range limited by the post
      assembly.  Image commands specified both a start and stop
      azimuth such that the width of images varied.  On receiving a
      command to acquire an image, the camera first rotated to a
      preset azimuth and then rotated to the start azimuth.  The
      camera stepped in azimuth after each vertical scan until the
      stop azimuth was reached.  The sequence ended by the camera
      moving back to the preset position and then to the park
      position with the window behind the post.  The preset position
      at the beginning and end of the sequence prevented the camera
      from turning through mechanical stops.  Internal radiometric
      calibration could be done by closing the shutter while the
      camera was in the preset position either before or after the
      image data were acquired.  The camera had two scanning rates so
      that data could be collected at 250 or 16,000 bits/sec.
 
      The photosensor array consisted of 12 silicon photodiodes (or
      diodes) sensitive to light between 0.4 and 1.1 micrometers.
      The diodes were arranged in a 2x6 array.  There were four broad
      band, high resolution (0.04 deg angular resolution) diodes,
      known as BB1, BB2, BB3, and BB4.  The distance between the lens
      and each high resolution diode was different to vary the
      in-focus distance of each diode.  In-focus distances were 1.9,
      3.7, 4.5, and 13.3 meters for BB1, BB2, BB3, an BB4,
      respectively.  There was a low resolution (0.12 deg angular
      resolution), broad band diode known as the SURVEY diode.  There
      were also six narrow band, low resolution diodes for color
      (BLUE, GREEN, and RED) and infrared (IR1, IR2, and IR3) images.
      The narrow bandwidth was generated by covering diodes with a
      set of interference filters, chosen to survive the spacecraft
      sterilization process.  The interference filters had
      significant out-of-band leaks.  Also, the infrared filters were
      known to degrade due to neutron radiation from the lander RTGs
      [Patterson et al., 1977].  The twelfth diode was also a low
      resolution diode covered by a red filter for imaging the Sun.
      The in-focus distance for the low resolution diodes was about
      3.7 meters.
 
      Diodes in the camera generated a voltage proportional to
      incoming radiance.  Each diode, except for the SUN diode, had
      an amplifier to enhance the voltage signal.  The SUN diode did
      not need an amplifier because of the strong signal when
      directly viewing the Sun.  Voltage from the amplifier was
      digitized as a 6-bit number in an A/D converter that also
      performed automatic dark current subtraction.  Dark current was
      sampled after every line in slow scan mode and after every 64th
      line in rapid scan mode.  The A/D converter had 6 gains and 32
      offsets so that the full dynamic range of the diode output
      could be stored in 6-bits.  Gain defined the voltage range
      sampled and its resolution.  Low gain (high gain number)
      covered a wide range in voltage and had low voltage resolution.
      The offset could be varied from a slightly negative voltage to
      several volts in 32 small steps.  Digital values from the A/D
      converter could be dumped to the spacecraft tape recorder or
      transmitted to Earth or an orbiter in real-time (usually done
      at beginning or end of a transmission link when the bit error
      rate was relatively high).
 
      Each camera had two pinlights in the post assembly.  Using a
      special command, the lights turned on and an image was acquired
      while viewing the pinlights.  This command, known as a scan
      verification, monitored the mechanical scanning operation of
      the camera.  A third pinlight with four different radiance
      levels was located between the dark current shutter and the
      photosensor array.  This pinlight was used with the shutter
      closed for radiometric calibration of the camera.
 
 
    Operation and Sampling Modes
    ============================
      Operation of Viking Lander cameras was versatile in that many
      parameters for the image could be specified.  Commands to
      acquire an image involved selecting the sampling mode, diode,
      start and stop azimuths, center elevation, gain and offset,
      scan rate, and specifying whether automatic dark current
      subtraction, internal calibration, rescan, or dusting were
      done.  Image start time and whether the image was transmitted
      in real-time or sent to the tape recorder were also specified.
 
      The camera had seven sampling modes: low resolution (0.12 deg)
      stepping with three diodes (known as triplet mode); low
      resolution stepping with one diode; high resolution (0.04 deg)
      stepping with one diode; and four different calibration lamp
      intensity levels.  In triplet mode, elevation scanning was
      repeated three times with three different diodes at every
      azimuth position.  An unusual sampling mode effect was an
      elevation shift when the step size did not match the diode
      resolution.  There was a -5.6 deg elevation shift when using a
      low resolution diode with high resolution stepping and a +5.6
      deg shift when using a high resolution diode with low
      resolution stepping.  These non-nominal modes were mostly used
      to generate high resolution color images or to better resolve
      the solar disk.  For the triplet mode, the specified diode was
      the first of the three diodes, e.g., BLUE diode for a color
      image.  Start and stop azimuths had to be multiples of 2.5 deg.
      Center elevation had to be a multiple of 10 deg.  The elevation
      range was determined by the step size with a range of about 20
      deg for high resolution and about 60 deg for low resolution
      since there was always 512 steps in an elevation scan.  Rescan
      was done by inhibiting the azimuth rotation and repeatedly
      scanning in elevation.  Rescan could be activated by commanding
      the camera to operate for a time longer then it took to scan
      the azimuth range of the image.
 
 
    Principal Investigator
    ======================
      The principal investigator for the Viking Lander imaging system
      during instrument development and the Viking Primary Mission
      was Thomas A.  Mutch of Brown University.  From the Extended
      Mission until the end of the Viking Mission, Raymond E.
      Arvidson of Washington University was the lander imaging
      principal investigator.
 

        