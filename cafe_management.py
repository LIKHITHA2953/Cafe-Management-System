
# Café Menu Dictionary

menu = {
    'pizza': 50,
    'salad': 30,
    'burger': 100,
    'popcorn': 70,
    'chicken puff': 100
}

# Greeting and Menu Display

print("Welcome to our Cafe")
print("Pizza: 50\nSalad: 30\nBurger: 100\nPopcorn: 70\nChicken Puff: 100")

order_total = 0

# Taking first order

order_item = input("Enter your item: ").lower()

if order_item in menu:
    order_total += menu[order_item]
    print(f"Your item {order_item} has been added to your order")
else:
    print(f"Ordered item {order_item} is not available")

# Asking for more orders

order = input("Do you want to add another item? (Yes/No): ").lower()

if order == "yes":
    order_item2 = input("Enter your second item: ").lower()

    if order_item2 in menu:
        order_total += menu[order_item2]
        print(f"Item {order_item2} has been added")
    else:
        print(f"Ordered item {order_item2} is not available")

# Displaying final bill

print(f"Your total order value is {order_total}")
