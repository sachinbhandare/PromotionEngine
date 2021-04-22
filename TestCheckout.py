import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout

def test_CanAddItemPrice(checkout):
    checkout.addItemPrice('A', 50)

def test_addItem(checkout):
    checkout.addItem('A')

def test_CanCalculateTotal(checkout):
    checkout.addItemPrice('A', 50)
    checkout.addItem('A')
    assert checkout.calculateTotal() == 50

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItemPrice('A',50)
    checkout.addItemPrice('B',30)
    checkout.addItem('A')
    checkout.addItem('B')
    assert checkout.calculateTotal() == 80