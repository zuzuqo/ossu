import socket


def parse_http_response(text_response):
    lines = text_response.split('\n')
    status_raw, lines = lines[0], lines[1:]
    protocol, status_code, message = status_raw.split(' ')
    empty_index = 1
    headers = {}
    for index, line in enumerate(lines):
        line = line.strip()
        line = line.strip('\r')
        if line == '':
            empty_index = index
            break
        print(line)
        k, _, v = line.partition(':')
        headers.setdefault(k.strip(), v.strip())
    response_content = ''.join(lines[empty_index + 1:])
    return int(status_code), headers, response_content


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
result = sock.recv(2 ** 11)
status_code, headers, content = parse_http_response(result.decode())
print(f'Status Code: {status_code}')
print(f'Headers: {headers}')
print(f'Content: {content}')
# print(result.decode())
