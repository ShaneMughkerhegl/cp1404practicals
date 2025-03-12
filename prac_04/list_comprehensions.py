# list_comprehensions.py

def main():
    """Demonstrate list comprehensions."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # TODO: Write list comprehensions
    squared_numbers = [n ** 2 for n in numbers]
    print(f"Squared numbers: {squared_numbers}")

    even_numbers = [n for n in numbers if n % 2 == 0]
    print(f"Even numbers: {even_numbers}")

    numbers_plus_ten = [n + 10 for n in numbers]
    print(f"Numbers plus ten: {numbers_plus_ten}")


if __name__ == "__main__":
    main()