from typing import List, Callable
from store import Store
from products import Product, NonStockedProduct, LimitedProduct
import promotions


def create_store() -> Store:
    """
    Create and return the store with initial products and promotions.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
    ]

    # Add promotions to products
    product_list[0].set_promotion(promotions.SecondHalfPrice("Second Half price!"))
    product_list[1].set_promotion(promotions.ThirdOneFree("Third One Free!"))
    product_list[3].set_promotion(promotions.PercentDiscount("30% off!", percent=30))

    return Store(product_list)


def display_products(store: Store) -> None:
    """Display all products in the store."""
    print("\nProducts in Store\n-----------------")
    products = store.get_all_products()
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product}")


def handle_order(store: Store) -> None:
    """Handle user orders interactively."""
    print("\nWhen you want to finish the order, press Enter without typing.")
    total_payment = 0.0
    products = store.get_all_products()

    while True:
        display_products(store)
        product_number = input("Which product # do you want? (Enter to finish): ")
        if not product_number:
            break

        try:
            product_index = int(product_number) - 1
            if not (0 <= product_index < len(products)):
                print("Invalid product number. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        product = products[product_index]

        try:
            amount = int(input(f"How many units of '{product.name}' do you want? "))
            if amount <= 0:
                print("Amount must be a positive number.")
                continue

            if isinstance(product, LimitedProduct) and amount > product.maximum:
                print(
                    f"Cannot order more than {product.maximum} units of '{product.name}'."
                )
                continue

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        try:
            total_payment += store.order([(product, amount)])
            print(
                f"Order successful! Added {amount} of '{product.name}' to your order."
            )
        except ValueError as e:
            print(f"Error: {e}")

    print(f"\nOrder Summary: Total payment: ${total_payment:.2f}\n")


def display_menu() -> None:
    """Display the store menu."""
    print("\nStore Menu\n----------")
    print("1. List all products in store")
    print("2. Show total quantity of products in store")
    print("3. Make an order")
    print("4. Quit")


def main(input_func: Callable = input, print_func: Callable = print) -> None:
    """Main function for running the store application."""
    store = create_store()

    menu_options = {
        1: lambda: display_products(store),
        2: lambda: print_func(
            f"\nTotal quantity in store: {store.get_total_quantity()}\n"
        ),
        3: lambda: handle_order(store),
        4: lambda: print_func("Goodbye!"),
    }

    while True:
        display_menu()
        try:
            choice = int(input_func("Enter your choice: "))
        except ValueError:
            print_func("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice in menu_options:
            if choice == 4:
                menu_options[choice]()
                break
            menu_options[choice]()
        else:
            print_func("Invalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()
