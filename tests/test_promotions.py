import pytest
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

def test_percent_discount():
    promotion = PercentDiscount("10% Off", 10)
    assert promotion.apply(100) == 90
    assert promotion.apply(200) == 180

def test_second_half_price():
    promotion = SecondHalfPrice("Second Half Price")
    assert promotion.apply(100) == 50
    assert promotion.apply(200) == 100

def test_third_one_free():
    promotion = ThirdOneFree("Third One Free")
    assert promotion.apply(150) == 100
    assert promotion.apply(300) == 200

