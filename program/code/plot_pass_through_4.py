import numpy as np 
from matplotlib import pyplot as plt 

algo_5_3_k1_x =[295, 210, 113, 231, 108, 142, 158, 167, 440, 442, 318, 322, 240, 240, 304, 308, 296, 296, 300, 298]
b1_5_3_k1_x = [295, 210, 113, 231, 108, 142, 158, 167, 442, 440, 320, 320, 240, 240, 308, 304, 300, 296, 298, 296]
b2_5_3_k1_x = [295, 210, 113, 231, 108, 142, 158, 167, 442, 440, 320, 320, 240, 240, 308, 304, 300, 296, 298, 296]
b3_5_3_k1_x =[297, 246, 197, 279, 234, 224, 206, 227, 540, 546, 488, 482, 486, 488, 464, 454, 510, 512, 508, 508]

algo_5_3_k5_x = [295, 210, 113, 231, 108, 142, 158, 167, 444, 438, 318, 322, 240, 240, 306, 306, 304, 292, 296, 298]
b1_5_3_k5_x = [295, 218, 117, 231, 112, 142, 158, 171, 446, 444, 322, 322, 240, 244, 308, 308, 298, 296, 298, 298]
b2_5_3_k5_x = [295, 210, 113, 231, 108, 142, 158, 167, 442, 440, 318, 322, 242, 238, 306, 306, 296, 296, 298, 300]
b3_5_3_k5_x = [297, 252, 203, 277, 210, 224, 244, 237, 536, 570, 488, 506, 454, 474, 492, 482, 510, 508, 520, 520]


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

plt.title("CDF of num of flow pass through switch, d=5, w=3, k=5, dist = 4") 
plt.xlabel("flow number") 
plt.ylabel("flow/num of flow") 

### k = 1
# plt.plot(sorted_x_k1[0],y_k1[0],label='algo',linestyle = 'dashed')
# plt.plot(sorted_x_k1[1],y_k1[1],label='baseline 1',linestyle = 'solid')
# plt.plot(sorted_x_k1[2],y_k1[2],label='baseline 2',linestyle = 'dotted')
# plt.plot(sorted_x_k1[3],y_k1[3],label='baseline 3',linestyle = '-.')

### k = 5
plt.plot(sorted_x_k5[0],y_k5[0],label='algo',linestyle = 'dashed')
plt.plot(sorted_x_k5[1],y_k5[1],label='baseline 1',linestyle = 'solid')
plt.plot(sorted_x_k5[2],y_k5[2],label='baseline 2',linestyle = 'dotted')
plt.plot(sorted_x_k5[3],y_k5[3],label='baseline 3',linestyle = '-.')

plt.legend()
plt.show()