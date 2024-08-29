"""Module providing a function printing python version."""

from package.asset_manager import AssetManager
import datetime

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
