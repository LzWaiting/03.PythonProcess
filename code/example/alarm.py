import signal
import time

signal.alarm(3)	# 异步执行函数
time.sleep(2)
signal.alarm(5) # 覆盖第一个alarm时间

signal.pause()	# 阻塞等待信号

while True:
	time.sleep(1)
	print('等待时钟信号...')