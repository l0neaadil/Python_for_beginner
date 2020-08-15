# Files_2


file = open('Demo1.txt', 'r')
print(file.read())                # reads the whole file
print(file.read(32))               # reads all the first n characters
print(file.readline())              # reads line
print(file.readline())
print(file.readlines())             # reads all lines
print(file.readlines()[3])           # prints line no 4
for line in file:
    print(len(line))
    print('no of words:', len(line.split(' ')))
file.close()
