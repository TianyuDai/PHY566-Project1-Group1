import pylab as pl
import random
n=100#times of walk

def random_walk():#return final walker postion, xmean, x2mean, and r2mean
    walker=[0]*4#initialize walker, four elements denote four directions(right, left, upward and downward). 
    xsum=0#initialize sum{x_n}
    x2sum=0#initialize sum{x^2_n}
    r2sum=0#initialize sum{r^2_n}
    xmean=[0.0]*(n+1)#initialize sum{x_n}/n
    x2mean=[0.0]*(n+1)#initialize sum{x^2_n}/n
    r2mean=[0.0]*(n+1)#initialize sum{r^2_n}/n
    for i in range(n):
        movestep=random.randint(0,3)#random move in four equally probable directions
        walker[movestep]+=1#The number of steps in the certain direction plus 1
        xsum+=walker[0]-walker[1]#sum x_n from 0 to i
        x2sum+=(walker[0]-walker[1])**2#sum x_n^2 from 0 to i
        r2sum+=(walker[0]-walker[1])**2+(walker[2]-walker[3])**2#sum r_n^2 from 0 to i
        xmean[i+1]=float(xsum)/(i+1)#sum{x_n}/n where n=i
        x2mean[i+1]=float(x2sum)/(i+1)#sum{x_n^2}/n where n=i
        r2mean[i+1]=float(r2sum)/(i+1)#sum{r_n^2}/n where n=i
    return (xmean,x2mean,r2mean)#return final walker postion, xmean, x2mean, and r2mean

walks=10000#number of different walks
'''
Here, we sum data for all walks and then calculate the average
'''
x_average_sum=[0.0]*n
x2_average_sum=[0.0]*n
r2_average_sum=[0.0]*n
for i in range(walks):
    newdata=random_walk()
    x_average_sum=[x_average_sum[k]+newdata[0][k] for k in range(n)]
    x2_average_sum=[x2_average_sum[k]+newdata[1][k] for k in range(n)]
    r2_average_sum=[r2_average_sum[k]+newdata[2][k] for k in range(n)]
x_average=[k/walks for k in x_average_sum]#<x_n>
x2_average=[k/walks for k in x2_average_sum]#<x_n^2>
r2_average=[k/walks for k in r2_average_sum]#<r^2>

pl.plot(x_average,'s-',label='$<x_n>$')
pl.plot(x2_average,'.-',label='$<x_n^2>$')
pl.plot(r2_average,'o-',label='$<r^2>$')
pl.ylim(0, 50)
pl.xlabel('N')
pl.legend(loc=2)
pl.savefig('RandomWalk.pdf')
pl.show()
