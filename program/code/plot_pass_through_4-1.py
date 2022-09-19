import numpy as np 
from matplotlib import markers, pyplot as plt 

algo_5_3_k1_x =[227, 238, 241, 200, 324, 194, 0, 0, 412, 406, 398, 398, 466, 464, 0, 0, 280, 282, 278, 280]
b1_5_3_k1_x = [227, 238, 241, 200, 324, 194, 0, 0, 410, 408, 398, 398, 464, 466, 0, 0, 280, 280, 280, 280]
b2_5_3_k1_x = [227, 238, 241, 200, 324, 194, 0, 0, 410, 408, 398, 398, 464, 466, 0, 0, 280, 280, 280, 280]
b3_5_3_k1_x =[257, 294, 285, 262, 374, 262, 130, 132, 572, 560, 568, 556, 620, 600, 304, 314, 526, 524, 524, 524]

algo_5_3_k5_x = [227, 238, 241, 200, 324, 194, 4, 2, 406, 412, 400, 394, 464, 466, 12, 14, 292, 284, 280, 284]
b1_5_3_k5_x = [227, 238, 241, 202, 324, 194, 4, 4, 402, 416, 398, 400, 460, 470, 16, 16, 292, 274, 292, 286]
b2_5_3_k5_x = [227, 238, 241, 200, 324, 194, 2, 2, 410, 408, 398, 398, 464, 466, 12, 12, 284, 286, 286, 284]
b3_5_3_k5_x =  [249, 268, 307, 254, 374, 272, 138, 140, 520, 522, 562, 566, 616, 620, 330, 340, 514, 516, 522, 522]


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

plt.title("CDF of num of flow pass through switch, d=5, w=3, k=5, dist = 4-1") 
plt.xlabel("flow number") 
plt.ylabel("flow/num of flow") 

# ### k = 1
# plt.plot(sorted_x_k1[0],y_k1[0],label='algo',linestyle = 'dashed')
# plt.plot(sorted_x_k1[1],y_k1[1],label='baseline 1',linestyle = 'solid')
# plt.plot(sorted_x_k1[2],y_k1[2],label='baseline 2',linestyle = 'dotted')
# plt.plot(sorted_x_k1[3],y_k1[3],label='baseline 3',linestyle = '-.')

### k = 5
plt.plot(sorted_x_k5[0],y_k5[0],label='algo',color= 'black',linestyle = 'dashed',marker = 's')
plt.plot(sorted_x_k5[1],y_k5[1],label='baseline 1',linestyle = 'solid',marker = '^')
plt.plot(sorted_x_k5[2],y_k5[2],label='baseline 2',linestyle = 'dotted',marker = 'v')
plt.plot(sorted_x_k5[3],y_k5[3],label='baseline 3',linestyle = '-.',marker = 'o')

plt.legend()
plt.show()