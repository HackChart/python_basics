import math


# Define a class apple with four instance variables
class Apple:
    def __init__(self, color, weight, height, diameter):
        self.color = color
        self.weight = weight
        self.height = height
        self.diameter = diameter


# Create a circle class that has a method that returns area (use math module for pi)
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * math.pow(self.radius, 2)

    @property
    def diameter(self):
        return self.radius * 2

    def change_radius(self):
        new_radius = input("Please enter the new radius:    ")
        self.radius = new_radius
        print("The radius has been changed.")


# Create a triangle class that has a method that returns area
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @property
    def area(self):
        return (self.base * self.height) / 2


# Create a hexagon class that has a method that returns perimeter
class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    @property
    def perimeter(self):
        return self.side_length * 6


if __name__ == "__main__":
    apple1 = Apple("dark red", 10, 5, 3)
    print(apple1.color)
    print(apple1.weight)
    print(apple1.height)
    print(apple1.diameter)
    circle1 = Circle(3)
    print(circle1.area)
    print(circle1.radius)
    circle1.change_radius()
    print(circle1.radius)
    triangle = Triangle(3, 6)
    print("The base of the triangle is {}".format(triangle.base))
    print("The height of the triange is {}".format(triangle.height))
    print("The area of the triangle is {}".format(triangle.area))
    hexagon = Hexagon(3)
    print("The perimeter of the hexagon is {}".format(hexagon.perimeter))
