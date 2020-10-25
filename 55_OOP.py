# Super
class Parent:
    def __init__(self, name):
        print('hello1', name)


class Child(Parent):
    def __init__(self):
        print('hello2')
        super() .__init__('mac')


child1 = Child()

# Note: 
# The __init__() function is called automatically every time the class 
# is being used to create a new object.
# When you add the __init__() function, the child class will no longer 
# inherit the parent's __init__() function. The child's __init__() function
# overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, we used
# super() function.
