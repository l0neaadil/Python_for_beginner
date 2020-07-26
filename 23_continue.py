# Continue
list = [2, 3, 4, 5, 6, 7, 8]
for element in list:
    if element == 7:
        continue
    print(element)

print("-------0-0------")

"""
i = 4
while i < 10:                           # this time continue will act infinite times
    if i == 7:
        continue
    print(i)
    i += 1
"""

print("-------0-0-------")

j = 4
while j < 10:                           # this time continue will act not as break
    j += 1
    if j == 7:
        continue
    print(j)
