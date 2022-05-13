import enum
from tkinter import W

from numpy import record
from switch_node import SwitchNode
from countminsketch import CountMinSketch
from scapy.all import *

switch0 = SwitchNode()
switch1 = SwitchNode()
switch2 = SwitchNode()
switch3 = SwitchNode()
switch4 = SwitchNode()
switch5 = SwitchNode()
switch6 = SwitchNode()
switch7 = SwitchNode()
switch8 = SwitchNode()
switch9 = SwitchNode()

sketch0 = CountMinSketch(3, 5)
sketch1 = CountMinSketch(3, 5)
sketch2 = CountMinSketch(3, 5)
sketch3 = CountMinSketch(3, 5)
sketch4 = CountMinSketch(3, 5)
sketch5 = CountMinSketch(3, 5)
sketch6 = CountMinSketch(3, 5)
sketch7 = CountMinSketch(3, 5)
sketch8 = CountMinSketch(3, 5)
sketch9 = CountMinSketch(3, 5)

switch_list = [switch0,switch1,switch2,switch3,switch4,switch5,switch6,switch7,switch8,switch9]
sketch_list = [sketch0,sketch1,sketch2,sketch3,sketch4,sketch5,sketch6,sketch7,sketch8,sketch9]

dijk_list = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    dijk_list[i][i] = 0
print(dijk_list)

record_original_list = {}
recode_path_list = {}
store_set = {}

for index,switch in enumerate(switch_list):
    for i in range(10):
        if(index != i):
            switch.add_link(i)


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
def find_best_sketch(IP):
    min = 99999
    which_sketch = -1
    for index,sketch in enumerate(sketch_list):
        tmp = sketch.query(IP)
        if(tmp<min):
            min = tmp
            which_sketch = index
    return which_sketch

def dijkstra(start,end,been):
    n = 10
    costs = [99999 for _ in range(n)]
    costs[start] = 0
    parents = [-1 for _ in range(n)]
    visited = [False for _ in range(n)] # 標記已確定好最短花銷的點
    print(visited)
    print('co',costs)
    print('been:',been)
    t = []  # 已經確定好最短花銷的點列表
    for i in been:
        t.append(i)
        visited[i] = True
        print(t,visited)
    while len(t) < n:
        # 從costs裡面找最短花銷(找還沒確定的點的路徑)，標記這個最短邊的頂點，把頂點加入t中
        minCost = 99999
        minNode = None
        for i in range(n):
            if not visited[i] and costs[i] < minCost:
                minCost = costs[i]
                minNode = i
        t.append(minNode)
        print(minNode)
        visited[minNode] = True

        # 從這個頂點出發，遍歷與它相鄰的頂點的邊，計算最短路徑，更新costs和parents
        for index,edge in enumerate(dijk_list[minNode]):
            if not visited[index] and minCost + edge < costs[index]:
                costs[index] = minCost + edge
                parents[index] = minNode
    return costs, parents
def shortes_path(start,end,parent):
    path = [end]
    if(start != end):
        while(parent[end]!=start):
            path.append(parent[end])
            end = parent[end]
        path.reverse()
    return path


## def algo():
# switch1.switch_table['A'] = 1
# print(switch1.switch_table)

pcaps = rdpcap("u1_pt1_10sec_00000_20091218002604.pcapng")

for packets in pcaps:
    try:
        tmp = [0]
        if(packets['IP'].src not in switch0.switch_table):
            record_original_list[packets['IP'].src] = 1
            best_are = find_best_sketch(packets['IP'].src)
            print('best',best_are)
            cost,parents = dijkstra(0,best_are,[])
            path = shortes_path(0,best_are,parents)
            print('path:',path)
            for i in path:
                if(i not in tmp):
                    tmp.append(i)
            print('tmp1',tmp)
            cost,parents = dijkstra(best_are,5,tmp)
            print('parene1',parents)
            path = shortes_path(best_are,5,parents)
            for i in path:
                tmp.append(i)
            print('tmp:',tmp)
            for index,value in enumerate(tmp):
                if(value!=5):
                    num_to_switch(value).switch_table[packets['IP'].src] = tmp[index+1]
                    dijk_list[value][tmp[index+1]] += 1
                    dijk_list[tmp[index+1]][value] += 1
            num_to_sketch(best_are).add(packets['IP'].src)
            store_set[packets['IP'].src] = [best_are]
            recode_path_list[packets['IP'].src] = tmp
        else:
            record_original_list[packets['IP'].src] += 1
            tmp2 = recode_path_list[packets['IP'].src]
            for i in tmp2:
                num_to_sketch(i).add(packets['IP'].src)
    except IndexError:
        pass

max = 0
for i in record_original_list.keys():
    tmp = ARE(i)
    if(max < tmp):
        max = tmp
print(dijkstra(0,5))
print(dijk_list)
print(store_set['41.177.117.184'])
print(max)
