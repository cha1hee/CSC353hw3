DROP FUNCTION IF EXISTS dept_countF;
DELIMITER //
CREATE FUNCTION dept_countF(dept_name VARCHAR(20)) RETURNS INTEGER READS SQL DATA
BEGIN
DECLARE dcount INT;
-- Setting dcount (exhibit A)
SET dcount = (SELECT COUNT(*)
FROM instructor
WHERE instructor.dept_name = dept_name);
-- Setting dcount (exhibit B)
SELECT COUNT(*) INTO dcount
FROM instructor
WHERE instructor.dept_name = dept_name;
RETURN dcount;
END
//
DELIMITER ;
SELECT dept_countF(‘History’); -- should output 2
SET @historyCount = dept_countF(‘History’);
SELECT @historyCount; -- should also output 2
DROP PROCEDURE IF EXISTS dept_countP;
DELIMITER //
CREATE PROCEDURE dept_countP(IN dept_name VARCHAR(20), OUT dcount INT)
BEGIN
SELECT COUNT(*) INTO dcount
FROM instructor
WHERE instructor.dept_name = dept_name;
END
//
DELIMITER ;
CALL dept_countP(‘History’, @xyz);
SELECT @xyz; -- should output 2