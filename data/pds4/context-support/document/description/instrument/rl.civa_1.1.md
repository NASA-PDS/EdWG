                                              
                                                                     
        Instrument Overview                                            
        ===================                                            
        Integrated set of imaging instruments, designed to characterize
        the 360 degrees panorama (CIVA-P) as seen from the Rosetta
        Lander Philae, and to study surface and subsurface samples
        (CIVA-M). CIVA-P is a panoramic stereo camera, while CIVA-M is
        an optical microscope coupled to a near infrared microscopic
        hyperspectral imager                                            
  
        Scientific Objectives                                   
        =====================                                           
        stereoscopic imaging of the site surrounding the Lander
        (CIVA-P), and by optical imaging and infrared spectral imaging
        of surface and subsurface samples of the cometary nucleus, at
        a microscopic scale (CIVA-M)                                  
                                                                       
        Calibration                                                    
        ===========                                                    
        Following calibration functions are applied to the CIVA-P
        images, at IAS level:
  
  Non-linearity correction
             
  The TH7888A detector presents a strong deviation
  from linearity when the signal is higher than ~ 80%
  of the saturation level. This saturation level depends
  on the camera, on the gain setting and on the
  temperature of the detector. A linearity correction
  transformation which includes the subtraction of the offest
  has therefore been applied to level 1 CIVA images which
  reach levels close to saturation (CIVA 1, CIVA 2, CIVA 3
  and CIVA4). The linearity files providing the actual DN level
  from the measured DN level (1024 floating point values)
  are civa1scale.txt, civa2scale.txt, civa3scale.txt,
  civa4scale.txt. The offset was evaluated as 18.4 DN, 19 DN,
  13 DN and 20.9 DN for these four cameras.
  
  Cameras CIVA 5, CIVA 6 and CIVA 7 have low DN values,
  hence the corrected values correspond to the subtraction
  of an offset of 17.8 DN, 20.5 DN and 14.5 DN for CIVA 5,
  CIVA 6 and CIVA 7 respectively.
  
  Regions of images from the CIVA 1, CIVA 2, CIVA 3 and CIVA 4
  cameras are saturated. This situation is indicated in
  the image file by a value of the recovered DN equal to
  the maximum floating value of the transformation table
  provided in 'civaNscale.txt' (N=1 to 4).                   
                                                                       
        Operational Considerations                                     
        ==========================                                     
        CIVA-P will be operated to take one stereo image of the Orbiter
        jus after release of Philae, to be used as calibration for the
        on-comet images. Then, immediately after touch-down, a full
        panorama of the landing site, with a partial stereoscopic
        coverage, will be taken by CIVA-P, and immediately transmitted
        to the Earth for quick look data reduction. This first panorama
        will be key to assess the landing conditions, and to declare
        secure the planned Philae sequence of operations. Follow-ons
        partial or global panoramas could be acquired either to monitor
        changes with solar illumination and/or cometary activity, to
        increase the stereoscopic coverage, and to image after their
        deployment Philae systems and sensors.
   
        CIVA-M will be turned on after all samplings (surface and
        subsurface) by SD2. It will consist in sequences of calibration
        (by imaging an oven with a calibration target), imaging of ovens
        prior to be filled, and after being filled by SD2 with cometary
        samples. CIVA-M/V will image each oven in three colors, while
        CIVA-M/I will acquire a complete 3D (x,y,lambda) image cube of
        them. After compression and storage in the IME mass memory, the
        data will be transferred to CDMS for downlink. 
                                                                       
        Electronics                                                    
        ===========                                                    
        This Imaging Main Electronics (IME) is a facility, developed 
        under the co-responsibility of IWP/DLR and IAS, for both ROLIS
        and CIVA: they share a common I/F with the Lander, for both the
        power subsystem and the Central Data Management System (CDMS).
        Thus the IME includes the CIVA-Central Electronics (CIVA-CE),
        mainly based on a dedicated CDPU (Command and Data Processing
        Unit); it is equipped with a 16 Mbytes mass memory.
        The CIVA-CDPU (Command and Data Processing Unit), developed by
        IAS, has the following functions: on/off power control; camera
        program uploading; camera heads check out; command reception 
        (from ROLIS-DPU) and management; CIVA payload sequencing; 
        status monitoring; image acquisition; integration time
        optimization; image compression (using wavelet based software);
        error encoding and data formatting. It consists of a TEMIC
        TSC21020 processor, 2 Kword PROMs for boot sequence, 512 Kbyte
        EEPROM for application program and parameters storage, 128
        KWord Fast SRAM for application program, 128 KWord Fast SRAM for
        application data and 6 Mbyte SRAM for 2 images data (1024x1024
        pixels) storage/processing. The CDPU electronics is integrated
        into a 3D-packaged cube which is implemented into the IME.
        The CIVA-CE includes two more electrical boards:
        one is dedicated to the IR detector, and the second to the CIVA
        peripherics.
  
        Location                                                       
        ========                                                       
        CIVA-P is constituted of 7 identical miniaturized cameras, 
        implemented as 5 single cameras and one stereoscopic pair of
        two co-aligned ones, thus filling the 360 deg. panoramic field
        of view by six contiguous and overlapping FOV of 70 deg. each,
        60 deg. apart one from the next.
        CIVA-M is constituted of a visible microscope, CIVA-M/V and a
        near infrared hyperspectral imager CIVA-M/I. CIVA-M/V and CIVA-M/I
        are mounted on the Philae base-plate
        (balcony), close to the drill and sample distribution system
        (SD2). They will image and analyse the samples (from a distance
        of 13.0 mm) whenever they will be deposited within containers
        (Mid Temperature Ovens), mounted on a rotating carousel, and
        closed by a sapphire window transparent in both the Visible and
        the near IR.                            
                                                                       
        Operational Modes                                              
        =================                                              
        CIVA can be basically operated in 4 modes:
        - Software upload.
        - Pannoramic imaging
        - Visible Microscopic imaging    
        - Hyperspectral Microscopic imaging                            
                                                                       
        Subsystems                                                     
        ==========                                                     
        The sub-systems are described in Bibring et al, 2007.          
                                                                       
                                                                       
        Measured Parameters                                            
        ===================                                            
        Stereoscopic imaging of the site surrounding the Lander
        (CIVA-P), and  optical imaging and infrared spectral imaging of
        surface and subsurface samples of the cometary nucleus, at a
        microscopic scale (CIVA-M).
        CIVA will analyse cometary material from micron size particles
        to meter size features: 7 micrometres to a few mm with the
        microscope, 1 mm to meters with the panoramic cameras.  
      