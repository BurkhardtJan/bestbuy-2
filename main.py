import products
import store
import promotions

MENU = """
   Store Menu
   ----------   
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""


def list_products(my_store):
    """
    Prints out all products in store
    """
    print("------")
    i = 1
    for product in my_store.get_all_products():
        print(f"{i}. ", product)
        i += 1
    print("------")


def print_amount(my_store):
    """
    Prints out the amount of products in store

    """
    quantity = my_store.get_total_quantity()
    print(f"Total of {quantity} items in store")


def make_order(my_store):
    """
    Handels inputs for orders and the order itself.
    Negative amount interpreted as return, because same behavior in the demo.
    """
    list_products(best_buy)
    print("When you want to finish order, enter empty text.")
    shopping_list = []
    all_products = my_store.get_all_products()
    while True:
        item = input("Which product # do you want? ")
        quantity = input("What amount do you want? ")
        if item == "":
            break
        try:
            product = all_products[int(item) - 1]
            quantity = int(quantity)
            if int(item) <= 0:
                raise IndexError
        except IndexError:
            print("Error adding product!")
        except ValueError:
            print(f"Error while making order! invalid literal for int() with base 10: '{quantity}'")
        else:
            shopping_list.append((product, quantity))
            print("Product added to list!")
    try:
        payment = my_store.order(shopping_list)
        print(f"Order made! Total payment: ${payment}")
    except Exception as e:
        print(e)


def start(my_store):
    """
    Main Loop, shows menu and handels inputs.
    """
    while True:
        print(MENU)
        choice = input("Please choose a number: ")
        if choice == "1":
            list_products(my_store)
        elif choice == "2":
            print_amount(my_store)
        elif choice == "3":
            make_order(my_store)
        elif choice == "4":
            quit()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]
    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)
