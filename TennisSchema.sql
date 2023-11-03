DROP SCHEMA IF EXISTS tennishw3;
CREATE SCHEMA tennishw3;
USE tennishw3;

DROP TABLE IF EXISTS player;
CREATE TABLE player
	(id 		INT,
	 name		VARCHAR(33),
	 country	VARCHAR(3),
	 hand		CHAR(1) CHECK(hand = 'R' OR hand = 'L' OR hand = 'U' OR hand = 'A'),
	 height		INT CHECK(height >= 0),
	 PRIMARY KEY (id)
	);

DROP TABLE IF EXISTS tournament;
CREATE TABLE tournament
	(id				VARCHAR(36),
	 name			VARCHAR(40),
	 tourn_level	CHAR(1),
	 tourn_date		DATE,
	 PRIMARY KEY (id)
	);

DROP TABLE IF EXISTS matchinfo;
CREATE TABLE matchinfo
	(match_id		VARCHAR(37),
	 tourney_id		VARCHAR(36),
	 surface		VARCHAR(10),
	 score			VARCHAR(34),
	 num_sets		INT CHECK(num_sets >= 0),
	 PRIMARY KEY(match_id),
	 FOREIGN KEY (tourney_id) REFERENCES tournament (id) ON DELETE CASCADE
	);

DROP TABLE IF EXISTS plays;
CREATE TABLE plays
	(play_id		VARCHAR(15),
	 match_id		VARCHAR(37),
	 player_id		INT,
	 win_or_lose	CHAR(1) CHECK(win_or_lose = 'W' OR win_or_lose = 'L'),
	 ace			INT CHECK(ace >= 0),
	 df				INT CHECK (df >= 0),
	 fstIn			INT CHECK(fstIn >= 0),
	 first_won		INT CHECK(first_won >= 0),
	 second_won		INT CHECK(second_won >= 0),
	 PRIMARY KEY(play_id),
	 FOREIGN KEY (match_id) REFERENCES matchinfo (match_id) ON DELETE SET NULL,
	 FOREIGN KEY (player_id) REFERENCES player (id) ON DELETE SET NULL
	);

SELECT * FROM plays WHERE plays.player_id = '100003';

DELETE FROM player WHERE player.id = '100003';

SELECT * FROM plays WHERE plays.match_id = '1968-311-241';

SELECT * FROM matchinfo WHERE tourney_id = '1968-311';

DELETE FROM tournament WHERE id = '1968-311';