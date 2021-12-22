from db.run_sql import run_sql

from models.player import Player



def save(player):
    sql = "INSERT INTO players (name, colour, clue) VALUES (%s, %s, %s) RETURNING id"
    values = [player.name, player.colour, player.clue]
    results = run_sql(sql, values)
    player.id = results[0]['id']
    return player