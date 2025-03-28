                                           
                                                                     
                                               

        Scientific Objectives and Experiment Overview                   
        =============================================                   
        ROLIS is a miniature Charge Coupled Device (CCD) imager
        pointing downwards from the balcony of the Rosetta Lander.
        From here, ROLIS can observe about 30x30 cm of the nucleus 
        surface below the Lander at a spatial sampling of 0.3mm/pixel.
        In order to illuminate the image field, ROLIS incorporates four
        independent arrays of light emitting diodes (LEDs) radiating
        through the visible and near-IR, in spectral bands 
        centred at 470, 530, 640 and 870nm, with a Full Width Half
        Maximum of about 100nm.
        ROLIS will also operate during the descent phase, imaging the
        landing site and its vicinity shortly before touchdown.
              
        From images of the cometary surface ROLIS will seek to identify
        the possible presence of a dust mantle, refractory crust and
        exposed ice.
        If present, surface features such as pores, cracks and vents
        would be readily detected, as well as traces of erosion caused
        by sublimation, ice grains and carbonaceous aggregates larger
        than the ROLIS spatial resolution limits.
        
        Together, the descent sequence and the close-up images will
        reveal the surface features over a broad range of scale
        lengths, allowing an assessment of the surface's diversity.
        
        Multi-spectral imaging in four spectral channels will allow us
        to complement the spatial information with spectral information.
        Although the limited spectral range and resolution of ROLIS will
        not allow exact mineralogy to be extracted, the study of the
        spectral slope should allow a broad classification of the solid
        surface phases to be derived, distinguishing between
        carbonaceous, silicates and organic materials. Further, the
        analysis of colour ratios over a given field will provide
        information on the degree of soil heterogeneity at small scales.
   
  
        Operational Considerations                                     
        ==========================                                     
  
        The Rosetta Lander and its payload are designed to achieve the
        primary mission goals within 3 days of landing, which takes
        place when the comet is at a heliocentric distance of 3 AU,
        before the onset of major cometary activity. Rosetta will
        approach the comet in the year 2014 and will start its descent
        phase at the ending of 2014. Should an extended mission be
        possible, it will be of great interest to use ROLIS to search
        for signs of evolution of the surface features as the
        Churyumov-Gerasimenko (CG) approaches the Sun.
  
        The ROLIS camera is designed for operations at temperatures 
        down to -150 deg C what makes it possible to operate on the
        comet between approximately 3.5 to 1.8 AU. The comparatively
        warm temperatures at 1.8 AU would not be a problem for ROLIS
        either.
                             
        Imaging the borehole sides could reveal stratification and
        provide 
        clues on the mechanical strength of the surface layer. This
        could be achieved by rotating the Lander around its axis by a
        few degrees.
  
        The detection and precise measurement of the surface features
        would be greatly facilitated by the acquisition of stereo
        pairs, also achieved by rotating the Lander. They would provide
        the additional information from the lone-of-sight dimension,
        making it easier to identify surface features visually and to
        quantify their dimensions.
  
        
                                                                       
        Calibration                                                    
        ===========                                                    
        Following calibration functions are applied to the ROLIS
        images at DLR :
              1) Dark correction: Each image is corrected by
                 subtracting a dark frame derived by ground or
                 in-flight calibrations.
              
              2) Flat filed correction: each image is corrected by
                 applying calibration flat fields derived during ground
                 calibration.
              
              3) If possible, photometric cross-calibration with OSIRIS
                 data
                                                                       
                                                               
        Electronics                                                    
        ===========                                                    
        The Imaging Main Electronics (IME) is a facility device,
        developed under the co-responsibility of IWP/DLR and IAS, for
        both ROLIS and CIVA: they share a common interface with the
        Lander, for both the power subsystem and the Central Data
        Management System (CDMS).
  
        The ROLIS IME tasks include implementation of the commanding
        interface to the Lander, data acquisition from the ROLIS-D
        camera, local storage of the images, image processing and
        compression, recording of HK information and the data link to
        the Lander. In addition, it provides storage, commanding, and
        telemetry support for the CIVA instrument, which is interfaced
        through a dedicated digital signal processor board.
        The ROLIS-part of IME consists of the DPU- and the MM- (Mass
        Memory) boards. The DPU is based on a Harris RTX 2010 processor
        running at 10 MHz and programmed in FORTH. The ROLIS experiment
        S/W is stored in a 64-kByte EEPROM, which can be partially or
        completely uploaded during flight.
        The MM consists of 16 MBytes of static RAM which is used as
        buffer for images and temporary storage. The memory enables
        the storage of a maximum of 7 uncompressed images and several
        compressed images, which number depends on their compression
        ratio, and is allocated to both the ROLIS and CIVA experiments.
  
        To gain comprehensive information about the ROLIS-DPU here a 
        few details:
        - Processor: Harris RTX-2010RH at 10 MHz
        - FPGA: Actel 1280 RH 
        - 16 KByte PROM with Common DPU (ComDPU) Software
        - 64 KByte EEPROM with ROLIS Software
        - 256 KByte SRAM
        - 14 bit ADC for ROLIS and CIVA analogue HK
        - interface to CDMS (max. 32 kbps), Watchdog
        - 78 kbps serial DPU-DPU I/F to the CIVA part of IME
        - Extension bus for special experiment hardware.
  
        The following notes contain details about the ROLIS MM:
        - FPGA: Actel 54SX16 RT 
        - 4x 32 Mbit SRAM cubes for images 
        - Memory controller
        - High-speed serial I/F to the ROLIS-D (10 Mbits per second).
  
  
        Accommodation                                                  
        ============                                                   
        The two main modules of ROLIS, the ROLIS-D camera and the
        on-board processor unit & Mass Memory as part of the IME are
        located on the Lander at different sites:
        The IME is located in the warm compartment of PHILAE in the
        Central Elelectronics Box (CEB-Z) , whereas ROLIS-D is situated
        on the Lander balcony. Both ROLIS constituents are connected
        via a cable. 
                              
        The ROLIS-D location on the  instrument common working circle 
        allows it to inspect the sampling sites of the Lander's in situ
        analyzers before and after the drilling operation. Such 
        inspection, achieved by rotating the Lander body, can provide
        an important contribution to the interpretation of the sample
        analysis, by placing these measurements into the context of the
        surface colours and morphology. 
        Software
        ========
        Two types of software are used: 
        1. ComDPU software (in the PROM)
        2. ROLIS software (in the EEPROM).
   
        After power switch on first the ComDPU software will be copied
        into RAM and started from the RAM. Analogue for the ROLIS
        software: after starting the boot process the ROLIS software
        will be copied from the EEPROM into the RAM (overwriting the
        ComDPU software) and get started.
  
        Detector Geometry
        =============                                             
        The ROLIS CCD consists of a matrix of a total of 1066x1064 pixels
        of which 1024x1024 are active and are used for imaging. 
        
        Each line consists of 1066 elements organized as follows:
            
        - 2 dummy pixel	
        - 10 inactive prescan pixels (can be used to estimate bias level)
        - 1 isolation pixel 
        - 16 masked pixels (can be used to estimate dark current)
        - 5 isolation pixels
        - 1024 useful imaging pixels 
        - 8 inactive postscan pixels (can be used to estimate bias level)
       
        Each frame is made of 1064 lines organized as follows:
        
        - 1 dummy line
        - 12 masked lines (can be used to estimate dark current)
        - 3 isolation lines
        - 1024 useful imaging lines 
        - 3 isolation lines
        - 12 masked lines (can be used to estimate dark current)
        - 1 dummy line
        - 8 inactive postscan lines (can be used to estimate bias level)
  
        Imaging Modes                                              
        =============                                             
        ROLIS can be operated in 3 basic imaging modes:
  
        - SINGLE IMAGE MODE
         In this mode the 1024x1024 active area is stored. The image
         can be acquired with or without LED illumination.
         
        - DESCENT IMAGING RING-BUFFER-MODE
         In this mode the 1024x1024 active area is stored in the 7-position
         ring buffer. The newest images overwrite the oldest one. 
         The acquisition sequence is stopped by the touchdown signal.
         The images are acquired without LED illumination.
        
        - FULL-FRAME IMAGE STRIPE                       
         In this mode the full 1066x1064 array is readout, but only 
         a 1066x30 subframe is relayed. This mode is used for diagnostic 
         and for monitoring the bias level and dark generation.
              
        Measured Parameters                                            
        ===================                 
        The basic product of ROLIS are images.
        The ROLIS-D optics project a square Field Of View 
        of 57.7 deg x 57.7 deg onto the CCD. This gives a sampling of 
        about 0,33mm/pixel at an object distance of 30cm. With the
        Infinity Lens (IFL) in the optical path, the objective is
        focused for objects at distances ranging from 1.4m to infinity.
        With it removed, the camera is focused at an object distance
        of 30cm with a depth of field of approximately (+10; -8) cm.
    
      