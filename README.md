# cookie-enter.py
Cookie enter game i made with python! Have fun!

**Disclamer!** Version 1.1.3 and above doesn't have real .exe files (they are Linux binary's) at least what I think! If you want more infomation there exist an issue in issue tracker: https://github.com/Alfix-Januarivinter/cookie-enter.py/issues/1

You need to have nerdfont installed on your system for the version 1.1.5+ symbols to be displayed properly!

## Tkinter
If you want aren't on windows and want to use the .py files you have to install tkinter (you won't need to install tkinter if you are using the .exe file)

### **On MacOS**
```bash
brew install tcl-tk
```

### **On Arch Linux**
```bash
sudo pacman -S tk
```

### **On Debian**
```bash
sudo apt-get install tk-dev tk8.6-dev libtk8.6 libtcl8.6 tcl-dev
```   

## Compiling from source
You need the ```cookie.enter.py``` file, if you haven't already install pyinstaller :
```bash
pip install pyinstaller
```
or
```bash
pipx install pyinstaller
```

You need a terminal in the same folder as the file, and then to compile the python file:
```bash
pyinstaller --onefile cookie-enter.py
```

## For myself if I forget how to push using git. (Hehe)
Add files to git
```bash
git add .
```

Commit your changes with a message
```bash
git commit -m "Some stupid message"
```

Push it to the repository
```bash
git push -u origin main
```

If you get an error, just try this:
```bash
git pull origin main --allow-unrelated-histories   
```

And if somehow the project isn't a remote repository then:
```bash
git init
```
```bash
git remote add origin https://github.com/Alfix-Januativinter/another-useless-repository
```
