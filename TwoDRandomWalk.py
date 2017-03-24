import pylab as pl
import random
n=100#times of walk
nlist=[i for i in range(n)]#time list

def random_walk(n):#return final walker postion, xmean, x2mean, and r2mean
    walker=[0,0]#initialize walker
    x=0
    x2=0
    r2=0
    xlist=[0.0]*(n+1)
    x2list=[0.0]*(n+1)
    r2list=[0.0]*(n+1)
    for i in range(n):
        movestep=random.randint(0,3)#random move in four equally probable directions
        if movestep==0:
            walker[0]+=1 # add 1 to the number of total steps in this direction
        elif movestep==1:
            walker[0]-=1
        elif movestep==2:
            walker[1]+=1
        else:
            walker[1]-=1
        x=walker[0]#x
        x2=(walker[0])**2#x^2
        r2=(walker[0])**2+(walker[1])**2#r^2=x^2+y^2
        xlist[i+1]=float(x)#sum{x_n}/n where n=i
        x2list[i+1]=float(x2)#sum{x_n^2}/n where n=i
        r2list[i+1]=float(r2)#sum{r_n^2}/n where n=i
    return (xlist,x2list,r2list)#return xmean, x2mean, and r2mean

walks=10000#number of different walks
'''
Here, we sum data for all walks and then calculate the average
'''
x_average_sum=[0.0]*(n+1)
x2_average_sum=[0.0]*(n+1)
r2_average_sum=[0.0]*(n+1)
for i in range(walks):
    newdata=random_walk(n)
    x_average_sum=[x_average_sum[k]+newdata[0][k] for k in range(n+1)]
    x2_average_sum=[x2_average_sum[k]+newdata[1][k] for k in range(n+1)]
    r2_average_sum=[r2_average_sum[k]+newdata[2][k] for k in range(n+1)]
x_average=[x_average_sum[k]/walks for k in range(n+1)]#<x_n>
x2_average=[x2_average_sum[k]/walks for k in range(n+1)]#<x_n^2>
r2_average=[r2_average_sum[k]/walks for k in range(n+1)]#<r^2>

pl.plot(x_average,'.-',label='$<x_n>$')
pl.plot(x2_average,'s-',label='$<x_n^2>$')
pl.plot(r2_average,'o-',label='$<r^2>$')
pl.xlabel('n')
pl.ylim(-10, 100)
pl.legend(loc=2)
pl.savefig('RandomWalk.pdf')
pl.show()
