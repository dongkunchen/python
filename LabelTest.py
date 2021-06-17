import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

'''
Label:標籤控件可以顯示文本
'''

#win 父窗體
#text 顯示文本內容
#bg 背景色
#fg 字體顏色
#anchor n s e w center se
label = tkinter.Label(win,
                      text="dongkun is a handsome man",
                      bg="blue",
                      fg="red",
                      font=("黑體", 20),
                      width=10,
                      height=4,
                      wraplength=100,
                      justify="left",
                      anchor="n"
                      )

#顯示出來
label.pack()

win.mainloop()