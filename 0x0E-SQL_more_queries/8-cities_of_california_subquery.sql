-- lists all the cities of California that can be found in the database hbtn_0d_usa

SELECT cities.id, cities.name FROM cities c JOIN states s ON c.state_id = s.id WHERE s.name = California;
