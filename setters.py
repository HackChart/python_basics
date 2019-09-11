class Product:
    __price = 0.0
    tax_rate = 0.12

    def __init__(self, base_price):
        self.__price = base_price

    @property
    def price(self):
        return self.__price + (self.__price * self.tax_rate)

    @price.setter
    def price(self, price):
        self.__price = price


class Circle:
    def __init__(self, diameter):
        self.diameter = diameter  # By using only one attr, we always keep radius and diameter coherent with each other

    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2


if __name__ == "__main__":
    apple = Product(1)
    print(apple.price)
    dir(Product)
    apple.price = 4
    print("The value of the __price attribute is now {}".format(apple._Product__price))
    print(apple.price)
    circle = Circle(10)
    print(circle.diameter)
    print(circle.radius)
    circle.radius = 4
    print("The new value of the radius is {}".format(circle.radius))
    print("The new value of the diamter is {}".format(circle.diameter))