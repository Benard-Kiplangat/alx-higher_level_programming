#!/usr/bin/python3
"""A script that list all states with a name starting with capital N
 Takes arguments from the command line for username, pswd, and name
 Uses MySQLdb and runs on local host at port 3306
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    conn.close()
