order_amount = float(input("Enter unit price (TRY): "))
available_stock = int(input("Enter available stock quantity: "))
requested_quantity = int(input("Enter requested quantity: "))
is_member_input = input("Is the customer a member? (yes/no): ").strip().lower()

is_member = is_member_input == "yes"

if requested_quantity <= 0:
    print("\nOrder Rejected: Requested quantity must be greater than zero.")
elif requested_quantity > available_stock:
    print(
        f"\nOrder Rejected: Insufficient stock. Available: {available_stock}, Requested: {requested_quantity}."
    )
else:
    subtotal = order_amount * requested_quantity

    if is_member and subtotal >= 500:
        discount = subtotal * 0.10
        final_price = subtotal - discount
        approval_reason = (
            "Order Approved (Member discount of 10% applied for total >= 500 TRY)."
        )
    else:
        final_price = subtotal
        approval_reason = "Order Approved (Standard pricing applied)."

    print(f"\nStatus: {approval_reason}")
    print(f"Final Price: {final_price:.2f} TRY")
