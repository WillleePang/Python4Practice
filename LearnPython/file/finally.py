# -*- encoding: utf-8 -*-
# Filename: finally.py

__author__ = 'pangwilllee'

import time

try:
    f = file(r'd:\files\poem.txt')
    while True:  # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(0.5)
        print line,
finally:
    f.close()
    print 'Cleaning up...closed the file'