# List and operations on a list
x = [6, 2, 9, 5, 1, 0, 3]
y = ['w', 'r', 1, 4, [1, 2, 'h']]
print(x, y, '\n \t concat:', x + y)

print(y[3])
print(y[4])
print(len(x), len(y))

x.insert(2, y)
y.insert(4, 0)
print(x, y)
x.append(99)                 # push function

x.remove(2)                  # deletes 2 if present in list
y.remove(4)
print(x, y)
x.pop()                      # deletes last item
print(x, y)

y.clear()                    # removes all values of y
print(x, y)
g = [1, 9, 2, 8, 4, 7]
g.sort()
print(g)
print(g[::-1])
g.reverse()
print(g)
t = g
e =g.copy()
print(t, e)

g.append('copy')
print(g, t, e)

e.append(4)
e.append(4)
print(e.count(4))             # counts no of 4's in e
print(e)
