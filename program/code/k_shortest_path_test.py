import enum
import copy
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

sketch_t0 = CountMinSketch(3, 5)
sketch_t1 = CountMinSketch(3, 5)
sketch_t2 = CountMinSketch(3, 5)
sketch_t3 = CountMinSketch(3, 5)
sketch_t4 = CountMinSketch(3, 5)
sketch_t5 = CountMinSketch(3, 5)
sketch_t6 = CountMinSketch(3, 5)
sketch_t7 = CountMinSketch(3, 5)

sketch_a0 = CountMinSketch(3, 5)
sketch_a1 = CountMinSketch(3, 5)
sketch_a2 = CountMinSketch(3, 5)
sketch_a3 = CountMinSketch(3, 5)
sketch_a4 = CountMinSketch(3, 5)
sketch_a5 = CountMinSketch(3, 5)
sketch_a6 = CountMinSketch(3, 5)
sketch_a7 = CountMinSketch(3, 5)

sketch_c0 = CountMinSketch(3, 5)
sketch_c1 = CountMinSketch(3, 5)
sketch_c2 = CountMinSketch(3, 5)
sketch_c3 = CountMinSketch(3, 5)



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
store_set = {}
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
print(sys.getsizeof(sketch_a0))
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
def are(IP):
    min = 99999
    for i in store_set[IP]:
        tmp = num_to_sketch(i).query(IP)
        if(tmp<min):
            min = tmp
    ori = record_original_list[IP]
    return (min - ori) / ori 

def are_with_path(IP,path):
    min = 99999
    for i in path:
        tmp = num_to_sketch(i).query(IP)
        if(tmp<min):
            min = tmp
    return min

def find_small_ARE(IP,path):
    min = 99999
    which_switch = -1
    for i in path:
        tmp = num_to_sketch(i).query(IP)
        if(min>tmp):
            min = tmp
            which_switch = i
    return which_switch
def Algo():
    MAX = 0             ## MAX of ARE of all flow.
    MIN = 100000        ## MIN of the ARE for one flow to decide store in which switch. 
    which_flow = ''
    flow_num = -1
    which_switch = -1
    for value in record_original_list.keys():
        if(MAX<are(value)):
            MAX = are(value)
            which_flow = value

    if(which_flow != ''):
        print('The worst flow is',which_flow,'Its ARE is',MAX,"total =",record_original_list[which_flow])
        for index,sketch in enumerate(sketch_list):
            if(index in recode_path_list[which_flow]):
                if(index not in store_set[which_flow]):
                    tmp = sketch.query(which_flow)
                    if(MIN>tmp):
                        which_switch = index
                        MIN = tmp
        if(which_switch !=-1):
            if(MIN != MAX):      
                print('Put',which_flow,'into the switch',(which_switch))
                num_to_sketch(which_switch).add(which_flow)
                tmp_list = [which_switch]
                store_set[which_flow].extend(tmp_list)
                Algo()
            else:
                print('Can not be better.')
        else:
            print('Can not find more switch')
    else:
        print('Everyone is best.')

def dijkstra(start,end,cost_list):
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
        for index,edge in enumerate(cost_list[minNode]):
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
def calculate_cost(path):
    cost = 0
    for index in range(len(path)-1):
        cost += dijk_list[path[index]][path[index+1]]
    return cost
def k_shortest_path(ID,start,end,k):

    cost,parents = dijkstra(start,end,dijk_list)
    sp = []
    ans = []
    B = []
    time = 0
    path = shortes_path(start,end,parents)
    sp.append(path)
    while(time<k-1):
        if(time<len(sp)):
            for i in range(len(sp[time])-1):
                dijk_list_tmp = copy.deepcopy(dijk_list)
                for j in sp:
                    if(sp[time][i] in j):
                        dijk_list_tmp[sp[time][i]][j[j.index(sp[time][i])+1]] = 9999
                        dijk_list_tmp[j[j.index(sp[time][i])+1]][sp[time][i]]= 9999
                cost,parents = dijkstra(start,end,dijk_list_tmp)
                if(shortes_path(start,end,parents) not in B and shortes_path(start,end,parents) not in sp):
                    B.append(shortes_path(start,end,parents))
            for choose_path in B:
                Max = 0
                ans = []
                tmp = calculate_cost(choose_path)
                if(tmp > Max):
                    ans = choose_path
                    Max = tmp
            if(ans in B):
                B.remove(ans)
                if(ans not in sp):
                    sp.append(ans)
            time += 1
        else:
            break
    Min = 99999
    best_path = []
    for i in sp:
        tmp = are_with_path(ID,i)
        if(tmp < Min):
            Min = tmp
            best_path = i
    return best_path    
## def algo():
# switch1.switch_table['A'] = 1
# print(switch1.switch_table)

pcaps = rdpcap("u1_pt1_10sec_00000_20091218002604.pcapng")
k = 5 #k times
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
            path = k_shortest_path(tmp,s,end,k)
            which_sketch = find_small_ARE(tmp,path)
            for index,value in enumerate(path):
                if(value!=end):
                    link_list[value][path[index+1]] += 1
                    link_list[path[index+1]][value] += 1
            num_to_sketch(which_sketch).add(tmp)
            store_set[tmp] = [which_sketch]
            recode_path_list[tmp] = path
        else:
            record_original_list[tmp] += 1
            tmp2 = recode_path_list[tmp]
            i = store_set[tmp][0]
            num_to_sketch(i).add(tmp)
    except IndexError:
        pass

max = 0
max_id =''
for i in record_original_list.keys():
    tmp = are(i)
    if(max < tmp):
        max_id = i
        max = tmp
print(dijk_list)
print(link_list)
print(i)
print(max)

Algo()

total_are = 0
total_flow = 0

for i in record_original_list.keys():
    tmp = are(i)
    total_are += tmp
    total_flow += 1
    if(max < tmp):
        max_id = i
        max = tmp
print("ave :",total_are/total_flow)

print(dijk_list)