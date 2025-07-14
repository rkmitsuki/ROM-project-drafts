from scipy.stats import qmc 
import math 
import numpy
from random import random
npara = int(3)
nsamp = int(250)
l_bound = [0,0,0]
u_bound = [1,1,1]
sampler = qmc.LatinHypercube(d=npara)
sample = sampler.random(n=nsamp)


lub = qmc.scale(sample,l_bound,u_bound)



def feval(co): 
    x,y,z = co
    return 0.26*math.sqrt(x*x+y*y+100*z*z) - 0.18*math.pow(abs(x*y*z),1/3) 
fr = [feval(l) for l in lub]  
fr = numpy.reshape(fr,(nsamp,1))

with open("doe.txt","w") as doe1:
    doe1.write("#n \t x \t y \t z \n")
    doe1.write("#n \t unit \t unit \t unit \n")
    doe1.write("#n \t Float \t Float \t Float \n")
    for item,it in zip(lub,fr):
        doe1.write("%s \t %s \t %s \t %s \n" %(item[0],item[1],item[2],it[0]))


import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

f = open("doe.txt")
f1 = open("doe1.txt","w") 
lines=f.readlines()[3:]
for line in lines:
    f1.write("%s \n" %line) 
f.close()
f1.close()

data=pd.read_csv('doe1.txt',sep='\t',header=None)


mpl.rcParams['legend.fontsize'] = 10 
fig = plt.figure()
ax = fig.add_subplot(projection='3d') 
##ax.set_xlim(xmin=-10,xmax=10)
##ax.set_ylim(-10,10)
##ax.set_zlim(-10,10)

x,y,z,t = data[0],data[1],data[2],data[3]
ax.scatter(x,y,z,color='red') 
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.savefig('3Ddata.png', dpi=500) 
plt.show()