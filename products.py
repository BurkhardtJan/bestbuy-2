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


class NonStockedProduct(Product):
    """
    Represents a non-physical product in the store.
    Quantities always zero.
    """

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        """
        Prints the product.
        """
        print(f"{self.name}, Price: ${self.price}, Quantity: Unlimited")

    def buy(self, quantity) -> float:
        """
        Buys the product.
        """
        return self.price * quantity


class LimitedProduct(Product):
    """
    Represents a limited product in the store.
    Only a certain amount is allowed to be bought.
    """

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        """
        Prints the product.
        """
        print(f"{self.name}, Price: ${self.price}, Limited to {self.maximum} per order!")

    def buy(self, quantity) -> float:
        """
        Buys the product.
        """
        if quantity > self.maximum:
            raise ValueError("Error while making order! Quantity larger than limit!")
        else:
            return super().buy(quantity)
