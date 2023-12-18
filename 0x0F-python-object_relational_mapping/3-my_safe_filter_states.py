#!/usr/bin/python3
# A script that list all states with a name that matches the argument provided
# This script should be safe from sql injection unlike the last script
# Takes arguments from the command line for username, pswd, name, and state
# Uses MySQLdb and runs on local host at port 3306

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT * FROM states")
    [print (row) for row in cur.fetchall() if row[1] == sys.argv[4]]
    cur.close()
    conn.close()
