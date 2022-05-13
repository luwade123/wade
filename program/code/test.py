from errno import ESTALE
from re import A
from scapy.all import *

# pcaps = rdpcap("u1_pt1_10sec_00000_20091218002604.pcapng")

# src = []
# dst = []
# flow = [] 
# tmp = ""
# dis = {}
# # path = 'src.txt'
# # f1 = open(path, 'w')
# # path2 = 'dst.txt'
# # f2 = open(path2, 'w')
# path = 'same.txt'
# f3 = open(path,'w')
# path2 = 'dis.txt'
# f4 = open(path2,'w')
# for packets in pcaps:
#     try:
#         src = packets['IP'].src
#         dst = packets['IP'].dst
#         tmp = src + ' ' + dst
#         if(tmp not in flow):
#             flow.append(tmp)
#             a = hash((src,'testabc')) % 16
#             b = hash((dst,'testbca')) % 16
#             if(a == b):
#                 dis[src] = a
#                 dis[dst] = b+1 % 16
#                 f3.write(tmp)
#                 f3.write('\n')
#             else:
#                 if(src not in dis):
#                     dis[src] = a
#                 if(dst not in dis):
#                     dis[dst] = b
#     except IndexError:
#         pass
# for i in dis.keys():
#     f4.write(i)
#     f4.write(':')
#     f4.write(str(dis[i]))
#     f4.write('\n')
# for i in dst:
#     if(i not in src):
#         src.append(i)
#         f1.write(i)
#         f1.write('\n')

routing = {}

path='dis.txt'
f = open(path,'r')
for line in f:
    src = line.split(':')
    tmp = src[1].split('\n')
    routing[src[0]] = tmp[0]

s = int(int(routing['244.3.210.230'])/2)
print(s)
# for i in routing:
#     print(i,routing[i])
    