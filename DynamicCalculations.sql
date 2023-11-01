-- QUESTION # 1: aceCount
DROP FUNCTION IF EXISTS aceCount;
DELIMITER //
CREATE FUNCTION aceCount(name VARCHAR(20), startDate DATE, finishDate DATE) RETURNS DOUBLE READS SQL DATA
BEGIN
DECLARE aceAVG DOUBLE;
-- Setting dcount (exhibit A)
SET aceAVG = (SELECT AVG(plays.ace)
	FROM plays, tournament, matchinfo, player
		WHERE plays.player_id = player.id
			AND plays.match_id = matchinfo.match_id 
			AND matchinfo.tourney_id = tournament.id
			AND player.name = name
			AND tournament.tourn_date > startDate
			AND tournament.tourn_date < finishDate
		GROUP BY player.name);
RETURN aceAVG;
END
//
DELIMITER ;
-- tested with:
SELECT aceCount('Taylor Fritz', '1968-11-21', '2023-08-11'); -- should output 2


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

-- QUESTION # 3: TopAces
CREATE OR REPLACE VIEW TopAces AS
SELECT nameAndAvg.name FROM (SELECT player.name, AVG(plays.ace) AS playerAces
	FROM plays, tournament, matchinfo, player
		WHERE plays.player_id = player.id
			AND plays.match_id = matchinfo.match_id 
			AND matchinfo.tourney_id = tournament.id
		GROUP BY player.name
	ORDER BY playerAces DESC
	LIMIT 10) AS nameAndAvg;




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



DROP TRIGGER IF EXISTS onInsertionPlayer;
DELIMITER //
CREATE TRIGGER onInsertionPlayer BEFORE INSERT ON player
BEGIN
	IF NEW.country = 'RUS' OR NEW.country = 'EST' THEN
	-- INSERT INTO player SET NEW.country = 'USR';
	SET NEW.country = 'USR';
	-- WHERE player.country = 'RUS' OR player.country = 'EST';
	-- NEW.country = 'USR';
	-- CALL updateCountry(NEW.country);
	END IF;
END
//
DELIMITER ;

INSERT INTO player VALUES ('9999127', 'Test Player', 'RUS', 'R', '56');

SELECT * FROM player WHERE player.country = 'USR';