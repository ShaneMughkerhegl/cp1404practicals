# list_exercises.py

# Basic list operations

def main():
    """Get user input for five numbers and display various statistics."""
    numbers = []
    for i in range(5):
        number = int(input(f"Number {i + 1}: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")


# Woefully inadequate security checker

def check_username():
    """Check if username is in the authorized list."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    user = input("Enter username: ")
    if user in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()
    check_username()