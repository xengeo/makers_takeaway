

class Order():

    def __init__(self):
        # self._order = {}
        # Parameters: Nothing
        # Returns: Nothing
        # Side-effects: Establishes self._items (dict), self._is_complete = False
        self._order = {}
        self._is_complete = False

    def view_order(self):
        return self._order
        
    def mark_complete(self):
        # Parameters: Nothing
        # Return: Nothing
        # Side-effect: self._is_complete set to True
        self._is_complete = True

    def print_receipt(self):
        # Parameters: Nothing
        # Returns: List of items selected and grand total as formatted string
        # Side-effect: Nothing
        pass

    def send_delivery_text(self):
        # Parameters: Nothing
        # Return: Nothing
        # Side-effects: Texts user through twilio
        pass