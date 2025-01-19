#version 1.0.8 (release) sandbox if bug contact a developer https://github.com/Alfix-Januarivinter/cookie-enter.py
c = int(input("enter cookies: "))
b = int(input("enter multiplier: "))
print("Welcome to Cookie enter! Sandbox edition!")
l = "To little cookies!"
p = "Wrong input!"
x = "exit"
z = "esc"
while True:
    print(c)
    a = input("Menu: ")
    if a == "sandbox" or a == "s":
        while True:
            print(c)
            print(b)
            a = input("sandbox: ")
            if a == "reset" or a == "r":
                c = 0
                b = 1
            elif a == "unlimited" or a == "un":
                c = 10000000000000000000000000000000000000000000000000000000000000
                b = 100000000000000000000
            elif a == "2":
                c = c + c
                b = b + b
            elif a == "choose" or a == "co":
                c = int(input("enter cookies: "))
                b = int(input("enter multiplier: "))  
            elif a == x or a == z:
                break
            else:
                print(p)
    if a == "enter" or a == "e":
        while True:
            print(c)
            a = input(": ")
            if a == x or a == z:
                break
            else:
                c = c + b
    elif a == "upgrade" or a == "up":
        while True:
            print("cookies = " + str(c))
            print("cookie multiplier = " + str(b))
            print("+1 = 100 / +2 = 200 / +5 = 450 / +10 = 800 / +20 = 1400 / +50 = 3000 / +100 = 4500")
            a = input("Upgrade: ")
            if a == x or a == z:
                break
            h = int(input("Upgrade times: "))
            if h < 0:
                h = 0
            if a == "1":
                h1 = h * 100
                if c >= h1:
                    c = c - h1
                    b = b + h
                else:
                    print(l)
            elif a == "2":
                h2 = h * 200
                d2 = h * 2
                if c >= h2:
                    c = c - h2
                    b = b + d2
                else:
                    print(l)
            elif a == "5":
                h3 = h * 450
                d3 = h * 5
                if c >= h3:
                    c = c - h3
                    b = b + d3
                else:
                    print(l)
            elif a == "10":
                h4 = h * 800
                d4 = h * 10
                if c >= h4:
                    c = c - h4
                    b = b + d4
                else:
                    print(l)
            elif a == "20":
                h5 = h * 1400
                d5 = h * 20
                if c >= h5:
                    c = c - h5
                    b = b + d5
                else:
                    print(l)
            elif a == "50":
                h6 = h * 3000
                d6 = h * 50
                if c >= h6:
                    c = c - h6
                    b = b + d6
                else:
                    print(l)
            elif a == "100":
                h7 = h * 4500
                d = h * 100
                if c >= h7:
                    c = c - h7
                    b = b + d
                else:
                    print(l)
            else:
                print(p)
    elif a == x or a == z:
        break
    else:
        print(p)
print("bye!")