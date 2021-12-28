from db.run_sql import run_sql


def save(board):
    sql = "INSERT INTO board (row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [board.row_1, board.row_2, board.row_3, board.row_4, board.row_5, board.row_6, board.row_7, board.row_8, board.row_9]
    results = run_sql(sql, values)
    board.id = results[0]['id']
    return board