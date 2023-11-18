num = int(input("Input Number: "))
text = " "
count = num
for x in range(num): 
    text += "*"
    if x > 0:
        text += "*"
    print(" "*(count-1),text)
    count -= 1