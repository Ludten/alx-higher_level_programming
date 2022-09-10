#!/usr/bin/python3
"""
A module that lists all states from a database
"""

import sys
from unicodedata import name
import MySQLdb


def mydbsql():
    db = None
    try:
        db = MySQLdb.connect(
            host='127.0.0.1',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
        db.autocommit = True
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id")
        rows = cursor.fetchall()
        for row in rows:
            print("{}".format(row))
    except (Exception, MySQLdb.DatabaseError) as error:
        print(error)
    finally:
        if db is not None:
            db.close()


if __name__ == "__main__":
    mydbsql()
