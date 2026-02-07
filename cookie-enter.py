# Cookie-enter Version 1.1.4 (Added themes and saves!)
# If you encounter any bugs, please contact the developer at:
# https://github.com/Alfix-Januarivinter/cookie-enter.py

import json
import tkinter as tk

# Save file
SAVE_FILE = "cookie_save.json"

# Constants and Variables
cookies = 0
multiplier = 1
ascending_multiplier = 1
ascending_cost = 1500
dark_mode = False

open_windows = []

FEW_COOKIES = "Too few cookies!"
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
}

DARK_THEME = {
    "bg": "black",
    "fg": "white",
    "button_bg": "gray",
    "entry_bg": "black",
    "label_bg": "black",
}


# Functions
def update_display():
    cookie_label.config(text=f"Cookies: {cookies}")
    multiplier_label.config(text=f"Multiplier: {multiplier}")
    ascending_label.config(text=f"Ascending: {ascending_multiplier}")
    ascending_button.config(
        text=f"Upgrade Ascending Multiplier cost: {ascending_cost} cookies"
    )


def collect_cookies():
    global cookies
    cookies += multiplier * ascending_multiplier
    update_display()


def upgrade_multiplier(upgrade_key):
    global cookies, multiplier
    cost, increase = UPGRADE_OPTIONS[upgrade_key]
    if cookies >= cost:
        cookies -= cost
        multiplier += increase
        status_label.config(text="Upgrade successful!", fg="green")
    else:
        status_label.config(text=FEW_COOKIES, fg="red")
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
    upgrade_window.geometry("400x550")

    open_windows.append(upgrade_window)
    upgrade_window.protocol(
        "WM_DELETE_WINDOW", lambda w=upgrade_window: close_window(w)
    )

    tk.Label(upgrade_window, text="Choose an Upgrade", font=("Arial", 14)).pack(pady=10)

    for key, (cost, increase) in UPGRADE_OPTIONS.items():
        tk.Button(
            upgrade_window,
            text=f"+{increase} Multiplier = {cost} Cookies",
            font=("Arial", 14),
            width=25,
            command=lambda k=key: upgrade_multiplier(k),
        ).pack(pady=10)

    apply_theme_to_window(upgrade_window)


def cookies_ascending():
    global cookies, multiplier, ascending_multiplier, ascending_cost
    if cookies >= ascending_cost:
        cookies -= ascending_cost
        ascending_multiplier += 1
        ascending_cost *= 2
        cookies = 0
        multiplier = 1
        status_label.config(text="Upgrade successful!", fg="green")
    else:
        status_label.config(text=FEW_COOKIES, fg="red")
    update_display()


def save_game():
    data = {
        "cookies": cookies,
        "multiplier": multiplier,
        "ascending_multiplier": ascending_multiplier,
        "ascending_cost": ascending_cost,
        "dark_mode": dark_mode,
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    status_label.config(text="Game saved!", fg="green")


def load_game():
    global cookies, multiplier, ascending_multiplier, ascending_cost, dark_mode
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)

        cookies = data.get("cookies", 0)
        multiplier = data.get("multiplier", 1)
        ascending_multiplier = data.get("ascending_multiplier", 1)
        ascending_cost = data.get("ascending_cost", 1500)
        dark_mode = data.get("dark_mode", False)

        dark_mode_var.set(dark_mode)
        status_label.config(text="Game loaded!", fg="green")
    except FileNotFoundError:
        status_label.config(text="No save file found.", fg="orange")

    update_display()


def apply_theme():
    apply_theme_to_window(root)
    for window in open_windows:
        apply_theme_to_window(window)


def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    dark_mode_var.set(dark_mode)
    apply_theme()


# Exit function
def exit_game():
    save_game()
    root.after(50, root.quit)


# Labels and buttons
root = tk.Tk()
root.title("Cookie Enter")
root.geometry("600x600")

cookie_label = tk.Label(root, font=("Arial", 14))
cookie_label.pack(pady=10)

multiplier_label = tk.Label(root, font=("Arial", 14))
multiplier_label.pack(pady=10)

ascending_label = tk.Label(root, font=("Arial", 14))
ascending_label.pack(pady=10)

collect_button = tk.Button(
    root, text="Collect Cookies", font=("Arial", 14), command=collect_cookies
)
collect_button.pack(pady=10)

upgrade_button = tk.Button(
    root, text="Upgrade Multiplier", font=("Arial", 14), command=open_upgrade_menu
)
upgrade_button.pack(pady=10)

ascending_button = tk.Button(root, font=("Arial", 14), command=cookies_ascending)
ascending_button.pack(pady=10)

save_button = tk.Button(root, text="Save Game", font=("Arial", 14), command=save_game)
save_button.pack(pady=5)

load_button = tk.Button(root, text="Load Game", font=("Arial", 14), command=load_game)
load_button.pack(pady=5)

dark_mode_var = tk.BooleanVar(value=False)
dark_mode_button = tk.Button(
    root, text="Toogle Themes", font=("Arial", 10), command=toggle_dark_mode
)
dark_mode_button.place(relx=0.95, rely=0.02, anchor="ne")

status_label = tk.Label(root, font=("Arial", 12))
status_label.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=exit_game)
exit_button.pack(side="bottom", pady=10)

load_game()
apply_theme()

root.mainloop()
