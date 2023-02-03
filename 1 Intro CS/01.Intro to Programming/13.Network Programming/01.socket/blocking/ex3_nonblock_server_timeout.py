import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8888))
sock.listen(5)
# sock.setblocking(True)
sock.settimeout(5)          # -> set.blocking(True) after 5sec
sock.settimeout(0)          # -> set.blocking(False)
sock.settimeout(None)       # -> set.blocking(True)

try:
    client, addr = sock.accept()
except socket.error:
    print('no connections')
else:
    result = client.recv(1024)
    client.close()
    print(f"Message {result.decode('utf-8')}")
