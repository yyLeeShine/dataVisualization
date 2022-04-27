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
victor = [0.52,0.56,0.52,0.60,0.60,0.60,0.56,0.56,0.56,0.56,0.60,0.56,0.60,0.56,0.52,0.52,0.56,0.56,0.56,0.56]
mpquic = [1.8 ,1.79,1.52,1.85,1.79,1.69,1.29,1.81,1.69,1.75,1.82,1.88,1.95,1.92,1.75,1.82,1.82,1.59,1.52,1.42]
mptcp = [0.76,2.58,4.46,0.69,1.92,1.75,0.79,2.51,1.36,1.02,1.16,1.65,1.06,1.29,0.83,1.71,2.68,3.01,2.74]

fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(9.33, 7.66),dpi=100)#figsize代表了画图的大小
#axs.set_ylim([xmin,xmax])
bp=axs.boxplot([victor,mpquic,mptcp], positions = [0.55,2.77,4.99], widths = 0.3, labels=labels)
axs.set_title('rateBuf(in percentage)', fontsize=20)
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
plt.savefig('plotname.png', transparent=True)
plt.show()
