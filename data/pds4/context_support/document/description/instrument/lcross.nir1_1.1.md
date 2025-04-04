
 
  Instrument Overview
  ===================
 
  The LCROSS near infrared camera #1 (NIR1) is a ruggedized Goodrich
  Sensors Unlimited SU320-KTX camera. The Goodrich unit consists of a
  camera module and a lens. The camera's focal plane InGaAs sensor has
  a 320 [H] x 240 [V] pixel format.
 
  NIR1 is one of two near infrared cameras in the LCROSS payload. The
  cameras are identical except that NIR1 contains a long-pass filter
  (> 1.4 microns). NIR2 contains no filter.
 
  The 25mm, f/1.4 C-mount glass lens from UkaOptics (Model Number #2514M)
  provides a 28.7 deg [H] x 21.7 deg [V] (36.0 deg [Diagonal]) field-of-view.
  The NIR1 filter is Spectragon catalog filter LP-1400nm (25.4mm diameter x
  1.0mm thick).
 
  NIR1 camera's focal plane InGaAs sensor is sensitive from 0.9 to
  1.7 microns. The addition of the Spectragon filter in NIR1 provides
  an effective 1.4-1.7 micron response for the unit.
 
  Although the camera's native format is 320 [H] x 240 [V] 12-bit images,
  the images are converted by the camera to an analog NTSC
  signal before transfer to the DHU where they are captured at 720 [H] x
  486 [V], the same resolution as the VIS camera.
 
  Also, like the VIS camera, the NIR images are captured in 24-bit per pixel
  RGB. Because the NIR cameras provide grayscale images, the three
  RGB channels are identical except for noise introduced in the
  conversion to and from NTSC.  These images are compressed in the
  DHU using a lossy compression algorithm performed by the Analog
  Devices 611 Video Codec set on 80% quality and decompressed on the
  ground.
 
  The near-infrared cameras contain no cryogenic liquids or moving
  parts.  Each contains an internal thermo-electric cooler which can
  actively cool InGaAs sensor, but the default setting is near room
  temperature (~20 C).  Each camera's peak power during operation is
  1.6 W.  Both gain and exposure time are configurable with commands
  sent to the camera, and different gains and exposures are used at
  different times during the LCROSS mission.
 
  Scientific Objectives
  =====================
 
  The main science objective for the near infrared cameras (NIR1 & NIR2)
  is to provide near infrared contextual imagery of the ejecta cloud
  morphology. When used together as a pair, NIR1 (filter) provides a scene
  image integrated between 1.4 and 1.7 microns, whereas NIR2 (no filter)
  provides a scene image integrated over 0.9 to 1.7 microns. When utilizing
  the cameras as a pair, the difference in the overall camera efficiency
  (electrons out/photons in) due to the presence of an effective 80%
  transmissive long-pass filter (lambda > 1.4 microns) in NIR1 needs to be
  taken into account. The water band at 1.5 microns, if present in the ejecta,
  will be visible in both cameras.
 
  The filtered NIR1 is also used to image the impact flash event in the
  near-infrared (1.4 - 1.7 microns).
 
  The unfiltered NIR2 is used for a star field calibration and the final
  minutes of the mission, taking advantage of its larger spectral range and
  greater sensitivity.
 
  Calibration
  ===========
 
  The image files were initially processed by the LCROSS GSEOS (Ground
  Support Equipment Operating System) which extracted the image
  files from telemetry, performed decompression, and converted them to a
  24-bit RGB format with MET-based packet timestamp encoded in the filename.
  The near infrared cameras are only capable of generating grayscale images.
  The RGB values are typically within +/- 2 DN of each other, this difference
  due to noise introduced in the conversion to and from NTSC. Therefore, the
  images were further processed with the LCROSS Make Archive Program to
  extract the correct grayscale image and generate the binary image and
  ASCII label (.lbl) files, time stamping each pair with the S/C UTC time
  at time of data collection.
 
  The flight near-infrared cameras were not directly radiometrically
  calibrated pre-flight. A flight spare camera, both with (to mimic NIR1)
  and without (to mimic NIR2) an internal spare flight NIR1 filter was
  calibrated using a NIST-calibrated reference source. The calibration steps
  and validation of this approach, using flight data, along with the
  assumptions and caveats, are described in the LCROSS Instrument Response
  and Calibration Report in the CALIB directory of this archive.
 
 
  Operational Modes
  =================
 
  The LCROSS near-infrared cameras have numerous parameters and mode
  settings, but LCROSS uses these cameras in limited ways. For all images,
  digital gain is set to 1. Throughout the mission there are four main
  modes used for these cameras:
 
  (1) Fixed Short Exposure time (OPR 5 & 7/ENH:ENABLE OFF/AGC:ENABLE OFF)
  (2) Fixed Long Exposure time (OPR 15/ENH:ENABLE OFF/AGC:ENABLE OFF)
  (3) Automatic Gain Control Enabled (ENH:ENABLE OFF/AGC:ENABLE ON)
  (4) Image Enhancement Enabled (Fixed OPR/ENH:ENABLE ON/AGC:ENABLE OFF)
 
  The mode settings are documented with each image.
 
  (1) OPR 5 & 7 have an effective integration time of 0.61 ms and 1.16 ms
      per image with a factory-derived optimized pixel gain. This setting
      was designed to place a integrated scene input of ~10^9 photons/s/pixel
      detected by the camera within the camera's effective analog 8-bit range.
      OPR 5 & OPR 7 are the adopted curtain mode setting for NIR2 & NIR1,
      respectively, based on the expected radiance values for the lunar
      south pole on October 9, 2009.
      Other OPR settings were used during calibration targets (Earth and Moon
      from 300,000-800,000km distances). See the LCROSS Instrument Response
      and Calibration Report for details of the exposure time and gain
      parameters for these OPR settings.
  (2) OPR 15 has an effective integration time of 16.24 ms per image with
      a factor-derived optimized pixel gain. This setting was designed to
      place an integrated (dim) scene input of less than 10^7 photons/s/pixel
      detected by the camera within the camera's effective analog 8-bit range.
      This setting is used for starfield and crater observations.
      OPR 10, used only in NIR2 for some final images in the impact
      sequence, has an effective integration time of 3.08 ms per image.
  (3) Automatic Gain Control enabled will adjust the operational
      configuration (OPR number) to achieve the best camera sensitivity
      settings for the given imaging scene.  The range of available OPRs
      provide integration times 0.11ms (OPR 0) and (16.24 ms). This setting
      was designed to allow for the cameras to optimize the integration time
      to place the scene within the middle range of the effective 8-bit range,
      particularly when the scene's brightness is unknown.
  (4) Image Enhancement enabled linearly stretches the image over
      the available pixel depth to result in a higher contrast scene for
      display. This setting was designed to provide additional information to
      pick out a potentially dim signal against an unknown background
      (e.g., starfield and flash). It is used typically with the long
      exposure setting and in addition to one of the other modes above.
 

        