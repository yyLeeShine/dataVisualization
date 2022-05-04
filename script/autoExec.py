import os
import time
r = os.popen('/usr/local/go/bin/go run ./scatter_receiver.go')
info = r.readlines()  #读取命令行的输出到一个list
for line in info:  #按行遍历
    print(line)

time.sleep(10)

r = os.popen('/usr/local/go/bin/go run ./scatter_receiver.go')
info = r.readlines()  #读取命令行的输出到一个list
for line in info:  #按行遍历
    print(line)

time.sleep(10)

r = os.popen('/usr/local/go/bin/go run ./scatter_receiver.go')
info = r.readlines()  #读取命令行的输出到一个list
for line in info:  #按行遍历
    print(line)

time.sleep(10)

r = os.popen('/usr/local/go/bin/go run ./scatter_receiver.go')
info = r.readlines()  #读取命令行的输出到一个list
for line in info:  #按行遍历
    print(line)

time.sleep(10)

r = os.popen('/usr/local/go/bin/go run ./scatter_receiver.go')
info = r.readlines()  #读取命令行的输出到一个list
for line in info:  #按行遍历
    print(line)

time.sleep(10)

r = os.popen('/usr/local/go/bin/go run ./scatter_receiver.go')
info = r.readlines()  #读取命令行的输出到一个list
for line in info:  #按行遍历
    print(line)