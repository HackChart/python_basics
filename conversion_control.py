# We can control the way that our classes are converted with magic methods
# It is important to add built in magic methods to our own objects so that others can use them easily


class Character:
    # Defines how the class is initialized
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    # Defines how the class looks if converted to a string
    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.name)  # Will show as ClassName: InstanceName

    # Defines how the class would look if converted to an int
    def __int__(self):
        return 1  # Not verty useful in this case, since our class doesn't hold an nums as str

    # Defines how the class would look if converted to a float
    def __float__(self):
        return 1.0  # Returns 1 as if to say the instance exists


class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value

    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.value = self * other
        return self.value
