# Version 1.1.2 (Added tools!)
# If you encounter any bugs, please contact the developer at: https://github.com/Alfix-Januarivinter/cookie-enter.py

import tkinter as tk

# Constants and Variables
FEW_COOKIES = "Too few cookies!"
UPGRADE_OPTIONS = {
    "1": (100, 1),
    "2": (200, 2),
    "5": (450, 5),
    "10": (800, 10),
    "20": (1400, 20),
    "50": (3000, 50),
    "100": (4500, 100),
}
cookies = 0
multiplier = 1

# Functions
def update_display():
    """Update the display for cookies and multiplier."""
    cookie_label.config(text=f"Cookies: {cookies}")
    multiplier_label.config(text=f"Multiplier: x{multiplier}")
    status_label.config(text="")

def collect_cookies():
    """Increase cookies based on the multiplier."""
    global cookies
    cookies += multiplier
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
    upgrade_window.geometry("300x400")

    tk.Label(upgrade_window, text="Choose an Upgrade", font=("Arial", 14)).pack(pady=10)

    for key, (cost, increase) in UPGRADE_OPTIONS.items():
        tk.Button(
            upgrade_window,
            text=f"+{increase} Multiplier = {cost} Cookies",
            font=("Arial", 12),
            command=lambda k=key: upgrade_multiplier(k)
        ).pack(pady=5)

# Exit function
def exit_game():
    root.quit()  # Quit the application

# Main GUI Setup
root = tk.Tk()
root.title("Cookie Enter")
root.geometry("400x300")

# Labels
cookie_label = tk.Label(root, text=f"Cookies: {cookies}", font=("Arial", 14))
cookie_label.pack(pady=10)

multiplier_label = tk.Label(root, text=f"Multiplier: x{multiplier}", font=("Arial", 14))
multiplier_label.pack(pady=10)

# Buttons
collect_button = tk.Button(root, text="Collect Cookies", font=("Arial", 14), command=collect_cookies)
collect_button.pack(pady=10)

upgrade_button = tk.Button(root, text="Upgrade Multiplier", font=("Arial", 14), command=open_upgrade_menu)
upgrade_button.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
status_label.pack(pady=10)

# Exit Button (new)
exit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=exit_game)
exit_button.pack(side="bottom", pady=10)

# Run the main loop
root.mainloop()