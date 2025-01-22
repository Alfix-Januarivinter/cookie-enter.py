# Version 1.1.0 Gui (Improved Design Release)
# If you encounter any bugs, please contact the developer at: https://github.com/Alfix-Januarivinter/cookie-enter.py

FEW_COOKIES = "Too few cookies!"
INVALID_INPUT = "Invalid input!"
EXIT = ["exit", "esc"]

UPGRADE_OPTIONS = {
    "1": (100, 1),
    "2": (200, 2),
    "5": (450, 5),
    "10": (800, 10),
    "20": (1400, 20),
    "50": (3000, 50),
    "100": (4500, 100)
}

cookies = 0
multiplier = 1


def display():
    """Display the current number of cookies and the multiplier."""
    print(f"Cookies: {cookies}\nMultiplier: {multiplier}\n")

def cookies_increase():
    """Increase the number of cookies based on the current multiplier."""
    global cookies
    cookies += multiplier

def enter():
    """Handle the main game loop where users collect cookies."""
    while True:
        display()
        user_input = input("Press Enter to collect cookies or type 'exit' or 'esc' to return to the menu: ").strip().lower()
        if user_input in EXIT:
            break
        cookies_increase()

def upgrade(upgrade_choice, upgrade_times):
    """Handle the upgrade logic, increasing the multiplier if the user has enough cookies."""
    global cookies, multiplier
    cost_per_upgrade, multiplier_increase = UPGRADE_OPTIONS[upgrade_choice]
    total_cost = cost_per_upgrade * upgrade_times

    if cookies >= total_cost:
        cookies -= total_cost
        multiplier += multiplier_increase * upgrade_times
        print(f"\nUpgrade successful! Multiplier increased to {multiplier}.\n")
    else:
        print(f"\n{FEW_COOKIES}\n")

def handle_upgrade():
    """Handle the upgrade menu where users can select and apply upgrades."""
    while True:
        display()
        print("Available Upgrades:")
        for key, (cost, increase) in UPGRADE_OPTIONS.items():
            print(f"  +{increase} Multiplier = {cost} Cookies (Option: {key})")
        print("Type 'exit' or 'esc' to return to the main menu.")

        upgrade_choice = input("Choose an upgrade option: ").strip()
        if upgrade_choice in EXIT:
            break

        if upgrade_choice not in UPGRADE_OPTIONS:
            print(f"\n{INVALID_INPUT}\n")
            continue

        try:
            upgrade_times = int(input("Enter the number of times to apply the upgrade: ").strip())
            if upgrade_times <= 0:
                print(f"\n{INVALID_INPUT}\n")
                continue
        except ValueError:
            print(f"\n{INVALID_INPUT}\n")
            continue

        upgrade(upgrade_choice, upgrade_times)

def main_menu():
    """Display the main menu and handle user navigation."""
    while True:
        print("\nMain Menu")
        print("1. Enter the Cookie Game (type 'enter' or 'e')")
        print("2. Upgrade Multiplier (type 'upgrade' or 'up')")
        print("3. Exit the Game (type 'exit' or 'esc')")

        user_input = input("Select an option: ").strip().lower()
        if user_input in ["enter", "e"]:
            enter()
        elif user_input in ["upgrade", "up"]:
            handle_upgrade()
        elif user_input in EXIT:
            print("\nThanks for playing! Goodbye!\n")
            break
        else:
            print(f"\n{INVALID_INPUT}\n")

def main():
    """Entry point of the game."""
    print("Welcome to Cookie Enter! Collect cookies and upgrade your multiplier to earn even more!")
    main_menu()

if __name__ == "__main__":
    main()