# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


import threading


lock = threading.Lock


def safe_write_file(opened_file, content):
    lock.acquire()
    opened_file.write(content)
    lock.release()
