import socket

url = 'example.com'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((url, 80))
content_items = [
    'GET / HTTP/1.1',
    f'Host: {url}',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(content_items)
print('--- HTTP MESSAGE ---')
print(content)
print('=== END OF MESSAGE ===')
sock.send(content.encode())
result = sock.recv(2**11)
print(result.decode())
