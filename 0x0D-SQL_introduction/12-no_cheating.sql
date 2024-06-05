-- script that updates the score of Bob to 10 in the second_table
FROM `second_table`
WHERE `name` = Bob
UPDATE `second_table` (`score` 10)
