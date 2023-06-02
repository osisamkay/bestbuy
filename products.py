class Product:
    """Represents a specific type of product available in the store."""

    def __init__(self, name, price, quantity):
        """
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity), raises an exception.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.

        Raises:
            ValueError: If the name is empty or if the price or quantity is negative.
        """
        if not name:
            raise ValueError("Invalid name")
        if price < 0:
            raise ValueError("Invalid price")
        if quantity < 0:
            raise ValueError("Invalid quantity")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self):
        """Getter function for quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """
        Setter function for quantity.
        If quantity reaches 0, deactivates the product.

        Args:
            quantity (int): The new quantity of the product.
        """
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self):
        """Getter function for active."""
        return self.active and self.quantity > 0

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def get_promotion(self):
        """Getter function for promotion."""
        return self.promotion

    def set_promotion(self, promotion):
        """
        Setter function for promotion.

        Args:
            promotion (Promotion): The promotion to set for the product.
        """
        self.promotion = promotion

    def show(self):
        """Returns a string that represents the product, including the current promotion if it exists."""
        promotion_info = f"Promotion: {self.promotion.name}" if self.promotion else "No Promotion"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, {promotion_info}"

    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price of the purchase.
        Updates the quantity of the product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            Exception: If the product is inactive or there is not enough quantity available.
        """
        if not self.active:
            raise Exception("Product is inactive")
        if quantity > self.quantity:
            raise Exception("Not enough quantity available")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity

        return total_price


class NonStockedProduct(Product):
    """Represents a non-stocked product available in the store."""

    def __init__(self, name, price):
        """
        Initiator (constructor) method for non-stocked product.
        Calls the parent constructor and sets the quantity to 0.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        super().__init__(name, price, quantity=0)

    def show(self):
        """Returns a string that represents the non-stocked product."""
        return f"{self.name} (Non-Stocked), Price: {self.price}"


class LimitedProduct(Product):
    """Represents a limited quantity product available in the store."""

    def __init__(self, name, price, quantity, maximum):
        """
        Initiator (constructor) method for limited quantity product.
        Calls the parent constructor and adds a maximum quantity attribute.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
            maximum (int): The maximum quantity allowed for the product.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        """Returns a string that represents the limited quantity product."""
        return f"{self.name} (Limited), Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(10)
    print(bose.show(), bose.is_active())




if __name__ == "__main__":
    main()
