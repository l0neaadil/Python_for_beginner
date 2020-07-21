# For Loop
string = "3456789"
list = [3, 4, 5, 6, 7, 8, 9]
tuple = (3, 4, 5, 6, 7, 8, 9)
set = {3, 4, 5, 6, 7, 8, 9}
dictionary = {1: 'a', 2: 'b', 3: 'c'}

print(string, list, tuple, set, dictionary)

for element in string:
    print(element)
for element in list:
    print(element)
for element in tuple:
    print(element)
for element in set:
    print(element)

for element in dictionary.keys():
    print(element)
for element in dictionary.values():
    print(element)


for element in range(0, 31, 2):
    print(element % 2)
    print(element / 2)
