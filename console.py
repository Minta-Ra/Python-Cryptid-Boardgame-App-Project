import pdb
from models.player import Player
from models.board import Board

import repositories.player_repository as player_repository


player_1 = Player("Jane", "Red", "Not within one space of forest")
player_repository.save(player_1)

player_2 = Player("Roger", "Blue", "Within three spaces of a blue structure")
player_repository.save(player_2)

player_3 = Player("Emma", "Yellow", "Not within one space of a mountain")
player_repository.save(player_3)

################################

pdb.set_trace()