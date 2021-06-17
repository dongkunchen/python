import win32com
import win32com.client
import os

def makeWordFile(fileName):
    word = win32com.client.Dispatch("Word.Application")
    #讓文檔可見
    word.Visible = True
    #創建文檔
    doc = word.Documents.Add()

    #寫內容
    #從頭開始寫
    r = doc.Range(0, 0)
    r.InsertAfter("親愛的" + name + "\n")
    r.InsertAfter("         我想你....\n")

    #存儲文件
    doc.SaveAs(path)
    #關閉文件
    doc.Close()
    #退出word
    word.Quit()


names = ["張三","李四","王五"]
for name in names:
    path = os.path.join(os.getcwd(), name)
    makeWordFile(path)