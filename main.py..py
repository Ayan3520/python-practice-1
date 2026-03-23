customer_name = input("Enter customer name: ")
item1_name = input("Enter name of item 1: ")
item1_price = float(input("Enter price of item 1 (tenge): "))
item2_name = input("Enter name of item 2: ")
item2_price = float(input("Enter price of item 2 (tenge): "))
num_people = int(input("Enter number of people: "))

subtotal = item1_price + item2_price
tip = 0.10 * subtotal
total = subtotal + tip
per_person = total / num_people

print("=" * 30)
print("CAFE BILL")
print("-" * 30)
print(f"Customer: {customer_name}")
print(f"{item1_name}: {item1_price} tenge")
print(f"{item2_name}: {item2_price} tenge")
print(f"Subtotal: {subtotal} tenge")
print(f"Tip (10%): {tip} tenge")
print(f"Total: {total} tenge")
print(f"Per person: {per_person} tenge")
print("=" * 30)

print("Tip included:", tip > 0)
print("Bill over 5000 tenge:", total > 5000)
