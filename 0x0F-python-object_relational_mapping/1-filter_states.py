#!/usr/bin/python3
"""
A module that lists all states from a database
"""

import sys
import MySQLdb


def mydbsql():
    """
    A function that starts a mysqldb connection and returns all
    states with name starting with N in a database
    """
    db = None
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
        cursor = db.cursor()

        sql = """
        SELECT * FROM states
        WHERE name LIKE "N%"
        ORDER BY id ASC
        """

        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            if row[1][0] == 'N':
                print(row)
    except (Exception, MySQLdb.DatabaseError) as error:
        print(error)
    finally:
        if db is not None:
            cursor.close()
            db.close()


if __name__ == "__main__":
    mydbsql()
