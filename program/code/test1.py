from countminsketch import CountMinSketch

sketch1 = CountMinSketch(2, 1)
sketch2 = CountMinSketch(2, 1)
sketch3 = CountMinSketch(2, 1)
sketch4 = CountMinSketch(2, 1)
sketch5 = CountMinSketch(2, 1)
sketch6 = CountMinSketch(2, 1)

set_of_sketch = [sketch1,sketch2,sketch3,sketch4,sketch5,sketch6]
set_of_flow = ['A\n','B\n','C\n']
Store_in = [[0 for _ in range(len(set_of_sketch))] for _ in range(len(set_of_flow))]

flow_set = {}               #use for test
def id_to_int(id):
    for index, flow_id in enumerate(set_of_flow):
        if(flow_id == id):
            return index  
def sketch_add(switch_number,flow_id):
    for index, sketch in enumerate(set_of_sketch):
        if(switch_number == index +1):
            sketch.add(flow_id,flow_set[flow_id])
            Store_in[id_to_int(flow_id)][index] = 1
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
def sketch_query(switch_number,flow_id):
    for index, sketch in enumerate(set_of_sketch):
        if(switch_number == index + 1):
            return sketch.query(flow_id)
    # if(switch_number == 1):
    #     return sketch1.query(flow_id)
    # elif(switch_number == 2):
    #     return sketch2.query(flow_id)
    # elif(switch_number == 3):
    #     return sketch3.query(flow_id)
    # elif(switch_number == 4):
    #     return sketch4.query(flow_id)
    # elif(switch_number == 5):
    #     return sketch5.query(flow_id)
    # elif(switch_number == 6):
    #     return sketch6.query(flow_id)
def ARE(id,num_id,total):
    MIN = 10000
    for (item, sketch) in zip(Store_in[num_id],set_of_sketch):
        if(item == 1):
            tmp = sketch.query(id)
            if(tmp<MIN):
                MIN = tmp
    return abs(MIN-total)/total

def Algo():
    MAX = 0             ## MAX of ARE of all flow.
    MIN = 100000        ## MIN of the ARE for one flow to decide store in which switch. 
    which_flow = ''
    flow_num = -1
    which_switch = -1
    for index,flow in enumerate(set_of_flow):
        are = ARE(flow,int(index),flow_set[flow])
        if(MAX<are):
            MAX = are
            which_flow = flow
            flow_num = index
    
    if(flow_num!=-1):
        print('The worst flow is',which_flow,'Its ARE is',MAX)
        for index,i in enumerate(Store_in[flow_num]):
            if(i == 0):
                tmp = sketch_query(index+1,which_flow)
                if(MIN>tmp):
                    which_switch = index+1
                    MIN = tmp
        if(which_switch !=-1):
            if(MIN != MAX):
                print('Put',which_flow.replace('\n',''),'into the switch',which_switch)
                sketch_add(which_switch,which_flow)
                Algo()
            else:
                print('Can not be better.')
        else:
            print('Can not find more switch')
    else:
        print('Everyone is best.')
    
        

packet = open("packet.txt", 'r')


for packets in packet:
    if(packets in flow_set):
        flow_set[packets] += 1 
    else:
        flow_set[packets] = 1
    if(packets == 'A\n'):
        sketch1.add(packets)
        # sketch2.add(packets)
        # sketch4.add(packets)
        # sketch5.add(packets)
        Store_in[0][1-1] = 1
        # Store_in[0][2-1] = 1
        # Store_in[0][4-1] = 1
        # Store_in[0][5-1] = 1
    if(packets == 'B\n'):
        sketch1.add(packets)
        # sketch2.add(packets)
        # sketch3.add(packets)
        # sketch5.add(packets)
        # sketch6.add(packets)
        Store_in[1][1-1] = 1
        # Store_in[1][2-1] = 1
        # Store_in[1][3-1] = 1
        # Store_in[1][5-1] = 1
        # Store_in[1][6-1] = 1
    if(packets == 'C\n'):
        sketch1.add(packets)
        # sketch3.add(packets)
        # sketch4.add(packets)
        # sketch6.add(packets)
        Store_in[2][1-1] = 1
        # Store_in[2][3-1] = 1
        # Store_in[2][4-1] = 1
        # Store_in[2][6-1] = 1
for sketch in set_of_sketch:
    print(sketch.tables)
for index,value in enumerate(flow_set.keys()):
    print(ARE(value,index,flow_set[value]))
Algo()
for sketch in set_of_sketch:
    print(sketch.tables)
