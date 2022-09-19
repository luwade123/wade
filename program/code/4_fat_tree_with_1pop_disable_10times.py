import enum
import copy
from tkinter import W
from tracemalloc import start

from numpy import append, record
from switch_node import SwitchNode
from countminsketch import CountMinSketch
from scapy.all import *
test_time = 10
file_name = '4_1_fat_tree_algo_with_new_bar2.txt'
f1 = open(file_name,'w')
for top_k in range(3):
    for d_w in range(4):
        ten_times_ans = []
        two_switch_store = [[],[]]
        three_switch_store = [[],[],[]]
        bar_counting = [0,0,0]
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

            sketch_a0 = CountMinSketch(w, d)
            sketch_a1 = CountMinSketch(w, d)
            sketch_a2 = CountMinSketch(w, d)
            sketch_a3 = CountMinSketch(w, d)
            sketch_a4 = CountMinSketch(w, d)
            sketch_a5 = CountMinSketch(w, d)

            sketch_c0 = CountMinSketch(w, d)
            sketch_c1 = CountMinSketch(w, d)
            sketch_c2 = CountMinSketch(w, d)

            switch_list = [t0,t1,t2,t3,t4,t5,t6,t7,a0,a1,a2,a3,a4,a5,a6,a7,c0,c1,c2,c3]
            sketch_list = [sketch_t0,sketch_t1,sketch_t2,sketch_t3,sketch_t4,sketch_t5,sketch_a0,sketch_a1,sketch_a2,sketch_a3,sketch_a4,sketch_a5,sketch_c0,sketch_c1,sketch_c2]

            num_of_switch = len(sketch_list)
            dijk_list = [[9999 for _ in range(num_of_switch)] for _ in range(num_of_switch)]
            link_list = [[0 for _ in range(num_of_switch)] for _ in range(num_of_switch)]
            for i in range(num_of_switch):
                dijk_list[i][i] = 0
            # print(dijk_list)

            are_store = {}
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



            # print(sys.getsizeof(sketch_a0))
            path='dst2.txt'
            f = open(path,'r')
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
                # print("store set",old_path)
                if(start not in old_path):
                    old_path.insert(0,start)
                else:
                    start_point_in += 1
                if(end not in old_path):
                    old_path.append(end)
                # print("plus start and end",old_path)
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

            def Algo():
                MAX = 0             ## MAX of ARE of all flow.
                    ## MIN of the ARE for one flow to decide store in which switch. 
                which_flow = ''
                flow_num = -1
                which_switch = -1
                which_switch2 = -1
                for value in record_original_list.keys():
                    if(record_original_list[value]>10):
                        if(MAX<are(value)):
                            MAX = are(value)
                            which_flow = value
                MIN = collision(which_flow)
                if(which_flow != ''):
                    print('The worst flow is',which_flow,'Its ARE is',MAX,"total =",record_original_list[which_flow])
                #     for index,sketch in enumerate(sketch_list):
                #         if(index not in store_set[which_flow]):
                #             tmp = sketch.query(which_flow)
                #             if(MIN>tmp):
                #                 which_switch2 = index
                #                 MIN = tmp
                #     if(which_switch2 !=-1):                
                #         print('oringinal Put',which_flow,'into the switch',(which_switch2),"collision = ",num_to_sketch(which_switch2).query(which_flow),"MIN",MIN)                
                    which_path,which_switch,choose_path = find_switch(which_flow)
                    if(which_switch !=-1):
                        front_path = []
                        del_path = []
                        end_path = []
                        flag = 0
                        print("old",recode_path_list[which_flow])
                        print("last",choose_path[-1])
                        for i in recode_path_list[which_flow]:
                            if(flag == 0):
                                if(i == choose_path[0]):
                                    del_path.append(i)
                                    flag = 1
                                else:
                                    front_path.append(i)
                            elif(flag == 1):
                                del_path.append(i)
                                if(i == choose_path[-1]):
                                    flag = 2
                            elif(flag == 2):
                                end_path.append(i)
                        # print("front",front_path)    
                        # print("delete",del_path)
                        # print("end",end_path)
                        delete_the_link_cost(del_path)
                        add_the_link_cost(choose_path)
                        # print("choose",choose_path)
                        recode_path_list[which_flow] = front_path + choose_path +end_path
                        # print("new",recode_path_list[which_flow])
                        print("new are = ",num_to_sketch(which_switch).query(which_flow)/record_original_list[which_flow])
                        print('Put',which_flow,'into the switch',(which_switch),"collision",num_to_sketch(which_switch).query(which_flow))
                        
                        if(which_flow not in are_store.keys()):
                            are_store[which_flow] = [are(which_flow)]
                        else:
                            are_store[which_flow].append(are(which_flow))
                        num_to_sketch(which_switch).add(which_flow,record_original_list[which_flow])
                        # print(store_set[which_flow])
                        store_set[which_flow].insert(which_path,which_switch)
                        
                        
                        # print(store_set[which_flow])
                        Algo()
                    else:
                        ten_times_ans.append(MAX)
                        print('Can not be better.')

                else:
                    print('Everyone is best.')

            pcaps = rdpcap("u1_pt1_10sec_00000_20091218002604.pcapng")
            #k times
            all =0
            for packets in pcaps:
                try:
                    src = packets['IP'].src
                    dst = packets['IP'].dst
                    tmp = src + ' ' + dst
                    s = int(routing[src])%6
                    end = int(routing[dst])%6
                    if(s == end):
                        if(new_routing[dst] == -1):
                            end = (end+1)%6
                            new_routing[dst] = str(end)
                        else:
                            end = int(new_routing[dst])
                    if(tmp not in have_been_record):
                        have_been_record.append(tmp)
                        record_original_list[tmp] = 1
                        path = k_shortest_path(tmp,s,end,k_number)
                        # print("first_path",path,tmp)
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
            # print(dijk_list)
            # print(link_list)
            # print(i)
            # print(max)

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
            for i in are_store.keys():
                are_store[i].append(are(i))
            ### situation of flow store switch
            for i in are_store.keys():
                # print(i,"store = ",are_store[i])
                if(len(are_store[i]) == 3):
                    print(are_store[i],i,file=f1)
                    three_switch_store[0].append(are_store[i][0])
                    three_switch_store[1].append(are_store[i][1])
                    three_switch_store[2].append(are_store[i][2])
                    bar_counting[2] += 1
                elif(len(are_store[i]) == 2):
                    two_switch_store[0].append(are_store[i][0])
                    two_switch_store[1].append(are_store[i][1])
                    bar_counting[1] += 1
            for i in record_original_list.keys():
                if(record_original_list[i]>10):
                    if(len(store_set[i]) == 1):
                        bar_counting[0] += 1 

        # print("all ans", ten_times_ans)

        sum = 0
        for i in ten_times_ans:
            sum += i

        # print("ave",sum/test_time)
        print("4-1 algo",file=f1) 
        print("d:",d,"w:",w,"k:",k_number,file=f1) 
        print("all",ten_times_ans,"\n",file=f1) 
        print("ans",sum/test_time,"\n",file=f1) 

        # bar = {}
        # bar_store_list= {}
        # bar_counting = {}
        # for flow_name in record_original_list.keys():
        #     if(record_original_list[flow_name]>10):
        #         bar[flow_name] = are(flow_name)
        # trimmean_list = sorted(bar.items(),key=lambda x:x[1])
        # for i in range(round(len(trimmean_list)*0.95)):
        #     id = str(trimmean_list[i][0])
        #     print(id)
        #     number = len(store_set[id])
        #     if(number not in bar_store_list.keys()):
        #         bar_store_list[number] = are(id)
        #         bar_counting[number] = 1
        #     else:
        #         bar_store_list[number] += are(id)
        #         bar_counting[number] += 1
        # for i in bar_store_list.keys():
        #     print("number",i,"average are: ",bar_store_list[i]/bar_counting[i]," ") 
        #     print("number",i,"average are: ",bar_store_list[i]/bar_counting[i],"total flow",bar_counting[i]," ",file=f1) 
        # print("\n",file=f1)

        for i in range(3):
            print("number",i,"switch:",bar_counting[i],file=f1)

        ### situation of flow store switch
        print("2-1",two_switch_store[0],file=f1)
        print("2-2",two_switch_store[1],file=f1)
        print("3-1",three_switch_store[0],file=f1)
        print("3-2",three_switch_store[1],file=f1)
        print("3-3",three_switch_store[2],file=f1)