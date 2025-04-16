from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Hummer", 200, 4)
taxi.drive(18)
fare = taxi.get_fare()
print(f"Fare for 18km: ${fare:.2f}")
assert round(fare, 2) == 48.8, "Fare should be $48.80"
