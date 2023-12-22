#!/usr/bin/python3
"""A script that list all states with a name that matches the argument provided
 Takes arguments from the command line for username, pswd, name, and state
 Uses MySQLdb and runs on local host at port 3306
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name='{:s}'\
    ORDER BY states.id".format(argv[4])
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
