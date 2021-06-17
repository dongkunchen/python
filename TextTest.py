import tkinter


win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

'''
文本控件,用於顯示多行文本
'''
#創建滾動條
scroll = tkinter.Scrollbar()

#創建文本框
text = tkinter.Text(win, width=30, height=4)
#side滾動條放那一側 fill填充
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)
#關聯
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str = "dongkun is a handsome dongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsomedongkun is a handsome"

#插入文件
text.insert(tkinter.INSERT, str)


win.mainloop()