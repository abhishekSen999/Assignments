import multiprocessing
import BufferHeader
import time
import os

def _writeAsynchronously(lock,buffer):
    #locking as this is supposed to be a 
    # lock.acquire()

    print("************",buffer.getBlockNumber(),"***************asynchronous writing")
    time.sleep(4)#sleep for 4 seconds to simulate writing to disk
    
    buffer.clearDelayedWriteBit()
    # lock.release()
    print("************",buffer.getBlockNumber(),"***************asynchronous writing over")
    #print("reached",buffer.isDelayedWrite(),"pid ",os.getpid())

def asynchronousWrite(lock,buffer):
    
    writingProcess=multiprocessing.Process(target=_writeAsynchronously,args=(lock,buffer,))
    writingProcess.start()
    
    return 1
