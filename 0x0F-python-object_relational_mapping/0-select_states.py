#!/usr/bin/python3
"""script lists all states from databases hbtn_0e_0_usa"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    user, pwd, db = argv[1], argv[2], argv[3]
    con = MySQLdb.connect(host="localhost", port=3306,
                          user=user, password=pwd, database=db)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    data = cursor.fetchall()
    for state in data:
        print(state)
    cursor.close()
    con.close()
