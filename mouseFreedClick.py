import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

#<ButtonRelease-1>釋放鼠標左鍵
#<ButtonRelease-3>釋放鼠標右鍵
#<ButtonRelease-2>釋放鼠標中鍵
label = tkinter.Label(win, text="dongkun is a handsome man", bg="red")
label.pack()

def func(event):
    print(event.x, event.y)

label.bind("<ButtonRelease-1>", func)

win.mainloop()