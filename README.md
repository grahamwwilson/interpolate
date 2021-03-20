# interpolate
estimate time at specific energy using linear interpolation

This code is pretty straightforward.
 
1. It reads in columns from a data file. 
   (the method supports compressed files too)

The default input file is specified as Oscillations.dat (works for both 
compressed and uncompressed files).

The file can also be compressed (to save space). 

The supplied files are compressed and named, 
Oscillations.dat.gz and Oscillations2.dat.gz

To view at command line you can use less.
ie. less Oscillations.dat.gz
or uncompress it
gunzip Oscillations.dat.gz (results in file Oscillations.dat)

To compress again,  gzip Oscillations.dat

2. The program uses "argparse" to parse command line arguments. 
To understand usage type 

python TimeOfEnergyValue.py -h

If you do not have argparse installed you will need to install it.

pip3 install argparse 

3. Some examples are included in Example_Output.txt 
illustrating results with different arguments on the two files.

