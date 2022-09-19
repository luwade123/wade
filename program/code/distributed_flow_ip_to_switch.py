from errno import ESTALE
from re import A
from scapy.all import *

pcaps = rdpcap("u1_pt1_10sec_00000_20091218002604.pcapng")

src = []
dst = []
flow = [] 
tmp = ""
dis = {}
# path = 'src.txt'
# f1 = open(path, 'r')
# path2 = 'dst_4_-3.txt'
# f2 = open(path2, 'w')
# path = 'same.txt'
# f3 = open(path,'r')
# dict = {}
# path2 = 'dist2(more_skwe).txt'
# f4 = open(path2,'r')
# for line in f4:
#     tmp = line.partition(":")
#     if(tmp[2] not in dict.keys()):
#         dict[tmp[2]] = 1
#     else:
#         dict[tmp[2]] += 1
# all = 0
# for i in dict.keys():
#     all += dict[i] 
#     print(i,":",dict[i])

# print("all",all)
for packets in pcaps:
    try:
        src = packets['IP'].src
        dst = packets['IP'].dst
        tmp = src + ' ' + dst
        if(tmp not in flow):
            flow.append(tmp)
            a = hash((src,'testabc')) % 2
            b = hash((dst,'testbca')) % 2
            if(a == b):
                dis[src] = a
                dis[dst] = (b+1) % 2
                # f4.write(tmp)
                # f4.write('\n')
            else:
                if(src not in dis):
                    dis[src] = a
                if(dst not in dis):
                    dis[dst] = b
    except IndexError:
        pass
# for i in dis.keys():
#     f2.write(i)
#     f2.write(':')
#     f2.write(str(dis[i]))
#     f2.write('\n')
# for i in dst:
#     if(i not in src):
#         src.append(i)
#         f1.write(i)
#         f1.write('\n')

# routing = {}

# path='dis.txt'
# f = open(path,'r')
# for line in f:
#     src = line.split(':')
#     tmp = src[1].split('\n')
#     routing[src[0]] = tmp[0]

# s = int(int(routing['244.3.210.230'])/2)

# for i in routing:
#     print(i,routing[i])
    
print(len(flow))