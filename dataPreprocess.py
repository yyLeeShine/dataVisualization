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
		result.append(int(element[-1]))
		str = fileobject.readline()

	return result
if __name__ == '__main__':
	res = sttPreprocess("./stt.txt","4G")
	a = 1