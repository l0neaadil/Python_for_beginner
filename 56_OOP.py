class Parent1:
    def __init__(self, name1):
        print('hello1', name1)


class Parent2:
    def __init__(self, name2):
        print('hello2', name2)


class Child(Parent1, Parent2):
    def __init__(self):
        print('hello3')
        print(Child.__mro__)
        Parent2.__init__(self, 'gani')
        Parent1.__init__(self, 'lone')


Child()
