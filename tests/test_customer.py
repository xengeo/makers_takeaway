# File: tests/test_customer.py 

from lib.customer import Customer

"""
Test customer is initiated with an empty order
#view_order returns: Empty list
"""
def test_customer_initially_returns_empty_order():
    bob = Customer()
    assert bob.view_order() == []

