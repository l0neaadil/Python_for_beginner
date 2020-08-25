# String to Bytes:
result = 'hello world'

output = b'hello world'
print(output)
print(type(output))

output = result.encode('utf-8')
print(output)
print(type(output))

output = bytes(result, 'utf-8')
print(output)
print(type(output))


