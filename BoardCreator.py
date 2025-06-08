from tkinter import *
from MiniBoard import MiniBoard



def CreateBoard(root, click_handler):

    def keep_square(event):
        if event.widget == root:
            size = min(event.width, event.height)
            if root.winfo_width() != root.winfo_height():
                root.geometry(f"{size}x{size}")

    root.bind("<Configure>", keep_square)
    root.minsize(500, 500)

    boards = [[None for _ in range(3)] for _ in range(3)]

    for boardRow in range(3):
        root.grid_rowconfigure(boardRow, weight=1, minsize=150)
        root.grid_columnconfigure(boardRow, weight=1, minsize=150)

        for boardCol in range(3):
            frame = Frame(root, borderwidth=2, relief=RAISED)
            frame.grid(row=boardRow, column=boardCol, sticky="nsew", padx=10, pady=10)

            mini = MiniBoard(boardRow, boardCol, frame)
            boards[boardRow][boardCol] = mini

            for frameRow in range(3):
                frame.grid_rowconfigure(frameRow, weight=1)
                frame.grid_columnconfigure(frameRow, weight=1)

                for frameCol in range(3):
                    def make_click_handler(br=boardRow, bc=boardCol, fr=frameRow, fc=frameCol):
                        return lambda: click_handler(br, bc, fr, fc)

                    btn = Button(frame, text="", font=("Arial", 20), width=2, height=1, command=make_click_handler())
                    btn.grid(row=frameRow, column=frameCol, sticky="nsew")

                    mini.cells[frameRow][frameCol] = btn

    return boards
