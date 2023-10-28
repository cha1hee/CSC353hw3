DROP SCHEMA IF EXISTS tennishw3;
CREATE SCHEMA tennishw3;
USE tennishw3;

DROP TABLE IF EXISTS player;
CREATE TABLE player
	(id 		VARCHAR(6),
	 name		VARCHAR(33),
	 country	VARCHAR(3),
	 hand		VARCHAR(1),
	 height		VARCHAR(4),
	 PRIMARY KEY (id)
	);

DROP TABLE IF EXISTS tournament;
CREATE TABLE tournament
	(id				VARCHAR(6),
	 name			VARCHAR(10),
	 tourn_level	VARCHAR(2),
	 tourn_date		DATE,
	 PRIMARY KEY (id)
	);

DROP TABLE IF EXISTS matchinfo;
CREATE TABLE matchinfo
	(match_num		VARCHAR(6),
	 tourney_id		VARCHAR(6),
	 surface		VARCHAR(5),
	 score			VARCHAR(20),
	 num_sets		VARCHAR(1),
	 PRIMARY KEY(match_num, tourney_id),
	 FOREIGN KEY (tourney_id) REFERENCES tournament (id)
	);

DROP TABLE IF EXISTS plays;
CREATE TABLE plays
	(match_num		VARCHAR(6),
	 player_id		VARCHAR(6),
	 winorlose		VARCHAR(1),
	 ace			NUMERIC(2),
	 df				NUMERIC(2),
	 fstIn			NUMERIC(2),
	 PRIMARY KEY(match_num, player_id),
	 FOREIGN KEY (match_num) REFERENCES matchinfo (match_num),
	 FOREIGN KEY (player_id) REFERENCES player (id)
	);
	
