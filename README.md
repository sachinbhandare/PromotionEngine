# PromotionEngine

We need you to implement a simple promotion engine for a checkout process. Our Cart contains a list of single character SKU ids (A, B, C.	) over which the promotion engine will need to run.

The promotion engine will need to calculate the total order value after applying the 2 promotion types

1. buy 'n' items of a SKU for a fixed price (3 A's for 130)
2. buy SKU 1 & SKU 2 for a fixed price ( C + D = 30 )

The promotion engine should be modular to allow for more promotion types to be added at a later date (e.g. a future promotion could be x% of a SKU unit price). For this coding exercise you can assume that the promotions will be mutually exclusive; in other words if one is applied the other promotions will not apply

### Test Setup
```
Unit price for - SKU IDs 
A	50
B	30
C	20
D	15
```

### Active Promotions
```
3 of A's for 130
2 of B's for 45 
C & D for 30
```

### Scenario A
```
1 * A 50
1 * B 30 
1 * C 30

Total : 100
```

### Scenario B
```
5 * A = 130 + 2*50
5 * B = 45 + 45 + 30
1 * C = 20

Total = 370
```
### Scenario C
```
3 * A = 130
5 * B = 45 + 45 + 1 * 30
1 * C = -
1 * D = 30


Total = 280
```

Sample testing output:
```
(python3_pytest) sbhandare@pranavs-laplop:~/PromotionEngine$ pytest -v -s TestCheckout.py 
============================================================= test session starts =============================================================
platform linux -- Python 3.8.5, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- /home/sbhandare/PromotionEngine/python3_pytest/bin/python
cachedir: .pytest_cache
rootdir: /home/sbhandare/PromotionEngine
collected 8 items                                                                                                                             

TestCheckout.py::test_CanCalculateTotal PASSED
TestCheckout.py::test_GetCorrectTotalWithMultipleItems PASSED
TestCheckout.py::test_CanAddDiscountRule PASSED
TestCheckout.py::test_CanApplyDiscountRule PASSED
TestCheckout.py::test_ScenarioA PASSED
TestCheckout.py::test_ScenarioB PASSED
TestCheckout.py::test_ScenarioB1 SKIPPED (unconditional skip)
TestCheckout.py::test_ScenarioC PASSED

======================================================== 7 passed, 1 skipped in 0.01s =========================================================
```
