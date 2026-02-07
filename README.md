# cookie-enter.py
Cookie enter game i made with python! Have fun!

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
