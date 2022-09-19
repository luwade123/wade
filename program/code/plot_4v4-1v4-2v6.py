import numpy as np 
from matplotlib import pyplot as plt 
 
x = ['5/3','5/6','5/9','6/9']
y1 = [12.3442,4.1312,2.1324,1.4609]
y2 = [19.5973,6.7492,2.55145,2.3689]
y3 = [32.1634,12.2651,5.4217,4.9767]
y4 = [3.0608,0.9464,0.252,0.1404]
plt.title("Performance") 
plt.xlabel("sketch d/w") 
plt.ylabel("biggest ARE") 
plt.plot(x,y1,label='k=4') 
plt.plot(x,y2,label='k=4 with 1 disable') 
plt.plot(x,y3,label='k=4 with 2 disable') 
plt.plot(x,y4,label='k=6') 
plt.legend()
plt.show()