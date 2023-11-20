menuList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0])

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append([menuName, menuPrice]) 
showBill()

print("----------------")   
total = 0
for number in range(len(menuList)):
    total += menuList[number][1]
print("Total Price is %d THB" %(total))