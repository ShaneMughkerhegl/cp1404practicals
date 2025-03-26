# Import the Guitar class
from guitar import Guitar

# File containing guitar data
FILENAME = "guitars.csv"


# Main program function
def main():
    # Load guitars from file
    guitars = load_guitars(FILENAME)

    # Display all loaded guitars
    print("These are the guitars loaded:")
    display_guitars(guitars)

    # Ask the user to add new guitars
    print("\nAdd your own guitars!")
    guitars = add_new_guitars(guitars)

    # Sort guitars by year
    guitars.sort()

    # Display sorted guitars
    print("\nSorted guitars:")
    display_guitars(guitars)

    # Save all guitars to file
    save_guitars(FILENAME, guitars)


# Load guitars from the CSV file
def load_guitars(filename):
    guitars = []

    # Open the file for reading
    with open(filename, "r") as in_file:
        # Skip the header
        next(in_file)

        # Process each line
        for line in in_file:
            # Strip whitespace and split values
            parts = line.strip().split(',')

            # Extract data and convert types
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])

            # Create Guitar object and add to list
            guitars.append(Guitar(name, year, cost))

    # Return the list of guitars
    return guitars


# Display a list of Guitar objects
def display_guitars(guitars):
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


# Allow user to add new guitars
def add_new_guitars(guitars):
    while True:
        # Ask for name
        name = input("Name: ")

        # Blank name ends input
        if name == "":
            break

        # Ask for year and cost
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        # Create new guitar and add to list
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)

        # Confirm addition
        print(f"{new_guitar} added.\n")

    # Return updated list
    return guitars


# Save guitars back to CSV file
def save_guitars(filename, guitars):
    # Open the file for writing
    with open(filename, "w") as out_file:
        # Write header
        out_file.write("Name,Year,Cost\n")

        # Write each guitar as a line
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

    # Confirm save
    print(f"\nGuitars saved to {filename}")


# Run the program
if __name__ == "__main__":
    main()
