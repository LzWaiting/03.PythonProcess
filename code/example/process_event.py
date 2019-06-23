from multiprocessing import Event,Process
from time import sleep

def wait_event():
	print('想操作临界区')
	e.wait()
	print('开始操作临界区资源',e.is_set())
	with open('file') as f:
		print(f.read())

# 超时阻塞,控制临界资源的操作
def wait_event_timeout():
	print('想操作临界区')
	e.wait(2)
	if e.is_set():
		with open('file') as f:
			print(f.read())
	else:
		print('不能读取文件')

e = Event()
p1 = Process(target=wait_event)
p2 = Process(target=wait_event_timeout)

p1.start()
p2.start()

print('主进程操作')
with open('file','w') as f:
	sleep(3)
	f.write("I love China")
e.set()
print('释放临界区')

p1.join()
p2.join()