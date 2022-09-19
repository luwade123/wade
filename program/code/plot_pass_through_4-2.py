import numpy as np 
from matplotlib import pyplot as plt 

algo_5_3_k1_x =[398, 384, 326, 316, 0, 0, 0, 0, 636, 634, 564, 566, 0, 0, 0, 0, 244, 244, 244, 244]
b1_5_3_k1_x = [398, 384, 326, 316, 0, 0, 0, 0, 636, 634, 566, 564, 0, 0, 0, 0, 244, 244, 244, 244]
b2_5_3_k1_x = [398, 384, 326, 316, 0, 0, 0, 0, 636, 634, 566, 564, 0, 0, 0, 0, 244, 244, 244, 244]
b3_5_3_k1_x =[414, 424, 350, 386, 130, 130, 134, 132, 810, 806, 712, 714, 306, 314, 318, 302, 548, 546, 544, 544]

algo_5_3_k5_x = [398, 384, 326, 316, 4, 2, 4, 2, 634, 636, 566, 564, 14, 14, 14, 12, 256, 256, 256, 250]
b1_5_3_k5_x = [398, 384, 326, 316, 4, 4, 2, 2, 634, 636, 570, 560, 14, 14, 12, 12, 258, 252, 258, 248]
b2_5_3_k5_x = [398, 384, 326, 316, 2, 2, 4, 2, 636, 634, 564, 566, 12, 12, 14, 14, 254, 252, 256, 256]
b3_5_3_k5_x =  [406, 398, 366, 352, 144, 162, 134, 134, 784, 786, 702, 694, 376, 346, 320, 320, 562, 564, 554, 552]


algo_5_3_k1_y = []
b1_5_3_k1_y = [] 
b2_5_3_k1_y = [] 
b3_5_3_k1_y = [] 

algo_5_3_k5_y = []
b1_5_3_k5_y = [] 
b2_5_3_k5_y = [] 
b3_5_3_k5_y = [] 

x_k1 = [algo_5_3_k1_x,b1_5_3_k1_x,b2_5_3_k1_x,b3_5_3_k1_x]
x_k5 = [algo_5_3_k5_x,b1_5_3_k5_x,b2_5_3_k5_x,b3_5_3_k5_x]

y_k1 = [algo_5_3_k1_y,b1_5_3_k1_y,b2_5_3_k1_y,b3_5_3_k1_y]
y_k5 = [algo_5_3_k5_y,b1_5_3_k5_y,b2_5_3_k5_y,b3_5_3_k5_y]

sorted_x_k1 =[]
sorted_x_k5 =[]
sum_k1 = []
sum_k5 = []
for i in x_k1:
    tmp = 0
    for data in i:
        tmp += data
    sum_k1.append(tmp)

for i in x_k5:
    tmp = 0
    for data in i:
        tmp += data
    sum_k5.append(tmp)


for index,x in enumerate(x_k1):
    tmp = 0
    tmp_x = sorted(x)
    sorted_x_k1.append(tmp_x)
    for data in tmp_x:
        tmp += data
        y_k1[index].append(tmp/sum_k1[index])

for index,x in enumerate(x_k5):
    tmp = 0
    tmp_x = sorted(x)
    sorted_x_k5.append(tmp_x)
    for data in tmp_x:
        tmp += data
        y_k5[index].append(tmp/sum_k5[index])

plt.title("CDF of num of flow pass through switch, d=5, w=3, k=1, dist = 4-2") 
plt.xlabel("flow number") 
plt.ylabel("flow/num of flow") 

### k = 1
plt.plot(sorted_x_k1[0],y_k1[0],label='algo',linestyle = 'dashed')
plt.plot(sorted_x_k1[1],y_k1[1],label='baseline 1',linestyle = 'solid')
plt.plot(sorted_x_k1[2],y_k1[2],label='baseline 2',linestyle = 'dotted')
plt.plot(sorted_x_k1[3],y_k1[3],label='baseline 3',linestyle = '-.')

### k = 5
# plt.plot(sorted_x_k5[0],y_k5[0],label='algo',linestyle = 'dashed')
# plt.plot(sorted_x_k5[1],y_k5[1],label='baseline 1',linestyle = 'solid')
# plt.plot(sorted_x_k5[2],y_k5[2],label='baseline 2',linestyle = 'dotted')
# plt.plot(sorted_x_k5[3],y_k5[3],label='baseline 3',linestyle = '-.')

plt.legend()
plt.show()