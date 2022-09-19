import numpy as np 
from matplotlib import pyplot as plt 

algo_5_3_k1_x =[9, 21, 14, 10, 17, 16, 0, 0, 21, 17, 10, 14, 14, 19, 0, 0, 15, 20, 17, 18]
b1_5_3_k1_x = [94, 76, 94, 58, 98, 58, 0, 0, 63, 78, 68, 73, 69, 77, 0, 0, 40, 49, 46, 54]
b2_5_3_k1_x =[15, 12, 10, 16, 17, 12, 0, 0, 15, 15, 16, 15, 14, 18, 0, 0, 13, 17, 17, 17]
b3_5_3_k1_x =[8, 11, 7, 15, 16, 12, 9, 11, 11, 17, 13, 11, 12, 13, 12, 10, 14, 14, 12, 11]

algo_5_3_k5_x = [15, 17, 13, 18, 14, 19, 1, 1, 15, 18, 12, 15, 14, 13, 4, 3, 20, 16, 15, 16]
b1_5_3_k5_x = [94, 76, 94, 59, 98, 58, 2, 0, 66, 75, 73, 69, 81, 65, 4, 3, 48, 52, 52, 42]
b2_5_3_k5_x = [15, 19, 16, 14, 11, 10, 1, 0, 15, 14, 12, 15, 14, 15, 2, 4, 16, 12, 17, 17]
b3_5_3_k5_x = [4, 13, 8, 12, 16, 13, 12, 9, 17, 12, 13, 12, 16, 11, 14, 11, 13, 13, 10, 10]


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

plt.title("CDF of num of flow store in switch, d=5, w=3, k=1, dist = 4-1") 
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