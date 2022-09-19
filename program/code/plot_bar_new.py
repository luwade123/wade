import numpy as np
import matplotlib.pyplot as plt

left = np.array([1, 2, 3, 4, 5])
# height1 = np.array([225/227,225/227,220/227,216/227,219/227])
# height2 = np.array([2/227,2/227,7/227,11/227,8/227])
# height3 = np.array([2/227,2/227,7/227,11/227,8/227])
height1 = np.array([2319/2390,2268/2390,2286/2390,2297/2390,2260/2390])
height2 = np.array([70/2390*100,120/2390*100,103/2390*100,92/2390*100,127/2390*100])
height3 = np.array([1/2390*100,2/2390*100,1/2390*100,1/2390*100,3/2390*100])
labels = ['4_3', '4_2', '4_1', '4', '6']

#選擇要在下面的棒狀圖 blue
# plt.bar(left, height1, color='#2166ac', tick_label=labels,hatch='*',label = 'Stored in 1 switch')

#選擇要在上面的棒狀圖 red
plt.bar(left, height2, color='#ac4821', tick_label=labels,hatch='/',label = 'Stored in 2 switch')
plt.bar(left, height3, bottom=height2, color='#21acac', tick_label=labels,hatch='x',label = 'Stored in 3 switch')

# plt.ylim(0)
plt.title("Flow Stored Situation with sketch d = 5, w = 3") 
plt.xlabel("Topology") 
plt.ylabel("% of flows") 
plt.legend()
plt.show()