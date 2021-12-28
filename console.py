import pdb
from models.player import Player
from models.board import Board

import repositories.player_repository as player_repository
import repositories.board_repository as board_repository


player_1 = Player("Jane", "Red", "Not within one space of forest")
player_repository.save(player_1)

player_2 = Player("Roger", "Blue", "Within three spaces of a blue structure")
player_repository.save(player_2)

player_3 = Player("Emma", "Yellow", "Not within one space of a mountain")
player_repository.save(player_3)

board = Board("YNYYNYYNNYNNNNNYNNYNNYYNYYYNYYNYYNYY",
              "YNYYNYYNNYNNYNNYNNYYNYYNYYNNYYNYYNYY",
              "NNYNNYNNYNNYYNNYNNYYNNYNYYNNNNNYYNYY",
              "NNYNNNNNYNNNYNYYNYNYNNYYNNNNYYNYYNYY",
              "NNNNYNNNNYNNYNNYNYNNYNYNNYNNYNNYNNYN",
              "YYNNYNNYNNYNNNNNNYYNNYNNNYNNNNNYNNNN",
              "YYNNYNNYNNYNNYNNNNYNNYNNYNNNNNNNNNNY",
              "YYNNNNNYNNYNNYNYNYYNYYNYYNYNNYNNYNNY",
              "YYNYYNNYNYYNYYNYNYNNNYNYYNYYNYNNYNNY")
board_repository.save(board)
    



# board = Board("YNY YNY YNN YNN NNN YNN YNN YYN YYY NYY NYY NYY
#             YNY YNY YNN YNN YNN YNN YYN YYN YYN NYY NYY NYY
#             NNY NNY NNY NNY YNN YNN YYN NYN YYN NNN NYY NYY
#             NNY NNN NNY NNN YNY YNY NYN NYY NNN NYY NYY NYY
#             NNN NYN NNN YNN YNN YNY NNY NYN NYN NYN NYN NYN
#             YYN NYN NYN NYN NNN NNY YNN YNN NYN NNN NYN NNN
#             YYN NYN NYN NYN NYN NNN YNN YNN YNN NNN NNN NNY
#             YYN NNN NYN NYN NYN YNY YNY YNY YNY NNY NNY NNY
#             YYN YYN NYN YYN YYN YNY NNN YNY YNY YNY NNY NNY")

################################

pdb.set_trace()