from urllib import request

url = 'http://example.com'

response = request.urlopen(url)

print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)
# заголовки в виде внутреннего объекта
print(response.headers)
# словарь всех заголовков
print(response.getheaders())
# получение заголовка
print(response.headers.get('Content-Type'))
print(response.getheader('Content-Type'))
