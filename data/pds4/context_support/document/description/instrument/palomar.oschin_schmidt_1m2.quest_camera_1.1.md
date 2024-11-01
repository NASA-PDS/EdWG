The QUEST camera (Baltay et al. 2007) began operations at 
Palomar Observatory in June 2003 and replaced the tri-camera.  
It was designed and constructed at Yale University and 
consists of 112 CCD chips manufactured by the Sarnoff 
Corporation.  Four rows, or fingers, each contain twenty-
eight CCDs.  Each CCD is 600 x 2400 with 13 micron square 
pixels.  The pixel scale is 0.87 arc-sec/pixel.  The camera 
covers an area of 4.6 degrees by 3.6 degrees with an effective 
area of 9.6 square degrees of sky.  The central wavelength is 
760 nm.  During the point-and-track observations used by NEAT, 
a red (effective wavelength 610 nm) Bessel filter was used.

The table below provides a comparison of the QUEST and tri-camera
instruments used by NEAT at Palomar Observatory.

--------------------------------------------------------------
|  Site                  Pal/Tri-cam      Palomar/QUEST      |
|  Dates of Operation:  4/01 - 6/03       6/03 - 4/07        |
|  Telescope Diameter:      1.2m               1.2m          |
|  f/ratio:                 2.50               2.50          |
|  Camera:              4096 x 4096 x 3   600 x 2400 x 112   |
|  Pixel Size:             15 x 15 u          13 x 13 u      |
|  Pixel Scale:           1.01"/pix           0.87"/pix      |
|  Cooling:              TEC @ ~-30C        LN2 @ -120C      |
|  Filter:                   None             610 nm         |
|  IAU Site Code:            644                644          |
|                                                            |
|  Latitude / Longitude: +33deg 21.4'    116deg 51.8'W       |
|  Elevation / Timezone:   1726.3m           UTC - 8         |
|____________________________________________________________|



The fingers are symmetrical about the bore sight.  As a result, 
the pointing centers listed in the "logs-dot-group" file are the 
pointing centers of the bore sight; not CCD chip centers.  Fingers 
B and C are offset from the bore sight by +/-30.07 arc-secs 
(0.5012 deg.) while fingers A and D are offset by +/-90.17 arc-secs 
(1.5028 deg.), respectively.  The twenty-eight CCDs are laid out 
in a North-South orientation (chips 01-28) from +/-2.25 degrees 
(chips 01 - 28) from the bore sight pointing coordinates (see 
table 1, below).


          Finger
CCD     D        C
       RA       RA       DEC
01  -1.5028  -0.5012   2.2483
02  -1.5028  -0.5012   2.0819
03  -1.5028  -0.5012   1.9155
04  -1.5028  -0.5012   1.7490
05  -1.5028  -0.5012   1.5826
06  -1.5028  -0.5012   1.4160
07  -1.5028  -0.5012   1.2495
08  -1.5028  -0.5012   1.0829
09  -1.5028  -0.5012   0.9164
10  -1.5028  -0.5012   0.7498
11  -1.5028  -0.5012   0.5832
12  -1.5028  -0.5012   0.4166
13  -1.5028  -0.5012   0.2499
14  -1.5028  -0.5012   0.0833
15  -1.5028  -0.5012  -0.0833
16  -1.5028  -0.5012  -0.2499
17  -1.5028  -0.5012  -0.4155
18  -1.5028  -0.5012  -0.5832
19  -1.5028  -0.5012  -0.7498
20  -1.5028  -0.5012  -0.9164
21  -1.5028  -0.5012  -1.0829
22  -1.5028  -0.5012  -1.2495
23  -1.5028  -0.5012  -1.4160
24  -1.5028  -0.5012  -1.5826
25  -1.5028  -0.5012  -1.7490
26  -1.5028  -0.5012  -1.9155
27  -1.5028  -0.5012  -2.0819
28  -1.5028  -0.5012  -2.2483
--------------------------------
Table 1:  QUEST CCD chip offsets, in degrees, for 
          fingers C and D.  Fingers B and A are mirror 
          copies and consist of the same, positive, 
          values (ie finger B's RA offset is 0.5012 
          degrees and A's RA offset is 1.5028 degrees).


Regardless of the camera, each CCD chip read to a unique output 
file.  Filenames are based on the universal start time of the 
exposure and, if appropriate, identify the specific chip used.
Within the QUEST data, the overscan regions are available in 
the 40 extra rows (rows 600-640).  The QUEST images are 3.1 Mb 
in size, uncompressed, with North towards the left and West 
downward initially.