# Function
def sum(arg1, arg2):
    if type(arg1) != type(arg2):
        print("error")
        return
    print(arg1 + arg2)


sum(15, 14)
sum(0.4, 0.6)
sum(0.4, 7)
sum("hello  ", "world")
sum("hello", 15)

print('------0-0------')


def std(name, age):
    print('Student\'s name is: ', name)
    print('Student\'s age is: ', age)


std(1234, 10)
std('lone', 7)

print('------0-0-------')


def student(name='not entered', age=0):
    print('Student\'s name is: ', name)
    print('Student\'s age is: ', age)


student('abcd', 10)
student()


