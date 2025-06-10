from tkinter import *
from GameState import GameState
from BoardCreator import CreateBoard
from ButtonClickHandler import HandleClick
from PlayerAI import MakeAIMove


def launch_game(vs_ai=False, difficulty=None, player_symbol="X"):
    root = Tk()
    state = GameState()
    state.vs_ai = vs_ai
    state.difficulty = difficulty
    state.player_symbol = player_symbol

    boards = None

    player_label = Label(root,
                         text=f"Сейчас ходит: {state.current_player}",
                         font=("Arial", 16, "bold"),
                         fg="red" if state.current_player == "X" else "blue")
    player_label.grid(row=0, column=0, columnspan=3, pady=10)
    state.player_label = player_label

    def click_wrapper(br, bc, fr, fc):
        HandleClick(br, bc, fr, fc, boards, state)

    nonlocal_boards = {"boards": None}
    boards = CreateBoard(root, click_wrapper)
    nonlocal_boards["boards"] = boards

    if player_symbol == "X":
        state.ai_symbol = "O"
    else:
        state.ai_symbol = "X"
        MakeAIMove(boards, state)

    root.mainloop()
