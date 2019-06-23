from socketserver import *

# 创建服务器类
class Server(ThreadingMixIn,UDPServer):	# 多线程并发
	pass

class Handler(DatagramRequestHandler):
	def handle(self):
		# print(self.client_address)	# 客户端地址
		# print(self.request)			# 消息和地址元组
		while True:
			data = self.rfile.readline()	# 接收信息
			if not data:
				break
			print(data.decode())
			self.wfile.write(b'Receive')	# 发送信息

if __name__ == '__main__':
	server_addr = ('0.0.0.0',8888)
	# 创建服务器对象
	server = Server(server_addr,Handler)
	# 启动服务器
	server.serve_forever()