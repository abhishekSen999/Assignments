import multiprocessing
import BufferHeader
import time

def _writeAsynchronously(buffer):
    time.sleep(4)#sleep for 4 seconds to simulate writing to disk
    
    buffer.clearDelayedWriteBit()
    print("reached",buffer.isDelayedWrite())

def asynchronousWrite(buffer):
    
    writingProcess=multiprocessing.Process(target=_writeAsynchronously,args=(buffer,))
    writingProcess.start()
    
    return 1
