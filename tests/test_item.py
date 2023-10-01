from lib.item import Item

"""
Test item added is formatteed
#returns formatted string describing item name and price
"""
def test_item_name_and_price_formatted():
    item_1 = Item(item='Fish', price=5.00)
    assert item_1.format_item() == "Fish:  £5.00"