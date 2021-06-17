#惡作劇程式請注意執行會改變背景及聲音 
#用於惡搞請勿濫用
#Spoof program, please note that running the program will change the background and automatically play music
#But no harm to the computer
#Don't abuse
import time
import pygame

import win32api
import win32con
import win32gui

#線程模塊
import threading

def go():
    pygame.mixer.init()
    while True:
        for i in range(5):
            filePath = r"E:\code\python" + "\\" + str(i) + ".mp3"
            track = pygame.mixer.music.load(filePath)
            pygame.mixer.music.play()
            time.sleep(10)
            pygame.mixer.music.stop()

def setWallPaper(path):
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(reg_key, "WallpaperStyle",0,win32con.REG_SZ,"6")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)

th = threading.Thread(target=go, name="LoopThread")
th.start()
while True:
    for i in range(9):
        filePath = r"E:\code\python" + "\\" + str(i) + ".jpg"
        setWallPaper(filePath)
        time.sleep(5)
