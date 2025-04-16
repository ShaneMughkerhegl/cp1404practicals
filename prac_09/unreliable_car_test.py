from unreliable_car import UnreliableCar

car = UnreliableCar("Old Bomb", 100, 50)
distances = [car.drive(10) for _ in range(100)]
print(f"Drove {sum(distances)} km in 100 attempts")
