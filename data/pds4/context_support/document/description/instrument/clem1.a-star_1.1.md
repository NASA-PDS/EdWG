
              Online Reference: http://wundow.wustl.edu/clbin/clsearch.pl

 
 
    Instrument Overview
    ===================
      On Clementine 1 there were two star tracker cameras, A Star and
      B Star Tracker Cameras.  They were mounted on opposite sides of
      the spacecraft, allowing at least one to obtain star field
      coverage at all times without interference from the Sun.  Each
      could provide three-axis attitude determination from a single
      image provided the Sun, Moon, and Earth were not in the field
      of view.
 
      The primary function of the star tracker cameras was to provide
      stellar images that were processed against an onboard star
      catalog to find pointing, thus establishing absolute angular
      references for attitude determination.  The scientific uses of
      the cameras were secondary.  Only broad band operation was
      available.  Owing to the line-transfer electronic shuttering,
      imaging was limited to dim targets such as the lunar surface
      illuminated by earth shine.
 
      The Wide-Field-of-View Star Tracker cameras have a concentric
      optics design with a fiber optic field flattener to couple the
      image surface to a CCD array.  The CCD is kept cleared by
      continuously shifting lines and reading out pixels at the 5 MHz
      base rate, which is approximately 100 microseconds per line.
      Image acquisition is accomplished by stopping this clearing
      process for the appropriate integration time (13-bit
      programmable), then proceeding with a second line-shifting
      operation into a readout buffer.
 
      The Thomson focal plane array (FPA) used is a frame-transfer
      device, accomplishing electronic shuttering by rapidly shifting
      the active pixel area into the storage area, pausing for the
      13-bit programmable shuttering system spectral integration
      time, then rapidly shifting the captured image into a storage
      buffer from which the image is read out.  Post-FPA electronics
      allow three gain states followed by 5 bits of offset that span
      248 counts in the analog regime to augment the basic 8-bit
      analog/digital (A/D) conversion.  Gain is A/D digitization
      noise limited, so proper exposure is critical.  System noise is
      about 1.0 bits rms at the highest sensitivity setting.
 
 
    Scientific Objectives
    =====================
      Science observations of the star tracker cameras were limited
      to dim targets such as the lunar surface illuminated by earth
      shine and observations of the earth illuminated by moon shine
      during the low earth orbit phase.  Additionally the star
      tracker camera was used to acquire lunar 'horizon glow'
      observations and solar corona observations prior to sun rise
      over the Moon.
 
 
    Calibration
    ===========
      The Star Tracker cameras were calibrated before launch.
      Laboratory observations of a flat field under various operating
      temperatures and camera operation modes provides information
      about the sensitivity of the camera under expected spaceflight
      conditions.  During inflight operations, a variety of
      calibration observations were made including images of stars
      with known radiance (Vega).
 
 
    Operational Considerations
    ==========================
      Most star tracker observations used for spacecraft attitdue
      determination were acquired prior to and after a pass over the
      sunlit side of the Moon.  No star tracker observations were
      made on the sunlit side of the lunar surface due to the extreme
      sensitivity of the cameras and the potential for damage.
 
 
    Operational Modes
    =================
      The Star Tracker Cameras had three operating modes:
 
      1. 13-bit programmable integration time.  The range of integration
      times (in microseconds) is given by:
      Integration Time = [(N+3)*94.5 - 45, N=0,2,3...2**13]
 
      2. Gain Mode. The gain mode represents the multiplicative constant
      applied to the image data passing through the A/D converter.
      Three gain state settings were available (1,2,4) although gain
      setting 4 was seldom used during lunar observations.
 
      3. Offset Mode. The offset mode represents the additive constant
      applied to the image data passing through the A/D converter.
      There were 14 offset mode settings (1-14) although offset modes
      1 and 6 were predominantly used during systematic lunar
      observations.
 
 
    Camera Specifications
    =====================
 
      Thomson Focal Plane Array Detectors
      -----------------------------------
        Type              : Si Charge Coupled Device
                              Thomson TH7863
        Pixel format      : 576x384
        Pixel size        : 23x23 microns
        Readout rate      : 5MHz
        Wavelength        : 0.5 to 1.1 microns
        Field of view     : 43 deg. x 28 deg.
        Pixel IFOV        : 1.3 microradians
        Point spread      : 2 pixels
 
 
      Electronics
      -----------
        A/D resolution    : 8 bits
        Readout time      : 54.8 ms
        Integration time  : 0.2-733 ms
        Digitization gain : 75, 150, 350 electrons/count
        Offset control    : 248 gray levels
        Power             : 4.5 W
 
 
      Filters
      -------
        The Star Tracker cameras did not have a filter wheel
        assembly.  They acquired only broad band images in the range
        .5 to 1.1 microns.
 
 
      Optics
      ------
        Clear aperture    : 14nm
        Speed             : F/1.3
 
 
      Mechanical
      ----------
        Mass                : 290 grams
        Size                : 11.7 cm x 11.7 cm x 13.2 cm
 

        