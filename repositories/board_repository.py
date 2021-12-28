from db.run_sql import run_sql
from models.board import Board


def save(board):
    sql = "INSERT INTO board (row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [board.row_1, board.row_2, board.row_3, board.row_4, board.row_5, board.row_6, board.row_7, board.row_8, board.row_9]
    results = run_sql(sql, values)
    board.id = results[0]['id']
    return board

def select_board_by_id(id):
    board = None
    sql = "SELECT * FROM board WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        board = Board(result["row_1"], result["row_2"], result["row_3"], result["row_4"], result["row_5"], result["row_6"], result["row_7"], result["row_8"], result["row_9"], result["id"])
    return board