#!/usr/bin/python3
"""List all states using mysqldb"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states "
                "WHERE SUBSTR(name, 1, 1)='N' COLLATE latin1_general_cs "
                "ORDER BY id")
    for row in cur.fetchall():
        print("({}, '{}')".format(row[0], row[1]))
