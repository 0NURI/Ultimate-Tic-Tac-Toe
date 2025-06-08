from tkinter import *
from GameState import GameState
from BoardCreator import CreateBoard
from ButtonClickHandler import HandleClick

root = Tk()
state = GameState()
boards = None

def click_wrapper(br, bc, fr, fc):
    HandleClick(br, bc, fr, fc, boards, state)

boards = CreateBoard(root, click_wrapper)

root.mainloop()
