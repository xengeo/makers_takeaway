# File: tests/test_customer.py 

import pytest
from unittest.mock import Mock

from lib.customer import Customer

"""
Test customer is initiated with an empty order
#view_order returns: Empty list
"""
def test_customer_initially_returns_empty_order():
    bob = Customer()
    assert bob.view_order() == []


"""
Test the customer can view menu
#view menu returns all items printed
"""

def test_menu_returns_menu_items():

    menu_mock = Mock()
    menu_mock.view_menu.return_value = ['Fish:  £5.50',
                                        'Burger:  £4.50',
                                        'Wrap:  £5.00',
                                        'Chips:  £2.00',
                                        'Salad:  £3.00',
                                        'Soda:  £1.00',
                                        'Water:  £0.90',
                                        'Doughnut:  £2.50']
    bob = Customer()
    result =  bob.view_menu(menu_mock) 
    
    menu_mock.view_menu.assert_called()
    assert result == ['Fish:  £5.50',
                        'Burger:  £4.50',
                        'Wrap:  £5.00',
                        'Chips:  £2.00',
                        'Salad:  £3.00',
                        'Soda:  £1.00',
                        'Water:  £0.90',
                        'Doughnut:  £2.50']
    