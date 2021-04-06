# interpolate
ElapsedTimes.py

python ElapsedTimes.py
 
## Function
   The ElapsedTimes.py program reads in columns from the 
   SimDataFile.dat data file and compares time interval measurements 
   from the simulation with the Run 76 data values for 129 complete 
   oscillations.

   The Run 76 data times are based on the computer clock (not very precise)

   Example output for Simulation-48.

   graham:interpolate$ python ElapsedTimes.py 

   Found argument list: 

   Namespace(file='SimDataFile.dat')

   Simulation: elapsed time (s) =  151.23983563816347

   Data: elapsed time (s)       =  151.23968445

   Data - Simulation(s)  -0.00015118816347126085

   Simulation: mean period:  1.17240182665243

   Data: mean period:        1.1724006546511627

   Data/Simulation =  0.999999000341657

   [(D/S) - 1] (%)  -9.996583429927597e-05

## How to use this
   This can be used to adjust the simulation period to match the data 
   more exactly (or within some tolerance) when making further 
   adjustments to other model parameters 
