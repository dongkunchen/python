import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

'''
供用戶通過拖曳指示器改變便量的值,
可以水平 tkinter.HORIZONTAL
也可以垂直 tkinter.VERTICAL(默認沒設就是垂直)
length 水平時表示寬度 垂直時表示高度
tickinterval 選擇值將會該值的倍數
'''
scale = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=100, length=200)
scale.pack()

#設置值
scale.set(20)

#取值
def showNum():
    print(scale.get())
tkinter.Button(win,text="按鈕", command=showNum).pack()

win.mainloop()