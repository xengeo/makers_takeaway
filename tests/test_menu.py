from lib.menu import Menu


"""
Test menu initiates with empty menu
"""
def test_menu_begins_empty():
    menu_1 = Menu()
    assert menu_1._menu == []


"""
Test items are added to menu
"""