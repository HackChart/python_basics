# I want you to add a __str__ method to the Letter class that loops through the pattern attribute of an instance
# and returns "dot" for every "." (period) and "dash" for every "_" (underscore). Join them with a hyphen.
# I've included an S class as an example (I'll generate the others when I test your code) and it's __str__
# output should be "dot-dot-dot".


class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        morse = []
        for item in self.pattern:
            if item == ".":
                morse.append("dot")
            elif item == "_":
                morse.append("dash")
            else:
                continue
        return "-".join(morse)

    def __iter__(self):
        yield from self.pattern

    def __contains__(self, item):
        return item in self.pattern


class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.', 'a', '_', '_']
        super().__init__(pattern)


if __name__ == "__main__":
    test_pattern = S()
    print(test_pattern)
    print(str(test_pattern))