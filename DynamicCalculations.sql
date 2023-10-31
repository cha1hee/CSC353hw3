-- EXAMPLE FUNCTION
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

-- EXAMPLE PROCEDURE
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



-- QUESTION # 2: showAggregateStatistics
DROP PROCEDURE IF EXISTS showAggregateStatistics;
DELIMITER //
CREATE PROCEDURE showAggregateStatistics(IN name VARCHAR(33), start DATE, finish DATE)
BEGIN
SELECT 
	player.name AS name, 
	AVG(ace) AS aces, 
	AVG(df) AS double_faults, 
	AVG(fstIn) AS first_in 
		FROM plays, player, tournament, matchinfo 
			WHERE 
				player.id = plays.player_id AND 
				player.name = name AND 
				tournament.tourn_date > start AND 
				tournament.tourn_date < finish AND 
				matchinfo.tourney_id = tournament.id AND 
				plays.match_id = matchinfo.match_id
		GROUP BY player.name;
END
//
DELIMITER ;
-- tested with:
CALL showAggregateStatistics('Taylor Fritz', '1968-11-21', '2023-01-02');

-- FOR TESTING PURPOSES
-- test procedure (just displays all data for the person within selected date range)
DROP PROCEDURE IF EXISTS testAggregateStatistics;
DELIMITER //
CREATE PROCEDURE testAggregateStatistics(IN name VARCHAR(33), start DATE, finish DATE)
BEGIN
SELECT player.name AS name, ace, df, fstIn FROM plays, player, tournament, matchinfo 
WHERE player.id = plays.player_id AND player.name = name AND tournament.tourn_date > start AND tournament.tourn_date < finish AND matchinfo.tourney_id = tournament.id AND plays.match_id = matchinfo.match_id;
END
//
DELIMITER ;
CALL testAggregateStatistics('Taylor Fritz', '1968-11-21', '2023-01-02');
