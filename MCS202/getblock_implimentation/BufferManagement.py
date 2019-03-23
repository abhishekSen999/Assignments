import multiprocessing
import AsynchronousWrite
import time
class BufferManagement(object):
    def getBlock(self,blockNumber,lock,hashQ,freeList):
        bufferFound=False
        while (not bufferFound):

            lock.acquire()#lock
            if (hashQ.isPresentInHashQ(blockNumber)):

                buffer=hashQ.findBlockInHashQ(blockNumber)
                if(buffer.isLocked()):
                    lock.release()
                    time.sleep(4)
                    continue
                buffer.setLockedBit()
                freeList.removeFromFreeList(buffer)
                lock.release()
                return buffer
            else:
                if (freeList.isEmpty()):
                    lock.release()
                    time.sleep(4)
                    continue
                buffer=freeList.removeAnyFromFreeList()
                if(buffer.isDelayedWrite()):
                    self.asynchronous

            

