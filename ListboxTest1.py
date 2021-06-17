import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

'''
列表框控件,可以包含一個或者多個文本框
作用:在listbox控件的小窗口顯示一個字符串
'''

#1.創建一個listbox,添加幾個元素
lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
lb.pack()

for item in ["good", "nice", "handsome", "very handsome", "very cool"]:
    #按順序添加
    lb.insert(tkinter.END, item)
#在開始添加
lb.insert(tkinter.ACTIVE, "cool")
#將列表當成一個元素添加
#lb.insert(tkinter.END,["great", "very handsome"])
# 刪除 參數1為開始的索引參數2為結束的索引如果沒指定參數二只刪除第一個索引處的內容
# lb.delete(1,3)
# lb.delete(1)

# 選中 參數1為開始的索引參數2為結束的索引如果沒指定參數二只選中第一個索引處的內容
lb.select_set(2,5)
#lb.select_set(2)

#取消
#lb.select_clear(2,4)
#lb.select_clear(3)
#獲取到列表中元素的個數
#print(lb.size())
#從列表中取值
#print(lb.get(2,4))
#print(lb.get(2))

#返回當前的索引項,不適item元素
print(lb.curselection())

#判斷有沒有被選中
print(lb.select_includes(1))
print(lb.select_includes(3))

win.mainloop()