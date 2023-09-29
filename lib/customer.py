
class Customer():

    def __init__(self, name) -> None:
        # attributes: name (string), order (list of Order instances)
        # Returns: Nothing
        # Side-effects: assign name and order
        pass
    
    def view_menu(self):
        # Parameters: Nothing
        # Return: string representing menu dictionary
        # Side-effects: Nothing
        pass

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
        # Return: string representing order dictionary
        # Side-effects: Nothing
        pass

    def complete_order(self):
        # Parameters: Nothing
        # Return: Nothing
        # Side-effects: calls order.mark_complete(), order.print_receipt(), order.send_text()
        pass




