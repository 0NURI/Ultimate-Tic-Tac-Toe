# PlayerAI.py
import copy, random
from Utils import (
    CheckGlobalWin, CheckGlobalDraw,
    check_win_matrix, extract_symbol_matrix
)

def moves_for_board(symbols, board_statuses, active_board):
    if active_board is None:
        for board_row in range(3):
            for board_col in range(3):
                if board_statuses[board_row][board_col] is None:
                    for cell_row in range(3):
                        for cell_col in range(3):
                            if symbols[board_row][board_col][cell_row][cell_col] == "":
                                yield (board_row, board_col, cell_row, cell_col)
    else:
        board_row, board_col = active_board
        if board_statuses[board_row][board_col] is None:
            for cell_row in range(3):
                for cell_col in range(3):
                    if symbols[board_row][board_col][cell_row][cell_col] == "":
                        yield (board_row, board_col, cell_row, cell_col)


def simulate_move(symbols, board_statuses, move, player_symbol):
    board_row, board_col, cell_row, cell_col = move
    symbols[board_row][board_col][cell_row][cell_col] = player_symbol

    mini_board = symbols[board_row][board_col]
    winner = check_win_matrix(mini_board)
    if (winner):
        board_statuses[board_row][board_col] = winner
    elif all(cell for row in mini_board for cell in row):
        board_statuses[board_row][board_col] = "draw"

    next_board = (cell_row, cell_col)
    if board_statuses[cell_row][cell_col] is not None:
        next_board = None
    return next_board

def minimax(symbols, board_statuses, active_board, depth, is_max_turn, ai_symbol, player_symbol, alpha=float('-inf'), beta=float('inf')):
    winner = CheckGlobalWin(board_statuses)
    if winner == ai_symbol: return 10 - depth
    if winner == player_symbol: return depth - 10
    if CheckGlobalDraw(board_statuses): return 0
    if depth == 0: return 0  # потенциально можно что-то придумать

    if is_max_turn: # робот играет
        best_score = float('-inf')
        for move in moves_for_board(symbols, board_statuses, active_board):
            symbols_copy, statuses_copy = copy.deepcopy(symbols), copy.deepcopy(board_statuses)
            next_board = simulate_move(symbols_copy, statuses_copy, move, ai_symbol)
            score = minimax(symbols_copy, statuses_copy, next_board, depth-1, False, ai_symbol, player_symbol, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else: # кожаный играет
        best_score = float('inf')
        for move in moves_for_board(symbols, board_statuses, active_board):
            symbols_copy, statuses_copy = copy.deepcopy(symbols), copy.deepcopy(board_statuses)
            next_board = simulate_move(symbols_copy, statuses_copy, move, player_symbol)
            score = minimax(symbols_copy, statuses_copy, next_board, depth-1, True, ai_symbol, player_symbol, alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

def best_move(boards, state, depth):
    symbols = extract_symbol_matrix(boards)
    board_statuses = copy.deepcopy(state.mini_board_statuses)

    best_score = float('-inf')
    best_move_found = None
    for move in moves_for_board(symbols, board_statuses, state.active_board):
        symbols_copy, statuses_copy = copy.deepcopy(symbols), copy.deepcopy(board_statuses)
        next_board = simulate_move(symbols_copy, statuses_copy, move, state.ai_symbol)
        score = minimax(symbols_copy, statuses_copy, next_board, depth-1, False,
                        state.ai_symbol, state.player_symbol)
        if score > best_score:
            best_score, best_move_found = score, move
    return best_move_found

def random_move(boards, state):
    symbols = extract_symbol_matrix(boards)
    possible_moves = list(moves_for_board(symbols, state.mini_board_statuses, state.active_board))
    return random.choice(possible_moves) if possible_moves else None

def MakeAIMove(boards, state):
    level = state.difficulty or "easy"

    # первый ход — играем в центр или угол, если все мини-доски ещё пустые
    if state.active_board is None and all(
        status is None for row in state.mini_board_statuses for status in row
    ):
        preferred_positions = [(1, 1), (0, 0), (0, 2), (2, 0), (2, 2)]  # центр, затем углы
        for board_row, board_col in preferred_positions:
            mini_board = boards[board_row][board_col]
            for cell_row, cell_col in preferred_positions:
                if mini_board.cells[cell_row][cell_col]["text"] == "":
                    from ButtonClickHandler import HandleClick
                    HandleClick(board_row, board_col, cell_row, cell_col, boards, state)
                    return

    if level == "easy":
        move = random_move(boards, state)
    else:
        depth = {"medium": 4, "hard": 6}.get(level, 2)
        move = best_move(boards, state, depth)

    if move:
        from ButtonClickHandler import HandleClick
        HandleClick(*move, boards, state)
