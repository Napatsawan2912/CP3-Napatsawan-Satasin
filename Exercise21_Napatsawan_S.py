from tkinter import *
import math

def leftClickButton(event):
    BMI = (float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    if BMI >= 30.0:
        labelResult.configure(text="อ้วนมาก")
    elif BMI >= 25.0 and BMI <= 29.9:
        labelResult.configure(text="อ้วน")
    elif BMI >= 23.0 and BMI <= 24.9:
        labelResult.configure(text="น้ำหนักเกิน")
    elif BMI >= 18.6 and BMI <= 22.9:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    elif BMI <= 18.5:
        labelResult.configure(text="ผอมเกินไป")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()