import multiprocessing
def print_value_1(num):
    n=(num*num*num*num*num*num*num*num*num*num*num*num*num*num*num*num*num*num*num)
    print("value1:",n )

def print_value_2(num):
    print("value2",(num))

if __name__=="__main__":
    p1=multiprocessing.Process(target=print_value_1, args=(10,))
    p2=multiprocessing.Process(target=print_value_2,args=(10,))
    p1.start()
    p2.start()
    p2.join()
    p1.join()
    
    print("done")
    k=input("press enter to exit")


