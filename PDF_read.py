import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def readPDF(path, toPath):
    #以二進制形式打開pdf文件
    f = open(path, "rb")
    #創建一個pdf文黨分析器
    parser = PDFParser(f)
    #創建pdf文檔
    pdfFile = PDFDocument()
    #鏈接分析器語文檔對象
    parser.set_document(pdfFile)
    pdfFile.set_parser(parser)
    #提供初始化密碼
    pdfFile.initialize()
    #檢測文檔是否提供txt轉換
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #解析數據
        #數據管理器
        manager = PDFResourceManager()
        #創建一個PDF設備對象
        laparams = LAParams()
        device = PDFPageAggregator(manager, laparams=laparams)
        #解釋器對象
        interpreter = PDFPageInterpreter(manager, device)

        #開始循環處理,每次處理一頁
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            #
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(toPath, "a") as f:
                        str = x.get_text()
                        #print(str)
                        f.write(str+"\n")

path = r"E:\code\python\000003.pdf"
toPath = r"E:\code\python\000004.txt"
readPDF(path, toPath)