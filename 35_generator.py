# Generators
# Any function that contains a yield keyword is termed as generator.
# yield is used to return from a function without destroying the state of its local variables. 


# # Part_1
# def my_func():
#     yield 'a'
#     yield 'b'
#     yield 'c'
#
#
# x = my_func()
# print(next(x))
# print(next(x))

# Part_2


def test():
    n = 1
    print('_____', n, '______')
    yield n
    n += 1
    print('_____', n, '______')
    yield n
    n += 1
    print('_____', n, '______')
    yield n


x = test()
print(next(x))
print(next(x))
print(next(x))


