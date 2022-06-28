import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_lcd"
)
txt_isi = input(" ")
txt_tambah = input(" ")

cursor = db.cursor()
sql = "UPDATE pyarduino SET isi=%s, tambah=%s"
val = (txt_isi, txt_tambah)
cursor.execute(sql, val)

db.commit()

print("{} data diubah".format(cursor.rowcount))