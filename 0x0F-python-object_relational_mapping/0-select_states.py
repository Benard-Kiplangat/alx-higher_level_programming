#!/usr/bin/python3
""" A script that list all states from the database hbtn_0e_0_usa
    Takes arguments from the command line for username, pswd, and name
    Uses MySQLdb and runs on local host at port 3306
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    num_rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    for i in range(num_rows):
        print(cur.fetchone())
