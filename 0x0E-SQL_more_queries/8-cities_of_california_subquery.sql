-- script lists all the cities of california
SELECT id, state_id, name FROM cities where state_id = (SELECT id FROM states WHERE name = "California") ORDER BY id;
