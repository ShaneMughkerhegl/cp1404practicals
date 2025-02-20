import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.00
INITIAL_PRICE = 10.00
FILENAME = "stock_simulation_output.txt"

# Open file for writing
out_file = open(FILENAME, 'w')

# Variables
price = INITIAL_PRICE
number_of_days = 0

# Write the starting price to the file
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate the stock price changes
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    price_change = 0
    # 50% chance to increase or decrease the price
    if random.randint(1, 2) == 1:
        # Price increases by a random value between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Price decreases by a random value between 0 and MAX_DECREASE
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    # Output the price for the current day to the file
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file after the loop ends
out_file.close()
