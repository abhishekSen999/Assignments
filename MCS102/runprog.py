# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 16:31:45 2018

@author: abhishek sen
"""




import SetupEvolution as se
import DNA
ob=se.SetupEvolution(0.1)
absolute_path=input("enter the absolute path : ")
dna1=ob.generate(absolute_path)
dna1.calculate_fitness1()