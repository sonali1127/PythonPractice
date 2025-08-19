import time
# time.time() - Returns the current epoch time (seconds since 1970)
# time.ctime() - Converts the time to a readable format (human-friendly)
# time.sleep(sec) - Pauses the program for the given number of seconds
# time.localtime() - Returns the local time as a struct (can extract hours, minutes, etc.)
# time.strftime(fmt, time.localtime()) - Formats time using a specific pattern (e.g., "HH:MM:SS")
# time.perf_counter() - High-precision timer for measuring performance or time intervals
#(time.time()-time.time())
def uwhile():
    i=0
    while i<=500:
        print(i)
        i=i+1
def ufor():
    for i in range(501):
        print(i)
init=time.perf_counter() 
uwhile()
a=time.perf_counter()
ufor()
print(a)
print(time.perf_counter())