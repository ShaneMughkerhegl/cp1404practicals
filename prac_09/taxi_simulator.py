from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0.0
    current_taxi = None

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive
>>> "
    choice = input(menu).lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (IndexError, ValueError):
                print("Invalid taxi choice")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                bill += trip_cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        choice = input(menu).lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

if __name__ == "__main__":
    main()
