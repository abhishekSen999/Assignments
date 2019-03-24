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
        self.child.setValue()

    def flipValue(self):
        self.child.flipValue()  
    
    def getValue(self):
        return self.child.getValue()

    def getChild(self):
        return self.child

class Parent2(object):
    def __init__(self,parent1):
        
        self.child=Child()

    def setChild(self):
        self.child.setValue()

    def flipValue(self):
        self.child.flipValue()  
    
    def getValue(self):
        return self.child.getValue()

def flip(parent,lock):
    #lock.acquire()
    parent.flipValue()
    child=parent.getChild()
    child.flipValue()
    #lock.release()

if __name__=="__main__":
    BaseManager.register('Parent',Parent)
    manager=BaseManager()
    manager.start()
    parent_obj=manager.Parent()
    parent_obj.setChild()
    lock=multiprocessing.Lock()
    print(parent_obj.getValue())
    p1=multiprocessing.Process(target=flip,args=(parent_obj,lock,))
    p2=multiprocessing.Process(target=flip,args=(parent_obj,lock,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(parent_obj.getValue())

