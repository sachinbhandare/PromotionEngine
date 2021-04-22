import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout

def test_CanAddItemPrice(checkout):
    checkout.addItemPrice('A', 1)

def test_addItem(checkout):
    checkout.addItem('A')