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

class AssetManager:
    def __init__(self):
        self.assets = []
        self.next_id = 1

    def create_asset(self, name, type, purchase_date, asset_quantity):
        new_asset = Asset(name, type, purchase_date, asset_quantity, True)  # Availability set to True by default
        new_asset.asset_id = self.next_id
        self.assets.append(new_asset)
        self.next_id += 1  # Increment for next asset
        return new_asset


asset_manager = AssetManager()
# Create assets
laptop = asset_manager.create_asset("Laptop", "Hardware", datetime.date(2023, 7, 15), 4)
office = asset_manager.create_asset("Chair", "Software", datetime.date(2024, 1, 1), 0)  # Now has 0 quantity

# Print only available assets
print("Available Assets:")
for asset in asset_manager.assets:
    if asset.availability:
        print(f"- {asset.name} (ID: {asset.asset_id})")
