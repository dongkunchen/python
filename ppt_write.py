import win32com
import win32com.client

def makePPT(path):
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True

    #增加一個文件
    pptFile = ppt.Presentations.Add()

    #創建頁 參數1為頁數(從1開始) 參數2為類型
    page1 = pptFile.Slides.Add(1,1)
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "dongkun"
    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = "dongkun is a handsome man"

    # 創建頁
    page2 = pptFile.Slides.Add(2, 1)
    t3 = page2.Shapes[0].TextFrame.TextRange
    t3.Text = "dongkun is a very handsome man"
    t4 = page2.Shapes[1].TextFrame.TextRange
    t4.Text = "dongkun is a very cool man"



    #保存
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()


path = r"E:\code\python\c.ppt"
makePPT(path)