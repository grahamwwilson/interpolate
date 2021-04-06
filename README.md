# interpolate
TimeOfEnergyValue.py

Estimate time at specific energy using linear interpolation
 
## 1. Data formats
   The TimeOfEnergyValue.py program reads in columns from the 
   Oscillations data file and estimates the time at which the 
   energy percentage is a specified 
   value based on linear interpolation.

   The default input file is specified as Oscillations.dat (works for 
   both compressed and uncompressed files). The file can also be 
   compressed (to save space). 

   The supplied files are compressed and named, 
   Oscillations.dat.gz and Oscillations2.dat.gz

   To view the compressed files at the command line you can use less.
   ie. less Oscillations.dat.gz
   or uncompress it
   gunzip Oscillations.dat.gz (results in file Oscillations.dat)
   To compress again,  gzip Oscillations.dat

## 2. argparse
   The program uses "argparse" to parse the two command line 
   arguments, namely the file name and the energy percentage.

   To understand usage type 
   python TimeOfEnergyValue.py -h

   If you do not have argparse installed you will need to install it.
   For python3,
   pip3 install argparse

## 3. Examples
   Some examples are included in Example_Output.txt illustrating 
   results with different arguments on the two supplied files.
