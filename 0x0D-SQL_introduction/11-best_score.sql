-- List all records with a score >=10 in the second table
-- Records are ordered by descending score.
-- List only scores that are above or equal to 10 in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC; 
