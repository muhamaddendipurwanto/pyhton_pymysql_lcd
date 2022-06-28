from unittest import result
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_lcd"
)

cursor = db.cursor()
sql = "SELECT * FROM pyarduino"
cursor.execute(sql)

result = cursor.fetchone()


print(result)