class Guitar: # Represents a guitar with name, year, and cost.

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self): # Returns the age of the guitar.
        return 2024 - self.year

    def is_vintage(self): # Checks if the guitar is vintage (50+ years old).
        return self.get_age() >= 50

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"