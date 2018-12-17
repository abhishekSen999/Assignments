# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:35:32 2018

@author: abhishek sen
"""
import Sudoku_solver as ss
import tkinter as tk

from tkinter import *
import tkinter
import tkinter.messagebox as msgbox


def sudoku_execution(size,sudoku_entry):
    sudoku=[]
    for i in range(size):
        row=[]
        for j in range(size):
            s=sudoku_entry[i][j].get()
            #checking if entry is integer
            if s!="" and set(s).issubset({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}): 
                n=int(s)
            else:
                n=0
            row.append(n)
            
        sudoku.append(row)
    print 
    ob=ss.Sudoku_solver()    
    recieved=ob.run(size,sudoku)
    #recieved=ob.run(size)
    if recieved[0]==False:
        msgbox.showinfo("Error", "Invalid Input")
        
    else:
        for i in range(size):
            for j in range(size):
                sudoku_entry[i][j].delete(0,'end')
                sudoku_entry[i][j].insert(0,recieved[1][i][j])

    



def take_input(s):
    game =tk.Toplevel()
    game.wm_title("SUDOKU: "+s+"*"+s)
    size=int(s)
    sudoku_entry=[]
    for i in range(size):
        row=[]
        for j in range(size):
            row.append(Entry(game,width=5,borderwidth=4))
            row[j].grid(row=i, column=j)
        
        sudoku_entry.append(row)
        
    Button(game, text='Find',command=lambda: sudoku_execution(size,sudoku_entry)).grid(row=size, column=size-1 )
    mainloop()
    
    
    
def execute():
    s=size.get()
    take_input(s)
  



master =tk.Tk()
master.wm_title("SUDOKU")
size_label=Label(master,text="Size of Side = ")
size_label.grid(row=0, column=0 )
size=Entry(master,width=20)
size.grid(row=0,column=1,columnspan=20)
confirm=Button(master, text = "start" , command= execute )
confirm.grid(row =1, column=1)
mainloop()

    
            

            
            
    
   





