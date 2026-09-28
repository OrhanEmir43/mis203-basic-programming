item1_name = input("Enter name for Item 1: ")
item1_qty = int(input(f"Enter quantity for {item1_name}: "))
item1_price = float(input(f"Enter unit price for {item1_name}: $"))

item2_name = input("\nEnter name for Item 2: ")
item2_qty = int(input(f"Enter quantity for {item2_name}: "))
item2_price = float(input(f"Enter unit price for {item2_name}: $"))

delivery_fee = float(input("\nEnter delivery fee: $"))
tax_percent = float(input("Enter tax percentage: $")

line1_total = item1_qty * item1_price
line2_total = item2_qty * item2_price

subtotal = line1_total + line2_total
tax_amount = subtotal * (tax_percent / 100)
final_total = subtotal + tax_amount + delivery_fee

print("\n" + "=" * 40)
print(f"{'INVOICE RECEIPT':^40}")
print("=" * 40)
print(f"{item1_name:<18} {item1_qty:>2} x ${item1_price:>6.2f} = ${line1_total:>8.2f}")
print(f"{item2_name:<18} {item2_qty:>2} x ${item2_price:>6.2f} = ${line2_total:>8.2f}")
print("-" * 40)
print(f"{'Subtotal:':<29} ${subtotal:>8.2f}")
print(f"{f'Tax ({tax_percent}%):':<29} ${tax_amount:>8.2f}")
print(f"{'Delivery Fee:':<29} ${delivery_fee:>8.2f}")
print("-" * 40)
print(f"{'Final Total:':<29} ${final_total:>8.2f}")
print("=" * 40)
