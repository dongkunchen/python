import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dongkun")
win.geometry("600x400+200+20")

#表格
tree = ttk.Treeview(win)
tree.pack()

#定義列
tree["columns"] = ("姓名", "年齡", "身高", "體重")
#設置列,列還不會顯示
tree.column("姓名", width=100)
tree.column("年齡", width=100)
tree.column("身高", width=100)
tree.column("體重", width=100)

#設置表頭 真正會顯示的是text內容
tree.heading("姓名", text="姓名-name")
tree.heading("年齡", text="年齡-age")
tree.heading("身高", text="身高-height")
tree.heading("體重", text="體重-weight")

#添加數據
tree.insert("", 0, text="line1", values=("張三","28","165","70"))
tree.insert("", 1, text="line2", values=("李四","29","166","71"))

win.mainloop()