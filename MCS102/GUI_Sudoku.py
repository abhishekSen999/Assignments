# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:49:31 2018

@author: abhishek sen
"""
import Sudoku_solver as sudoku
import tkinter as tkr




class GUI_Sudoku(object):

    def clear_button(self):
        print("cleared")
        
    def __init__(self):
        window= tkr.Tk()
        clear=tkr.Button(window,text="clear",command = self.clear_button)
        clear.pack()
        window.mainloop() 
        
    
    
    
GUI_Sudoku()    
    
        
        
        
        
