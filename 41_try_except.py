# try_except_else_finally
# Zero Division / value Error

result = None
try:
    a = int(input("Enter a no. "))
    b = int(input("Enter a no. "))
    result = a / b
except Exception as e:
    print('error: ', e, ': ', type(e))
else:
    print('code has no error')
finally:
    print('result = ', result)
    print('press  restart')
