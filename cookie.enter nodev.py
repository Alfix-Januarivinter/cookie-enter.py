# Version 1.1.0 nodev (New Design Release)
# If you encounter any bugs, please contact the developer at: https://github.com/Alfix-Januarivinter/cookie-enter.py
FEW_COOKIES="Too few cookies!"
INVALID_INPUT="Invalid input!"
EXIT = ["exit","esc"]
UPGRADE_OPTIONS={
    "1": (100, 1),
    "2": (200, 2),
    "5": (450, 5),
    "10": (800, 10),
    "20": (1400, 20),
    "50": (3000, 50),
    "100": (4500, 100)
}
cookies=0
multiplier=1
print("Welcome to Cookie Enter!")
def display():
    print(f"Cookies = {cookies}\nCookie Multiplier = {multiplier}")
def cookies_increase():
    global cookies
    cookies+=multiplier
def enter():
    while True:
        print(cookies)
        user_input=input(": ").strip().lower()
        if user_input in EXIT:
            break
        cookies_increase()
def upgrade(upgrade,upgrade_times):
    global cookies,multiplier
    cost_per_upgrade,multiplier_increase=UPGRADE_OPTIONS[upgrade]
    total_cost=cost_per_upgrade*upgrade_times
    if cookies>=total_cost:
        cookies-=total_cost
        multiplier+=multiplier_increase*upgrade_times
        print(f"Upgrade successful! Multiplier increased to {multiplier}.")
    else:
        print(FEW_COOKIES)
def handle_upgrade():
    while True:
        display()
        print(" / ".join([f"+{v[1]} = {v[0]}" for v in UPGRADE_OPTIONS.values()]))
        upgrade_choice=input("Upgrade: ").strip()
        if upgrade_choice in EXIT:
            break
        if upgrade_choice not in UPGRADE_OPTIONS:
            print(INVALID_INPUT)
            continue
        try:
            upgrade_times = max(0,int(input("Upgrade times: ").strip()))
        except ValueError:
            print(INVALID_INPUT)
            continue
        upgrade(upgrade_choice,upgrade_times)
def main_menu():
    while True:
        print(cookies)
        user_input=input("Menu: ").strip().lower()
        if user_input in ["enter","e"]:
            enter()
        elif user_input in ["upgrade","up"]:
            handle_upgrade()
        elif user_input in EXIT:
            break
        else:
            print(INVALID_INPUT)
def main():
    main_menu()
    print("Bye!")
if __name__=="__main__":
    main()