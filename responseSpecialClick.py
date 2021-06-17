import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

label = tkinter.Label(win, text="dongkun is a handsome man", bg="red")
#設置焦點
label.focus_set()
label.pack()

#<Shift_L> 左shift
#<Shift_R> 右shift
#<F5>
#<Return> 回車
#<BackSpace> 退格
def func(event):
    print("event.char =", event.char)
    print("event.keycode =", event.keycode)
label.bind("<Shift_L>", func)

win.mainloop()