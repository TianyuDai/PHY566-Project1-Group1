import pylab as pl
import random

time = 500000
N = 80*40 # number of gas molecules of each species
sites = [[i/40-1 for i in range (120)] for j in range (80)]# recod whether a site is occupied, 1 denotes molecule A, -1 denotes molecule B and 0 deontes umoccupied
molA = [[int(i/80), i%80] for i in range (N)] # Initialize coordinates of every molecule
molB = [[int(i/80)+80, i%80] for i in range (N)]

def Rmove(x, y):
    if x == 0 and y == 0:
        move=random.choice([1,4])
    if x == 0 and y == 79:
        move=random.choice([2,4])
    if x == 0 and y != 0 and y != 79:
        move=random.choice([1,2,4])
    if x == 119 and y == 0:
        move= random.choice([1,3])
    if x == 119 and y == 79:
        move=random.choice([2,3])
    if x == 119 and y != 0 and y != 79:
        move=random.choice([1,2,3])
    if y == 0 and x != 0 and x != 119:
        move=random.choice([1,3,4])
    if y == 79 and x != 0 and x != 119:
        move=random.choice([2,3,4])
    if x != 0 and x != 119 and y != 0 and y != 79:
        move = random.choice([1,2,3,4]) # the A-melocule moves at random one position up/down/left/right
    return move

def Diffusion(r,m,x,y,sites, k, mol):# where r is a random number from 0 to N-1, namely a random particle
    # x and y are the coordinations of this particle, sites1 and sites2 corresponds to sitesA and sitesB, mol corresponds to molA or molB
    if m == 1 and sites[y+1][x] == 0: #decide whether a site is occupied already 
        sites[y+1][x] = k #update the occupied sites
        sites[y][x] = 0
        mol[r][1] = mol[r][1]+1 # move the molecule
    if m == 2 and sites[y-1][x] == 0: #decide whether a site is occupied already
        sites[y-1][x] = k #update the occupied sites
        sites[y][x] = 0
        mol[r][1] = mol[r][1]-1 # move the molecule
    if m ==3 and sites[y][x-1] == 0: #decide whether a site is occupied already
        sites[y][x-1] = k #update the occupied sites
        sites[y][x] = k
        mol[r][0] = mol[r][0]-1 # move the molecule
    if m ==4 and sites[y][x+1] == 0: #decide whether a site is occupied already
        sites[y][x+1] = k #update the occupied sites
        sites[y][x] = k
        mol[r][0] = mol[r][0]+1 # move the molecule
    
       
for i in range(time):
    m = random.randint(0,2*N-1) # pick a random location occupied by an melocule on the grid 
    if m/3200:                    # if the location is occupied by molecule B
        xB, yB = (int(molB[m-3200][0]), int(molB[m-3200][1])) # check for boundary condition
        moveB = Rmove(xB,yB)
        Diffusion(m-3200,moveB,xB,yB,sites,1,molB)
    else:    # if the location is occupied by molecule A
        xA, yA = (int(molA[m][0]), int(molA[m][1])) # check for boundary condition
        moveA = Rmove(xA,yA)
        Diffusion(m,moveA,xA,yA,sites,-1,molA)
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