import pylab as pl  
import random 
time = pl.linspace(10000,1000000,100) 
N = 80*40 # number of gas molecules of each species 
sumA=[0.0]*120 
sumB=[0.0]*120 

def Diffusion(r,move,x,y):# where r is a random number from 0 to N-1, namely a random particle 
    # x and y are the coordinations of this particle, sites1 and sites2 corresponds to sitesA and sitesB, mol corresponds to molA or molB 
    if move == 0 and y+1<80: 
        if not sites[y+1][x]: #decide whether a site is occupied already
            sites[y+1][x] = sites[y][x] #update the occupied sites 
            sites[y][x] = 0 
            mol[r][1] += 1 # move the molecule 
    if move == 1 and y-1>=0: 
        if not sites[y-1][x]: #decide whether a site is occupied already 
            sites[y-1][x] = sites[y][x] #update the occupied sites 
            sites[y][x] = 0
            mol[r][1] -= 1 # move the molecule 
    if move ==2 and x-1>=0: 
        if not sites[y][x-1]: #decide whether a site is occupied already 
            sites[y][x-1] = sites[y][x] #update the occupied sites 
            sites[y][x] = 0 
            mol[r][0] -= 1 # move the molecule 
    if move ==3 and x+1<120: 
        if not sites[y][x+1]: #decide whether a site is occupied already 
            sites[y][x+1] = sites[y][x] #update the occupied sites 
            sites[y][x] = 0 
            mol[r][0] += 1 # move the molecule

for j in range(100):
    sites = [[p/40-1 for p in range (120)] for q in range (80)]
    mol = [[p/80+p/N*40, p%80] for p in range (2*N)]
    for i in range(int(time[j])):
        print j
        R = random.randint(0,2*N*4-1) # pick a random location occupied by an melocule and the direction of move
        move=R/(2*N)
        m=R%(2*N)
        xm, ym = (mol[m][0], mol[m][1]) # check for boundary condition
        Diffusion(m,move,xm,ym)
    for k in range (120):  
        for l in range (80):  
            if sites[l][k]==1:  
                sumB[k]+=1 
            elif sites[l][k]==-1:  
                sumA[k]+=1 
        sumA[k]/=(80.0*100.0)
        sumB[k]/=(80.0*100.0)
    
    
pl.plot([i for i in range(120)], sumA, '-ob')   
pl.plot([i for i in range(120)], sumB, '-or') 
pl.title('Linear population densities') 
pl.xlabel('x') 
pl.ylabel('density') 
pl.legend(['nA(x)', 'nB(x)'], loc="right") 
pl.savefig('densities.pdf') 
pl.show()
    
