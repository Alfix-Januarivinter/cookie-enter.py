# Version 1.1.3 (Added ascending!)
# If you encounter any bugs, please contact the developer at: https://github.com/Alfix-Januarivinter/cookie-enter.py

import tkinter as tk

# Constants and Variables
cookies = 0
multiplier = 1
ascending_multiplier = 1
ascending_cost = ascending_multiplier * 1500

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


# Functions
def update_display():
    """Update the display for cookies and multiplier."""
    cookie_label.config(text=f"Cookies: {cookies}")
    multiplier_label.config(text=f"Multiplier: {multiplier}")
    ascending_label.config(text=f"Ascending: {ascending_multiplier}")
    status_label.config(text="")
    ascending_button.config(
        text=f"Upgrade Ascending Multiplier  cost: {ascending_cost} cookies"
    )


def collect_cookies():
    """Increase cookies based on the multiplier."""
    global cookies
    cookies += multiplier * ascending_multiplier
    update_display()


def upgrade_multiplier(upgrade_key):
    """Handle upgrades and update the multiplier."""
    global cookies, multiplier
    cost, increase = UPGRADE_OPTIONS[upgrade_key]
    if cookies >= cost:
        cookies -= cost
        multiplier += increase
        status_label.config(text="Upgrade successful!", fg="green")
    else:
        status_label.config(text=FEW_COOKIES, fg="red")
    update_display()


def open_upgrade_menu():
    """Open a new window for the upgrade menu."""
    upgrade_window = tk.Toplevel(root)
    upgrade_window.title("Upgrade Menu")
    upgrade_window.geometry("300x450")

    tk.Label(upgrade_window, text="Choose an Upgrade", font=("Arial", 14)).pack(pady=10)

    for key, (cost, increase) in UPGRADE_OPTIONS.items():
        tk.Button(
            upgrade_window,
            text=f"+{increase} Multiplier = {cost} Cookies",
            font=("Arial", 12),
            command=lambda k=key: upgrade_multiplier(k),
        ).pack(pady=5)


def cookies_ascending():
    """Ascending upgrade."""
    global cookies, multiplier, ascending_multiplier
    global ascending_cost
    if cookies >= ascending_cost:
        cookies -= ascending_cost
        ascending_multiplier += 1
        ascending_cost = ascending_cost * 2
        cookies = 0
        multiplier = 1
        status_label.config(text="Upgrade successful!", fg="green")
    else:
        status_label.config(text=FEW_COOKIES, fg="red")
    update_display()


# Exit function
def exit_game():
    root.quit()


# Main GUI Setup
root = tk.Tk()
root.title("Cookie Enter")
root.geometry("600x500")

# Labels
cookie_label = tk.Label(root, text=f"Cookies: {cookies}", font=("Arial", 14))
cookie_label.pack(pady=10)

multiplier_label = tk.Label(root, text=f"Multiplier: {multiplier}", font=("Arial", 14))
multiplier_label.pack(pady=10)

ascending_label = tk.Label(
    root, text=f"Ascending: {ascending_multiplier}", font=("Arial", 14)
)
ascending_label.pack(pady=10)

# Buttons
collect_button = tk.Button(
    root, text="Collect Cookies", font=("Arial", 14), command=collect_cookies
)
collect_button.pack(pady=10)

upgrade_button = tk.Button(
    root, text="Upgrade Multiplier", font=("Arial", 14), command=open_upgrade_menu
)
upgrade_button.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
status_label.pack(pady=10)

# Ascending Button
ascending_button = tk.Button(
    root,
    text=f"Upgrade Ascending Multiplier  cost: {ascending_cost} cookies",
    font=("Arial", 14),
    command=cookies_ascending,
)
ascending_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=exit_game)
exit_button.pack(side="bottom", pady=10)

# Run the main loop
root.mainloop()
