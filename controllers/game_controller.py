from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.player_repository as player_repository
import repositories.board_repository as board_repository


game_blueprint = Blueprint("game", __name__)

# Create route for game
@game_blueprint.route("/game")
def game():
    players = player_repository.select_all()
    board = board_repository.select_board_by_id(1)
    return render_template("game/index.html", players=players, board=board)

