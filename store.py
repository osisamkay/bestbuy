from typing import List

from bestbuy.promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount
from products import Product, NonStockedProduct, LimitedProduct


class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of items in the store."""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """Returns all active products in the store."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Buys the products from the shopping list and returns the total price of the order.

        Args:
            shopping_list (List[tuple]): A list of tuples where each tuple contains a Product instance and the quantity to buy.

        Returns:
            float: The total price of the order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    for product in product_list:
        print(product.show())

    # Test buy with promotions
    print(product_list[0].buy(3))
    print(product_list[1].buy(4))
    print(product_list[3].buy(2))

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))


if __name__ == "__main__":
    main()
