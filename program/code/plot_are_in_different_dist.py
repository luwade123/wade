from cProfile import label
import numpy as np 
from matplotlib import pyplot as plt 
 
x = ['4-3','4-2','4-1','4']



topo_4_algo = [95.16666666666667 ,25.625,14.583333333333334,10.833333333333334]
topo_4_baseline1 =[3768.0,2279.0 ,2046.0 ,1980.0  ]
topo_4_baseline2 =[1608.0,562.0 ,432.0 ,408.0  ]
topo_4_baseline3 = [331.0,328.0 ,332.0 ,264.0 ]
plt.title("WRE Performance with different traffic ") 
plt.xlabel("Traffic") 
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
plt.plot(x,topo_4_baseline1,marker='v',linestyle = '-.',label='CM Sketch')
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