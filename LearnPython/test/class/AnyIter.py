# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


class AnyIter(object):
    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        return self

    def next(self, howmany=1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval


if __name__ == "__main__":
    # print range(1, 5), range(10), range(1)
    a = AnyIter(range(10))
    i = iter(a)
    for j in range(1, 5):
        print j, ':', i.next(j)