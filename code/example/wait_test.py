from multiprocessing import Event

# 创建事件对象
e = Event()

print(e.is_set())

e.wait(3)
e.set()
print(e.is_set())

e.clear()
print(e.is_set())