import os
from multiprocessing import Process

filename = './send.jpg'
# 获取文件大小
size = os.path.getsize(filename)

# 如果子进程使用父进程的对象,那么相互之间有偏移量的影响
# f = open(filename,'rb')

# 复制前半部分
def copy1():
	f = open(filename,'rb')
	fw = open('copy1.jpg','wb')
	n = size // 2
	while True:
		if n < 1024:
			msg = f.read(n)
			fw.write(msg)
			break
		msg = f.read(1024)
		fw.write(msg)
		n -= 1024
	f.close()
	fw.close()

# 复制后半部分
def copy2():
	f = open(filename,'rb')
	fw = open('copy2.jpg','wb')
	n = size // 2
	f.seek(n,0)
	while True:
		msg = f.read(1024)
		if not msg:
			break
		fw.write(msg)
	f.close()
	fw.close()

things = [copy1,copy2]
process = []

for th in things:
	p = Process(target=th)
	p.start()
	process.append(p)

for i in process:
	i.join()

