# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:53:13 2018

@author: abhishek sen
"""
import numpy as np
import Population 
class SetupEvolution(object):
    
    def __init__(self,mutation_rate=0.001):
        mutation_rate=0.001
        
        
    def generate(self,absolute_path):
        mutation_rate=0.001
        population_size=100
        crossover_rate=0.9
        elite=population_size*5/100
        final_timetable=self.draw(population_size,mutation_rate,crossover_rate,elite,absolute_path)
        return final_timetable
    
    def draw(self,population_size,mutation_rate,crossover_rate,elite,absolute_path):
        p=Population.Population(population_size,mutation_rate,crossover_rate,elite,absolute_path)
        p.calculate_fitness()
        final_timetable= None 
        while True:
            p.generate()
            p.calculate_fitness()
            final_timetable=p.check_completion()
            print("generation: ",p.get_generation(),"student collisions: ",final_timetable.student_collisions,"prfessor collisions: ",final_timetable.professor_collisions,"overall fitness in that generation",final_timetable.fitness)
            if (p.get_finished()): break
        
        print("total number of generations: ",p.get_generation())
        return final_timetable
            
    