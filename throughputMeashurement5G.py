import matplotlib.pyplot as plt
import matplotlib
from pylab import plot, show, savefig, xlim, figure, ylim, legend, boxplot, setp, axes
import dataPreprocess
import numpy as np
from matplotlib.patches import Polygon
# fake data
color = ['#ABDBF0','#F7BC8F','#9585D9','#FD7C54']
colorSurround = ['#7BC6E6','#F1914F','#5740C0','#FB2C08']
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'

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


labels = ["QUIC","MPQUIC","TCP","MPTCP"]
labels2 = ["QUIC","MPQUIC","TCP","MPTCP"]
fs = 10  # fontsize
plt.rc('font',family='Times New Roman',size=12,weight='bold')
plt.xticks(fontsize=20,rotation=90)
plt.yticks(fontsize=20)

QUIC9 = dataPreprocess.universalPreprocess("magazine9.txt","QUIC",30)
MPQUIC9 = dataPreprocess.universalPreprocess("magazine9.txt","MPQUIC",30)
TCP9 = dataPreprocess.universalPreprocess("magazine9.txt","TCP",30)
MPTCP9 = dataPreprocess.universalPreprocess("magazine9.txt","MPTCP",30)

morning9 = [QUIC9,MPQUIC9,TCP9,MPTCP9]


QUIC12 = dataPreprocess.universalPreprocess("magazine12.txt","QUIC",30)
MPQUIC12 = dataPreprocess.universalPreprocess("magazine12.txt","MPQUIC",30)
TCP12 = dataPreprocess.universalPreprocess("magazine12.txt","TCP",30)
MPTCP12 = dataPreprocess.universalPreprocess("magazine12.txt","MPTCP",30)

morning12 = [QUIC12,MPQUIC12,TCP12,MPTCP12]

QUIC18 = dataPreprocess.universalPreprocess("magazine18.txt","QUIC",30)
MPQUIC18 = dataPreprocess.universalPreprocess("magazine18.txt","MPQUIC",30)
TCP18 = dataPreprocess.universalPreprocess("magazine18.txt","TCP",30)
MPTCP18 = dataPreprocess.universalPreprocess("magazine18.txt","MPTCP",30)

afternoon = [QUIC18,MPQUIC18,TCP18,MPTCP18]

QUIC23 = dataPreprocess.universalPreprocess("magazine23.txt","QUIC",30)
MPQUIC23 = dataPreprocess.universalPreprocess("magazine23.txt","MPQUIC",30)
TCP23 = dataPreprocess.universalPreprocess("magazine23.txt","TCP",30)
MPTCP23 = dataPreprocess.universalPreprocess("magazine23.txt","MPTCP",30)

evening23 = [QUIC23,MPQUIC23,TCP23,MPTCP23]

fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(9.33, 6.66),dpi=100)#figsize代表了画图的大小

mn9bp = axs.boxplot(morning9, positions = [1,1.2,1.4,1.6],widths = 0.13)
setBoxColors(mn9bp,axs)
setBoxProperties(mn9bp)

mn12bp = axs.boxplot(morning12,positions = [2.4,2.6,2.8,3.0],widths = 0.13)
setBoxColors(mn12bp,axs)
setBoxProperties(mn12bp)

anbp = axs.boxplot(afternoon,positions = [3.8,4.0,4.2,4.4],widths = 0.13)
setBoxColors(anbp,axs)
setBoxProperties(anbp)

enbp = axs.boxplot(evening23,positions = [5.2,5.4,5.6,5.8],widths = 0.13)

setBoxColors(enbp,axs)
setBoxProperties(enbp)


y_ticks = np.arange(0, 60, 10)
axs.set_yticks(y_ticks)
axs.set_xticks([0.935,1.665,2.335,3.065,3.755,4.465,5.135,5.865],)
axs.set_xticklabels(['         9:00 ', '10:00          ','          12:00 ','13:00          ','          18:00 ',' 19:00          ','          23:00 ','24:00          '])

#axs.set(
#    axisbelow=True,  # Hide the grid behind plot objects
#    xlabel='Time',
#    ylabel='Goodput measurement(Mbps)',
#		weight='bold'
#)
axs.tick_params(width=1.5)
axs.spines['bottom'].set_linewidth(1.5)
axs.spines['right'].set_linewidth(1.5)
axs.spines['top'].set_linewidth(1.5)
axs.spines['left'].set_linewidth(1.5)
#for ax in axs.flat:
#    ax.set_yscale('log')
#    ax.set_yticklabels([])
#QUIC = plot([1,1],'-',color = color[0])
#MPQUIC, = plot([1,1],'-',color = color[1])
#TCP = plot([1,1],'-',color = color[2])
#MPTCP = plot([1,1],'-',color = color[3])
#axs.legend((QUIC,MPQUIC,TCP,MPTCP),('QUIC', 'MPQUIC','TCP','MPTCP'))
#QUIC.set_visible(False)
#MPQUIC.set_visible(False)
#TCP.set_visible(False)
#MPTCP.set_visible(False)
fig.subplots_adjust(hspace=0.4)
plt.show()