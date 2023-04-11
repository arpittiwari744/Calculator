from tkinter import *
#Create window 
root = Tk()
Tk.title(root, "Simple Calculator")
#Input field  
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10,ipadx=10,ipady=10)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+ str(number))

def button_add():
    first_number = e.get()
    global f_num
    global opt
    opt = "addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_subtract():
    first_number = e.get()
    global f_num
    global opt
    opt = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global opt
    opt = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num
    global opt
    opt = "division"
    f_num = int(first_number)
    e.delete(0,END)

def button_clear():
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if opt == "addition":
        e.insert(0, f_num + int(second_number))

    if opt == "subtraction":
        e.insert(0, f_num - int(second_number))

    if opt == "multiplication":
        e.insert(0, f_num * int(second_number))

    if opt == "division":
        e.insert(0, f_num / int(second_number))

#Buttons of Calculator
Button_1 = Button(root, text="1", padx=20, pady=20,
                  command=lambda: button_click(1))

Button_2 = Button(root, text="2", padx=20, pady=20,
                  command=lambda: button_click(2))

Button_3 = Button(root, text="3", padx=20, pady=20,
                  command=lambda: button_click(3))

Button_4 = Button(root, text="4", padx=20, pady=20,
                  command=lambda: button_click(4))

Button_5 = Button(root, text="5", padx=20, pady=20,
                  command=lambda: button_click(5))

Button_6 = Button(root, text="6", padx=20, pady=20,
                  command=lambda: button_click(6))

Button_7 = Button(root, text="7", padx=20, pady=20,
                  command=lambda: button_click(7))

Button_8 = Button(root, text="8", padx=20, pady=20,
                  command=lambda: button_click(8))

Button_9 = Button(root, text="9", padx=20, pady=20,
                  command=lambda: button_click(9))

Button_0 = Button(root, text="0", padx=20, pady=20,
                  command=lambda: button_click(0))

Button_add = Button(root, text="+", padx=20, pady=20, command=button_add)

Button_subtract = Button(root, text="-", padx=20,
                         pady=20, command=button_subtract)

Button_multiply = Button(root, text="*", padx=20,
                         pady=20, command=button_multiply)

Button_divide = Button(root, text="/", padx=20, pady=20, command=button_divide)

Button_clear = Button(root, text="C", padx=20, pady=20, command=button_clear)

Button_equal = Button(root, text="=", padx=20, pady=20, command=button_equal)

Button_1.grid(row=3, column=1)
Button_2.grid(row=3, column=2)
Button_3.grid(row=3, column=3)

Button_4.grid(row=2, column=1)
Button_5.grid(row=2, column=2)
Button_6.grid(row=2, column=3)

Button_7.grid(row=1, column=1)
Button_8.grid(row=1, column=2)
Button_9.grid(row=1, column=3)
Button_0.grid(row=4, column=2)

Button_add.grid(row=3, column=4)
Button_subtract.grid(row=2, column=4)
Button_multiply.grid(row=1, column=4)
Button_divide.grid(row=4, column=3)

Button_clear.grid(row=4, column=1)
Button_equal.grid(row=4, column=4)

root.mainloop()