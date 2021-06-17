import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

'''
框架控鍵
在螢幕上顯示一個矩形區域作為容器使用
'''

frm = tkinter.Frame(win)
frm.pack()

#Left
frm_1 = tkinter.Frame(frm)
tkinter.Label(frm_1, text="左上", bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm_1, text="左下", bg="blue").pack(side=tkinter.TOP)
frm_1.pack(side=tkinter.LEFT)

#Right
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r, text="右上", bg="red").pack(side=tkinter.TOP)
tkinter.Label(frm_r, text="右下", bg="yellow").pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.RIGHT)

win.mainloop()