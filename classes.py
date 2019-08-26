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
