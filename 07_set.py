# Sets
# a set contains unique elements only

a = {1, 9, 4, 5, 8, 1, 2, 9}
print(a, '\n', len(a))

a.add(15)
a.update({3, 25, 27, 29})
print(a)

a.remove(25)                     # if element is not present it will show error
a.discard(27)                    # if element is not present it will not show error
a.pop()
print(a)

a.clear()
print(a)

a = {1, 2, 3, 4, 5}
b = {5, 4, 6, 7, 8, 9}
c = a | b                                # union of a and b
d = a.union(b)                           # same as a | b
e = a & b                                # intersection of a and b
f = a.intersection(b)                    # same as a & b
print(a, b, '\n', c, d, '\n', e, f)

