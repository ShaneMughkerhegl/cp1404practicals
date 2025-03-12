# subject_reader.py

def main():
    """Read subject data and display formatted information."""
    data = load_data("subject_data.txt")
    display_subject_details(data)

def load_data(filename):
    """Load data from file and return as a nested list."""
    subjects = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            parts[2] = int(parts[2])  # Convert student count to int
            subjects.append(parts)
    return subjects

def display_subject_details(subjects):
    """Display subject details in a formatted way."""
    for subject in subjects:
        code, lecturer, students = subject
        print(f"{code} is taught by {lecturer} and has {students} students")

if __name__ == "__main__":
    main()