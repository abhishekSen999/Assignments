import random
import time
import multiprocessing
import BufferDataStructure
import BufferHeader
import BufferManagement
import os
import random


def pseudoOperation(bufferDataStructure ,buffer):
    """
    0-write operation followed by marking buffer delayed write block and validating block 
    1-work done(disk read is done if buffer was not initially valid), validate buffer 
    2-mark buffer invalid
    3-process went into long sleep while holding the buffer
    """
    time.sleep(2) #simulating an operation
    operation=random.randint(0,3)
    if(operation==0):
        print("delayed Write: ",buffer)
        bufferDataStructure.setDelayedWriteBit(buffer)
        bufferDataStructure.setValidBit(buffer)
    elif(operation==1):
        bufferDataStructure.setValidBit(buffer)
    elif(operation==2):
        bufferDataStructure.clearValidBit(buffer)
    elif(operation==3):
        print("process: ",os.getpid()," is going into long sleep")
        time.sleep(15)
        print("process: ",os.getpid()," woke up")


def pseudoBRelease(bufferDataStructure,lock,buffer):
    lock.acquire()
    if(bufferDataStructure.isValid(buffer)):
        bufferDataStructure.addToFreeListEnd(buffer)
    else:
        bufferDataStructure.addToFreeListFirst(buffer)

    
    bufferDataStructure.clearLockedBit(buffer)
    print("process: ",os.getpid()," is will unlock buffer  ",buffer," lock status: ",bufferDataStructure.isLocked(buffer))
    lock.release()


def process(bufferDataStructure,lock,maxNoOfBlocks):
    
    i=0
    while(i<10):
        time.sleep(2)#process will request a random block after every 2 second
        requestedBlock=random.randint(0,maxNoOfBlocks-1)
        print("process : ",os.getpid()," has requested block number : ",requestedBlock)
        recievedBuffer=BufferManagement.getBlock(requestedBlock,lock,bufferDataStructure)
        print("process : ",os.getpid(),"recieved buffer: ",recievedBuffer)

        print("\n",os.getpid()," hashQ: ")
        bufferDataStructure.printHashQ()
        print("\n",os.getpid()," freeList")
        bufferDataStructure.printFreeList()

        
        pseudoOperation(bufferDataStructure ,recievedBuffer)
        pseudoBRelease(bufferDataStructure,lock,recievedBuffer)
        i+=1

        




