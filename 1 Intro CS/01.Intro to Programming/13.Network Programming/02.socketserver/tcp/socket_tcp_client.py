import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8888))

sock.send(f"Time {time.time()}".encode())
sock.close()
