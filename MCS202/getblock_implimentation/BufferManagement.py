import multiprocessing
import AsynchronousWrite
import time
import os
import BufferDataStructure

def getBlock(blockNumber,lock,bufferDataStructure):
    bufferFound=False
    while (not bufferFound):

        lock.acquire()     #lock

        #The buffer is in the hashQ 
        if (bufferDataStructure.isPresentInHashQ(blockNumber)):
            #buffer=hashQ.findBlockInHashQ(blockNumber)
            if(bufferDataStructure.isLocked(blockNumber)):

                #For revealing the scenario under which process is going to sleep
                print("Process ",os.getpid()," is going to sleep as buffer ",blockNumber," is present in hashQ and is busy")
                lock.release()
                time.sleep(4)
                continue
            
            #Reqiured buffer is in the hash queue and unlocked
            bufferDataStructure.setLockedBit(blockNumber)
            bufferDataStructure.removeFromFreeList(blockNumber)

            #Return the buffer to the requesting process
            print("Process ",os.getpid()," will get buffer ",blockNumber," from hashQ")
            bufferFound=True
            lock.release()
            return blockNumber

        #Buffer is not in the hashQ. Hence, check freelist for the buffer  
        else:
            #Freelist is empty
            if (bufferDataStructure.isEmptyFreeList()):   

                #For revealing the scenario under which process is going to sleep
                print("Process ",os.getpid()," is going to sleep as freeList is empty")

                lock.release()
                time.sleep(4) 
                continue

            #Freelist is not empty
            blockNumber_freeList=bufferDataStructure.getAnyFromFreeList() #just getting the first free buffer(not removing from free list yet)

            #Check if the buffer is marked as 'delayed write'
            if(bufferDataStructure.isDelayedWrite(blockNumber_freeList)):

                #Now removing it from free list
                bufferDataStructure.removeFromFreeList(blockNumber_freeList)
                print("freelist after removing ",blockNumber_freeList)
                bufferDataStructure.printFreeList()
                #For revealing the scenario under which process is going to do asynchronous write
                print("Process ",os.getpid()," came across free buffer ",blockNumber_freeList, " but marked as delayed write so is executing asynchronous write")
                
                lock.release()
                AsynchronousWrite.asynchronousWrite(lock,bufferDataStructure,blockNumber_freeList)
                continue

            #Found a free buffer in the freelist 
            bufferDataStructure.removeFromHashQ(blockNumber_freeList)

            print("Replace buffer ",blockNumber_freeList," in freeList, with buffer ",blockNumber)


            print("Buffer ",blockNumber_freeList," is removed from free list")
            print("Buffer ",blockNumber," added to the hash queue")
            #replacing the old block number(returnrd from the freeList ) with the new block number
            bufferDataStructure.setBlockNumber(blockNumber_freeList,blockNumber)
            

            #Add buffer to the new hash queue
            bufferDataStructure.addBlockToHashQ(blockNumber)

            #remove it from the free list
            bufferDataStructure.removeFromFreeList(blockNumber) 

            #Update status of the buffer
            bufferDataStructure.setLockedBit(blockNumber)
            bufferDataStructure.clearValidBit(blockNumber)


            bufferFound=True
            lock.release()
            return blockNumber





