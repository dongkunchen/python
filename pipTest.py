'''
Mac:無須安裝
Linux:無須安裝
windows:勾選了pip和Add python.exe to Path

要安裝第三方模塊 需要知道模塊的名字
Pillow 非常強大的處理圖像的工具庫

'''
from PIL import Image
#打開圖片
im = Image.open("111.jpg")
print(im.format,im.size,im.mode)
#設置圖片的大小
#保存成新圖片

