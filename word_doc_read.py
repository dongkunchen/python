import win32com
import win32com.client

def readWordFile(path):
    #調用系統word功能,可以處裡doc docx兩種文件
    mw = win32com.client.Dispatch("Word.Application")
    #打開文件
    doc = mw.Documents.Open(path)
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)
    #關閉文件
    doc.Close()
    #退出word
    mw.Quit()


path = r"E:\code\python\1.doc"
readWordFile(path)