# Decorators part_2
def decorator_x(func):
    def body():
        print('X' * 15)
        func()
        print('X' * 15)
    return body


def decorator_y(func):
    def body():
        print('*' * 15)
        func()
        print('*' * 15)
    return body


@decorator_x
@decorator_y         # decorator_x(decorator_y(main_func))
def main_func():
    print('hello world')


main_func()

# hello = decorator_x(decorator_y(main_func))
# hello()



