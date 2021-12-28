from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.player_repository as player_repository


players_blueprint = Blueprint("players", __name__)

# Show player's clue
@players_blueprint.route("/game/clue/<id>")
def show_players(id):
    player = player_repository.select(id)
    return render_template("game/showclue.html", player=player)
