import BufferHeader
import time
import AsynchronousWrite
import multiprocessing 

from multiprocessing.managers import BaseManager
from multiprocessing import Process, Manager

BaseManager.register('BufferHeader',BufferHeader.BufferHeader)
manager=BaseManager()
manager.start()
buffer=manager.BufferHeader(5)
buffer.setDelayedWriteBit()

pid=AsynchronousWrite.asynchronousWrite(buffer)
pid=AsynchronousWrite.asynchronousWrite(buffer)
print("1 ",buffer.isDelayedWrite())

while(True):
    print("2 ",buffer.isDelayedWrite())
    if(not buffer.isDelayedWrite()):
        break