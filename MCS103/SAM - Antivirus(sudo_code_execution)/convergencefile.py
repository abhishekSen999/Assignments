import sys
import re
class Evaluation(object):
    """
    This class is used to implement a series of mathematical equations taken input as string containing variables and outputs the variables 
    and their values after the series of operations are over 
    
    Sample inputs:
        "y=5;x=y+4;x=3*x;x= x + y "
        
    sample output:
        ['y', 'x']
        [5, 32]
        
    Sample inputs:
        "y=5;x=y+4;x*=3;x+= y "
        
    sample output:
        ['y', 'x']
        [5, 32]
        
        
    function findValue(expression): recursively finds value of expression
    
    function chechEquation(sequenceOfOperations) goes through the list and evualates each equation and stores the values and corresponding variables
    
    
    
    
    
    """
    bufferVariables=[]
    bufferValues=[]
    
  #  def checkExpression(self,espression="a<3"):
        
    def findValue(self, expression="2+3*(5-3)+2" ):
        expression=expression.strip()#avoiding excess spaces
        
        val=0
        #if bracket is present then compute thet section separately and reinsertiong in the expression
        bracket=expression.find('(')
        if(bracket!=-1):
            endBracket=expression.find(')')
            expression=expression[0:bracket]+str(self.findValue(expression[bracket+1:endBracket]))+expression[endBracket+1:]
            return(self.findValue(expression))
        
        
        divide=expression.find('/')
        multiply=expression.find('*')
        add=expression.find('+')
        sub=expression.find('-')
        
        
        
        #if expression is just number or variable
        if divide==-1 and multiply==-1 and add ==-1 and sub==-1:
            if expression.isnumeric():return(int(expression))
            elif self.bufferVariables.__contains__(expression):return self.bufferValues[self.bufferVariables.index(expression)]
            else:
                sys.exit
            
                   
                   
                   
                   
        #handeling operations as in a binary expression tree while following BEDMAS
        if add!=-1:
            val=self.findValue(expression[0:add])+self.findValue(expression[add+1:])
            return val
        elif sub!=-1:
            val=self.findValue(expression[0:sub])-self.findValue(expression[sub+1:])
            return val
        elif multiply!=-1:
            val=self.findValue(expression[0:multiply])*self.findValue(expression[multiply+1:])
            return val
        else:
            val=self.findValue(expression[0:divide])/self.findValue(expression[divide+1:])
            return val 
            
    
    
    def checkEquations(self,sequenceOfOperations=["y=5","x=y+4","x=3*x","x=x+y"]):
               
        for i in sequenceOfOperations:
            assignment=i.find("=")
            #checking if assignment is taking place in the statement
            if assignment!= -1:
                var=i[0:assignment]#extracting the name of the variable
                rhs=i[assignment+1:]
                #handeling expression like x+=5
                if var.endswith('+') or var.endswith('-') or var.endswith('*') or var.endswith('/'):
                    rhs=var+rhs
                    var=var.strip(var[-1])
                    
                if self.bufferVariables.__contains__(var):  # if variable already present in buffer the its value is updated
                    val=self.findValue(rhs)
                    self.bufferValues[self.bufferVariables.index(var)]=val
                else:  # if variable is not present in buffer it is added and a initialised with 0 followed by assigning its given value
                    self.bufferVariables.append(var)
                    self.bufferValues.append(0)
                    self.bufferValues[-1]=self.findValue(rhs);
 
    

    def checkCondition(self, s="False"):
        #self.bufferValues=[2,3,4]
        #self.bufferVariables=['a','b','c']
        condition1= s.find('<')
        lhs,rhs="",""
        if condition1>=0:
            equality=s.find('=')
            if(equality>=0):
                lhs=s[:condition1]
                lhs=lhs.strip()
                rhs=s[equality+1:]
                rhs=rhs.strip()
                if lhs.isnumeric():
                    self.bufferValues.append(int(lhs))
                    lhs="X"+lhs
                    self.bufferVariables.append(lhs)
                if rhs.isnumeric():
                    self.bufferValues.append(int(rhs))
                    rhs="X"+rhs
                    self.bufferVariables.append(rhs)
                
                
                return self.bufferValues[self.bufferVariables.index(lhs)] <= self.bufferValues[self.bufferVariables.index(rhs)]
            else:
                lhs=s[:condition1]
                lhs=lhs.strip()
                rhs=s[condition1+1:]
                rhs=rhs.strip()
                
                if lhs.isnumeric():
                    self.bufferValues.append(int(lhs))
                    lhs="X"+lhs
                    self.bufferVariables.append(lhs)
                if rhs.isnumeric():
                    self.bufferValues.append(int(rhs))
                    rhs="X"+rhs
                    self.bufferVariables.append(rhs)
                
                return  self.bufferValues[self.bufferVariables.index(lhs)] < self.bufferValues[self.bufferVariables.index(rhs)]
                
            
        condition2=s.find('>')
            
        
        lhs,rhs="",""
        if condition2>=0:
            equality=s.find('=')
            if(equality>=0):
                lhs=s[:condition2]
                lhs=lhs.strip()
                rhs=s[equality+1:]
                rhs=rhs.strip()
                if lhs.isnumeric():
                    self.bufferValues.append(int(lhs))
                    lhs="X"+lhs
                    self.bufferVariables.append(lhs)
                if rhs.isnumeric():
                    self.bufferValues.append(int(rhs))
                    rhs="X"+rhs
                    self.bufferVariables.append(rhs)
                
                return self.bufferValues[self.bufferVariables.index(lhs)] >= self.bufferValues[self.bufferVariables.index(rhs)]
            else:
                lhs=s[:condition2]
                lhs=lhs.strip()
                rhs=s[condition2+1:]
                rhs=rhs.strip()
                if lhs.isnumeric():
                    self.bufferValues.append(int(lhs))
                    lhs="X"+lhs
                    self.bufferVariables.append(lhs)
                if rhs.isnumeric():
                    self.bufferValues.append(int(rhs))
                    rhs="X"+rhs
                    self.bufferVariables.append(rhs)
                
                return  self.bufferValues[self.bufferVariables.index(lhs)] > self.bufferValues[self.bufferVariables.index(rhs)]
                
        condition3=s.find('==')
        
        
        lhs,rhs="",""
        if condition3>=0:
                lhs=s[:condition3]
                lhs=lhs.strip()
                rhs=s[condition3+1+1:]
                rhs=rhs.strip()
                if lhs.isnumeric():
                    self.bufferValues.append(int(lhs))
                    lhs="X"+lhs
                    self.bufferVariables.append(lhs)
                if rhs.isnumeric():
                    self.bufferValues.append(int(rhs))
                    rhs="X"+rhs
                    self.bufferVariables.append(rhs)
                
                return  self.bufferValues[self.bufferVariables.index(lhs)] == self.bufferValues[self.bufferVariables.index(rhs)]
        
        condition4=s.find('!=')
        
        lhs,rhs="",""
        if condition4>=0:
                lhs=s[:condition4]
                lhs=lhs.strip()
                rhs=s[condition4+1+1:]
                rhs=rhs.strip()
                if lhs.isnumeric():
                    self.bufferValues.append(int(lhs))
                    lhs="X"+lhs
                    self.bufferVariables.append(lhs)
                if rhs.isnumeric():
                    self.bufferValues.append(int(rhs))
                    rhs="X"+rhs
                    self.bufferVariables.append(rhs)
                
                return  self.bufferValues[self.bufferVariables.index(lhs)] != self.bufferValues[self.bufferVariables.index(rhs)]
        
        #s=s.strip()
        if s=="True": return True
        
        if s=="False": return False






 
def isConverging( sequenceOfOperations, loopVar, intendedValue, evaluation_object):
    
    #storing initial value of loop variable
    loopVarVal_initial=evaluation_object.bufferValues[evaluation_object.bufferVariables.index(loopVar)]
    
    #evaluating the sequence of operations and storing its values and variables
    evaluation_object.checkEquations(sequenceOfOperations)
    
     #storing final value of loop variable
    loopVarVal_final=evaluation_object.bufferValues[evaluation_object.bufferVariables.index(loopVar)]
    
    #returning if the gap between intended value and loop variable has reduced or not
    return (abs(loopVarVal_final-intendedValue)<abs(loopVarVal_initial-intendedValue))



def convergence(path):
    
    #print("\n\nconvergence : ",path,"\n\n")
    '''
    in the for loop whole file to check infinite loop is being copied
    '''
    
    file_read=open(path,"r")
    whileStart=-1
    sequenceOfOperations=''
    for line in file_read:
        sequenceOfOperations+=line
    file_read.close()
    
    '''
    all the lines are being seperated to form the list
    '''
    
    sequenceOfOperations=sequenceOfOperations.split('\n') #the file is breakdown into equations
    operationsBeforeWhile=[]            #operations before execution of while loop
    
    '''
    while keyword is being searched in the file and whole file before while loop is being copied to operationsBeforeWhile
    '''
    
    for i in range(0,len(sequenceOfOperations)):    #searching for while loop
        if(re.match(r'(.*)while(.*)',sequenceOfOperations[i],)):
            whileStart=i
            break
        operationsBeforeWhile.append(sequenceOfOperations[i])
    
    '''
    returning if while loop is not present in the code
    '''
    
    if whileStart==-1:
        return True
    
    '''
    all the \t and \n are being removed from the code before while loop
    '''
    
    for i in range(0,len(operationsBeforeWhile)):
        operationsBeforeWhile[i]=operationsBeforeWhile[i].strip()
    
    '''
    whole of the code before while loop is being evaluated to get updated values of variables used in the file
    '''
    
    obj=Evaluation()
    obj.checkEquations(operationsBeforeWhile)
    
    
    ''' 
    checking if condition is true before loop starts
    '''
    whileStatement=sequenceOfOperations[whileStart]
    condition=whileStatement[whileStatement.find('(')+1:whileStatement.find(')')]
    #print (condition)
    isTrueBeforeLoopStarts=obj.checkCondition(condition)
    
    
    
    
    '''
    whole of the while loop is stored in another variable operationsInWhile
    '''
    
    operationsInWhile=[]
    for i in range(whileStart+1,len(sequenceOfOperations)): #operations in while loop are searched
        operationsInWhile.append(sequenceOfOperations[i])
        if(re.match(r'(.*)\t(.*)',sequenceOfOperations[i],)):
            break
    '''
    all the \t and \n are being removed from the code in while loop
    '''
    
    for i in range(0,len(operationsInWhile)):
        operationsInWhile[i]=operationsInWhile[i].strip()
    
    '''
    the variables and constants used in while loop conditions are stored in the variables
    '''
    
    end=sequenceOfOperations[whileStart].find('<')  #extracting condition variables and intended values
    end=max(sequenceOfOperations[whileStart].find('>'),end)
    if end != -1:
        loopVar=sequenceOfOperations[whileStart][sequenceOfOperations[whileStart].find('(')+1:end]
        intendedValue=sequenceOfOperations[whileStart][end+1:sequenceOfOperations[whileStart].find(')')]
        if intendedValue.isalpha():
            intendedValue=obj.bufferValues[obj.bufferVariables.index(intendedValue)]
        
        
        '''
        copying the before while values in another object and then checking the values are being converged to the conditions or not
        '''
        
        obj2=Evaluation()
        obj2.bufferValues.append(obj.bufferValues)
        obj2.bufferVariables.append(obj.bufferVariables)
        isLoopVariableConverging=isConverging(operationsInWhile,loopVar,int(intendedValue),obj2)
    else:
          isLoopVariableConverging=False
            
    isFinite=((isTrueBeforeLoopStarts and isLoopVariableConverging) or (not isTrueBeforeLoopStarts ))   
    return isFinite
    
    
    
    
    
    
    
    
if __name__ == "__main__":
     ob=Evaluation()
     print(ob.checkCondition())
       