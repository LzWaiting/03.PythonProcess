from threading import Thread
from time import sleep,ctime

class myThread(Thread):
	def __init__(self,target,name="myThread1",args=(),kwargs={}):
		super().__init__()
		self.name = name
		self.target = target
		self.args = args
		self.kwargs = kwargs
		
	def run(self):
		self.target(*self.args,**self.kwargs)

def player(song,sec):
	for i in range(2):
		print("Playing %s:%s"%(song,ctime()))
		sleep(sec)

t = myThread(target=player,\
	args=('世上只有妈妈好',),kwargs={'sec':2})

t.start()
t.join()