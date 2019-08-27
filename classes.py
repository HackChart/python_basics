class UserInformation:
    name = "Austin"
    age = 24
    height = "6'0"
    weight = 195
    username = "HackChart"
    password = "tempPass"
    course = "Introduction to Python"

    # We can also override how our class initializes by defining __init__
    def __init__(self, name, username, password, **kwargs):
        self.name = name
        self.username = username
        self.password = password

        # To set attributes using kwargs, we need to iterate over the packed kwargs and split them into key value pairs
        for key, value in kwargs.items():
            # Then we use setattr to assign them to an attribute
            setattr(self, key, value)  # setattr( the object you want to set on, key, value)

    def praise(self):
        return "You're doing a great job, {}! Keep it up!".format(self.name)

    def assurance(self):
        return "Hey {}, you may want to go back and review that chapter again.".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        else:
            return self.assurance()


print(UserInformation.name)

# =========================================
# INHERITANCE
# =========================================


# You can inherit class attributes and methods from a parent class by specifing it in the class argument
class Parent:

    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def say_hello(self):
        print("Hello, world! This is a method inheritted from the parent class!")


class Child(Parent):  # By specifying Parent as an argument for Child, Child inherits all of parents info
    inheritance = True


# When create an instance of child, we have to specifiy a name, even though child doesnt require one on its own
# This is because it inherits the __init__ function from Parent, which requires this parameter
child_instance = Child("Child")
child_instance.say_hello()  # This instance of child also inherits all of the methods found in parent
