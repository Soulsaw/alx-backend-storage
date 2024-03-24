-- this script compute in store a student average
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN p_user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;

    -- Compute average score
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    -- Update or insert average score for the user
    UPDATE users SET average_score = avg_score WHERE id = p_user_id;
END;
//

DELIMITER ;
