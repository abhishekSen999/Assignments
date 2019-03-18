import os
def parent_child():
    print("prodess id: ",os.getpid())
    pid=os.fork()
    if(pid==0):
        print("parent process id: ",os.getppid())
    

if __name__=="__main__":
    parent_child()