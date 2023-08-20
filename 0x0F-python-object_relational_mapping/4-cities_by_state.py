#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    usr, pwd, db = argv[1:4]
    con = MySQLdb.connect(host="localhost", port=3306,
                          user=usr, password=pwd, db=db)
    cursor = con.cursor()
    query = "SELECT c.id, c.name, s.name FROM cities c\
             JOIN states s ON c.state_id = s.id"
    cursor.execute(query)
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    con.close()
