'''
Created on Jan 26, 2016

@author: Chris
'''
import matplotlib.pyplot as plt
from pylab import *
import math
init = float(-10)
init2 = float(-10)
list0 = []
list1 = []
list2 = []
while (init <= 10):
    temp = 0
    temp = math.sin(init)
    list0.append(init)
    list1.append(temp)
    init = init + .05
    
while (init2 <= 10):
    temp = 0 
    temp = math.sin(init2)/init2  
    list2.append(temp)
    init2 = init2 + .05
        
plt.plot(list0,list1,'b')
plt.plot(list0,list2,'g')      

plt.xlabel('x values')
ylabel('function values')
title('Sin(x) vs x (blue) and Sin(x)/x vs x (Green)')
plt.show() 

