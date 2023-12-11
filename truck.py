import datetime
import itertools


class Truck:
    id_iter = itertools.count(1)

    # Constructor for a truck
    def __init__(self, time, location='4001 South 700 East', speed=18, mileage=0, capacity=16):
        self.id = next(self.id_iter)
        self.packages = []
        self.route = []
        self.time = time
        self.location = location
        self.speed = speed
        self.mileage = mileage
        self.capacity = capacity

    # Adds packages to the truck and checks capacity
    def load(self, packages):
        if len(packages) <= self.capacity:
            self.packages = packages
        else:
            print("This truck is full with 16 packages")
