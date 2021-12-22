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
    map TEXT
    -- player_id INT REFERENCES players(id)
);