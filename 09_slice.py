# Slice()
string = '345678901'
list = [3, 4, 5, 6, 7, 8, 9, 0, 1]
tupple = (3, 4, 5, 6, 7, 8, 9, 0, 1)

x = slice(0, 4)
print(list[x], tupple[x], string[x])                          # ist method

print(list[2:5], tupple[2:5], string[2:5])                    # 2nd method
print(list[2:], tupple[2:], string[2:])                       # from given element to end
print(list[:5], tupple[:5], string[:5])                       # from beginning to given element

print(list[:], tupple[:], string[:])                          # copy of variable

print(list[0:9:3], tupple[2:8:1], string[3:6:1])              # step : cancels "step-1" steps in between
print(list[-9:-5], tupple[-5:-3], string[-3:-1])

print(list[::-1], tupple[::-1], string[::-1])                 # reverses the order
print(list[0:-1])
