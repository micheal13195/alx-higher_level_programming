-- List all records with a score >=10 in the second table
-- Records are ordered by descending score.
-- List only scores that are above or equal to 10 in descending order
SELECT `score >= 10`, `name`
FROM `second_table`
ORDER BY `score` DESC; 
