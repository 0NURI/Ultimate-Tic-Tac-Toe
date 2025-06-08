class GameState:
    def __init__(self):
        self.current_player = "X"
        self.active_board = None
        self.last_move = None  # (br, bc, fr, fc)

        self.mini_board_statuses = [
            [None for _ in range(3)]
            for _ in range(3)
        ]

        self.game_over = False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
