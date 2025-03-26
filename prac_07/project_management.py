# Import the Project class and datetime module
from project import Project
import datetime

# Default data file
FILENAME = "projects.txt"


# Main program function
def main():
    # Load projects from default file
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    # Display menu options
    while True:
        print_menu()
        choice = input(">>> ").lower()

        # Quit the program
        if choice == 'q':
            # Ask to save before quitting
            if input(f"Would you like to save to {FILENAME}? ").lower() in ['y', 'yes']:
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
            break

        # Load from a new file
        elif choice == 'l':
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)

        # Save to a new file
        elif choice == 's':
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)

        # Display incomplete and complete projects
        elif choice == 'd':
            display_projects(projects)

        # Filter projects by date
        elif choice == 'f':
            filter_by_date(projects)

        # Add a new project
        elif choice == 'a':
            new_project = add_project()
            projects.append(new_project)

        # Update an existing project
        elif choice == 'u':
            update_project(projects)

        # Handle invalid choice
        else:
            print("Invalid option")


# Display menu options
def print_menu():
    print("- (L)oad projects  ")
    print("- (S)ave projects  ")
    print("- (D)isplay projects  ")
    print("- (F)ilter projects by date")
    print("- (A)dd new project  ")
    print("- (U)pdate project")
    print("- (Q)uit")


# Load projects from a file
def load_projects(filename):
    projects = []

    # Open the file for reading
    with open(filename, "r") as in_file:
        next(in_file)  # Skip header

        # Read each line and create a Project object
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)

    return projects


# Save projects to a file
def save_projects(filename, projects):
    with open(filename, "w") as out_file:
        # Write header
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")

        # Write each project using its save string
        for project in projects:
            out_file.write(project.to_save_string() + "\n")

    print(f"Projects saved to {filename}")


# Display incomplete and complete projects sorted by priority
def display_projects(projects):
    # Sort projects by priority
    projects.sort()

    # Separate incomplete and complete
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")

    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


# Filter projects that start after a given date
def filter_by_date(projects):
    # Get date input from user
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    # Filter and sort by start date
    filtered = [p for p in projects if p.start_date > date]
    filtered.sort(key=lambda p: p.start_date)

    # Display filtered projects
    for p in filtered:
        print(p)


# Add a new project from user input
def add_project():
    print("Let's add a new project")

    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    return Project(name, start_date, priority, cost_estimate, completion)


# Update a selected project
def update_project(projects):
    # Show all projects with indexes
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    # Let user select a project
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)

    # Ask for new completion %
    new_completion = input("New Percentage: ")
    if new_completion != "":
        project.completion_percentage = int(new_completion)

    # Ask for new priority
    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)


# Run the program
if __name__ == "__main__":
    main()
