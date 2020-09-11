# Encapsulation
class Car:
    def __init__(self, speed, power, color):
        self.__speed = speed
        self.__color = color
        self.__power = power

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_power(self, value):
        self.__power = value

    def get_power(self):
        return self.__power

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color


ford = Car(100, 50, 'blue')
audi = Car(110, 51, 'green')

print(ford.get_speed(), ford.get_color(), ford.get_power())
ford.set_speed(140)
print(ford.get_speed())
