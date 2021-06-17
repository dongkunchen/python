import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

def update():
    print(r.get())

#一組單選框綁定同一變量才能有單選效果
#r = tkinter.StringVar() 看value類型選擇
r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win, text="one", value=1, variable=r, command=update)
radio1.pack()
radio2 = tkinter.Radiobutton(win, text="two", value=2, variable=r, command=update)
radio2.pack()
radio3 = tkinter.Radiobutton(win, text="three", value=3, variable=r, command=update)
radio3.pack()

win.mainloop()