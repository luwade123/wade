import numpy as np 
from matplotlib import pyplot as plt 

algo_5_3_k1_x =[18, 16, 16, 26, 0, 0, 0, 0, 15, 22, 21, 25, 0, 0, 0, 0, 19, 23, 21, 20]
b1_5_3_k1_x = [103, 134, 118, 123, 0, 0, 0, 0, 105, 105, 106, 106, 0, 0, 0, 0, 45, 47, 49, 42]
b2_5_3_k1_x =[20, 7, 16, 22, 0, 0, 0, 0, 17, 19, 20, 26, 0, 0, 0, 0, 20, 24, 25, 23]
b3_5_3_k1_x =[7, 9, 11, 13, 16, 13, 14, 11, 16, 11, 10, 13, 9, 14, 13, 11, 12, 9, 15, 12]

algo_5_3_k5_x = [17, 12, 20, 22, 0, 0, 0, 0, 14, 22, 22, 20, 3, 4, 2, 3, 23, 21, 19, 20]
b1_5_3_k5_x = [103, 134, 118, 123, 2, 1, 0, 0, 102, 108, 102, 110, 3, 6, 3, 3, 47, 45, 48, 55]
b2_5_3_k5_x = [17, 13, 19, 19, 0, 0, 0, 0, 13, 24, 18, 17, 4, 3, 4, 4, 26, 19, 21, 18]
b3_5_3_k5_x = [6, 8, 14, 12, 13, 12, 8, 11, 12, 14, 11, 14, 9, 11, 13, 13, 15, 14, 14, 15]


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

plt.title("CDF of num of flow store in switch, d=5, w=3, k=5, dist = 4-2") 
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
