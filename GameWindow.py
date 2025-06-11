from tkinter import *
from GameState import GameState
from BoardCreator import CreateBoard
from ButtonClickHandler import HandleClick
from PlayerAI import MakeAIMove


def launch_game(vs_ai=False, difficulty=None, player_symbol="X"):
    root = Tk()
    state = GameState()
    state.vs_ai       = vs_ai
    state.difficulty  = difficulty
    state.player_symbol = player_symbol

    boards = None

    for r in range(3):
        root.grid_rowconfigure(r, weight=1)
        root.grid_columnconfigure(r, weight=1)

    player_label = Label(root,
                         text=f"Сейчас ходит: {state.current_player}",
                         font=("Arial", 16, "bold"),
                         fg="red" if state.current_player == "X" else "blue")
    player_label.grid(row=3, column=0, columnspan=3, pady=(10, 5))
    state.player_label = player_label

    root.grid_rowconfigure(3, weight=0)

    def click_wrapper(br, bc, fr, fc):
        HandleClick(br, bc, fr, fc, boards, state)

    boards = CreateBoard(root, click_wrapper)

    state.ai_symbol = "O" if player_symbol == "X" else "X"
    if state.player_symbol == "O":
        MakeAIMove(boards, state)

    root.mainloop()
