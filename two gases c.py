import pylab as pl  
import random
import numpy as np
time = 10**8
N = 80*40 # number of gas molecules of each species
runs = 10
sumA=[0.0]*120 
sumB=[0.0]*120 

for j in range(runs):
    sites = [[p/40-1 for p in range (120)] for q in range (80)] # a matrix to record whether a site is ocuppied by molecule of A or B
    mol = [[p/80+p/N*40, p%80] for p in range (2*N)] # a matrix used to record all the melocules' coordinates
    for i in range(time):
        print j, i
        R = random.randint(0,2*N*4-1) # pick a random location occupied by an melocule and the direction of move
        move=R/(2*N)
        m=R%(2*N)
        x, y = (mol[m][0], mol[m][1]) # check for boundary condition
        if move == 0 and y+1<80: 
            if not sites[y+1][x]: #decide whether a site is occupied already
                sites[y+1][x] = sites[y][x] #update the occupied sites 
                sites[y][x] = 0 
                mol[m][1] += 1 # move the molecule 
        if move == 1 and y-1>=0: 
            if not sites[y-1][x]: #decide whether a site is occupied already 
                sites[y-1][x] = sites[y][x] #update the occupied sites 
                sites[y][x] = 0
                mol[m][1] -= 1 # move the molecule 
        if move ==2 and x-1>=0: 
            if not sites[y][x-1]: #decide whether a site is occupied already 
                sites[y][x-1] = sites[y][x] #update the occupied sites 
                sites[y][x] = 0 
                mol[m][0] -= 1 # move the molecule 
        if move ==3 and x+1<120: 
            if not sites[y][x+1]: #decide whether a site is occupied already 
                sites[y][x+1] = sites[y][x] #update the occupied sites 
                sites[y][x] = 0 
                mol[m][0] += 1 # move the molecule
    for k in range (120):  
        for l in range (80):  
            if sites[l][k]==1:  
                sumB[k]+=1 
            elif sites[l][k]==-1:  
                sumA[k]+=1

np.savetxt('sumA_1.txt',sumA)
np.savetxt('sumB_1.txt',sumB)

pl.plot([i for i in range(120)], [j/(80.0*runs) for j in sumA], '-ob')   
pl.plot([i for i in range(120)], [j/(80.0*runs) for j in sumB], '-or') 
pl.title(' Average linear population densities, t=%d' %time) 
pl.xlabel('x') 
pl.ylabel('density') 
pl.legend(['nA(x)', 'nB(x)'], loc="right") 
pl.savefig('average densities.pdf') 
pl.show() 
