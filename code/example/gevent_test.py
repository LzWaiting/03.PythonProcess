import gevent
from time import sleep

def foo(a,b):
	print('a = %d,b = %d'%(a,b))
	gevent.sleep(2)
	print('Running foo again')

def bar():
	print('Running int bar')
	gevent.sleep(3)
	print('Running bar again')

# 生成协程
f = gevent.spawn(foo,1,2)
b = gevent.spawn(bar)
print('--------')
gevent.joinall([f,b])
print('++++++++')