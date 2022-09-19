import enum
import copy
from tkinter import W

from numpy import record
from switch_node import SwitchNode
from countminsketch import CountMinSketch
from scapy.all import *


dijk_list = [[99999 for _ in range(20)] for _ in range(20)]
link_list = [[0 for _ in range(20)] for _ in range(20)]
for i in range(20):
    dijk_list[i][i] = 0


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

print(dijk_list)


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
            if not visited[index] and minCost + edge < costs[index]:
                costs[index] = minCost + edge 
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
def k_shortest_path(start,end,k):

    cost,parents = dijkstra(start,end,dijk_list)
    sp = []
    B = []

    time = 0
    path = shortes_path(start,end,parents)
    sp.append(path)
    print("sp",sp)
    while(time<k-1):
        if(time<len(sp)):
            for i in range(len(sp[time])-1):
                tmp3 = []
                dijk_list_tmp = copy.deepcopy(dijk_list)
                for tmp in range(20):
                    dijk_list_tmp[end][tmp] = 9999
                for index in range(i):
                    tmp3.insert(index,sp[time][index])
                for index2 in tmp3:
                    for tmp in range(20):
                        dijk_list_tmp[index2][tmp] = 9999
                for j in sp:
                    if(sp[time][i] in j):
                        print("who",sp[time][i],"to",j[j.index(sp[time][i])+1])
                        print("before",dijk_list_tmp[sp[time][i]][j[j.index(sp[time][i])+1]])
                        dijk_list_tmp[sp[time][i]][j[j.index(sp[time][i])+1]] += 5
                        dijk_list_tmp[j[j.index(sp[time][i])+1]][sp[time][i]] += 5
                        print("after",dijk_list_tmp[sp[time][i]][j[j.index(sp[time][i])+1]])
                cost,parents2 = dijkstra(sp[time][i],end,dijk_list_tmp)
                print(shortes_path(sp[time][i],end,parents2))
                path2 = shortes_path(sp[time][i],end,parents2)
                for index in range(i):
                    path2.insert(index,sp[time][index])
                if((path2 not in B) and path2 not in sp):
                    B.append(path2)
                print(B)
            for choose_path in B:
                Max = 0
                ans = []
                tmp = calculate_cost(choose_path)
                if(tmp > Max):
                    ans = choose_path
                    Max = tmp
            if(ans in B):
                B.remove(ans)
                print("ans",ans)
                if(ans not in sp):
                    sp.append(ans)
            time += 1
        else:
            break
    print(sp)
    return sp


print(k_shortest_path(0,0,8))
