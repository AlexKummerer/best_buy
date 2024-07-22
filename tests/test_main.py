import pytest
from products import Product
from store import Store
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

def test_order_product(monkeypatch, capsys):
    inputs = iter(["1", "1", "", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    milk = Product("Milk", 1.50, 10)
    bread = Product("Bread", 2.00, 20)
    eggs = Product("Eggs", 0.50, 30)
    store = Store([milk, bread, eggs])

    percent_discount = PercentDiscount("10% Off", 10)
    second_half_price = SecondHalfPrice("Second Half Price")
    third_one_free = ThirdOneFree("Third One Free")

    total = store.order([(milk, 3), (bread, 2), (eggs, 10)])
    print(f"Total price without promotion: {total}")
    print(f"Total price with 10% off: {percent_discount.apply(total)}")
    print(f"Total price with second half price: {second_half_price.apply(total)}")
    print(f"Total price with third one free: {third_one_free.apply(total)}")

    captured = capsys.readouterr()
    assert "Total price without promotion: 13.5" in captured.out
    assert "Total price with 10% off: 12.15" in captured.out
    assert "Total price with second half price: 6.75" in captured.out
    assert "Total price with third one free: 9.346153846153847" in captured.out