from tkinter import *


def show_menu(callback):
    menu_root = Tk()
    menu_root.title("Выбор режима игры")

    Label(menu_root, text="Выберите режим игры:", font=("Arial", 14)).pack(pady=10)

    def choose_vs_human():
        menu_root.destroy()
        callback(vs_ai=False)

    def choose_vs_ai(difficulty):
        player_symbol = symbol_var.get()
        menu_root.destroy()
        callback(vs_ai=True, difficulty=difficulty, player_symbol=player_symbol)

    Button(menu_root, text="Против друга", font=("Arial", 12), command=choose_vs_human).pack(pady=5)

    Label(menu_root, text="Против компьютера:", font=("Arial", 12)).pack(pady=10)

    Label(menu_root, text="Ваш символ:", font=("Arial", 10)).pack()
    symbol_var = StringVar(value="X")
    symbol_frame = Frame(menu_root)
    symbol_frame.pack()
    Radiobutton(symbol_frame, text="X", variable=symbol_var, value="X").pack(side=LEFT, padx=5)
    Radiobutton(symbol_frame, text="O", variable=symbol_var, value="O").pack(side=LEFT, padx=5)

    Button(menu_root, text="Лёгкий (рандом)", command=lambda: choose_vs_ai("easy")).pack(pady=2)
    Button(menu_root, text="Средний (глубина 2)", command=lambda: choose_vs_ai("medium")).pack(pady=2)
    Button(menu_root, text="Сложный (глубина 4)", command=lambda: choose_vs_ai("hard")).pack(pady=2)

    menu_root.mainloop()
