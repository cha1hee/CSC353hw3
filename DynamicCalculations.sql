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
SELECT aceCount('Taylor Fritz', '1968-11-21', '2023-08-11'); -- should output 2

