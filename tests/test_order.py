import pytest

from lib.order import Order


"""
Test initially order list is empty
"""
def test_order_dict_is_initially_empty():
    order_1 = Order()
    assert order_1.view_order() == {}

"""
Test order status is complete
is initially False
"""
def test_order_status_is_initially_false():
    order_1 = Order()
    assert order_1._is_complete == False


"""
Test order can be marked complete
with mark_complete
"""
def test_order_can_be_marked_complete():
    order_1 = Order()
    order_1.mark_complete()
    assert order_1._is_complete == True


"""
Test an item can be added to Order
"""


"""
Test mark complete on empty order 
raises error "This order is empty"
"""
