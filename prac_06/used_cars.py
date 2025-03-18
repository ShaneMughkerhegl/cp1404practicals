def main(): # Demonstrates the usage of the Car class.
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Limo fuel level: {limo.fuel}")
    limo.drive(115)
    print(limo)

if __name__ == "__main__":
    main()