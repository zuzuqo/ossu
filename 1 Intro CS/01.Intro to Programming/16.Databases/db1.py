import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

sql_drop = 'DROP TABLE IF EXISTS Tracks'
sql_create = 'CREATE TABLE Tracks (title TEXT, plays INTEGER)'

cur.execute(sql_drop)
cur.execute(sql_create)

conn.close()
