import mysql.connector
 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jFm4q!ri-hXPRkZ",
    database="assetdatabase"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("SELECT * FROM assets")
 
myresult = mycursor.fetchall()
 
for x in myresult:
    print(x)