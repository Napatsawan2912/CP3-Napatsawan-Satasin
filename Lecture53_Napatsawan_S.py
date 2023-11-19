def vatCalculate(TotalPrice):
    result = TotalPrice+(TotalPrice*7/100)
    return result

price = int(input("Input Price: "))
print("---------------------")
print("Total Price is", vatCalculate(price), "THB")