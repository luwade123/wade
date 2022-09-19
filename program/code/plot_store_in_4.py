import numpy as np 
from matplotlib import pyplot as plt 

algo_5_3_k1_x =[10, 13, 7, 11, 12, 13, 15, 15, 12, 11, 10, 12, 12, 12, 18, 14, 14, 12, 14, 15]
b1_5_3_k1_x = [88, 72, 26, 69, 31, 61, 65, 66, 70, 73, 49, 45, 45, 41, 59, 62, 57, 46, 51, 51] 
b2_5_3_k1_x =[9, 14, 7, 9, 12, 14, 13, 11, 14, 11, 11, 11, 10, 14, 14, 16, 13, 11, 13, 12]
b3_5_3_k1_x =[6, 10, 9, 13, 12, 14, 9, 11, 14, 10, 12, 11, 13, 14, 17, 13, 13, 12, 12, 14]

algo_5_3_k5_x = [12, 12, 10, 14, 11, 13, 13, 15, 12, 13, 11, 12, 16, 11, 15, 16, 12, 14, 14, 10]
b1_5_3_k5_x = [88, 73, 27, 69, 32, 61, 65, 67, 66, 78, 47, 48, 43, 44, 63, 59, 43, 55, 55, 52]
b2_5_3_k5_x = [13, 12, 8, 8, 8, 6, 14, 13, 12, 12, 11, 9, 11, 18, 14, 17, 16, 12, 14, 11]
b3_5_3_k5_x =  [6, 10, 10, 14, 12, 14, 10, 10, 13, 13, 15, 13, 12, 13, 18, 10, 11, 13, 10, 12]


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

plt.title("CDF of num of flow store in switch, d=5, w=3, k=5, dist = 4") 
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