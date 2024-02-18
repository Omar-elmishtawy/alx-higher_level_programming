#!/usr/bin/python3

"""Execute sql queries using MySQLdb"""
import MySQLdb
import sys

if __name__ == 'main':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host='localhost')
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    states = c.fetchall()

    for state in states:
        print(state)
