USE sql_tic_tac_toe;

CREATE TABLE score(
	match_id INT PRIMARY KEY AUTO_INCREMENT,
    won_p1 INT DEFAULT 0,
    lost_p1 INT DEFAULT 0,
    won_p2 INT DEFAULT 0,
    lost_p2 INT DEFAULT 0
);

CREATE TABLE player(
	player_id INT PRIMARY KEY AUTO_INCREMENT,
	player_name VARCHAR(20),
    match_id INT NOT NULL
);

ALTER TABLE player ADD FOREIGN KEY (match_id) REFERENCES score(match_id);

DESCRIBE score;
DESCRIBE player;

SELECT * FROM score;
SELECT * FROM player;

SELECT * FROM score INNER JOIN player ON score.match_id = player.match_id WHERE player.match_id = 46;

SELECT last_insert_id();

SELECT match_id FROM player WHERE match_id = 2;

DELETE FROM score WHERE match_id = 1;

ALTER TABLE player AUTO_INCREMENT = 0;
ALTER TABLE score AUTO_INCREMENT = 0;

DROP TABLE player;
DROP TABLE score;
