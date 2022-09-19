from cProfile import label
import numpy as np 
from matplotlib import pyplot as plt 
 
x = ['5/3','5/6','5/9','6/9']
top_k_x = ['1','3','5']

topo_4_algo_dist_4_1 = [14.583333333333334,6.833333333333333 ,1.8461538461538463,1.7272727272727273]
topo_4_algo_dist_4_2 = [25.625,8.181818181818182,3.3636363636363638,4.333333333333333]
topo_4_algo_dist_4_3 = [95.16666666666667,48.666666666666664,23.272727272727273,21.75]
topo_4_algo_dist_4 = [10.833333333333334,4.133333333333334,1.75,1.4166666666666667]

topo_4_baseline1_dist_4_1 = [1546.0,708.0,422.0,323.0]
topo_4_baseline1_dist_4_2 = [2279.0,890.0,723.0,644.0]
topo_4_baseline1_dist_4_3 = [3768.0,2852.0 ,909.0,911.0 ]
topo_4_baseline1_dist_4 = [1980.0,622.0,286.0,337.0 ]

topo_4_algo = [11.382251082251083,3.7382326007326014,1.4765068265068264,1.3255099067599065 ]
topo_4_baseline1 =[1446.75 ,713.0357142857143 ,335.75 ,310.42857142857144 ]
topo_4_baseline2 =[378.04464285714283 ,179.07142857142858 ,86.89285714285714 ,58.92857142857143 ]
topo_4_baseline3 = [370.20119047619045 ,185.81547619047618 ,76.32142857142857 ,54.795918367346935 ]
plt.title("ARE Performance with different memory usage ") 
plt.xlabel("memory usage") 
plt.ylabel("WRE") 

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
plt.plot(x,topo_4_algo,marker='x',linestyle = '--',label='Multi-Switch Sketch')
# plt.plot(x,topo_4_baseline1,marker='v',linestyle = '-.',label='CM Sketch')
plt.plot(x,topo_4_baseline2,marker='>',linestyle = ':',label='Shortest',color = 'green')
plt.plot(x,topo_4_baseline3,marker='<',linestyle = '-',label='All',color = 'red')


# plt.plot(x,k5_y1,label='k = 5') 
# plt.plot(x,k1_y1,label='k = 1') 


# plt.plot(x,y1,label='CM-sketch') 
# plt.plot(x,y2,label='better sketch') 

# plt.plot(x,k5_y3,label='Fat-tree with k = 4 (2 pop disable)') 
# plt.plot(x,k5_y2,label='Fat-tree with k = 4 (1 pop disable)') 
# plt.plot(x,k5_y1,label='Fat-tree with k = 4') 
# plt.plot(x,k5_y4,label='Fat-tree with k = 6') 

for pos in ['right', 'top']:
    plt.gca().spines[pos].set_visible(False)
plt.legend(frameon=False)
plt.show()