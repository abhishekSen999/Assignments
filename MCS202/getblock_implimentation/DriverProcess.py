import random
import BufferHeader
import multiprocessing
from multiprocessing.managers import BaseManager
from multiprocessing import Process, Manager
import random
import time
import HashQueue
import FreeList
import BufferHeader
import BufferManagement
import os
import myProcess
def main():

    lengthOfHashQ=4
    freeListSize=20
    maxNoOfBlocks=50

    #using shared memory objects using BaseManager from multiprocessing library
    BaseManager.register('HashQueue',HashQueue.HashQueue)
    BaseManager.register('FreeList',FreeList.FreeList)
    manager=BaseManager()
    manager.start()

    hashQ=manager.HashQueue(lengthOfHashQ)
    freeList=manager.FreeList(freeListSize)
    lock=multiprocessing.Lock()
    p1=multiprocessing.Process(target=myProcess.process,args=(hashQ,freeList,lock,maxNoOfBlocks,))
    p2=multiprocessing.Process(target=myProcess.process,args=(hashQ,freeList,lock,maxNoOfBlocks,))
    p3=multiprocessing.Process(target=myProcess.process,args=(hashQ,freeList,lock,maxNoOfBlocks,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("end")





