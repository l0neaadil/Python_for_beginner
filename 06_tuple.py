# Tuple
x = (5, 1, 6, 9, 3, 1)
y = (1, "m", 4, (2, 5))

print(x)
print(y.count(1))
z = x.count(1)
r = len(x)
print(z, r)

t = x + y                    # concatination
print(t)

q = ('hi',)*5                # hi is written 5 times
print(q)

a, b, c, d, e, f = x           # unpacking
print(a, '   ', e)
a, b, *c = x
print(a, '  ', b, '   ', c)
a, b, *_ = x
print(a, '  ', b)
a, b, *_, c = y
print(a, '  ', b, '  ', c)
a, *b, c = y
print(a, '  ', b, '  ', c)
