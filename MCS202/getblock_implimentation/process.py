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
    0-write operation followed by marking buffer delayed write 
    1-work done(disk read is done if buffer was not initially valid), validate buffer 
    2-mark buffer invalid
    3-
    """
    time.sleep(2) #simulating an operation
    operation=random.randint(0,2)
    if(operation==0):
        buffer.setDelayedWriteBit()
    elif(operation==1):
        buffer.setValidBit()
    elif(operation==2):
        buffer.clearValidBit()


def sudoBRelease(hashQ,freeList,lock,buffer):
    lock.acquire()
    if(buffer.isValid()):
        freeList.addToFreeListEnd(buffer)
    else:
        freeList.addToFreeListFirst(buffer)

    buffer.clearLockedBit()
    lock.release()


def process(hashQ,freeList,lock,maxNoOfBlocks):
    
    while(True):
        time.sleep(2)#process will request a random block after every 2 second
        requestedBlock=random.randint(0,maxNoOfBlocks-1)
        print("process : ",os.getpid()," has requested block number : ",requestedBlock)
        recievedBuffer=BufferManagement.getBlock(requestedBlock,lock,hashQ,freeList)
        print("process : ",os.getpid(),"recieved buffer: ",recievedBuffer.getBlockNumber())
        
        sudoOperation(recievedBuffer)

        




