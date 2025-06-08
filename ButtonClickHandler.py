from Utils import *

def HandleClick(br, bc, fr, fc, boards, state):
    if state.game_over: return

    # Проверка: можно ли ходить на эту мини-доску
    if state.active_board is not None and (br, bc) != state.active_board:
        return


    mini = boards[br][bc]
    cell = mini.cells[fr][fc]

    if cell["text"] != "":
        return

    # Ставим X или O
    cell.config(text=state.current_player)

    # Проверяем, не победил ли кто-то в этой мини-доске
    winner = mini.check_win()
    if winner:
        mini.mark_winner(winner)
        state.mini_board_statuses[br][bc] = winner
        print(f"Мини-доску ({br}, {bc}) выиграл {winner}")
        global_winner = CheckGlobalWin(state.mini_board_statuses)
        if global_winner:
            state.game_over = True
            print(f"Глобальную доску выиграл {global_winner}")
    elif mini.check_draw():
        mini.mark_draw()
        state.mini_board_statuses[br][bc] = "draw"
        print(f"Мини-доска ({br}, {bc}) закончилась вничью")
        global_winner = CheckGlobalWin(state.mini_board_statuses)
        if global_winner:
            state.game_over = True
            print(f"Глобальную доску выиграл {global_winner}")
        elif CheckGlobalDraw(state.mini_board_statuses):
            state.game_over = True
            print(f"Ничья!")

    # Определение следующей активной доски
    next_board = (fr, fc)
    next_mini = boards[next_board[0]][next_board[1]]

    if next_mini.winner is None and not next_mini.check_draw():
        state.active_board = next_board
    else:
        state.active_board = None

    # Сохраняем последний ход
    state.last_move = (br, bc, fr, fc)

    # Меняем игрока
    state.switch_player()

    # Обновляем визуал
    UpdateActiveBoardVisuals(boards, state.active_board, state.last_move)

