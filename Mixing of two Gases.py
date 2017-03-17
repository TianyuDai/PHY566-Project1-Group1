import pylab as pl
import numpy as np
import random

time = 10000000
N = 40*80 # number of gas molecules of each species
molA = pl.zeros([N,2]) # a matrix used to record all the melocules' coordinates of species A
molB = pl.zeros([N,2]) # a matrix used to record all the melocules' coordinates of species B
sitesA = pl.zeros([80,120]) # a matrix to recod whether a site is occupied by a molecule of A 
sitesB = pl.zeros([80,120]) # a matrix to recod whether a site is occupied by a molecule of B
for i in range(40):
    for j in range(80):
        molA[80*i+j,0] = i # initial coordiantes of every melocule
        molA[80*i+j,1] = j
        molB[80*i+j,0] = 80+i
        molB[80*i+j,1] = j
        sitesA[j,i] = 1 # the left third of the gird are occupied by a gas of species A
        sitesB[j,80+i] = 1 # the right third of the gird are occupied by a gas of species B

def Diffusion(r,m,x,y,sites1,sites2,mol):# where r is a random number from 0 to N-1, namely a random particle
    # x and y are the coordinations of this particle, sites1 and sites2 corresponds to sitesA and sitesB, mol corresponds to molA or molB
    if m == 1 and y+1<80:
        if not sites1[y+1,x]+sites2[y+1,x]:#decide whether a site is occupied already 
            sites1[y+1,x] = 1 #update the occupied sites
            sites1[y,x] = 0
            mol[r,1] = mol[r,1]+1 # move the molecule
    if m == 2 and y>0: 
        if not sites1[y-1,x]+sites2[y-1,x]: #decide whether a site is occupied already
            sites1[y-1,x] = 1 #update the occupied sites
            sites1[y,x] = 0
            mol[r,1] = mol[r,1]-1 # move the molecule
    if m ==3 and x>0:
        if not sites1[y,x-1]+sites2[y,x-1]: #decide whether a site is occupied already
            sites1[y,x-1] = 1 #update the occupied sites
            sites1[y,x] = 0
            mol[r,0] = mol[r,0]-1 # move the molecule
    if m ==4 and x<119:
        if not sites1[y,x+1]+sites2[y,x+1]:#decide whether a site is occupied already
            sites1[y,x+1] = 1 #update the occupied sites
            sites1[y,x] = 0
            mol[r,0] = mol[r,0]+1 # move the molecule
           
for i in range(time):
    A = random.randint(0,N-1) # pick a random location occupied by an A-melocule on the grid 
    xA, yA = (int(molA[A,0]), int(molA[A,1])) # check for boundary condition
    moveA = random.choice([1,2,3,4])
    Diffusion(A,moveA,xA,yA,sitesA,sitesB,molA)
    B = random.randint(0,N-1) # pick a random location occupied by a B-melocule on the grid
    xB, yB = (int(molB[B,0]), int(molB[B,1])) # check for boundary condition
    moveB = random.choice([1,2,3,4])
    Diffusion(B,moveB,xB,yB,sitesB,sitesA,molB)

#sitesA=np.loadtxt('sitesA.txt')
#sitesB=np.loadtxt('sitesB.txt')
#molA=np.loadtxt('molA.txt')
#molB=np.loadtxt('molB.txt')
    
pl.plot(molA[:,0],molA[:,1],'r.', molB[:,0],molB[:,1],'b.')
pl.xlim(0,119)
pl.ylim(0,79)
pl.title('Mixing of two Gases, t=%d' %time)
pl.xlabel('x')
pl.ylabel('y')
pl.savefig('mixing_5.pdf')
pl.show()     

pl.plot([i for i in range(120)], [sum(sitesA[:,i])/float(N) for i in range(120)], '-or')  
pl.plot([i for i in range(120)], [sum(sitesB[:,i])/float(N) for i in range(120)], '-ob')
pl.title('Linear population densities, t=%d' %time)
pl.xlabel('x')
pl.ylabel('density')
pl.legend(['nA(x)', 'nB(x)'], loc="right")
pl.savefig('densities_5.pdf')
pl.show()   

np.savetxt('sitesA.txt', sitesA)
np.savetxt('sitesB.txt', sitesB)
np.savetxt('molA.txt', molA)
np.savetxt('molB.txt', molB)
    
 

