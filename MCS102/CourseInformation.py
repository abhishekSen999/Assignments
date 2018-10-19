#course_information
class CourseInformation(object):
    
    def __init__(self,absolute_path='E:/Assignments/MCS102/COURSE_DATA.csv'):
        import pandas as pd
        import numpy as np
        course_data=pd.read_csv(absolute_path)
        
        self.professors=np.array(course_data.professor.unique())
        
        paper_code=np.array(course_data.paper_code)
        
        theory_freq=np.array(course_data.theory)
        dpt_sem= np.unique([pc[0:5] for pc in paper_code])
        
        theory_classes_frequency=np.array([pc for pc,freq in zip(paper_code,theory_freq) for i in range(freq)])
        course_map={
                'MCA-1':0,
                'MCA-3':1,
                'MCS-1':2,
                'MCS-3':3
            }

        self.theory_class_wise_partition=[[],[],[],[]]
        for i in theory_classes_frequency :
            self.theory_class_wise_partition[course_map[i[0:5]]].append(i)
        
        self.lab_class_wise_partition=[[],[],[],[]]
        lab1_freq=np.array(course_data.lab1)
        lab2_freq=np.array(course_data.lab2)

        for pc,lb1_frq,lb2_frq in zip(paper_code,lab1_freq,lab2_freq):
            k=int(lb1_frq)+int(lb2_frq)
            for frq in range(k):
                self.lab_class_wise_partition[course_map[pc[0:5]]].append(pc)
                
                
                
        
        day_slots=["monday","tuesday","wednesday","thursday","friday","saturday"]
        #time_slots=["9-10","10-11","11-12","12-1"]
        time_slots=["9-10","10-11","11-12","12-1","1-2","2-3","3-4","4-5"]
        #day_time_slots = [str(d)+"-"+str(t) for d,t in zip(range(len(day_slots)),range(len(time_slots)))]
        self.day_time_slots=np.empty(len(day_slots)*len(time_slots),dtype=object)
        index=0
        for ds in range(len(day_slots)):
            for ts in range(len(time_slots)):
                self.day_time_slots[index]=str(ds)+"-"+str(ts) 
                index+=1

