import pytest
from products import Product


def test_create_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True


def test_create_product_with_invalid_details():
    with pytest.raises(Exception):
        Product("", price=-500, quantity=50)


def test_product_quantity_zero_becomes_inactive():
    product = Product("Bose QuietComfort Earbuds", price=250, quantity=0)
    assert product.is_active() is False



def test_product_purchase_modifies_quantity():
    product = Product("Google Pixel 7", price=500, quantity=100)
    quantity_to_buy = 3
    total_price = product.buy(quantity_to_buy)
    assert product.quantity == 97  # Quantity reduced by 3
    assert total_price == 3 * 500  # Total price equals quantity * price


def test_buying_larger_quantity_invokes_exception():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(Exception):
        product.buy(150)  # Attempt to buy 150 when only 100 available
