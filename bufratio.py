import matplotlib.pyplot as plt
import matplotlib
from pylab import plot, show, savefig, xlim, figure, ylim, legend, boxplot, setp, axes
from matplotlib.patches import Polygon
import numpy as np
import dataPreprocess
# fake data
def setBoxColors(bp,axs):
	for box in bp['boxes'] :
		box_x = []
		box_y = []
		for j in range(5):
			box_x.append(box.get_xdata()[j])
			box_y.append(box.get_ydata()[j])
		box_coords = np.column_stack([box_x, box_y])
	# Alternate between Dark Khaki and Royal Blue
		axs.add_patch(Polygon(box_coords, color=color[bp['boxes'].index(box)%4]))
color = ['#ABDBF0','#F7BC8F','#9585D9','#FD7C54']
colorSurround = ['#7BC6E6','#F1914F','#5740C0','#FB2C08']
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
def setBoxProperties(bp):
	for box in bp['boxes'] :
		setp(box, color=colorSurround[bp['boxes'].index(box)%4])
	for box in bp['medians'] :
		setp(box, color='black',linewidth=0.8)
	for box in bp['fliers'] :
		setp(box, color='red',marker='.')
		#setp(box['medians'], color='black')
    #setp(bp['boxes'][0], color='blue')
    #setp(bp['caps'][0], color='blue')
    #setp(bp['caps'][1], color='blue')
    #setp(bp['whiskers'][0], color='blue')
    #setp(bp['whiskers'][1], color='blue')
    #setp(bp['fliers'][0], color='blue')
    #setp(bp['fliers'][1], color='blue')
    #setp(bp['medians'][0], color='blue')
    #setp(bp['boxes'][1], color='red')
    #setp(bp['caps'][2], color='red')
    #setp(bp['caps'][3], color='red')
    #setp(bp['whiskers'][2], color='red')
    #setp(bp['whiskers'][3], color='red')
    #setp(bp['fliers'][2], color='red')
    #setp(bp['fliers'][3], color='red')
    #setp(bp['medians'][1], color='red')
labels = ["VICTOR","MPQUIC","MPTCP"]
fs = 10  # fontsize
plt.rc('font',family='Times New Roman',size=12,weight='bold')
plt.xticks(fontsize=20,rotation=90)
plt.yticks(fontsize=20)
victor2 = [7.04,7.75,7.98,8.31,8.48,8.39,8.06,8.06,8.74,7.74,8.74,8.16,9.15,8.37,7.89,6.69,7.71,7.59,7.80,8.52]
mpquic2 = [9.82 ,7.94 ,8.64 ,9.46 ,9.06 ,9.06 ,7.73 ,9.11 ,9.62 ,9.59 ,8.76 ,9.55 ,9.35 ,9.34 ,9.44 ,10.09,9.32 ,8.76 ,8.86 ,8.7  ]
mptcp2 = [15.92,15.03,18.33,15.89,15.72,15.60,15.48,14.84,14.76,14.87,14.40,14.42,15.11,15.12,16.11,14.62,14.96,14.83,14.83]

fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(5, 4),dpi=100)#figsize代表了画图的大小
bp=axs.boxplot([victor2,mpquic2,mptcp2], labels=labels,)
axs.set_ylim([6,16.5])
axs.yaxis.tick_right()
axs.set_title('bufRatio(in percentage)', fontsize=20)
setBoxColors(bp,axs)
setBoxProperties(bp)
#fps4G = dataPreprocess.fpsPreprocess("clientlog3.txt","noChan",50)[1:50]
#fps4G4G = dataPreprocess.fpsPreprocess("clientlog3.txt","chanSend",50)[1:50]
#fps4G4G2 = dataPreprocess.fpsPreprocess("clientlog3.txt","chanRec",50)[1:50]
#axs[1].boxplot([fps4G,fps4G4G,fps4G4G2], labels=labels, showmeans=True)
#axs[1].set_title('FPSmeasurement', fontsize=fs)




#for ax in axs.flat:
#    ax.set_yscale('log')
#    ax.set_yticklabels([])

fig.subplots_adjust(hspace=0.4)
plt.show()