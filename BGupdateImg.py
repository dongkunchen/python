# win鍵+r --> regedit --> HKEY_CURRENT_USER --> Control panel --> Desktop
# 注意這是惡作劇程式別亂用會改變背景但無害~

import win32api
import win32con
import win32gui


def setWallPaper(path):
    # 打開註冊表
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 2.拉伸 0.居中 6.適應 10.填充
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "6")
    #
    # win32api.RegSetValueEx(reg_key, "WallPaper")
    # SPIF_SENDWININICHANGE立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)


setWallPaper(r"E:\code\python\1.jpg")
