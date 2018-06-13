import sqlite3
import os,sys

d_path = sys.argv[1].split('.')[0]

conn = sqlite3.connect('./project_message.db')
cursor = conn.cursor()
command = "SELECT * FROM %s" % (d_path)
cursor.execute(command) 
data = cursor.fetchall()

for row in data:
    print (row)
