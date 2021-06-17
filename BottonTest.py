import tkinter

def func():
    print("dongkun is a handsome man")

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

#創建按鈕
#command點擊事件
button1 = tkinter.Button(win, text="按鈕", command=func, width=10, height=10)
button1.pack()

button2 = tkinter.Button(win, text="按鈕", command=win.quit)
button2.pack()

win.mainloop()