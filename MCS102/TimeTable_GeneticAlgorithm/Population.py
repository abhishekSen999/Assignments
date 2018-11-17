# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:51:24 2018

@author: abhishek sen
"""

#class population to create a population of dna of predefined size
import DNA 
import CourseInformation as ci
import numpy as np
class Population(object):
    def __init__(self,size,mutation_rate,crossover_rate,elite,absolute_path):
        
        self.finished=False
        self.size=size
        self.mutation_rate=mutation_rate
        self.crossover_rate=crossover_rate
        self.elite=elite#states the number of elite DNA strands which will get passed on to the next generation
        #self.population=np.empty(self.size,dtype=object)
        self.population=np.empty(self.size,dtype=object)
        self.generation=0
        
        crs_info=ci.CourseInformation(absolute_path)#getting course information using CourseInformation class
        for i in range(self.size):
            self.population[i]=DNA.DNA(crs_info.theory_class_wise_partition,crs_info.day_time_slots,crs_info.professors,crs_info.lab_class_wise_partition)
    
    
    def calculate_fitness(self):
        total_fitness=0.0
        for i in range(self.size):
            total_fitness+=self.population[i].calculate_fitness()#adding each of their individual_fitness 
        
        for i in range(self.size):
            self.population[i].fitness=self.population[i].individual_fitness/total_fitness*100
            
            
    def natural_selection(self):
        import random
        check=0
        while True:
            check+=1
            pi = random.randint(0,self.size-1)
            rnd=random.random()*100
            if self.population[pi].fitness>rnd: return pi
            if check>1000: break
        return -1
    """     
    def elitism(self,new_population):
        #as sorting on basis of fitness is n*logn complexity at best,
        #we would preffer selecting 'elite' times  best DNA which is elite*n complexity
        #as elite<<n hence this is better than n*logn
        last_elite=-1
        new_population_index=0
        for i in range(int(self.elite)):
            max_fitness_index=-1
            #finding the index to start searching from 
            if last_elite == -1:
                max_fitness_index=0
            else:
                for j in range(self.size):
                    if self.population[j].fitness<self.population[last_elite].fitness:
                        max_fitness_index=j
                        break
            
            for j in range(self.size):
                if self.population[j].fitness<self.population[last_elite].fitness and self.population[j].fitness>self.population[max_fitness_index].fitness:
                    max_fitness_index=j
            
            
            new_population[i]=self.population[max_fitness_index]
            
            last_elite=max_fitness_index
    
    """


    def elitism(self,new_population):
        #elite=3
        #population=np.array([1,4,7,4,9,5,4,3,5,3])
        #new_population=np.empty(len(population),dtype=np.int64)
        
        last_elite=-1
        
        
        new_population_index=0
        for i in range(int(self.elite)):
            #print("last_elite",last_elite)
            index_max_fitness=-1
            if last_elite==-1:
                index_max_fitness=0
            else:
                for j in range (len(self.population)):
                    if self.population[j].fitness<=self.population[last_elite].fitness and j!= last_elite:
                        index_max_fitness=j
                        
            for j in range (len(self.population)):
                if last_elite==-1:
                    if self.population[j].fitness>self.population[index_max_fitness].fitness:
                        index_max_fitness=j
                else:
                    if self.population[j].fitness>self.population[index_max_fitness].fitness and self.population[j].fitness<=self.population[last_elite].fitness and j!= last_elite:
                        index_max_fitness=j
            
            new_population[new_population_index]=self.population[index_max_fitness]
            new_population_index+=1
            last_elite=index_max_fitness
            

        
    def generate(self):
        
        #creating new population using elitism, crossover and mutation
        new_population=np.empty(self.size,dtype=object)
        self.elitism(new_population)
        for i in range (int(self.elite),int(self.size)):
            p1,p2=0,0
            while True:
                p1=self.natural_selection()
                p2=self.natural_selection()
                if p1!=-1 and p2!=-1 and p1!=p2: break
            
            parent1=self.population[p1]
            parent2=self.population[p2]
            child=parent1.crossover(parent2,self.crossover_rate)
            child.mutation(self.mutation_rate)
            new_population[i]=child
            
        #replacing present polulation with new polulation
        for i in range(self.size):
            self.population[i]=new_population[i]
            
        self.generation+=1
    
    
    def check_completion(self):#returns the best child
        
        index_best_dna=0
        for i in range(1,self.size):
            index_best_dna= i if self.population[i].fitness>self.population[index_best_dna].fitness else index_best_dna
        
        if self.population[index_best_dna].individual_fitness==1:
            
            self.finished=True
            return self.population[index_best_dna]
        else:
            self.finished=False
            return self.population[index_best_dna]
                
                
    def get_finished(self):
        return self.finished
    def get_generation(self):
        return self.generation
        
    
    
  