# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 21:26:50 2018

@author: abhishek sen
"""
class DNA(object):
    
    #self.day_time_allotment
    
    def __init__(self,theory_class_wise_partition,day_time_slots,professors,lab_class_wise_partition):
        """
        list of instance variables:
            day_time_allotment: stores alloted day and time for a particular class in theory_class_wise_partition
            
        """
        self.lab_class_wise_partition=lab_class_wise_partition
        self.day_time_slots=np.copy(day_time_slots)
        self.professors=np.copy(professors)
        self.fitness=0.0
        self.day_time_allotment=np.empty(np.shape(theory_class_wise_partition),dtype=object)

        for i in range(np.shape(self.day_time_allotment)[0]): 
            self.day_time_allotment[i]=np.empty(np.shape(theory_class_wise_partition[i]),dtype=object)
        
        
       #filling up the day_time_allotment array with random permuted slots 
        for i in range(len(day_time_allotment)):
            perm_slots=np.random.permutation(day_time_slots)
            index_perm=0
            for j in range(len(day_time_allotment[i])):
                self.day_time_allotment[i][j]=perm_slots[index_perm]
                index_perm+=1
        
        #for i in self.day_time_allotment:
         #   print (i)
    def calculate_fitness(self):
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
        for i,j in zip(professors,range(len(professors))):
            professor_index_map[i]=j
        
        
        
        days=6
        
        #professor time table of structure(professor_index,day,time)
        
        professor_timetable=np.zeros((len(self.professors),days,int(len(self.day_time_slots)/days)))
        
        for i in range(len(self.day_time_allotment)):
            for j in range(len(self.day_time_allotment[i])):
                #calculating indexes for professor_timetable
                professor_index=professor_index_map[course_professor_map[theory_class_wise_partition[i][j]]]
                dash=self.day_time_allotment[i][j].find('-')
                day_index=int(self.day_time_allotment[i][j][0:dash])
                time_index=int(self.day_time_allotment[i][j][dash+1:])
                professor_timetable[professor_index][day_index][time_index]+=1
        
        
        
        
        course_map={
                'MCA-1':0,
                'MCA-3':1,
                'MCS-1':2,
                'MCS-3':3
            }
         
        student_timetable=np.zeros((len(day_time_allotment),days,int(len(self.day_time_slots)/days)),dtype="S15")
        for i in range(len(self.day_time_allotment)):
            for j in range(len(self.day_time_allotment[i])):
                #calculating indexes for student_timetable
                dash=self.day_time_allotment[i][j].find('-')
                student_index=course_map[str(theory_class_wise_partition[i][j][0:5])]
                day_index=int(self.day_time_allotment[i][j][0:dash])
                time_index=int(self.day_time_allotment[i][j][dash+1:])
                
                student_timetable[student_index][day_index][time_index]=theory_class_wise_partition[i][j]+course_professor_map[theory_class_wise_partition[i][j]]
        
        
        
        
        
        
        for i in student_timetable:
            print (i,"\n")
            
            
        for i in professor_timetable:
            print (i,"\n")
