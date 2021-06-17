import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

#綁定變量
lbv = tkinter.StringVar()
#與BORWSE相似,但不支持鼠標移動 按下之後移動選中的位置  要設置listvariable=lbv才能取值
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE,listvariable=lbv)
lb.pack()

for item in ["good", "nice", "handsome", "very handsome", "very cool"]:
    lb.insert(tkinter.END, item)

#打印當前列表中的選項
print(lbv.get())
#設置選項 因取出元組所以設置也要元組
#lbv.set(("1", "2", "3"))

#綁定事件
def myPrint(event):
    print(lb.get(lb.curselection()))
lb.bind("<Double-Button-1>", myPrint)


win.mainloop()