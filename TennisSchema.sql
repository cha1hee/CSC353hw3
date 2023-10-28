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
	(id MEDIUMINT NOT NULL AUTO_INCREMENT,
	 name			VARCHAR(20),
	 tourn_level	VARCHAR(3),
	 tourn_date		DATE,
	 PRIMARY KEY (id)
	);

DROP TABLE IF EXISTS matchinfo;
CREATE TABLE matchinfo
	(match_num MEDIUMINT NOT NULL AUTO_INCREMENT,
	 tourney_id		VARCHAR(),
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
	 win_or_lose	VARCHAR(1),
	 ace			NUMERIC(1),
	 df				NUMERIC(1),
	 fstIn			NUMERIC(1),
	 PRIMARY KEY(match_num, player_id),
	 FOREIGN KEY (match_num) REFERENCES matchinfo (match_num),
	 FOREIGN KEY (player_id) REFERENCES player (id)
	);
	
