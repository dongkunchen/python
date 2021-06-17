import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

'''
多選框

'''
def update():
    message = ""
    if hobby1.get() == True:
        message += "money\n"
    if hobby2.get() == True:
        message += "power\n"
    if hobby3.get() == True:
        message += "people\n"
    #清除text所有內容
    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT, message)




hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()
hobby3 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win, text="money", variable=hobby1, command=update)
check1.pack()
check2 = tkinter.Checkbutton(win, text="power", variable=hobby2, command=update)
check2.pack()
check3 = tkinter.Checkbutton(win, text="people", variable=hobby3, command=update)
check3.pack()

text = tkinter.Text(win,width=50, height=5)
text.pack()

win.mainloop()