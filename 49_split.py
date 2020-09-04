# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace

string = "hello, my name is Lone,/ I am 26 years old"

x = string.split()              # default separator is any whitespace    
print(x)

x = string.split(" ")
print(x)

x = string.split(", ")
print(x)

x = string.split("/ ")
print(x)
