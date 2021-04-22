from Checkout import Checkout

def test_CanInstantiatieCheckout():
    co = Checkout()

def test_CanAddItemPrice():
    co = Checkout()
    co.addItemPrice('A', 1)