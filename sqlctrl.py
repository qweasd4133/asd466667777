import sqlite3

conn = sqlite3.connect('Devops.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM produck_info')
records = cursor.fetchall()
print (records)