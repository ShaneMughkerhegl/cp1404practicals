def get_password(min_length):
    password = input("Enter your password: ")

    while len(password) < min_length:
        print("Error: Password is too short.")
        password = input("Enter your password: ")

    return password

def print_asterisks(password):  # This is the new function that prints asterisks
    print("Password entered: " + "*" * len(password))

def main():
    min_length = 8  # Minimum length for the password
    password = get_password(min_length)

    print_asterisks(password)  # Calling the new print_asterisks function

    print("Success: Password is long enough.")

main()
