'''
Created on Jan 28, 2016

@author: Chris
'''
from pylab import *
import matplotlib.pyplot as plt
a=[]
b=[]
c=[]
i = 0
f = open('Output.txt', 'r')
data = f.read()
datalist = data.split()
length = len(datalist)
bound = int(length/3)
for i in range (0,bound):
    a.append(datalist[i*3])
    b.append(datalist[3*i+1])
    c.append(datalist[(3*i+2)])
    
    
    
plt.plot(a,b,'b')
plt.plot(a,c,'g')      
plt.xlabel('x values')
ylabel('function values')
title('Sin(x) vs x (blue) and Sin(x)/x vs x (Green)')
savefig('functions.jpeg')
savefig('functions.pdf')
savefig('functions.eps')
plt.show()     
    
    
    


