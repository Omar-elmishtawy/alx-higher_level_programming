#!/usr/bin/python3
import MySQLdb
import sys 

if __name__ == 'main'
    db = MySQLdb.connect(user=sys.argv[0], passwd=sys.argv[1], db=sys.argv[2], port=3306)
    c=db.cursor()
    c.execute("SELECT * FROM states ORDER BY if ASC")
    states = c.fetchall()

    for state in states:
        print(state)
