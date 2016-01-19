# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


from random import choice


class RandSeq(object):
    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self

    def next(self):
        return choice(self.data)


if __name__ == "__main__":
    # seq = RandSeq([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    # for i in range(100):
    #     print seq.next(),
    for eachItem in RandSeq(('rock', 'paper', 'scissors')):
        print eachItem
