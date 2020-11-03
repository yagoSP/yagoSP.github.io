import socket

ip = '0.0.0.0'
port= '666'

server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.blind((ip, port))

server.listen(10)
print('server on: {} , {}' .format(ip, port))
server.accept()
