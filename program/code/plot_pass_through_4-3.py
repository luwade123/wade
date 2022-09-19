import numpy as np 
from matplotlib import pyplot as plt 

algo_5_3_k1_x =[712, 712, 0, 0, 0, 0, 0, 0, 714, 710, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b1_5_3_k1_x = [712, 712, 0, 0, 0, 0, 0, 0, 712, 712, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b2_5_3_k1_x = [712, 712, 0, 0, 0, 0, 0, 0, 712, 712, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b3_5_3_k1_x =[712, 712, 200, 198, 232, 224, 190, 188, 1326, 1330, 398, 398, 456, 456, 378, 378, 616, 616, 616, 616]

algo_5_3_k5_x = [712, 712, 2, 2, 2, 2, 2, 2, 722, 714, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6]
b1_5_3_k5_x = [712, 712, 2, 2, 2, 2, 2, 2, 714, 722, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6]
b2_5_3_k5_x = [712, 712, 2, 2, 2, 2, 2, 2, 718, 718, 4, 4, 4, 4, 4, 4, 6, 6, 6, 6]
b3_5_3_k5_x =  [712, 712, 212, 210, 202, 200, 208, 202, 1328, 1330, 422, 424, 402, 402, 410, 410, 618, 616, 620, 616]


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

plt.title("CDF of num of flow pass through switch, d=5, w=3, k=1, dist = 4-3") 
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