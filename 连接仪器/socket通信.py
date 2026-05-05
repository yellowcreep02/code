import socket

tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

addr = ('192.168.1.44',8080)
tcp_client_socket.connect(addr)
tcp_client_socket.send('你好世界'.encode('GBK'))
tcp_client_socket.close()
