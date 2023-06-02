import store
import products


def start(store_obj):
    """Start the user interface."""
    while True:
        print("\n---- Store Menu ----")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            display_products(store_obj)
        elif choice == "2":
            display_total_amount(store_obj)
        elif choice == "3":
            make_order(store_obj)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def display_products(store_obj):
    """Display all products in the store."""
    print("\n---- Products in Store ----")
    products = store_obj.get_all_products()
    for product in products:
        print(f"{product.name} - Price: {product.price} - Quantity: {product.quantity}")


def display_total_amount(store_obj):
    """Display the total amount of items in the store."""
    total_quantity = store_obj.get_total_quantity()
    print(f"\nTotal amount in store: {total_quantity}")


def make_order(store_obj):
    """Make an order for products."""
    print("\n---- Make an Order ----")
    products = store_obj.get_all_products()
    if len(products) == 0:
        print("No products available in the store.")
        return

    shopping_list = []
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.name} - Price: {product.price} - Quantity: {product.quantity}")

    while True:
        choice = input("Enter the number of the product to buy (0 to finish): ")
        if choice == "0":
            break

        try:
            index = int(choice) - 1
            if index < 0 or index >= len(products):
                raise ValueError
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        quantity = input("Enter the quantity to buy: ")
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity. Please try again.")
            continue

        product = products[index]
        if quantity > product.quantity:
            print("Insufficient quantity. Please enter a lower quantity.")
            continue

        shopping_list.append((product, quantity))
        product.quantity -= quantity
        print("Product added to the shopping list.")

    total_price = store_obj.order(shopping_list)
    print(f"Order placed successfully. Total price: {total_price}")


if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)

    # Start the user interface
    start(best_buy)
