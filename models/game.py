class Game():
    def __init__(self, board, players):
        # Board as an object
        self.board = board
        # Players as a list of objects
        self.players = players
        self.map = self.generate_map(board)


    def generate_map(self, board):
        map = []
        # All map fields
        rows = board.row_1 + board.row_2 + board.row_3 + board.row_4 + board.row_5 + board.row_6 + board.row_7 + board.row_8 + board.row_9
        for position in range(0, len(rows) +1):
            if position % 3 == 0 and position != 0:
                # Grab 3 letters [start : end]
                field_result = rows[position - 3 : position]
                # Print to check results of each field (every 3)
                # print(field_result)

                # Generate objects of each field
                single_board_field = {"field_result" : field_result, "player_token" : []}
                map.append(single_board_field)

