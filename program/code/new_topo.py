import enum
from tkinter import W

from numpy import record
from switch_node import SwitchNode
from countminsketch import CountMinSketch
from scapy.all import *
t0 = SwitchNode()
t1 = SwitchNode()
t2 = SwitchNode()
t3 = SwitchNode()
t4 = SwitchNode()
t5 = SwitchNode()
t6 = SwitchNode()
t7 = SwitchNode()

a0 = SwitchNode()
a1 = SwitchNode()
a2 = SwitchNode()
a3 = SwitchNode()
a4 = SwitchNode()
a5 = SwitchNode()
a6 = SwitchNode()
a7 = SwitchNode()

c0 = SwitchNode()
c1 = SwitchNode()
c2 = SwitchNode()
c3 = SwitchNode()

sketch_t0 = CountMinSketch(9, 6)
sketch_t1 = CountMinSketch(9, 6)
sketch_t2 = CountMinSketch(9, 6)
sketch_t3 = CountMinSketch(9, 6)
sketch_t4 = CountMinSketch(9, 6)
sketch_t5 = CountMinSketch(9, 6)
sketch_t6 = CountMinSketch(9, 6)
sketch_t7 = CountMinSketch(9, 6)

sketch_a0 = CountMinSketch(9, 6)
sketch_a1 = CountMinSketch(9, 6)
sketch_a2 = CountMinSketch(9, 6)
sketch_a3 = CountMinSketch(9, 6)
sketch_a4 = CountMinSketch(9, 6)
sketch_a5 = CountMinSketch(9, 6)
sketch_a6 = CountMinSketch(9, 6)
sketch_a7 = CountMinSketch(9, 6)

sketch_c0 = CountMinSketch(9, 6)
sketch_c1 = CountMinSketch(9, 6)
sketch_c2 = CountMinSketch(9, 6)
sketch_c3 = CountMinSketch(9, 6)

switch_list = [t0,t1,t2,t3,t4,t5,t6,t7,a0,a1,a2,a3,a4,a5,a6,a7,c0,c1,c2,c3]
sketch_list = [sketch_t0,sketch_t1,sketch_t2,sketch_t3,sketch_t4,sketch_t5,sketch_t6,sketch_t7,sketch_a0,sketch_a1,sketch_a2,sketch_a3,sketch_a4,sketch_a5,sketch_a6,sketch_a7,sketch_c0,sketch_c1,sketch_c2,sketch_c3]

dijk_list = [[9999 for _ in range(20)] for _ in range(20)]
link_list = [[0 for _ in range(20)] for _ in range(20)]
for i in range(20):
    dijk_list[i][i] = 0
print(dijk_list)

record_original_list = {}
recode_path_list = {}
have_been_record = []
routing = {}
for index,switch in enumerate(switch_list):
    for i in range(10):
        if(index != i):
            switch.add_link(i)

dijk_list[0][8] = 1
dijk_list[8][0] = 1     ## t0 a0
dijk_list[0][9] = 1
dijk_list[9][0] = 1     ## t0 a1
dijk_list[1][8] = 1
dijk_list[8][1] = 1     ## t1 a0
dijk_list[1][9] = 1
dijk_list[9][1] = 1     ## t1 a1

dijk_list[2][10] = 1
dijk_list[10][2] = 1     ## t2 a2
dijk_list[2][11] = 1
dijk_list[11][2] = 1     ## t2 a3
dijk_list[3][10] = 1
dijk_list[10][3] = 1     ## t3 a2
dijk_list[3][11] = 1
dijk_list[11][3] = 1     ## t3 a3

dijk_list[4][12] = 1
dijk_list[12][4] = 1     ## t4 a4
dijk_list[4][13] = 1
dijk_list[13][4] = 1     ## t4 a5
dijk_list[5][12] = 1
dijk_list[12][5] = 1     ## t5 a4
dijk_list[5][13] = 1
dijk_list[13][5] = 1     ## t5 a5

dijk_list[6][14] = 1
dijk_list[14][6] = 1     ## t6 a6
dijk_list[6][15] = 1
dijk_list[15][6] = 1     ## t6 a7
dijk_list[7][14] = 1
dijk_list[14][7] = 1     ## t7 a6
dijk_list[7][15] = 1
dijk_list[15][7] = 1     ## t7 a7

dijk_list[8][16] = 1
dijk_list[16][8] = 1     ## a0 c0
dijk_list[8][17] = 1
dijk_list[17][8] = 1     ## a0 c1
dijk_list[9][18] = 1
dijk_list[18][9] = 1     ## a1 c2
dijk_list[9][19] = 1
dijk_list[19][9] = 1     ## a1 c3

dijk_list[10][16] = 1
dijk_list[16][10] = 1     ## a2 c0
dijk_list[10][17] = 1
dijk_list[17][10] = 1     ## a2 c1
dijk_list[11][18] = 1
dijk_list[18][11] = 1     ## a3 c2
dijk_list[11][19] = 1
dijk_list[19][11] = 1     ## a3 c3

dijk_list[12][16] = 1
dijk_list[16][12] = 1     ## a4 c0
dijk_list[12][17] = 1
dijk_list[17][12] = 1     ## a4 c1
dijk_list[13][18] = 1
dijk_list[18][13] = 1     ## a5 c2
dijk_list[13][19] = 1
dijk_list[19][13] = 1     ## a5 c3

dijk_list[14][16] = 1
dijk_list[16][14] = 1     ## a6 c0
dijk_list[14][17] = 1
dijk_list[17][14] = 1     ## a6 c1
dijk_list[15][18] = 1
dijk_list[18][15] = 1     ## a7 c2
dijk_list[15][19] = 1
dijk_list[19][15] = 1     ## a7 c3

path='dis.txt'
f = open(path,'r')
for line in f:
    src = line.split(':')
    tmp = src[1].split('\n')
    routing[src[0]] = tmp[0]

def num_to_switch(number):
    for index,value in enumerate(switch_list):
        if(number == index):
            return value
def num_to_sketch(number):
    for index,value in enumerate(sketch_list):
        if(number == index):
            return value
def ARE(IP):
    min = 99999
    for i in recode_path_list[IP]:
        tmp = num_to_sketch(i).query(IP)
        if(tmp<min):
            min = tmp
    ori = record_original_list[IP]
    return (min - ori) / ori 
def dijkstra(start,end):
    n = 20
    costs = [99999 for _ in range(n)]
    costs[start] = 0
    parents = [-1 for _ in range(n)]
    visited = [False for _ in range(n)] # 標記已確定好最短花銷的點
    t = []  # 已經確定好最短花銷的點列表
    while len(t) < n:
        # 從costs裡面找最短花銷(找還沒確定的點的路徑)，標記這個最短邊的頂點，把頂點加入t中
        minCost = 99999
        minNode = None
        for i in range(n):
            if not visited[i] and costs[i] < minCost:
                minCost = costs[i]
                minNode = i
        t.append(minNode)
        visited[minNode] = True

        # 從這個頂點出發，遍歷與它相鄰的頂點的邊，計算最短路徑，更新costs和parents
        for index,edge in enumerate(dijk_list[minNode]):
            if not visited[index] and minCost + edge + link_list[minNode][index]< costs[index]:
                costs[index] = minCost + edge + link_list[minNode][index]
                parents[index] = minNode
    return costs, parents
def shortes_path(start,end,parent):
    path = [end]
    while(parent[end]!=-1):
        path.append(parent[end])
        end = parent[end]
    path.reverse()
    return path
print(dijkstra(0,5))
cost,parents = dijkstra(0,5)
print(shortes_path(0,5,parents))
## def algo():
# switch1.switch_table['A'] = 1
# print(switch1.switch_table)

pcaps = rdpcap("u1_pt1_10sec_00000_20091218002604.pcapng")

for packets in pcaps:
    try:
        src = packets['IP'].src
        dst = packets['IP'].dst
        tmp = src + ' ' + dst
        s = int(int(routing[src])/2)
        end = int(int(routing[dst])/2)
        if(tmp not in have_been_record):
            have_been_record.append(tmp)
            record_original_list[tmp] = 1
            cost,parents = dijkstra(s,end)
            path = shortes_path(s,end,parents)
            for index,value in enumerate(path):
                if(value!=end):
                    link_list[value][path[index+1]] += 1
                    link_list[path[index+1]][value] += 1
                num_to_sketch(value).add(tmp)
            recode_path_list[tmp] = path
        else:
            record_original_list[tmp] += 1
            tmp2 = recode_path_list[tmp]
            for i in tmp2:
                num_to_sketch(i).add(tmp)
    except IndexError:
        pass

max = 0
max_id =''
for i in record_original_list.keys():
    tmp = ARE(i)
    if(max < tmp):
        max_id = i
        max = tmp
print(dijkstra(0,5))
print(dijk_list)
print(link_list)
print(i)
pa = 'output.txt'
f10 = open(pa,'a')
f10.write(str(max))
f10.write('\n')
print(max)
