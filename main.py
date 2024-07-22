import promotions
from store import Store
from products import Product, NonStockedProduct, LimitedProduct

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    NonStockedProduct("Windows License", price=125),
    LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
]
best_buy = Store(product_list)

second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)


def get_product_list() -> None:
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
        try:
            product_number = int(product_number)
            if product_number < 1 or product_number > len(best_buy.products):
                print("Invalid product number. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid product number.")
            continue
        try:
            amount = int(input("What amount do you want? "))
            if amount <= 0:
                print("Amount must be positive. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            continue
        product = best_buy.products[product_number - 1]
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
        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
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
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
