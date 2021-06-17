import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dongkun")
win.geometry("600x400+200+20")

tree = ttk.Treeview(win)
tree.pack()

#添加一級樹枝
treeF1 = tree.insert("",0,"中國",text="中國CHI",values=("F1"))
treeF2 = tree.insert("",1,"美國",text="美國USA",values=("F2"))
treeF3 = tree.insert("",2,"英國",text="英國ENG",values=("F3"))

#添加二級樹枝
treeF1_1 = tree.insert(treeF1,0,"黑龍江",text="中國黑龍江",values=("F1_1"))
treeF1_2 = tree.insert(treeF1,1,"吉林",text="中國吉林",values=("F1_2"))
treeF1_3 = tree.insert(treeF1,2,"遼寧",text="中國遼寧",values=("F1_3"))

treeF2_1 = tree.insert(treeF2,0,"德州",text="美國德州",values=("F2_1"))
treeF2_2 = tree.insert(treeF2,1,"舊金山",text="美國舊金山",values=("F2_2"))
treeF2_3 = tree.insert(treeF2,2,"底特律",text="美國底特律",values=("F2_3"))

#添加三級樹枝
treeF1_1_1 = tree.insert(treeF1_1,0,"哈爾濱",text="黑龍江哈爾濱",values=("F1_1_1"))
treeF1_1_2 = tree.insert(treeF1_1,1,"五常",text="黑龍江五常",values=("F1_1_2"))


win.mainloop()