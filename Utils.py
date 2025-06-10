from tkinter import *


def CheckGlobalWin(statuses):
    for i in range(3):
        if statuses[i][0] in ("X", "O") and all(statuses[i][j] == statuses[i][0] for j in range(3)):
            return statuses[i][0]

        if statuses[i][0] in ("X", "O") and all(statuses[j][i] == statuses[0][i] for j in range(3)):
            return statuses[0][i]

    if statuses[1][1] in ("X", "O"):
        if all(statuses[i][i] == statuses[1][1] for i in range(3)):
            return statuses[1][1]
        if all(statuses[i][2 - i] == statuses[1][1] for i in range(3)):
            return statuses[1][1]

    return None


def CheckGlobalDraw(statuses):
    return all(
        all(cell is not None for cell in row)
        for row in statuses
    )


def UpdateActiveBoardVisuals(boards, active_board, last_move=None):
    for i in range(3):
        for j in range(3):
            mini = boards[i][j]

            if mini.winner is not None:
                continue

            is_active = (active_board is None) or ((i, j) == active_board)
            bg = "lightyellow" if is_active else "lightgray"

            mini.frame.configure(background=bg)

            for row_i, row in enumerate(mini.cells):
                for col_i, btn in enumerate(row):
                    is_last = (i, j, row_i, col_i) == last_move
                    symbol = btn["text"]
                    fg = "black" if symbol in ("X", "O") else "gray"

                    btn.config(
                        state=NORMAL if is_active else DISABLED,
                        disabledforeground=fg,
                        fg=fg,
                        bg="lightgreen" if is_last else bg
                    )
