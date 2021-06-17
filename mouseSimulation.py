import win32con
import win32api
import time

#設置鼠標的位置
win32api.SetCursorPos([30,40])
time.sleep(0.1)

#鼠標左鍵按下
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
#鼠標左鍵抬起
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)