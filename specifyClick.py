import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

def func(event):
    print("event.char =", event.char)
    print("event.keycode =", event.keycode)
win.bind("a", func)
#匹配按鍵觸發事件

win.mainloop()