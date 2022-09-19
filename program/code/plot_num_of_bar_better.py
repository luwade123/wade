import numpy as np
import matplotlib.pyplot as plt

left = np.array([1, 2, 3, 4, 5])
height1 = np.array([2313/2390,2273/2390,2279/2390,2262/2390,2245/2390])
height2 = np.array([74/2390*100,117/2390*100,110/2390*100,126/2390*100,140/2390*100])
height3 = np.array([3/2390*100,0/2390*100,1/2390*100,2/2390*100,5/2390*100])
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