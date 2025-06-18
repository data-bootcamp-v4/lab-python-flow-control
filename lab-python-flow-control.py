

products = ["t-shirt", "mug", "hat", "book", "keychain"]

   # a. Prompt the user to enter the name of a product that a customer wants to order.
customer_orders = set()
for i in range(3):
    product = input(f'Enter the name of a product to order (t-shirt, mug, hat, book, keychain): {products}:')
    customer_orders.add(product)
    #b. Add the product name to the "customer_orders" set.
print(customer_orders)
  #c. Ask the user if they want to add another product (yes/no).remo
customer_orders = set()

anProduct = input('Do you want another product?: ').lower()

if anProduct == 'yes':
    for i in range(5):
        product = input(f'Enter the name of a product to order (t-shirt, mug, hat, book, keychain): {products}:')
        customer_orders.add(product)
else:
    print('Bye bye')
      # d. Continue the loop until the user does not want to add another product.
anProduct = input('Do you want another product?: ').lower()
    
while anProduct == 'yes':
        product = input(f'Enter the name of a product to order (t-shirt, mug, hat, book, keychain): {products}:')
        customer_orders.add(product)
        anProduct = input('Do you want another product?: ').lower()