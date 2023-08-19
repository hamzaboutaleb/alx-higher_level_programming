#!/usr/bin/python3
import MySQLdb
from sys import argv
"""script lists all states from databases hbtn_0e_0_usa"""

if __name__ == "__main__":
    user = argv[1]
    pwd = argv[2]
    db = argv[3]
    con = MySQLdb.connect(
        host="localhost", port=3306, user=user, password=pwd,
        database=db
        )
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    data = cursor.fetchall()
    for state in data:
        print(state)
    cursor.close()
    db.close()
