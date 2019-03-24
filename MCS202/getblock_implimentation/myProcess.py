import random
import time
import multiprocessing
import HashQueue
import FreeList
import BufferHeader
import BufferManagement
import os
import random


def sudoOperation(buffer):
    """
    0-write operation followed by marking buffer delayed write block and validating block 
    1-work done(disk read is done if buffer was not initially valid), validate buffer 
    2-mark buffer invalid
    3-process went into long sleep while holding the buffer
    """
    time.sleep(2) #simulating an operation
    operation=random.randint(0,3)
    if(operation==0):
        print("delayed Write: ",buffer.getBlockNumber())
        buffer.setDelayedWriteBit()
        buffer.setValidBit()
    elif(operation==1):
        buffer.setValidBit()
    elif(operation==2):
        buffer.clearValidBit()
    elif(operation==3):
        print("process: ",os.getpid()," is going into long sleep")
        time.sleep(15)
        print("process: ",os.getpid()," woke up")


def sudoBRelease(hashQ,freeList,lock,buffer):
    lock.acquire()
    if(buffer.isValid()):
        freeList.addToFreeListEnd(buffer)
    else:
        freeList.addToFreeListFirst(buffer)

    
    buffer.clearLockedBit()
    print("process: ",os.getpid()," is will unlock buffer  ",buffer.getBlockNumber()," lock status: ",buffer.isLocked())
    lock.release()


def process(hashQ,freeList,lock,maxNoOfBlocks):
    
    i=0
    while(i<10):
        time.sleep(2)#process will request a random block after every 2 second
        requestedBlock=random.randint(0,maxNoOfBlocks-1)
        print("process : ",os.getpid()," has requested block number : ",requestedBlock)
        recievedBuffer=BufferManagement.getBlock(requestedBlock,lock,hashQ,freeList)
        print("process : ",os.getpid(),"recieved buffer: ",recievedBuffer.getBlockNumber())

        print("\n",os.getpid()," hashQ: ")
        hashQ.printHashQ()
        print("\n",os.getpid()," freeList")
        freeList.printFreeList()

        
        sudoOperation(recievedBuffer)
        sudoBRelease(hashQ,freeList,lock,recievedBuffer)
        i+=1

        




