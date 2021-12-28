DROP TABLE IF EXISTS board;
DROP TABLE IF EXISTS players;


CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    colour VARCHAR(255),
    clue VARCHAR(255)
);

CREATE TABLE board (
    id SERIAL PRIMARY KEY,
    row_1 VARCHAR(255),
    row_2 VARCHAR(255),
    row_3 VARCHAR(255),
    row_4 VARCHAR(255),
    row_5 VARCHAR(255),
    row_6 VARCHAR(255),
    row_7 VARCHAR(255),
    row_8 VARCHAR(255),
    row_9 VARCHAR(255)
    -- player_id INT REFERENCES players(id)
);