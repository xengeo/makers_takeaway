from lib.menu import Menu


class Customer():

    def __init__(self) -> None:
        # attributes: order (list of Order instances)
        # Parameters: Nothing
        # Returns: Nothing
        # Side-effects: assign self._order (A list of Orders)
        self._order = []
    
    def view_menu(self, menu):
        # Parameters: Nothing
        # Return: string representing menu dictionary
        # Side-effects: Nothing
        return menu.view_menu()

    def start_order(self):
        # Parameters: Nothing
        # Returns: Nothing
        # Side-effects: creates instance of Order class
        pass

    def add_item_to_order(self):
        # Parameters: item (from the menu dictionary)
        # Return: Nothing
        # Side-effect: Add items to Order dictionary
        pass

    def view_order(self):
        # Parameters: Nothing
        # Return: string representing items on the order
        # Side-effects: Nothing
        return self._order

    def complete_order(self):
        # Parameters: Nothing
        # Return: Nothing
        # Side-effects: calls order.mark_complete(), order.print_receipt(), order.send_text()
        pass




