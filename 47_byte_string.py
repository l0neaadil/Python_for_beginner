# String to Bytes:
string = 'hello world'

output = b'hello world'
print(output)
print(type(output))

output = string.encode('utf-8')
print(output)
print(type(output))

output = bytes(string, 'utf-8')
print(output)
print(type(output))


