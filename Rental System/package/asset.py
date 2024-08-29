import datetime

class Asset:
    def __init__(self, asset_id, name, type, purchase_date, asset_quantity, availability):
        self.asset_id = None
        self.name = name
        self.type = type
        self.purchase_date = purchase_date
        self.asset_quantity = asset_quantity
        self.availability = self.is_available()
    
    def is_available(self):
        return self.asset_quantity > 0
    
    def rent(self):
        if self.availability == True:
            self.asset_quantity -= 1
            self.availability = self.is_available()
            print(f"{self.name} rented successfully!")
        else:
            print(f"Sorry, {self.name} is currently unavailable.")