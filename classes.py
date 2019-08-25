class UserInformation:
    name = "Austin"
    age = 24
    height = "6'0"
    weight = 195
    username = "HackChart"
    password = "tempPass"
    course = "Introduction to Python"

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