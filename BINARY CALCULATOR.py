from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
root=Tk()
root.title("Our 1st Project")
root.geometry('1920x1080')
photo = PhotoImage(file="project 2.png")
lable = Label(image=photo)
lable.pack()
i = PhotoImage(file="100.png")
root.iconphoto(True,i)
m = Label(root, text="WELCOME TO OUR ADVANCED BINARY CALCULATOR", font="vani 27 bold", fg="gold", bg="gray15",relief=GROOVE, padx=20 )
m.place(x=200, y=30)
o = Label(root, text="FOLLOW THIS COMMAND", font="vani 19 bold", fg="black", bg="skyblue", justify=CENTER)
o.place(x=850, y=150)
s=scrolledtext.ScrolledText(root, wrap=WORD, font="Arial 15 bold", width=40, height=15,bg="skyblue")
s.place(x=850, y=200)

s.insert('insert',"~ Press 1 - Decimal Conversion\n\n")
s.insert('insert',"~ Press 2 - Binary Conversion\n\n")
s.insert('insert',"~ Press 3 - Octal Conversion\n\n")
s.insert('insert',"~ Press 4 - Hexadecimal Conversion\n\n")
s.insert('insert',"~ Press 5 - Binary operation(add, sub, mul)\n\n")
s.insert('insert',"~ Press 6 - Binary operation(divide)\n\n")
s.insert('insert',"~ Press 7 - 1's & 2's complement\n\n")
s.insert('insert',"~ Press 8 - Binary Encryption & Decryption \n\n")
s.insert('insert',"~ Press 9 - Bit's Shift Calculation\n\n")
s.insert('insert',"~ Press 10 - BitWise Operator\n\n")
s.config(state=DISABLED)


# variable
a1 = IntVar()
def pr1():

    # # todo num to all
    if a1.get()==1:
        nx=Toplevel()

        nx.title("Decimal Conversion")
        nx.geometry('1920x1080')
        i = PhotoImage(file="100.png")
        nx.iconphoto(True, i)
        nx.configure(bg="skyblue")

        # variable
        num1 = IntVar()
        biin = StringVar()
        occt = StringVar()
        hexaa = StringVar()

        def pr():
            a = (num1.get())
            b = str(bin(a))
            c = str(oct(a))
            d = str(hex(a))
            biin.set(b)
            occt.set(c)
            hexaa.set(d)

        def pk():
            num1.set(0)
            biin.set("")
            occt.set("")
            hexaa.set("")

        def exit():
            if messagebox.askyesno("Exit", 'Do you really want to exit'):
                nx.destroy()

        a= Label(nx, text='DECIMAL CONVERSION', font=("vani 30 bold"), bg='white', fg='black', relief= GROOVE, padx=40, pady=7)
        a.place(x=400, y=20)
        n = Label(nx, text='Enter number = ', font=("times 25 bold"), fg='black', bg="skyblue")
        n.place(x=380, y=200)
        a = Label(nx, text='Binary = ', font=("times 25 bold"), fg='black', bg='skyblue')
        a.place(x=380, y=300)
        a = Label(nx, text='Octal = ', font=("times 25 bold"), fg='black', bg='skyblue')
        a.place(x=380, y=400)
        a = Label(nx, text='Hexadecimal = ', font=("times 25 bold"), fg='black',bg='skyblue')
        a.place(x=380, y=500)
        a = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num1)
        a.place(x=670, y=200)
        b = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=biin)
        b.place(x=670, y=300)
        b = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=occt)
        b.place(x=670, y=400)
        b = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=hexaa)
        b.place(x=670, y=500)
        p = Button(nx, text='Convert', font='times 20 bold', fg='black', bg='white', command=pr)
        p.place(x=650, y=600)

        f = Button(nx, fg="black", bg="white",text="Clear", font="Times 20 bold", command=pk)
        f.place(x=450, y=600)

        g = Button(nx, fg="black", bg="white", text="Exit", font="Times 20 bold", command=exit)
        g.place(x=850, y=600)
        nx.mainloop()

#   todo bin to all
    if a1.get()==2:
        nx=Toplevel()
        nx.title("Binary Conversion")
        nx.geometry('1920x1080')
        nx.configure(bg="skyblue")
        i = PhotoImage(file="100.png")
        nx.iconphoto(True, i)

        binn = StringVar()
        deci = StringVar()
        octa = StringVar()
        hexaa = StringVar()

        def kj():
            # todo bin to decimal
            x = binn.get()
            b = int(x, 2)
            deci.set(b)
            # todo bin to oct
            a = binn.get()
            c = oct(int(a, 2))
            octa.set(c)
            # todo bin to hex
            a1 = binn.get()
            c1 = hex(int(a1, 2))
            hexaa.set(c1)

        def pk():
            binn.set(0)
            deci.set("")
            octa.set("")
            hexaa.set("")

        def exit():
            if messagebox.askyesno("Exit", 'Do you really want to exit'):
                nx.destroy()

        t = Label(nx, text="BINARY CONVERSION", font="vani 30 bold", relief= SUNKEN, padx= 40, pady=7, bg='white')
        t.place(x=400, y=20)

        a = Label(nx, text="Enter your binary = ", font="Times 25 bold", fg='black',bg='skyblue')
        a.place(x=350, y=200)

        b = Label(nx, text="Decimal = ", font="Times 25 bold", fg='black',bg='skyblue')
        b.place(x=380, y=300)

        c = Label(nx, text="Octal = ", font="Times 25 bold", fg='black',bg='skyblue')
        c.place(x=380, y=400)

        d = Label(nx, text="Hexadecimal = ", font="Times 25 bold", fg='black',bg='skyblue')
        d.place(x=380, y=500)

        a = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=binn)
        a.place(x=670, y=200)
        b = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=deci)
        b.place(x=670, y=300)
        b = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=octa)
        b.place(x=670, y=400)
        b = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=hexaa)
        b.place(x=670, y=500)
        p = Button(nx, text='Convert', font='times 20 bold', fg='black', bg='white', command=kj)
        p.place(x=650, y=600)

        f = Button(nx, fg="black", bg="white", text="Clear", font="Times 20 bold", command=pk)
        f.place(x=450, y=600)

        g = Button(nx, fg="black", bg="white", text="Exit", font="Times 20 bold", command=exit)
        g.place(x=850, y=600)

        nx.mainloop()

#    todo octal to all
    if a1.get() == 3:
        nx = Toplevel()
        nx.title("Octal Conversion")
        nx.geometry('1920x1080')
        nx.configure(bg="skyblue")
        i = PhotoImage(file="100.png")
        nx.iconphoto(True, i)
        # variable
        octa = StringVar()
        deci = StringVar()
        bina = StringVar()
        hexaa = StringVar()

        # function
        def hello():
            # todo oct to decimal
            a = octa.get()
            c = int(a, 8)
            str(c)
            deci.set(c)
            # todo oct to bin
            a = octa.get()
            c = bin(int(a, 8))
            bina.set(c)
            # todo oct to hexa
            a = octa.get()
            c = hex(int(a, 8))
            hexaa.set(c)

        def pk():
            octa.set(0)
            deci.set("")
            bina.set("")
            hexaa.set("")

        def exit():
            if messagebox.askyesno("Exit", 'Do you really want to exit'):
                nx.destroy()

        t =Label(nx, text="OCTAL CONVERSION", font="Vani 30 bold", relief= SUNKEN, padx= 40, pady=7,bg='white')
        t.place(x=400, y=20)

        a = Label(nx, text="Enter your octal - ", font="Times 25 bold", fg='black',bg='skyblue')
        a.place(x=380, y=200)

        b = Label(nx, text="Decimal - ", font="Times 25 bold", fg='black',bg='skyblue')
        b.place(x=380, y=300)

        c = Label(nx, text="Binary - ", font="Times 25 bold", fg='black',bg='skyblue')
        c.place(x=380, y=400)

        d = Label(nx, text="Hexadecimal -", font="Times 25 bold", fg='black',bg='skyblue')
        d.place(x=380, y=500)

        a = Entry(nx, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=octa)
        a.place(x=670, y=200)
        b = Entry(nx, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=deci)
        b.place(x=670, y=300)
        b = Entry(nx, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=bina)
        b.place(x=670, y=400)
        b = Entry(nx, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=hexaa)
        b.place(x=670, y=500)

        p = Button(nx, text='Convert', font='times 20 bold', fg='black', bg='white', command=hello)
        p.place(x=650, y=600)

        f = Button(nx, fg="black", bg="white", text="Clear", font="Times 20 bold", command=pk)
        f.place(x=450, y=600)

        g = Button(nx, fg="black", bg="white", text="Exit", font="Times 20 bold", command=exit)
        g.place(x=850, y=600)
        nx.mainloop()

#     todo hexta to all
    if a1.get() == 4:
        nx = Toplevel()
        nx.title("Hexadecimal conversion")
        nx.geometry('1920x1080')
        nx.configure(bg="skyblue")
        i = PhotoImage(file="100.png")
        nx.iconphoto(True, i)
        # photo = PhotoImage(file="100.png")
        # lable = Label(image=photo)
        # lable.pack()
        # variable
        hexaa = StringVar()
        decci = StringVar()
        biin = StringVar()
        occt = StringVar()

        # function
        def pr():
            # todo hex to dec
            a = hexaa.get()
            b = int(int(a, 16))
            decci.set(b)
            # todo hex to bin
            a = hexaa.get()
            b = bin(int(a, 16))
            biin.set(b)

            #    todo hexa to oct
            a = hexaa.get()
            b = oct(int(a, 16))
            occt.set(b)

        def pk():
            hexaa.set(0)
            decci.set("")
            biin.set("")
            occt.set("")

        def exit():
            if messagebox.askyesno("Exit", 'Do you really want to exit'):
                nx.destroy()

        t = Label(nx, text="HEXADECIMAL CONVERSION", font="Vani 30 bold", relief=SUNKEN, padx=40, pady=10,bg='white')
        t.place(x=370, y=20)

        n = Label(nx, text='Enter your Hexadecimal = ', font="Times 25 bold", fg='black',bg='skyblue')
        n.place(x=280, y=200)
        a = Label(nx, text='Decimal = ', font="Times 25 bold", fg='black',bg='skyblue')
        a.place(x=380, y=300)
        a = Label(nx, text='Binary = ', font="Times 25 bold", fg='black',bg='skyblue')
        a.place(x=380, y=400)
        a = Label(nx, text='Octal = ', font="Times 25 bold", fg='black',bg='skyblue')
        a.place(x=380, y=500)

        a = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=hexaa)
        a.place(x=670, y=200)
        b = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=decci)
        b.place(x=670, y=300)
        b = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=biin)
        b.place(x=670, y=400)
        b = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=occt)
        b.place(x=670, y=500)

        p = Button(nx, text='Convert', font='times 20 bold', fg='black', bg='white', command=pr)
        p.place(x=650, y=600)

        f = Button(nx, fg="black", bg="white", text="Clear", font="Times 20 bold", command=pk)
        f.place(x=450, y=600)

        g = Button(nx, fg="black", bg="white", text="Exit", font="Times 20 bold", command=exit)
        g.place(x=850, y=600)

        nx.mainloop()

    # todo binary arthemetic
    if a1.get()==5:
        x=Toplevel()
        x.title("Add, Sub, Mul Operation")
        x.geometry('1920x1080')
        x.configure(bg="skyblue")
        i = PhotoImage(file="100.png")
        x.iconphoto(True, i)
        num1 = IntVar()
        num3=StringVar()
        num2 = IntVar()
        num4=StringVar()
        result = StringVar()
        result1=StringVar()

        # function
        def add():
            # todo add
            b1 = str(num1.get())
            b2 = str(num2.get())
            a1=int(b1,2)
            num3.set(a1)
            a2=int(b2, 2)
            num4.set(a2)
            sum = int(b1, 2) + int(b2, 2)
            result1.set(sum)
            sum1 = str(bin(sum))
            result.set(sum1)

        def sub():
            b1 = str(num1.get())
            b2 = str(num2.get())
            a1 = int(b1, 2)
            num3.set(a1)
            a2 = int(b2, 2)
            num4.set(a2)
            sum = int(b1, 2) - int(b2, 2)
            result1.set(sum)
            sum1 = str(bin(sum))
            result.set(sum1)


        def mul():
            b1 = str(num1.get())
            b2 = str(num2.get())
            a1 = int(b1, 2)
            num3.set(a1)
            a2 = int(b2, 2)
            num4.set(a2)
            sum = int(b1, 2) * int(b2, 2)
            result1.set(sum)
            sum1 = str(bin(sum))
            result.set(sum1)

        # #     todo sub
        #     b1 = str(num1.get())
        #     b2 = str(num2.get())
        #     sum = int(b1, 2) - int(b2, 2)
        #     sum1 = str(bin(sum))
        #     sub.set(sum1)
        #     # todo multiple
        #     b1 = str(num1.get())
        #     b2 = str(num2.get())
        #     sum = int(b1, 2) * int(b2, 2)
        #     sum1 = str(bin(sum))
        #     multi.set(sum1)
        def pk():
            num1.set(0)
            num3.set(0)
            num2.set(0)
            num4.set(0)
            result.set('')
            result1.set('')

        def exit():
            if messagebox.askyesno("Exit", 'Do you really want to exit'):
                x.destroy()

        t=Label(x,text='BINARY OPERATIONS',font="Vani 30 bold",bg='white',fg='black',relief=RIDGE, padx=40, pady=7)
        t.place(x=470, y=10)

        c = Label(x, text="BINARY", font="Vani 22 bold", fg='black',bg='skyblue')
        c.place(x=650, y=150)

        c = Label(x, text="DECIMAL", font="Vani 22 bold", fg='black',bg='skyblue')
        c.place(x=1050, y=150)

        a = Label(x, text="Enter 1st binary number = ", font="Times 25 bold", fg='black',bg='skyblue')
        a.place(x=150, y=250)

        b = Label(x, text="Enter 2nd binary number = ", font="Times 25 bold", fg='black',bg='skyblue')
        b.place(x=150, y=350)

        c = Label(x, text="Result = ", font="Times 25 bold", fg='black',bg='skyblue')
        c.place(x=150, y=450)


        a = Entry(x, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num1)
        a.place(x=550, y=250)
        b = Entry(x, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num2)
        b.place(x=550, y=350)
        b = Entry(x, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=result)
        b.place(x=550, y=450)

        a = Entry(x, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num3)
        a.place(x=950, y=250)
        b = Entry(x, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num4)
        b.place(x=950, y=350)
        b = Entry(x, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=result1)
        b.place(x=950, y=450)

        p = Button(x, text='ADDITION', font='times 20 bold', fg='black', bg='white', command=add)
        p.place(x=200, y=550)
        p = Button(x, text='SUBTRACTION', font='times 20 bold', fg='black', bg='white', command=sub)
        p.place(x=600, y=550)
        p = Button(x, text='MULTIPLICATION', font='times 20 bold', fg='black', bg='white', command=mul)
        p.place(x=1000, y=550)

        f = Button(x, fg="black", bg="white", text="Clear", font="Times 20 bold", command=pk)
        f.place(x=430, y=650)

        g = Button(x, fg="black", bg="white", text="Exit", font="Times 20 bold", command=exit)
        g.place(x=900, y=650)

        x.mainloop()

    if a1.get() == 6:
        k=Toplevel()
        # root.configure(bg='royal blue')
        k.title("Division Operation")
        k.geometry('1920x1080')
        k.configure(bg="skyblue")
        i = PhotoImage(file="100.png")
        k.iconphoto(True, i)
        num1 = StringVar()
        num = StringVar()
        num2 = StringVar()
        num3 = StringVar()
        qui = StringVar()
        qui1 = StringVar()
        rem = StringVar()
        rem1 = StringVar()

        # function
        def pr():
            a = num1.get()
            b = num2.get()
            a1 = int(str(int(a, 2)))
            num.set(a1)
            b1 = int(str(int(b, 2)))
            num3.set(b1)
            c = int(a1 / b1)
            qui1.set(c)
            r = str(bin(c))
            qui.set(r)
            c1 = int(a1 % b1)
            rem1.set(c1)
            r1 = str(bin(c1))
            rem.set(r1)

        def pr1():
            num1.set(0)
            num.set(0)
            num2.set(0)
            num3.set(0)
            qui.set('')
            qui1.set('')
            rem.set('')
            rem1.set('')

        def pr2():
            if messagebox.askyesno("Exit", 'Do you really want to exit'):
                k.destroy()

        t = Label(k, text='DIVISION OPERATION', font="Vani 31 bold", bg='white', fg='black', relief=RIDGE, padx=40, pady=7)
        t.place(x=430, y=10)

        c = Label(k, text="BINARY", font="Vani 22 bold", fg='black',bg='skyblue')
        c.place(x=630, y=150)

        c = Label(k, text="DECIMAL", font="Vani 22 bold", fg='black',bg='skyblue')
        c.place(x=980, y=150)

        n = Label(k, text='Enter 1st binary = ', font=('times new rommon', 20, 'bold'), fg='black',bg='skyblue')
        n.place(x=200, y=250)
        a = Label(k, text='Enter 2nd binary = ', font=('times new rommon', 20, 'bold'), fg='black',bg='skyblue')
        a.place(x=200, y=350)
        a = Label(k, text='Quotient = ', font=('times new rommon', 20, 'bold'), fg='black',bg='skyblue')
        a.place(x=200, y=450)
        a = Label(k, text='Remainder = ', font=('times new rommon', 20, 'bold'), fg='black',bg='skyblue')
        a.place(x=200, y=550)
        a = Entry(k, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num1)
        a.place(x=530, y=250)
        b = Entry(k, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num2)
        b.place(x=530, y=350)
        b = Entry(k, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=qui)
        b.place(x=530, y=450)
        b = Entry(k, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=rem)
        b.place(x=530, y=550)

        a = Entry(k, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num)
        a.place(x=900, y=250)
        b = Entry(k, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num3)
        b.place(x=900, y=350)
        b = Entry(k, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=qui1)
        b.place(x=900, y=450)
        b = Entry(k, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=rem1)
        b.place(x=900, y=550)

        p = Button(k, text='Convert', font='times 20 bold', fg='black', bg='white', command=pr)
        p.place(x=750, y=650)

        p = Button(k, text='Clear', font='times 20 bold', fg='black', bg='white', command=pr1)
        p.place(x=450, y=650)

        p = Button(k, text='Exit', font='times 20 bold', fg='black', bg='white', command=pr2)
        p.place(x=1050, y=650)

        k.mainloop()

    if a1.get()==7:
        kk=Toplevel()
        kk.title("1's & 2's Complement")
        kk.geometry('1920x1080')
        kk.configure(bg="skyblue")
        i = PhotoImage(file="100.png")
        kk.iconphoto(True, i)

        binn = StringVar()
        one = StringVar()
        two = StringVar()
        # function
        def pr():
            a = binn.get()
            b = []
            for i in a:
                if (int(i) == 0):
                    b.append(1)
                elif (int(i) == 1):
                    b.append(0)

            x = ""
            for j in b:
                v = str(j)
                x = x + v
            one.set(x)
            c = "1"
            c1 = str(int(x, 2) + int(c, 2))
            d1= bin(int(c1))
            two.set(d1)

        def pr1():
            binn.set(0)
            one.set('')
            two.set('')

        def pr2():
            if messagebox.askyesno("Exit", 'Do you really want to exit'):
                kk.destroy()

        n = Label(kk, text="1's & 2's COMPLEMENT", font="times 30 bold", fg='black', bg='white', relief=SUNKEN, padx=30)
        n.place(x=430, y=20)
        n = Label(kk, text='Enter your binary = ', font="Times 25 bold", fg='black', bg='skyblue')
        n.place(x=320, y=200)
        a = Label(kk, text="1's complement = ", font="Times 25 bold", fg='black', bg='skyblue')
        a.place(x=360, y=320)
        a = Label(kk, text="2's complement = ", font=('times new rommon', 20, 'bold'), fg='black', bg='skyblue')
        a.place(x=360, y=440)
        a = Entry(kk, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=binn)
        a.place(x=650, y=200)
        b = Entry(kk, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=one)
        b.place(x=650, y=320)
        b = Entry(kk, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=two)
        b.place(x=650, y=440)

        p = Button(kk, text='Convert', font='times 20 bold', fg='black', bg='white', command=pr)
        p.place(x=650, y=600)
        p = Button(kk, text='Clear', font='times 20 bold', fg='black', bg='white', command=pr1)
        p.place(x=400, y=600)
        p = Button(kk, text='Exit', font='times 20 bold', fg='black', bg='white', command=pr2)
        p.place(x=900, y=600)

        kk.mainloop()
    if a1.get() == 8:
        k = Toplevel()
        k.title("Algebra Binary")
        k.geometry('1920x1080')
        k.configure(bg="skyblue")
        i = PhotoImage(file="100.png")
        k.iconphoto(True, i)

        # todo variable
        algebra = StringVar()
        binn = StringVar()
        bn = StringVar()
        rt = StringVar()

        def pr():
            x = algebra.get()
            n = x.upper()
            a = {"A": "1000001", "B": "1000010", "C": "1000011", "D": "1000100", "E": "1000101", "F": "1000110",
                 "G": "1000111", "H": "1001000", "I": "1001001",
                 "J": "1001010", "K": "1001011", "L": "1001100", "M": "1001101", "N": "1001110", "O": "1001111",
                 "P": "1010000", "Q": "1010001", "R": "1010010",
                 "S": "1010011", "T": "1010100", "U": "1010101", "V": "1010110", "W": "1010111", "X": "1011000",
                 "Y": "1011001", "Z": "1011010"}
            x1 = ''
            for i in n:
                for j in a:
                    if i == j:
                        x1 += a[i]
            binn.set(x1)

        def p1():
            n = bn.get()
            n1 = str(n)

            a = {"A": "1000001", "B": "1000010", "C": "1000011", "D": "1000100", "E": "1000101", "F": "1000110",
                 "G": "1000111", "H": "1001000", "I": "1001001",
                 "J": "1001010", "K": "1001011", "L": "1001100", "M": "1001101", "N": "1001110", "O": "1001111",
                 "P": "1010000", "Q": "1010001", "R": "1010010",
                 "S": "1010011", "T": "1010100", "U": "1010101", "V": "1010110", "W": "1010111", "X": "1011000",
                 "Y": "1011001", "Z": "1011010"}
            b = ""
            c = 0
            d = ""
            for i in n1:
                b = b + i
                c += 1
                if c == 7:
                    for j, k in a.items():
                        if b == k:
                            d = d + j
                    c = 0
                    b = ''

            rt.set(d)

        def p2():
            bn.set('')
            rt.set('')

        def pr1():
            algebra.set('')
            binn.set('')

        def pr2():
            if messagebox.askyesno("Exit", 'Do you really want to exit'):
                k.destroy()

        t = Label(k, text='ENCRYPTION & DECRYPTION', font="Vani 31 bold", bg='white', fg='black', relief=RIDGE, padx=40,
                  pady=7)
        t.place(x=360, y=10)

        c = Label(k, text="Encrption", font="Vani 22 bold", fg='black', bg='skyblue')
        c.place(x=320, y=200)

        c = Label(k, text="Binary", font="Vani 22 bold", fg='black', bg='skyblue')
        c.place(x=900, y=200)

        c = Label(k, text="Binary", font="Vani 22 bold", fg='black', bg='skyblue')
        c.place(x=340, y=500)

        c = Label(k, text="Decryption", font="Vani 22 bold", fg='black', bg='skyblue')
        c.place(x=880, y=500)

        a = Entry(k, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=algebra)
        a.place(x=230, y=260)

        b = Entry(k, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=binn)
        b.place(x=800, y=260)

        a = Entry(k, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=bn)
        a.place(x=230, y=550)

        b = Entry(k, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=rt)
        b.place(x=800, y=550)

        p = Button(k, text='Convert', font='times 20 bold', fg='black', bg='white', command=pr)
        p.place(x=710, y=350)

        p = Button(k, text='Convert', font='times 20 bold', fg='black', bg='white', command=p1)
        p.place(x=610, y=630)

        p = Button(k, text='Clear', font='times 20 bold', fg='black', bg='white', command=pr1)
        p.place(x=520, y=350)

        p = Button(k, text='Exit', font='times 20 bold', fg='black', bg='white', command=pr2)
        p.place(x=855, y=630)

        p = Button(k, text='Clear', font='times 20 bold', fg='black', bg='white', command=p2)
        p.place(x=390, y=630)

        k.mainloop()

    if a1.get() == 9:
        x = Toplevel()
        x.title("Bit's Calculation")
        x.geometry('1920x1080')
        x.configure(bg="skyblue")
        i = PhotoImage(file="100.png")
        x.iconphoto(True, i)

        # todo input format
        Int1 = IntVar()
        Int2 = IntVar()
        DEC = StringVar()
        BIN = StringVar()
        OCT = StringVar()
        HEX = StringVar()

        def Ls():
            # todo decimal
            a=Int1.get();b=Int2.get()
            x = (a << b);Bin = bin(x);Oct = oct(x);Hex = hex(x)
            DEC.set(x),BIN.set(Bin),OCT.set(Oct),HEX.set(Hex)

        def Rs():
            # todo decimal
            a=Int1.get();b=Int2.get()
            x = (a >> b);Bin = bin(x);Oct = oct(x);Hex = hex(x)
            DEC.set(x),BIN.set(Bin),OCT.set(Oct),HEX.set(Hex)

        def pk():
            Int1.set(0)
            Int2.set(0)
            DEC.set("")
            BIN.set("")
            OCT.set("")
            HEX.set("")


        def exit():
            if messagebox.askyesno("Exit", 'Do you really want to exit'):
                x.destroy()

        t = Label(x, text="BIT'S CALCULATION", font="Vani 30 bold", bg='white', fg='black', relief=RIDGE, padx=40,pady=7)
        t.place(x=470, y=10)

        c = Label(x, text="DECIMAL", font="Vani 22 bold", fg='black', bg='skyblue')
        c.place(x=500, y=250)

        c = Label(x, text="BINARY", font="Vani 22 bold", fg='black', bg='skyblue')
        c.place(x=500, y=330)

        d = Label(x, text="OCTAL", font="Vani 22 bold", fg='black', bg='skyblue')
        d.place(x=500, y=420)

        E = Label(x, text="HEXA", font="Vani 22 bold", fg='black', bg='skyblue')
        E.place(x=500, y=500)

        a = Label(x, text="Enter 1st number ", font="Times 25 bold", fg='black', bg='skyblue')
        a.place(x=100, y=250)

        b = Label(x, text="Enter 2nd number ", font="Times 25 bold", fg='black', bg='skyblue')
        b.place(x=100, y=450)

        a = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE,textvariable=Int1)
        a.place(x=100, y=300,width=250)

        b = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE,textvariable=Int2)
        b.place(x=100, y=500,width=250)

        b = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE,textvariable=DEC)
        b.place(x=700, y=250)

        b = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE,textvariable=BIN)
        b.place(x=700, y=330)

        b = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE,textvariable=OCT)
        b.place(x=700, y=420)

        b = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE,textvariable=HEX)
        b.place(x=700, y=500)

        p = Button(x, text='LEFT << SHIFT', font='times 20 bold', fg='black', bg='white',command=Ls)
        p.place(x=1100, y=280)

        p = Button(x, text='RIGHT >> SHIFT', font='times 20 bold', fg='black', bg='white',command=Rs)
        p.place(x=1100, y=450)

        p = Button(x, text='CLEAR', font='times 20 bold', fg='black', bg='white', command=pk)
        p.place(x=400, y=600)

        p = Button(x, text='EXIT', font='times 20 bold', fg='black', bg='white', command=exit)
        p.place(x=800, y=600)

        x.mainloop()
    if a1.get() == 10:
        x = Toplevel()
        x.title("BitWise Operator")
        x.geometry('1920x1080')
        x.configure(bg="skyblue")
        i = PhotoImage(file="100.png")
        x.iconphoto(True, i)
        t = Label(x, text="BitWise Operator", font="Vani 30 bold", bg='white', fg='black', relief=RIDGE, padx=40,pady=7)
        t.place(x=470, y=10)

        num1 = IntVar()
        num2 = IntVar()
        num1.set('')
        num2.set('')
        num3 = StringVar()
        num4 = StringVar()
        num5 = StringVar()
        num6 = StringVar()
        num7 = StringVar()
        num8 = StringVar()

        def AND():
            a = num1.get()
            b = num2.get()
            x = str(bin(a))
            y = str(bin(b))

            x = x[2:]
            y = y[2:]
            x1 = ''
            y1 = ''
            l1 = len(x)
            l2 = len(y)

            if l1 > l2:
                while (l1 > l2):
                    y1 += "0"
                    l2 += 1

            elif l1 < l2:
                while (l2 > l1):
                    x1 += "0"
                    l1 += 1
            x1 = x1 + x
            y1 = y1 + y
            z1 = len(y1)
            s1 = 0
            num4.set(x1)
            num5.set(y1)

            SUM = ''

            # for i in range(z1):
            while (z1 > s1):
                if x1[s1] == '1' and y1[s1] == '1':
                    SUM += "1"
                elif x1[s1] == '0' and y1[s1] == '0':
                    SUM += '0'
                    # if x1[s1]=='1' and y1[s1]=='1':
                    #     SUM+="1"
                    # elif x1[s1]=='0' and y1[s1]=='0':
                    #     SUM+='0'
                elif x1[s1] != y1[s1]:
                    SUM += "0"
                s1 += 1

            num6.set(SUM)
            result = int(SUM, 2)
            num3.set(result)
            result1 = oct(result)
            num7.set(result1)
            result2 = hex(result)
            num8.set(result2)

        def OR():
            a = num1.get()
            b = num2.get()
            x = str(bin(a))
            y = str(bin(b))
            x = x[2:]
            y = y[2:]
            x1 = ''
            y1 = ''
            l1 = len(x)
            l2 = len(y)

            if l1 > l2:
                while (l1 > l2):
                    y1 += "0"
                    l2 += 1

            elif l1 < l2:
                while (l2 > l1):
                    x1 += "0"
                    l1 += 1

            x1 = x1 + x
            y1 = y1 + y
            z1 = len(y1)
            s1 = 0
            num4.set(x1)
            num5.set(y1)

            SUM = ''

            while (z1 > s1):
                if x1[s1] == '1' and y1[s1] == '1':
                    SUM += "1"
                elif x1[s1] == '0' and y1[s1] == '0':
                    SUM += '0'
                elif x1[s1] != y1[s1]:
                    SUM += "1"
                s1 += 1
            num6.set(SUM)
            result = int(SUM, 2)
            num3.set(result)
            result1 = oct(result)
            num7.set(result1)
            result2 = hex(result)
            num8.set(result2)

        def XOR():
            a = num1.get()
            b = num2.get()
            x = str(bin(a))
            y = str(bin(b))
            x = x[2:]
            y = y[2:]
            x1 = ''
            y1 = ''
            l1 = len(x)
            l2 = len(y)

            if l1 > l2:
                while (l1 > l2):
                    y1 += "0"
                    l2 += 1

            elif l1 < l2:
                while (l2 > l1):
                    x1 += "0"
                    l1 += 1

            x1 = x1 + x
            y1 = y1 + y
            z1 = len(y1)
            s1 = 0
            num4.set(x1)
            num5.set(y1)

            SUM = ''

            while (z1 > s1):
                if x1[s1] == '1' and y1[s1] == '1':
                    SUM += "0"
                elif x1[s1] == '0' and y1[s1] == '0':
                    SUM += '0'
                elif x1[s1] != y1[s1]:
                    SUM += "1"
                s1 += 1
            num6.set(SUM)
            result = int(SUM, 2)
            num3.set(result)
            result1 = oct(result)
            num7.set(result1)
            result2 = hex(result)
            num8.set(result2)

        def pr1():
            num1.set('')
            num2.set('')
            num3.set('')
            num4.set('')
            num5.set('')
            num6.set('')
            num7.set('')
            num8.set('')

        def pr2():
            if messagebox.askyesno("Exit", 'Do you really want to exit'):
                root.destroy()

        # t = Label(x, text="Bitwise Operators", font="Vani 30 bold", fg="gold", bg="gray15", relief=RIDGE, padx=40,
        #           pady=7)
        # t.place(x=550, y=10)

        c = Label(x, text="Decimal", font="Vani 22 bold", fg='black', bg='skyblue')
        c.place(x=450, y=150)

        c = Label(x, text="Binary", font="Vani 22 bold", fg='black', bg='skyblue')
        c.place(x=840, y=150)

        c = Label(x, text="Octal", font="Vani 22 bold", fg='black', bg='skyblue')
        c.place(x=1150, y=150)

        c = Label(x, text="Hexadecimal", font="Vani 22 bold", fg='black', bg='skyblue')
        c.place(x=1100, y=350)

        n = Label(x, text='Enter 1st number = ', font=('times new rommon', 20, 'bold'), fg='black', bg='skyblue')
        n.place(x=35, y=250)

        a = Label(x, text='Enter 2nd number = ', font=('times new rommon', 20, 'bold'), fg='black', bg='skyblue')
        a.place(x=35, y=350)

        a = Label(x, text='Result = ', font=('times new rommon', 20, 'bold'), fg='black', bg='skyblue')
        a.place(x=35, y=450)

        a = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num1)
        a.place(x=345, y=250)

        b = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num2)
        b.place(x=345, y=350)

        b = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num3)
        b.place(x=345, y=450)

        a = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num4)
        a.place(x=735, y=250)

        b = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num5)
        b.place(x=735, y=350)

        b = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num6)
        b.place(x=735, y=450)

        b = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num7)
        b.place(x=1065, y=250,width=250)
        #
        b = Entry(x, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=num8)
        b.place(x=1065, y=450,width=250)

        p = Button(x, text='AND (&)', font='times 20 bold', fg='green', bg='white', command=AND)
        p.place(x=350, y=550)

        p = Button(x, text='OR (|)', font='times 20 bold', fg='green', bg='white', command=OR)
        p.place(x=750, y=550)

        p = Button(x, text='XOR (^)', font='times 20 bold', fg='green', bg='white', command=XOR)
        p.place(x=1130, y=550)

        p = Button(x, text='Clear', font='times 20 bold', fg='black', bg='white', command=pr1)
        p.place(x=580, y=650)

        p = Button(x, text='Exit', font='times 20 bold', fg='black', bg='white', command=pr2)
        p.place(x=950, y=650)


        x.mainloop()
    else:
        messagebox.showerror("Error", "You Entered Invalid Command Try Again")


def pr2():
    a1.set(0)

def pr3():
    if messagebox.askyesno("Exit", 'Do you really want to exit'):
        root.destroy()


n = Label(root, text='Enter command =  ', font=("vani 19 bold"), fg='black',bg="skyblue")
n.place(x=780, y=580)
a = Entry(root, font='arial 20 bold', fg='black', justify=CENTER, relief=GROOVE,bg="white", textvariable=a1)
a.place(x=1000, y=580)
p = Button(root, text='Enter', font='times 20 bold', fg='white',bg="black",command=pr1)
p.place(x=1000, y=650)
q = Button(root, text='Clear', font='times 20 bold', fg='white',bg="black",command=pr2)
q.place(x=800, y=650)
r= Button(root, fg= "white", text="Exit", font="Times 20 bold",bg= "black", command = pr3)
r.place(x= 1200, y=650)
root.mainloop()