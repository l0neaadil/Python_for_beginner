# Global, Local and Non-Local variables


def func():
    x = 50
    print('1______', x)

    def inner():
        x = 100
        print('2_____', x)
    print('3______', x)
    inner()
    print("4_______", x)


x = 150
func()
print('5______', x)

