# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:27:44 2018
 
@author: abhishek sen
"""
import numpy as np
import math
class Sudoku_solver(object):
        
        
    #returns a list [(true/false depending on whether it is solved or not),(the solved 2d array of True)]
    def run(self,side=9,arr=[[0,0,2,0,0,0,9,0,7],[0,0,8,0,0,0,0,0,0],[1,0,0,2,0,7,0,0,5],[0,8,0,0,0,5,0,0,0],[0,4,0,6,0,3,0,5,0],[0,0,0,9,0,0,0,7,2],[4,0,0,5,0,2,0,0,3],[0,1,0,0,0,0,0,0,0],[5,0,7,0,0,0,4,0,0]]):
        sudoku=np.copy(arr)
        if not self.isCorrect(side,sudoku):
            print("\n1",sudoku)
            return [False]
        return self.sudoku_solver(side,arr,0,0)
        
        
        
        
    def sudoku_solver(self,side,arr,row,col):
        
        root=int(math.sqrt(side))
        sudoku=np.copy(arr)
        if self.isSolved(side,sudoku): return [True,sudoku]
        
        #skipping over filled up slots
        while sudoku[row,col]!=0:
            row+=0 if col<(side-1) else 1
            col=(col+1)%side
        
        row_array=sudoku[row,:]
        col_array=sudoku[:,col]
        
        r=row-row%root #row number of 1st element in that internal square
        c=col-col%root #col number of 1st element in that internal square
        
        #various ways :-
        
        #internal_square_array=np.zeros(side,dtype=np.int8)
        #k=0
        #for i in range(0,root):
        #    for j in range(0,root):
        #        internal_square_array[k]=sudoku[r+i,c+j]
        
        #internal_square_array=np.array([j for i in sudoku[r:r+root] for j in i[c:c+root]])
        
        internal_square_array=sudoku[r:r+root,c:c+root].reshape(side)
        
        
        
        possible=np.array([i for i in range(1,side+1)])
        
        allowed_values=np.setdiff1d(possible,row_array)
        allowed_values=np.setdiff1d(allowed_values,col_array)
        allowed_values=np.setdiff1d(allowed_values,internal_square_array)
        
        for value in allowed_values:
            sudoku[row,col]=value
            row1=row
            col1=col
            row1+=0 if col<(side-1) else 1
            col1=(col1+1)%side
            recieved=self.sudoku_solver(side,sudoku,row1,col1)
            if recieved[0]==True :
                return recieved
            
        return[False]
    
    def isCorrect(self,side,sudoku):
        root=int(math.sqrt(side))
        row=[0 for i in range(side+1)] 
        col=[0 for i in range(side+1)]
        box=[0 for i in range(side+1)]
        
        #checking correctness in row
        for i in range(side):
             row=[0 for i in range(side+1)] 
             row_array=sudoku[i,:]
             print(row_array)
             for j in range(side):
                 row[row_array[j]]+=1
                 
             for j in range(1,side+1):
                 if row[j]>1:
                     print("row",row,j)
                     return False
        
        #checking correctness in column         
        for i in range(side):
            col=[0 for i in range(side+1)]
            col_array=sudoku[:,i]
            for j in range(side):
                col[col_array[j]]+=1
                
            for j in range(1,side+1):
                if col[j]>1:
                    print("col",col,j)
                    return False
                
        #checking correctness in each internal square
        i=0
        j=0
        while(i<side and j<side):
            box=[0 for i in range(side+1)]
            box_array=sudoku[i:i+root,j:j+root].reshape(side)
            for k in range(side):
                box[box_array[k]]+=1
            for k in range(1,side+1):
                if box[k]>1:
                    print ("box",i,j)
                    print(box)
                    return False
                
            j=(j+root)%side
            if (j==0):
                i=i+root
                
            
        return True
    
    
    def isSolved(self,side,arr):
        result=int(side*(side+1)/2)
        
        root=int(math.sqrt(side))
        
        #checking rows
        for i in np.sum(arr,0):
            if i!=result :
                return False
            
        #checking columns
        for i in np.sum(arr,1):
            if i!=result :
                return False
            
        #checking internal squares
        check_arr=np.zeros((root,root),dtype=np.int8)
        for row in range(0,side):
            for col in range(0,side):
                check_arr[int((row-row%root)/root)][int((col-col%root)/root)]+=arr[row][col]
        
        if len([False for i,j in zip(range(root),range(root)) if check_arr[i,j]!=result])>0:
            return False
        
        
        return True


        
        
        
        
