import numpy as np 
from matplotlib import pyplot as plt 

algo_5_3_k1_x =[3.0200526317420837, 4.334103639921171, 3.0859296577564357, 3.2792348397119304, 4.724892857142858, 3.7958526025726416, 4.235683106123786, 4.375239458673733, 4.64499568668047, 3.9227818572935615, 3.1993461032668886, 2.641474844405546, 3.284824045930429, 5.3949299686799685, 5.040631805156564, 4.49563329360554, 4.709504592083332, 3.7986238792418563, 4.892820669934641, 4.853575089825272]
b1_5_3_k1_x = [19.49515813530847, 21.985096120218625, 14.30159064623665, 18.110519225820177, 14.11288422122469, 18.064669042604564, 19.534704421837162, 23.19703349498872, 19.337682083232696, 19.34434848236386, 18.23335903370357, 15.695336931106583, 15.110441640998399, 18.158344505015247, 20.790292717600988, 21.493264011374528, 19.662755329904147, 16.267286695162024, 19.60660871504948, 17.621800825349293]
b2_5_3_k1_x =[3.1638932845321097, 5.254906500684404, 2.1595679406639157, 1.7195428557672183, 2.719816230717639, 5.181887734925243, 4.162516271118061, 3.158354613740462, 5.74924189989597, 2.242611583298336, 4.028711534037622, 3.8310525636914528, 2.7111133744705267, 5.860623168838376, 3.7966005235821676, 4.707722349241015, 6.114054063913614, 3.9613057227999757, 4.846446380041143, 4.3973341772280605]
b3_5_3_k1_x =[0.33745014245014243, 2.321262516962256, 3.1958908917821938, 4.262391861992864, 3.665043245804115, 5.663281665652356, 2.2722308167022227, 5.190833957649814, 4.641184482696844, 2.9137684619302266, 4.174737624266493, 3.8340220736054067, 3.8790580572632334, 4.867070887442945, 4.959761887938802, 3.7761894619760557, 5.223870542734498, 4.5849206349206355, 4.681932138977753, 6.105436830226638]

algo_5_3_k5_x =[3.278083021079545, 2.7082815381638126, 3.3732040476258924, 3.5371636156892827, 3.5293584632199657, 4.100512882003589, 4.209567195643076, 5.310780415820738, 4.448068459318459, 4.199439000474349, 3.5415063208469473, 2.8327419881498512, 6.066609736093019, 3.326328455495122, 4.526341766813426, 4.739375962778978, 4.853837209302325, 5.3285325120420035, 4.660260450303456, 2.137634130994022]
b1_5_3_k5_x = [22.39136462172567, 24.456786478639547, 17.789571140092768, 20.644153193647675, 14.484047442547515, 19.8568279348803, 21.500196741049177, 23.057283777374263, 19.330085675696736, 24.615453986347262, 18.68881175079995, 20.714928615971775, 17.465285357770302, 18.19022505998995, 19.932418131034773, 24.262065841803405, 15.006958496768343, 21.082981439190263, 21.241437106920163, 23.201382969976276]
b2_5_3_k5_x = [4.56197407348526, 3.3048376201857215, 3.5787384390410404, 2.0634047654111765, 3.331205287279231, 0.6971417802259877, 5.4427214240177735, 4.673371496426783, 5.19014030156242, 3.026913100624656, 3.9256646362474115, 2.913264186230058, 3.64977614977615, 7.799902581534896, 3.6584501002756986, 4.147950607624184, 5.039736247062928, 3.5089882740183973, 5.044747707389341, 2.6857006188130095]
b3_5_3_k5_x = [0.3606711901222071, 2.792895228858104, 4.564260071302121, 4.173013583638584, 3.710164157154982, 5.527046086485587, 4.017430254930255, 3.0698186096676148, 4.769417500286587, 3.5519042973770665, 3.382413269098052, 3.957924891437644, 4.270317731484743, 3.9800119916592, 5.328245435516593, 3.736682846744599, 3.3396918906356103, 5.398069412174702, 3.006201415072383, 4.067790600427885]



algo_5_3_k1_y = []
b1_5_3_k1_y = [] 
b2_5_3_k1_y = [] 
b3_5_3_k1_y = [] 

algo_5_3_k5_y = []
b1_5_3_k5_y = [] 
b2_5_3_k5_y = [] 
b3_5_3_k5_y = [] 

x_k1 = [algo_5_3_k1_x,b1_5_3_k1_x,b2_5_3_k1_x,b3_5_3_k1_x]
x_k5 = [algo_5_3_k5_x,b1_5_3_k5_x,b2_5_3_k5_x,b3_5_3_k5_x]

y_k1 = [algo_5_3_k1_y,b1_5_3_k1_y,b2_5_3_k1_y,b3_5_3_k1_y]
y_k5 = [algo_5_3_k5_y,b1_5_3_k5_y,b2_5_3_k5_y,b3_5_3_k5_y]

sorted_x_k1 =[]
sorted_x_k5 =[]
sum_k1 = []
sum_k5 = []
for i in x_k1:
    tmp = 0
    for data in i:
        tmp += data
    sum_k1.append(tmp)

for i in x_k5:
    tmp = 0
    for data in i:
        tmp += data
    sum_k5.append(tmp)


for index,x in enumerate(x_k1):
    tmp = 0
    tmp_x = sorted(x)
    sorted_x_k1.append(tmp_x)
    for data in tmp_x:
        tmp += data
        y_k1[index].append(tmp/sum_k1[index])

for index,x in enumerate(x_k5):
    tmp = 0
    tmp_x = sorted(x)
    sorted_x_k5.append(tmp_x)
    for data in tmp_x:
        tmp += data
        y_k5[index].append(tmp/sum_k5[index])

plt.title("CDF of average ARE of every switch, d=5, w=3, k=1, dist = 4") 
plt.xlabel("ARE of switch") 
plt.ylabel("ARE/total of ARE") 

### k = 1
plt.plot(sorted_x_k1[0],y_k1[0],label='algo',linestyle = 'dashed')
# plt.plot(sorted_x_k1[1],y_k1[1],label='baseline 1',linestyle = 'solid')
plt.plot(sorted_x_k1[2],y_k1[2],label='baseline 2',linestyle = 'dotted')
plt.plot(sorted_x_k1[3],y_k1[3],label='baseline 3',linestyle = '-.')

### k = 5
# plt.plot(sorted_x_k5[0],y_k5[0],label='algo',linestyle = 'dashed')
# plt.plot(sorted_x_k5[1],y_k5[1],label='baseline 1',linestyle = 'solid')
# plt.plot(sorted_x_k5[2],y_k5[2],label='baseline 2',linestyle = 'dotted')
# plt.plot(sorted_x_k5[3],y_k5[3],label='baseline 3',linestyle = '-.')

plt.legend()
plt.show()