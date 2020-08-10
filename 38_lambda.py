# Lambda, Map & Filter
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 0]
a = map(lambda x: x * 2, list1)
b = map(lambda x: x ** 2, list2)
print(list(a))
print(list(b))
c = map(lambda x, y: x + y, list1, list2)
print(list(c))
d = filter(lambda x: True if x > 3 else False, list1)
print(list(d))
