import pylab
from scipy.optimize import curve_fit
D=2.0	 			# Diffusion constant
M=100 				# position, denote as i in the first loop
N=30000 			# time, denote as j
dx=1
dt=0.01
x=pylab.linspace(-dx*M, dx*M, (2*M+1))
phi=[[pylab.exp(-10*i*i) for i in x] for j in range (N)] 						# Initialize phi as sharply peaked around x=0
num_sigma=[]
for j in range (N-1): 
	for i in range (2*M): 
		phi[j+1][i]=phi[j][i]+D*dt/dx/dx*(phi[j][i+1]+phi[j][i-1]-2*phi[j][i]) 		# Iteration of phi to get the value of each x for every time snapshot
def Normal(x, sigma):  																# Normal distribution
	return 1/pylab.sqrt(2*pylab.pi*sigma*sigma)*pylab.exp(-x*x/2/sigma/sigma)
def cal(k):  																		# Fitting value of sigma at different time
	sigfit, err=curve_fit(Normal, x, phi[k])
	num_sigma.append(sigfit) 														# Record the fitting value in the list num_sigma
num_t=[100, 5000, 12000, 20000, 28000] 												# Five time nodes to be snapshotted
theo_t=pylab.linspace(0, (N-1)*dt, 300)
theo_sigma=[pylab.sqrt(2*D*i) for i in theo_t] 										# Theoretical dependence of sigma and t
for i in num_t:  																	# Fit for different snapshot
	cal(i)
pylab.plot([i*dt for i in num_t], num_sigma, 'o') 									# Numerical plot
pylab.plot(theo_t, theo_sigma)   													# Theoretical plot
pylab.title('Dependence of $\sigma$ and t')
pylab.xlabel('Time t (s)')
pylab.ylabel('$\sigma$')
pylab.legend(['Fitting', 'Theoretical'], loc=0)
pylab.savefig('sigma.pdf')
pylab.show()
