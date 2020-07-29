# Decorators
def decorator_x(func):
    def body():
        print('X' * 15)
        func()
        print('X' * 15)
    return body


def main_func():
    print('hello world')


hello = decorator_x(main_func)
hello()


# Simple_Method


def decorator_y(junk):
    def body():
        print('*' * 15)
        junk()
        print('*' * 15)
    return body


@ decorator_y
def main_func():
    print('hello world')


main_func()
