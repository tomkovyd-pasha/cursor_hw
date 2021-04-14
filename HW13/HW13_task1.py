# 1. Write the method that return the number of threads currently in execution.
# Also prepare the method that will be executed with threads and run during the first method counting.


from threading import Thread
import threading
import time
import datetime
import time
import concurrent.futures
import multiprocessing


def method_1():
    a = [x ** 2 if x >= 20000 else x ** 3 for x in range(10000000) if x % 2 == 0]
    return a


start_time = time.time()
method_1()
print(f'Count of threads - {threading.active_count()}')
print(f'Execution time - {round(time.time() - start_time, 4)}')
