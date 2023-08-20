#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    user, pwd, db, name = argv[1], argv[2], argv[3], argv[4]
    con = MySQLdb.connect(host="localhost", port=3306, user=user,
                          password=pwd, db=db)
    cursor = con.cursor()
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id".format(name)
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    con.close()
