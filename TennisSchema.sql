DROP SCHEMA IF EXISTS tennishw3;
CREATE SCHEMA tennishw3;

DROP TABLE IF EXISTS player;
CREATE TABLE player
	(id			VARCHAR(8),
	 name		VARCHAR(),
	 dob		DATE(),
	 country	VARCHAR(),
	 hand		VARCHAR(1),
	 height		VARCHAR(),
	 PRIMARY KEY (id)
	);

DROP TABLE IF EXISTS matchinfo;
CREATE TABLE matchinfo
	(match_num		VARCHAR(),
	 surface		VARCHAR(),
	 score			VARCHAR(),
	 num_sets		VARCHAR(),
	 PRIMARY KEY(match_num, tourney_id),
	 FOREIGN KEY (tourney_id) REFERENCES tournament (id)
	);

DROP TABLE IF EXISTS plays;
CREATE TABLE plays
	(match_num		VARCHAR(),
	 player_id		VARCHAR(),
	 winorlose		VARCHAR(),
	 ace			NUMERIC(),
	 df				NUMERIC(),
	 fstIn			NUMERIC(),
	 PRIMARY KEY(match_num, player_id),
	 FOREIGN KEY (match_num) REFERENCES matchinfo (match_num),
	 FOREIGN KEY (palyer_id) REFERENCES player (id)
	);

DROP TABLE IF EXISTS tournament;
CREATE TABLE tournament;
	(id				VARCHAR(),
	 name			VARCHAR(),
	 tourn_evel		INT(),
	 location		VARCHAR(),
	 tourn_date		DATE(),
	 winner			VARCHAR(),
	 PRIMARY KEY (id)
	);
	
