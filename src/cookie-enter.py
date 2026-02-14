# Cookie-enter.py Version 1.1.6 (Quality Update!)
# If you encounter any bugs/issues, please contact the developer at:
# https://github.com/Alfix-Januarivinter/cookie-enter.py

import json
import tkinter as tk

# Save file
SAVE_FILE = "cookie_save.json"
GAME_VERSION = "1.1.6"
INCOMPATIBLE_VERSIONS = ["1.1.1", "1.1.2", "1.1.3b", "1.1.3"]

# Constants and Variables
cookies = 0
multiplier = 1
permanent_multiplier = 1
ascending_multiplier = 1
ascending_cost = 1500
dark_mode = False
autosave_enabled = False

open_windows = []

UPGRADE_OPTIONS = {
    "1": (100, 1),
    "2": (200, 2),
    "5": (450, 5),
    "10": (800, 10),
    "20": (1400, 20),
    "50": (3000, 50),
    "100": (4500, 100),
    "1000": (45000, 1000),
}

# Themes
LIGHT_THEME = {
    "bg": "white",
    "fg": "black",
    "button_bg": "lightgray",
    "entry_bg": "white",
    "label_bg": "white",
    "toggle_on": "#90ee90",
    "toggle_off": "lightgray",
}

DARK_THEME = {
    "bg": "black",
    "fg": "white",
    "button_bg": "gray",
    "entry_bg": "black",
    "label_bg": "black",
    "toggle_on": "#2e8b57",
    "toggle_off": "gray",
}


# Functions
def format_number(value: int) -> str:
    return f"{value:,}".replace(",", "'")


def update_display():
    cookie_label.config(text=f"Cookies : {format_number(cookies)}󰆘")
    multiplier_label.config(
        text=f"Multiplier: {format_number(multiplier + permanent_multiplier - 1)}"
    )
    ascending_label.config(text=f"Ascending: {format_number(ascending_multiplier)}")
    ascending_button.config(
        text=f"Upgrade Ascending Multiplier cost: {format_number(ascending_cost)}󰆘 Cookies"
    )

    for btn in upgrade_buttons:
        btn["button"].config(state=tk.NORMAL if cookies >= btn["cost"] else tk.DISABLED)

    ascending_button.config(
        state=tk.NORMAL if cookies >= ascending_cost else tk.DISABLED
    )


def collect_cookies():
    global cookies
    cookies += (multiplier + permanent_multiplier - 1) * ascending_multiplier
    update_display()


def upgrade_multiplier(upgrade_key):
    global cookies, multiplier
    cost, increase = UPGRADE_OPTIONS[upgrade_key]
    if cookies >= cost:
        cookies -= cost
        multiplier += increase
        status_label.config(text="Upgrade successful !", fg="green")
    else:
        status_label.config(text="To few cookies !", fg="red")
    update_display()


def apply_theme_to_window(window):
    theme = DARK_THEME if dark_mode else LIGHT_THEME
    window.config(bg=theme["bg"])

    for widget in window.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(bg=theme["label_bg"], fg=theme["fg"])
        elif isinstance(widget, tk.Button):
            widget.config(bg=theme["button_bg"], fg=theme["fg"])


def close_window(window):
    if window in open_windows:
        open_windows.remove(window)
    window.destroy()


def open_upgrade_menu():
    upgrade_window = tk.Toplevel(root)
    upgrade_window.title("Upgrade Menu")
    upgrade_window.geometry("400x560")

    open_windows.append(upgrade_window)
    upgrade_window.protocol(
        "WM_DELETE_WINDOW", lambda w=upgrade_window: close_window(w)
    )

    tk.Label(upgrade_window, text="Choose an Upgrade", font=("Arial", 14)).pack(pady=10)

    for key, (cost, increase) in UPGRADE_OPTIONS.items():
        btn = tk.Button(
            upgrade_window,
            text=f"+{format_number(increase)} Multiplier = {format_number(cost)}󰆘 Cookies",
            font=("Arial", 14),
            width=30,
            padx=10,
            pady=6,
            command=lambda k=key: upgrade_multiplier(k),
        )
        btn.pack(pady=10)
        upgrade_buttons.append({"button": btn, "cost": cost})

    apply_theme_to_window(upgrade_window)
    update_display()


def cookies_ascending():
    global \
        cookies, \
        multiplier, \
        permanent_multiplier, \
        ascending_multiplier, \
        ascending_cost
    if cookies >= ascending_cost:
        cookies = 0
        multiplier = 1
        permanent_multiplier += 1
        ascending_multiplier += 1
        ascending_cost *= 2
        status_label.config(text="Ascending successful !", fg="green")
    else:
        status_label.config(text="To few cookies !", fg="red")
    update_display()


def save_game():
    data = {
        "version": GAME_VERSION,
        "cookies": cookies,
        "multiplier": multiplier,
        "permanent_multiplier": permanent_multiplier,
        "ascending_multiplier": ascending_multiplier,
        "ascending_cost": ascending_cost,
        "dark_mode": dark_mode,
        "autosave_enabled": autosave_enabled,
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    status_label.config(text="Game saved 󰆓!", fg="green")


def load_game():
    global cookies, multiplier, permanent_multiplier, ascending_multiplier
    global ascending_cost, dark_mode, autosave_enabled
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)

        if data.get("version") in INCOMPATIBLE_VERSIONS:
            status_label.config(text="Incompatible save version !", fg="red")
            return

        cookies = data.get("cookies", 0)
        multiplier = data.get("multiplier", 1)
        permanent_multiplier = data.get("permanent_multiplier", 1)
        ascending_multiplier = data.get("ascending_multiplier", 1)
        ascending_cost = data.get("ascending_cost", 1500)
        dark_mode = data.get("dark_mode", False)
        autosave_enabled = data.get("autosave_enabled", False)

        dark_mode_var.set(dark_mode)
        autosave_var.set(autosave_enabled)

        save_game()
        status_label.config(text="Game loaded 󱣪!", fg="green")
    except FileNotFoundError:
        status_label.config(text="No save file found 󱙃.", fg="red")

    update_display()
    apply_theme()


def apply_theme():
    apply_theme_to_window(root)
    for window in open_windows:
        apply_theme_to_window(window)

    theme = DARK_THEME if dark_mode else LIGHT_THEME
    dark_mode_button.config(bg=theme["toggle_on"] if dark_mode else theme["toggle_off"])
    autosave_button.config(
        bg=theme["toggle_on"] if autosave_enabled else theme["toggle_off"]
    )


def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    dark_mode_var.set(dark_mode)
    apply_theme()


def toggle_autosave():
    global autosave_enabled
    autosave_enabled = not autosave_enabled
    autosave_var.set(autosave_enabled)
    apply_theme()


def autosave_loop():
    if autosave_enabled:
        save_game()
    root.after(20000, autosave_loop)


def open_help():
    help_window = tk.Toplevel(root)
    help_window.title("Help")
    help_window.geometry("725x300")

    open_windows.append(help_window)
    help_window.protocol("WM_DELETE_WINDOW", lambda w=help_window: close_window(w))

    tk.Label(
        help_window,
        text="This is a game where you click a button and you get cookies!.\n You may see now a label that says you have 0 cookies,\n if not you haven't already clicked on the button where it says collect cookies!\n And you can get more cookies per click by upgrading your multiplier.\n You can do that by hitting upgrade multiplier button and then another menu appears.\n When hitting upgrade ascending multiplier button,\n your cookies will be reset and same for your multiplier (except for your permanent multiplier)\n and you will get 1 ascending multiplier which multiplies with your multiplier!\n Have fun!\n If you encounter any bugs/issues, please contact the developer at\n https://github.com/Alfix-Januarivinter/cookie-enter.py",
        font=("Arial", 12),
    ).pack(expand=True)
    apply_theme_to_window(help_window)


def exit_game():
    save_game()
    root.after(50, root.quit)


# GUI
root = tk.Tk()
root.title("Cookie Enter")
root.geometry("600x600")
icon = tk.PhotoImage(file="cookie.png")
root.iconphoto(True, icon)

upgrade_buttons = []

help_button = tk.Button(root, text="?", font=("Arial", 12), command=open_help)
help_button.place(relx=0.02, rely=0.02, anchor="nw")

cookie_label = tk.Label(root, font=("Arial", 14))
cookie_label.pack(pady=10)

multiplier_label = tk.Label(root, font=("Arial", 14))
multiplier_label.pack(pady=10)

ascending_label = tk.Label(root, font=("Arial", 14))
ascending_label.pack(pady=10)

collect_button = tk.Button(
    root,
    text="Collect Cookies 󰆘",
    font=("Arial", 14),
    padx=12,
    pady=6,
    command=collect_cookies,
)
collect_button.pack(pady=10)

upgrade_button = tk.Button(
    root,
    text="Upgrade Multiplier ",
    font=("Arial", 14),
    padx=12,
    pady=6,
    command=open_upgrade_menu,
)
upgrade_button.pack(pady=10)

ascending_button = tk.Button(
    root, font=("Arial", 14), padx=12, pady=6, command=cookies_ascending
)
ascending_button.pack(pady=10)

save_button = tk.Button(
    root, text="Save Game 󰆓", font=("Arial", 14), padx=12, pady=6, command=save_game
)
save_button.pack(pady=5)

load_button = tk.Button(
    root, text="Load Game 󱣪", font=("Arial", 14), padx=12, pady=6, command=load_game
)
load_button.pack(pady=5)

dark_mode_var = tk.BooleanVar(value=False)
dark_mode_button = tk.Button(
    root, text="Toggle Themes 󰔎", font=("Arial", 10), command=toggle_dark_mode
)
dark_mode_button.place(relx=0.95, rely=0.02, anchor="ne")

autosave_var = tk.BooleanVar(value=False)
autosave_button = tk.Button(
    root, text="Autosave", font=("Arial", 10), command=toggle_autosave
)
autosave_button.place(relx=0.95, rely=0.10, anchor="ne")

status_label = tk.Label(root, font=("Arial", 12))
status_label.pack(pady=10)

exit_button = tk.Button(
    root, text="Exit ", font=("Arial", 14), padx=12, pady=6, command=exit_game
)
exit_button.pack(side="bottom", pady=10)

load_game()
autosave_loop()
root.mainloop()
