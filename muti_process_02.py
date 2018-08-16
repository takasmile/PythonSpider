# multiprocessing Pool类使用
from multiprocessing import Pool
import os
import time
import random


def run_task(name):
    print('Task %s (pid = %s) is running...' % (name, os.getpid()))
    time.sleep(random.random() * 3)
    print('Task %s rnd.' % name)


if __name__ == '__main__':
    print('Current process %s.' % os.getpid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i, ))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done.')