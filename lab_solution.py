# Lab | Flow Control
# Exercise: Managing Customer Orders Optimized

# Initial inventory
products = {
    "t-shirt": 4,
    "mug": 6,
    "hat": 9,
    "book": 3,
    "keychain": 2
}

# Initialize customer orders set
customer_orders = set()

# Step 2: Use a while loop to get customer orders
add_more = True
while add_more:
    # Prompt user to enter a product
    product = input("Enter the name of a product that a customer wants to order: ").lower()

    # Add the product to the customer_orders set
    customer_orders.add(product)

    # Ask if user wants to add another product
    another = input("Do you want to add another product? (yes/no): ").lower()

    # Continue loop based on user input
    if another != "yes":
        add_more = False

# Display customer orders
print("\nCustomer Orders:", customer_orders)

# Step 3: Update inventory only for the ordered products
for product in customer_orders:
    if product in products:
        products[product] -= 1
    else:
        print(f"Warning: '{product}' is not in the inventory.")

# Display updated inventory
print("\nUpdated Inventory:")
for product, quantity in products.items():
    print(f"{product}: {quantity}")

# Display order summary
print(f"\nOrder Summary:")
print(f"Products ordered: {customer_orders}")
print(f"Total products ordered: {len(customer_orders)}")
