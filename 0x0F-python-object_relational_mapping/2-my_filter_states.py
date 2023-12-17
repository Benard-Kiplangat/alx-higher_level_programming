#!/usr/bin/python3
import MySQLdb
import sys

conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = conn.Cursor()
cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC".format(sys.argv[3]))

query_rows = cur.fechall()
for row in query_rows:
    print(row)

cur.close()
conn.close()
