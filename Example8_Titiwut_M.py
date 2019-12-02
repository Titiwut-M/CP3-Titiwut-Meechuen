usernameInput = input("Enter username : ")
passwordInput = input("Enter password : ")
if usernameInput == "titiwut" and passwordInput == "1234":
    print("------Welcome to KONG's Shop------")
    print("1. PlayStation 4 2700 THB")
    print("2. Nintendo Switch 9500 THB")
    print("3. Earphone 5900 THB")
    print("4. iPhone 36000 THB")
    print("5. If you want to cancel your order")
    yourProduct = int(input("Enter product number: "))
    if yourProduct == 1:
        print("How many PlayStation 4 do you want to buy?")
        numberProduct1 = int(input(">>"))
        sum1 = 2700*numberProduct1
        print("Total =",sum1,"THB","Thank you For Purchase")
    elif yourProduct == 2:
        print("Total =","How many Nintento Switch do you want to buy?")
        numberProduct2 = int(input(">>"))
        sum2 = 9500*numberProduct2
        print("Total =",sum2,"THB","Thank you For Purchase")
    elif yourProduct == 3:
        print("How many Earphone do you want to buy?")
        numberProduct3 = int(input(">>"))
        sum3 = 5900*numberProduct3
        print("Total =",sum3,"THB","Thank you For Purchase")
    elif yourProduct == 4:
        print("How many iPhone do you want to buy?")
        numberProduct4 = int(input(">>"))
        sum4 = 36000*numberProduct4
        print("Total =",sum4,"THB","Thank you For Purchase")
    else:
        print("------See You Next Time------")
else:
    print("Wrong Username or Password")
    print("Please Try again")