# Lambda
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

# def double(x):
#     return 2 * x
# def add(x, y):
#     return x + y
# def product(x, y, z):
#     return x * y * z

double = lambda x: 2 * x
add = lambda x, y: x + y
product = lambda x, y, z: x * y * z
print(double(10))
print(add(10, 20))
print(product(10, 20, 30))
