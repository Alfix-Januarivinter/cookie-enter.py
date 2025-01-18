#version 1.0.5 (release) sandbox if bug contact a developer https://github.com/Alfix-Januarivinter/cookie-enter.py
c = int(input("enter cookies: "))
b = int(input("enter multiplier: "))
print("Welcome to Cookie enter! Sandbox edition!")
while True:
    print(c)
    a = input("Menu: ")
    if a == "sandbox":
        while True:
            s = input("sandbox: ")
            if s == "reset":
                c = 0
                b = 1
            elif s == "unlimited":
                c = 10000000000000000000000000000000000000000000000000000000000000
                b = 100000000000000000000
            elif s == "2":
                c = c + c
                b = b + b
            elif s == "choose":
                c = int(input("enter cookies: "))
                b = int(input("enter multiplier: "))  
            elif s == "exit":
                break
            else:
                print("wrong input!")
    if a == "enter":
        while True:
            print(c)
            enter = input(": ")
            if enter == "exit":
                break
            else:
                c = c + b
    elif a == "upgrade":
        while True:
            print("cookies = " + str(c))
            print("cookie multiplier = " + str(b))
            print("*+1 = 100 *+2 = 200 *+5 = 450 *+10 = 800 *+20 = 1400 *+50 = 3000 *+100 = 4500")
            u = input("Upgrade: ")
            h = int(input("Upgrade times: "))
            if h < 0:
                h = 0
            h1 = h * 100
            h2 = h * 200
            d2 = h * 2
            h3 = h * 450
            d3 = h * 5
            h4 = h * 800
            d4 = h * 10
            h5 = h * 1400
            d5 = h * 20
            h6 = h * 3000
            d6 = h * 50
            h7 = h * 4500
            d7 = h * 100
            if u == "1":
                if c >= h1:
                    c = c - h1
                    b = b + h
                else:
                    print("to little cookies!")
            elif u == "2":
                if c >= h2:
                    c = c - h2
                    b = b + d2
                else:
                    print("to little cookies!")
            elif u == "5":
                if c >= h3:
                    c = c - h3
                    b = b + d3
                else:
                    print("to little cookies!")
            elif u == "10":
                if c >= h4:
                    c = c - h4
                    b = b + d4
                else:
                    print("to little cookies!")
            elif u == "20":
                if c >= h5:
                    c = c - h5
                    b = b + d5
                else:
                    print("to little cookies!")
            elif u == "50":
                if c >= h6:
                    c = c - h6
                    b = b + d6
                else:
                    print("to little cookies!")
            elif u == "100":
                if c >= h7:
                    c = c - h7
                    b = b + d7
                else:
                    print("to little cookies!")
            elif u == "exit":
                break
            else:
                print("wrong input!")
    elif a == "exit":
        break
    else:
        print("wrong input!")
print("bye!")