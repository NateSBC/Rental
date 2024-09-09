import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jFm4q!ri-hXPRkZ",
    database="assetdatabase"
)

mycursor = mydb.cursor()

class Asset:
    """Class to represent an asset."""

    def __init__(self, ID, asset_name, asset_type, asset_quantity):
        self.asset_id = ID
        self.asset_name = asset_name
        self.asset_type = asset_type
        self.asset_quantity = asset_quantity
        
    def create_asset(self):
        sql = "INSERT INTO assets (asset_name, asset_type, asset_quantity) VALUES ( %s, %s, %s)"
        val = (field2_value, field3_value, field4_value)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print("{asset_name}: Asset added successfully!")
        except mysql.connector.Error as err:
            print("Error:", err)
            
    def update_asset(self):
        sql = "UPDATE assets SET asset_name = %s, asset_type = %s, asset_quantity = %s WHERE ID = %s"
        val = (new_field2_value, new_field3_value, new_field4_value, id_to_update)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print("{asset_name}: Asset updated successfully!")
        except mysql.connector.Error as err:
            print("Error:", err)

    def rent(self, name):
        sql = "UPDATE assets SET asset_quantity = asset_quantity - 1 WHERE asset_name = %s"
        val = (name,)
        try:
            mycursor.execute(sql, val)
            mydb.commit()
            print(f"{name}: Asset rented successfully!")
        except mysql.connector.Error as err:
            print("Error:", err)

play_again = "y"
while play_again == "y":

    mycursor.execute("SELECT * FROM assets") 
    # fetch all the matching rows  
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    First_Question = input("\n'Add', 'Update' or 'Rent'?: ")     
    if First_Question == 'Add':
        field2_value = input("Enter Asset Name: ")
        field3_value = input("Enter Asset Type: ")
        field4_value = int(input("Enter Asset Quantity: "))
        new_asset = Asset(None, field2_value, field3_value, field4_value)
        new_asset.create_asset()

    elif First_Question == 'Update':
        id_to_update = int(input("Enter the ID of the row to update: "))
        new_field2_value = input("Enter the new Asset Name: ")
        new_field3_value = input("Enter the new Asset Type: ")
        new_field4_value = int(input("Enter the new Quantity: "))
        up_asset = Asset(None, new_field2_value, new_field3_value, new_field4_value)
        up_asset.update_asset()

    elif First_Question == 'Rent':
        name = input("Enter the name of the Asset to rent: ")
        Asset.rent(None, name)

    elif First_Question == 'q':
        print("You have quit this app successfully")
        break

    play_again = input("Do you want to play again? (y/n): ")

mydb.close()