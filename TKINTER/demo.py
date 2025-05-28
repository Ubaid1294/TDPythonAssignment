# Step 1: import tkinter
# Step 2: GUI interaction
# Step 3: Adding inputs
# Step 4: main loop
# from tkinter import *
# window = Tk()
# inp = Label(window,text='Hello World!')
# inp.pack()
# window.mainloop()
from tkinter import *
window = Tk()
window.title('Simple')
window.geometry('500x600')
window.configure(bg='green')
frame1 = Frame(window,width=300,height=300,cursor= "dot")
frame2 = Frame(window,width=300,height=300,cursor= "dotbox")
button1 = Button(frame1,text="Button 1",bg='blue')
button2 = Button(frame2,text="Button 2",bg='red')
button3 = Button(frame1,text="Button 3",bg='yellow',fg='red')

frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button1.pack()
button2.pack()
button3.pack()


mainloop()