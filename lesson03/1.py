class Geometry_figure:

    def ploshad(self):
        raise NotImplementedError("Метод должен быть переопределен в дочернем классе")

class Rectangle(Geometry_figure):
    def __init__(self, lenght, height):
        self.lenght = lenght
        self.height = height

    def ploshad(self):
        return self.lenght * self.height

class Circle(Geometry_figure):
    def __init__(self, radius):
        self.radius = radius

    def ploshad(self):
        return 3.14 * self.radius**2

class Rhomb(Geometry_figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def ploshad(self):
        return self.base * self.height

rectangle = Rectangle(2, 10)
print(f"Площадь прямоугольника = {rectangle.ploshad()} см^2")

circle = Circle(5)
print(f"Площадь круга = {circle.ploshad()} см^2")

rhomb = Rhomb(2, 4)
print(f"Площадь ромба = {rhomb.ploshad()}")

try:
    figure = Geometry_figure()
    figure.ploshad()
except NotImplementedError as e:
    print(f"ошибка: {e}")
