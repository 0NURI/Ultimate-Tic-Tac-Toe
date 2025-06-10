from Menu import show_menu
from GameWindow import launch_game


def on_mode_selected(vs_ai=False, difficulty=None, player_symbol="X"):
    launch_game(vs_ai=vs_ai, difficulty=difficulty, player_symbol=player_symbol)


show_menu(on_mode_selected)
