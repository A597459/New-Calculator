from tkinter import *
from tkinter import messagebox
import math
from turtle import clear

screen = Tk()
screen.title('MY calculator')
screen.maxsize(width=361, height=374)
screen.minsize(width=280, height=374)
screen.configure(bg='blue')
screen.iconbitmap('calculator.ico')


def click(number):
    global operator
    operator += str(number)
    tex.set(operator)


def clear():
    global operator
    operator = ''
    tex.set(operator)


def equal():
    global operator
    try:
        result = eval(operator)
        operator = result
        tex.set(result)
    except:
        messagebox.showinfo('Notification', 'Something went wrong', parent=screen)


def cmsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Something went wrong', parent=screen)


def cmcos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Something went wrong', parent=screen)


def cmtan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Something went wrong', parent=screen)


def cmsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Something went wrong', parent=screen)


def cmlog():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification', 'Something went wrong', parent=screen)


# Binding function:


def on_enter7(e):
    btn7.configure(bg='#a52845')


def on_leave7(e):
    btn7.configure(bg='#eee')


def on_enter8(e):
    btn8.configure(bg='#a52845')


def on_leave8(e):
    btn8.configure(bg='#eee')


def on_enter9(e):
    btn9.configure(bg='#a52845')


def on_leave9(e):
    btn9.configure(bg='#eee')


def on_enteradd(e):
    btnadd.configure(bg='#a52845')


def on_leaveadd(e):
    btnadd.configure(bg='#eee')


def on_enter4(e):
    btn4.configure(bg='#a52845')


def on_leave4(e):
    btn4.configure(bg='#eee')


def on_enter5(e):
    btn5.configure(bg='#a52845')


def on_leave5(e):
    btn5.configure(bg='#eee')


def on_enter6(e):
    btn6.configure(bg='#a52845')


def on_leave6(e):
    btn6.configure(bg='#eee')


def on_enterSub(e):
    btnSub.configure(bg='#a52845')


def on_leaveSub(e):
    btnSub.configure(bg='#eee')


def on_enter1(e):
    btn1.configure(bg='#a52845')


def on_leave1(e):
    btn1.configure(bg='#eee')


def on_enter2(e):
    btn2.configure(bg='#a52845')


def on_leave2(e):
    btn2.configure(bg='#eee')


def on_enter3(e):
    btn3.configure(bg='#a52845')


def on_leave3(e):
    btn3.configure(bg='#eee')


def on_entermul(e):
    btnmul.configure(bg='#a52845')


def on_leavemul(e):
    btnmul.configure(bg='#eee')


def on_enter0(e):
    btn0.configure(bg='#a52845')


def on_leave0(e):
    btn0.configure(bg='#eee')


def on_enterc(e):
    btnc.configure(bg='#a52845')


def on_leavec(e):
    btnc.configure(bg='#eee')


def on_enterequal(e):
    btnequal.configure(bg='#a52845')


def on_leaveequal(e):
    btnequal.configure(bg='#eee')


def on_enterdiv(e):
    btndiv.configure(bg='#a52845')


def on_leavediv(e):
    btndiv.configure(bg='#eee')


def on_enteryenter(e):
    entry1.configure(bg='brown')


def on_enteryleave(e):
    entry1.configure(bg='gray')


def on_entersin(e):
    btnsin.configure(bg='#a52845')


def on_leavesin(e):
    btnsin.configure(bg='#eee')


def on_entercos(e):
    btncos.configure(bg='#a52845')


def on_leavecos(e):
    btncos.configure(bg='#eee')


def on_entertan(e):
    btntan.configure(bg='#a52845')


def on_leavetan(e):
    btntan.configure(bg='#eee')


def on_entersqrt(e):
    btnsqrt.configure(bg='#a52845')


def on_leavesqrt(e):
    btnsqrt.configure(bg='#eee')


def on_enterlog(e):
    btnlog.configure(bg='#a52845')


def on_leavelog(e):
    btnlog.configure(bg='#eee')


tex = StringVar()
operator = ''

entry1 = Entry(screen, font=('arial', 18, 'italic bold'), border=5, justify='right',
               textvariable=tex)

entry1.grid(row=0, columnspan=4, ipadx=5, ipady=5)

btn7 = Button(screen, text=7, font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8, command=lambda: click(7),
              activebackground='pink', activeforeground='orange')
btn7.grid(row=1, column=0)

btn8 = Button(screen, text=8, font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8, command=lambda: click(8),
              activebackground='pink', activeforeground='orange')
btn8.grid(row=1, column=1)

btn9 = Button(screen, text=9, font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8, command=lambda: click(9),
              activebackground='pink', activeforeground='orange')
btn9.grid(row=1, column=2)

btnadd = Button(screen, text='+', font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8,
                command=lambda: click('+'),
                activebackground='pink', activeforeground='orange')
btnadd.grid(row=1, column=3)

btn4 = Button(screen, text=4, font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8, command=lambda: click(4),
              activebackground='pink', activeforeground='orange', )
btn4.grid(row=2, column=0)

btn5 = Button(screen, text=5, font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8, command=lambda: click(5),
              activebackground='pink', activeforeground='orange')
btn5.grid(row=2, column=1)

btn6 = Button(screen, text=6, font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8, command=lambda: click(6),
              activebackground='pink', activeforeground='orange')
btn6.grid(row=2, column=2)

btnSub = Button(screen, text='-', font=('arial', 20, 'italic bold'), border=5, padx=14, pady=8,
                command=lambda: click('-'),
                activebackground='pink', activeforeground='orange')
btnSub.grid(row=2, column=3)

btn1 = Button(screen, text=1, font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8, command=lambda: click(1),
              activebackground='pink', activeforeground='orange')
btn1.grid(row=3, column=0)

btn2 = Button(screen, text=2, font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8, command=lambda: click(2),
              activebackground='pink', activeforeground='orange')
btn2.grid(row=3, column=1)

btn3 = Button(screen, text=3, font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8, command=lambda: click(3),
              activebackground='pink', activeforeground='orange')
btn3.grid(row=3, column=2)

btnmul = Button(screen, text='*', font=('arial', 20, 'italic bold'), border=5, padx=13, pady=8,
                command=lambda: click('*'),
                activebackground='pink', activeforeground='orange')
btnmul.grid(row=3, column=3)

btn0 = Button(screen, text=0, font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8, command=lambda: click(0),
              activebackground='pink', activeforeground='orange')
btn0.grid(row=4, column=0)

btnc = Button(screen, text='c', font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8, command=clear,
              activebackground='pink', activeforeground='orange')
btnc.grid(row=4, column=1)

btnequal = Button(screen, text='=', font=('arial', 20, 'italic bold'), border=5, padx=10, pady=8, command=equal,
                  activebackground='pink', activeforeground='orange')
btnequal.grid(row=4, column=2)

btndiv = Button(screen, text='/', font=('arial', 20, 'italic bold'), border=5, padx=15, pady=8,
                command=lambda: click('/'),
                activebackground='pink', activeforeground='orange')
btndiv.grid(row=4, column=3)

# Advence calculation:

btnsin = Button(screen, text='sin', font=('arial', 20, 'italic bold'), border=4, padx=5, pady=7, command=cmsin,
                activebackground='pink', activeforeground='orange')
btnsin.grid(row=0, column=4)

btncos = Button(screen, text='cos', font=('arial', 20, 'italic bold'), border=4, padx=1, pady=7, command=cmcos,
                activebackground='pink', activeforeground='orange')
btncos.grid(row=1, column=4)

btntan = Button(screen, text='tan', font=('arial', 20, 'italic bold'), border=4, padx=4, pady=7, command=cmtan,
                activebackground='pink', activeforeground='orange')
btntan.grid(row=2, column=4)

btnsqrt = Button(screen, text='sqrt', font=('arial', 20, 'italic bold'), border=4, padx=0, pady=7, command=cmsqrt,
                 activebackground='pink', activeforeground='orange')
btnsqrt.grid(row=3, column=4)

btnlog = Button(screen, text='log', font=('arial', 20, 'italic bold'), border=4, padx=5, pady=7, command=cmlog,
                activebackground='pink', activeforeground='orange')
btnlog.grid(row=4, column=4)

entry1.bind('<Enter>', on_enteryenter)
entry1.bind('<Leave>', on_enteryleave)

#  Binding:

btn7.bind('<Enter>', on_enter7)
btn7.bind('<Leave>', on_leave7)

btn8.bind('<Enter>', on_enter8)
btn8.bind('<Leave>', on_leave8)

btn9.bind('<Enter>', on_enter9)
btn9.bind('<Leave>', on_leave9)

btnadd.bind('<Enter>', on_enteradd)
btnadd.bind('<Leave>', on_leaveadd)

btn4.bind('<Enter>', on_enter4)
btn4.bind('<Leave>', on_leave4)

btn5.bind('<Enter>', on_enter5)
btn5.bind('<Leave>', on_leave5)

btn6.bind('<Enter>', on_enter6)
btn6.bind('<Leave>', on_leave6)

btnSub.bind('<Enter>', on_enterSub)
btnSub.bind('<Leave>', on_leaveSub)

btn1.bind('<Enter>', on_enter1)
btn1.bind('<Leave>', on_leave1)

btn2.bind('<Enter>', on_enter2)
btn2.bind('<Leave>', on_leave2)

btn3.bind('<Enter>', on_enter3)
btn3.bind('<Leave>', on_leave3)

btnmul.bind('<Enter>', on_entermul)
btnmul.bind('<Leave>', on_leavemul)

btn0.bind('<Enter>', on_enter0)
btn0.bind('<Leave>', on_leave0)

btnc.bind('<Enter>', on_enterc)
btnc.bind('<Leave>', on_leavec)

btnequal.bind('<Enter>', on_enterequal)
btnequal.bind('<Leave>', on_leaveequal)

btndiv.bind('<Enter>', on_enterdiv)
btndiv.bind('<Leave>', on_leavediv)

btnsin.bind('<Enter>', on_entersin)
btnsin.bind('<Leave>', on_leavesin)

btncos.bind('<Enter>', on_entercos)
btncos.bind('<Leave>', on_leavecos)

btntan.bind('<Enter>', on_entertan)
btntan.bind('<Leave>', on_leavetan)

btnsqrt.bind('<Enter>', on_entersqrt)
btnsqrt.bind('<Leave>', on_leavesqrt)

btnlog.bind('<Enter>', on_enterlog)
btnlog.bind('<Leave>', on_leavelog)

screen.mainloop()
