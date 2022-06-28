import mysql.connector
import pymysql.cursors

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

if db.is_connected():
    print("Berhasil terhubung ke database")