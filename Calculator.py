from tkinter import *

root = Tk()
root.title('Calculator')

text = Entry(root, width =38, borderwidth=5)
text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
cal_icon = PhotoImage(file=r'widgets/calculator-icon.png')
root.iconphoto(False, cal_icon)


fun=''
num2=0
text.insert(0, 0)
i=0
global num1


def button_click(num):
    global i
    if i==0:
        text.delete(0,END)
        i+=1
    current = text.get()
    text.delete(0, END)
    text.insert(0, current+str(num))


def clear():
    global num1
    global num2
    global fun
    global i
    num1=0
    i=0
    num2=0
    fun=''
    equal()
    text.delete(0, END)
    text.insert(0, 0)


def button_add():
    global num1
    global fun
    equal()
    num1 = text.get()
    fun='+'
    text.delete(0, END)


def button_sub():
    global num1
    global fun
    equal()
    num1 = text.get()
    fun='-'
    text.delete(0, END)


def button_mul():
    global num1
    global fun
    equal()
    num1 = text.get()
    fun='x'
    text.delete(0, END)


def button_div():
    global num1
    global fun
    equal()
    num1 = text.get()
    fun = '/'
    text.delete(0, END)


def equal():
    global num2
    global num1
    global fun

    if fun != '':
        num2 = text.get()
        text.delete(0, END)
    if fun == '+':
        ans = int(num2)+int(num1)
        text.insert(0, int(num2)+int(num1))
        num2 = num1
        num1 = ans

    elif fun == '-':
        ans = int(num1)-int(num2)
        text.insert(0, int(num1)-int(num2))
        num2 = num1
        num1 = ans

    elif fun == 'x':
        ans = int(num1)*int(num2)
        text.insert(0, ans)
        num2 = num1
        num1 = ans

    elif fun == '/':
        ans = int(num1)//int(num2)
        text.insert(0, ans)
        num2 = num1
        num1 = ans

    else:
        pass
    fun =''

button_1= Button(root, text='1', padx= 40, pady=20, command=lambda: button_click(1))
button_2= Button(root, text='2', padx= 40, pady=20, command=lambda: button_click(2))
button_3= Button(root, text='3', padx= 40, pady=20, command=lambda: button_click(3))
button_4= Button(root, text='4', padx= 40, pady=20, command=lambda: button_click(4))
button_5= Button(root, text='5', padx= 40, pady=20, command=lambda: button_click(5))
button_6= Button(root, text='6', padx= 40, pady=20, command=lambda: button_click(6))
button_7= Button(root, text='7', padx= 40, pady=20, command=lambda: button_click(7))
button_8= Button(root, text='8', padx= 40, pady=20, command=lambda: button_click(8))
button_9= Button(root, text='9', padx= 40, pady=20, command=lambda: button_click(9))
button_0= Button(root, text='0', padx= 40, pady=20, command=lambda: button_click(0))
button_add= Button(root, text='+', padx= 40, pady=20, command=button_add)
button_sub= Button(root, text='-', padx= 40, pady=20, command=button_sub)
button_mul= Button(root, text='x', padx= 40, pady=20, command=button_mul)
button_div= Button(root, text='/', padx= 42, pady=20, command=button_div)
button_equal= Button(root, text='=', padx= 40, pady=20, command=equal)
button_clear= Button(root, text='C', padx= 39, pady=20, command=clear)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=4, column=1)
button_sub.grid(row=4, column=2)
button_equal.grid(row=4, column=3)

button_clear.grid(row=1, column=3)
button_mul.grid(row=2, column=3)
button_div.grid(row=3, column=3)

root.mainloop()
