# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


def convert(func, seq):
    'conv. sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]


myseq = [123, 24.3, -123.2e2, 9999999999l]

print convert(int, myseq)
print convert(float, myseq)
print convert(long, myseq)

