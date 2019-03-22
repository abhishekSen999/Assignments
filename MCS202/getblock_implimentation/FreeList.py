import random
import BufferHeader
import numpy as np


class FreeList(object):

    def __init__(self, size=20):
        # expecting a free list size of 1 or more
        if(size < 1):
            return
        self.size = size
        self.freeListHeader = BufferHeader.BufferHeader(0)
        prevBlock = self.freeListHeader
        # implememnting the circular free list
        for i in range(1, self.size):
            block = BufferHeader.BufferHeader(i)
            prevBlock.addNextFreeList(block)
            block.addPrevFreeList(prevBlock)
            prevBlock = block

        prevBlock.addNextFreeList(self.freeListHeader)
        self.freeListHeader.addPrevFreeList(prevBlock)

    def addToFreeListEnd(self, block):
        if(self.freeListHeader == None):
            self.freeListHeader = block
            return
        lastBlock = self.freeListHeader.getPrevFreeList()

        lastBlock.addNextFreeList(block)
        block.addPrevFreeList(lastBlock)

        block.addNextFreeList(self.freeListHeader)
        self.freeListHeader.addPrevFreeList(block)

    def addToFreeListFirst(self, block):
        if(self.freeListHeader == None):
            self.freeListHeader = block
            return
        lastBlock = self.freeListHeader.getPrevFreeList()

        lastBlock.addNextFreeList(block)
        block.addPrevFreeList(lastBlock)

        block.addNextFreeList(self.freeListHeader)
        self.freeListHeader.addPrevFreeList(block)
        # only change in add to first from adding to end as it is a circular Queue
        self.freeListHeader = block

    def removeFromFreeList(self, block):
        # validating if block in free list
        if(block.getPrevFreeList() == None or block.getNextFreeList() == None):
            return -1  # nothing is removed
        # only single element and that is the block that will be removed
        if (self.freeListHeader.getNextFreeList() == self.freeListHeader and self.freeListHeader == block):
            block.removeNextFreeList()
            block.removePrevFreeList()
            self.freeListHeader = None
            return 2  # successfully removed
        # if block to be remove is the header then shift heaader to next place then follow the same cource of action
        elif (self.freeListHeader == block):
            self.freeListHeader = block.getNextFreeList()

        # altering freelist links
        block.getPrevFreeList().addNextFreeList(block.getNextFreeList())
        block.getNextFreeList().addPrevFreeList(block.getPrevFreeList())

        # removing links from present block
        block.removeNextFreeList()
        block.removePrevFreeList()
        return 1

    def printFreeList(self):
        block = self.freeListHeader
        if(block==None):
            print("empty freeList")
        while(block!=None):
            print("<-", block.getBlockNumber(), "->", end="")
            block = block.getNextFreeList()
            if(block == self.freeListHeader):
                break
        print()


# if __name__ == "__main__":
#     fl = FreeList(20)
#     fl.printFreeList()
#     sequence = np.random.permutation(20)
#     for i in range(20):
#         block = fl.freeListHeader
#         while (random.random() <0.4):
#             block = block.getNextFreeList()
#         print("removing:", block.getBlockNumber())
#         fl.removeFromFreeList(block)
#         fl.printFreeList()
    

