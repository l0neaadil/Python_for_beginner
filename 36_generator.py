# Generators
def my_generator():
    for i in range(1, 5):
        print('______', i, '_______')
        yield i


x = my_generator()
print(next(x))
next(x)
print(next(x))
next(x)
