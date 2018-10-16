import re
def isBufferOverflow(path):
    #print("\n\nisBufferOverflow : ",path,"\n\n")
    file_read=open(path,"r")
    sequenceOfOperations=''
    '''
    in the for loop whole file to check virus is copied
    '''
    for line in file_read:
        sequenceOfOperations+=line    
    '''
    all the lines are being seperated to form the list
    '''
    sequenceOfOperations=sequenceOfOperations.split('\n')
    file_read.close()
    variableName=''
    '''
    the array intialization is searched in the file like numpy.empty(n,dtype)
    variable name and it's size is being stored
    '''
    for i in range(0,len(sequenceOfOperations)):
        #if(re.match(r'(.*)numpy.empty(.*)',sequenceOfOperations[i],)):
         if sequenceOfOperations[i].find('numpy.empty')>=0:
            variableName=sequenceOfOperations[i][0:sequenceOfOperations[i].find('=')]  #finding the array name and size
            variableValue=(int)(sequenceOfOperations[i][(sequenceOfOperations[i].find('(')+1):sequenceOfOperations[i].find(',')])
            variableName+='['           #to eliminate print states
            '''
            for every array found in the file all the accesses to the the array is being checked,
            if any index out of bound has occured or not.
            '''        
            for j in range(i+1,len(sequenceOfOperations)):
                if(re.match(r'(.*)'+re.escape(variableName)+r'(.*)',sequenceOfOperations[j],)):
                    checkValue=(int)(sequenceOfOperations[j][(sequenceOfOperations[j].find('[')+1):sequenceOfOperations[j].find(']')])  #checking values accessed in whole of the program
                    if(checkValue>=variableValue):
                        return True
    return False

