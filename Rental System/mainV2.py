"""Module providing a function printing python version."""

import datetime

class Asset:
    """Class to create the"""
    def __init__(self, asset_id, name, type, purchase_date, asset_quantity, availability):
        self.asset_id = None
        self.name = name
        self.type = type
        self.purchase_date = purchase_date
        self.asset_quantity = asset_quantity
        self.availability = self.is_available()
    
    def is_available(self):
        """Checks if asset quantity is over 0, if so then availability True."""
        return self.asset_quantity > 0
    
    def rent(self):
        """Program to rent. Removes an asset once selected and decreases by 1"""
        if self.availability:
            self.asset_quantity -= 1
            self.availability = self.is_available()
            print(f"{self.name} rented successfully!")
        else:
            print(f"Sorry, {self.name} is currently unavailable.")

class AssetManager:
    def __init__(self):
        self.assets = []
        self.next_id = 1 # Starts Asset ID as 1

    def create_asset(self, name, type, purchase_date, asset_quantity, availability):
        new_asset = Asset(self.next_id, name, type, purchase_date, asset_quantity, True)  # Availability set to True by default
        new_asset.asset_id = self.next_id
        self.assets.append(new_asset)
        self.next_id += 1  # Increments the ID +1 for next asset
        return new_asset

asset_manager = AssetManager()

laptop = asset_manager.create_asset("Laptop", "Hardware", datetime.date(2023, 7, 15), 4, True)
office = asset_manager.create_asset("MS Office", "Software", datetime.date(2024, 1, 1), 3, True) 
mouse = asset_manager.create_asset("Mouse", "Software", datetime.date(2024, 1, 1), 3, True)



while True: # Loops and shows the available assets to the user (reduces each time one is selected)
    print("Available Assets:")
    for asset in asset_manager.assets:
        if asset.availability:
            print(f"{asset.asset_id}- {asset.name} (Quantity: {asset.asset_quantity})") # Show users the currently available assets 
    asset_id_rent = input("Enter asset ID to rent (or 'q' to quit): ")
    if asset_id_rent.lower() == 'q':
        break
    try:
        asset_id = int(asset_id_rent)
        found_asset = None
        for asset in asset_manager.assets:
            if asset.asset_id == asset_id:
                found_asset = asset
                break
        if found_asset:
            found_asset.rent()
        else:
            print(f"Asset with ID {asset_id} not found.")
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")
