import BufferHeader
import time
import AsynchronousWrite

buffer=BufferHeader.BufferHeader(5)
buffer.setDelayedWriteBit()
AsynchronousWrite.asynchronousWrite(buffer)
print(buffer.isDelayedWrite())
time.sleep(6)
print(buffer.isDelayedWrite())