-- This script compute the average score of a student
DELIMITER @@
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT
)
BEGIN
	DECLARE user_score FLOAT;
	SELECT AVG(score) INTO user_score FROM corrections WHERE user_id = user_id;

	-- update the user score
	UPDATE users SET average_score = user_score WHERE id = user_id;
END;
@@
DELIMITER ;
