#version 1.0.3 (release) if bug contact a developer https://github.com/Alfix-Januarivinter/cookie-enter.py
cookies = 0
cookie_multi = 1
print("welcome to cookie enter")
while True:
    print(cookies)
    what_todo = input("Menu: ")
    if what_todo == "enter":
        while True:
            print(cookies)
            enter = input(": ")
            if enter == "exit":
                break
            else:
                cookies = cookies + cookie_multi
    elif what_todo == "upgrade":
        while True:
            print("cookies = " + str(cookies))
            print("cookie multiplier = " + str(cookie_multi))
            print("*+1 = 100 *+2 = 200 *+5 = 450 *+10 = 800 *+20 = 1400 *+50 = 3000 *+100 = 4500")
            up = input("Upgrade: ")
            if up == "1":
                if cookies >= 100:
                    cookies = cookies - 100
                    cookie_multi = cookie_multi + 1
                else:
                    print("to little cookies")
            elif up == "2":
                if cookies >= 200:
                    cookies = cookies - 200
                    cookie_multi = cookie_multi + 2
                else:
                    print("to little cookies")
            elif up == "5":
                if cookies >= 450:
                    cookies = cookies - 450
                    cookie_multi = cookie_multi + 5
                else:
                    print("to little cookies")
            elif up == "10":
                if cookies >= 800:
                    cookies = cookies - 800
                    cookie_multi = cookie_multi + 10
                else:
                    print("to little cookies")
            elif up == "20":
                if cookies >= 1400:
                    cookies = cookies - 1400
                    cookie_multi = cookie_multi + 20
                else:
                    print("to little cookies")
            elif up == "50":
                if cookies >= 3000:
                    cookies = cookies - 3000
                    cookie_multi = cookie_multi + 50
                else:
                    print("to little cookies")
            elif up == "100":
                if cookies >= 4500:
                    cookies = cookies - 4500
                    cookie_multi = cookie_multi + 100
                else:
                    print("to little cookies")
            elif up == "exit":
                break
            else:
                print("wrong input")
    elif what_todo == "exit":
        break
    else:
        print("wrong input")
print("bye")