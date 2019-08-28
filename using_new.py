# IDE raises an error, but the code runs
# Use new on immutable objects, init on mutatable objs
class Double(int):
    def __new__(*args, **kwargs):  # DOES NOT NEED SELF
        cls = int.__new__(*args, **kwargs)  # Safer to use __new__ than super
        return cls * 2  # Can return a value, unlike __init__


print(Double(5))


