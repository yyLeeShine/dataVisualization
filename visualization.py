import matplotlib.pyplot as plt
import dataPreprocess
# fake data
labels = ["4G","4G+4G","LINE","4G+LINE"]
fs = 10  # fontsize

tpt4G = dataPreprocess.throughputPreprocess("clientlog.txt","4G",50)[1:50]
tpt4G4G = dataPreprocess.throughputPreprocess("clientlog.txt","4G+4G",50)[1:50]
tptLINE = dataPreprocess.throughputPreprocess("clientlog.txt","LINE",50)[1:50]
tpt4GLINE = dataPreprocess.throughputPreprocess("clientlog.txt","4G+LINE",50)[1:50]

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))#figsize代表了画图的大小
axs[0].boxplot([tpt4G,tpt4G4G,tptLINE,tpt4GLINE], labels=labels,showmeans=True,)
axs[0].set_title('throughputMeasurement', fontsize=fs)

fps4G = dataPreprocess.fpsPreprocess("clientlog.txt","4G",50)[1:50]
fps4G4G = dataPreprocess.fpsPreprocess("clientlog.txt","4G+4G",50)[1:50]
fpsLINE = dataPreprocess.fpsPreprocess("clientlog.txt","LINE",50)[1:50]
fps4GLINE = dataPreprocess.fpsPreprocess("clientlog.txt","4G+LINE",50)[1:50]
axs[1].boxplot([fps4G,fps4G4G,fpsLINE,fps4GLINE], labels=labels, showmeans=True)
axs[1].set_title('FPSmeasurement', fontsize=fs)




#for ax in axs.flat:
#    ax.set_yscale('log')
#    ax.set_yticklabels([])

fig.subplots_adjust(hspace=0.4)
plt.show()