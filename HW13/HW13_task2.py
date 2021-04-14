# 2. Print current date by using 2 threads.
# #1. Define a subclass using Thread class.
# #2. Instantiate the subclass and trigger the thread.


from threading import Thread
import datetime


class SubThread(Thread):
    def run(self):
        print(f'Current time is {datetime.datetime.now()}, Threads is {self.name}')


sub_1, sub_2 = SubThread(), SubThread()

for i in sub_1, sub_2:
    i.start()
    i.join()
