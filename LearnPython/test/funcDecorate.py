# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


# ==================================
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


@makebold
@makeitalic
def say():
    return "Hello"


# ==================================
import time


def foo():
    print 'in foo()'


def timeit(func):
    start = time.clock()
    func()
    end = time.clock()
    print 'used:', end - start


timeit(foo)

# ==================================
from time import ctime, sleep


def tsfunc(func):
    print '[%s] %s()called' % (ctime(), func.__name__)
    return func


@tsfunc
def foo1():
    pass


foo1()