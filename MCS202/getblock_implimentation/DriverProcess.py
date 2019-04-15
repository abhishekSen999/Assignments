import random
import BufferHeader
import multiprocessing
from multiprocessing.managers import BaseManager
from multiprocessing import Process, Manager
import random
import time
import BufferDataStructure
import BufferHeader
import BufferManagement
import os
import myProcess
import SleepQueue
import numpy as np




lengthOfHashQ=4
freeListSize=20
maxNoOfBlocks=30
noOfProcesses=5

#using shared memory objects using BaseManager from multiprocessing library
#BaseManager is used to create proxy classes in this session which are present in the shared memory
BaseManager.register('BufferDataStructure',BufferDataStructure.BufferDataStructure)
BaseManager.register('SleepQueue',SleepQueue.SleepQueue)

manager=BaseManager()
manager.start()

sleepQueue=manager.SleepQueue()
bufferDataSructure=manager.BufferDataStructure(freeListSize,lengthOfHashQ)
#bufferDataSructure.mapFreeListIntoHashQ()

print("\nInitial State of hashQ")
bufferDataSructure.printHashQ()
print("\nInitial State of freeList")
bufferDataSructure.printFreeList()

lock=multiprocessing.Lock()

<<<<<<< HEAD
#Creating processes_array
process_array=np.empty(noOfProcesses,dtype=object)

#initializing the elements in process array with procvesses from the multiprocessing class
for i in range(noOfProcesses):
    process_array[i]=multiprocessing.Process(target=myProcess.process,args=(sleepQueue,bufferDataSructure,lock,maxNoOfBlocks,))

for i in range(noOfProcesses):
    process_array[i].start()


=======
#Creating processes
#Process(Process(target=callable object,args=argument tuple for the target invocation)
p1=multiprocessing.Process(target=myProcess.process,args=(sleepQueue,bufferDataSructure,lock,maxNoOfBlocks,))
p2=multiprocessing.Process(target=myProcess.process,args=(sleepQueue,bufferDataSructure,lock,maxNoOfBlocks,))
p3=multiprocessing.Process(target=myProcess.process,args=(sleepQueue,bufferDataSructure,lock,maxNoOfBlocks,))

#Starting processes
p1.start()
p2.start()
p3.start()
>>>>>>> db90a51dbcfae65b2fab79291837087e94d5d0f4
    

#waiting for processes to join (join- finish their operation and join this execution)
<<<<<<< HEAD
for i in range(noOfProcesses):
    process_array[i].join()
=======
p1.join()
p2.join()
p3.join()

>>>>>>> db90a51dbcfae65b2fab79291837087e94d5d0f4
#print when all the processes are finished
print("\n~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~\n")








