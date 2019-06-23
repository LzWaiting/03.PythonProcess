import threading
from time import sleep
import os

a = 1

# 线程函数
def music():
	global a
	print("Thread a =",a)
	a = 10000
	for i in range(5):
		sleep(1)
		print("播放音乐",os.getpid())

# 创建线程对象
t = threading.Thread(target=music)
t.start()

for i in range(5):
	sleep(1.5)
	print('想听灌篮高手',os.getpid())
	
t.join()

print("main Thread a =",a)