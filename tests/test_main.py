import pytest
from unittest.mock import patch
from io import StringIO
import main  # Ensure main.py is in the same directory or correctly imported

@pytest.fixture
def mock_input_output():
    inputs = iter([
        '1',  # List all products
        '2',  # Show total amount in store
        '3',  # Make an order
        '1',  # Select product 1 (MacBook Air M2)
        '2',  # Amount: 2
        '',   # Finish order
        '4'   # Quit
    ])
    with patch('builtins.input', lambda _: next(inputs)), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        yield mock_stdout

def test_main(mock_input_output):
    # Debugging print statements to ensure the patches are applied
    print("Starting test_main")
    
    # Run the main function while the input and output are being mocked
    main.main()
    
    # Capture the output
    output = mock_input_output.getvalue()

    # Debug print the captured output to trace issues
    print("Captured Output:")
    print(output)

    # Check the output contains the expected values
    assert "Products in store" in output
    assert "MacBook Air M2" in output
    assert "Total quantity in store" in output
    assert "Order successful! Total price: 2900" in output
    assert "Order Summary" in output
    assert "Total payment: 2900.0" in output
    assert "Goodbye!" in output
