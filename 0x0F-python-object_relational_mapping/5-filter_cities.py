#!/usr/bin/python3

"""
list all states
"""


import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    sql = """SELECT c.id, c.name
        FROM cities AS c
        WHERE c.state_id = (SELECT id FROM states
        WHERE name = %s)
        ORDER BY c.id ASC"""

    cursor.execute(sql, (sys.argv[4],))

    data = cursor.fetchall()
    print(", ".join(row[1] for row in data))

    cursor.close()
    db.close()
