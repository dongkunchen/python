import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

#綁定變量
e = tkinter.Variable()
'''
輸入控件
用於顯示簡單的文本內容
'''

#show密文顯示 show="*"entry = tkinter.Entry(win, show="*")
entry = tkinter.Entry(win, textvariable=e)
entry.pack()
#e就代表輸入框這個對象
#設置值
e.set("dongkun is a handsome man")
#取值
print(e.get())
print(entry.get())
win.mainloop()