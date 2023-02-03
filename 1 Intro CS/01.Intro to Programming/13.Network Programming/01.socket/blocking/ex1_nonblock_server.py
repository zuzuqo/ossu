import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8888))
sock.listen(5)
sock.setblocking(False)

client, addr = sock.accept()
result = client.recv(1024)
client.close()

print(f"Message {result.decode('utf-8')}")
