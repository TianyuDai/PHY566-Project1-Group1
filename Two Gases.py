import pylab as pl  
import random 
time = 500000000 
N = 80*40 # number of gas molecules of each species 
sites = [[i/40-1 for i in range (120)] for j in range (80)]# recod whether a site is occupied, 1 denotes molecule A, -1 denotes molecule B and 0 deontes umoccupied 
mol = [[i/80+i/N*40, i%80] for i in range (2*N)] # Initialize coordinates of every molecule, first N rows are molecule A and second N row are molecule B 

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

for i in range(time): 
    R = random.randint(0,2*N*4-1) # pick a random location occupied by an melocule and the direction of move
    move=R/(2*N)
    m=R%(2*N)
    xm, ym = (mol[m][0], mol[m][1]) # check for boundary condition
    Diffusion(m,move,xm,ym) 

pl.imshow(sites, cmap='bwr') 
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
    sumA[i]/=80.0
    sumB[i]/=80.0
pl.plot([i for i in range(120)], sumA, '-or')   
pl.plot([i for i in range(120)], sumB, '-ob') 
pl.title('Linear population densities, t=%d' %time) 
pl.xlabel('x') 
pl.ylabel('density') 
pl.legend(['nA(x)', 'nB(x)'], loc="right") 
pl.savefig('densities_5.pdf') 
pl.show()  
