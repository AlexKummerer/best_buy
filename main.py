from store import Store
from products import Product

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = Store(product_list)


def get_product_list() -> None:
    """
    List all products in store
    """
    products = best_buy.get_all_products()
    print("\nProducts in store\n-----------------")
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product}")


def order_product() -> None:
    """
    Make an order
    """

    print("When you want to finish order, enter empty text.")

    total_payment = 0.0
    while True:
        get_product_list()
        product_number = input("Which product # do you want? ")

        if not product_number:
            break

        amount = int(input("What amount do you want? "))
        product = best_buy.products[int(product_number) - 1]

        try:
            total_payment += best_buy.order([(product, amount)])
            print(f"Order successful! Total price: {product.price * amount}")
        except ValueError as error:
            print(error)
            break

    print("\nOrder Summary\n-------------")
    print(f"Order made! Total payment: {total_payment}")


def command_line_menu() -> None:
    """
    Display command line menu
    """
    print("\nStore Menu\n----------")
    print(
        "1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit\n"
    )


def main() -> None:
    """
    Main function
    """
    while True:
        command_line_menu()
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            get_product_list()
        elif user_input == 2:
            print(f"\nTotal quantity in store: {best_buy.get_total_quantity()}")
        elif user_input == 3:
            try:
                order_product()
            except ValueError as error:
                print(error)
        elif user_input == 4:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
