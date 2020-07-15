# Strings
a = "python for beginners..."
b = "beginner's python..."
c = 'BEGINNER"S PYTHON...\n'
d = "beginner\"s python..."
e = 'beginner\'s python...'
print(a, b, c, d, e)

msg = ''' Hi,
     Welcome to python for beginner's.
 Thanks'''
print(msg)

x = 11
y = 29
y = f'{x} and {y} are prime nos'
print(y)

print(a[0], b[1], c[2], d[-1], e[-6])
print(len(a), a.upper(), c.lower())
print(a, c)
print(e.find('t'), 'inn' in b, b.find('inn'))
print(c.replace('BEGINNER"S', 'ABSOLUTE BEGINNER"S'))
print(c)


