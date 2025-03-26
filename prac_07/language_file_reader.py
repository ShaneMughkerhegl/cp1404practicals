# Import the ProgrammingLanguage class from the other file
from programming_language import ProgrammingLanguage

# File containing language data
FILENAME = "languages.csv"


# Main function to run the program
def main():
    # Load languages from CSV
    languages = load_languages(FILENAME)

    # Print each language object
    for language in languages:
        print(language)


# Load programming languages from a CSV file
def load_languages(filename):
    languages = []

    # Open the file for reading
    with open(filename, "r") as in_file:
        # Skip the header line
        next(in_file)

        # Read each line and convert into a ProgrammingLanguage object
        for line in in_file:
            # Remove whitespace and split line into parts
            parts = line.strip().split(',')

            # Extract values and convert types
            name = parts[0]
            typing = parts[1]
            reflection = parts[2].lower() == 'true'
            year = int(parts[3])
            pointer_arithmetic = parts[4].lower() == 'true'

            # Create the ProgrammingLanguage object
            language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)

            # Add to the list
            languages.append(language)

    # Return the completed list
    return languages


# Run the program if this file is executed
if __name__ == "__main__":
    main()
