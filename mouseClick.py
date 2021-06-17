import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

def func(event):
    print(event.x, event.y)

#<Button-1>鼠標左鍵
#<Button-3>鼠標右鍵
#<Button-2>鼠標中鍵
#<Double-Button-1>鼠標左鍵雙擊
#<Double-Button-3>鼠標右鍵雙擊
#<Double-Button-2>鼠標中鍵雙擊
#<Triple-Button-1>鼠標左鍵三擊

button1 = tkinter.Button(win, text="leftmouse button")
#bind 給控件綁定事件
button1.bind("<Button-1>", func)
button1.pack()

win.mainloop()