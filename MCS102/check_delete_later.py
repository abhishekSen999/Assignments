# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 00:32:43 2018

@author: abhishek sen
"""

import tkinter
#import tkMessageBox

top = tkinter.Tk()

def helloCallBack():
   #tkMessageBox.showinfo( "Hello Python", "Hello World")
   print("fucked")
B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
