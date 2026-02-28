# Cookie-enter.py Version 1.1.7 (CPS and unlocking Update!)
# If you encounter any bugs/issues, please contact the developer at:
# https://github.com/Alfix-Januarivinter/cookie-enter.py

import json
import tkinter as tk

import pygame

pygame.mixer.init()

# Save file
SAVE_FILE = "cookie_save.json"
GAME_VERSION = "1.1.7"
INCOMPATIBLE_VERSIONS = ["1.1.1", "1.1.2", "1.1.3b", "1.1.3"]

# Constants and Variables
cookies = 0
multiplier = 1
ascending_multiplier = 1
ascending_cost = 1000
cps = 0
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

CPS_UPGRADE_TIERS = [
    {"asc": 5, "unlock_cookies": 2500, "cost": 500, "cps": 1},
    {"asc": 7, "unlock_cookies": 10000, "cost": 4500, "cps": 10},
    {"asc": 10, "unlock_cookies": 40000, "cost": 20000, "cps": 50},
    {"asc": 12, "unlock_cookies": 70000, "cost": 30000, "cps": 100},
]

MAX_CPS_UNLOCK_ASC = 15
MAX_CPS_UNLOCK_COST = 1000000
MAX_CPS_PER_500 = 1

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

upgrade_buttons = []
cps_upgrade_buttons = []
max_upgrade_button = None
unlocked_upgrades = set()
unlocked_cps_upgrades = set()


# Functions
def format_number(value: int) -> str:
    return f"{value:,}".replace(",", "'")


def play_sound(file):
    try:
        pygame.mixer.Sound(file).play()
    except Exception:
        pass


def unlock_multiplier(upgrade_key):
    global cookies
    full_cost, increase = UPGRADE_OPTIONS[upgrade_key]
    unlock_cost = full_cost // 10

    if upgrade_key in unlocked_upgrades:
        return

    if cookies >= unlock_cost:
        cookies -= unlock_cost
        unlocked_upgrades.add(upgrade_key)
        play_sound("upgrade.mp3")
        status_label.config(
            text=f" Unlocked +{format_number(increase)} multiplier!", fg="green"
        )
    else:
        status_label.config(text="Not enough cookies to unlock! ", fg="red")

    update_display()
    for win in list(open_windows):
        if win.title() == "Upgrade Menu":
            close_window(win)
            break
    open_upgrade_menu()


def update_display():
    global upgrade_buttons, cps_upgrade_buttons, max_upgrade_button
    cookie_label.config(text=f"Cookies : {format_number(cookies)}󰆘")
    net_label.config(
        text=f"Net Worth : {format_number(ascending_cost - 1000 + cookies + ((multiplier - 1) * 45) + (cps * 300))}󰆘"
    )
    multiplier_label.config(text=f"Multiplier: {format_number(multiplier)}")
    ascending_label.config(text=f"Ascending: {format_number(ascending_multiplier)}")
    ascending_button.config(
        text=f"Upgrade Ascending Multiplier cost: {format_number(ascending_cost)}󰆘 Cookies"
    )
    cps_label.config(text=f"CPS: {format_number(cps)}󱐋")

    alive = []
    for entry in upgrade_buttons:
        try:
            btn = entry["button"]
            if not btn.winfo_exists():
                continue
            if entry.get("is_unlock", False):
                full_cost, _ = UPGRADE_OPTIONS[entry["key"]]
                unlock_cost = full_cost // 10
                if cookies >= unlock_cost:
                    btn.config(state=tk.NORMAL, bg="#ffeb3b", fg="black")
                else:
                    btn.config(state=tk.DISABLED, fg="darkgray", bg="gray")
            else:
                btn.config(state=tk.NORMAL if cookies >= entry["cost"] else tk.DISABLED)
            alive.append(entry)
        except tk.TclError:
            pass
    upgrade_buttons[:] = alive

    ascending_button.config(
        state=tk.NORMAL if cookies >= ascending_cost else tk.DISABLED
    )

    if max_upgrade_button is not None:
        try:
            if max_upgrade_button.winfo_exists():
                max_upgrades = int(cookies / 100)
                max_cost = int(max_upgrades * 100)
                if ascending_multiplier <= 5:
                    new_text = f"Max: +{format_number(max_upgrades)} = {format_number(max_cost)}󰆘"
                    state = tk.NORMAL if max_upgrades > 0 else tk.DISABLED
                    fg_color = "white" if dark_mode else "black"
                else:
                    new_text = f"Locked — requires Ascending ≤ 5 (current: {ascending_multiplier})"
                    state = tk.DISABLED
                    fg_color = "red"
                max_upgrade_button.config(text=new_text, state=state, fg=fg_color)
        except tk.TclError:
            pass

    new_list = []
    for btn in cps_upgrade_buttons:
        try:
            if not btn.winfo_exists():
                continue
            text = btn.cget("text")
            if "Unlock" in text:
                for tier in CPS_UPGRADE_TIERS:
                    if str(tier["unlock_cookies"]) in text:
                        if (
                            ascending_multiplier >= tier["asc"]
                            and cookies >= tier["unlock_cookies"]
                        ):
                            btn.config(state=tk.NORMAL, bg="#ffeb3b", fg="black")
                        else:
                            btn.config(state=tk.DISABLED, fg="darkgray", bg="gray")
                        break
            else:
                theme = DARK_THEME if dark_mode else LIGHT_THEME
                affordable = False
                if "Max CPS" in text:
                    affordable = (
                        ascending_multiplier >= MAX_CPS_UNLOCK_ASC
                        and cookies >= MAX_CPS_UNLOCK_COST
                    )
                else:
                    try:
                        cost_str = (
                            text.split("=")[-1]
                            .strip()
                            .split("󰆘")[0]
                            .replace("'", "")
                            .replace(",", "")
                        )
                        cost = int(cost_str)
                        affordable = cookies >= cost
                    except (ValueError, IndexError):
                        pass

                if affordable:
                    btn.config(state=tk.NORMAL, bg=theme["button_bg"], fg=theme["fg"])
                else:
                    btn.config(state=tk.DISABLED, fg="darkgray", bg="gray")
            new_list.append(btn)
        except tk.TclError:
            pass
    cps_upgrade_buttons[:] = new_list


def auto_collect():
    global cookies
    cookies += cps * ascending_multiplier
    update_display()
    root.after(1000, auto_collect)


def collect_cookies():
    global cookies
    cookies += (multiplier) * ascending_multiplier
    play_sound("click.mp3")
    update_display()


def upgrade_multiplier(upgrade_key):
    global cookies, multiplier
    cost, increase = UPGRADE_OPTIONS[upgrade_key]
    if cookies >= cost:
        cookies -= cost
        multiplier += increase
        play_sound("upgrade.mp3")
        status_label.config(text="Upgrade successful !", fg="green")
    else:
        status_label.config(text="Too few cookies !", fg="red")
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
    global max_upgrade_button
    if max_upgrade_button is not None:
        try:
            if max_upgrade_button.winfo_toplevel() == window:
                max_upgrade_button = None
        except tk.TclError:
            max_upgrade_button = None
    window.destroy()


def max_upgrade():
    global cookies, multiplier
    max_upgrades = int(cookies / 100)
    max_cost = int(max_upgrades * 100)
    if ascending_multiplier > 5:
        status_label.config(
            text=f"Max upgrade locked — requires Ascending ≤ 5 (current: {ascending_multiplier})",
            fg="orange",
        )
        play_sound("click.mp3")
        return
    if cookies >= max_cost:
        cookies -= max_cost
        multiplier += max_upgrades
        play_sound("upgrade.mp3")
        status_label.config(text="Upgrade successful !", fg="green")
    else:
        status_label.config(text="Too few cookies !", fg="red")
    update_display()


def open_upgrade_menu():
    global upgrade_buttons
    upgrade_buttons = []
    upgrade_window = tk.Toplevel(root)
    upgrade_window.title("Upgrade Menu")
    upgrade_window.geometry("525x650")

    open_windows.append(upgrade_window)
    upgrade_window.protocol(
        "WM_DELETE_WINDOW", lambda w=upgrade_window: close_window(w)
    )

    tk.Label(upgrade_window, text="Choose an Upgrade", font=("Arial", 14)).pack(pady=10)

    for key, (cost, increase) in UPGRADE_OPTIONS.items():
        if key in unlocked_upgrades:
            btn = tk.Button(
                upgrade_window,
                text=f"+{format_number(increase)} Multiplier = {format_number(cost)}󰆘 Cookies",
                font=("Arial", 14),
                width=37,
                padx=10,
                pady=6,
                command=lambda k=key: [play_sound("click.mp3"), upgrade_multiplier(k)],
            )
        else:
            unlock_cost = cost // 10
            btn = tk.Button(
                upgrade_window,
                text=f" Unlock {format_number(unlock_cost)}󰆘 (+{format_number(increase)})",
                font=("Arial", 14),
                width=37,
                padx=10,
                pady=6,
                command=lambda k=key: [play_sound("click.mp3"), unlock_multiplier(k)],
            )
            if cookies >= unlock_cost:
                btn.config(state=tk.NORMAL, bg="#ffeb3b", fg="black")
            else:
                btn.config(state=tk.DISABLED, fg="darkgray", bg="gray")

        btn.pack(pady=10)
        upgrade_buttons.append(
            {
                "button": btn,
                "cost": cost,
                "key": key,
                "is_unlock": key not in unlocked_upgrades,
            }
        )

    global max_upgrade_button
    max_upgrade_button = None
    max_upgrades = int(cookies / 100)
    max_cost = int(max_upgrades * 100)
    if ascending_multiplier <= 5:
        txt = f"Max: +{format_number(max_upgrades)} Multiplier = {format_number(max_cost)}󰆘 Cookies"
        state = tk.NORMAL if max_upgrades > 0 else tk.DISABLED
        fg_color = "white" if dark_mode else "black"
    else:
        txt = f"Locked — requires Ascending ≤ 5 (current: {ascending_multiplier})"
        state = tk.DISABLED
        fg_color = "red"
    max_btn = tk.Button(
        upgrade_window,
        text=txt,
        font=("Arial", 14),
        padx=10,
        pady=6,
        command=lambda: [play_sound("click.mp3"), max_upgrade()],
        state=state,
        fg=fg_color,
    )
    max_btn.pack(pady=10)
    max_upgrade_button = max_btn

    apply_theme_to_window(upgrade_window)
    update_display()


def cookies_ascending():
    global cookies, multiplier, ascending_multiplier, ascending_cost, cps
    if cookies >= ascending_cost:
        cookies -= ascending_cost
        leftover_multiplier = int((cookies / ascending_multiplier) / 1000)
        cookies = 0
        multiplier = 1 + leftover_multiplier
        cps = 0
        ascending_multiplier += 1
        ascending_cost *= 2
        play_sound("upgrade.mp3")
        status_label.config(text="Ascending successful !", fg="green")
        save_game()
    else:
        status_label.config(text="Too few cookies !", fg="red")
    update_display()


def open_autoclicker_menu():
    if ascending_multiplier < 5:
        status_label.config(text="Autoclicker unlocks at Ascending 5!", fg="orange")
        play_sound("click.mp3")
        return

    for win in list(open_windows):
        if win.title() == "Autoclicker Menu":
            close_window(win)
            break

    global cps_upgrade_buttons
    cps_upgrade_buttons = []
    win = tk.Toplevel(root)
    win.title("Autoclicker Menu")
    win.geometry("525x400")
    open_windows.append(win)
    win.protocol("WM_DELETE_WINDOW", lambda w=win: close_window(w))

    tk.Label(win, text="Autoclicker Upgrades (CPS)", font=("Arial", 14)).pack(pady=10)

    for i, tier in enumerate(CPS_UPGRADE_TIERS):
        asc_req = tier["asc"]
        unlock_c = tier["unlock_cookies"]
        cost = tier["cost"]
        cps_gain = tier["cps"]

        unlocked = i in unlocked_cps_upgrades

        if unlocked:
            btn = tk.Button(
                win,
                text=f"+{format_number(cps_gain)}󱐋 CPS = {format_number(cost)}󰆘 Cookies",
                font=("Arial", 14),
                width=37,
                padx=10,
                pady=6,
                command=lambda c=cost, g=cps_gain: [
                    play_sound("click.mp3"),
                    buy_cps_upgrade(c, g),
                ],
            )
            if cookies >= cost:
                btn.config(state=tk.NORMAL)
            else:
                btn.config(state=tk.DISABLED, bg="gray", fg="darkgray")
        else:
            if ascending_multiplier >= asc_req and cookies >= unlock_c:
                btn_state = tk.NORMAL
                bg_color = "#ffeb3b"
                fg_color = "black"
            else:
                btn_state = tk.DISABLED
                bg_color = "gray"
                fg_color = "darkgray"

            btn = tk.Button(
                win,
                text=f"Unlock {format_number(unlock_c)}󰆘 (+{format_number(cps_gain)} CPS) [Asc {asc_req}+]",
                font=("Arial", 14),
                width=37,
                padx=10,
                pady=6,
                state=btn_state,
                bg=bg_color,
                fg=fg_color,
                command=lambda idx=i: [play_sound("click.mp3"), unlock_cps_tier(idx)],
            )

        btn.pack(pady=10)
        cps_upgrade_buttons.append(btn)

    if ascending_multiplier >= MAX_CPS_UNLOCK_ASC:
        max_cps_affordable = cookies >= MAX_CPS_UNLOCK_COST
        max_btn = tk.Button(
            win,
            text=f"Max CPS: {format_number(MAX_CPS_UNLOCK_COST)}󰆘 for +{format_number(int(cookies // 500) * MAX_CPS_PER_500)} CPS",
            font=("Arial", 14),
            width=37,
            padx=10,
            pady=6,
            state=tk.NORMAL if max_cps_affordable else tk.DISABLED,
            bg="#ffeb3b" if max_cps_affordable else "gray",
            fg="black" if max_cps_affordable else "darkgray",
            command=lambda: [play_sound("click.mp3"), max_cps_upgrade()],
        )
    else:
        max_btn = tk.Button(
            win,
            text=f"Max CPS locked — requires Ascending {MAX_CPS_UNLOCK_ASC}",
            font=("Arial", 14),
            width=37,
            padx=10,
            pady=6,
            state=tk.DISABLED,
            bg="gray",
            fg="red",
        )
    max_btn.pack(pady=10)

    apply_theme_to_window(win)
    update_display()


def unlock_cps_tier(index):
    global cookies
    tier = CPS_UPGRADE_TIERS[index]
    if ascending_multiplier >= tier["asc"] and cookies >= tier["unlock_cookies"]:
        cookies -= tier["unlock_cookies"]
        unlocked_cps_upgrades.add(index)
        status_label.config(text="CPS tier unlocked!", fg="green")
        play_sound("upgrade.mp3")
        open_autoclicker_menu()
        update_display()
    else:
        status_label.config(text="Not enough cookies or ascending level!", fg="red")


def buy_cps_upgrade(cost, gain):
    global cookies, cps
    if cookies >= cost:
        cookies -= cost
        cps += gain
        play_sound("upgrade.mp3")
        status_label.config(text=f"+{gain} CPS added!", fg="green")
        update_display()
    else:
        status_label.config(text="Too few cookies!", fg="red")


def max_cps_upgrade():
    global cookies, cps
    if cookies >= MAX_CPS_UNLOCK_COST:
        extra_cps = int(cookies // 500) * MAX_CPS_PER_500
        cookies -= MAX_CPS_UNLOCK_COST
        cps += extra_cps
        play_sound("upgrade.mp3")
        status_label.config(text=f"+{extra_cps} CPS from max upgrade!", fg="green")
        update_display()
    else:
        status_label.config(text="Not enough cookies for max CPS!", fg="red")


def save_game():
    data = {
        "version": GAME_VERSION,
        "cookies": cookies,
        "multiplier": multiplier,
        "ascending_multiplier": ascending_multiplier,
        "ascending_cost": ascending_cost,
        "cps": cps,
        "dark_mode": dark_mode,
        "autosave_enabled": autosave_enabled,
        "unlocked_upgrades": list(unlocked_upgrades),
        "unlocked_cps_upgrades": list(unlocked_cps_upgrades),
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    status_label.config(text="Game saved 󰆓!", fg="green")


def load_game():
    global \
        cookies, \
        multiplier, \
        ascending_multiplier, \
        ascending_cost, \
        cps, \
        dark_mode, \
        autosave_enabled
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)

        if data.get("version") in INCOMPATIBLE_VERSIONS:
            status_label.config(
                text="Incompatible save version, cannot load save !", fg="red"
            )
            return

        cookies = data.get("cookies", 0)
        multiplier = data.get("multiplier", 1)
        ascending_multiplier = data.get("ascending_multiplier", 1)
        ascending_cost = data.get("ascending_cost", 1000)
        cps = data.get("cps", 0)
        dark_mode = data.get("dark_mode", False)
        autosave_enabled = data.get("autosave_enabled", False)
        unlocked_upgrades.clear()
        unlocked_upgrades.update(data.get("unlocked_upgrades", []))
        unlocked_cps_upgrades.clear()
        unlocked_cps_upgrades.update(data.get("unlocked_cps_upgrades", []))

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
    help_window.geometry("725x370")

    open_windows.append(help_window)
    help_window.protocol("WM_DELETE_WINDOW", lambda w=help_window: close_window(w))

    tk.Label(
        help_window,
        text="This is a game where you click a button and you get cookies!.\n You may see now a label that says you have 0 cookies,\n if not you haven't already clicked on the button where it says collect cookies!\n And you can get more cookies per click by upgrading your multiplier.\n You can do that by hitting upgrade multiplier button and then another menu appears.\n When hitting upgrade ascending multiplier button,\n your cookies multiplier and cps will be reset,\n but you will get some back from your leftover cookies\n and you will get 1 ascending multiplier which multiplies with your multiplier,\n and same for cps!\n Once you are at ascending 5 or higher you will unlock cps!\n Cps (cookies per secound) is a built in autoclicker that gives you cookies every secound,\n it gives you the amount of cps you have every secound!\n Have fun!\n If you encounter any bugs/issues, please contact the developer at\n https://github.com/Alfix-Januarivinter/cookie-enter.py",
        font=("Arial", 12),
    ).pack(expand=True)
    apply_theme_to_window(help_window)


def exit_game():
    save_game()
    root.quit()


# GUI
root = tk.Tk()
root.title("Cookie Enter")
root.geometry("600x700")
icon = tk.PhotoImage(file="cookie.png")
root.iconphoto(True, icon)

help_button = tk.Button(
    root,
    text="?",
    font=("Arial", 12),
    command=lambda: [play_sound("click.mp3"), open_help()],
)
help_button.place(relx=0.02, rely=0.02, anchor="nw")

net_label = tk.Label(root, font=("Arial", 14))
net_label.pack(pady=10)

cookie_label = tk.Label(root, font=("Arial", 14))
cookie_label.pack(pady=10)

multiplier_label = tk.Label(root, font=("Arial", 14))
multiplier_label.pack(pady=10)

ascending_label = tk.Label(root, font=("Arial", 14))
ascending_label.pack(pady=10)

cps_label = tk.Label(root, text="CPS: 0󱐋", font=("Arial", 14))
cps_label.pack(pady=5)

collect_button = tk.Button(
    root,
    text="Collect Cookies 󰆘",
    font=("Arial", 14),
    padx=12,
    pady=6,
    command=lambda: [play_sound("click.mp3"), collect_cookies()],
)
collect_button.pack(pady=10)

upgrade_button = tk.Button(
    root,
    text="Upgrade Multiplier ",
    font=("Arial", 14),
    padx=12,
    pady=6,
    command=lambda: [play_sound("click.mp3"), open_upgrade_menu()],
)
upgrade_button.pack(pady=10)

autoclick_button = tk.Button(
    root,
    text="Upgrade CPS 󱐋",
    font=("Arial", 14),
    padx=12,
    pady=6,
    command=lambda: [play_sound("click.mp3"), open_autoclicker_menu()],
)
autoclick_button.pack(pady=5)

ascending_button = tk.Button(
    root,
    font=("Arial", 14),
    padx=12,
    pady=6,
    command=lambda: [play_sound("click.mp3"), cookies_ascending()],
)
ascending_button.pack(pady=10)

save_button = tk.Button(
    root,
    text="Save Game 󰆓",
    font=("Arial", 14),
    padx=12,
    pady=6,
    command=lambda: [play_sound("click.mp3"), save_game()],
)
save_button.pack(pady=5)

load_button = tk.Button(
    root,
    text="Load Game 󱣪",
    font=("Arial", 14),
    padx=12,
    pady=6,
    command=lambda: [play_sound("click.mp3"), load_game()],
)
load_button.pack(pady=5)

dark_mode_var = tk.BooleanVar(value=False)
dark_mode_button = tk.Button(
    root,
    text="Toggle Themes 󰔎",
    font=("Arial", 10),
    command=lambda: [play_sound("click.mp3"), toggle_dark_mode()],
)
dark_mode_button.place(relx=0.95, rely=0.02, anchor="ne")

autosave_var = tk.BooleanVar(value=False)
autosave_button = tk.Button(
    root,
    text="Autosave",
    font=("Arial", 10),
    command=lambda: [play_sound("click.mp3"), toggle_autosave()],
)
autosave_button.place(relx=0.95, rely=0.10, anchor="ne")

status_label = tk.Label(root, font=("Arial", 12))
status_label.pack(pady=10)

exit_button = tk.Button(
    root,
    text="Exit ",
    font=("Arial", 14),
    padx=12,
    pady=6,
    command=lambda: [play_sound("click.mp3"), exit_game()],
)
exit_button.pack(side="bottom", pady=10)

load_game()
autosave_loop()
auto_collect()
root.mainloop()
