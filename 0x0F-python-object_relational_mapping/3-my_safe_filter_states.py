#!/usr/bin/python3
"""
Write a script that takes in an argument and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    usr, pwd, db, name = argv[1:5]
    con = MySQLdb.connect(host="localhost", port=3306,
                          user=usr, password=pwd, db=db)
    cursor = con.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id"
    cursor.execute(query, (name,))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    con.close()
