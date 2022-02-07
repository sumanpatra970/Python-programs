from threading import Thread
from time import sleep
class hii(Thread):
    def run(self):
        for i in range(1,5):
            sleep(1)
            print("hii")
class hello(Thread):
    def run(self):
        for i in range(1,5):
            sleep(1)
            print("hello")

t1=hii()
t2=hello()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("bye")
print(__name__)