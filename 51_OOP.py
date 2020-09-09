# Introduction
class Car:
    def __init__(self, speed, color, engine):
        self.speed = speed
        self.color = color
        self.engine = engine

    def vehicle(self):
        print(f'car is having powerful engine of: {self.engine} cc')


ford = Car(120, 'blue', 1100)
honda = Car(125, 'green', 1200)
audi = Car(130, 'yellow', 1300)

print(audi.engine)
audi.vehicle()
