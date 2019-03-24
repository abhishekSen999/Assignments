import multiprocessing
import BufferHeader
import time
import os

def _writeAsynchronously(lock,bufferDataStructure,blockNumber):
    #locking as this is supposed to be a 
    #lock.acquire()

    print("************",blockNumber,"***************asynchronous writing")
    time.sleep(4)#sleep for 4 seconds to simulate writing to disk
    
    bufferDataStructure.clearDelayedWriteBit(blockNumber)
    #lock.release()
    print("************",blockNumber,"***************asynchronous writing over")
    #adding buffer to first of free list
    bufferDataStructure.addToFreeListFirst(blockNumber)
    #print("reached",buffer.isDelayedWrite(),"pid ",os.getpid())

def asynchronousWrite(lock,bufferDataStructure,blockNumber):
    
    writingProcess=multiprocessing.Process(target=_writeAsynchronously,args=(lock,bufferDataStructure,blockNumber,))
    writingProcess.start()
    
    return 1
