# files

# Method 1

file = open('Demo1.txt', 'w')
for i in range(1, 8):
    file.write('This is line no %d\n' % i)
file.close()

# Method 2

with open('Demo2.txt', 'w') as file:
    for i in range(1, 8):
        file.write('This is line no %d\n' % i)
