import pylab
from scipy.optimize import curve_fit
D=2.0	 			# Diffusion constant
M=100 				# position, denote as i in the first loop
N=30000 			# time, denote as j
dx=1
dt=0.01
x=pylab.linspace(-dx*M, dx*M, (2*M+1))
phi=[[pylab.exp(-10000*i*i) for i in x] for j in range (N)] 						# Initialize phi as sharply peaked around x=0
num_sigma=[]
