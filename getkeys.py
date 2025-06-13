# -*- coding: utf-8 -*-
"""
Created on Sat May 28 15:29:43 2022

@author: jusla
"""

# getkeys.py
# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi


keyList = ["\b"]
for char in "%'(&":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

# old code "ABCDEFGHIJKLMNOPQRSTUVWXYZ 684444444444444123456789,.'APS$/\\<>?[]+=-_;:`~!@#%^&*()|{}"