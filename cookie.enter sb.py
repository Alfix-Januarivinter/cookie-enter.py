# Version 1.1.2 sandbox (Added tools!)
# If you encounter any bugs, please contact the developer at: https://github.com/Alfix-Januarivinter/cookie-enter.py

import tkinter as tk

# Constants and Variables
FEW_COOKIES = "Too few cookies!"
INVALID_INPUT = "Invalid input!"
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
EXIT = ["exit", "quit"]

# Functions
def update_display():
    """Update the display for cookies and multiplier."""
    cookie_label.config(text=f"Cookies: {cookies}")
    multiplier_label.config(text=f"Multiplier: x{multiplier}")
    root.update()  # Force the window to update and reflect changes

def collect_cookies():
    """Increase cookies based on the multiplier."""
    global cookies
    cookies += multiplier
    update_display()

def upgrade_multiplier(upgrade_key):
    """Handle upgrades and update the multiplier."""
    global cookies, multiplier
    cost, increase = UPGRADE_OPTIONS[upgrade_key]
    
    # Check if the player has enough cookies for the upgrade
    if cookies >= cost:
        cookies -= cost
        multiplier += increase
        status_label.config(text="Upgrade successful!", fg="green")
    else:
        status_label.config(text=FEW_COOKIES, fg="red")
    
    # Force the window to update after status label change
    root.update()
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

def sandbox():
    """Sandbox mode to modify the game values manually."""
    def execute_sandbox_command():
        global cookies, multiplier
        command = sandbox_entry.get()

        if command in EXIT:
            sandbox_window.destroy()
            return
        
        if command == "reset" or command == "r":
            cookies = 0
            multiplier = 1
        elif command == "unlimited" or command == "un":
            cookies = 10000000000000000000000000000000000000000000000000000000000000
            multiplier = 100000000000000000000
        elif command == "2":
            cookies = cookies + cookies
            multiplier = multiplier + multiplier
        elif command == "choose" or command == "co":
            # Prompt the user for custom cookie and multiplier values
            sandbox_entry.config(state="disabled")  # Disable the original entry
            choose_label.config(text="Enter custom cookies and multiplier:")

            cookie_label_text.config(text="Cookies:")
            multiplier_label_text.config(text="Multiplier:")

            cookie_entry.pack(pady=5)
            multiplier_entry.pack(pady=5)
            confirm_button.pack(pady=10)  # Show the Confirm button
        else:
            sandbox_status_label.config(text=INVALID_INPUT, fg="red")
            return
        
        sandbox_status_label.config(text="Command executed successfully!", fg="green")
        update_display()
    
    def confirm_choose_values():
        """Confirm the custom values entered by the user."""
        global cookies, multiplier
        try:
            cookies = int(cookie_entry.get())
            multiplier = int(multiplier_entry.get())
            sandbox_status_label.config(text="Values confirmed!", fg="green")
            update_display()
        except ValueError:
            sandbox_status_label.config(text="Invalid input! Please enter numbers.", fg="red")

    # Create Sandbox Window
    sandbox_window = tk.Toplevel(root)
    sandbox_window.title("Sandbox Mode")
    sandbox_window.geometry("400x400")
    
    # Label for Sandbox
    sandbox_label = tk.Label(sandbox_window, text="Enter command: reset, unlimited, 2, choose, or exit", font=("Arial", 12))
    sandbox_label.pack(pady=10)
    
    # Entry widget to input commands
    sandbox_entry = tk.Entry(sandbox_window, font=("Arial", 12))
    sandbox_entry.pack(pady=10)
    
    # Button to execute the sandbox command
    sandbox_button = tk.Button(sandbox_window, text="Execute", font=("Arial", 12), command=execute_sandbox_command)
    sandbox_button.pack(pady=10)
    
    # Status Label to show the result of command
    sandbox_status_label = tk.Label(sandbox_window, text="", font=("Arial", 12))
    sandbox_status_label.pack(pady=10)

    # UI for "choose" command (after it's triggered)
    choose_label = tk.Label(sandbox_window, text="", font=("Arial", 12))
    choose_label.pack(pady=10)

    cookie_label_text = tk.Label(sandbox_window, text="Cookies:", font=("Arial", 12))
    multiplier_label_text = tk.Label(sandbox_window, text="Multiplier:", font=("Arial", 12))

    cookie_entry = tk.Entry(sandbox_window, font=("Arial", 12))
    multiplier_entry = tk.Entry(sandbox_window, font=("Arial", 12))
    confirm_button = tk.Button(sandbox_window, text="Confirm Values", font=("Arial", 12), command=confirm_choose_values)

    # Initially hide the input fields and the confirm button
    cookie_label_text.pack_forget()
    multiplier_label_text.pack_forget()
    cookie_entry.pack_forget()
    multiplier_entry.pack_forget()
    confirm_button.pack_forget()

# Main GUI Setup
root = tk.Tk()
root.title("Cookie Enter Sandbox Edition")
root.geometry("400x400")  # Increased window size for better layout

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

sandbox_button = tk.Button(root, text="Sandbox Mode", font=("Arial", 14), command=lambda: sandbox())
sandbox_button.pack(pady=10)

# Status Label (To display upgrade status messages)
status_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
status_label.pack(pady=10)

# Exit Button (No save now)
def exit_game():
    root.quit()  # Quit the application

exit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=exit_game)
exit_button.pack(side="bottom", pady=10)

# Run the main loop
root.mainloop()
