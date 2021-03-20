#
# TimeOfEnergyValue.py
#
# Scan through data file and find estimate of the time 
# at which the energy falls to xx% (for example 10%)
# using linear interpolation.
#
# Use argparse so that different values than the default can 
# also be given from the command line
#
# Example default usage:    python TimeOfEnergyValue.py
#         will calculate time at 10% energy using the default file
#
# Example alternative usage 2:
#         python TimeOfEnergyValue.py -e 15.0
#       - this calculates time at 15% energy using the default file
#
# Example alternative usage 3:
#         python TimeOfEnergyValue.py -f 'Oscillations-75.dat' -e 20.0
#       - this calculates time at 20% energy using the specified file
#
from matplotlib import pyplot as plt
import numpy as np
from pylab import *
#import sys
import argparse

# Use argparse to parse command line arguments. 
# Type python TimeOfEnergyValue.py -h for help (functionality works in standard fashion as script from command line).
parser = argparse.ArgumentParser(description='Calculator for Time of Energy Value')
parser.add_argument("-f", "--file", default='Oscillations.dat', help="input data file name")
parser.add_argument("-e", "--evalue", default=10.0, type=float, help="Energy value (%%)") # Need double-% for some reason...

args = parser.parse_args()
print(args)
print('file     =', args.file)
print('evalue   =', args.evalue)

# Read each line from the input data file into numpy arrays
# i time[s]   theta[rad]  omega[rad/s]   Energy[%]  theta_0[rad]  omega_0[rad/s]   drag-induced angular acceleration[rad/s^2]

ivalue, time, theta, omega, energy, theta0, omega0, alpha = genfromtxt(args.file, usecols=(0,1,2,3,4,5,6,7),unpack=True)

# Scan sequentially through the numpy arrays to find the two neighboring
# elements that straddle the requested energy percentage value. Assumes 
# that the values decrease monotonically and there is a straddle point.
# This could be done more efficiently and/or with more checks.
for i in range(0, energy.size):
    if energy[i] > args.evalue:
       i1 = i
       t1 = time[i]
       e1 = energy[i]
    if energy[i] <= args.evalue:
       i2 = i
       t2 = time[i]
       e2 = energy[i]
       break          #found the first second value - so we're done

print('Found straddling points, ',i1,t1,e1)
print('Found straddling points, ',i2,t2,e2)

tave = 0.5*(t1+t2)
eave = 0.5*(e1+e2)
print('Averaged estimate for t(s)=',tave,'with Eave(%)=',eave)

# Estimate dE/dt in the vicinity of E=Evalue using the two points
gradient=(e2-e1)/(t2-t1)
print('Gradient estimate (%/s) =',gradient)

# Simple linear interpolation
# See for example: https://en.wikipedia.org/wiki/Linear_interpolation

testimate = t1 + (args.evalue-e1)/gradient

print('-------------------------------------------------------------------------------------')
print('Estimated time at evalue(%) =',args.evalue,'using linear interpolation is',testimate,'s')
print('-------------------------------------------------------------------------------------')

# More sophisticated interpolation methods are possible 
# (using more points and/or more general functional form than 
#  a straight line). Probably not warranted.

