import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

#菜單條
menubar = tkinter.Menu(win)

#菜單
menu = tkinter.Menu(menubar, tearoff=False)
for item in ["Python", "C", "C++", "OC", "Swift", "C#", "shell", "Java", "退出"]:
        menu.add_command(label=item)

menubar.add_cascade(label="語言", menu=menu)

def showMenu(event):
    menubar.post(event.x_root, event.y_root)
#<Button-3>代表鼠標右鍵
win.bind("<Button-3>", showMenu)

win.mainloop()