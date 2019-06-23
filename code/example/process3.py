from multiprocessing import Process
from time import sleep

# 带参数的进程函数
def worker(sec,name):
	for i in range(3):
		sleep(sec)
		print("I'm %s"%name)
		print("I'm working...")

p = Process(target=worker,args=(2,),\
	kwargs={'name':'Jam'},name='worker')
p.start()

print('Process name:',p.name)# 获取进程名称
print('Process PID:',p.pid)# 获取进程PID号

print('Process is alive:',p.is_alive())

p.join(3)
print('Process is alive:',p.is_alive())