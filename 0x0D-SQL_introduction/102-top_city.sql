-- displays the top 3 of cities temperature during July and August ordered

SELECT city, AVG(value) as avg_temp from temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
