import mysql.connector

class Asset:
    """Class to represent an asset."""

    def __init__(self, ID, asset_name, asset_type, asset_quantity, availability):
        self.asset_id = ID
        self.name = asset_name
        self.type = asset_type
        self.asset_quantity = asset_quantity
        self.availability = availability

    def rent(self):
        """Decrements asset quantity and updates availability if rented."""
        if self.availability:
            self.asset_quantity -= 1
            print(f"{self.name} rented successfully!")
        else:
            print(f"Sorry, {self.name} is currently unavailable.")

    def return_asset(self):
        """Increases asset quantity and updates availability if returned."""
        if not self.availability:
            self.asset_quantity += 1
            print(f"{self.name} returned successfully!")
        else:
            print(f"{self.name} is already available.")


class AssetManager:
    """Class to manage assets using a MySQL database."""

    def __init__(self):
        # Load credentials from environment variables (recommended)
        self.db_config = {
            'host': 'localhost',
            'port': '33060',  # Double-check the actual port
            'user': ['root'],
            'password': ['jFm4q!ri-hXPRkZ'],
            'database': 'assetdatabase'
        }
        self.connect_to_db()  # Connect on initialization

    def connect_to_db(self):
        try:
            self.conn = mysql.connector.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            print("Connected to MySQL database successfully.")
        except mysql.connector.Error as err:
            print("Error connecting to MySQL database:", err)
            exit(1)  # Exit program on critical error

    def create_asset(self, name, type, asset_quantity):
        """Creates a new asset and inserts it into the database."""
        sql = "INSERT INTO assets (name, type, asset_quantity) VALUES ( %s, %s, %s)"
        val = (name, type, asset_quantity)
        try:
            self.cursor.execute(sql, val)
            self.conn.commit()
            print("Asset added to the database successfully.")
            # Retrieve ID using LAST_INSERT_ID()
            self.cursor.execute("SELECT LAST_INSERT_ID()")
            new_id = self.cursor.fetchone()[0]
            return Asset(new_id, name, type, asset_quantity)
        except mysql.connector.Error as err:
            print("Error adding asset to the database:", err)
            return None

    def get_all_assets(self):
        """Fetches all assets from the database and returns a list of Asset objects."""
        sql = "SELECT * FROM assets"
        self.cursor.execute(sql)
        return [Asset(row[0], row[1], row[2], row[3], row[4]) for row in self.cursor.fetchall()]

    def get_asset_by_id(self, asset_id):
        """Fetches a specific asset by ID and returns an Asset object."""
        sql = "SELECT * FROM assets WHERE asset_id = %s"
        val = (asset_id,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result:
            return Asset(*result)  # Unpack data to create an Asset object
        else:
            return None

    def update_asset(self, asset_id, asset_name=None, asset_type=None, asset_quantity=None, availability=None):
        """Updates an existing asset in the database with optional parameters."""
        sql = "UPDATE assets SET "
        updates = []
        params = []
        if asset_name is not None:
            updates.append("name=%s")
            params.append(asset_name)
        if asset_type is not None:
            updates.append("type=%s")
            params.append(asset_type)
        if asset_quantity is not None:
            updates.append("asset_quantity=%s")
            params.append(asset_quantity)
        if availability is not None:
            updates.append("availability=%s")
            params.append(availability)
        if not updates:
            return False  # No updates to apply
        sql += ", ".join(updates) + " WHERE asset_id=%s"
        params.append(asset_id)
        try:
            self.cursor.execute(sql, params)
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print("Error updating asset:", err)
            return False

    def delete_asset(self, asset_id):
        """Deletes an asset from the database."""
        sql = "DELETE FROM assets WHERE asset_id = %s"
        val = (asset_id,)
        try:
            self.cursor.execute(sql, val)
            self.conn.commit()
            print("Asset deleted successfully.")
        except mysql.connector.Error as err:
            print("Error deleting asset:", err)

    def close_connection(self):
        """Closes the database connection."""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

# Example usage
asset_manager = AssetManager()

# Create new assets
asset1 = asset_manager.create_asset("Laptop", "Hardware", 4)
asset2 = asset_manager.create_asset("Microsoft Office", "Software", 5)

# Get all assets
assets = asset_manager.get_all_assets()
for asset in assets:
    print(f"Asset ID: {asset.asset_id}, Name: {asset.name}, Type: {asset.type}, Quantity: {asset.asset_quantity}")

# Rent an asset
asset1.rent()

# Return an asset
asset1.return_asset()

# Update an asset
asset1.name = "New Laptop"
asset_manager.update_asset(asset1.asset_id, asset_name=asset1.name)

# Delete an asset
asset_manager.delete_asset(asset2.asset_id)

# Close the connection
asset_manager.close_connection()