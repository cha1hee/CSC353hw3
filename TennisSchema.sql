DROP SCHEMA IF EXISTS tennishw3;
CREATE SCHEMA tennishw3;
USE tennishw3;

DROP TABLE IF EXISTS player;
CREATE TABLE player
	(id MEDIUMINT NOT NULL AUTO_INCREMENT,
	 name		VARCHAR(33),
	 country	VARCHAR(3),
	 hand		VARCHAR(1),
	 height		VARCHAR(4),
	 PRIMARY KEY (id)
	);

DROP TABLE IF EXISTS tournament;
CREATE TABLE tournament
	(id				VARCHAR(2),
	 name			VARCHAR(2),
	 tourn_evel		NUMERIC(2),
	 location		VARCHAR(2),
	 tourn_date		DATE,
	 winner			VARCHAR(2),
	 PRIMARY KEY (id)
	);

DROP TABLE IF EXISTS matchinfo;
CREATE TABLE matchinfo
	(match_num		VARCHAR(1),
	 tourney_id		VARCHAR(1),
	 surface		VARCHAR(1),
	 score			VARCHAR(1),
	 num_sets		VARCHAR(1),
	 PRIMARY KEY(match_num, tourney_id),
	 FOREIGN KEY (tourney_id) REFERENCES tournament (id)
	);

DROP TABLE IF EXISTS plays;
CREATE TABLE plays
	(match_num		VARCHAR(1),
	 player_id		MEDIUMINT,
	 winorlose		VARCHAR(1),
	 ace			NUMERIC(1),
	 df				NUMERIC(1),
	 fstIn			NUMERIC(1),
	 PRIMARY KEY(match_num, player_id),
	 FOREIGN KEY (match_num) REFERENCES matchinfo (match_num),
	 FOREIGN KEY (player_id) REFERENCES player (id)
	);
	
