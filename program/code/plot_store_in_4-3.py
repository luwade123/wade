import numpy as np 
from matplotlib import pyplot as plt 

algo_5_3_k1_x =[48, 59, 0, 0, 0, 0, 0, 0, 65, 73, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b1_5_3_k1_x = [239, 239, 0, 0, 0, 0, 0, 0, 119, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b2_5_3_k1_x =[50, 61, 0, 0, 0, 0, 0, 0, 64, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b3_5_3_k1_x =[10, 9, 10, 14, 10, 12, 10, 12, 12, 12, 12, 13, 12, 16, 12, 15, 13, 12, 9, 14]

algo_5_3_k5_x = [68, 67, 0, 0, 0, 0, 0, 0, 44, 63, 0, 0, 0, 0, 0, 0, 2, 2, 0, 1]
b1_5_3_k5_x = [239, 239, 1, 1, 1, 0, 1, 1, 124, 120, 2, 2, 1, 1, 2, 2, 3, 2, 3, 2]
b2_5_3_k5_x = [57, 51, 0, 0, 0, 0, 0, 0, 58, 69, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
b3_5_3_k5_x = [7, 8, 10, 15, 11, 12, 12, 11, 12, 16, 13, 12, 10, 9, 14, 14, 11, 14, 15, 13]


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

plt.title("CDF of num of flow store in switch, d=5, w=3, k=5, dist = 4-3") 
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