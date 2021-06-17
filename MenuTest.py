import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

#菜單條
menubar = tkinter.Menu(win)
win.config(menu=menubar)

def func():
    print("dongkun is a handsome man")

#創建一個菜單選項
menu1 = tkinter.Menu(menubar, tearoff=False)
#給菜單添加內容
for item in ["Python", "C", "C++", "OC", "Swift", "C#", "shell", "Java", "退出"]:
    if item == "退出":
        menu1.add_separator()#添加分隔線
        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(label=item, command=func)
#向菜單條上添添加內容
menubar.add_cascade(label="語言",menu=menu1)

menu2 = tkinter.Menu(menubar, tearoff=False)
menu2.add_command(label="red")
menu2.add_command(label="blue")
menubar.add_cascade(label="顏色", menu=menu2)


win.mainloop()