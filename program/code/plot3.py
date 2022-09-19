from cProfile import label
import numpy as np 
from matplotlib import pyplot as plt 
 
x = ['4-3','4-2','4-1','4','6']

plt.title("sketch d = 5,w = 3, Performance with different topology ") 
plt.xlabel("Fat-Tree k") 
plt.ylabel("WRE") 
algo_k_1=[102.6723485,31.85795455,20.15120594,11.90444139,3.323845528]
algo_k_3=[100.2860334,30.96205877,18.75069573,11.66720779,3.075625823]
algo_k_5=[101.1909722,30.98341554,18.52175325,11.38225108,2.935007022]
base1_k_1=[4196.5,2403.708333,2107,2090.791667,497]
base1_k_3=[3772.958333,2391.75,1917.571429,1911.416667,466.3571429]
base1_k_5=[3752.416667,2379.291667,1903.107143,1891.5,545]
base2_k_1=[1687.8125,745,742.1466837,362.952381,142.7857143]
base2_k_3=[1688.270833,659.7277778,719.6666667,359.7767857,177.0714286]
base2_k_5=[1812.541667,753.2569444,688.2857143,378.0446429,159]
base3_k_1=[1414.1875,700.3666667,621.2306548,523.1857639,181.2297619]
base3_k_3=[1523.729167,688.3611111,461.0714286,456.7916667,178.8761447]
base3_k_5=[1458.333333,767.2986111,456.8125,434.3229167,249.8133117]



# plt.plot(x,algo_k_1,marker='*',linestyle = ':',label='a1')
# plt.plot(x,algo_k_3,marker='o',linestyle = '-',label='a3')
plt.plot(x,algo_k_5,marker='x',linestyle = '--',label='Multi-Switch Sketch')
# plt.plot(x,base1_k_1,marker='v',linestyle = '-.',label='b1_1')
# plt.plot(x,base1_k__3,label='b1_3')
plt.plot(x,base1_k_5,marker='v',linestyle = '-.',label='CM sketch')
# plt.plot(x,base2_k_1,marker='>',linestyle = ':',label='b2_1')
# plt.plot(x,base2_k_3,label='b2_3')
plt.plot(x,base2_k_5,marker='>',linestyle = ':',label='Shortest')
# plt.plot(x,base3_k_1,marker='<',linestyle = '-',label='b3_1')
# plt.plot(x,base3_k_3,label='b3_3')
plt.plot(x,base3_k_5,marker='<',linestyle = '-',label='All')
for pos in ['right', 'top']:
    plt.gca().spines[pos].set_visible(False)
# y = [0,1,2,3,50,700,2500]
# plt.yticks(y)
plt.legend(frameon=False)
plt.show()