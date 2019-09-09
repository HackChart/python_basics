import math


# TODO: Define a class apple with four instance variables
class Apple:
    def __init__(self, color, weight, height, diameter):
        self.color = color
        self.weight = weight
        self.height = height
        self.diameter = diameter


# TODO: Create a circle class that has a method that returns area (use math module for pi)
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * math.pow(self.radius, 2)

    def change_radius(self):
        new_radius = input("Please enter the new radius:    ")
        self.radius = new_radius
        print("The radius has been changed.")


# TODO: Create a triangle class that has a method that returns area

# TODO: Create a hexagon class that has a method that returns perimeter


if __name__ == "__main__":
    apple1 = Apple("dark red", 10, 5, 3)
    print(apple1.color)
    print(apple1.weight)
    print(apple1.height)
    print(apple1.diameter)
    circle1 = Circle(3)
    print(circle1.calculate_area())
    print(circle1.radius)
    circle1.change_radius()
    print(circle1.radius)
