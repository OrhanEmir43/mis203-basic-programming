tickets_sold = 0
total_revenue = 0.0
free_tickets = 0

while True:
    customer_name = input("Customer name (or q to quit): ").strip()
    if customer_name.lower() == 'q':
        break

    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age.")
        continue

    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    day = input("Day (weekday/weekend): ").strip().lower()
    if day not in ['weekday', 'weekend']:
        print("Invalid day.")
        continue

    student_input = input("Student (yes/no): ").strip().lower()
    if student_input not in ['yes', 'no']:
        print("Please answer yes or no.")
        continue

    is_student = (student_input == 'yes')

    
    base_price = 200.0 if day == 'weekday' else 250.0


    if age < 7:
        discount = 1.00
        category = "Free"
    elif age >= 65:
        discount = 0.50
        category = "Senior"
    elif 7 <= age <= 13:
        discount = 0.40
        category = "Child"
    elif is_student and age <= 26:
        discount = 0.30
        category = "Student"
    else:
        discount = 0.0
        category = "Standard"

    final_price = base_price * (1 - discount)

  
    tickets_sold += 1
    total_revenue += final_price
    if category == "Free":
        free_tickets += 1

    print(f"{customer_name}: {final_price:.2f} TRY ({category})")


if tickets_sold > 0:
    avg_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold} Total revenue: {total_revenue:.2f} TRY Average price: {avg_price:.2f} TRY Free tickets: {free_tickets}")
else:
    print("No tickets sold.")
