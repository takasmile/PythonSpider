# multiprocessing首次尝试
import os
from multiprocessing import Process
import time


def run_proc(name):
    print('Child process %s (%s) Running ...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=(str(i), ))
        print('Process will start.')
        time.sleep(1)
        p.start()
    p.join()
    print('Process end.')
