import mysql.connector

conn = mysql.connector.connect(host = "localhost", database = "dbmusic", user = "root", password = "T34ch3rL3mp10!")

if conn.is_connected():
    print("Connected to MySql Database, dbmusic")
else:
    print("Connection failed")

cursor = conn.cursor() # create an instance of the cursor

