# File: lib/items.p

class Item():
    
    def __init__(self, item, price):
        # Parameters: Item (string) and price (float)
        # Returns: Nothing
        # Side-effects: Sets attributes self.item and self.price
        self._name = item
        self._price = price
        
    def format_item(self):
        return f"{self._name}:  £{self._price:.2f}" #This keeps the price to two decimals
    