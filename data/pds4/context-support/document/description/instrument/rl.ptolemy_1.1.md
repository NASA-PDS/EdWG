                                                       
                                                                              
        Instrument Overview                                                     
        ===================                                                     
        Ptolemy is part of the Rosetta instrument payload and is one of         
        two evolved gas analysers of the Lander space-craft Philae. It          
        provides data on the chemical and isotopic composition of the           
        nucleus of comet 67P/Churyumov-Gerasimenko.                             
                                                                                
                                                                                
        Scientific Objectives                                                   
        =====================                                                   
        The aims of Ptolemy are                                                 
        i) the determination of the chemical composition (accuracy 10%          
           and mass to charge ratio range 10-150) and                           
        ii) light element (H, C, N, O) isotopic composition of major            
            components with an accuracy of 1% of volatile and                   
            refractory cometary components                                      
                                                                                
                                                                                
        Calibration                                                             
        ===========                                                             
        The calibration of individual components (pressure sensors and          
        temperature sensors) is incorporated in the EGSE software.              
        Mass calibration of the mass spectrometer is achieved by using          
        argon gas as a mass marker in the helium gas supply system.             
                                                                                
                                                                                
        Operational Considerations                                              
        ==========================                                              
                                                                                
                                                                                
        Detectors                                                               
        =========                                                               
        The detector is an ion trap mass spectrometer.                          
                                                                                
                                                                                
        Electronics                                                             
        ===========                                                             
        Details on the electronics of the instrument are described in           
        the Ptolemy ADP.                                                        
                                                                                
        Location                                                                
        ========                                                                
        Ptolemy is mounted on the large Pi-plate in the warm                    
        compartment of Philae.  Samples are delivered by the Sample             
        Drilling and Distribution unit (SD2) to ovens located on the            
        balcony of Philae.                                                      
                                                                                
        Operational Modes                                                       
        =================                                                       
        Ptolemy operates in three distinct modes; Safe, Standby and             
        Science.  Housekeeping data is collected during all three               
        modes.  On power on, Ptolemy enters Safe mode.                          
        Safe mode is used for processor memory management such as               
        loading new science sequences and check memory commands. The            
        only mode change is from Safe to Standby mode.                          
        Standby mode is used to enable components for use during the            
        subsequent Science mode.  Ptolemy can be commanded to operate           
        a Science mode sequence or be returned to Safe mode.                    
        Science mode operates a previously loaded sequence. At the              
        successful completion of a Science mode sequence, Ptolemy               
        returns to Standby mode.                                                
                                                                                
        Subsystems                                                              
        ==========                                                              
        The subsystems are: Sample Collection (SC), Gas Distribution            
        and Processing System (GDPS), Gas Chromatography (GC), and              
        Mass Spectrometer (MS).                                                 
        Sample collection consists mainly of the SD2 instrument which           
        acquires solid samples and distributes them to Ptolemy ovens on         
        the carousel.  Gaseous samples can also be collected by an oven         
        filled with molecular sieve or be analysed directly by the mass         
        spectrometer.                                                           
        The Gas Distribution and Processing System consists of heaters,         
        valves temperature and pressure sensors in order to prepare the         
        sample for direct MS analysis or for injection into one of              
        three columns of the GC system.  The GDPS also contains                 
        reference materials so that the comet samples can be directly           
        compared with terrestrial compounds of known isotopic value.            
        The Gas Chromatography system includes 3 GC columns to separate         
        the sample into individual components as well as the helium             
        carrier gas required for gas chromatography.                            
        The Mass spectrometer analyses compounds giving a mass spectrum         
        as they are eluted from a GC column.                                    
        The sub-systems are described in more detail in Morse et al,            
        2009.                                                                   
                                                                                
                                                                                
        Measured Parameters                                                     
        ===================                                                     
        The Ptolemy GC measures the retention times of molecular                
        species in separation columns, the Ptolemy MS measures the mass         
        to charge ratio of ionised fragments of molecular species. The          
        temperature and pressure of various components are monitored.           
      