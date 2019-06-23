from multiprocessing import Process
from time import sleep,ctime

def tm():
	while True:
		sleep(2)
		print(ctime())		

p = Process(target = tm)

p.daemon = True	# 需在start前使用,且不和join共用

p.start()

sleep(5)
print('main process exit')