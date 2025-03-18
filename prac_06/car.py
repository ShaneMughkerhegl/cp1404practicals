class Car: # Represents a car with fuel capacity, odometer reading, and name.

    def __init__(self, name, fuel=0): # Initializes a Car instance.
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount): # Adds fuel to the car.
        self.fuel += amount

    def drive(self, distance): # Drives the car a certain distance if enough fuel is available.
        if distance > self.fuel:
            distance = self.fuel  # Can only drive as far as fuel allows
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self): # Returns a string representation of the car.
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"