import os
import time
for i in range(30):
	os.system('iperf -c 120.26.8.97 -n 10M')
	time.sleep(5)