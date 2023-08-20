#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user, pwd, db, state = argv[1:5]
    con = MySQLdb.connect(host="localhost", port=3306,
                          user=user, password=pwd, db=db)
    cursor = con.cursor()
    query = "SELECT name FROM cities WHERE\
             state_id = (SELECT id FROM states WHERE name LIKE BINARY %s)\
             ORDER BY id"
    cursor.execute(query, (state,))
    cities = cursor.fetchall()
    cities = [city[0] for city in cities]
    print(", ".join(cities))
    cursor.close()
    con.close()
