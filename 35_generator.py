# Generators
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


