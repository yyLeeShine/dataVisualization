import matplotlib.pyplot as plt
import dataPreprocess
# fake data
labels = ["noChan","chanSend","chanRec"]
fs = 10  # fontsize
plt.rc('font',family='Times New Roman')

noChan = dataPreprocess.throughputPreprocess("clientlog3.txt","noChan",50)[1:50]
chanSend = dataPreprocess.throughputPreprocess("clientlog3.txt","chanSend",50)[1:50]
chanRec = dataPreprocess.throughputPreprocess("clientlog3.txt","chanRec",50)[1:50]

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))#figsize代表了画图的大小
axs[0].boxplot([noChan,chanSend,chanRec], labels=labels,showmeans=True,)
axs[0].set_title('throughputMeasurement', fontsize=fs)

fps4G = dataPreprocess.fpsPreprocess("clientlog3.txt","noChan",50)[1:50]
fps4G4G = dataPreprocess.fpsPreprocess("clientlog3.txt","chanSend",50)[1:50]
fps4G4G2 = dataPreprocess.fpsPreprocess("clientlog3.txt","chanRec",50)[1:50]
axs[1].boxplot([fps4G,fps4G4G,fps4G4G2], labels=labels, showmeans=True)
axs[1].set_title('FPSmeasurement', fontsize=fs)




#for ax in axs.flat:
#    ax.set_yscale('log')
#    ax.set_yticklabels([])

fig.subplots_adjust(hspace=0.4)
plt.show()