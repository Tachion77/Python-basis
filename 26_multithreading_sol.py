import time
import threading
from threading import Thread

def sleep(i):
    print("Thread number %i is sleeping" % i)
    time.sleep(5)
    print("Now thread number %i is awake" % i)

for i in range(10):
    th = Thread(target=sleep, args=(i,))
    th.start()
    print("Current threads: %i." % threading.active_count())