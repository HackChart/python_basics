
class RaceCar:
    # We can define attributes here, but if we change the value here, it will affect all instances
    # even those that have already been created. To prevent this, we can move this attr inside init
    # laps = 0

    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = 0

        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining -= length * 0.125
        self.laps += 1


