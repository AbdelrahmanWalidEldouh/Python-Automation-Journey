products = {"apples": 30, "oranges": 40, "bananas": 50, "watermelons": 20, "pears": 30}


def mange(product_name, quantity):
    try:
        quantity = int(quantity)

        if product_name in products and quantity <= products[product_name]:
            products[product_name] -= quantity
            print(f"{quantity} Sold From {product_name}")
        else:
            print("Item not found or not enough quantity.")

    except ValueError:
        print("Invalid input: Please enter a valid number for quantity.")


i = ""
while i != "exit":
    i = input("Enter product name (or 'exit' to quit): ").lower().strip()

    if i == "exit":
        break

    x = input("Product quantity: ")

    mange(i, x)

    ask = input("Do you want to see the remaining stock? (y/n) ").strip().lower()
    if ask == "yes" or ask == "y":
        for product, quant in products.items():
            print(product, quant)
