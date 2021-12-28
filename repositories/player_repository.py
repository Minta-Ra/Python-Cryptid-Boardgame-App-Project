from db.run_sql import run_sql

from models.player import Player


def save(player):
    sql = "INSERT INTO players (name, colour, clue) VALUES (%s, %s, %s) RETURNING id"
    values = [player.name, player.colour, player.clue]
    results = run_sql(sql, values)
    player.id = results[0]['id']
    return player

def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for row in results:
        player = Player(row["name"], row["colour"], row["clue"], row["id"])
        players.append(player)
    return players

def select(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        player = Player(result["name"], result["colour"], result["clue"], result["id"])
    return player
