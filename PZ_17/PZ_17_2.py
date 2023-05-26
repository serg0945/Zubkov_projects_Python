import math


# Родительский (супер) класс

class Figure:
    def __init__(self):  # Инициализация экземпляря класса
        pass

    def square(self):
        pass

    def perimetr(self):
        pass


# Классы Square, Rectangle и Circle - подклассы (дочерние классы)

# Определение площади и периметра Квадрата

class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def square(self):
        return self.side ** 2

    def perimetr(self):
        return self.side * 4


# Определение площади и периметра Прямоугольника

class Rectangle(Figure):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimetr(self):
        return (self.width + self.height) * 2


# Определение площади и периметра Круга

class Circle(Figure):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def square(self):
        return (self.radius ** 2) * math.pi

    def perimetr(self):
        return 2 * math.pi * self.radius


a = Circle(2)
print(a.square())
