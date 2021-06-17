import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

#<Enter>鼠標光標進入控件時觸發
#<Leave>鼠標光標離開控件時觸發
label = tkinter.Label(win, text="dongkun is a handsome man", bg="red")
label.pack()

def func(event):
    print(event.x, event.y)

label.bind("<Enter>", func)

win.mainloop()