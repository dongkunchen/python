import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

'''
數值範圍控件
'''
def update():
    print(v.get())


#綁定變量
v = tkinter.StringVar()
#increment 步長 默認為1
#values 最好步要與from_=0, to=100, increment=1同時使用
#command只要值改變就會執行對應方法
sp = tkinter.Spinbox(win, from_=0, to=100, increment=1, textvariable=v, command=update)
#sp = tkinter.Spinbox(win, values=(0,2,4,6,8))
sp.pack()

#賦值
v.set(20)
#取值
print(v.get())




win.mainloop()