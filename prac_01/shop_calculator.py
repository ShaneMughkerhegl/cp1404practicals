
# shop_calculator.py
num_items = int(input("Number of items: "))
while num_items < 0:
   print("Invalid number of items!")
   num_items = int(input("Number of items: "))
total_price = sum(float(input("Price of item: ")) for _ in range(num_items))
if total_price > 100:
   total_price *= 0.9
print(f"Total price for {num_items} items is ${total_price:.2f}")
