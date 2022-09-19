import enum
import copy
from tkinter import W
from tracemalloc import start

from numpy import append, record
from switch_node import SwitchNode
from countminsketch import CountMinSketch
from scapy.all import *

test_time = 30
ten_times_ans = []
dst_path='dst_4_-3.txt'
dst_num = 2
file_name = '4_1_fat_tree_baseline2.txt'
f1 = open(file_name,'w')
for top_k in range(3):
    for d_w in range(4):
        ten_times_ans = []
        for ten_times in range(test_time):
            print("times = ",ten_times)
            if(top_k == 0):
                k_number = 1
            elif(top_k == 1):
                k_number = 3
            elif(top_k == 2):
                k_number = 5
            if(d_w == 0):
                d = 5
                w = 3
            elif(d_w == 1):
                d = 5
                w = 6
            elif(d_w == 2):
                d = 5
                w = 9
            elif(d_w == 3):
                d = 6
                w = 9
            sketch_t0 = CountMinSketch(w, d)
            sketch_t1 = CountMinSketch(w, d)
            sketch_t2 = CountMinSketch(w, d)
            sketch_t3 = CountMinSketch(w, d)
            sketch_t4 = CountMinSketch(w, d)
            sketch_t5 = CountMinSketch(w, d)

            sketch_a0 = CountMinSketch(w, d)
            sketch_a1 = CountMinSketch(w, d)
            sketch_a2 = CountMinSketch(w, d)
            sketch_a3 = CountMinSketch(w, d)
            sketch_a4 = CountMinSketch(w, d)
            sketch_a5 = CountMinSketch(w, d)

            sketch_c0 = CountMinSketch(w, d)
            sketch_c1 = CountMinSketch(w, d)
            sketch_c2 = CountMinSketch(w, d)

            sketch_list = [sketch_t0,sketch_t1,sketch_t2,sketch_t3,sketch_t4,sketch_t5,sketch_a0,sketch_a1,sketch_a2,sketch_a3,sketch_a4,sketch_a5,sketch_c0,sketch_c1,sketch_c2]

            num_of_switch = len(sketch_list)
            dijk_list = [[9999 for _ in range(num_of_switch)] for _ in range(num_of_switch)]
            link_list = [[0 for _ in range(num_of_switch)] for _ in range(num_of_switch)]
            for i in range(num_of_switch):
                dijk_list[i][i] = 0
            # print(dijk_list)

            dijk_list[0][6] = 1
            dijk_list[6][0] = 1     ## t0 a0
            dijk_list[0][7] = 1
            dijk_list[7][0] = 1     ## t0 a1
            dijk_list[1][6] = 1
            dijk_list[6][1] = 1     ## t1 a0
            dijk_list[1][7] = 1
            dijk_list[7][1] = 1     ## t1 a1

            dijk_list[2][8] = 1
            dijk_list[8][2] = 1     ## t2 a2
            dijk_list[2][9] = 1
            dijk_list[9][2] = 1     ## t2 a3
            dijk_list[3][8] = 1
            dijk_list[8][3] = 1     ## t3 a2
            dijk_list[3][9] = 1
            dijk_list[9][3] = 1     ## t3 a3

            dijk_list[4][10] = 1
            dijk_list[10][4] = 1     ## t4 a4
            dijk_list[4][11] = 1
            dijk_list[11][4] = 1     ## t4 a5
            dijk_list[5][10] = 1
            dijk_list[10][5] = 1     ## t5 a4
            dijk_list[5][11] = 1
            dijk_list[11][5] = 1     ## t5 a5


            dijk_list[6][12] = 1
            dijk_list[12][6] = 1     ## a0 c0
            dijk_list[6][13] = 1
            dijk_list[13][6] = 1     ## a0 c1
            dijk_list[7][14] = 1
            dijk_list[14][7] = 1     ## a1 c2


            dijk_list[8][12] = 1
            dijk_list[12][8] = 1     ## a2 c0
            dijk_list[8][13] = 1
            dijk_list[13][8] = 1     ## a2 c1
            dijk_list[9][14] = 1
            dijk_list[14][9] = 1     ## a3 c2


            dijk_list[10][12] = 1
            dijk_list[12][10] = 1     ## a4 c0
            dijk_list[10][13] = 1
            dijk_list[13][10] = 1     ## a4 c1
            dijk_list[11][14] = 1
            dijk_list[14][11] = 1     ## a5 c2

            record_original_list = {}
            recode_path_list = {}
            new_routing = {}
            have_been_record = []
            routing = {}
            store_set = {}

            
            print(sys.getsizeof(sketch_c0))

            f = open(dst_path,'r')
            for line in f:
                src = line.split(':')
                tmp = src[1].split('\n')
                routing[src[0]] = tmp[0]
                new_routing[src[0]] = -1
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
            def collision(IP):
                min = 99999
                for i in store_set[IP]:
                    tmp = num_to_sketch(i).query(IP)
                    if(tmp<min):
                        min = tmp

                return min

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

            def dijkstra(start,end,cost_list):
                n = num_of_switch
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
                        # if not visited[index] and minCost + edge < costs[index]:
                            costs[index] = minCost + edge + link_list[minNode][index]
                            # costs[index] = minCost + edge 
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
                tmp3=[]
                time = 0
                path = shortes_path(start,end,parents)
                sp.append(path)
                # print("sp",sp)
                while(time<k-1):
                    if(time<len(sp)):
                        for i in range(len(sp[time])-1):
                            dijk_list_tmp = copy.deepcopy(dijk_list)
                            for tmp in range(num_of_switch):
                                dijk_list_tmp[end][tmp] = 9999
                            for index in range(i):
                                tmp3.insert(index,sp[time][index])
                            for index2 in tmp3:
                                for tmp in range(num_of_switch):
                                    dijk_list_tmp[index2][tmp] = 9999
                            for j in sp:
                                if(sp[time][i] in j):
                                    # print("who",sp[time][i],"to",j[j.index(sp[time][i])+1])
                                    dijk_list_tmp[sp[time][i]][j[j.index(sp[time][i])+1]] += 9
                                    dijk_list_tmp[j[j.index(sp[time][i])+1]][sp[time][i]] += 9
                            cost,parents2 = dijkstra(sp[time][i],end,dijk_list_tmp)
                            # print(shortes_path(sp[time][i],end,parents2))
                            path2 = shortes_path(sp[time][i],end,parents2)
                            for index in range(i):
                                path2.insert(index,sp[time][index])
                            if((path2 not in B) and path2 not in sp):
                                B.append(path2)
                        for choose_path in B:
                            Min = 9999
                            ans = []
                            tmp = calculate_cost(choose_path)
                            if(tmp < Min):
                                ans = choose_path
                                Min = tmp
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

            def delete_the_link_cost(path):
                for index,value in enumerate(path):
                    if(value != path[-1]):
                        link_list[value][path[index+1]] -= 1
                        link_list[path[index+1]][value] -= 1

            def add_the_link_cost(path):
                for index,value in enumerate(path):
                    if(value != path[-1]):
                        link_list[value][path[index+1]] += 1
                        link_list[path[index+1]][value] += 1

            pcaps = rdpcap("u1_pt1_10sec_00000_20091218002604.pcapng")
            #k times
            all =0
            for packets in pcaps:
                try:
                    src = packets['IP'].src
                    dst = packets['IP'].dst
                    tmp = src + ' ' + dst
                    s = int(routing[src])% 6
                    end = int(routing[dst])% 6
                    if(s == end):
                        if(new_routing[dst] == -1):
                            end = (end+1)%dst_num
                            new_routing[dst] = str(end)
                        else:
                            end = int(new_routing[dst])
                    if(tmp not in have_been_record):
                        have_been_record.append(tmp)
                        record_original_list[tmp] = 1
                        path = k_shortest_path(tmp,s,end,k_number)
                        # cost,parents = dijkstra(s,end,dijk_list)
                        # path = shortes_path(s,end,parents)
                        # print("first_path",path)
                        which_sketch = find_small_ARE(tmp,path)
                        for index,value in enumerate(path):
                            if(value!=path[-1]):
                                link_list[value][path[index+1]] += 1
                                link_list[path[index+1]][value] += 1
                        num_to_sketch(which_sketch).add(tmp)
                        store_set[tmp] = [which_sketch]
                        recode_path_list[tmp] = path
                        all += 1
                    else:
                        record_original_list[tmp] += 1
                        switch = store_set[tmp][0]
                        num_to_sketch(switch).add(tmp)
                except IndexError:
                    pass

            max = 0
            max_id =''
            for i in record_original_list.keys():
                tmp = are(i)
                if(max < tmp):
                    max_id = i
                    max = tmp
            print(i)
            print(max)
            ten_times_ans.append(max)

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

            # print(dijk_list)

            all =0
            cdf = []
            for i in link_list:
                for j in i:
                    if(j>0):
                        cdf.append(j)
                        all += j

            cdf.sort()
            # print(cdf)
        # print(all)

        print("all",ten_times_ans)
        sum = 0
        for i in ten_times_ans:
            sum += i

        print("d:",d,"w:",w,"k:",k_number)
        print("4-1 base2")
        print("ans",sum/test_time)
        
        print("4-1 base2",file=f1) 
        print("d:",d,"w:",w,"k:",k_number,file=f1) 
        print("all",ten_times_ans,"\n",file=f1) 
        print("ans",sum/test_time,"\n",file=f1) 