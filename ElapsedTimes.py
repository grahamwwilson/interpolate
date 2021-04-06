#
# ElapsedTimes.py
#
# Scan through SimDataFile.dat file and find time elapsed between
# "calibration events"
#
#
from matplotlib import pyplot as plt
import numpy as np
from pylab import *
import argparse

# Use argparse to parse command line arguments. 
# Type python ElapsedTimes.py -h for help (functionality works in standard fashion as script from command line).
parser = argparse.ArgumentParser(description='Calculator for Elapsed Times')
parser.add_argument("-f", "--file", default='SimDataFile.dat', help="input data file name")

args=parser.parse_args()
print('Found argument list: ')
print(args)
simfile=args.file

# Read each line from the input data file into numpy arrays
# eventtype event clockticks time[s]  Energy[%]
sim_type = genfromtxt(simfile, usecols=0, unpack=True, dtype=str)
sim_event, sim_clockticks, sim_time, sim_energy = genfromtxt(simfile, usecols=(1,2,3,4), unpack=True)

# Now calculate relevant quantities
tstart=0.5*(sim_time[2]+sim_time[3])
tend=0.5*(sim_time[1034]+sim_time[1035])

elapsed_time = tend-tstart
mean_period = elapsed_time/129.0

data_time=151.23968445
data_period=data_time/129.0

print('Simulation: elapsed time (s) = ',elapsed_time)
print('Data: elapsed time (s)       = ',data_time)
print('Data - Simulation(s) ',data_time-elapsed_time)
print('Simulation: mean period: ',mean_period)
print('Data: mean period:       ',data_period)
print('Data/Simulation = ',data_period/mean_period)
ratio=data_period/mean_period
print(' [(D/S) - 1] (%) ',100.0*(ratio-1.0))
