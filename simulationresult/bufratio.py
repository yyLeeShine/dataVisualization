import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks",rc={"lines.linewidth": 2,'grid.linewidth': 2},)

# Load the example exercise dataset
df = sns.load_dataset('bufratio',data_home='/Users/liyahui/work/PycharmProjects/dataVisualization/simulationresult/',cache=True)

# Draw a pointplot to show pulse as a function of three categorical factors
g = sns.catplot(x="loss", y="value", hue="protocol",
                capsize=.2, height=8.5, aspect=1.5,kind="point", data=df,markers=[".", ".","."],
                   linestyles=[":", "--","-."],palette=['b','#F7BC8F','#9585D9'])#一个kind是包含了MPQUIC、MPTCP、VICTOR,x轴应当是不同的组合
#g.despine(left=True)g.set_xlim(0,20) # 限制x的值为[0,20]
g.set(ylim=(0, 1))
plt.grid()
# Loop over the bars

plt.savefig('bufratio.png', transparent=True,dpi = 600)
plt.show()