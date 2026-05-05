import socket

#1.创建socket对象
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2.为对象绑定ip与端口号
tcp_server_socket.bind(('127.0.0.1',5050))
#3.将对象设置为被动模式
tcp_server_socket.listen(128)
#4.等待客户端连接
tcp_client,tcp_addr = tcp_server_socket.accept()#连接时获取客户端连接对象以及连接信息
print('客户端新连接',tcp_addr)
#5.客户端接受数据
recv_data = tcp_client.recv(2048).decode()
print(recv_data)
#6.服务端回复数据
tcp_client.send('数据已接受'.encode())

#关闭客户端
tcp_client.close()
#关闭服务端
tcp_server_socket.close()