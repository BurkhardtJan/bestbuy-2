class Product:
    """
    Represents a product in the store.
    """

    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Initial quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """
        Returns the quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product.
        """
        self.quantity -= quantity
        if (self.quantity <= 0):
            self.deactivate()

    def is_active(self) -> bool:
        """
        Returns whether the product is active.
        :return:
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        :return:
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        :return:
        """
        self.active = False

    def show(self):
        """
        Prints the product.
        """
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        """
        Buys the product. Handles problems.
        """
        if self.quantity >= quantity and self.is_active():
            self.set_quantity(quantity)
            return self.price * quantity
        else:
            raise ValueError("Error while making order! Quantity larger than what exists")


if __name__ == '__main__':
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
