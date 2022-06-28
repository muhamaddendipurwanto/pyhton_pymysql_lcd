import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_lcd"
)

cursor = db.cursor()
sql = "INSERT INTO pyarduino (isi, tambah) VALUES (%s, %s)"
val = ("SAYA SUKA BELAJAR","ARDUINO DAN PYTHON")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))