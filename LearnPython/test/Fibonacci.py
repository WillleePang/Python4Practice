# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'



def fab1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a+b
        b = a+b
        n += 1


def fab2(max):
    n, a, b = 0, 0, 1
    l = []
    while n < max:
        l.append(b)
        a, b = b, a+b
        n += 1
    return l


class fab3(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return r
        raise StopIteration()


def fab4(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


BLOCK_SIZE = 1024


def read_file(f_path):
    with open(f_path, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return
