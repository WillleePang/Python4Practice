# -*- encoding: utf-8 -*-
# Filename:raising.py

__author__ = 'pangwilllee'


class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleatst = atleast

try:
    s = raw_input('Enter something -->　')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)

except EOFError:
    print '\nWhy did you do an EOF on me?'
except ShortInputException, x:
    print 'ShortInputException: The input was of length %d,\
    was excepting at least %d' % (x.length, x.atleatst)
else:
    print 'No exception was raised'
