# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


class Time60(object):
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    def __str__(self):
        return '%d:%d' % (self.hr, self.min)

    def __add__(self, other):
        return self.__class__(self.hr + other.hr, self.min + other.min)

    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self

    __repr__ = __str__


if __name__ == "__main__":
    mon = Time60(11, 30)
    tue = Time60(10, 14)
    print mon, tue
    tog = mon + tue
    print tog, repr(tog)
