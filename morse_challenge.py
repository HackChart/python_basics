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
    # TODO: Look into unjoining a string
    @classmethod
    def from_string(cls, user_string):
        morse_list = []
        if "dash" in user_string:
            morse_list.append('_')
        # TODO: Return value to pattern (create an instance of Letter)





class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.']
        super().__init__(pattern)