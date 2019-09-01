# Create a class method in Letter named from_string that takes a string like "dash-dot"
# and creates an instance with the correct pattern (['_', '.']).


class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __iter__(self):
        yield from self.pattern

    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

# TODO: Find a way to iterate through a single string that seperates values
    @classmethod
    def from_string(cls, user_string):
        morse_list = []
        user_string = user_string.split('-')
        for item in user_string:
            if item == "dash":
                morse_list.append("_")
            elif item == "dot":
                morse_list.append(".")
            else:
                continue
        return cls(pattern=morse_list)
        # TODO: Return value to pattern (create an instance of Letter)


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)