from multiprocessing import Process,Queue
import time

# 创建消息队列
q = Queue()

def fun1():
	time.sleep(1)
	q.put({'a':1,'b':2})

def fun2():
	time.sleep(2)
	print('收到消息:',q.get())

funs = [fun1,fun2]
jobs = []

for f in funs:
	p = Process(target=f)
	jobs.append(p)
	p.start()

for i in jobs:
	i.join()

q.close()