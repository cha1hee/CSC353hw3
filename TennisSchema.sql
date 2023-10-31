DROP SCHEMA IF EXISTS tennishw3;
CREATE SCHEMA tennishw3;
USE tennishw3;

DROP TABLE IF EXISTS player;
CREATE TABLE player
	(id 		VARCHAR(10),
	 name		VARCHAR(33),
	 country	VARCHAR(3),
	 hand		VARCHAR(1),
	 height		VARCHAR(4),
	 PRIMARY KEY (id)
	);

DROP TABLE IF EXISTS tournament;
CREATE TABLE tournament
	(id				VARCHAR(40),
	 name			VARCHAR(40),
	 tourn_level	VARCHAR(2),
	 tourn_date		DATE,
	 PRIMARY KEY (id)
	);

DROP TABLE IF EXISTS matchinfo;
CREATE TABLE matchinfo
	(match_id		VARCHAR(80),
	 tourney_id		VARCHAR(40),
	 surface		VARCHAR(10),
	 score			VARCHAR(50),
	 num_sets		VARCHAR(1),
	 PRIMARY KEY(match_id, tourney_id),
	 FOREIGN KEY (tourney_id) REFERENCES tournament (id) ON DELETE CASCADE
	);

DROP TABLE IF EXISTS plays;
CREATE TABLE plays
	(match_id		VARCHAR(80),
	 player_id		VARCHAR(10),
	 winorlose		VARCHAR(1),
	 ace			NUMERIC(3),
	 df				NUMERIC(3),
	 fstIn			INT(3),
	 PRIMARY KEY(match_id, player_id),
	 FOREIGN KEY (match_id) REFERENCES matchinfo (match_id),
	 FOREIGN KEY (player_id) REFERENCES player (id) ON DELETE SET NULL
	);
	
