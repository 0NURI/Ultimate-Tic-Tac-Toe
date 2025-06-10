import random


def MakeAIMove(boards, state):
    possible_moves = []

    if state.active_board:
        br, bc = state.active_board
        mini = boards[br][bc]
        for fr in range(3):
            for fc in range(3):
                if mini.cells[fr][fc]["text"] == "":
                    possible_moves.append((br, bc, fr, fc))
    else:
        for br in range(3):
            for bc in range(3):
                mini = boards[br][bc]
                if mini.winner is None:
                    for fr in range(3):
                        for fc in range(3):
                            if mini.cells[fr][fc]["text"] == "":
                                possible_moves.append((br, bc, fr, fc))

    if possible_moves:
        move = random.choice(possible_moves)

        from ButtonClickHandler import HandleClick
        HandleClick(*move, boards, state)
