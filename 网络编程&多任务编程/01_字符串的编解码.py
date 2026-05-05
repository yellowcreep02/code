import socket
#创建并配置socket对象
set_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
set_socket.connect(('127.0.0.1',5050))
#发送数据
set_socket.send('helloyellow'.encode())
#接受数据,代码阻塞直到服务器回复消息后自动释放阻塞
recv_data = set_socket.recv(2048)
print('接受结束',recv_data.decode('utf-8'))
set_socket.close()


