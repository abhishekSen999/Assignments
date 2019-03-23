import random
import time
import multiprocessing
import HashQueue
import FreeList
import BufferHeader
import BufferManagement
import os


def sudoOperation():
    """
    0-write operation followed by marking buffer delayed write and unlocking
    1-work done(disk read is done if buffer was not initially valid), validate buffer ,unlock buffer
    2-mark buffer invalid
    3-

    """

def sudoBRelease(hashQ,freeList,lock,block):


def process(hashQ,freeList,lock,maxNoOfBlocks):
    
    while(True):
        time.sleep(2)#process will request a random block after every 1 second
        requestedBlock=random.randint(0,maxNoOfBlocks-1)
        print("process : ",os.getpid()," has requested block number : ",requestedBlock)
        recievedBuffer=BufferManagement.getBlock(requestedBlock,lock,hashQ,freeList)
        print("process : ",os.getpid(),"recieved buffer: ",recievedBuffer.getBlockNumber())
        time.sleep(2)
        sudoOperation(buffer)




