import BufferHeader
import numpy as np
class HashQueue(object):
    def __init__(self,size=4):
        self.size=size
        self.hashQ=np.empty(self.size,dtype=object)
        for i in range(self.size):
            self.hashQ[i]=None
            

    def findBlockInHashQ(self, blockNumber ):
        queue=possibleBlock=self.hashQ[blockNumber%self.size] #possible queue
        while(queue!=None):
            if(possibleBlock.getBlockNumber()==blockNumber):
                return possibleBlock #block is found

            possibleBlock=possibleBlock.getNextHashQ()
            
            if(possibleBlock==queue):
                break

        return None

    def isPresentInHashQ(self,blockNumber):
        if(self.findBlockInHashQ(blockNumber)!=None):
            return True
        return False

    def addBlockToHashQ(self,block):
        queueStart=self.hashQ[block.getBlockNumber() %self.size] #queue to which the block has to be added 
        
        if (queueStart==None):#if queue is empty
            self.hashQ[block.getBlockNumber() %self.size]=block
            block.addNextHashQ(block)
            block.addPrevHashQ(block)
            return 1 ##success
        queueEnd=queueStart.getPrevHashQ()

        queueEnd.addNextHashQ(block)
        block.addPrevHashQ(queueEnd)

        block.addNextHashQ(queueStart)
        queueStart.addPrevHashQ(block)
               
        return 1

    def removeFromHashQ(self,block):

        
        if(block.getNextHashQ()==None and block.getPrevHashQ()==None):#block not in hashQ(starting cases)
            print("line 50 hashq")
            return 1
        if(block.getNextHashQ()==block):#only one element in hashQ
            print("line 53 hashq")
            block.removeNextHashQ()
            block.removePrevHashQ()
            self.hashQ[block.getBlockNumber()%self.size]=None
            return 1
        print ("here")
        if(self.hashQ[block.getBlockNumber()%self.size].getBlockNumber()==block.getBlockNumber()):#when the element to be removed is first element of the queue
            print("removing first element from hashQ")
            self.hashQ[block.getBlockNumber()%self.size]=block.getNextHashQ()
        block.getPrevHashQ().addNextHashQ(block.getNextHashQ())
        block.getNextHashQ().addPrevHashQ(block.getPrevHashQ())


    def printHashQ(self):
        for i in range(self.size):
            block=self.hashQ[i]
            if(block==None):
                print("empty\n")
                continue

            while(True):
                print("<-",block.getBlockNumber(),"->" ,end="")
                block=block.getNextHashQ()
                if(block==self.hashQ[i]):
                    break
            
            print("\n")

#code for block manipulation through this pool
    def 










# if __name__=="__main__":
#     hQ=HashQueue(4)
#     for i in range(20):
#         block=BufferHeader.BufferHeader(i)
#         hQ.addBlockToHashQ(block)
        

#     block=hQ.findBlockInHashQ(19)
#     hQ.removeFromHashQ(block)
#     hQ.removeFromHashQ(hQ.findBlockInHashQ(0))
#     hQ.removeFromHashQ(hQ.findBlockInHashQ(4))
#     hQ.removeFromHashQ(hQ.findBlockInHashQ(8))
#     hQ.removeFromHashQ(hQ.findBlockInHashQ(12))
#     hQ.removeFromHashQ(hQ.findBlockInHashQ(16))
#     block.setBlockNumber(24)
#     hQ.printHashQ()
#     print("end")

#     hQ.addBlockToHashQ(block)

#     hQ.printHashQ()
#     print("end")



    
    


    

        
    