import win32com
import win32com.client

def readWordFileToOtherFile(path, toPath):
    mw = win32com.client.Dispatch("Word.Application")
    doc = mw.Documents.Open(path)
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)

    #將word文件保存到另一個文件
    doc.SaveAs(toPath, 2)#2表示為txt文件

    doc.Close()
    mw.Quit()


path = r"E:\code\python\1.doc"
toPath = r"E:\code\python\a.txt"
readWordFileToOtherFile(path, toPath)