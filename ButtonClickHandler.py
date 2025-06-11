from Utils import *
from PlayerAI import MakeAIMove


def HandleClick(br, bc, fr, fc, boards, state):
    if state.game_over: return

    if state.active_board is not None and (br, bc) != state.active_board:
        return

    mini = boards[br][bc]
    cell = mini.cells[fr][fc]

    if cell["text"] != "":
        return

    cell.config(text=state.current_player)

    winner = mini.check_win()
    if winner:
        mini.mark_winner(winner)
        state.mini_board_statuses[br][bc] = winner
        print(f"Мини-доску ({br}, {bc}) выиграл {winner}")
        global_winner = CheckGlobalWin(state.mini_board_statuses)
        if global_winner:
            state.game_over = True
            state.player_label.config(text=f"Победил {global_winner}!", fg="red")
            print(f"Глобальную доску выиграл {global_winner}")
            return
    elif mini.check_draw():
        mini.mark_draw()
        state.mini_board_statuses[br][bc] = "draw"
        print(f"Мини-доска ({br}, {bc}) закончилась вничью")
        global_winner = CheckGlobalWin(state.mini_board_statuses)
        if global_winner:
            state.game_over = True
            state.player_label.config(text=f"Победил {global_winner}!", fg="red")
            print(f"Глобальную доску выиграл {global_winner}")
            return  # обязательно остановить выполнение
        elif CheckGlobalDraw(state.mini_board_statuses):
            state.game_over = True
            state.player_label.config(text=f"Ничья!", fg="red")
            return

    next_board = (fr, fc)
    next_mini = boards[next_board[0]][next_board[1]]

    if next_mini.winner is None and not next_mini.check_draw():
        state.active_board = next_board
    else:
        state.active_board = None

    state.last_move = (br, bc, fr, fc)

    state.switch_player()

    state.player_label.config(text=f"Сейчас ходит: {state.current_player}")

    UpdateActiveBoardVisuals(boards, state.active_board, state.last_move)

    if not state.game_over and state.vs_ai and state.current_player != state.player_symbol:
        MakeAIMove(boards, state)
