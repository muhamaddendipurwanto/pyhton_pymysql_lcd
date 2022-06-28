from pyfirmata import Arduino, util, STRING_DATA
board = Arduino('COM4')
import time

from unittest import result
import mysql.connector
time.sleep(1)

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


board.send_sysex( STRING_DATA, util.str_to_two_byte_iter(format(result) ))

def msg( text ):
    if text:
        board.send_sysex( STRING_DATA, util.str_to_two_byte_iter( format(text )) )