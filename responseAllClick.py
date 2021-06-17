import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")


# #<Key>響應所有的按鍵
# label = tkinter.Label(win, text="dongkun is a handsome man", bg="red")
# #設置焦點
# label.focus_set()
# label.pack()
#
# def func(event):
#     print("event.char =", event.char)
#     print("event.keycode =", event.keycode)
# label.bind("<Key>", func)

def func(event):
    print("event.char =", event.char)
    print("event.keycode =", event.keycode)
win.bind("<Key>", func)

win.mainloop()
