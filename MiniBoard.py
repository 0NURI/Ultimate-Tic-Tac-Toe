from tkinter import *


class MiniBoard:
    def __init__(self, row, col, frame):
        self.row = row
        self.col = col
        self.frame = frame
        self.cells = [[None for _ in range(3)] for _ in range(3)]
        self.winner = None

    def check_win(self):
        for i in range(3):

            row = [self.cells[i][j]["text"] for j in range(3)]
            if row[0] != "" and all(cell == row[0] for cell in row):
                return row[0]

            col = [self.cells[j][i]["text"] for j in range(3)]
            if col[0] != "" and all(cell == col[0] for cell in col):
                return col[0]

        diag1 = [self.cells[i][i]["text"] for i in range(3)]
        if diag1[0] != "" and all(cell == diag1[0] for cell in diag1):
            return diag1[0]

        diag2 = [self.cells[i][2 - i]["text"] for i in range(3)]
        if diag2[0] != "" and all(cell == diag2[0] for cell in diag2):
            return diag2[0]

        return None

    def mark_winner(self, winner):
        self.winner = winner
        for row in self.cells:
            for btn in row:
                btn.config(state=DISABLED)

        label = Label(self.frame, text=winner, font=("Arial", 60), fg="gray", bg="white")
        label.place(relx=0.5, rely=0.5, anchor="center")

    def check_draw(self):
        return all(
            self.cells[r][c]["text"] != ""
            for r in range(3)
            for c in range(3)
        )

    def mark_draw(self):
        self.winner = "draw"

        for row in self.cells:
            for btn in row:
                btn.config(state=DISABLED)

        label = Label(
            self.frame,
            text="-",
            font=("Arial", 40),
            fg="gray",
            bg="white"
        )
        label.place(relx=0.5, rely=0.5, anchor="center")
