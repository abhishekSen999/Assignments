<center><h1> SIMULATION OF BUFFER MANAGEMENT IN UNIX SYSTEM </center>

<br>

Academic project to implement Getblk and Brelse Algorithms. We are aiming to simulate buffer management in UNIX system.

## Language used : 

 Python

## Installation :
We need to install following things for running the code -
- VSCode 
- Python3
- Windows Subsystem for Linux(WSL) (on Windows system)

## To compile :
In order to compile and run the code follow the given steps -
1. Open VSCode
2. Go to File -> Open Folder -> Select the designated folder
3. Open *DriverProcess.py* and run

## Code structure :
The structure is as follows :
* DriverProcess.py : This is our driver class. It imports *multiprocessing* package provided by python that supports spawning processes. It creates an object of BaseManager class so that the processes can access the shared objects by using proxy classes.

* BufferHeader.py : Defines the buffer header and functions to access and change(only status bits) the block number and status bits. 

* BufferDataStructure.py : Defines the basic structure of the data structures used in buffer cache : freelist and hashqueues. Also provides several functions to manipulate them (add,remove,printe etc)

* myProcess.py : Simulates the functions of the process. Consists of three fuctions :
    1. pseudoOperation() : To simulate various cases like write, I/O error etc randomly.
    2. pseudoBrealse() : Function to release the buffer 
    3. process() : Target function called, when a process is created. Generates request for any block(within the given range;0 - number of blocks) and calls pseudoOperation(). After using the buffer, it releases that.

* BufferManagement.py : It implements getBlk algorithm, to allocate free buffer to the requesting process. 

* AsynchronousWrite.py : Used only in case of 'Delayed write' case. This allows asynchronous write on the disk.


## Code Flow : 
The driver process (DriverProcess.py) creates shared memory(BufferDataStructure). It then creates three processes and starts them. After every 2 seconds, the process requests for the desired block number and getblock is called to allocate that a buffer to the requesting process. As per the scenario, the process either gets a free buffer or sleeps. 