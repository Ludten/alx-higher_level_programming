#!/usr/bin/python3
"""
A module that lists all cities from a database
"""

import sys
import MySQLdb


def mydbsql():
    """
    A function that starts a mysqldb connection and returns all
    cities in a particular state in a database
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
        SELECT c.name, s.name
        FROM cities c
        JOIN states s
        ON c.state_id = s.id
        WHERE s.name = %s
        ORDER BY c.id ASC;
        """

        cursor.execute(sql, (sys.argv[4], ))
        print(', '.join(["{:s}".format(row[0])
                         for row in cursor.fetchall()]))
    except (Exception, MySQLdb.DatabaseError) as error:
        print(error)
    finally:
        if db is not None:
            cursor.close()
            db.close()


if __name__ == "__main__":
    mydbsql()
