#version 1.0.4 (release) if bug contact a developer https://github.com/Alfix-Januarivinter/cookie-enter.py
#1.0.4 c = Cookies b = Cookie_Multi a = what_todo u = up
c = 0
b = 1
print("welcome to Cookie enter")
while True:
    print(c)
    a = input("Menu: ")
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
            if u == "1":
                if c >= 100:
                    c = c - 100
                    b = b + 1
                else:
                    print("to little cookies")
            elif u == "2":
                if c >= 200:
                    c = c - 200
                    b = b + 2
                else:
                    print("to little cookies")
            elif u == "5":
                if c >= 450:
                    c = c - 450
                    b = b + 5
                else:
                    print("to little cookies")
            elif u == "10":
                if c >= 800:
                    c = c - 800
                    b = b + 10
                else:
                    print("to little cookies")
            elif u == "20":
                if c >= 1400:
                    c = c - 1400
                    b = b + 20
                else:
                    print("to little cookies")
            elif u == "50":
                if c >= 3000:
                    c = c - 3000
                    b = b + 50
                else:
                    print("to little cookies")
            elif u == "100":
                if c >= 4500:
                    c = c - 4500
                    b = b + 100
                else:
                    print("to little cookies")
            elif u == "exit":
                break
            else:
                print("wrong input")
    elif a == "exit":
        break
    else:
        print("wrong input")
print("bye")