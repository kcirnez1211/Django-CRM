import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE fiesta")

print("ALL DONE!")