# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 07:57:01 2018

@author: abhishek sen
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk
class GUI(object):
    def __init__(self,student_timetable):
        self.create_table("test",student_timetable)
        
    def create_table(self,name,table):
        day_slots=tuple(["MONDAY"," TUESDAY"," WEDNESDAY"," THURSDAY"," FRIDAY"," SATURDAY"])
        time_slots=tuple(["9:00-10:00","10:00-11:00","11:00-12:00","12:00-1:00","1:00-2:00","2:00-3:00","3:00-4:00","4:00-5:00"])    
        course=["MCA-1st sem","MCA-3rd sem","MCS-1st sem","MCS-2nd sem"]
        root = Tk()
        style=ttk.Style(root)
        style.theme_use("clam")
        style.configure("Treeview", background="blue", fieldbackground="blue", foreground="white")
        root.geometry("1500x1000")
        
        #picking up each day* time  timetable(2d) from the 3d timetable(time table of all the classes)
        for class_index in range(len(table)):
            
            data = table[class_index]
            
            w = tk.Label(root, text=course[class_index])
            w.pack()
            frame = Frame(root)
            frame.pack()
            tree = ttk.Treeview(frame, columns =tuple(range(len(time_slots)+1)), height = len(data), show = "headings")
            tree.pack(side = 'left')
            
            tree.heading(0,text="day\\time")
            for i in range(1,len(time_slots)+1):
                
                tree.heading(i,text=time_slots[i-1])
            
            
            
            for i in range(len(time_slots)+1):
                tree.column(i,width=150,anchor=tk.CENTER)
            
            scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            scroll.pack(side = 'right', fill = 'y')
            
            tree.configure(yscrollcommand=scroll.set)
            
            
            k=0;
            for val in data:
                row=tuple(val)
                row=(day_slots[k],)+row
                k=k+1
                
                tree.tag_configure('oddrow', background='khaki',foreground='black')
                tree.tag_configure('evenrow', background='white',foreground='black')
                if (k%2==0):
                    tree.insert('', 'end', values = row ,tags = ('evenrow',))
                else:
                    tree.insert('', 'end', values = row ,tags = ('oddrow',))
            
        root.mainloop()
