Username = input("Username: ")
Password = input("Password: ")
if Username == "cus" and Password == "001" :
    print("--------------------")
    print("Welcome to My shop!")
    print("1. Apple        50THB")
    print("2. Banana        70THB")
    print("3. Orange        40THB")
    print("--------------------")
    fruit = int(input("Choose the fruit you want(1-3): "))
    amount = int(input("How many fruits do you want: "))
    print("--------------------")
    if fruit == 1 :
        print("Total price is",50*amount,"THB")
    elif fruit == 2 :
        print("Total price is",70*amount,"THB")
    elif fruit == 3 :
        print("Total price is",40*amount,"THB")
    print("--------------------")
    print("Thank You!!")
else :
    print("ERROR!!")
