# inheritance
class Polygon:

    def set_values(self, width, height):
        self.width = width
        self.height = height


class Rectangle(Polygon):
    def area(self):
        return self.width * self.height


class Triangle(Polygon):
    def area(self):
        return self.width * self.height / 2


rect = Rectangle()
tri = Triangle()
rect.set_values(int(input("enter length  ")), int(input('now breadth  ')))
tri.set_values(50, 30)
print(rect.area())
print(tri.area())
