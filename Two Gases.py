import pylab as pl
import random

time = 50000000
N = 80*40 # number of gas molecules of each species
sites = [[i/40-1 for i in range (120)] for j in range (80)]# recod whether a site is occupied, 1 denotes molecule A, -1 denotes molecule B and 0 deontes unoccupied
def Diffusion(r,m,x,y,sites):# where r is a random number from 0 to N-1, namely a random particle
    # x and y are the coordinations of this particle, sites1 and sites2 corresponds to sitesA and sitesB, mol corresponds to molA or molB
    if m == 1 and y+1<80: 
        if not sites[y+1][x]: #decide whether a site is occupied already 
            sites[y+1][x] = sites[y][x] #update the occupied sites
            sites[y][x] = 0
    if m == 2 and y-1>=0: 
        if not sites[y-1][x]: #decide whether a site is occupied already
            sites[y-1][x] = sites[y][x] #update the occupied sites
            sites[y][x] = 0
    if m ==3 and x-1>=0: 
        if not sites[y][x-1]: #decide whether a site is occupied already
            sites[y][x-1] = sites[y][x] #update the occupied sites
            sites[y][x] = 0
    if m ==4 and x+1<120: 
        if not sites[y][x+1]: #decide whether a site is occupied already
            sites[y][x+1] = sites[y][x] #update the occupied sites
            sites[y][x] = 0
    
for i in range(time):
    M = random.randint(0, 80*120-1) # pick a random location occupied by an melocule on the grid 
    if sites[M%80][M/80]:                    # if the location is occupied by molecule B
        x, y = (M/80, M%80) # check for boundary condition
        move = random.choice([1, 2, 3, 4])
        Diffusion(M,move,x,y,sites)
pl.imshow(sites, cmap='BrBG')
pl.title('Mixing of two Gases, t=%d' %time)
pl.xlabel('x')
pl.ylabel('y')
#pl.legend(['gas A', 'gas B'], loc="right")
pl.savefig('mixing_5.pdf')
pl.show()     

sumA=[0.0]*120
sumB=[0.0]*120
for i in range (120): 
    for j in range (80): 
        if sites[j][i]==1: 
            sumA[i]+=1
        elif sites[j][i]==-1: 
            sumB[i]+=1
pl.plot([i for i in range(120)], sumA, '-or')  
pl.plot([i for i in range(120)], sumB, '-ob')
pl.title('Linear population densities, t=10000000')
pl.xlabel('x')
pl.ylabel('density')
pl.legend(['nA(x)', 'nB(x)'], loc="right")
pl.savefig('densities_5.pdf')
pl.show()