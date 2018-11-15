# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 16:31:45 2018

@author: abhishek sen
"""




import SetupEvolution as se
import DNA
import GUI
ob=se.SetupEvolution(0.1)
#absolute_path=input("enter the absolute path : ")
absolute_path='E:/Assignments/MCS102/TimeTable_GeneticAlgorithm/COURSE_DATA.csv'
dna1=ob.generate(absolute_path)
dna1.calculate_fitness1()

for i in dna1.theory_day_time_allotment:
    print (i)
    
GUI.GUI(dna1.student_timetable)
    
