import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('localhost', 8888))
sock.connect(('', 8888))
message = time.time()
# sock.send(b"Test message")
sock.send(f"Time {message}".encode())
sock.close()
