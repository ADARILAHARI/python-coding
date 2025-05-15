# importing my sql and requied libraries
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd ="root"
)

print(database)

database.close()