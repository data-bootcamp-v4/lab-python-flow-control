# 1. Define products and initialize inventory using a loop
products = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = {}

print("=== INVENTORY SETUP ===")
for product in products:
    while True:
        user_input = input(f"Enter the quantity for '{product}': ").strip()
        if user_input.isdigit():
            inventory[product] = int(user_input)
            break
        else:
            print(f"  ⚠ Invalid input. Please enter a whole number (e.g. 5).")

print("\n--- Initial Inventory ---")
for product, qty in inventory.items():
    print(f"  {product}: {qty}")


# 2. Take customer orders using a while loop
customer_orders = set()
add_another = "yes"

print("\n=== PLACE YOUR ORDER ===")
print(f"Available products: {products}")

while add_another == "yes":
    product_name = input("Enter a product name: ").strip().lower()

    if product_name in products:
        customer_orders.add(product_name)
        print(f"  '{product_name}' added to your order.")
    else:
        print(f"  '{product_name}' is not available. Choose from: {products}")

    while True:
        add_another = input("Add another product? (yes/no): ").strip().lower()
        if add_another in ("yes", "no"):
            break
        else:
            print("  ⚠ Please type 'yes' or 'no'.")

print(f"\nCustomer Orders: {customer_orders}")


# 3. Calculate and print order statistics
total_products_ordered = len(customer_orders)
percentage_ordered = (total_products_ordered / len(products)) * 100
order_status = (total_products_ordered, percentage_ordered)

print("\n=== ORDER STATISTICS ===")
print(f"  Total Products Ordered: {order_status[0]}")
print(f"  Percentage of Products Ordered: {order_status[1]:.1f}%")


# 4. Update inventory only for ordered products
for product in customer_orders:
    if inventory[product] > 0:
        inventory[product] -= 1
    else:
        print(f"  Warning: '{product}' is out of stock!")

print("\n=== UPDATED INVENTORY ===")
for product, qty in inventory.items():
    print(f"  {product}: {qty}")
