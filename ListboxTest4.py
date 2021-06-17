import tkinter

win = tkinter.Tk()
win.title("dongkun")
#win.geometry("400x400+200+20")


#MULTIPLE 支持多選
lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)
lb.pack()

for item in ["good", "nice", "handsome", "very handsome", "very cool","good", "nice", "handsome", "very handsome", "very cool", "very cool","good", "nice", "handsome", "very handsome", "very cool", "very cool","good", "nice", "handsome", "very handsome", "very cool", "very cool","good", "nice", "handsome", "very handsome", "very cool"]:
    lb.insert(tkinter.END, item)
#按住shift可以實現連選
#按住ctrl可以實現多選
#滾動條
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
#額外給屬性賦值
sc['command'] = lb.yview()

win.mainloop()