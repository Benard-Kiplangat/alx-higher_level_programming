#!/usr/bin/python3
# A script that list all cities that matches the given name from the arguments
# Takes arguments from the command line for username, pswd, name, and state
# Uses MySQLdb and runs on local host at port 3306

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT c.name FROM cities AS c INNER JOIN states AS s ON c.state_id = s.id WHERE s.name=%s ORDER BY c.id ASC", (sys.argv[4], ))
    print(", ".join([row[0] for row in cur.fetchall()]))
    cur.close()
    conn.close()
