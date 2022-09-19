import enum
import copy
from tkinter import W
from tracemalloc import start

from numpy import append, record
from switch_node import SwitchNode
from countminsketch import CountMinSketch
from scapy.all import *
from scipy import stats
test_time = 1
ten_times_ans = []
dst_path='dst_4_-1.txt'
dst_num = 6
file_name = '4_fat_tree_baseline3_with_all_situation_dst=4-1.txt'
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
            sketch_t0 = CountMinSketch(w, d)
            sketch_t1 = CountMinSketch(w, d)
            sketch_t2 = CountMinSketch(w, d)
            sketch_t3 = CountMinSketch(w, d)
            sketch_t4 = CountMinSketch(w, d)
            sketch_t5 = CountMinSketch(w, d)
            sketch_t6 = CountMinSketch(w, d)
            sketch_t7 = CountMinSketch(w, d)

            sketch_a0 = CountMinSketch(w, d)
            sketch_a1 = CountMinSketch(w, d)
            sketch_a2 = CountMinSketch(w, d)
            sketch_a3 = CountMinSketch(w, d)
            sketch_a4 = CountMinSketch(w, d)
            sketch_a5 = CountMinSketch(w, d)
            sketch_a6 = CountMinSketch(w, d)
            sketch_a7 = CountMinSketch(w, d)

            sketch_c0 = CountMinSketch(w, d)
            sketch_c1 = CountMinSketch(w, d)
            sketch_c2 = CountMinSketch(w, d)
            sketch_c3 = CountMinSketch(w, d)


            switch_list = [t0,t1,t2,t3,t4,t5,t6,t7,a0,a1,a2,a3,a4,a5,a6,a7,c0,c1,c2,c3]
            sketch_list = [sketch_t0,sketch_t1,sketch_t2,sketch_t3,sketch_t4,sketch_t5,sketch_t6,sketch_t7,sketch_a0,sketch_a1,sketch_a2,sketch_a3,sketch_a4,sketch_a5,sketch_a6,sketch_a7,sketch_c0,sketch_c1,sketch_c2,sketch_c3]

            num_of_switch = len(sketch_list)
            dijk_list = [[9999 for _ in range(num_of_switch)] for _ in range(num_of_switch)]
            link_list = [[0 for _ in range(num_of_switch)] for _ in range(num_of_switch)]
            for i in range(num_of_switch):
                dijk_list[i][i] = 0
            # print(dijk_list)

            record_original_list = {}
            recode_path_list = {}
            have_been_record = []
            routing = {}
            new_routing = {}
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

            f = open(dst_path,'r')
            for line in f:
                src = line.split(':')
                tmp = src[1].split('\n')
                routing[src[0]] = tmp[0]
                new_routing[src[0]] = -1

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
            def find_small_ARE_in_all_switch(IP):
                min = 99999
                which_switch = -1
                for index in range(len(sketch_list)):
                    tmp = num_to_sketch(index).query(IP)
                    if(min>tmp):
                        min = tmp
                        which_switch = index
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
            def k_shortest_path_return_list(start,end,k):
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
                            Max = 0
                            ans = []
                            tmp = calculate_cost(choose_path)
                            if(tmp > Max):
                                ans = choose_path
                                Max = tmp
                        # print("B",B)
                        if(ans in B):
                            B.remove(ans)
                            if(ans not in sp):
                                sp.append(ans)
                        time += 1
                    else:
                        break
                return sp  
            def k_shortest_path_with_limit(ID,start,end,k,infront_path):
                dijk_list_tmp = copy.deepcopy(dijk_list)
                for sw in infront_path:
                    for i in range(num_of_switch):
                        if(i != sw):
                            dijk_list_tmp[i][sw] = 9999

                cost,parents = dijkstra(start,end,dijk_list_tmp)
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
                                for sw in infront_path:
                                    dijk_list_tmp[sw][tmp] = 10020
                                    dijk_list_tmp[tmp][sw] = 10020
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

            def find_switch(ID):
                start = recode_path_list[ID][0]
                end = recode_path_list[ID][-1]
                old_path = copy.deepcopy(store_set[ID])
                oringin = len(old_path)
                start_point_in = 0
                print("store set",old_path)
                if(start not in old_path):
                    old_path.insert(0,start)
                else:
                    start_point_in += 1
                if(end not in old_path):
                    old_path.append(end)
                print("plus start and end",old_path)
                k_path = []
                for i in range(len(old_path)-1):
                    tmp = k_shortest_path_return_list(old_path[i],old_path[i+1],k_number)
                    k_path.append(tmp)
                which_path = -1
                min_are = collision(ID) - record_original_list[ID]
                min_switch = -1
                sketch_set = []
                all_path = []
                # print("k_path",k_path)
                for index,list in enumerate(k_path):
                    for path in list:
                        # print("path",path)
                        if(len(sketch_set)+oringin < num_of_switch):
                            for switch in path:
                                if(switch not in store_set[ID]):
                                    if(switch not in sketch_set):
                                        sketch_set.append(switch)
                                        # print("switch",switch)
                                        tmp_are = num_to_sketch(switch).query(ID)
                                        if(tmp_are< min_are):
                                            min_are = tmp_are
                                            min_switch = switch
                                            which_path = index
                                            all_path = path
                        else:
                            break
                which_path += start_point_in
                if(len(sketch_set)+oringin < num_of_switch):
                    print("sketch set:",sketch_set)
                # for index in range(20):
                #     if(index not in sketch_set):
                #         if(min_are>num_to_sketch(index).query(ID)):
                #             print("MIN = ",min_are )
                #             print(index,"can do",num_to_sketch(index).query(ID))
                return which_path,min_switch,all_path

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
                    s = int(routing[src]) % 8
                    end = int(routing[dst]) % 8
                    if(s == end):
                        if(new_routing[dst] == -1):
                            end = (end+1)%dst_num
                            new_routing[dst] = str(end)
                        else:
                            end = int(new_routing[dst])
                    if(tmp not in have_been_record):
                        have_been_record.append(tmp)
                        record_original_list[tmp] = 1
                        # path = k_shortest_path(tmp,s,end,k_number)
                        which_sketch = find_small_ARE_in_all_switch(tmp)
                        if(which_sketch != s and which_sketch !=end):
                            path1 = k_shortest_path(tmp,s,which_sketch,k_number)
                            path2 = k_shortest_path_with_limit(tmp,which_sketch,end,k_number,path1)
                            print("1  :",path1,"2   :",path2)
                            path = path1
                            for i in range(1,len(path2)):
                                path.append(path2[i])
                        elif(which_sketch == s or which_sketch == end):
                            path = k_shortest_path(tmp,s,end,k_number) 
                        print("which switch",which_sketch)
                        print("path",path)
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
                # print(store_set[i])
            # print(dijk_list)
            # print(link_list)
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
            print(cdf)
            print(all)

        print("all ans",ten_times_ans)
        sum = 0
        for i in ten_times_ans:
            sum += i
        print("d:",d,"w:",w,"k:",k_number)
        print("4 base3")
        print("ans",sum/test_time)
        print("4 base3",file=f1) 
        print("d:",d,"w:",w,"k:",k_number,file=f1) 
        print("all",ten_times_ans,"\n",file=f1) 
        print("ans",sum/test_time,"\n",file=f1) 

        ### situation of flow pass through switch 
        switch_flow = []
        for index, switch in enumerate(link_list):
            tmp = 0
            for num in switch:
                tmp += num
            switch_flow.append(tmp)
            print("4_baseline3_switch_",index,"=",tmp,file = f1)

        print("pass through",switch_flow,file=f1)

        ### situation of how many flow that switch stored and ARE of flow
        num_of_flow_in_switch = [ 0 for _ in range(20)]
        are_of_flow_in_switch = [ [] for _ in range(20)]
        for flow in store_set.keys():
            if(record_original_list[flow]>10):
                tmp = are(flow)
                # if(tmp == 0):
                #     print("it's zero",store_set[flow],file =f1)
                #     print("its path = ",recode_path_list[flow],file =f1)
                for switch in store_set[flow]:
                    num_of_flow_in_switch[switch] += 1
                    are_of_flow_in_switch[switch].append(tmp) 
        print("num_of_flow_store_in_switch",num_of_flow_in_switch,file=f1)

        tmp_list = []
        ave_list = []
        for index,switch in enumerate(are_of_flow_in_switch):
            print("switch",index,"are",switch,file=f1)
            tmp_list.append(stats.trim_mean(switch,0.1))
            sum = 0
            for i in switch:
                sum += i
            ave_list.append(sum/len(switch))
        print("switch_ARE_with_trim_mean",tmp_list,file=f1)
        print("switch_ARE_not with_trim_mean",ave_list,file=f1)