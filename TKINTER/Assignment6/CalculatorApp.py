# Module 10 & 11: CALCULATOR USING TKINTER

# Steps to follow
# Step 1: importing modules
# Step 2: GUI integration
# Step 3: Adding Inputs
# Step 4: mainloop


from tkinter import *

window = Tk()
window.geometry('400x450')
window.title('Calculator')
window.configure(background = "light blue")

# Entry box for input from user
EntryBox = Entry(window, width = 40 , borderwidth = 2, bg = 'lightgreen', fg = 'black', font = ('Arial',12))
EntryBox.place(x=30,y=30,width=340,height=35)

# Buttons

# Functionality

def click(num):
    result = EntryBox.get()
    EntryBox.delete(0, END)
    EntryBox.insert(0, str(result) + str(num))

Button1 = Button(window, text = '1', width =10, height=2, bg='light blue',fg='black',font= ('Arial',12,'bold'), relief=RAISED, command= lambda : click(1))
Button1.place(x=30,y=80)

Button2 = Button(window, text = '2', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command= lambda : click(2))
Button2.place(x=145,y=80)

Button3 = Button(window, text = '3', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command= lambda : click(3))
Button3.place(x=260,y=80)

Button4 = Button(window, text = '4', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command= lambda : click(4))
Button4.place(x=30,y=140)

Button5 = Button(window, text = '5', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command= lambda : click(5))
Button5.place(x=145,y=140)

Button6 = Button(window, text = '6', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command= lambda : click(6))
Button6.place(x=260,y=140)

Button7 = Button(window, text = '7', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command= lambda : click(7))
Button7.place(x=30,y=200)

Button8 = Button(window, text = '8', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command= lambda : click(8))
Button8.place(x=145,y=200)

Button9 = Button(window, text = '9', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command= lambda : click(9))
Button9.place(x=260,y=200)

Button0 = Button(window, text = '0', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command= lambda : click(0))
Button0.place(x=30,y=260)


# Operators
def add():
    result = EntryBox.get()
    global math
    math = 'Addition'
    global i
    i = int(result)
    EntryBox.delete(0, END)


ButtonP = Button(window, text = '+', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command = add)
ButtonP.place(x=145,y=260)


def sub():
    result = EntryBox.get()
    global math
    math = 'Subtraction'
    global i
    i = int(result)
    EntryBox.delete(0, END)


ButtonM = Button(window, text = '-', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command = sub)
ButtonM.place(x=260,y=260)


def mul():
    result2 = EntryBox.get()
    global math
    math = 'Multiplication'
    global i
    i = int(result2)
    EntryBox.delete(0, END)


ButtonMul = Button(window, text = '*', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command = mul)
ButtonMul.place(x=30,y=320)


def div():
    result = EntryBox.get()
    global math
    math = 'Division'
    global i
    i = int(result)
    EntryBox.delete(0, END)


ButtonDiv = Button(window, text = '/', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command = div)
ButtonDiv.place(x=145,y=320)


def equal():
    result = EntryBox.get()
    EntryBox.delete(0, END)
    if math == 'Addition':
        EntryBox.insert(0, int(i) + int(result))
    elif math == 'Subtraction':
        EntryBox.insert(0, int(i) - int(result))
    elif math == 'Multiplication':
        EntryBox.insert(0, int(i) * int(result))
    elif math == 'Division':
        EntryBox.insert(0, int(i)/int(result))



ButtonEqual = Button(window, text = '=', width =10, height=2, bg= 'light blue',fg='black', font=('Arial',12,'bold'), relief=RAISED, command = equal)
ButtonEqual.place(x=260,y=320)



def Clear():
    EntryBox.delete(0, END)

ButtonClear = Button(window, text = 'Clear', width =33, height=2, bg= 'salmon',fg='black', font=('Arial',12,'bold'), relief=RAISED, command=Clear)
ButtonClear.place(x=30,y=380)



mainloop()
