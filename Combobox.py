import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

'''
下拉框
'''
cv = tkinter.StringVar()
com = ttk.Combobox(win, textvariable=cv)
com.pack()
#設置下拉數據
com["value"] = ("黑龍江", "吉林", "遼寧")

#設置默認值
com.current(0)

#綁定事件
def func(event):
    print(com.get())
    print(cv.get())

com.bind("<<ComboboxSelected>>", func)


win.mainloop()