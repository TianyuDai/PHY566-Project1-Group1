import pylab as pl  
import random 
time = 10**6
N = 80*40 # number of gas molecules of each species 
sites = [[i/40-1 for i in range (120)] for j in range (80)]# recod whether a site is occupied, 1 denotes molecule A, -1 denotes molecule B and 0 deontes umoccupied 
mol = [[i/80+i/N*40, i%80] for i in range (2*N)] # Initialize coordinates of every molecule, first N rows are molecule A and second N row are molecule B 

for i in range(time): 
    R = random.randint(0,2*N*4-1) # pick a random number to decide the location occupied by an melocule and its moving direction 
    m=R%(2*N) # the molecule decided by the random number
    move=R/(2*N) # moving direction of the molecule
    
    x, y = (mol[m][0], mol[m][1]) # coordinates of the molecule
    if move == 0 and y+1<80: # moving direction and boundary condition
        if not sites[y+1][x]: #decide whether a site is occupied already
            sites[y+1][x] = sites[y][x] #update the occupied sites 
            sites[y][x] = 0 
            mol[m][1] += 1 # move the molecule 
    if move == 1 and y-1>=0: # moving direction and boundary condition 
        if not sites[y-1][x]: #decide whether a site is occupied already 
            sites[y-1][x] = sites[y][x] #update the occupied sites 
            sites[y][x] = 0
            mol[m][1] -= 1 # move the molecule 
    if move ==2 and x-1>=0: # moving direction and boundary condition
        if not sites[y][x-1]: #decide whether a site is occupied already 
            sites[y][x-1] = sites[y][x] #update the occupied sites 
            sites[y][x] = 0 
            mol[m][0] -= 1 # move the molecule 
    if move ==3 and x+1<120: # moving direction and boundary condition
        if not sites[y][x+1]: #decide whether a site is occupied already 
            sites[y][x+1] = sites[y][x] #update the occupied sites 
            sites[y][x] = 0 
            mol[m][0] += 1 # move the molecule 
    
pl.imshow(sites, cmap='bwr') 
pl.title('Mixing of two Gases')#, t=%d' %time) 
pl.xlabel('x') 
pl.ylabel('y') 
pl.savefig('mixing_try.jpg') 
pl.show()      

sumA=[0.0]*120 
sumB=[0.0]*120 
for i in range (120):  
    for j in range (80):  
        if sites[j][i]==1:  
            sumB[i]+=1 # counting how many B molecules are there on every column of the grid.
        elif sites[j][i]==-1:  
            sumA[i]+=1 # counting how many A molecules are there on every column of the grid.
    sumA[i]/=80.0 # linear population density xA
    sumB[i]/=80.0 # linear population density xB
pl.plot([i for i in range(120)], sumA, '-ob')   
pl.plot([i for i in range(120)], sumB, '-or') 
pl.title('Linear population densities t=%d' %time) 
pl.xlabel('x') 
pl.ylabel('density') 
pl.legend(['nA(x)', 'nB(x)'], loc="right") 
pl.savefig('densities_init.jpg') 
pl.show()  
