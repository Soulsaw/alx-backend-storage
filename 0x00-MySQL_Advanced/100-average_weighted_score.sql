-- this script compute in store a student average
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
    IN p_user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;

    -- Compute average score
    SELECT SUM(score * weight) / SUM(weight) INTO avg_score
    FROM corrections AS c, projects AS p
    WHERE p.id = c.project_id AND c.user_id = p_user_id;

    -- Update or insert average score for the user
    UPDATE users SET average_score = avg_score WHERE id = p_user_id;
END;
//

DELIMITER ;
