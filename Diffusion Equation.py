import pylab
from scipy.optimize import curve_fit
D=2.0	 			# Diffusion constant
M=100 				# position, denote as i in the first loop
N=30000 			# time, denote as j
dx=1
dt=0.01
x=pylab.linspace(-dx*M, dx*M, (2*M+1))
