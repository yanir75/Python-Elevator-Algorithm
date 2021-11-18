import Elevator


class Building:

    def __init__(self, elevators):
        self.maxFloor = elevators[0].maxFloor
        self.elevators = elevators
        self.minFloor = elevators[0].minFloor
        self.total = sum([i.speed for i in self.elevators])
        for i in elevators:
            i.perc = i.speed/self.total*100

    def sort_by_speed(self):
        self.elevators.sort(reverse=True,key=lambda x: x.speed)

    def to_string(self):
        return str(self.elevators)
