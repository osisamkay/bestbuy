class Promotion:
    """Base class for promotions."""

    def __init__(self, name):
        """
        Initiator (constructor) method.

        Args:
            name (str): The name of the promotion.
        """
        self.name = name

    def apply_promotion(self, product, quantity):
        """
        Apply the promotion to the product and quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The discounted price after applying the promotion.
        """
        return product.price * quantity


class PercentDiscount(Promotion):
    """Promotion for percentage discount."""

    def __init__(self, name, percent):
        """
        Initiator (constructor) method for percentage discount promotion.

        Args:
            name (str): The name of the promotion.
            percent (float): The percentage discount to apply.
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Apply the percentage discount promotion to the product and quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The discounted price after applying the promotion.
        """
        price = super().apply_promotion(product, quantity)
        discount = price * (self.percent / 100)
        return price - discount


class SecondHalfPrice(Promotion):
    """Promotion for second item at half price."""

    def __init__(self, name):
        """
        Initiator (constructor) method for second item at half price promotion.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply the second item at half price promotion to the product and quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The discounted price after applying the promotion.
        """
        price = super().apply_promotion(product, quantity)
        items_with_discount = quantity // 2
        discounted_price = (price / quantity) * (items_with_discount + (quantity % 2))
        return discounted_price


class ThirdOneFree(Promotion):
    """Promotion for buy 2, get 1 free."""

    def __init__(self, name):
        """
        Initiator (constructor) method for buy 2, get 1 free promotion.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply the buy 2, get 1 free promotion to the product and quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The discounted price after applying the promotion.
        """
        price = super().apply_promotion(product, quantity)
        free_items = quantity // 3
        discounted_price = (price / quantity) * (quantity - free_items)
        return discounted_price
