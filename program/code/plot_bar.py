from matplotlib import pyplot as plt
# import pandas as pd
# import seaborn as sns

# df = pd.DataFrame([
#     ['1', 'store 1', 3.5993856132128608],
#     ['1', 'store 2', 7.6208430458430465],
#     ['3', 'store 1', 3.226584815992336],
#     ['3', 'store 2', 6.926645021645021],
#     ['5', 'store 1', 3.5244331992199767],
#     ['5', 'store 2', 7.923975481040698],
# ], columns=['Top-k', 'number of stored switch', 'ARE'])
# ax = plt.bar(x='Top-k', y='ARE', hue='number of stored switch',height = 10, data=df)
# ax.set_title('Final Term')

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# k = ['1', '3', '5']
# stored_one_switch = [3.5993856132128608, 3.226584815992336, 3.5244331992199767]
# stored_two_switch = [7.6208430458430465, 6.926645021645021, 7.923975481040698]
# x = np.arange(len(k))
# width = 0.3
# plt.bar(x, stored_one_switch, width, color='green', label='stored in 1 switch',)

# plt.bar(x + width, stored_two_switch, width, color='blue', label='stored in 2 switch')
# plt.xticks(x + width / 2, k)
# plt.ylabel('ARE')
# plt.title('d = 5,w = 3')

# plt.legend()
# plt.show()

import pandas as pd
import seaborn as sns
# df = pd.DataFrame([
#     ['1', 'store in 1 switch', 3.5993856132128608],
#     ['1', 'store in 2 switch', 7.6208430458430465],
#     ['1', 'only 1 switch', 4.289725823224249],
#     ['3', 'store in 1 switch', 3.226584815992336],
#     ['3', 'store in 2 switch', 6.926645021645021],
#     ['3', 'only 1 switch', 4.367521866533978],
#     ['5', 'store in 1 switch', 3.5244331992199767],
#     ['5', 'store in 2 switch', 7.923975481040698],
#     ['5', 'only 1 switch', 4.351344147251271],
# ], columns=['Top k', 'Class', 'ARE'])
df = pd.DataFrame([
    ['4-3', '3-1', 113.60606060606061],
    ['4-3', '3-2', 94.7878787878788],
    ['4-3', '3-3', 95.54545454545455],
    ['4-3', '2-1', 106.12672646797645],
    ['4-3', '2-2', 87.38958957708957],

    ['4-2', '2-1', 34.946686151689825],
    ['4-2', '2-2', 25.288321985032518],

    ['4-1', '3-1', 19.636363636363637],
    ['4-1', '3-2', 15.909090909090908],
    ['4-1', '3-3', 16.0],
    ['4-1', '2-1', 21.439075801759625],
    ['4-1', '2-2', 13.448366459001484],

    ['4', '3-1', 22.060606060606062 ],
    ['4', '3-2', 9.170454545454547 ],
    ['4', '3-3', 10.81439393939394 ],
    ['4', '2-1', 13.792041432366508 ],
    ['4', '2-2', 7.958766337578258 ],

    ['6', '3-1', 5.386969696969697],
    ['6', '3-2', 2.3484848484848486],
    ['6', '3-3', 2.1360606060606058],
    ['6', '2-1', 4.167376225634664 ],
    ['6', '2-2', 1.5253193970900085 ],
    
], columns=['Topo', 'Class', 'ARE(%)'])

ax = sns.barplot(x='Topo', y='ARE(%)', hue='Class', data=df)

hatches = ([ "x" ,"x" ,"x","x","x", "|", "|", "|", "|", "|", "/", "/", "/", "/", "/",'-','-','-','-','-','*','*','*','*','*'])

# Loop over the bars
for i,thisbar in enumerate(ax.patches):
    # Set a different hatch for each bar
    print(i)
    thisbar.set_hatch(hatches[i])
ax.set_title('Flow ARE store in different number of switch with Sketch with d = 5,w = 3,k = 5')
ax.legend(title = 'Class')
ax.legend(prop={'size': 10})
plt.show()