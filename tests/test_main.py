import pytest
import sys

sys.path.append("/mnt/data")
from main import get_product_list, order_product, command_line_menu


def test_combined_input_output(monkeypatch, capsys):
    inputs = iter(["2", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    command_line_menu()
    captured = capsys.readouterr()
    assert "Show total amount in store" in captured.out
    assert "Quit" in captured.out  # Adjust to match the actual menu option text


def test_order_product(monkeypatch, capsys):
    inputs = iter(["1", "1", "", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    order_product()
    captured = capsys.readouterr()
    assert "Order Summary" in captured.out
    assert "Total payment" in captured.out
