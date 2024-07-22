import pytest
from products import Product
from store import Store


def test_store_creation():
    product = Product("Test Product", 10.0, 5)
    store = Store([product])
    assert len(store.products) == 1


def test_store_add_product():
    product = Product("Test Product", 10.0, 5)
    store = Store([])
    store.add_product(product)
    assert len(store.products) == 1


def test_store_remove_product():
    product = Product("Test Product", 10.0, 5)
    store = Store([product])
    store.remove_product(product)
    assert len(store.products) == 0


def test_store_get_total_quantity():
    product1 = Product("Product 1", 10.0, 5)
    product2 = Product("Product 2", 20.0, 10)
    store = Store([product1, product2])
    assert store.get_total_quantity() == 15


def test_store_get_all_products():
    product1 = Product("Product 1", 10.0, 5)
    product2 = Product("Product 2", 20.0, 0)
    store = Store([product1, product2])
    assert len(store.get_all_products()) == 1


def test_store_order():
    product = Product("Test Product", 10.0, 5)
    store = Store([product])
    total_price = store.order([(product, 2)])
    assert total_price == 20.0
    assert product.get_quantity() == 3


def test_store_order_insufficient_stock():
    product = Product("Test Product", 10.0, 5)
    store = Store([product])
    with pytest.raises(ValueError):
        store.order([(product, 10)])
