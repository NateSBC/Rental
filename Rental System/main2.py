import datetime

#Test Updating Code

class Asset:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.is_rented = False
        self.rental_end = None

    def rent(self, duration):
        if self.is_rented:
            print(f"{self.name} is already rented.")
            return
        self.is_rented = True
        self.rental_end = datetime.datetime.now() + duration

    def return_asset(self):
        if not self.is_rented:
            print(f"{self.name} is not rented.")
            return
        self.is_rented = False
        self.rental_end = None

class AssetManager:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def list_assets(self):
        for asset in self.assets:
            if not asset.is_rented:
                print(f"{asset.name} ({asset.type}) is available")

    def rent_asset(self, asset_name, duration):
        for asset in self.assets:
            if asset.name == asset_name:
                asset.rent(duration)
                print(f"{asset.name} rented for {duration}")
                return
        print(f"Asset {asset_name} not found.")

asset_manager = AssetManager()
asset_manager.add_asset(Asset("Mouse", "physical"))
asset_manager.add_asset(Asset("IT Consultation", "service"))

asset_manager.list_assets()
asset_manager.rent_asset("Mouse", datetime.timedelta(days=1))
asset_manager.list_assets()
