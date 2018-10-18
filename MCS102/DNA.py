class DNA(object):
    
    #self.day_time_allotment
    
    def __init__(self,theory_class_wise_partition,day_time_slots,professors,lab_class_wise_partition):
        import numpy as np
        import random
        """
        list of instance variables:
            theory_day_time_allotment: stores alloted day and time for a particular theory class in theory_class_wise_partition
            lab_day_time_allotment: stores alloted day and time for a particular lab class in lab_class_wise_partition
        """
        self.collisions=0
        self.theory_class_wise_partition=theory_class_wise_partition
        self.lab_class_wise_partition=lab_class_wise_partition
        self.day_time_slots=np.copy(day_time_slots)
        self.professors=np.copy(professors)
        self.fitness=0.0
        
        self.theory_day_time_allotment=np.empty(np.shape(theory_class_wise_partition),dtype=object)
        for i in range(np.shape(self.theory_day_time_allotment)[0]): 
            self.theory_day_time_allotment[i]=np.empty(np.shape(theory_class_wise_partition[i]),dtype=object)
        
        self.lab_day_time_allotment=np.empty(np.shape(lab_class_wise_partition),dtype=object)
        for i in range(np.shape(self.lab_day_time_allotment)[0]):
            self.lab_day_time_allotment[i]=np.empty(np.shape(lab_class_wise_partition[i]),dtype=object)
        
        
        #last_time_slot=7
        #filling up the theory_day_time_allotment  array with random permuted slots 
        for i in range(len(self.theory_day_time_allotment)):
            
            perm_slots=np.copy(day_time_slots)
            #alloting labs and deleting those slots from perm_Slots
            for j in range(len(self.lab_day_time_allotment[i])):
                    
                    index=0
                    while True:
                        index=random.randint(0,len(perm_slots)-2)
                        
                         #checking if two concecutive slots are on the same day that is it is not the last available slot of the day
                        if  int(perm_slots[index][0])==int(perm_slots[index+1][0]):
                            break
                    #alloting the selected slot
                    lab_class1of2=perm_slots[index]
                    lab_class2of2=perm_slots[index+1]
                    self.lab_day_time_allotment[i][j]=str(lab_class1of2+":"+lab_class2of2)
                   # deleting the alloted slots from perm_slots being dont to avoid collisions on student's end
                    perm_slots=np.delete(perm_slots,[index,index+1])
            
            #alloting theory classes from the remaining slots
            perm_slots=np.random.permutation(perm_slots)
            index_perm=0
            for j in range(len(self.theory_day_time_allotment[i])):
                self.theory_day_time_allotment[i][j]=perm_slots[index_perm]
                index_perm+=1
        
        #for i in self.lab_day_time_allotment:
         #   print (i)
    def calculate_fitness(self):
        import numpy as np
        import random
        course_professor_map={
            'MCA-101':'NK',
            'MCA-102':'SV',
            'MCA-103':'PR',
            'MCA-104':'NS',
            'MCA-105':'DK',
            'MCA-106':'SP',
            'MCA-301':'RK',
            'MCA-302':'RC',
            'MCA-303':'NS',
            'MCA-304':'MK',
            'MCA-305':'PKH',
            'MCS-101':'NG',
            'MCS-102':'PB',
            'MCS-103':'RG',
            'MCS-104':'RK',
            'MCS-105':'NK',
            'MCS-302':'RC',
            'MCS-303':'PB',
            'MCS-304':'MS',
            'MCS-311':'VB',
            'MCS-312':'NG',
            'MCS-326':'SK'

            }
        #making map dictionary for swift hashing
        professor_index_map={}
        for i,j in zip(self.professors,range(len(self.professors))):
            professor_index_map[i]=j
        
        
        
        days=6
        
        #professor_time_table of structure(professor_index,day,time)
        professor_timetable=np.zeros((len(self.professors),days,int(len(self.day_time_slots)/days)))
        
        #filling uup professor_time_table with theory classes, stores the number of classes in each slot
        for i in range(len(self.theory_day_time_allotment)):
            for j in range(len(self.theory_day_time_allotment[i])):
                #calculating indexes for professor_timetable
                professor_index=professor_index_map[course_professor_map[self.theory_class_wise_partition[i][j]]]
                day_index=int(self.theory_day_time_allotment[i][j][0])
                time_index=int(self.theory_day_time_allotment[i][j][2])
                professor_timetable[professor_index][day_index][time_index]+=1
        
        
        #filling up professor_time_table with lab classes, stores the number of classes in each slot
        for i in range(len(self.lab_day_time_allotment)):
            for j in range(len(self.lab_day_time_allotment[i])):
                #calculating indexes for professor_timetable
                professor_index=professor_index_map[course_professor_map[self.lab_class_wise_partition[i][j]]]
                day_index=int(self.lab_day_time_allotment[i][j][0])
                #two time indexes as each class takes 2 consecutive slots
                time_index1=int(self.lab_day_time_allotment[i][j][2])
                time_index2=int(self.lab_day_time_allotment[i][j][6])
                professor_timetable[professor_index][day_index][time_index1]+=1
                professor_timetable[professor_index][day_index][time_index2]+=1
                
                
        
        
        
        course_map={
                'MCA-1':0,
                'MCA-3':1,
                'MCS-1':2,
                'MCS-3':3
            }
        
        collisions=0
        for i in range(len(professor_timetable)):
            for j in range(len(professor_timetable[i])):
                for k in range(len(professor_timetable[i][j])):
                    if professor_timetable[i][j][k]>1:
                        collisions+=professor_timetable[i][j][k]-1
        
        self.fitness=1/(collisions+1)
                  
        
        
        """
        #preparing student time table
        student_timetable=np.zeros((len(theory_day_time_allotment),days,int(len(self.day_time_slots)/days)),dtype="S15")
        
        
        for i in range(len(self.theory_day_time_allotment)):
            for j in range(len(self.theory_day_time_allotment[i])):
                #calculating indexes for student_timetable
                dash=self.day_time_allotment[i][j].find('-')
                student_index=course_map[str(theory_class_wise_partition[i][j][0:5])]
                day_index=int(self.day_time_allotment[i][j][0:dash])
                time_index=int(self.day_time_allotment[i][j][dash+1:])
                
                student_timetable[student_index][day_index][time_index]=theory_class_wise_partition[i][j]+course_professor_map[theory_class_wise_partition[i][j]]
        
      
        for i in student_timetable:
            print (i,"\n")
           
        
        print(collisions)
        
        for i in professor_timetable:
            print (i,"\n")
        """
    
    
        return self.fitness  
    
    
    #crossover function
    """
    
    """
    def crossover(self,dna1,crossover_rate):
        import numpy as np
        import random
        
        offspring1=DNA(self.theory_class_wise_partition,self.day_time_slots,self.professors,self.lab_class_wise_partition)
        offspring2=DNA(self.theory_class_wise_partition,self.day_time_slots,self.professors,self.lab_class_wise_partition)
        probability=crossover_rate
        
        #crossover of theory_day_time_allotment
        for i in range(len(self.theory_day_time_allotment)):
            if random.random()>crossover_rate: continue
            crossover_point=random.randint(0, len(self.theory_day_time_allotment[i])-1) 
            for j in range(0,crossover_point):
                offspring1.theory_day_time_allotment[i][j]=self.theory_day_time_allotment[i][j]
                offspring2.theory_day_time_allotment[i][j]=dna1.theory_day_time_allotment[i][j]
                
            for j in range(crossover_point,len(self.theory_day_time_allotment[i])):
                offspring1.theory_day_time_allotment[i][j]=dna1.theory_day_time_allotment[i][j]
                offspring2.theory_day_time_allotment[i][j]=self.theory_day_time_allotment[i][j]
        
        #crossover of lab_day_time_allotment
        for i in range(len(self.lab_day_time_allotment)):
            if random.random()>crossover_rate: continue
            crossover_point=random.randint(0, len(self.lab_day_time_allotment[i])-1) 
            for j in range(0,crossover_point):
                offspring1.lab_day_time_allotment[i][j]=self.lab_day_time_allotment[i][j]
                offspring2.lab_day_time_allotment[i][j]=dna1.lab_day_time_allotment[i][j]
                
            for j in range(crossover_point,len(self.lab_day_time_allotment[i])):
                offspring1.lab_day_time_allotment[i][j]=dna1.lab_day_time_allotment[i][j]
                offspring2.lab_day_time_allotment[i][j]=self.lab_day_time_allotment[i][j]

                
        fitness_offspring1=offspring1.calculate_fitness()
        fitness_offspring2=offspring2.calculate_fitness()
        
        print(fitness_offspring1,fitness_offspring2)
        bestOffspring=offspring1 if fitness_offspring1 > fitness_offspring2 else offspring2
       
        return bestOffspring
    
    def mutation(self,mutation_rate):
        import numpy as np
        import random
        #could have been lab_day_time allotment as well
        for i in range(len(self.theory_day_time_allotment)):
            if(random.random()<mutation_rate):
                
                
                #mutating theory_day_time_allotment
                perm_slots=np.copy(self.day_time_slots)
                #finding  the slots which are not already alloted to that class
                perm_slots=np.setdiff1d(perm_slots,self.theory_day_time_allotment[i])
                
                #separating the pairs of lab classes into one continuous array ["0-5:0-6","3-4:3-5"] ->["0-5","0-6","3-4","3-5"]
                separated_lab_day_time_allotment=np.empty(len(self.lab_day_time_allotment[i])*2,dtype=object)
                index_sep=0
                for cl in self.lab_day_time_allotment[i]:
                    separated_lab_day_time_allotment[index_sep]=cl[0:3]
                    index_sep+=1
                    separated_lab_day_time_allotment[index_sep]=cl[4:]
                    index_sep+=1
                
                perm_slots=np.setdiff1d(perm_slots,separated_lab_day_time_allotment[i])
                               
                mutation_index=random.randint(0,len(self.theory_day_time_allotment[i])-1)
                mutation_value_index=random.randint(0,len(perm_slots)-1)
                self.theory_day_time_allotment[i][mutation_index]=perm_slots[mutation_value_index]
                
                #mutating lab_day_time_allotment
                perm_slots=np.copy(self.day_time_slots)
                #finding  the slots which are not already alloted to that class
                perm_slots=np.setdiff1d(perm_slots,self.theory_day_time_allotment[i])
                perm_slots=np.setdiff1d(perm_slots,separated_lab_day_time_allotment[i])
                               
                mutation_index=random.randint(0,len(self.lab_day_time_allotment[i])-1)
               
                mutation_value_index=0
                count=0
                while True:
                    count+=1
                    mutation_value_index=random.randint(0,len(perm_slots)-2)
                    if count>1000:return
                    #checking if two concecutive slots are on the same day and  slots are consecutive 
                    if  int(perm_slots[mutation_value_index][0])==int(perm_slots[mutation_value_index+1][0]) and int(perm_slots[mutation_value_index][2])+1==int(perm_slots[mutation_value_index+1][2]):
                        break
                #alloting the selected slot
                print("mutation_value_index",mutation_value_index)
                lab_class1of2=perm_slots[mutation_value_index]
                lab_class2of2=perm_slots[mutation_value_index+1]
                self.lab_day_time_allotment[i][mutation_index]=str(lab_class1of2+":"+lab_class2of2)
            
            
            
                
                
                
                
                
                
        