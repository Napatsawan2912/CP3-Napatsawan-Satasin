menuList = []
priceList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName) 
        priceList.append(menuPrice)
showBill()

print("----------------")   
total = 0
for number in range(len(priceList)):
    total += priceList[number]
print("Total Price is %d THB" %(total))  