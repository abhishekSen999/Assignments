import multiprocessing
from multiprocessing.managers import BaseManager
from multiprocessing import Process, Manager

class Child(object):
    def __init__(self):
        self.value=0

    def setValue(self):
        self.value=1

    def flipValue(self):
        self.value=self.value+1

    def getValue(self):
        return self.value
    
class Parent(object):
    def __init__(self):
        self.child=Child()

    def setChild(self):
        self.child.setValue 

    def flipValue(self):
        self.child.flipValue()  
    
    def getValue(self):
        return self.child.getValue()

if __name__=="_-main__":
    BaseManager.register('Parent',Parent)
    BaseManager.register('FreeList',FreeList.FreeList)
    manager=BaseManager()
    manager.start()
