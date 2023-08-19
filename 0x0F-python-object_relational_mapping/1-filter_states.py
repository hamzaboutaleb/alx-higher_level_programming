#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    usr, pwd, db = argv[1], argv[2], argv[3]
    con = MySQLdb.connect(host="localhost", port=3306,
                          user=usr, password=pwd, db=db)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    con.close()
