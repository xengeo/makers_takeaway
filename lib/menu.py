
"""Simple class structure to hold items"""

# Standard imports
from pprint import pprint

# Project imports
from lib.item import Item


ITEMS = {
    'Fish': 5.50,
    'Burger': 4.50,
    'Wrap': 5.00,
    'Chips': 2.00,
    'Salad': 3.00,
    'Soda': 1.00,
    'Water': 0.90,
    'Doughnut': 2.50,
}
class Menu():

    def __init__(self) -> None:
        # Parameters: Nothing
        # Returns: Formatted string with items and prices
        # Side-effects: Converts item pair in dict of item:price into Item objects. 
        #               Adds item obj to list of item dicts. [{},{},{}]
        self._menu = []


    def view_menu(self):
        pprint([item.format_item() for item in self._menu])


    def initiate_menu_with_items(self):
        for name, price in ITEMS.items():
            item = Item(name, price)
            self._menu.append(item)


# menu = Menu()
# menu.initiate_menu_with_items()
# menu.view_menu()