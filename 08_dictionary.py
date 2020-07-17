# Dictionary
f = {'name': 'zahoor', 'age': 25, 'dsgn': 'student', 1: 2, (1, 2): 8}

print(f)
print(f[1])
print(f[(1, 2)])
print(f['age'])
print(f.get('dob'))
print(len(f))
f.pop(1)
print(f)

g = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

print(g[3])
print(len(f), len(g))
g[1] = 67                                 # replacing value of key
g[5] = 'y'                                  # adding new key_value pair
print(g)
print(f.keys(), "\n", g.values())

