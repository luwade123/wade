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
    ['4-3', '3-1', 106.27272727272727 ],
    ['4-3', '3-2', 104.0909090909091 ],
    ['4-3', '3-3', 102.54545454545455],
    ['4-3', '2-1', 109.64965168759811],
    ['4-3', '2-2', 90.61194014319014 ],

    ['4-2', '3-1', 33.31818181818181 ],
    ['4-2', '3-2', 30.454545454545453 ],
    ['4-2', '3-3', 29.545454545454547 ],
    ['4-2', '2-1', 35.060340700965696],
    ['4-2', '2-2', 25.984213356088357],


    ['4-1', '3-1', 20.0],
    ['4-1', '3-2', 18.416666666666668],
    ['4-1', '3-3', 17.75],
    ['4-1', '2-1', 23.762068112258348],
    ['4-1', '2-2', 12.973313254067852],

    ['4', '3-1', 19.583333333333332  ],
    ['4', '3-2', 14.833333333333334  ],
    ['4', '3-3', 14.333333333333334 ],
    ['4', '2-1', 19.49236014104435  ],
    ['4', '2-2', 11.814342667961089  ],

    ['6', '3-1', 6.160839160839161],
    ['6', '3-2', 3.24009324009324],
    ['6', '3-3', 2.191142191142191],
    ['6', '2-1', 4.566407933707773 ],
    ['6', '2-2', 1.614637399873731 ],
    
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