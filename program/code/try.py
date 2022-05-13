from errno import ESTALE
from re import L
from scapy.all import *

# pcaps = rdpcap("u1_pt1_10sec_00000_20091218002604.pcapng")
# fp = open("keys.txt","a")

sum=0
flow_set = {}
test_set = {}
test_set['hey'] = list()
tmp = [1]
tmp2 = [2]
test_set['hey'].extend(tmp2) 
test_set['hey'].extend(tmp) 
for i in range(6):
    if(i not in test_set['hey']):
        print(i)
print(test_set['hey'])
# for packets in pcaps:
#     try:
#         if(packets['IP'].src in flow_set):
#             sum += 1
#             flow_set[packets['IP'].src] += 1
#         else:
#             sum += 1
#             flow_set[packets['IP'].src] = 1
#     except IndexError:
#         pass

# MAX = 0

# for i in flow_set.values():
#     if(i>MAX):
#         MAX = i
# BIG = max(flow_set,key=flow_set.get)
# small = min(flow_set,key=flow_set.get)
# print(BIG)
# print(MAX)
# print(small)
# print(flow_set[small])

# print(len(flow_set))

# print('sum:',sum)
# for i in flow_set.keys():
#     fp.write(i+'\n')