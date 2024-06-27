import time
from contextlib import contextmanager







def generatore():

    yield "A"
    yield "B"
    yield "C"


prova_generatore=generatore()

print(next(prova_generatore))
print(next(prova_generatore))
#next passa all'elemento successivo ogni volta che lo si chiama 
 

@contextmanager
def context_manager_decorator(*args):
    start_time:float=time.time()
    yield
    end_time: float=time.time()
    elapsed_time : float=end_time-start_time
    print(f"Elapsed time: {elapsed_time} seconds")


@context_manager_decorator
def area_cerchio(raggio:float):

    return raggio*raggio*3.14

area_cerchio(1)


###############

import sys


a=[]

b=a

print(sys.getrefcount(a))
# conta quanti riferimenti ci sono per un elemento

threads:list=[]

def thread_function(name):

    print(f"{name} Time -{time.time()}")
    time.sleep(2)
    print(f"{name} Time -{time.time()}")

import threading

for i in range(3):

    x=threading.Thread(target=thread_function, args=(1, ))
    threads.append(x)
    x.start()

for t in threads:

    t.join()

print(f"Prima di thread")
x.start()
print(f"thread partito ")
x.join()
print("thread finito????")


