import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jFm4q!ri-hXPRkZ",
    database="assetdatabase"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM assets") 
  
# fetch all the matching rows  
result = mycursor.fetchall() 
  
# loop through the rows 
for row in result: 
    print(row) 
    print("\n") 