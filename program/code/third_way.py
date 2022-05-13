from countminsketch import CountMinSketch
from scapy.all import *

sketch1 = CountMinSketch(3, 5)
sketch2 = CountMinSketch(3, 5)
sketch3 = CountMinSketch(3, 5)
sketch4 = CountMinSketch(3, 5)
sketch5 = CountMinSketch(3, 5)
sketch6 = CountMinSketch(3, 5)


pcaps = rdpcap("u1_pt1_10sec_00000_20091218002604.pcapng")
keys = open("keys.txt", 'r')

set_of_sketch = [sketch1,sketch2,sketch3,sketch4,sketch5,sketch6]
set_of_flow = []
store_set = {}
for key in keys:
    set_of_flow.append(key)

# print(set_of_flow)

Store_in = [[0 for _ in range(len(set_of_sketch))] for _ in range(len(set_of_flow))]

flow_set = {}               #use for test
def id_to_int(id):
    for index, flow_id in enumerate(set_of_flow):
        if(flow_id == id):
            return index  
def sketch_add(switch_number,flow_id):
    for index, sketch in enumerate(set_of_sketch):
        if(switch_number == index):
            sketch.add(flow_id,1)
    # if(switch_number == 1):
    #     sketch1.add(flow_id,flow_set[flow_id])
    #     Store_in[id_to_int(flow_id)][1-1] = 1
    # elif(switch_number == 2):
    #     sketch2.add(flow_id,flow_set[flow_id])
    #     Store_in[id_to_int(flow_id)][2-1] = 1
    # elif(switch_number == 3):
    #     sketch3.add(flow_id,flow_set[flow_id])
    #     Store_in[id_to_int(flow_id)][3-1] = 1
    # elif(switch_number == 4):
    #     sketch4.add(flow_id,flow_set[flow_id])
    #     Store_in[id_to_int(flow_id)][4-1] = 1
    # elif(switch_number == 5):
    #     sketch5.add(flow_id,flow_set[flow_id])
    #     Store_in[id_to_int(flow_id)][5-1] = 1
    # elif(switch_number == 6):
    #     sketch6.add(flow_id,flow_set[flow_id])
    #     Store_in[id_to_int(flow_id)][6-1] = 1
def sketch_add_total(switch_number,flow_id):
    for index, sketch in enumerate(set_of_sketch):
        if(switch_number == index):
            sketch.add(flow_id,flow_set[flow_id])
def sketch_query(switch_number,flow_id):
    for index, sketch in enumerate(set_of_sketch):
        if(switch_number == index ):
            return sketch.query(flow_id)
def ARE(id,num_id,total):
    MIN = 30000
    for (item, sketch) in zip(Store_in[num_id],set_of_sketch):
        if(item == 1):
            tmp = sketch.query(id)
            if(tmp<MIN):
                MIN = tmp
    return abs(MIN-total)/total

def new_ARE(id,total):
    tmp = 0
    MIN = 30000
    for i in store_set[id]:
        tmp = sketch_query(i,id)
        if(tmp < MIN):
            MIN = tmp
    return MIN/total 
def which_switch(id):
    MIN = 30000
    which = -1
    count = -1
    for sketch in set_of_sketch:
        count += 1
        tmp = sketch.query(id)
        if(tmp<MIN):
            MIN = tmp
            which = count
    return which
def Algo():
    MAX = 0             ## MAX of ARE of all flow.
    MIN = 100000        ## MIN of the ARE for one flow to decide store in which switch. 
    which_flow = ''
    flow_num = -1
    which_switch = -1
    for value in flow_set.keys():
        if(MAX<new_ARE(value,flow_set[value])):
            MAX = new_ARE(value,flow_set[value])
            which_flow = value

    if(which_flow != ''):
        print('The worst flow is',which_flow,'Its ARE is',MAX)
        # for index,i in enumerate(Store_in[flow_num]):
        #     if(i == 0):
        #         tmp = sketch_query(index+1,which_flow)
        #         if(MIN>tmp):
        #             which_switch = index+1
        #             MIN = tmp
        for i in range(6):
            if(i not in store_set[which_flow]):
                tmp = sketch_query(i,which_flow)
                if(MIN>tmp):
                    which_switch = i
                    MIN = tmp
        if(which_switch !=-1):
            if(MIN != MAX):
                print('Put',which_flow.replace('\n',''),'into the switch',(which_switch+1))
                sketch_add(which_switch,which_flow)
                tmp_list = [which_switch]
                store_set[which_flow].extend(tmp_list)
                Algo()
            else:
                print('Can not be better.')
        else:
            print('Can not find more switch')
    else:
        print('Everyone is best.')
    
        

packet = open("packet.txt", 'r')


for packets in pcaps:
    try:
        if(packets['IP'].src in flow_set):
            flow_set[packets['IP'].src] += 1
            sketch_add(store_set[packets['IP'].src][0],packets['IP'].src)
        else:
            flow_set[packets['IP'].src] = 1
            tmp = which_switch(packets['IP'].src)
            sketch_add(tmp,packets['IP'].src)
            store_set[packets['IP'].src] = list()
            tmp_list = [tmp]
            store_set[packets['IP'].src].extend(tmp_list)
    except IndexError:
        pass
    
# for packets in packet:
#     if(packets in flow_set):
#         flow_set[packets] += 1 
#     else:
#         flow_set[packets] = 1
#     if(packets == 'A\n'):
#         sketch1.add(packets)
#         # sketch2.add(packets)
#         # sketch4.add(packets)
#         # sketch5.add(packets)
#         Store_in[0][1-1] = 1
#     if(packets == 'B\n'):
#         sketch1.add(packets)
#         # sketch2.add(packets)
#         # sketch3.add(packets)
#         # sketch5.add(packets)
#         # sketch6.add(packets)
#         Store_in[1][1-1] = 1
#         # Store_in[1][2-1] = 1
#         # Store_in[1][3-1] = 1
#         # Store_in[1][5-1] = 1
#         # Store_in[1][6-1] = 1
#     if(packets == 'C\n'):
#         sketch1.add(packets)
#         # sketch3.add(packets)
#         # sketch4.add(packets)
#         # sketch6.add(packets)
#         Store_in[2][1-1] = 1
#         # Store_in[2][3-1] = 1
#         # Store_in[2][4-1] = 1
#         # Store_in[2][6-1] = 1

# for sketch in set_of_sketch:
#     print(sketch.tables)
# for i in flow_set:
#     print(flow_set.values())
big_are = 0
who = ''
where = -1
# for value in flow_set.keys():
#     if(big_are<new_ARE(value,0,flow_set[value])):
#         big_are = new_ARE(value,0,flow_set[value])
#         who = value
# print(who,big_are)
# print(store_set[who])
# print('original:',flow_set[who])
Algo()
# print(sketch1[who])
# print(sketch2[who])
# print(sketch3[who])
# print(sketch4[who])
# print(sketch5[who])
# print(sketch6[who])
for sketch in set_of_sketch:
    print(sketch.tables)
