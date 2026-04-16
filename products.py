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
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True
        self._promotion = False

    @property
    def name(self):
        """Returns the product name."""
        return self._name

    @property
    def price(self):
        """Returns the product price."""
        return self._price

    @property
    def quantity(self):
        """Returns the product quantity."""
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the product quantity."""
        self._quantity = quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product and deactivates if quantity < 0.
        """
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    @property
    def promotion(self):
        """Returns the product promotion."""
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        """
        Sets the promotion.
        """
        self._promotion = promotion

    def set_promotion(self, promotion):
        """
        Alias for setter to maintain exersice calls
        """
        self.promotion = promotion

    @property
    def active(self):
        """Returns the product active status."""
        return self._active

    @active.setter
    def active(self, status):
        """Sets the product active status."""
        self._active = status

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

    def __str__(self):
        """
        Prints the product.
        """
        infos = f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"
        if self.promotion:
            return infos + f", promotion: {self.promotion.promotion_text}"
        else:
            return infos

    def buy(self, quantity) -> float:
        """
        Buys the product. Handles problems.
        """
        if self.quantity >= quantity and self.is_active():
            self.set_quantity(self.quantity - quantity)
            if self.promotion:
                return self.promotion.apply_promotion(self, quantity)
            else:
                return self.price * quantity
        else:
            raise ValueError("Error while making order! Quantity larger than what exists")

    def __gt__(self, other):
        """Compares the products by price (>)."""
        return self.price > other.price

    def __lt__(self, other):
        """Compares the products by price (<)."""
        return self.price < other.price

    def __ge__(self, other):
        """Compares the products by price (>=)."""
        return self.price >= other.price

    def __le__(self, other):
        """Compares the products by price (<=)."""
        return self.price <= other.price


class NonStockedProduct(Product):
    """
    Represents a non-physical product in the store.
    Quantities always zero.
    """

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def __str__(self):
        """
        Prints the product.
        """
        infos = f"{self.name}, Price: ${self.price}, Quantity: Unlimited"
        if self.promotion:
            return infos + f", promotion: {self.promotion.promotion_text}"
        else:
            return infos

    def buy(self, quantity) -> float:
        """
        Buys the product.
        """
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return self.price * quantity


class LimitedProduct(Product):
    """
    Represents a limited product in the store.
    Only a certain amount is allowed to be bought.
    """

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def __str__(self):
        """
        Prints the product.
        """
        infos = f"{self.name}, Price: ${self.price}, Limited to {self.maximum} per order!"
        if self.promotion:
            return infos + f", promotion: {self.promotion.promotion_text}"
        else:
            return infos

    def buy(self, quantity) -> float:
        """
        Buys the product.
        """
        if quantity > self.maximum:
            raise ValueError("Error while making order! Quantity larger than limit!")
        else:
            return super().buy(quantity)
