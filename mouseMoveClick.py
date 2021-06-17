import tkinter

win = tkinter.Tk()
win.title("dongkun")
win.geometry("400x400+200+20")

#<B1-Motion>左鍵移動
#<B3-Motion>右鍵移動
#<B2-Motion>中鍵移動
label = tkinter.Label(win, text="dongkun is a handsome man")
label.pack()

def func(event):
    print(event.x, event.y)

label.bind("<B1-Motion>", func)

win.mainloop()