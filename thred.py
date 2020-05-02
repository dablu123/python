from time import sleep
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Pushpendra")
            sleep(1)

class Dablu(Thread):
    def run(self):
        for i in range(10):
            print("Upadhyay")
            sleep(1)


t1 = Hello()
t2=Dablu()

t1.start()
sleep(.2)
t2.start()

t1.join()
t2.join()

print("Bye")