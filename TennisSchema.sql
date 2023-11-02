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
	(id				VARCHAR(35),
	 name			VARCHAR(40),
	 tourn_level	CHAR(1),
	 tourn_date		DATE,
	 PRIMARY KEY (id)
	);

DROP TABLE IF EXISTS matchinfo;
CREATE TABLE matchinfo
	(match_id		VARCHAR(36),
	 tourney_id		VARCHAR(35),
	 surface		VARCHAR(10),
	 score			VARCHAR(15),
	 num_sets		INT(1) CHECK(num_sets >= 0),
	 PRIMARY KEY(match_id, tourney_id),
	 FOREIGN KEY (tourney_id) REFERENCES tournament (id) ON DELETE CASCADE
	);

DROP TABLE IF EXISTS plays;
CREATE TABLE plays
	(match_id		VARCHAR(12),
	 player_id		INT(10),
	 win_or_lose	CHAR(1) CHECK(win_or_lose = 'W' OR win_or_lose = 'L'),
	 ace			NUMERIC(3) CHECK(ace >= 0),
	 df				NUMERIC(3) CHECK (df >= 0),
	 fstIn			INT(3) CHECK(fstIn >= 0),
	 first_won		INT(3) CHECK(first_won >= 0),
	 second_won		INT(3) CHECK(second_won >= 0),
	 PRIMARY KEY(match_id, player_id),
	 FOREIGN KEY (match_id) REFERENCES matchinfo (match_id),
	 FOREIGN KEY (player_id) REFERENCES player (id) ON DELETE SET NULL
	);
	
