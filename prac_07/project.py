# Import the datetime module to work with dates
import datetime


class Project:
    # Initialise a Project with name, start date, priority, cost estimate and completion %
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    # Define how to display a project
    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, " \
               f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, " \
               f"completion: {self.completion_percentage}%"

    # Define how to compare projects (used for sorting by priority)
    def __lt__(self, other):
        return self.priority < other.priority

    # Check if the project is complete
    def is_complete(self):
        return self.completion_percentage == 100

    # Return a tab-delimited string for saving to file
    def to_save_string(self):
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}" \
               f"\t{self.cost_estimate}\t{self.completion_percentage}"
