from cProfile import label
import numpy as np 
from matplotlib import pyplot as plt 
 
x = ['5/3','5/6','5/9','6/9']
top_k_x = ['1','3','5']
k1_y1 = [13.255,4.6421,1.9297,1.4222]           #k = 4
k1_y2 = [18.4326,7.2773,3.0086,2.6523]          #k = 4 -1
k1_y3 = [30.491,12.4594,5.6894,5.224]           #k = 4 -2
k1_y4 = [3.2592,0.7627,0.3195,0.2064]           #k = 6

k5_y1 = [12.3442,4.1312,1.4352,1.4609]          #k = 4
k5_y2 = [19.5973,6.7492,2.55145,2.3689]         #k = 4 -1
k5_y3 = [32.1634,12.2651,5.4217,4.9767]         #k = 4 -2
k5_y4 = [3.0608,0.6244,0.252,0.1404]            #k = 6

Fk_4_53_base1_y = [1520,1479.003,1524.933]      #k-path = 1,3,5
Fk_4_56_base1_y = [629.467,668.333,628.9]
Fk_4_59_base1_y = [347.267,338.267,358.2]
Fk_4_69_base1_y = [339.067,310.567,300.967]

Fk_4_53_base2_y =[389.605,470.933,355.35]
Fk_4_56_base2_y =[189.158,162.3,229.278]
Fk_4_59_base2_y =[82.206,72.661,81.233]
Fk_4_69_base2_y =[58.917,60.633,68.833]

Fk_4_53_base3_y =[426.843,419.455,400.522]
Fk_4_56_base3_y =[204.708,217.783,193.1]
Fk_4_59_base3_y =[74.267,73.9,81.483]
Fk_4_69_base3_y =[60.767,67.722,71.631]

Fk_4_53_algo_y = [13.255,11.426,11.1683]
Fk_4_56_algo_y = [4.642,4.108,4.1312]
Fk_4_59_algo_y = [1.93,1.585,1.4352]
Fk_4_69_algo_y = [1.42,1.3804,1.4609]

Fk_4_1_53_algo_y = [18.4326,19.4256,19.5973]
Fk_4_1_56_algo_y = [7.277,6.5035,6.7492]
Fk_4_1_59_algo_y = [3.009,2.8921,2.5515]
Fk_4_1_69_algo_y = [2.6523,2.657,2.369]

Fk_4_1_53_base1_y = [2345.933,2379.6,2327.9]
Fk_4_1_56_base1_y = [1075.967,1190.183,1082.5]
Fk_4_1_59_base1_y = [613.833,601.5,614.1]
Fk_4_1_69_base1_y = [568.833,586.933,570.367]

Fk_4_1_53_base2_y = [899.467,610.367,625.623]
Fk_4_1_56_base2_y = [280.607,255.867,249.537]
Fk_4_1_59_base2_y = [137.467,119.833,145.111]
Fk_4_1_69_base2_y = [120.367,110.067,99.783]

Fk_4_1_53_base3_y = [574.371,500.8,670.696]
Fk_4_1_56_base3_y = [354.855,342.658,239.906]
Fk_4_1_59_base3_y = [104.75,123.167,103.267]
Fk_4_1_69_base3_y = [95.55,96.633,95.667]

Fk_4_2_53_algo_y = [30.491,32.1182,32.1634]
Fk_4_2_56_algo_y = [12.4594,12.2144,12.2651]
Fk_4_2_59_algo_y = [5.6894,5.7322,5.4217]
Fk_4_2_69_algo_y = [5.224,4.9378,4.9767]

Fk_4_2_53_base1_y = [2101.3,2054.1,2171]
Fk_4_2_56_base1_y = [1069.567,1005.2,1036.9]
Fk_4_2_59_base1_y = [575.4,603.767,600]
Fk_4_2_69_base1_y = [544.767,542.067,553.833]

Fk_4_2_53_base2_y = [995.567,1140.394,954.108]
Fk_4_2_56_base2_y = [695.407,727.9,457.538]
Fk_4_2_59_base2_y = [265.033,259.267,266.633]
Fk_4_2_69_base2_y = [219.133,214.367,215.167]

Fk_4_2_53_base3_y = [704.183,775.808,772.583]
Fk_4_2_56_base3_y = [470.083,434.05,491.342]
Fk_4_2_59_base3_y = [180.567,182.9,167.267]
Fk_4_2_69_base3_y = [169.9,149.569,158.6]

Fk_6_53_algo_y = [3.2592,2.977,3.06]
Fk_6_56_algo_y = [0.7627,0.834,0.6244]
Fk_6_59_algo_y = [0.3195,0.2218,0.252]
Fk_6_69_algo_y = [0.2064,0.17,0.1404]

Fk_6_53_base1_y = [487.367,471.5,516]
Fk_6_56_base1_y = [198.367,174.667,182.533]
Fk_6_59_base1_y = [85.75,79.967,79.733]
Fk_6_69_base1_y = [81.15,77.3,70.433]

Fk_6_53_base2_y = [158.47,179.117,221.656]
Fk_6_56_base2_y = [131.572,84.433,66.994]
Fk_6_59_base2_y = [32.301,30.233,26.478]
Fk_6_69_base2_y = [23.469,27.808,23.527]

Fk_6_53_base3_y = [297.274,377.941,237.371]
Fk_6_56_base3_y = [74.412,65.694,84.034]
Fk_6_59_base3_y = [33.647,40.887,36.775]
Fk_6_69_base3_y = [31.87,30.786,31.646]


y5 = [10.5156,3.2986,1.2536,0.9971]
plt.title("Bsaeline1 Performance with sketch d = 5, w = 3 ") 
plt.xlabel("Top k-path") 
plt.ylabel("Worst ARE") 

## algo 5/3
# plt.plot(top_k_x,Fk_6_53_algo_y,label='Fat tree k = 6')
# plt.plot(top_k_x,Fk_4_53_algo_y,label='Fat tree k = 4')
# plt.plot(top_k_x,Fk_4_1_53_algo_y,label='Fat tree k = 4 with one pop disabled')
# plt.plot(top_k_x,Fk_4_2_53_algo_y,label='Fat tree k = 4 with two pod disabled')

## base 1 5/3
# plt.plot(top_k_x,Fk_6_53_base1_y,label='Fat tree k = 6')
# plt.plot(top_k_x,Fk_4_53_base1_y,label='Fat tree k = 4')
# plt.plot(top_k_x,Fk_4_1_53_base1_y,label='Fat tree k = 4 with one pop disabled')
# plt.plot(top_k_x,Fk_4_2_53_base1_y,label='Fat tree k = 4 with two pod disabled')

## base 2 5/3
plt.plot(top_k_x,Fk_6_53_base2_y,label='Fat tree k = 6')
plt.plot(top_k_x,Fk_4_53_base2_y,label='Fat tree k = 4')
plt.plot(top_k_x,Fk_4_1_53_base2_y,label='Fat tree k = 4 with one pop disabled')
plt.plot(top_k_x,Fk_4_2_53_base2_y,label='Fat tree k = 4 with two pod disabled')



# plt.plot(x,k5_y1,label='k = 5') 
# plt.plot(x,k1_y1,label='k = 1') 


# plt.plot(x,y1,label='CM-sketch') 
# plt.plot(x,y2,label='better sketch') 

# plt.plot(x,k5_y3,label='Fat-tree with k = 4 (2 pop disable)') 
# plt.plot(x,k5_y2,label='Fat-tree with k = 4 (1 pop disable)') 
# plt.plot(x,k5_y1,label='Fat-tree with k = 4') 
# plt.plot(x,k5_y4,label='Fat-tree with k = 6') 

plt.legend()
plt.show()