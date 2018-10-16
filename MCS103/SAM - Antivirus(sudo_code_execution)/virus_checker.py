import bufferfile
import convergencefile
def isVirus(path):
    """
    input: path to the file
    output: True if it is a virus, False otherwise
    """
    
    """checks if loops in files are finite or not
       if loop variable converges on the intended value then finite loop
    """
    isFiniteLoop=convergencefile.convergence(path)
    
    """
    checks if buffer Overflow is occuring or not
    """
    hasBufferOverflow=bufferfile.isBufferOverflow(path)
    
    """
    if file contains loops which are not finite or has statements which can cause buffer Overflow then it is a virus
    """
    is_Virus=((not isFiniteLoop) or hasBufferOverflow)
    
    return is_Virus
    
