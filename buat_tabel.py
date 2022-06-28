import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_lcd"
)

cursor = db.cursor()
sql = """CREATE TABLE pyarduino (
 isi VARCHAR(255),
 tambah VARCHAR(255)
)
"""

cursor.execute(sql)

print("Tabel Python Arduino berhasil dibuat!")