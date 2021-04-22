import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice('A',50)
    checkout.addItemPrice('B',30)
    checkout.addItemPrice('C',20)
    checkout.addItemPrice('D',15)
    return checkout

""" def test_CanAddItemPrice(checkout):
    checkout.addItemPrice('A', 50) """

def test_CanCalculateTotal(checkout):
    checkout.addItem('A')
    assert checkout.calculateTotal() == 50

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem('A')
    checkout.addItem('B')
    assert checkout.calculateTotal() == 80

def test_CanAddDiscountRule(checkout):
    checkout.addDiscount('A', 3, 130)

def test_CanApplyDiscountRule(checkout):
    checkout.addDiscount('A',3, 130)
    checkout.addDiscount('B',2, 45)
    checkout.addItem('A')
    checkout.addItem('A')
    checkout.addItem('A')
    checkout.addItem('B')
    checkout.addItem('B')
    assert checkout.calculateTotal() == 175

def test_ScenarioA(checkout):
    checkout.addItem('A')
    checkout.addItem('B')
    checkout.addItem('C')
    assert checkout.calculateTotal() == 100

def test_ScenarioB(checkout):
    checkout.addDiscount('A',3, 130)
    checkout.addDiscount('B',2, 45)
    checkout.addItems('A', 5)
    checkout.addItems('B', 5)
    checkout.addItems('C', 1)
    assert checkout.calculateTotal() == 370

@pytest.mark.skip
def test_ScenarioB1(checkout):
    checkout.addDiscount('A',3, 130)
    checkout.addItems('A', 5)
    assert checkout.calculateTotal() == 230
