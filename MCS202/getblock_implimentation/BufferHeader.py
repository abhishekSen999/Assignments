class BufferHeader:
    
    def __init__(self):
        self.block_number=0
        self.status_locked=0
        self.status_valid=0
        self.status_delayed_write=0
        self.waiting_process_count=0

        self.hashQ_next=None
        self.hashQ_prev=None
        self.freeList_next=None
        self.freeList_prev=None




    def setBlockNumber(block_number):
        self.block_number=block_number

    def getBlockNumber():
        return self.block_number





    def setLockedBit():
        self.status_locked=1

    def clearLockedBit():
        self.status_locked=0

    def isLocked():
        if(self.status_locked==1):
            return True
        return False





    def setValidBit():
        self.status_valid=1
    
    def clearValidBit():
        self.status_valid=0

    def isValid():
        if(self.status_valid==1):
            return True
        return False 





    def setDelayedWriteBit():
        self.status_delayed_write =1
    
    def clearDelayedWriteBit():
        self.status_delayed_write =0

    def isDelayedWrite():
        if(self.status_delayed_write ==1):
            return True
        return False 





    def addWaitingProcess():
        self.waiting_process_count= self.waiting_process_count+ 1
    
    def removeWaitingProcess ():
        if (self.waiting_process_count==0):
            return -1
        self.status_delayed_write = self.waiting_process_count- 1

    def hasWaitingProcess ():
        if(self.waiting_process_count >0):
            return True
        return False 

    
