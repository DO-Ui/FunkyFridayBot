from mss import mss
import pyautogui
from multiprocessing import Pool
from multiprocessing import get_context
import time

current = [1,2,3,4]

def watch(current):
    if current == 1:
        scan1 = mss()
        time.sleep(current/4)
        print("First point activated")
        while True:
            sct_img = scan1.grab({'top': 1203, 'left':1160, 'width': 1, 'height':1})
            img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
            point = img.getpixel((0,0))
            if point[0] == 194:
                pyautogui.press('left')
    elif current == 2:
        scan2 = mss()
        time.sleep(current/4)
        print("Second point activated")
        while True:
            sct_img = scan2.grab({'top': 1203, 'left':1300, 'width': 1, 'height':1})
            img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
            point = img.getpixel((0,0))
            if point[1] == 255:
                pyautogui.press('down')
    elif current == 3:
        scan3 = mss()
        time.sleep(current/4)
        print("Third point activated")
        while True:
            sct_img = scan3.grab({'top': 1203, 'left':1440, 'width': 1, 'height':1})
            img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
            point = img.getpixel((0,0))            

            if point[1] == 250:
                pyautogui.press('up')
    elif current == 4:
        scan4 = mss()
        time.sleep(current/4)
        print("Last point activated")
        while True:
            sct_img = scan4.grab({'top': 1203, 'left':1590, 'width': 1, 'height':1})
            img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
            point = img.getpixel((0,0))
            if point[0] == 249:
                pyautogui.press('right')
                

if __name__ == '__main__':
    with get_context("spawn").Pool(4) as p:
        p.map(watch, current)

