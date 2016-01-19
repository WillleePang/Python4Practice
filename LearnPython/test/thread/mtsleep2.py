# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

import thread
from time import sleep, ctime


loops = [4, 2]


# nloop循环名称，nsec休眠时间，lcok锁
def loop(nloop, nsec, lock):
    print 'start loop', nloop, ' at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()
    lock.release()


def main():
    print 'starting at:', ctime()
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        # 获取相同数量的锁
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        # 创建相同数量的线程
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass
    print 'all DONE at:', ctime()


if __name__ == '__main__':
    main()