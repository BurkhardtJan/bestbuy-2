from products import Product


class Store:
    """
    Represents a Store with multiple products.
    """

    def __init__(self, products):
        """
        Initializes the store with a list of products.
        """
        self.products = products

    def add_product(self, product):
        """
        Adds a product to the store.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of the store.
        """
        total = 0
        for product in self.products:
            total += product.quantity
        return total

    def get_all_products(self) -> list[Product]:
        """
        Returns a list of all active products in the store.
        """
        active_products = [product for product in self.products if product.is_active()]
        return active_products

    def order(self, shopping_list) -> float:
        """
        shopping_list is a list of tuples (product, quantity).
        Function manages orders.
        """
        total = 0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total

    def __contains__(self, item):
        return item in self.products

    def __getitem__(self, item):
        return self.products.index(item)

    def __add__(self, other):
        if isinstance(other, Store):
            all_items = list(self.products)
            for item in other.products:
                if item in all_items:
                    all_items[all_items.index(item)].quantity += item.quantity
                else:
                    all_items.append(item)
            new_store = Store(products=all_items)
            return new_store

    def __str__(self):
        return f"Store contains: {[str(p) for p in self.products]}"


if __name__ == "__main__":
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))
