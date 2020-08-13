# Type Error

result = None
a = input("Enter something ")
b = int(input("Enter a no. "))
try:
    result = a/b
except Exception as e:
    print('error: ', type(e))
print('result = ', result)
print('the end')

