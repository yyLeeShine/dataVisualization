import numpy as np
import matplotlib.pyplot as plt



np.random.seed(19680801)

mu = 200
sigma = 25
n_bins = 100
x = np.random.normal(mu, sigma, size=100)

fig, ax = plt.subplots(figsize=(8.5, 4))
ax.set_xlim([0,165])
ax.set_ylim([0,1])
fileobject = open('18mpquic.txt','r')
str = fileobject.readline()
result = []
while str != "":  # 寻找正确的位置
	if str.__contains__("ms") :
		result.append(float(str[0:-3]))
	elif str.__contains__("µs") :
		str2 = str[0:len(str)-3]
		result.append(float(float(str[0:-3]))/1000.0)
	else :
		result.append(float(float(str[0:-2])) * 1000.0)
	str = fileobject.readline()


# plot the cumulative histogram
n, bins, patches = ax.hist(result, 700, density=True, histtype='step',
                           cumulative=True)

fileobject = open('36mpquic.txt','r')
str = fileobject.readline()
result = []
while str != "":  # 寻找正确的位置
	if str.__contains__("ms") :
		result.append(float(str[0:-3]))
	elif str.__contains__("µs") :
		str2 = str[0:len(str)-3]
		result.append(float(float(str[0:-3]))/1000.0)
	else :
		result.append(float(float(str[0:-2])) * 1000.0)
	str = fileobject.readline()

n, bins, patches = ax.hist(result, 1500, linestyle='--',density=True, histtype='step',
                           cumulative=True, linewidth=1)

fileobject = open('36mptcp.txt','r')
str = fileobject.readline()
result = []
while str != "":  # 寻找正确的位置
	if str.__contains__("ms") :
		result.append(float(str[0:-3]))
	elif str.__contains__("µs") :
		str2 = str[0:len(str)-3]
		result.append(float(float(str[0:-3]))/1000.0)
	else :
		result.append(float(float(str[0:-2])) * 1000.0)
	str = fileobject.readline()

n, bins, patches = ax.hist(result, 1500, linestyle=':',density=True, histtype='step',
                           cumulative=True, linewidth=1)

fileobject = open('18mptcp.txt','r')
str = fileobject.readline()
result = []
while str != "":  # 寻找正确的位置
	if str.__contains__("ms") :
		result.append(float(str[0:-3]))
	elif str.__contains__("µs") :
		str2 = str[0:len(str)-3]
		result.append(float(float(str[0:-3]))/1000.0)
	else :
		result.append(float(float(str[0:-2])) * 1000.0)
	str = fileobject.readline()

n, bins, patches = ax.hist(result, 1500, linestyle='-.',density=True, histtype='step',
                           cumulative=True, linewidth=1)


# tidy up the figure
ax.grid(True)
ax.legend(loc='right')
ax.set_title('Cumulative step histograms')
ax.set_xlabel('Annual rainfall (mm)')
ax.set_ylabel('Likelihood of occurrence')
plt.xticks(np.arange(0,265,33))
plt.savefig('cdf.png', transparent=True,dpi = 600)
plt.show()