from .asset import Asset
import mysql.connector

class AssetManager:
    def __init__(self):
        self.db_config = {
            'host': 'localhost',
            'port': '33060',
            'user': 'root',
            'password': 'jFm4q!ri-hXPRkZ',
            'database': 'assetdatabase'
        }
        self.assets = []
        self.next_id = 1
    
    def connect_to_db(self):
        try:
            self.conn = mysql.connector.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            print("Connected to MySQL database successfully.")
        except mysql.connector.Error as err:
            print("Error connecting to MySQL database:", err)

    def create_asset(self, asset_name, asset_type, asset_quantity):
        new_asset = Asset(self.next_id, asset_name, asset_type, asset_quantity )  # Availability set to True by default
        
        
        sql = "INSERT INTO assets (asset_id, name, type, purchase_date, asset_quantity, availability) VALUES (%s, %s, %s, %s)"
        val = (new_asset.asset_id, new_asset.asset_name, new_asset.asset_type, new_asset.asset_quantity)

        try:
            self.cursor.execute(sql, val)
            self.conn.commit()
            print("Asset added to the database successfully.")
        except mysql.connector.Error as err:
            print("Error adding asset to the database:", err)
        
        
        new_asset.asset_id = self.next_id
        self.assets.append(new_asset)
        self.next_id += 1  # Increments the ID +1 for next asset
        return new_asset
    
    