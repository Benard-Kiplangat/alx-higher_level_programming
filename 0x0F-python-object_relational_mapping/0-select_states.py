#!/usr/bin/python3
# A script that list all states from the database hbtn_0e_0_usa
# Takes arguments from the command line for username, pswd, and name
# Uses MySQLdb and runs on local host at port 3306

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
                host="localhost", port=3306,
                user=sys.argv[1], passwd=sys.argv[2],
                db=sys.argv[3], charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
