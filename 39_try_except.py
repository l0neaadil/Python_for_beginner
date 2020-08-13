# Zero Division Error

# part 1

result = ''
print(type(result))
a = int(input("Enter a no. "))
b = int(input("Enter a no. "))
try:
    result = a / b
except:
    print('error has occured')
print('result = ', result)
print('the end')


# part2:


result = None
print(type(result))
a = int(input("Enter a no. "))
b = int(input("Enter a no. "))
try:
    result = a / b
except Exception as e:
    print('error: ', e, ': ', type(e))
print('result = ', result)
print('the end')
