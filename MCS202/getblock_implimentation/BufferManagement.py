import multiprocessing
import AsynchronousWrite
import time
import os
import BufferDataStructure
def getBlock(blockNumber,lock,bufferDataStructure):
    bufferFound=False
    while (not bufferFound):

        lock.acquire()#lock
        if (bufferDataStructure.isPresentInHashQ(blockNumber)):


            #buffer=hashQ.findBlockInHashQ(blockNumber)
            if(bufferDataStructure.isLocked(blockNumber)):

                #for revealing the scenario under which process is going to sleep
                print("process: ",os.getpid()," is going to sleep as buffer ",blockNumber," is present in hashQ and is busy")
                lock.release()
                time.sleep(4)
                continue
            
            
            bufferDataStructure.setLockedBit(blockNumber)
            bufferDataStructure.removeFromFreeList(blockNumber)

            #for revealing the scenario under which process is going to sleep
            print("process: ",os.getpid(),"  will get buffer  ",blockNumber," from hashQ")

            lock.release()
            return blockNumber
        else:
            if (bufferDataStructure.isEmptyFreeList()):

                #for revealing the scenario under which process is going to sleep
                print("process: ",os.getpid()," is going to sleep as freeList is empty")

                lock.release()
                time.sleep(4)
                continue


            blockNumber_freeList=bufferDataStructure.getAnyFromFreeList() #just getting the first free buffer(not removing from free list yet)

            if(bufferDataStructure.isDelayedWrite(blockNumber_freeList)):

                #now removing it from free list
                bufferDataStructure.removeFromFreeList(blockNumber_freeList)
                #for revealing the scenario under which process is going to do asynchronous write
                print("process: ",os.getpid()," came across block number: ",blockNumber_freeList, "marked as delayed write so is executing asynchronous write")
                
                lock.release()
                AsynchronousWrite.asynchronousWrite(lock,bufferDataStructure,blockNumber_freeList)
                continue


            bufferDataStructure.removeFromHashQ(blockNumber_freeList)

            print("process: ",os.getpid()," is will replace buffer  ",blockNumber_freeList,"  from freeList with buffer ",blockNumber)

            bufferDataStructure.setBlockNumber(blockNumber_freeList,blockNumber)
            
            bufferDataStructure.addBlockToHashQ(blockNumber)
            bufferDataStructure.removeFromFreeList(blockNumber)#as its block number has changed ,( it is removed from freeList using new block number 
            
            bufferDataStructure.setLockedBit(blockNumber)
            bufferDataStructure.clearValidBit(blockNumber)#making it invalid

            #for revealing the scenario under which process is returning
            # print("process: ",os.getpid()," is will get buffer  ",buffer.getBlockNumber(),"  from freeList")

            lock.release()
            return blockNumber

                

            

