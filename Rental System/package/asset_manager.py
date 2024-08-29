from .asset import Asset
import datetime

class AssetManager:
    def __init__(self):
        self.assets = []
        self.next_id = 1

    def create_asset(self, name, type, purchase_date, asset_quantity, availability):
        new_asset = Asset(self.next_id, name, type, purchase_date, asset_quantity, True)  # Availability set to True by default
        new_asset.asset_id = self.next_id
        self.assets.append(new_asset)
        self.next_id += 1  # Increments the ID +1 for next asset
        return new_asset