import numpy as np 
from matplotlib import pyplot as plt 
 
x = [1,2,3,4,5,6,7,8,9,10]
y1 = [95,104,102,96,105,106,97,104,103,102]
y2 = [30,31,33,27,34,28,31,30,30,27]
y3 = [10,8,10,9,9,10,10,9,9,10]
plt.title("Performance") 
plt.xlabel("sketch d/w") 
plt.ylabel("biggest ARE") 
plt.plot(x,y1,label='5/3') 
plt.plot(x,y2,label='5/6') 
plt.plot(x,y3,label='5/9') 
plt.legend()
plt.show()