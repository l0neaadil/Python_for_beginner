# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.
# syntax:   string.split(separator)

string = "hello, my name is Lone,/ I am 26 years old"

x = string.split()              # default separator is any whitespace    
print(x)

x = string.split(" ")
print(x)

x = string.split(", ")
print(x)

x = string.split("/ ")
print(x)



# The strip() method strips (removes) leading and trailing characters from a string.
# Syntax:    string.strip(characters)

string = '  3# hello world * '
print(string.strip())           # default characters are any whitespace
print(string.strip(' '))
print(string.strip(' 3#*'))
