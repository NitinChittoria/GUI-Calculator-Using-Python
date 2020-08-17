from tkinter import *
def click(event):
    global equation
    text=event.widget.cget("text")

    # print(text)
    if text=="=":
        if equation.get().isdigit():
            value=int(equation.get())
        else:
            try:
                value=eval(userentry.get())
            except Exception as e:
                print(e)
                equation.set("Error")
                userentry.update()

        equation.set(value)
        userentry.update()

    elif text=="C":
        equation.set("")
        userentry.update()
    elif text=="Del":
        x = userentry.get()
        userentry.delete(0, 'end')
        y = x[:-1]
        userentry.insert(0, y)

    else:
        equation.set(equation.get()+str(text))
        userentry.update()


root=Tk()
root.geometry("545x450")
root.resizable(0,0)
root.title("Calculator")
root.wm_iconbitmap("calc.ico")

equation=StringVar()
equation.set("")
userentry=Entry(root,textvariable=equation,font="Arial 28 bold",justify=RIGHT)
userentry.pack(fill=X,ipadx=5,padx=10,pady=5)


f=Frame(root,bg="white",borderwidth=2,relief=SUNKEN)
b=Button(f,text=7,bg="light grey",fg="black",font="comicsansms 35 bold",padx=7,pady=0,justify=LEFT)
b.pack(side=LEFT,padx=1,pady=2,anchor="w",fill=X)
b.bind("<Button-1>",click)

b=Button(f,text=8,bg="light grey",fg="black",font="comicsansms 35 bold",padx=7,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text=9,bg="light grey",fg="black",font="comicsansms 35 bold",padx=7,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="(",bg="light grey",fg="black",font="comicsansms 35 bold",padx=8,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text=")",bg="light grey",fg="black",font="comicsansms 35 bold",padx=8,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="Del",bg="light grey",fg="black",font="comicsansms 35",padx=9,pady=1,width=6)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="white",borderwidth=2,relief=SUNKEN)
b=Button(f,text=4,bg="light grey",fg="black",font="comicsansms 35 bold",padx=8,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text=5,bg="light grey",fg="black",font="comicsansms 35 bold",padx=7,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text=6,bg="light grey",fg="black",font="comicsansms 35 bold",padx=6,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="*",bg="light grey",fg="black",font="comicsansms 35 bold",padx=7,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="/",bg="light grey",fg="black",font="comicsansms 35 bold",padx=10,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="%",bg="light grey",fg="black",font="comicsansms 35 bold",padx=6,pady=0,width=6)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="white",borderwidth=2,relief=SUNKEN)
b=Button(f,text=1,bg="light grey",fg="black",font="comicsansms 35 bold",padx=8,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text=2,bg="light grey",fg="black",font="comicsansms 35 bold",padx=7,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text=3,bg="light grey",fg="black",font="comicsansms 35 bold",padx=6,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="-",bg="light grey",fg="black",font="comicsansms 37 bold",padx=8,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="+",bg="light grey",fg="black",font="comicsansms 32 bold",padx=7,pady=0)
b.pack(side=LEFT,padx=1,pady=2,fill=Y)
b.bind("<Button-1>",click)


b=Button(f,text="C",bg="light grey",fg="black",font="comicsansms 35 bold",padx=7,pady=0,width=8)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="white",borderwidth=2,relief=SUNKEN)
b=Button(f,text=0,bg="light grey",fg="black",font="comicsansms 40 bold",padx=46,pady=0)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text=".",bg="light grey",fg="black",font="comicsansms 35 bold",padx=13,pady=0)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)

b=Button(f,text="=",fg="white",bg="black",font="comicsansms 35 bold",padx=45,pady=0,width=8)
b.pack(side=LEFT,padx=1,pady=2)
b.bind("<Button-1>",click)
f.pack()




root.mainloop()
