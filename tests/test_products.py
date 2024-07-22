import pytest
from products import Product


def test_product_creation():
    product = Product("Test Product", 10.0, 5)
    assert product.name == "Test Product"
    assert product.price == 10.0
    assert product.quantity == 5
    assert product.active == True


def test_product_get_quantity():
    product = Product("Test Product", 10.0, 5)
    assert product.get_quantity() == 5


def test_product_set_quantity():
    product = Product("Test Product", 10.0, 5)
    product.set_quantity(10)
    assert product.get_quantity() == 10


def test_product_set_quantity_negative():
    product = Product("Test Product", 10.0, 5)
    with pytest.raises(ValueError):
        product.set_quantity(-1)


def test_product_is_active():
    product = Product("Test Product", 10.0, 5)
    assert product.is_active()
    product.deactivate()
    assert not product.is_active()


def test_product_buy():
    product = Product("Test Product", 10.0, 5)
    total_price = product.buy(2)
    assert total_price == 20.0
    assert product.get_quantity() == 3


def test_product_buy_insufficient_stock():
    product = Product("Test Product", 10.0, 5)
    with pytest.raises(ValueError):
        product.buy(10)
