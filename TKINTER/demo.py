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
# window.title('Simple')
# window.geometry('500x600')
# window.configure(bg='green')
# frame1 = Frame(window,width=300,height=300,cursor= "dot")
# frame2 = Frame(window,width=300,height=300,cursor= "dotbox")
# button1 = Button(frame1,text="Button 1",bg='blue')
# button2 = Button(frame2,text="Button 2",bg='red')
# button3 = Button(frame1,text="Button 3",bg='yellow',fg='red')
#
# frame1.pack(side=TOP)
# frame2.pack(side=BOTTOM)
# button1.pack()
# button2.pack()
# button3.pack()



# window.geometry('250x350')
# e1 = Entry(window,width=40,borderwidth=5)
# e2 = Entry(window,width=40,borderwidth=5)
#
# label1 = Label(window, text='Mail')
# label2 = Label(window, text='Password')
#
# label1.grid(column=1, row=0)
# label2.grid(column=1, row=1)
# e1.grid(column=2, row=0)
# e2.grid(column=2, row=1)

window.geometry('500x500')
# label1 = Label(window, text='Label 1',bg='red',fg='white')
# label2 = Label(window, text='Label 2',bg='blue',fg='white')
# label3 = Label(window, text='Label 3',bg='green',fg='white')
# label4 = Label(window, text='Label 4',bg='yellow',fg='black')
#
# label1.pack(side = TOP, fill = X, expand = False)
# label2.pack(side = LEFT, fill = Y, expand = False)
# label3.pack(side = RIGHT, fill = Y, expand = False)
# label4.pack(side = BOTTOM, fill = X, expand = False)

# def log_entry():
#     print("Logged in")
#
# button = Button(window,text='Login',command=log_entry,width=12,bg='red',fg='white',font=('Arial',12,'bold'),activebackground='green',activeforeground='black')
# button.pack()


# label1.pack()

# menu = Menu(window)
# file = Menu(menu, tearoff=0)
# file.add_command(label='New')
# file.add_command(label='Open')
# file.add_command(label='Save')
# file.add_command(label='Save As')
# file.add_separator()
# file.add_command(label='Exit',command=window.quit)
#
# menu.add_cascade(label='File', menu=file)
#
# window.config(menu=menu)

# import tkinter.messagebox
# tkinter.messagebox.showinfo('Info','Running out of time.')
# tkinter.messagebox.showerror('Error','Something went wrong.')
# tkinter.messagebox.showwarning('Warning','Something went wrong.')
# Question = tkinter.messagebox.askyesno('Weather','Will it rain?')
#
# if Question == True:
#     print('Take an Umbrella')
# else:
#     print('Ok')

# c = Canvas(window,width=500,height=500)
# c.pack()
#
# c.create_line(0,0,500,500,fill='green',width=5,dash=(4,4))
# c.create_line(0,500,500,0,fill='blue',width=5,dash=(4,4))
# c.create_rectangle(150,125,450,375,fill='red',outline='yellow',width=5)

# message1 = Message(window, text='Python')
# message1.pack()

# var = StringVar()
# message2 = Message(window, textvariable=var,relief=RAISED,padx=10,pady=10)
# var.set("Welcome")
# message2.pack()

# var = StringVar()
# entry_var = StringVar()
# def insert():
#     result = entry_var.get()
#     var.set(result)
#
# message3 = Message(window, textvariable=var,relief=RAISED,padx=50,pady=50)
# entry = Entry(window,textvariable=entry_var)
# button = Button(window,text="Ok",command=insert)
# message3.pack()
# entry.pack()
# button.pack()

#
# checkBox1 = IntVar()
# checkBox2 = IntVar()
# checkBox3 = IntVar()
# checkBox4 = IntVar()
#
# chk_btn_1 = Checkbutton(window,text='Apple',onvalue=1, offvalue=0, height=2,width=10)
# chk_btn_2 = Checkbutton(window,text='Banana',onvalue=1, offvalue=0, height=2,width=10)
# chk_btn_3 = Checkbutton(window,text='Orange',onvalue=1, offvalue=0, height=2,width=10)
# chk_btn_4 = Checkbutton(window,text='Pulm',onvalue=1, offvalue=0, height=2,width=10)
#
# chk_btn_1.pack()
# chk_btn_2.pack()
# chk_btn_3.pack()
# chk_btn_4.pack()


button = Button(window, text = 'Button', width =5, height =5)
button.place(x=400,y=400)



mainloop()