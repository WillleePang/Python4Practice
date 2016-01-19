# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

from random import randint
from operator import add, mul
from functools import partial


def testit(func, *nkwargs, **kwargs):

    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception, diag:
        result = (False, str(diag))
    return result


def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '121.34')

    for eachFunc in funcs:
        print '_' *20
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            if retval[0]:
                print '%s(%s) = True' % (eachFunc.__name__, 'eachVal'), retval[1]
            else:
                print '%s(%s) = Failed' % (eachFunc.__name__, 'eachVal'), retval[1]


def map(func, seq):
    mapped_seq = []
    for eachItem in seq:
        mapped_seq.append(func(eachItem))
    return mapped_seq


if __name__ == '__main__':
    test()
    print [n for n in [randint(1, 99) for i in range(9)] if n % 2]
    print map((lambda x: x+2), [1, 3, 6, 13])
    print reduce(lambda x, y: x+y, [1, 3, 6, 13])

    add1 = partial(add, 1)
    mul1000 = partial(mul, 1000)
    baseTwo = partial(int, base=16)
    print add1(1100), mul1000(1.5), baseTwo('0xac5d')