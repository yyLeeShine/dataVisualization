# filePath is the location of the file that needs to be processed
# location is the place where the data needs to be processed
# num is the total number of the processed data we will get
def sttPreprocess(filePath,location):

	fileobject = open(filePath,'r')
	str = fileobject.readline()
	result = []

	while str != "":#寻找正确的位置
		element = str.strip('\n').split(' ')
		if element[len(element)-1]==location :
			break
		str = fileobject.readline()

	str = fileobject.readline()

	while "time" in str  and str!="":
		str = str.strip('\n')
		element = str.split(' ')
		result.append(float(element[-1]))
		str = fileobject.readline()

	return result
# filePath is the location of the file that needs to be processed
# location is the place where the data needs to be processed
# num is the total number of the processed data we will get
def throughputPreprocess(filePath,location,num):

	fileobject = open(filePath,'r')
	str = fileobject.readline()
	result = []

	while str != "":#寻找正确的位置
		element = str.strip('\n').split(' ')
		if element[len(element)-1]==location :
			break
		str = fileobject.readline()

	str = fileobject.readline()

	while len(result) != num and str!="":
		str = str.strip('\n')
		element = str.split(' ')
		if(element[-2]!="throughput(MB):"):
			str = fileobject.readline()
			continue
		result.append(float(element[-1]))
		str = fileobject.readline()

	return result

# filePath is the location of the file that needs to be processed
# location is the place where the data needs to be processed
# num is the total number of the processed data we will get
def fpsPreprocess(filePath,location,num):

	fileobject = open(filePath,'r')
	str = fileobject.readline()
	result = []

	while str != "":#寻找正确的位置
		element = str.strip('\n').split(' ')
		if element[len(element)-1]==location :
			break
		str = fileobject.readline()

	str = fileobject.readline()

	while len(result) != num and str!="":
		str = str.strip('\n')
		element = str.split(' ')
		if(element[-2]!="FPS:"):
			str = fileobject.readline()
			continue
		result.append(float(element[-1]))
		str = fileobject.readline()

	return result
# filePath is the location of the file that needs to be processed
# location is the place where the data needs to be processed
# num is the total number of the processed data we will get
def universalPreprocess(filePath,location,num):

	fileobject = open(filePath,'r')
	str = fileobject.readline()
	str = str.strip('\n')
	result = []
	while str != location:#寻找正确的位置
		str = fileobject.readline()
		str = str.strip('\n')
	str = fileobject.readline()

	while len(result) != num and str!="":
		str = str.strip('\n')
		result.append(float(str))
		str = fileobject.readline()

	return result
if __name__ == '__main__':
	tpuRes = throughputPreprocess("./clientlog.txt","LINE",50)
	fpsRes = fpsPreprocess("./clientlog.txt","LINE",50)
	res = universalPreprocess("./magazinelog.txt","QUIC",30)
	a = 1